"""html_diff adapter: press listings without RSS → candidate press Items; the
discussion-draft catcher (plan Phase 4.3). Novelty is decided by state, not here —
the adapter returns ALL current entries and stays stateless."""

import pytest

from tests.conftest import load_fixture
from watcher.adapters.html_diff import extract_entries
from watcher.models import SourceError

SELECTORS = {"entry": "li.press-item", "title": "a", "link": "a", "date": "span.date"}


def test_all_current_entries_returned_as_press_items():
    items = extract_entries(
        load_fixture("member_press.html").decode(),
        SELECTORS,
        source_id="example-press",
        chamber="house",
        base_url="https://example.house.gov",
    )
    assert len(items) == 3
    assert all(i.kind == "press" for i in items)


def test_dates_normalized_to_iso():
    items = extract_entries(
        load_fixture("member_press.html").decode(),
        SELECTORS,
        source_id="example-press",
        chamber="house",
        base_url="https://example.house.gov",
    )
    assert items[0].date == "2026-07-30"  # "July 30, 2026" on the page


def test_relative_links_resolved_against_base_url():
    items = extract_entries(
        load_fixture("member_press.html").decode(),
        SELECTORS,
        source_id="example-press",
        chamber="house",
        base_url="https://example.house.gov",
    )
    relative = next(i for i in items if "item-one" in i.url)
    absolute = next(i for i in items if "item-three" in i.url)
    assert relative.url == "https://example.house.gov/media/press-releases/example-item-one"
    assert absolute.url.startswith("https://example.house.gov/")


OBERNOLTE_SELECTORS = {
    "entry": "div.media-body",
    "title": "div.h3 a",
    "link": "div.h3 a",
    "date": "div.row div.col-auto",
}
BLACKBURN_SELECTORS = {
    "entry": "div.element",
    "title": "div.element-title",
    "link": "a",
    "date": "span.element-datetime",
}
WARNER_SELECTORS = {
    "entry": "div.ArticleBlock",
    "title": "h3.elementor-heading-title",
    "link": "h3.elementor-heading-title a",
    "date": "time",
}


def test_obernolte_frontier_introduction_release_pinned():
    """Obernolte-unique property: the FRONTIER introduction release resolves to its
    exact slug URL (the GAAIA-analog catch). CMS-shape coverage lives in the
    parametrized fixture test below."""
    items = extract_entries(
        load_fixture("rep-obernolte-press.html").decode(),
        OBERNOLTE_SELECTORS,
        source_id="rep-obernolte-press",
        chamber="house",
        base_url="https://obernolte.house.gov/media/press-releases",
    )
    frontier = items[1]
    assert frontier.date == "2026-07-23"
    assert "FRONTIER Act" in frontier.title
    assert frontier.url == (
        "https://obernolte.house.gov/media/press-releases/"
        "obernolte-trahan-introduce-bipartisan-frontier-act-strengthen-oversight"
    )


def test_warner_ordinal_suffix_dates_normalize_on_every_entry():
    """Warner-unique property: WP/Elementor dates carry ordinal suffixes
    ('August 7th, 2026', '5th') — every entry must strip them, not just the first."""
    items = extract_entries(
        load_fixture("sen-warner-press.html").decode(),
        WARNER_SELECTORS,
        source_id="sen-warner-press",
        chamber="senate",
        base_url="https://www.warner.senate.gov/newsroom/press-releases",
    )
    assert [i.date for i in items] == ["2026-08-07", "2026-08-06", "2026-08-05"]


EVO_H5_SELECTORS = {
    "entry": "div.evo-media-object",
    "title": "div.h5 a",
    "link": "div.h5 a",
    "date": "div.row div.col-auto",
}
PAGELIST_SELECTORS = {
    "entry": "li.PageList__item",
    "title": "h2.ArticleTitle",
    "link": "a",
    "date": "p.Heading",
}


@pytest.mark.parametrize(
    ("fixture", "selectors", "chamber", "base_url", "first_date", "title_prefix"),
    [
        # evo-Drupal h3 — '%B %d, %Y' dates
        (
            "rep-obernolte-press.html",
            OBERNOLTE_SELECTORS,
            "house",
            "https://obernolte.house.gov/media/press-releases",
            "2026-08-06",
            "Energy and Commerce Members Obernolte",
        ),
        # Blackburn static HTML — m/d/Y dates, day not zero-padded ('08/5/2026')
        (
            "sen-blackburn-press.html",
            BLACKBURN_SELECTORS,
            "senate",
            "https://www.blackburn.senate.gov/press-releases",
            "2026-08-05",
            "Blackburn & Blumenthal Celebrate",
        ),
        # WP/Elementor ArticleBlock — ordinal-suffix dates ('August 7th, 2026')
        (
            "sen-warner-press.html",
            WARNER_SELECTORS,
            "senate",
            "https://www.warner.senate.gov/newsroom/press-releases",
            "2026-08-07",
            "Warner, Cortez Masto",
        ),
        # evo-Drupal h3 variant (same CMS as Obernolte)
        (
            "rep-houchin-press.html",
            OBERNOLTE_SELECTORS,
            "house",
            "https://houchin.house.gov/media/press-releases",
            "2026-08-04",
            "Houchin, McBath Introduce",
        ),
        (
            "rep-stevens-press.html",
            OBERNOLTE_SELECTORS,
            "house",
            "https://stevens.house.gov/media/press-releases",
            "2026-07-22",
            "STATEMENT: Rep. Haley Stevens",
        ),
        # evo-Drupal h5 variant
        (
            "rep-subramanyam-press.html",
            EVO_H5_SELECTORS,
            "house",
            "https://subramanyam.house.gov/media/press-releases",
            "2026-08-07",
            "Subramanyam, Beyer, Walkinshaw",
        ),
        # Senate PageList CMS — dotted dates ('08.10.2026')
        (
            "sen-cruz-press.html",
            PAGELIST_SELECTORS,
            "senate",
            "https://www.cruz.senate.gov/newsroom/press-releases",
            "2026-08-10",
            "Sens. Cruz, Gillibrand",
        ),
        (
            "sen-rounds-press.html",
            PAGELIST_SELECTORS,
            "senate",
            "https://www.rounds.senate.gov/newsroom/press-releases",
            "2026-08-10",
            "Rounds Introduces Bipartisan Bill",
        ),
        (
            "sen-peters-mi-press.html",
            PAGELIST_SELECTORS,
            "senate",
            "https://www.peters.senate.gov/newsroom/press-releases",
            "2026-08-06",
            "Peters Leads Resolution",
        ),
    ],
)
def test_real_page_fixtures_normalize_to_press_items(
    fixture, selectors, chamber, base_url, first_date, title_prefix
):
    """Real captures 2026-08-11, one per enabled html_diff source (see
    fixtures/README.md provenance). Pins each office's CMS shape."""
    sid = fixture.removesuffix(".html")
    items = extract_entries(
        load_fixture(fixture).decode(), selectors, source_id=sid, chamber=chamber, base_url=base_url
    )
    assert len(items) == 3
    first = items[0]
    assert first.kind == "press"
    assert first.chamber == chamber
    assert first.date == first_date
    assert first.title.startswith(title_prefix)
    assert first.url.startswith("http")


def test_real_page_selectors_missing_raise_source_error():
    """Adversarial: right entry container, wrong inner selectors → SourceError,
    never a silent empty field."""
    html = load_fixture("rep-obernolte-press.html").decode()
    broken = dict(OBERNOLTE_SELECTORS, title="h9.does-not-exist")
    with pytest.raises(SourceError):
        extract_entries(
            html,
            broken,
            source_id="rep-obernolte-press",
            chamber="house",
            base_url="https://obernolte.house.gov/media/press-releases",
        )


def test_unparseable_date_format_raises_source_error():
    """Adversarial: a date string outside every known format must raise, not
    silently fall back."""
    html = '<div class="e"><a href="/x">T</a><span class="d">someday soon</span></div>'
    with pytest.raises(SourceError):
        extract_entries(
            html,
            {"entry": "div.e", "title": "a", "link": "a", "date": "span.d"},
            source_id="x",
            chamber="house",
            base_url="https://example.gov",
        )


def test_one_bad_entry_is_skipped_and_the_rest_still_surface():
    """Issue #9: a single entry with an unparseable date (or a missed inner selector)
    must not take the whole source down — skip it, keep the other N-1."""
    html = """
    <ul>
      <li class="e"><a href="/one">One</a><span class="d">July 30, 2026</span></li>
      <li class="e"><a href="/two">Two</a><span class="d">someday soon</span></li>
      <li class="e"><a href="/three">Three</a></li>
      <li class="e"><a href="/four">Four</a><span class="d">July 27, 2026</span></li>
    </ul>
    """
    items = extract_entries(
        html,
        {"entry": "li.e", "title": "a", "link": "a", "date": "span.d"},
        source_id="x",
        chamber="house",
        base_url="https://example.gov",
    )
    assert [i.title for i in items] == ["One", "Four"]
    assert [i.date for i in items] == ["2026-07-30", "2026-07-27"]


def test_missing_selector_key_raises_source_error_not_key_error():
    """Issue #9: a config row missing one of {entry,title,link,date} must surface as a
    SourceError (health warning) rather than a KeyError that escapes the adapter."""
    html = '<div class="e"><a href="/x">T</a><span class="d">July 30, 2026</span></div>'
    with pytest.raises(SourceError, match="date"):
        extract_entries(
            html,
            {"entry": "div.e", "title": "a", "link": "a"},  # no "date"
            source_id="x",
            chamber="house",
            base_url="https://example.gov",
        )
    with pytest.raises(SourceError, match="entry"):
        extract_entries(
            html,
            {"title": "a", "link": "a", "date": "span.d"},  # no "entry"
            source_id="x",
            chamber="house",
            base_url="https://example.gov",
        )


def test_zero_matches_raises_source_error_not_empty_list():
    """Selector drift tripwire: a press page always has entries; zero matches means
    the selector broke, and silence would be indistinguishable from a quiet week."""
    with pytest.raises(SourceError):
        extract_entries(
            "<html><body><p>redesigned page</p></body></html>",
            SELECTORS,
            source_id="example-press",
            chamber="house",
            base_url="https://example.house.gov",
        )
