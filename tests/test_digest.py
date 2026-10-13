"""Digest rendering behavior: section order, pinning, sorting, health warnings,
deterministic output, append-not-overwrite (plan Phase 5)."""

import contextlib
from datetime import UTC

import pytest

from tests.conftest import make_item
from watcher.digest import render, write_digest


def sample_sections():
    pinned = [
        make_item(
            uid="p",
            title="Markup of H.R. 9363 scheduled",
            kind="markup",
            date="2026-08-06",
            matched_bills=["hr9363"],
        )
    ]
    scored = [
        (make_item(uid="m1", title="Full Committee Markup", kind="markup", date="2026-08-07"), 6),
        (make_item(uid="m2", title="AI hearing announced", kind="hearing", date="2026-08-05"), 5),
        (
            make_item(
                uid="n1", title="Frontier model press statement", kind="press", date="2026-08-03"
            ),
            7,
        ),
    ]
    return pinned, scored


def test_sections_appear_in_canonical_order():
    pinned, scored = sample_sections()
    text = render(
        date="2026-08-04",
        pinned=pinned,
        scored=scored,
        health=[("dead-source", 3)],
        suppressed_count=12,
    )
    i_tracked = text.index("Tracked bills")
    i_time = text.index("Time-critical")
    i_new = text.index("New & notable")
    i_health = text.index("Source health")
    assert i_tracked < i_time < i_new < i_health


def test_time_critical_sorted_soonest_event_first():
    _, scored = sample_sections()
    text = render(date="2026-08-04", pinned=[], scored=scored, health=[], suppressed_count=0)
    # m2 (event 08-05) must precede m1 (event 08-07) despite lower score
    assert text.index("AI hearing announced") < text.index("Full Committee Markup")


def test_press_items_sorted_by_score_not_date():
    text = render(
        date="2026-08-04",
        pinned=[],
        scored=[
            (make_item(uid="lo", title="Minor note", kind="press", date="2026-08-04"), 3),
            (make_item(uid="hi", title="Big AI story", kind="press", date="2026-08-01"), 9),
        ],
        health=[],
        suppressed_count=0,
    )
    assert text.index("Big AI story") < text.index("Minor note")


def test_empty_sections_omitted():
    text = render(date="2026-08-04", pinned=[], scored=[], health=[], suppressed_count=0)
    assert "Tracked bills" not in text
    assert "Source health" not in text


def test_item_line_contains_score_date_source_title_url():
    item = make_item(
        uid="x",
        title="AI hearing",
        kind="press",
        date="2026-08-02",
        source="senate-commerce-press",
        url="https://example.gov/x",
    )
    text = render(date="2026-08-04", pinned=[], scored=[(item, 5)], health=[], suppressed_count=0)
    line = next(ln for ln in text.splitlines() if "AI hearing" in ln)
    for token in ("5", "2026-08-02", "senate-commerce-press", "https://example.gov/x"):
        assert token in line


def test_suppressed_count_footer_present():
    text = render(date="2026-08-04", pinned=[], scored=[], health=[], suppressed_count=37)
    assert "37" in text  # silence must be distinguishable from a broken run


def test_health_escalates_to_stale_at_three_failures():
    text = render(
        date="2026-08-04",
        pinned=[],
        scored=[],
        health=[("flaky", 1), ("dead", 3)],
        suppressed_count=0,
    )
    assert "flaky" in text
    assert "STALE" in text
    stale_line = next(ln for ln in text.splitlines() if "STALE" in ln)
    assert "dead" in stale_line


def test_render_is_deterministic():
    pinned, scored = sample_sections()
    args = {
        "date": "2026-08-04",
        "pinned": pinned,
        "scored": scored,
        "health": [],
        "suppressed_count": 2,
    }
    assert render(**args) == render(**args)


def test_render_contains_no_wall_clock_timestamp():
    """The digest body must be a pure function of its inputs — rendering a past date
    today must not leak today's date (or any now-timestamp) into the output.

    Two guards (issue #9, M4): every date-shaped token in the output must be one of
    the input dates, and a wall-clock sentinel planted on the module must not
    appear. The first catches any ISO leak regardless of its source; the second
    catches non-ISO formatting of a `now()` read."""
    import re
    from datetime import datetime

    import watcher.digest as digest_module

    sentinel = "SENTINEL-NOW-1999-12-31T23:59:59"

    class _FrozenClock:
        @staticmethod
        def now(*_, **__):
            return sentinel

        @staticmethod
        def today(*_, **__):
            return sentinel

    with contextlib.ExitStack() as stack:
        for name in ("datetime", "date", "time"):
            stack.enter_context(_patched(digest_module, name, _FrozenClock))
        scored = [(make_item(uid="old", title="Old item", kind="press", date="2025-01-01"), 5)]
        text = render(date="2025-01-02", pinned=[], scored=scored, health=[], suppressed_count=0)

    assert sentinel not in text
    assert datetime.now(tz=UTC).date().isoformat() not in text
    found = set(re.findall(r"\d{4}-\d{2}-\d{2}", text))
    assert found == {"2025-01-01", "2025-01-02"}, f"unexpected date tokens: {found}"


@contextlib.contextmanager
def _patched(module, name, value):
    """setattr a (possibly absent) module attribute for the duration of the block."""
    missing = object()
    old = getattr(module, name, missing)
    setattr(module, name, value)
    try:
        yield
    finally:
        if old is missing:
            delattr(module, name)
        else:
            setattr(module, name, old)


def test_write_digest_appends_later_run_instead_of_overwriting(tmp_path):
    path = tmp_path / "20260804.md"
    write_digest(path, "# Digest 2026-08-04\n\nfirst run content\n")
    write_digest(path, "second run content\n")
    text = path.read_text()
    assert "first run content" in text
    assert "second run content" in text
    assert "Later run" in text


def test_write_digest_append_failure_leaves_existing_digest_intact(tmp_path, monkeypatch):
    """Issue #9: the append path used truncate-then-write, so a crash mid-append lost
    the morning's digest. The write must be atomic — if the final commit step fails,
    the original file is untouched."""
    import os

    path = tmp_path / "20260804.md"
    original = "# Digest 2026-08-04\n\nfirst run content\n"
    write_digest(path, original)

    def refuse_replace(*_args, **_kwargs):
        raise OSError("simulated crash at commit")

    monkeypatch.setattr(os, "replace", refuse_replace)
    with pytest.raises(OSError):
        write_digest(path, "second run content\n")

    assert path.read_text() == original
