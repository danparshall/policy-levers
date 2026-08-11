"""RSS adapter: committee/member press feeds → press Items (plan Phase 4.2)."""

import pytest

from tests.conftest import load_fixture
from watcher.adapters.rss import parse_feed
from watcher.models import SourceError


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


def test_trahan_real_feed_normalizes_to_press_items():
    """Real capture of trahan.house.gov/news/rss.aspx (2026-08-11) — the GAAIA-catcher.

    Fireside/ASP.NET CMS feed: escaped-HTML descriptions, DocumentID links, GMT pubDates.
    """
    items = parse_feed(load_fixture("rep-trahan-press.xml"), source_id="rep-trahan-press",
                       chamber="house", today="2026-08-11")
    assert len(items) == 2
    coalition, intro = items
    assert coalition.kind == "press"
    assert coalition.chamber == "house"
    assert coalition.title == "What They’re Saying: Broad Coalition Lauds Bipartisan FRONTIER Act"
    assert coalition.date == "2026-07-28"
    assert coalition.url == "http://trahan.house.gov/news/documentsingle.aspx?DocumentID=3825"
    assert "FRONTIER" in coalition.body_excerpt
    assert intro.date == "2026-07-23"
    assert intro.url == "http://trahan.house.gov/news/documentsingle.aspx?DocumentID=3823"
    assert "risk-based framework" in intro.body_excerpt


def test_franklin_real_feed_normalizes_to_press_items():
    """Real capture of franklin.house.gov/news/rss.aspx (2026-08-11) — Fireside CMS,
    same shape as Trahan; FRONTIER cosponsor release workflow."""
    items = parse_feed(load_fixture("rep-franklin-press.xml"), source_id="rep-franklin-press",
                       chamber="house", today="2026-08-11")
    assert len(items) == 2
    first, second = items
    assert first.kind == "press"
    assert first.chamber == "house"
    assert first.date == "2026-07-27"
    assert first.title == (
        "Obernolte, Franklin offer bipartisan bill to set national rules for advanced AI"
    )
    assert first.url == "http://franklin.house.gov/news/documentsingle.aspx?DocumentID=1923"
    assert second.date == "2026-07-23"
    assert "Frontier Act" in second.title


def test_hawley_real_feed_normalizes_to_press_items():
    """Real capture of hawley.senate.gov/rss/ (2026-08-11) — WordPress feed,
    slug-URL links, content:encoded stripped in fixture."""
    items = parse_feed(load_fixture("sen-hawley-press.xml"), source_id="sen-hawley-press",
                       chamber="senate", today="2026-08-11")
    assert len(items) == 2
    first = items[0]
    assert first.kind == "press"
    assert first.chamber == "senate"
    assert first.date == "2026-08-06"
    assert first.url.startswith("https://www.hawley.senate.gov/hawley-banks-tuberville")
    assert "WASHINGTON" in first.body_excerpt


def test_schumer_caucus_real_feed_normalizes_to_press_items():
    """Real capture of democrats.senate.gov/feed/ (2026-08-11) — Senate Dem caucus
    WordPress feed; carries floor wrap-ups and schedule notices (the floor signal)."""
    items = parse_feed(load_fixture("sen-schumer-press.xml"), source_id="sen-schumer-press",
                       chamber="senate", today="2026-08-11")
    assert len(items) == 2
    first, second = items
    assert first.kind == "press"
    assert first.chamber == "senate"
    assert first.date == "2026-08-08"
    assert first.title == "Wrap Up for Friday, August 7 and Saturday, August 8, 2026"
    assert first.url == (
        "https://www.democrats.senate.gov/2026/08/08/"
        "wrap-up-for-friday-august-7-and-saturday-august-8-2026"
    )
    assert "Pro Forma" in second.title


def test_uids_stable_across_reparse():
    a = parse_feed(load_fixture("committee_rss.xml"), source_id="x", chamber="senate",
                   today="2026-08-04")
    b = parse_feed(load_fixture("committee_rss.xml"), source_id="x", chamber="senate",
                   today="2026-08-05")  # different day, same content
    assert [i.uid for i in a] == [i.uid for i in b]
