"""THE ACCEPTANCE TEST (issue #3): backtest against June 2026.

The tool as built must have surfaced:
  (a) GAAIA on release day (2026-06-04) via the Trahan/Obernolte press layer,
  (b) H.R. 9363 at introduction (2026-06-18) via the API poller,
  (c) the 6/25 House Science markup IN ADVANCE via docs.house.gov.

Simulation: single run on 2026-06-23 against empty state with a 30-day backlog window
(equivalent to having run daily since late May, compressed). Real adapters parse
June fixtures; only network fetch is bypassed. Fixture provenance: tests/fixtures/README.md.
"""

import json

from watcher.adapters.congress_api import parse_bill_list
from watcher.adapters.html_diff import extract_entries
from watcher.adapters.structured import parse_meeting_feed
from watcher.run import run_watcher

from tests.conftest import load_fixture

TODAY = "2026-06-23"

TRAHAN_SELECTORS = {"entry": "li.press-item", "title": "a", "link": "a", "date": "span.date"}


class FixtureSource:
    """Real adapter parsing, fixture-fed — only the network hop is bypassed."""

    def __init__(self, source_id, items_fn):
        self.id = source_id
        self._items_fn = items_fn

    def fetch(self):
        return self._items_fn()


def june_sources():
    return [
        FixtureSource("trahan-press", lambda: extract_entries(
            load_fixture("trahan_press_june2026.html").decode(), TRAHAN_SELECTORS,
            source_id="trahan-press", chamber="house", base_url="https://trahan.house.gov")),
        FixtureSource("congress-api", lambda: parse_bill_list(
            json.loads(load_fixture("congress_api_hr9363_intro.json")),
            source_id="congress-api")),
        FixtureSource("docs-house-sy00", lambda: parse_meeting_feed(
            load_fixture("docshouse_sy00_june2026.xml"),
            source_id="docs-house-sy00", chamber="house")),
    ]


def run_june(tmp_path, keywords):
    return run_watcher(
        sources=june_sources(),
        state_path=tmp_path / "state" / "state.json",
        digest_dir=tmp_path / "digests",
        keywords=keywords,
        today=TODAY,
        include_backlog_days=30,
    )


def test_backtest_a_gaaia_surfaced_from_press_layer(tmp_path, keywords):
    text = run_june(tmp_path, keywords).read_text()
    assert "Great American AI Act" in text
    assert "2026-06-04" in text  # release day, correctly dated


def test_backtest_b_hr9363_surfaced_at_introduction(tmp_path, keywords):
    text = run_june(tmp_path, keywords).read_text()
    assert "9363" in text
    assert "2026-06-18" in text


def test_backtest_c_markup_surfaced_in_advance(tmp_path, keywords):
    text = run_june(tmp_path, keywords).read_text()
    markup_line = next(ln for ln in text.splitlines()
                       if "Markup" in ln and "docs-house-sy00" in ln)
    assert "2026-06-25" in markup_line  # event date is AFTER today (06-23): advance notice


def test_backtest_tracked_items_pinned_at_top(tmp_path, keywords):
    """GAAIA (tracked via alias) and H.R. 9363 (tracked via bill-id in uid) must both
    be pinned above everything else."""
    text = run_june(tmp_path, keywords).read_text()
    tracked_idx = text.index("Tracked bills")
    time_critical_idx = text.index("Time-critical")
    assert tracked_idx < text.index("Great American AI Act") < time_critical_idx
    assert tracked_idx < text.index("hr/9363") < time_critical_idx  # via item url in the line


def test_backtest_next_day_run_is_quiet(tmp_path, keywords):
    """Day-after run with unchanged sources: nothing new — no duplicate alarms."""
    run_june(tmp_path, keywords)
    second = run_watcher(
        sources=june_sources(),
        state_path=tmp_path / "state" / "state.json",
        digest_dir=tmp_path / "digests",
        keywords=keywords,
        today="2026-06-24",
        include_backlog_days=30,
    )
    assert second.name == "20260624.md"
    assert "Great American AI Act" not in second.read_text()
