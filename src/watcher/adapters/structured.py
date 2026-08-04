"""structured adapter — docs.house.gov meeting feeds + Majority Leader floor lookahead
(plan Phase 4.4).

Meeting feeds are pseudo-RSS with the actual event date buried in the description
(pubDate is publication time; advance notice lives in the difference). Uids come
from the feed's guid/EventID, so title edits between publications don't re-surface
the same meeting as "new."

Floor lookaheads reuse the html_diff extraction path but tag entries as `floor`.
"""

from __future__ import annotations

import re
from datetime import datetime

import feedparser
from bs4 import BeautifulSoup

from watcher.adapters.html_diff import _extract
from watcher.models import Item, SourceError

_MEETING_DATE_RE = re.compile(
    r"Meeting Date:\s*[A-Za-z]+,\s*([A-Za-z]+\s+\d{1,2},\s+\d{4})"
)


def _description_text(entry) -> str:
    raw = entry.get("summary") or entry.get("description") or ""
    # feedparser decodes the HTML entities; BS strips the residual tags for us.
    return BeautifulSoup(raw, "html.parser").get_text(" ", strip=True)


def _guid(entry) -> str:
    guid = entry.get("id") or entry.get("guid") or ""
    if not guid:
        raise SourceError(f"meeting item missing guid: {entry.get('title')!r}")
    return str(guid).strip()


def _event_date(description: str) -> str:
    m = _MEETING_DATE_RE.search(description)
    if not m:
        raise SourceError(f"could not find 'Meeting Date:' in description: {description[:120]!r}")
    # date-only parse — timezone is irrelevant
    return datetime.strptime(m.group(1), "%B %d, %Y").date().isoformat()  # noqa: DTZ007


def _committee_line(description: str) -> str:
    # Description shape: "Committee on X  Meeting Date: <weekday>, ..."
    idx = description.find("Meeting Date:")
    committee = description[:idx].strip() if idx > 0 else description
    return committee.rstrip(":").strip()


def _kind(title: str) -> str:
    return "markup" if "Markup" in title else "hearing"


def parse_meeting_feed(raw: bytes | str, *, source_id: str, chamber: str) -> list[Item]:
    feed = feedparser.parse(raw)
    entries = feed.get("entries") or []
    if not entries:
        raise SourceError(f"{source_id}: meeting feed parsed to zero entries")

    items: list[Item] = []
    for entry in entries:
        title = (entry.get("title") or "").strip()
        url = (entry.get("link") or "").strip()
        description = _description_text(entry)
        committee = _committee_line(description)
        guid = _guid(entry)
        items.append(Item(
            uid=f"{source_id}-{guid}",
            source=source_id,
            chamber=chamber,
            kind=_kind(title),
            title=title,
            url=url,
            date=_event_date(description),
            body_excerpt=committee,
        ))
    return items


def parse_floor_lookahead(
    html: str, *, selectors: dict, source_id: str, chamber: str, base_url: str
) -> list[Item]:
    return _extract(html, selectors, source_id=source_id, chamber=chamber,
                    base_url=base_url, kind="floor")
