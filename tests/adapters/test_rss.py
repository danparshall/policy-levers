"""RSS adapter: committee/member press feeds → press Items (plan Phase 4.2)."""

import pytest
from watcher.adapters.rss import parse_feed
from watcher.models import SourceError

from tests.conftest import load_fixture


def test_feed_entries_become_press_items():
    items = parse_feed(load_fixture("committee_rss.xml"), source_id="example-committee",
                       chamber="senate", today="2026-08-04")
    assert len(items) == 2
    first = items[0]
    assert first.kind == "press"
    assert first.chamber == "senate"
    assert first.title == "Chair Announces Hearing on Artificial Intelligence Oversight"
    assert first.date == "2026-07-28"
    assert first.url == "https://example.senate.gov/newsroom/press/ai-oversight-hearing"


def test_description_feeds_body_excerpt():
    items = parse_feed(load_fixture("committee_rss.xml"), source_id="example-committee",
                       chamber="senate", today="2026-08-04")
    assert "compute thresholds" in items[0].body_excerpt


def test_missing_pubdate_falls_back_to_today_and_flags_it():
    items = parse_feed(load_fixture("committee_rss.xml"), source_id="example-committee",
                       chamber="senate", today="2026-08-04")
    undated = next(i for i in items if "Nominations" in i.title)
    assert undated.date == "2026-08-04"
    assert "pubdate" in undated.body_excerpt.lower()  # fallback must be visible, not silent


def test_unparseable_or_empty_feed_raises_source_error():
    """Feed-drift tripwire: a press feed always has entries; zero parsed entries means
    the feed moved or broke — silence must not masquerade as a quiet week."""
    with pytest.raises(SourceError):
        parse_feed(b"<html>this is not a feed</html>", source_id="example-committee",
                   chamber="senate", today="2026-08-04")


def test_uids_stable_across_reparse():
    a = parse_feed(load_fixture("committee_rss.xml"), source_id="x", chamber="senate",
                   today="2026-08-04")
    b = parse_feed(load_fixture("committee_rss.xml"), source_id="x", chamber="senate",
                   today="2026-08-05")  # different day, same content
    assert [i.uid for i in a] == [i.uid for i in b]
