"""UID construction rules — content-derived, stable across runs (plan §Data model)."""

from watcher.models import make_bill_uid, make_hash_uid


def test_bill_uid_is_readable_and_deterministic():
    assert make_bill_uid("hr9363", "intro", "2026-06-18") == "hr9363-intro-2026-06-18"


def test_bill_uid_distinguishes_actions_on_same_bill():
    intro = make_bill_uid("hr9363", "intro", "2026-06-18")
    action = make_bill_uid("hr9363", "action", "2026-06-25")
    assert intro != action


def test_hash_uid_stable_across_calls():
    a = make_hash_uid("https://x.house.gov/press/1", "Some Title")
    b = make_hash_uid("https://x.house.gov/press/1", "Some Title")
    assert a == b


def test_hash_uid_changes_when_title_or_url_changes():
    base = make_hash_uid("https://x.house.gov/press/1", "Some Title")
    assert make_hash_uid("https://x.house.gov/press/2", "Some Title") != base
    assert make_hash_uid("https://x.house.gov/press/1", "Another Title") != base
