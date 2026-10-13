"""Orchestrator: fetch → triage → digest → state save (plan Phase 6).

Failure isolation: a source that raises SourceError degrades the digest (its failure
count ticks up) but never kills the run. Loss-proof ordering: state save happens
AFTER the digest is written on disk, so a crash mid-digest re-surfaces the items
on the next run rather than silently losing them.

`run_watcher` accepts a list of Source protocol objects (anything with `.id` and
`.fetch() -> list[Item]`); real Sources are wired up in Phase 8 by pairing an
adapter parse function with a fetch helper.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import TYPE_CHECKING, NamedTuple

from watcher.digest import STALE_THRESHOLD, render, write_digest
from watcher.models import SourceError
from watcher.scoring import triage
from watcher.state import State

if TYPE_CHECKING:
    from watcher.config import Keywords

log = logging.getLogger(__name__)

# src/watcher/run.py -> src/watcher -> src -> repo root. Env files are anchored
# here rather than CWD so a scheduler invoking with a different working directory
# still finds the API key instead of silently 401-ing every congress_api row.
REPO_ROOT = Path(__file__).resolve().parents[2]


def load_env_files(root: str | Path) -> None:
    """Load `.env.local` then `.env` from `root` into os.environ (first wins)."""
    from dotenv import load_dotenv

    root = Path(root)
    load_dotenv(root / ".env.local")
    load_dotenv(root / ".env")


class RunResult(NamedTuple):
    """Return value from run_watcher.

    `has_new_content` tells downstream steps (notify) whether the digest write
    surfaced anything actionable this run — True iff pinned, scored, or health
    warnings were present. False = the digest is either brand-new-empty or
    unchanged since the last write.

    `stale_sources` lists source ids at or past STALE_THRESHOLD consecutive
    failures, so the CLI can escalate selector drift to the cron log / exit code.
    """

    digest_path: Path
    has_new_content: bool
    stale_sources: list[str]


def _digest_filename(today: str) -> str:
    return today.replace("-", "") + ".md"


def run_watcher(
    *,
    sources: list,
    state_path: str | Path,
    digest_dir: str | Path,
    keywords: Keywords,
    today: str,
    include_backlog_days: int = 30,
) -> RunResult:
    state = State.load(state_path)

    good_fetches: list[tuple[object, list]] = []
    health: list[tuple[str, int]] = []
    all_new: list = []

    for source in sources:
        if not getattr(source, "enabled", True):
            continue
        try:
            items = source.fetch()
        except SourceError as exc:
            log.warning("%s: fetch failed (%s)", source.id, exc)
            failures = state.record_failure(source.id)
            health.append((source.id, failures))
            continue
        except Exception:
            # Belt over the SourceError braces: an adapter bug (KeyError, bs4 quirk)
            # must degrade one source, not kill the digest for all of them.
            log.exception("%s: adapter raised unexpectedly; treating as a failed fetch", source.id)
            failures = state.record_failure(source.id)
            health.append((source.id, failures))
            continue
        good_fetches.append((source, items))
        all_new.extend(
            state.new_items(
                source.id,
                items,
                today=today,
                include_backlog_days=include_backlog_days,
            )
        )

    triaged = triage(all_new, keywords)

    text = render(
        date=today,
        pinned=triaged.pinned,
        scored=triaged.listed,
        health=health,
        suppressed_count=triaged.suppressed_count,
    )

    digest_dir = Path(digest_dir)
    digest_dir.mkdir(parents=True, exist_ok=True)
    digest_path = digest_dir / _digest_filename(today)

    has_new_content = bool(triaged.pinned or triaged.listed or health)
    if has_new_content or not digest_path.exists():
        write_digest(digest_path, text)

    # State save is intentionally LAST — a crash in write_digest above must leave
    # state untouched so the items re-surface on the next run.
    for source, items in good_fetches:
        state.record_success(source.id, items)
    state.save(state_path)

    stale = [sid for sid, failures in health if failures >= STALE_THRESHOLD]
    return RunResult(digest_path=digest_path, has_new_content=has_new_content, stale_sources=stale)


def main() -> None:  # pragma: no cover — thin CLI over run_watcher
    """CLI entry: `uv run watcher [--include-backlog N] [--sources id1,id2] [--dry-run]`.

    Loads config from ./config/{sources,keywords}.yaml (relative to CWD), pulls
    CONGRESS_API_KEY from .env.local, wires live sources, and writes today's digest
    to ./digests/YYYYMMDD.md. Everything upstream of that is unit-tested with fakes.
    """
    import argparse
    import os
    import sys
    from datetime import date as _date
    from pathlib import Path

    from watcher.config import load_keywords, load_sources
    from watcher.sources import build_sources

    # Adapter/orchestrator warnings (skipped entries, rate limits, unexpected
    # exceptions) go to stderr so the cron log carries them.
    logging.basicConfig(level=logging.WARNING, stream=sys.stderr, format="watcher: %(message)s")

    parser = argparse.ArgumentParser(prog="watcher", description=__doc__)
    parser.add_argument(
        "--include-backlog",
        type=int,
        default=1,
        metavar="N",
        help="On a source's first run, surface items dated within the last N days "
        "(default 1 — daily cron mode). Bump for smoke runs.",
    )
    parser.add_argument(
        "--sources",
        type=str,
        default="",
        help="Comma-separated source ids to include (default: all enabled).",
    )
    parser.add_argument(
        "--config-dir",
        type=Path,
        default=Path("config"),
        help="Directory containing sources.yaml and keywords.yaml (default: ./config).",
    )
    parser.add_argument(
        "--state-path",
        type=Path,
        default=Path("data/watcher-state/state.json"),
        help="State file location (default: ./data/watcher-state/state.json).",
    )
    parser.add_argument(
        "--digest-dir",
        type=Path,
        default=Path("digests"),
        help="Where to write daily digest files (default: ./digests).",
    )
    parser.add_argument(
        "--notified-state-path",
        type=Path,
        default=Path("data/watcher-notified.json"),
        help="Notification bookkeeping (which digests we've emailed) "
        "(default: ./data/watcher-notified.json).",
    )
    parser.add_argument(
        "--no-notify",
        action="store_true",
        help="Skip the email step even if SMTP env vars are set. Useful for smoke runs.",
    )
    parser.add_argument(
        "--today",
        type=str,
        default=None,
        help="Override today's date (ISO YYYY-MM-DD); useful for backtest runs.",
    )
    parser.add_argument(
        "--env-dir",
        type=Path,
        default=REPO_ROOT,
        help="Directory holding .env.local / .env (default: the repo root, not CWD).",
    )
    parser.add_argument(
        "--fail-if-stale",
        action="store_true",
        help="Exit 2 after the run if any source has reached the STALE failure threshold "
        "(selector drift escalation for cron). The digest and notification still happen.",
    )
    args = parser.parse_args()

    # .env.local is Dan's convention (see plan Prerequisites #1). Fall back to .env
    # for CI or other environments.
    load_env_files(args.env_dir)
    api_key = os.environ.get("CONGRESS_API_KEY", "")

    source_cfgs = load_sources(args.config_dir / "sources.yaml")
    keywords = load_keywords(args.config_dir / "keywords.yaml")

    today = args.today or _date.today().isoformat()  # noqa: DTZ011 — US-Eastern-day is fine
    if args.sources:
        wanted = {s.strip() for s in args.sources.split(",") if s.strip()}
        source_cfgs = [c for c in source_cfgs if c.id in wanted]
        if not source_cfgs:
            parser.error(f"--sources filter matched nothing: {sorted(wanted)!r}")

    if not api_key and any(c.type == "congress_api" and c.enabled for c in source_cfgs):
        parser.error(
            "CONGRESS_API_KEY not set (checked .env.local, .env, environment). "
            "Either add the key or pass --sources to exclude congress_api rows."
        )

    sources = build_sources(
        source_cfgs,
        keywords=keywords,
        api_key=api_key,
        today=today,
        backlog_days=args.include_backlog,
    )

    result = run_watcher(
        sources=sources,
        state_path=args.state_path,
        digest_dir=args.digest_dir,
        keywords=keywords,
        today=today,
        include_backlog_days=args.include_backlog,
    )
    print(f"wrote {result.digest_path}")
    if result.stale_sources:
        print(f"STALE sources: {', '.join(result.stale_sources)}", file=sys.stderr)

    from watcher.notify import maybe_notify, smtp_sender_from_env

    sender = None if args.no_notify else smtp_sender_from_env()
    try:
        status = maybe_notify(
            digest_path=result.digest_path,
            has_new_content=result.has_new_content,
            notified_state_path=args.notified_state_path,
            sender=sender,
        )
    except Exception as exc:  # noqa: BLE001 — never let SMTP failures kill the cron run
        # A dead relay or auth glitch must not lose today's digest work. Log to
        # the cron log via stderr; STATE was already saved (line above), so the
        # next run will re-attempt notification with the same content-hash key
        # (idempotency still protects duplicates).
        print(f"notify: FAILED ({type(exc).__name__}: {exc})", file=sys.stderr)
    else:
        print(f"notify: {status}")

    if args.fail_if_stale and result.stale_sources:
        sys.exit(2)
