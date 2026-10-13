"""State store behavior: novelty filtering, baseline runs, failure counting,
explicit persistence (plan Phase 2)."""

from tests.conftest import make_item
from watcher.state import State


def items(*uids, date="2026-08-01"):
    return [make_item(uid=u, date=date) for u in uids]


def test_missing_file_yields_fresh_state(tmp_path):
    state = State.load(tmp_path / "nope" / "state.json")
    assert state.is_baseline("any-source")


def test_baseline_run_yields_no_new_items():
    state = State.load_fresh()
    new = state.new_items("src", items("a", "b", "c"), today="2026-08-04")
    assert new == []


def test_baseline_with_backlog_returns_only_recent_items():
    state = State.load_fresh()
    batch = items("old", date="2026-06-01") + items("recent", date="2026-08-01")
    new = state.new_items("src", batch, today="2026-08-04", include_backlog_days=7)
    assert [i.uid for i in new] == ["recent"]


def test_seen_items_filtered_after_success_roundtrip(tmp_path):
    path = tmp_path / "state.json"
    state = State.load(path)
    batch = items("a", "b")
    state.new_items("src", batch, today="2026-08-04")
    state.record_success("src", batch)
    state.save(path)

    reloaded = State.load(path)
    batch2 = items("a", "b", "c")
    new = reloaded.new_items("src", batch2, today="2026-08-05")
    assert [i.uid for i in new] == ["c"]


def test_refetching_same_items_is_safe():
    """UID dedupe makes re-fetch idempotent — the loss-proof ordering guarantee."""
    state = State.load_fresh()
    batch = items("a")
    state.new_items("src", batch, today="2026-08-04")
    state.record_success("src", batch)
    assert state.new_items("src", batch, today="2026-08-04") == []


def test_consecutive_failures_count_and_reset():
    state = State.load_fresh()
    assert state.record_failure("src") == 1
    assert state.record_failure("src") == 2
    assert state.record_failure("src") == 3
    state.record_success("src", [])
    assert state.record_failure("src") == 1


def test_mutations_not_persisted_without_save(tmp_path):
    path = tmp_path / "state.json"
    state = State.load(path)
    state.record_success("src", items("a"))
    state.save(path)

    state2 = State.load(path)
    state2.record_success("src", items("b"))
    # no save

    reloaded = State.load(path)
    new = reloaded.new_items("src", items("b"), today="2026-08-04")
    assert [i.uid for i in new] == ["b"]


def test_corrupted_state_file_is_quarantined_and_run_starts_fresh(tmp_path):
    """Issue #9 (H2): a truncated/garbage state.json must not take the cron down
    permanently. Pinned behavior: move the bad file aside (evidence preserved),
    start from a fresh baseline, and keep going."""
    path = tmp_path / "state.json"
    path.write_text('{"schema_version": 1, "sources": {"src": {"seen_uids": ["a"')  # truncated

    state = State.load(path)

    assert state.is_baseline("src")
    quarantined = list(tmp_path.glob("state.json.corrupt-*"))
    assert len(quarantined) == 1, "corrupt file should be moved aside, not deleted"
    assert '"seen_uids": ["a"' in quarantined[0].read_text()
    assert not path.exists()


def test_seen_uids_capped_oldest_evicted_first():
    """Issue #9: seen_uids must not grow without bound across a year of daily runs.
    Cap per source; evict least-recently-seen first."""
    state = State(max_seen_uids=3)
    state.record_success("src", items("a", "b", "c"))
    state.record_success("src", items("d"))  # pushes out the oldest ("a")

    new = state.new_items("src", items("a", "b", "c", "d"), today="2026-08-04")
    assert [i.uid for i in new] == ["a"]


def test_seen_uid_still_present_on_page_is_not_evicted():
    """A press listing shows the same entries for weeks. Re-seeing a uid must
    refresh it so the cap evicts genuinely-stale uids, not long-lived page rows."""
    state = State(max_seen_uids=3)
    state.record_success("src", items("a", "b", "c"))
    state.record_success("src", items("a", "d"))  # "a" re-seen; "b" is now oldest

    new = state.new_items("src", items("a", "b", "c", "d"), today="2026-08-04")
    assert [i.uid for i in new] == ["b"]


def test_seen_uid_cap_survives_save_load_roundtrip(tmp_path):
    path = tmp_path / "state.json"
    state = State(max_seen_uids=2)
    state.record_success("src", items("a", "b"))
    state.save(path)

    reloaded = State.load(path, max_seen_uids=2)
    reloaded.record_success("src", items("c"))
    new = reloaded.new_items("src", items("a", "b", "c"), today="2026-08-04")
    assert [i.uid for i in new] == ["a"]
