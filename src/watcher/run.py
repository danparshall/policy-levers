"""Orchestrator: fetch → triage → digest → state save (plan Phase 6).

Failure isolation: a source that raises SourceError degrades the digest (its failure
count ticks up) but never kills the run. Loss-proof ordering: state save happens
AFTER the digest is written on disk, so a crash mid-digest re-surfaces the items
on the next run rather than silently losing them.

`run_watcher` accepts a list of Source protocol objects (anything with `.id` and
`.fetch() -> list[Item]`); real Sources are wired up in Phase 8 by pairing an
adapter parse function with a fetch helper.
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from watcher.digest import render, write_digest
from watcher.models import SourceError
from watcher.scoring import triage
from watcher.state import State

if TYPE_CHECKING:
    from watcher.config import Keywords


def _digest_filename(today: str) -> str:
    return today.replace("-", "") + ".md"


def run_watcher(
    *,
    sources: list,
    state_path: str | Path,
    digest_dir: str | Path,
    keywords: Keywords,
    today: str,
    include_backlog_days: int = 30,
) -> Path:
    state = State.load(state_path)

    good_fetches: list[tuple[object, list]] = []
    health: list[tuple[str, int]] = []
    all_new: list = []

    for source in sources:
        if not getattr(source, "enabled", True):
            continue
        try:
            items = source.fetch()
        except SourceError:
            failures = state.record_failure(source.id)
            health.append((source.id, failures))
            continue
        good_fetches.append((source, items))
        all_new.extend(state.new_items(
            source.id, items, today=today, include_backlog_days=include_backlog_days,
        ))

    triaged = triage(all_new, keywords)

    text = render(
        date=today,
        pinned=triaged.pinned,
        scored=triaged.listed,
        health=health,
        suppressed_count=triaged.suppressed_count,
    )

    digest_dir = Path(digest_dir)
    digest_dir.mkdir(parents=True, exist_ok=True)
    digest_path = digest_dir / _digest_filename(today)

    has_new_content = bool(triaged.pinned or triaged.listed or health)
    if has_new_content or not digest_path.exists():
        write_digest(digest_path, text)

    # State save is intentionally LAST — a crash in write_digest above must leave
    # state untouched so the items re-surface on the next run.
    for source, items in good_fetches:
        state.record_success(source.id, items)
    state.save(state_path)

    return digest_path


def main() -> None:  # pragma: no cover — CLI entry, Phase 8 wires the real sources
    raise NotImplementedError(
        "Live source wiring lands in Phase 8; the tests here use fake sources."
    )
