"""html_diff adapter: press listings without RSS → candidate press Items; the
discussion-draft catcher (plan Phase 4.3). Novelty is decided by state, not here —
the adapter returns ALL current entries and stays stateless."""

import pytest
from watcher.adapters.html_diff import extract_entries
from watcher.models import SourceError

from tests.conftest import load_fixture

SELECTORS = {"entry": "li.press-item", "title": "a", "link": "a", "date": "span.date"}


def test_all_current_entries_returned_as_press_items():
    items = extract_entries(load_fixture("member_press.html").decode(), SELECTORS,
                            source_id="example-press", chamber="house",
                            base_url="https://example.house.gov")
    assert len(items) == 3
    assert all(i.kind == "press" for i in items)


def test_dates_normalized_to_iso():
    items = extract_entries(load_fixture("member_press.html").decode(), SELECTORS,
                            source_id="example-press", chamber="house",
                            base_url="https://example.house.gov")
    assert items[0].date == "2026-07-30"  # "July 30, 2026" on the page


def test_relative_links_resolved_against_base_url():
    items = extract_entries(load_fixture("member_press.html").decode(), SELECTORS,
                            source_id="example-press", chamber="house",
                            base_url="https://example.house.gov")
    relative = next(i for i in items if "item-one" in i.url)
    absolute = next(i for i in items if "item-three" in i.url)
    assert relative.url == "https://example.house.gov/media/press-releases/example-item-one"
    assert absolute.url.startswith("https://example.house.gov/")


def test_zero_matches_raises_source_error_not_empty_list():
    """Selector drift tripwire: a press page always has entries; zero matches means
    the selector broke, and silence would be indistinguishable from a quiet week."""
    with pytest.raises(SourceError):
        extract_entries("<html><body><p>redesigned page</p></body></html>", SELECTORS,
                        source_id="example-press", chamber="house",
                        base_url="https://example.house.gov")
