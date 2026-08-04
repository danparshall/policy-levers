"""Scorer behavior: word boundaries, case rules, weights, tracked bills, triage
(plan Phase 3). Word-boundary matching is mandatory — substring 'ai' would flood
the digest ('said', 'aid', 'brain')."""

from watcher.scoring import match_tracked, score_item, triage

from tests.conftest import make_item

# --- keyword matching rules ---

def test_short_allcaps_term_requires_word_boundary(keywords):
    hit = make_item(title="The AI Accountability Act")
    miss = make_item(title="He said aid to Bahrain requires brainstorming")
    assert score_item(hit, keywords) > 0
    assert score_item(miss, keywords) == 0


def test_short_allcaps_term_is_case_sensitive(keywords):
    # "Ai"/"ai" as a word is almost never the acronym — only exact-case "AI" matches
    miss = make_item(title="Ai Weiwei exhibit opens", body_excerpt="")
    assert score_item(miss, keywords) == 0


def test_phrases_match_case_insensitively(keywords):
    item = make_item(title="Hearing on Artificial Intelligence in Agriculture")
    assert score_item(item, keywords) > 0


# --- weighting ---

def test_title_hits_weigh_double_vs_body(keywords):
    in_title = make_item(title="AI oversight", body_excerpt="", kind="press")
    in_body = make_item(title="Committee update", body_excerpt="discusses AI oversight", kind="press")
    assert score_item(in_title, keywords) > score_item(in_body, keywords)


def test_tier_weights_order(keywords):
    high = make_item(title="frontier model rules", kind="press")
    medium = make_item(title="NIST framework update", kind="press")
    low = make_item(title="innovation agenda", kind="press")
    assert score_item(high, keywords) > score_item(medium, keywords) > score_item(low, keywords)


def test_kind_boost_applied(keywords):
    markup = make_item(title="NIST review", kind="markup")
    press = make_item(title="NIST review", kind="press")
    boost = keywords.kind_boost["markup"] - keywords.kind_boost["press"]
    assert score_item(markup, keywords) - score_item(press, keywords) == boost


# --- tracked bills ---

def test_tracked_alias_fills_matched_bills(keywords):
    item = make_item(title="Committee schedules markup of H.R. 9363")
    assert match_tracked(item, keywords) == ["hr9363"]


def test_tracked_alias_word_boundary(keywords):
    # "CAISI" must not fire inside another token
    item = make_item(title="Scaisiology conference announced")
    assert match_tracked(item, keywords) == []


def test_tracked_match_in_body_counts(keywords):
    item = make_item(title="Weekly wrap", body_excerpt="…includes the Great American AI Act draft…")
    assert "gaaia" in match_tracked(item, keywords)


# --- triage ---

def test_triage_pins_tracked_regardless_of_score(keywords):
    dull_but_tracked = make_item(uid="t1", title="Technical corrections to H.R. 9363", kind="press")
    result = triage([dull_but_tracked], keywords)
    assert [i.uid for i in result.pinned] == ["t1"]


def test_triage_splits_on_threshold(keywords):
    strong = make_item(uid="s", title="AI frontier model markup", kind="markup")
    weak = make_item(uid="w", title="Post office renaming", kind="press")
    result = triage([strong, weak], keywords)
    assert [i.uid for i, _ in result.listed] == ["s"]
    assert result.suppressed_count == 1


def test_triage_sorts_listed_by_score_desc(keywords):
    a = make_item(uid="a", title="NIST update", kind="press")           # medium
    b = make_item(uid="b", title="AI frontier model markup", kind="markup")  # high, boosted
    result = triage([a, b], keywords)
    scores = [s for _, s in result.listed]
    assert scores == sorted(scores, reverse=True)
    assert result.listed[0][0].uid == "b"


def test_event_kinds_bypass_threshold(keywords):
    """A markup/floor/hearing item is time-critical even with zero keyword hits —
    committee meeting feeds are already curated by source selection. Without this
    rule the June-2026 backtest's 'Full Committee Markup' could never surface."""
    quiet_markup = make_item(uid="q", title="Full Committee Markup", kind="markup")
    result = triage([quiet_markup], keywords)
    assert [i.uid for i, _ in result.listed] == ["q"]
    assert result.suppressed_count == 0


def test_tracked_matches_bill_id_from_uid(keywords):
    """congress_api items carry the bill id in their uid; tracked matching must fire
    on it even when no alias appears in the title (official long titles rarely
    contain 'H.R. NNNN')."""
    intro = make_item(uid="hr9363-intro-2026-06-18",
                      title="To redesignate the AI Safety Institute, and for other purposes.",
                      kind="bill_intro")
    assert "hr9363" in match_tracked(intro, keywords)


def test_triage_pinned_items_not_double_listed(keywords):
    tracked = make_item(uid="t", title="AI markup on H.R. 9363", kind="markup")
    result = triage([tracked], keywords)
    assert [i.uid for i in result.pinned] == ["t"]
    assert all(i.uid != "t" for i, _ in result.listed)
