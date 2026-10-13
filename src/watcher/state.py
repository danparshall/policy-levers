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
import logging
from dataclasses import dataclass, field
from datetime import UTC, date, datetime
from pathlib import Path
from typing import TYPE_CHECKING

from watcher.fileio import atomic_write_text

if TYPE_CHECKING:
    from watcher.models import Item

log = logging.getLogger(__name__)

SCHEMA_VERSION = 1

# Per-source cap on remembered uids. The poller returns up to 250 bills per fetch
# and a press listing shows ~10-20 rows, so a few thousand covers many months of
# daily runs; least-recently-seen uids are evicted first, and a uid that is still
# on the page is refreshed every run, so long-lived rows never age out.
MAX_SEEN_UIDS = 5000


@dataclass
class _SourceState:
    seeded: bool = False
    # Ordered oldest -> most recently seen (dict used as an insertion-ordered set).
    seen_uids: dict[str, None] = field(default_factory=dict)
    consecutive_failures: int = 0


@dataclass
class State:
    per_source: dict[str, _SourceState] = field(default_factory=dict)
    max_seen_uids: int = MAX_SEEN_UIDS

    @classmethod
    def load(cls, path: str | Path, *, max_seen_uids: int = MAX_SEEN_UIDS) -> State:
        """Load from disk; a missing file is a fresh baseline.

        A corrupt file (truncated JSON, wrong top-level shape) is moved aside to
        `<name>.corrupt-<UTC timestamp>` and treated as fresh: an unattended cron
        keeps running and the evidence is preserved for inspection. Cost of the
        reset is one baseline run (backlog-window items re-surface once).
        """
        p = Path(path)
        if not p.exists():
            return cls(max_seen_uids=max_seen_uids)
        problem: str | None = None
        try:
            doc = json.loads(p.read_text())
        except ValueError as exc:
            problem = str(exc)
        else:
            if not isinstance(doc, dict):
                problem = f"top-level JSON is {type(doc).__name__}, expected object"
        if problem is not None:
            stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%S")
            quarantine = p.with_name(f"{p.name}.corrupt-{stamp}")
            p.replace(quarantine)
            log.warning(
                "state file %s is corrupt (%s); moved to %s, starting fresh", p, problem, quarantine
            )
            return cls(max_seen_uids=max_seen_uids)
        st = cls(max_seen_uids=max_seen_uids)
        for source_id, blob in (doc.get("sources") or {}).items():
            st.per_source[source_id] = _SourceState(
                seeded=bool(blob.get("seeded", False)),
                seen_uids=dict.fromkeys(blob.get("seen_uids", [])),
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
            # Re-insert so a uid still present on the page moves to the "recent" end.
            s.seen_uids.pop(it.uid, None)
            s.seen_uids[it.uid] = None
        overflow = len(s.seen_uids) - self.max_seen_uids
        for uid in list(s.seen_uids)[:overflow] if overflow > 0 else ():
            del s.seen_uids[uid]

    def record_failure(self, source_id: str) -> int:
        s = self._get(source_id)
        s.consecutive_failures += 1
        return s.consecutive_failures

    def consecutive_failures(self, source_id: str) -> int:
        s = self.per_source.get(source_id)
        return 0 if s is None else s.consecutive_failures

    def save(self, path: str | Path) -> None:
        doc = {
            "schema_version": SCHEMA_VERSION,
            "sources": {
                sid: {
                    "seeded": s.seeded,
                    # oldest -> newest; order is what makes the cap an LRU on reload
                    "seen_uids": list(s.seen_uids),
                    "consecutive_failures": s.consecutive_failures,
                }
                for sid, s in self.per_source.items()
            },
        }
        atomic_write_text(path, json.dumps(doc, indent=2, sort_keys=True))
