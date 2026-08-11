"""HTML-diff adapter — press listings without RSS (plan Phase 4.3).

The discussion-draft catcher — the GAAIA failure mode lives here. Adapter stays
stateless: returns ALL current entries and lets the state layer decide novelty.

Selector drift tripwire: a page that previously had entries and now yields zero
matches raises SourceError, so silence is never indistinguishable from a quiet week.
"""

from __future__ import annotations

import re
from collections.abc import Iterable
from datetime import datetime
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from watcher.models import Item, SourceError, make_hash_uid

# %m/%d/%Y covers Blackburn's "08/5/2026" (strptime accepts non-zero-padded fields);
# %m.%d.%Y covers the Senate PageList CMS's "08.10.2026" (Cruz, Rounds, Peters-MI)
DATE_FORMATS = ("%B %d, %Y", "%b %d, %Y", "%Y-%m-%d", "%m/%d/%Y", "%m.%d.%Y")

# Warner (WP/Elementor) renders "August 7th, 2026" — strip ordinal suffixes
_ORDINAL_RE = re.compile(r"(\d{1,2})(st|nd|rd|th)\b")


def _iso_date(raw: str) -> str:
    text = _ORDINAL_RE.sub(r"\1", (raw or "").strip())
    for fmt in DATE_FORMATS:
        try:
            # date-only parse — timezone is irrelevant
            return datetime.strptime(text, fmt).date().isoformat()  # noqa: DTZ007
        except ValueError:
            continue
    raise SourceError(f"could not parse date {raw!r}")


def _pick_url(entry, link_selector: str, base_url: str) -> str:
    node = entry.select_one(link_selector)
    if node is None:
        raise SourceError(f"link selector {link_selector!r} missed entry")
    href = (node.get("href") or "").strip()
    if not href:
        raise SourceError("empty href on entry link")
    return urljoin(base_url + "/" if not base_url.endswith("/") else base_url, href)


def _pick_text(entry, selector: str, field_label: str) -> str:
    node = entry.select_one(selector)
    if node is None:
        raise SourceError(f"{field_label} selector {selector!r} missed entry")
    return node.get_text(strip=True)


def _extract(
    html: str,
    selectors: dict,
    *,
    source_id: str,
    chamber: str,
    base_url: str,
    kind: str,
) -> list[Item]:
    soup = BeautifulSoup(html, "html.parser")
    entries: Iterable = soup.select(selectors["entry"])
    entries = list(entries)
    if not entries:
        raise SourceError(
            f"{source_id}: entry selector {selectors['entry']!r} matched zero rows "
            "(selector drift, not a quiet week)"
        )

    items: list[Item] = []
    for entry in entries:
        title = _pick_text(entry, selectors["title"], "title")
        url = _pick_url(entry, selectors["link"], base_url)
        iso_date = _iso_date(_pick_text(entry, selectors["date"], "date"))
        items.append(Item(
            uid=make_hash_uid(url, title),
            source=source_id,
            chamber=chamber,
            kind=kind,
            title=title,
            url=url,
            date=iso_date,
        ))
    return items


def extract_entries(
    html: str, selectors: dict, *, source_id: str, chamber: str, base_url: str
) -> list[Item]:
    return _extract(html, selectors, source_id=source_id, chamber=chamber,
                    base_url=base_url, kind="press")
