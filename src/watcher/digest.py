"""Daily digest rendering + on-disk writing (plan Phase 5).

Sections in fixed order (each omitted if empty):
1. Tracked bills — pinned items, event-date ascending
2. Time-critical — markup/hearing/floor items in scored, soonest event first
3. New & notable — everything else in scored, score descending
4. Source health — sources with consecutive failures (STALE at 3+)

Then a "N items suppressed below threshold." footer so silence is distinguishable
from a broken run.

`render` is a pure function of its inputs — no wall-clock reads, no now-timestamps
in the body. `write_digest` appends a "Later run" section rather than overwriting,
so re-invocations same-day don't clobber the morning's alarm log.
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from watcher.models import Item

EVENT_KINDS = {"markup", "hearing", "floor"}
STALE_THRESHOLD = 3


def _format_item(item: Item, score: int | None) -> str:
    prefix = "" if score is None else f"[{score}] "
    return f"- {prefix}{item.date} · {item.source} · {item.title} ({item.url})"


def _health_line(source_id: str, failures: int) -> str:
    if failures >= STALE_THRESHOLD:
        return f"- STALE — {source_id}: {failures} consecutive failures"
    return f"- {source_id}: {failures} consecutive failure(s)"


def render(
    *,
    date: str,
    pinned: list[Item],
    scored: list[tuple[Item, int]],
    health: list[tuple[str, int]],
    suppressed_count: int,
) -> str:
    lines: list[str] = [f"# Legislative digest — {date}", ""]

    if pinned:
        lines.append("## Tracked bills")
        lines.append("")
        for item in sorted(pinned, key=lambda i: i.date):
            lines.append(_format_item(item, score=None))
        lines.append("")

    time_critical = [(i, s) for i, s in scored if i.kind in EVENT_KINDS]
    other = [(i, s) for i, s in scored if i.kind not in EVENT_KINDS]

    if time_critical:
        time_critical.sort(key=lambda pair: pair[0].date)
        lines.append("## Time-critical")
        lines.append("")
        for item, score in time_critical:
            lines.append(_format_item(item, score=score))
        lines.append("")

    if other:
        other.sort(key=lambda pair: pair[1], reverse=True)
        lines.append("## New & notable")
        lines.append("")
        for item, score in other:
            lines.append(_format_item(item, score=score))
        lines.append("")

    if health:
        lines.append("## Source health")
        lines.append("")
        for source_id, failures in sorted(health, key=lambda pair: (-pair[1], pair[0])):
            lines.append(_health_line(source_id, failures))
        lines.append("")

    lines.append(f"_{suppressed_count} items suppressed below threshold._")
    return "\n".join(lines) + "\n"


LATER_RUN_MARKER = "\n\n## Later run\n\n"


def write_digest(path: str | Path, text: str) -> None:
    p = Path(path)
    if p.exists():
        p.write_text(p.read_text() + LATER_RUN_MARKER + text)
        return
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
