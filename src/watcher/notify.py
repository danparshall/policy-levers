"""Email notification for new digest content (v1.1 follow-up to leg-watcher v1).

Motivation: the v1 pipeline writes a Markdown file to `digests/` and stops
there. That's a "pull" tool — Dan has to remember to open the file — which is
wrong for a system whose selling point is *lead time on time-critical Hill
events*. This module adds a push: an email is sent iff the digest is
substantive AND we haven't already sent this exact content.

Idempotency is keyed on `(digest_filename, sha256(digest_text))`. Rationale:

- Same date + same content (e.g. launchd fires twice on a wake catch-up, or
  Dan manually re-runs) → skip. The user asked explicitly not to be re-notified
  for the same digest.
- Same date + changed content (write_digest appended a "Later run" section
  because a mid-day re-run picked up a new item) → send again. This IS new
  information the user needs to see.
- Different date → send independently (each day is its own key).

`maybe_notify` returns a status string (`sent` / `skipped:*`) rather than a
bool so the CLI can log a diagnostic in the cron log — silent skips are hard
to debug later. The sender is injected so tests never hit real SMTP.

Env-var contract (see src/watcher/README.md):

  WATCHER_SMTP_HOST         e.g. smtp.gmail.com
  WATCHER_SMTP_PORT         default 587 (STARTTLS)
  WATCHER_SMTP_USERNAME     Gmail address
  WATCHER_SMTP_PASSWORD     Gmail *app password* (not the account password)
  WATCHER_NOTIFY_FROM       envelope From (usually same as username)
  WATCHER_NOTIFY_TO         where the digest goes
  WATCHER_NOTIFY_SUBJECT_PREFIX  optional, default "[leg-watcher]"

If any required var is missing, notifications are disabled — the watcher
continues to write digests, just doesn't email them. This is a first-install
graceful degrade, not a silent failure to catch: `sender_from_env` returns
None and the CLI logs "notify: skipped:no-config" once per run.
"""

from __future__ import annotations

import hashlib
import json
import os
import smtplib
from collections.abc import Callable
from dataclasses import dataclass
from email.message import EmailMessage
from pathlib import Path

Sender = Callable[[str, str], None]  # (body_text, subject) -> None


@dataclass(frozen=True)
class SmtpConfig:
    host: str
    port: int
    username: str
    password: str
    from_addr: str
    to_addr: str


def _smtp_config_from_env(env: dict[str, str] | None) -> SmtpConfig | None:
    e = os.environ if env is None else env
    required = (
        "WATCHER_SMTP_HOST",
        "WATCHER_SMTP_USERNAME",
        "WATCHER_SMTP_PASSWORD",
        "WATCHER_NOTIFY_FROM",
        "WATCHER_NOTIFY_TO",
    )
    if not all(e.get(k) for k in required):
        return None
    return SmtpConfig(
        host=e["WATCHER_SMTP_HOST"],
        port=int(e.get("WATCHER_SMTP_PORT", "587")),
        username=e["WATCHER_SMTP_USERNAME"],
        password=e["WATCHER_SMTP_PASSWORD"],
        from_addr=e["WATCHER_NOTIFY_FROM"],
        to_addr=e["WATCHER_NOTIFY_TO"],
    )


def _send_via_smtp(cfg: SmtpConfig, body: str, subject: str) -> None:  # pragma: no cover
    """Send a text email over SMTP+STARTTLS. Isolated for injection in tests."""
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = cfg.from_addr
    msg["To"] = cfg.to_addr
    msg.set_content(body)
    with smtplib.SMTP(cfg.host, cfg.port, timeout=30) as smtp:
        smtp.starttls()
        smtp.login(cfg.username, cfg.password)
        smtp.send_message(msg)


def smtp_sender_from_env(env: dict[str, str] | None = None) -> Sender | None:
    """Build a Sender bound to Gmail/SMTP credentials in env, or None if incomplete."""
    cfg = _smtp_config_from_env(env)
    if cfg is None:
        return None

    def send(body: str, subject: str) -> None:
        _send_via_smtp(cfg, body, subject)

    return send


def _load_notified(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        loaded = json.loads(path.read_text())
    except json.JSONDecodeError:
        # Corrupt state (e.g. truncated on power-loss mid-write) → recover by
        # treating as empty. The next successful send rewrites the file with
        # valid JSON. Losing the "already-notified" bookkeeping for one run is
        # cheaper than refusing to notify forever.
        return {}
    return loaded if isinstance(loaded, dict) else {}


def _save_notified(path: Path, state: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, sort_keys=True))


def maybe_notify(
    *,
    digest_path: Path,
    has_new_content: bool,
    notified_state_path: Path,
    sender: Sender | None,
    subject_prefix: str = "[leg-watcher]",
) -> str:
    """Send an email iff the digest is substantive and we haven't sent this
    exact content already. Returns a status string for logging.

    Statuses:
      "skipped:no-config"    sender is None (notifications disabled)
      "skipped:no-content"   run had no pinned/scored/health items
      "skipped:no-digest"    digest file missing on disk (defensive)
      "skipped:same-hash"    identical content already notified for this file
      "sent"                 email sent, state updated
    """
    if sender is None:
        return "skipped:no-config"
    if not has_new_content:
        return "skipped:no-content"
    if not digest_path.exists():
        return "skipped:no-digest"

    text = digest_path.read_text()
    content_sha = hashlib.sha256(text.encode("utf-8")).hexdigest()

    notified = _load_notified(notified_state_path)
    key = digest_path.name
    if notified.get(key, {}).get("content_sha256") == content_sha:
        return "skipped:same-hash"

    subject = f"{subject_prefix} {digest_path.stem}"
    sender(text, subject)

    notified[key] = {"content_sha256": content_sha}
    _save_notified(notified_state_path, notified)
    return "sent"
