"""structured adapter: docs.house.gov meeting feeds + floor lookaheads (plan Phase 4.4).

docshouse_sy00_live.xml is a REAL capture (2026-08-04) — the schema authority.
The event date must come from the 'Meeting Date:' text in the description, NOT the
item pubDate (pubDate is publication time; advance notice lives in the difference).
"""

import pytest
from watcher.adapters.structured import parse_floor_lookahead, parse_meeting_feed
from watcher.models import SourceError

from tests.conftest import load_fixture


def meeting_items():
    return parse_meeting_feed(load_fixture("docshouse_sy00_live.xml"),
                              source_id="docs-house-sy00", chamber="house")


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
        parse_meeting_feed(b"<html>not the meeting feed</html>",
                           source_id="docs-house-sy00", chamber="house")


def test_floor_lookahead_entries_become_floor_items():
    items = parse_floor_lookahead(
        load_fixture("floor_lookahead.html").decode(),
        selectors={"entry": "li.floor-item", "title": "a", "link": "a", "date": "span.floor-date"},
        source_id="house-floor", chamber="house",
        base_url="https://www.majorityleader.gov",
    )
    assert len(items) == 2
    hr9363 = next(i for i in items if "9363" in i.title)
    assert hr9363.kind == "floor"
    assert hr9363.date == "2026-06-24"
