"""structured adapter: docs.house.gov meeting feeds + floor lookaheads (plan Phase 4.4).

docshouse_sy00_live.xml is a REAL capture (2026-08-04) — the schema authority.
The event date must come from the 'Meeting Date:' text in the description, NOT the
item pubDate (pubDate is publication time; advance notice lives in the difference).
"""

import pytest

from tests.conftest import load_fixture
from watcher.adapters.structured import parse_floor_lookahead, parse_meeting_feed
from watcher.models import SourceError


def meeting_items():
    return parse_meeting_feed(
        load_fixture("docshouse_sy00_live.xml"), source_id="docs-house-sy00", chamber="house"
    )


def test_markup_titles_get_markup_kind():
    markup = next(i for i in meeting_items() if "Markup" in i.title)
    assert markup.kind == "markup"


def test_hearings_get_hearing_kind():
    hearing = next(i for i in meeting_items() if "Golden Age" in i.title)
    assert hearing.kind == "hearing"


def test_event_date_parsed_from_description_not_pubdate():
    markup = next(i for i in meeting_items() if "Markup" in i.title)
    assert markup.date == "2026-07-21"  # "Meeting Date: Tuesday, July 21, 2026 10:00 AM"


def test_uid_derived_from_event_guid():
    markup = next(i for i in meeting_items() if "Markup" in i.title)
    assert "119493" in markup.uid


def test_committee_name_lands_in_body_excerpt():
    items = meeting_items()
    assert any("Science, Space, and Technology" in i.body_excerpt for i in items)


def test_malformed_meeting_feed_raises_source_error():
    with pytest.raises(SourceError):
        parse_meeting_feed(
            b"<html>not the meeting feed</html>", source_id="docs-house-sy00", chamber="house"
        )


def _meeting_feed(*items_xml: str) -> bytes:
    body = "".join(items_xml)
    return (
        f'<?xml version="1.0"?><rss version="2.0"><channel><title>t</title>{body}</channel></rss>'
    ).encode()


def _meeting_item(guid: str, title: str, description: str) -> str:
    return (
        f"<item><title>{title}</title><link>https://docs.house.gov/{guid}</link>"
        f"<guid>{guid}</guid><description>{description}</description></item>"
    )


def test_one_bad_meeting_entry_is_skipped_and_the_rest_still_surface():
    """Issue #9: one entry without a parseable 'Meeting Date:' must not fail the
    whole feed — skip it, keep the other events."""
    raw = _meeting_feed(
        _meeting_item(
            "1", "Markup of H.R. 1", "Committee on X Meeting Date: Tuesday, July 21, 2026"
        ),
        _meeting_item("2", "Hearing: broken", "Committee on X (date TBD)"),
        _meeting_item("3", "Hearing: AI", "Committee on X Meeting Date: Friday, July 24, 2026"),
    )
    items = parse_meeting_feed(raw, source_id="docs-house-sy00", chamber="house")
    assert [i.date for i in items] == ["2026-07-21", "2026-07-24"]


def test_every_meeting_entry_bad_raises_source_error():
    """Skipping must not degrade into silence: if NO entry parses, that's drift."""
    raw = _meeting_feed(
        _meeting_item("1", "A", "no date here"),
        _meeting_item("2", "B", "none here either"),
    )
    with pytest.raises(SourceError):
        parse_meeting_feed(raw, source_id="docs-house-sy00", chamber="house")


def test_empty_stub_items_are_skipped():
    """docs.house.gov emits placeholder <item> stubs with guid=0 and empty
    title/description. Real bug hit on the 2026-08-04 smoke run: the adapter
    was raising SourceError on the empty description instead of skipping.
    The stub is a docs.house.gov quirk, not a parse failure."""
    items = meeting_items()
    # Fixture: 2 real items + 1 empty stub → 2 real items produced.
    assert len(items) == 2
    assert all(i.title for i in items)


def test_floor_lookahead_entries_become_floor_items():
    items = parse_floor_lookahead(
        load_fixture("floor_lookahead.html").decode(),
        selectors={"entry": "li.floor-item", "title": "a", "link": "a", "date": "span.floor-date"},
        source_id="house-floor",
        chamber="house",
        base_url="https://www.majorityleader.gov",
    )
    assert len(items) == 2
    hr9363 = next(i for i in items if "9363" in i.title)
    assert hr9363.kind == "floor"
    assert hr9363.date == "2026-06-24"


def test_senate_schedule_real_page_next_meeting_becomes_floor_item():
    """Real capture of senate.gov/legislative/schedule/floor_schedule.htm (2026-08-11).

    Entry selector targets #proceedings_schedule only — the second <article> is
    'Previous Meeting' (heading is not a date) and must NOT be picked up. Dates
    carry a weekday prefix ('Thursday, Aug 13, 2026')."""
    items = parse_floor_lookahead(
        load_fixture("senate-daily-schedule.html").decode(),
        selectors={
            "entry": "article#proceedings_schedule",
            "title": "span.floor-schedule",
            "link": "a",
            "date": "h3",
        },
        source_id="senate-daily-schedule",
        chamber="senate",
        base_url="https://www.senate.gov/legislative/schedule/floor_schedule.htm",
    )
    assert len(items) == 1
    nxt = items[0]
    assert nxt.kind == "floor"
    assert nxt.chamber == "senate"
    assert nxt.date == "2026-08-13"
    assert "pro forma session" in nxt.title
    assert nxt.url == "https://www.senate.gov/legislative/floor_activity_pail.htm"
