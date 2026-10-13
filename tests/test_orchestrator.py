"""Orchestrator behavior: failure isolation, crash-safe state ordering, idempotence
(plan Phase 6). Sources are injected as fakes — the boundary under test is
run_watcher itself, not the adapters."""

import pytest

from tests.conftest import make_item
from watcher.models import SourceError
from watcher.run import run_watcher


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
    return FakeSource(
        source_id,
        items=[
            make_item(
                uid=uid,
                source=source_id,
                title="AI frontier model markup scheduled",
                kind="markup",
                date=date,
            )
        ],
    )


def run(sources, tmp_path, keywords, today="2026-08-04", **kw):
    """Test helper: run_watcher returns a RunResult; existing tests want the Path."""
    return run_watcher(
        sources=sources,
        state_path=tmp_path / "state" / "state.json",
        digest_dir=tmp_path / "digests",
        keywords=keywords,
        today=today,
        include_backlog_days=kw.pop("include_backlog_days", 30),
    ).digest_path


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


class ExplodingSource:
    """Adapter bug stand-in: raises something that is NOT a SourceError."""

    def __init__(self, source_id, exc):
        self.id = source_id
        self._exc = exc

    def fetch(self):
        raise self._exc


@pytest.mark.parametrize(
    "exc",
    [KeyError("entry"), AttributeError("'NoneType' object has no attribute 'get'")],
    ids=["KeyError", "AttributeError"],
)
def test_unexpected_adapter_exception_is_isolated_like_source_error(tmp_path, keywords, exc):
    """Issue #9: an unattended cron must survive a single adapter blowing up with a
    non-SourceError (bs4 quirk, KeyError on a bad config). The healthy source
    still gets digested and the broken one shows up in source health."""
    digest_path = run([good_source(), ExplodingSource("buggy", exc)], tmp_path, keywords)
    text = digest_path.read_text()
    assert "AI frontier model markup scheduled" in text
    assert "buggy" in text


def test_run_result_reports_stale_sources(tmp_path, keywords):
    """Issue #9: selector drift must escalate beyond the digest body — the orchestrator
    surfaces which sources crossed the STALE threshold so the CLI can log/exit on it."""
    sources = [good_source(), FakeSource("broken", error=True)]
    results = []
    for day in ("2026-08-04", "2026-08-05", "2026-08-06"):
        results.append(
            run_watcher(
                sources=sources,
                state_path=tmp_path / "state" / "state.json",
                digest_dir=tmp_path / "digests",
                keywords=keywords,
                today=day,
                include_backlog_days=30,
            )
        )
    assert results[0].stale_sources == []
    assert results[1].stale_sources == []
    assert results[2].stale_sources == ["broken"]


def test_env_files_load_from_repo_root_regardless_of_cwd(tmp_path, monkeypatch):
    """Issue #9: `load_dotenv('.env.local')` resolved against CWD, so a cron with a
    different working directory silently ran without the API key. The loader must
    anchor to an explicit root."""
    from watcher.run import load_env_files

    root = tmp_path / "repo"
    root.mkdir()
    (root / ".env.local").write_text("CONGRESS_API_KEY=from-env-local\n")
    (root / ".env").write_text("CONGRESS_API_KEY=from-dot-env\nOTHER_KEY=from-dot-env\n")
    elsewhere = tmp_path / "elsewhere"
    elsewhere.mkdir()
    monkeypatch.chdir(elsewhere)
    monkeypatch.delenv("CONGRESS_API_KEY", raising=False)
    monkeypatch.delenv("OTHER_KEY", raising=False)

    load_env_files(root)

    import os

    assert os.environ["CONGRESS_API_KEY"] == "from-env-local"  # .env.local wins over .env
    assert os.environ["OTHER_KEY"] == "from-dot-env"
