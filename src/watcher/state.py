"""Per-source state store: seen-UIDs + consecutive-failure counters (plan Phase 2).

Design invariants:
- `new_items` is a pure filter (no persistence side effects).
- `record_success` / `record_failure` mutate in-memory only.
- `save` is atomic (temp + rename) and is only called by the orchestrator AFTER the
  digest is written — so a crash mid-digest re-surfaces items instead of losing them.

Simplified 2026-08-04 per the plan: no page snapshots. UID dedupe is the novelty
mechanism; zero-entries-from-a-nonempty-source is the selector-drift tripwire
inside the adapters (SourceError), not something the state layer detects.
"""

from __future__ import annotations

import json
import os
import tempfile
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from watcher.models import Item

SCHEMA_VERSION = 1


@dataclass
class _SourceState:
    seeded: bool = False
    seen_uids: set[str] = field(default_factory=set)
    consecutive_failures: int = 0


@dataclass
class State:
    per_source: dict[str, _SourceState] = field(default_factory=dict)

    @classmethod
    def load(cls, path: str | Path) -> State:
        p = Path(path)
        if not p.exists():
            return cls()
        doc = json.loads(p.read_text())
        st = cls()
        for source_id, blob in (doc.get("sources") or {}).items():
            st.per_source[source_id] = _SourceState(
                seeded=bool(blob.get("seeded", False)),
                seen_uids=set(blob.get("seen_uids", [])),
                consecutive_failures=int(blob.get("consecutive_failures", 0)),
            )
        return st

    @classmethod
    def load_fresh(cls) -> State:
        return cls()

    def _get(self, source_id: str) -> _SourceState:
        return self.per_source.setdefault(source_id, _SourceState())

    def is_baseline(self, source_id: str) -> bool:
        s = self.per_source.get(source_id)
        return s is None or not s.seeded

    def new_items(
        self,
        source_id: str,
        items: list[Item],
        today: str,
        include_backlog_days: int | None = None,
    ) -> list[Item]:
        """Return items the digest should treat as new. Pure — no state mutation.

        Baseline (source never recorded): return backlog window items only, or [] if
        no backlog is requested.
        Established: return items whose UID is not in this source's seen_uids.
        """
        if self.is_baseline(source_id):
            if not include_backlog_days:
                return []
            today_d = date.fromisoformat(today)
            cutoff = today_d.toordinal() - include_backlog_days
            return [it for it in items if date.fromisoformat(it.date).toordinal() >= cutoff]
        seen = self._get(source_id).seen_uids
        return [it for it in items if it.uid not in seen]

    def record_success(self, source_id: str, items: list[Item]) -> None:
        """Mark the fetch as successful: seed the source, learn every uid, reset failures."""
        s = self._get(source_id)
        s.seeded = True
        s.consecutive_failures = 0
        for it in items:
            s.seen_uids.add(it.uid)

    def record_failure(self, source_id: str) -> int:
        s = self._get(source_id)
        s.consecutive_failures += 1
        return s.consecutive_failures

    def consecutive_failures(self, source_id: str) -> int:
        s = self.per_source.get(source_id)
        return 0 if s is None else s.consecutive_failures

    def save(self, path: str | Path) -> None:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        doc = {
            "schema_version": SCHEMA_VERSION,
            "sources": {
                sid: {
                    "seeded": s.seeded,
                    "seen_uids": sorted(s.seen_uids),
                    "consecutive_failures": s.consecutive_failures,
                }
                for sid, s in self.per_source.items()
            },
        }
        # atomic write: temp file in the same directory + os.replace
        with tempfile.NamedTemporaryFile(
            mode="w", dir=p.parent, prefix=".state-", suffix=".tmp", delete=False
        ) as tf:
            json.dump(doc, tf, indent=2, sort_keys=True)
            tmp_path = tf.name
        os.replace(tmp_path, p)
