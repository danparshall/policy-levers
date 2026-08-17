"""Email notification of new digest content (v1.1 follow-up to leg-watcher v1).

Behaviour under test — `maybe_notify` decides whether to send an email:

  - sender=None            → "skipped:no-config"  (notifications disabled)
  - has_new_content=False  → "skipped:no-content" (empty / unchanged run)
  - digest file missing    → "skipped:no-digest"  (defensive)
  - prior send, same hash  → "skipped:same-hash"  (idempotent re-run)
  - new content or changed → "sent"                (single email + state update)

Idempotency is keyed on (digest filename, sha256(digest_text)). Same file +
different content re-sends; different file (next day) sends independently.
"""

from __future__ import annotations

import json

import pytest

from watcher.notify import maybe_notify, smtp_sender_from_env


class RecordingSender:
    """Callable stand-in for an SMTP sender. Captures (text, subject) tuples."""

    def __init__(self):
        self.calls: list[tuple[str, str]] = []

    def __call__(self, text: str, subject: str) -> None:
        self.calls.append((text, subject))


@pytest.fixture
def digest_file(tmp_path):
    """A digest file at digests/20260817.md with a realistic pinned+notable body."""
    d = tmp_path / "digests"
    d.mkdir()
    path = d / "20260817.md"
    path.write_text(
        "# Legislative digest — 2026-08-17\n\n"
        "## Tracked bills\n\n"
        "- 2026-08-17 · rep-obernolte-press · FRONTIER update (https://example)\n\n"
        "## New & notable\n\n"
        "- [7] 2026-08-16 · sen-warner-press · AI oversight (https://example)\n\n"
        "_2 items suppressed below threshold._\n"
    )
    return path


@pytest.fixture
def notified_state(tmp_path):
    return tmp_path / "watcher-notified.json"


# ------------------ sender absent / no-op cases ------------------


def test_no_sender_returns_no_config_and_does_not_touch_state(digest_file, notified_state):
    status = maybe_notify(
        digest_path=digest_file,
        has_new_content=True,
        notified_state_path=notified_state,
        sender=None,
    )
    assert status == "skipped:no-config"
    assert not notified_state.exists()  # nothing written when disabled


def test_no_new_content_skips_even_with_sender(digest_file, notified_state):
    sender = RecordingSender()
    status = maybe_notify(
        digest_path=digest_file,
        has_new_content=False,
        notified_state_path=notified_state,
        sender=sender,
    )
    assert status == "skipped:no-content"
    assert sender.calls == []
    assert not notified_state.exists()


def test_missing_digest_file_is_defensively_skipped(tmp_path, notified_state):
    sender = RecordingSender()
    status = maybe_notify(
        digest_path=tmp_path / "digests" / "20260817.md",  # does not exist
        has_new_content=True,
        notified_state_path=notified_state,
        sender=sender,
    )
    assert status == "skipped:no-digest"
    assert sender.calls == []


# ------------------ happy path + idempotency ------------------


def test_first_notification_sends_and_records_state(digest_file, notified_state):
    sender = RecordingSender()
    status = maybe_notify(
        digest_path=digest_file,
        has_new_content=True,
        notified_state_path=notified_state,
        sender=sender,
    )
    assert status == "sent"
    assert len(sender.calls) == 1
    body, subject = sender.calls[0]
    assert body == digest_file.read_text()  # full digest goes in the mail
    assert "20260817" in subject  # date-stemmed subject
    assert notified_state.exists()
    state = json.loads(notified_state.read_text())
    assert digest_file.name in state
    assert state[digest_file.name]["content_sha256"]


def test_second_notification_with_same_content_skips(digest_file, notified_state):
    sender = RecordingSender()
    first = maybe_notify(
        digest_path=digest_file,
        has_new_content=True,
        notified_state_path=notified_state,
        sender=sender,
    )
    second = maybe_notify(
        digest_path=digest_file,
        has_new_content=True,
        notified_state_path=notified_state,
        sender=sender,
    )
    assert first == "sent"
    assert second == "skipped:same-hash"
    assert len(sender.calls) == 1  # not called again


def test_notification_re_sends_when_digest_content_changes(digest_file, notified_state):
    """Same date, new items appended (e.g., manual mid-day re-run captured a floor
    notice) — send again. This is the "Later run" append case from digest.py."""
    sender = RecordingSender()
    maybe_notify(
        digest_path=digest_file,
        has_new_content=True,
        notified_state_path=notified_state,
        sender=sender,
    )
    # Simulate a later same-day run appending new content:
    digest_file.write_text(digest_file.read_text() + "\n\n## Later run\n\n(new item)\n")
    status = maybe_notify(
        digest_path=digest_file,
        has_new_content=True,
        notified_state_path=notified_state,
        sender=sender,
    )
    assert status == "sent"
    assert len(sender.calls) == 2
    assert "Later run" in sender.calls[1][0]


def test_next_day_digest_sends_independently(tmp_path, notified_state):
    """Different digest filename → different key; a stale yesterday-entry must
    not suppress today's send."""
    d = tmp_path / "digests"
    d.mkdir()
    yesterday = d / "20260816.md"
    yesterday.write_text("# yesterday\n\n## X\n\n- item\n")
    today = d / "20260817.md"
    today.write_text("# today\n\n## X\n\n- item\n")
    sender = RecordingSender()
    maybe_notify(
        digest_path=yesterday,
        has_new_content=True,
        notified_state_path=notified_state,
        sender=sender,
    )
    status = maybe_notify(
        digest_path=today,
        has_new_content=True,
        notified_state_path=notified_state,
        sender=sender,
    )
    assert status == "sent"
    assert len(sender.calls) == 2
    state = json.loads(notified_state.read_text())
    assert "20260816.md" in state
    assert "20260817.md" in state


def test_subject_uses_configurable_prefix(digest_file, notified_state):
    sender = RecordingSender()
    maybe_notify(
        digest_path=digest_file,
        has_new_content=True,
        notified_state_path=notified_state,
        sender=sender,
        subject_prefix="[my-prefix]",
    )
    _, subject = sender.calls[0]
    assert subject.startswith("[my-prefix]")


# ------------------ env → sender wiring ------------------


def test_smtp_sender_from_env_returns_none_when_config_incomplete():
    """Missing any required var → notifications disabled; the CLI must degrade
    gracefully rather than crash on a fresh install."""
    assert smtp_sender_from_env(env={}) is None
    assert (
        smtp_sender_from_env(
            env={
                "WATCHER_SMTP_HOST": "smtp.gmail.com",
                "WATCHER_SMTP_USERNAME": "a",
                # missing password + from + to
            }
        )
        is None
    )


def test_smtp_sender_from_env_returns_callable_when_complete():
    sender = smtp_sender_from_env(
        env={
            "WATCHER_SMTP_HOST": "smtp.gmail.com",
            "WATCHER_SMTP_USERNAME": "user@example.com",
            "WATCHER_SMTP_PASSWORD": "app-password-value",
            "WATCHER_NOTIFY_FROM": "user@example.com",
            "WATCHER_NOTIFY_TO": "user@example.com",
        }
    )
    assert sender is not None
    assert callable(sender)


# ------------------ state-file resilience ------------------


def test_corrupt_state_file_is_treated_as_empty_not_crash(digest_file, notified_state):
    """If the state file is malformed JSON (e.g., truncated mid-write), the next
    run must recover by treating it as empty rather than refusing to notify."""
    notified_state.write_text("{not valid json")
    sender = RecordingSender()
    status = maybe_notify(
        digest_path=digest_file,
        has_new_content=True,
        notified_state_path=notified_state,
        sender=sender,
    )
    assert status == "sent"
    assert json.loads(notified_state.read_text())  # rewritten as valid JSON


def test_state_directory_is_created_if_missing(digest_file, tmp_path):
    """First-ever run: data/ exists but the file path parent doesn't yet."""
    notified_state = tmp_path / "nested" / "dir" / "watcher-notified.json"
    sender = RecordingSender()
    status = maybe_notify(
        digest_path=digest_file,
        has_new_content=True,
        notified_state_path=notified_state,
        sender=sender,
    )
    assert status == "sent"
    assert notified_state.exists()
