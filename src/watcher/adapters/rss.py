"""RSS adapter — committee/member press feeds (plan Phase 4.2).

feedparser handles the schema drift RSS has accumulated. Missing pubDate falls back
to today but is flagged in the excerpt so silent date-drift never masquerades as
"published today." Empty parse → SourceError (a live press feed always has entries).
"""

from __future__ import annotations

from datetime import date, datetime

import feedparser

from watcher.models import Item, SourceError, make_hash_uid


def _entry_date(entry, today: str) -> tuple[str, bool]:
    parsed = entry.get("published_parsed") or entry.get("updated_parsed")
    if parsed:
        try:
            return date(*parsed[:3]).isoformat(), False
        except (TypeError, ValueError):
            pass
    return today, True


def parse_feed(raw: bytes | str, *, source_id: str, chamber: str, today: str) -> list[Item]:
    # sanity-check today is well-formed early — fail loud before catching junk feeds
    datetime.strptime(today, "%Y-%m-%d")

    feed = feedparser.parse(raw)
    entries = feed.get("entries") or []
    if not entries:
        raise SourceError(f"{source_id}: feed parsed to zero entries")

    items: list[Item] = []
    for entry in entries:
        title = (entry.get("title") or "").strip()
        url = (entry.get("link") or "").strip()
        description = (entry.get("summary") or entry.get("description") or "").strip()
        iso_date, was_fallback = _entry_date(entry, today)
        excerpt = f"{description} [pubdate missing]" if was_fallback else description
        items.append(Item(
            uid=make_hash_uid(url, title),
            source=source_id,
            chamber=chamber,
            kind="press",
            title=title,
            url=url,
            date=iso_date,
            body_excerpt=excerpt,
        ))
    return items
