"""html_diff adapter: press listings without RSS → candidate press Items; the
discussion-draft catcher (plan Phase 4.3). Novelty is decided by state, not here —
the adapter returns ALL current entries and stays stateless."""

import pytest

from tests.conftest import load_fixture
from watcher.adapters.html_diff import extract_entries
from watcher.models import SourceError

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


OBERNOLTE_SELECTORS = {"entry": "div.media-body", "title": "div.h3 a",
                       "link": "div.h3 a", "date": "div.row div.col-auto"}
BLACKBURN_SELECTORS = {"entry": "div.element", "title": "div.element-title",
                       "link": "a", "date": "span.element-datetime"}
WARNER_SELECTORS = {"entry": "div.ArticleBlock", "title": "h3.elementor-heading-title",
                    "link": "h3.elementor-heading-title a", "date": "time"}


def test_obernolte_real_page_normalizes_to_press_items():
    """Real capture of obernolte.house.gov/media/press-releases (2026-08-11) —
    evo-Drupal listing; '%B %d, %Y' dates. Pins the FRONTIER introduction release."""
    items = extract_entries(load_fixture("rep-obernolte-press.html").decode(),
                            OBERNOLTE_SELECTORS, source_id="rep-obernolte-press",
                            chamber="house",
                            base_url="https://obernolte.house.gov/media/press-releases")
    assert len(items) == 3
    assert all(i.kind == "press" and i.chamber == "house" for i in items)
    frontier = items[1]
    assert frontier.date == "2026-07-23"
    assert "FRONTIER Act" in frontier.title
    assert frontier.url == (
        "https://obernolte.house.gov/media/press-releases/"
        "obernolte-trahan-introduce-bipartisan-frontier-act-strengthen-oversight"
    )


def test_blackburn_real_page_slash_dates_normalize():
    """Real capture of blackburn.senate.gov/press-releases (2026-08-11) —
    dates are '08/5/2026' (m/d/Y, day not zero-padded)."""
    items = extract_entries(load_fixture("sen-blackburn-press.html").decode(),
                            BLACKBURN_SELECTORS, source_id="sen-blackburn-press",
                            chamber="senate",
                            base_url="https://www.blackburn.senate.gov/press-releases")
    assert len(items) == 3
    first = items[0]
    assert first.kind == "press"
    assert first.chamber == "senate"
    assert first.date == "2026-08-05"
    assert first.title.startswith("Blackburn & Blumenthal Celebrate")
    assert first.url.startswith(
        "https://www.blackburn.senate.gov/2026/8/blackburn-blumenthal-celebrate"
    )
    assert items[1].date == "2026-08-04"


def test_warner_real_page_ordinal_dates_normalize():
    """Real capture of warner.senate.gov/newsroom/press-releases (2026-08-11) —
    WP/Elementor ArticleBlock; dates carry ordinal suffixes ('August 7th, 2026')."""
    items = extract_entries(load_fixture("sen-warner-press.html").decode(),
                            WARNER_SELECTORS, source_id="sen-warner-press",
                            chamber="senate",
                            base_url="https://www.warner.senate.gov/newsroom/press-releases")
    assert len(items) == 3
    first = items[0]
    assert first.kind == "press"
    assert first.date == "2026-08-07"
    assert first.title.startswith("Warner, Cortez Masto")
    assert first.url.startswith(
        "https://www.warner.senate.gov/newsroom/press-releases/warner-cortez-masto"
    )
    assert items[2].date == "2026-08-05"


EVO_H5_SELECTORS = {"entry": "div.evo-media-object", "title": "div.h5 a",
                    "link": "div.h5 a", "date": "div.row div.col-auto"}
PAGELIST_SELECTORS = {"entry": "li.PageList__item", "title": "h2.ArticleTitle",
                      "link": "a", "date": "p.Heading"}


@pytest.mark.parametrize(
    ("fixture", "selectors", "chamber", "base_url", "first_date", "title_prefix"),
    [
        # evo-Drupal h3 variant (same CMS as Obernolte)
        ("rep-houchin-press.html", OBERNOLTE_SELECTORS, "house",
         "https://houchin.house.gov/media/press-releases",
         "2026-08-04", "Houchin, McBath Introduce"),
        ("rep-stevens-press.html", OBERNOLTE_SELECTORS, "house",
         "https://stevens.house.gov/media/press-releases",
         "2026-07-22", "STATEMENT: Rep. Haley Stevens"),
        # evo-Drupal h5 variant
        ("rep-subramanyam-press.html", EVO_H5_SELECTORS, "house",
         "https://subramanyam.house.gov/media/press-releases",
         "2026-08-07", "Subramanyam, Beyer, Walkinshaw"),
        # Senate PageList CMS — dotted dates ('08.10.2026')
        ("sen-cruz-press.html", PAGELIST_SELECTORS, "senate",
         "https://www.cruz.senate.gov/newsroom/press-releases",
         "2026-08-10", "Sens. Cruz, Gillibrand"),
        ("sen-rounds-press.html", PAGELIST_SELECTORS, "senate",
         "https://www.rounds.senate.gov/newsroom/press-releases",
         "2026-08-10", "Rounds Introduces Bipartisan Bill"),
        ("sen-peters-mi-press.html", PAGELIST_SELECTORS, "senate",
         "https://www.peters.senate.gov/newsroom/press-releases",
         "2026-08-06", "Peters Leads Resolution"),
    ],
)
def test_real_page_fixtures_normalize_to_press_items(
    fixture, selectors, chamber, base_url, first_date, title_prefix
):
    """Real captures 2026-08-11, one per enabled html_diff source (see
    fixtures/README.md provenance). Pins each office's CMS shape."""
    sid = fixture.removesuffix(".html")
    items = extract_entries(load_fixture(fixture).decode(), selectors,
                            source_id=sid, chamber=chamber, base_url=base_url)
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
        extract_entries(html, broken, source_id="rep-obernolte-press", chamber="house",
                        base_url="https://obernolte.house.gov/media/press-releases")


def test_unparseable_date_format_raises_source_error():
    """Adversarial: a date string outside every known format must raise, not
    silently fall back."""
    html = '<div class="e"><a href="/x">T</a><span class="d">someday soon</span></div>'
    with pytest.raises(SourceError):
        extract_entries(html, {"entry": "div.e", "title": "a", "link": "a",
                               "date": "span.d"},
                        source_id="x", chamber="house", base_url="https://example.gov")


def test_zero_matches_raises_source_error_not_empty_list():
    """Selector drift tripwire: a press page always has entries; zero matches means
    the selector broke, and silence would be indistinguishable from a quiet week."""
    with pytest.raises(SourceError):
        extract_entries("<html><body><p>redesigned page</p></body></html>", SELECTORS,
                        source_id="example-press", chamber="house",
                        base_url="https://example.house.gov")
