"""HTML-diff adapter — press listings without RSS (plan Phase 4.3).

The discussion-draft catcher — the GAAIA failure mode lives here. Adapter stays
stateless: returns ALL current entries and lets the state layer decide novelty.

Selector drift tripwire: a page that previously had entries and now yields zero
matches raises SourceError, so silence is never indistinguishable from a quiet week.
"""

from __future__ import annotations

import logging
import re
from datetime import datetime
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from watcher.models import Item, SourceError, make_hash_uid

log = logging.getLogger(__name__)

REQUIRED_SELECTORS = ("entry", "title", "link", "date")

# %m/%d/%Y covers Blackburn's "08/5/2026" (strptime accepts non-zero-padded fields);
# %m.%d.%Y covers the Senate PageList CMS's "08.10.2026" (Cruz, Rounds, Peters-MI);
# the %A-prefixed pair covers senate.gov's floor schedule ("Thursday, Aug 13, 2026")
DATE_FORMATS = (
    "%B %d, %Y",
    "%b %d, %Y",
    "%Y-%m-%d",
    "%m/%d/%Y",
    "%m.%d.%Y",
    "%A, %b %d, %Y",
    "%A, %B %d, %Y",
)

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
    # urljoin treats the last path segment of a base without a trailing slash as a
    # file and replaces it ("/media/press-releases" + "item" -> "/media/item").
    # The listing URL is a directory for our purposes, so force the trailing slash.
    base_dir = base_url if base_url.endswith("/") else base_url + "/"
    return urljoin(base_dir, href)


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
    missing = [key for key in REQUIRED_SELECTORS if not selectors.get(key)]
    if missing:
        raise SourceError(f"{source_id}: selectors config missing {missing!r}")

    soup = BeautifulSoup(html, "html.parser")
    entries = list(soup.select(selectors["entry"]))
    if not entries:
        raise SourceError(
            f"{source_id}: entry selector {selectors['entry']!r} matched zero rows "
            "(selector drift, not a quiet week)"
        )

    # Per-entry failures are isolated: one odd row (a dateless pinned post, a CMS
    # hiccup) must not drop the other N-1 entries from an unattended run. Only
    # every-entry-failed is treated as drift.
    items: list[Item] = []
    errors: list[str] = []
    for entry in entries:
        try:
            title = _pick_text(entry, selectors["title"], "title")
            url = _pick_url(entry, selectors["link"], base_url)
            iso_date = _iso_date(_pick_text(entry, selectors["date"], "date"))
        except SourceError as exc:
            errors.append(str(exc))
            log.warning("%s: skipping entry (%s)", source_id, exc)
            continue
        items.append(
            Item(
                uid=make_hash_uid(url, title),
                source=source_id,
                chamber=chamber,
                kind=kind,
                title=title,
                url=url,
                date=iso_date,
            )
        )
    if not items:
        raise SourceError(
            f"{source_id}: all {len(entries)} entries failed to parse (first: {errors[0]})"
        )
    return items


def extract_entries(
    html: str, selectors: dict, *, source_id: str, chamber: str, base_url: str
) -> list[Item]:
    return _extract(
        html, selectors, source_id=source_id, chamber=chamber, base_url=base_url, kind="press"
    )
