"""Orchestrator behavior: failure isolation, crash-safe state ordering, idempotence
(plan Phase 6). Sources are injected as fakes — the boundary under test is
run_watcher itself, not the adapters."""

import pytest
from watcher.models import SourceError
from watcher.run import run_watcher

from tests.conftest import make_item


class FakeSource:
    def __init__(self, source_id, items=None, error=False):
        self.id = source_id
        self._items = items or []
        self._error = error

    def fetch(self):
        if self._error:
            raise SourceError(f"{self.id} unavailable")
        return self._items


def good_source(source_id="good", uid="g1", date="2026-08-03"):
    return FakeSource(source_id, items=[
        make_item(uid=uid, source=source_id, title="AI frontier model markup scheduled",
                  kind="markup", date=date)
    ])


def run(sources, tmp_path, keywords, today="2026-08-04", **kw):
    return run_watcher(
        sources=sources,
        state_path=tmp_path / "state" / "state.json",
        digest_dir=tmp_path / "digests",
        keywords=keywords,
        today=today,
        include_backlog_days=kw.pop("include_backlog_days", 30),
    )


def test_happy_path_writes_digest_with_items(tmp_path, keywords):
    digest_path = run([good_source()], tmp_path, keywords)
    text = digest_path.read_text()
    assert "AI frontier model markup scheduled" in text
    assert digest_path.name == "20260804.md"


def test_failing_source_isolated_healthy_source_still_digested(tmp_path, keywords):
    digest_path = run([good_source(), FakeSource("broken", error=True)], tmp_path, keywords)
    text = digest_path.read_text()
    assert "AI frontier model markup scheduled" in text
    assert "broken" in text  # source-health warning present


def test_failure_counts_accumulate_to_stale_across_runs(tmp_path, keywords):
    sources = [good_source(), FakeSource("broken", error=True)]
    run(sources, tmp_path, keywords, today="2026-08-04")
    run(sources, tmp_path, keywords, today="2026-08-05")
    digest_path = run(sources, tmp_path, keywords, today="2026-08-06")
    assert "STALE" in digest_path.read_text()


def test_second_run_same_day_adds_nothing(tmp_path, keywords):
    sources = [good_source()]
    first = run(sources, tmp_path, keywords)
    content_after_first = first.read_text()
    second = run(sources, tmp_path, keywords)
    assert second.read_text() == content_after_first  # idempotent: no dup items, no growth


def test_state_not_saved_when_digest_write_fails(tmp_path, keywords, monkeypatch):
    """Loss-proof ordering: crash during digest write must leave state untouched,
    so the next run re-discovers the items instead of losing them forever."""
    import watcher.run as run_module

    def boom(*args, **kwargs):
        raise OSError("disk full")

    monkeypatch.setattr(run_module, "write_digest", boom)
    with pytest.raises(OSError):
        run([good_source()], tmp_path, keywords)
    monkeypatch.undo()

    digest_path = run([good_source()], tmp_path, keywords)
    assert "AI frontier model markup scheduled" in digest_path.read_text()


def test_baseline_without_backlog_digests_nothing_new(tmp_path, keywords):
    digest_path = run([good_source()], tmp_path, keywords, include_backlog_days=0)
    assert "AI frontier model markup scheduled" not in digest_path.read_text()


def test_disabled_sources_are_skipped(tmp_path, keywords):
    """A source whose fetch raises would poison health if invoked; disabled means never called."""
    never = FakeSource("disabled-src", error=True)
    never.enabled = False
    digest_path = run([never], tmp_path, keywords)
    assert "disabled-src" not in digest_path.read_text()
