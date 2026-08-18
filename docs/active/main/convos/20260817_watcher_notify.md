# Watcher Notify — Email push for new digest content

**Date:** 2026-08-17
**Branch:** main
**Machine:** Dans-MacBook-Air

## Summary

Session started as a health check on the leg-watcher merge from 2026-08-11: had
the daily launchd job actually produced anything? Answer yes — three digests
landed (Sat 8/15, Sun 8/16, Mon 8/17), all sources healthy (`consecutive_failures=0`
across 18 sources, 215 UIDs seen in the API poller). But the digests are
essentially empty — 8/15 caught one time-critical item (the Aug 17 pro forma
notice) with 5 items suppressed; 8/16 and 8/17 both show 0 items / 0 suppressed.
The one thing surfaced was exactly what senate-daily-schedule was enabled to
catch, so the tool is doing its job — recess week is just quiet, and 2 of the 3
days were weekend.

Real-content evaluation deferred until after Congress returns from recess (~Sep 2).

Dan then asked the load-bearing question the v1 shape never answered: "if
something *does* show up, how do I actually see it?" Traced the pipeline —
launchd → `uv run watcher` → writes `digests/YYYYMMDD.md` → done. No email, no
notification, `digests/` is gitignored so it doesn't even propagate to Pro or
tarragon. The tool is fundamentally pull-shaped for a use case that's push-shaped.

Built the push: `src/watcher/notify.py` — opt-in Gmail SMTP after each run,
gated on has-new-content, idempotent per Dan's explicit ask ("if I *do* get a
digest message, I don't want it a second time"). Shipped as PR #12 (`28b23ab`),
merged same session. To activate, Dan adds five `WATCHER_SMTP_*` /
`WATCHER_NOTIFY_*` vars to `.env.local` — the next 7:03am launchd run picks
them up automatically. First-install without the vars = graceful degrade, CLI
logs `notify: skipped:no-config`, digest still writes.

## Topics Explored

- Health of the 2026-08-15/16/17 digest runs — per-source failure counts,
  seen-UID growth, whether "0 items, 0 suppressed" indicates quiet or broken.
- Whether the launchd → digest-file flow has any push component (it doesn't).
- Notification transport tradeoffs — macOS Notification Center vs `open`-file
  vs email vs Slack vs GitHub Issue vs private-branch commit. Ranked by
  reach × complexity × phone-accessibility.
- How to key notification idempotency when `write_digest` supports mid-day
  appends ("Later run" sections) — content-hash keyed on
  `(digest_filename, sha256(text))` beats date-only.
- Where to store SMTP credentials given the Gmail-app-password requirement
  (verdict: `.env.local`, already gitignored + symlinked into worktrees).

## Provisional Findings

- **Watcher pipeline is healthy but silent.** launchd fires reliably at 7:03am,
  all 18 sources report `consecutive_failures=0`, digest files land on disk.
  What's absent is any signal path to the user — the tool is fundamentally
  pull-shaped ("Dan remembers to `cat digests/YYYYMMDD.md`") for a use case
  that's push-shaped ("catch time-critical Hill action with lead time").
- **Recess-week emptiness is real, not broken.** The 8/15 digest correctly
  surfaced the 8/17 pro forma notice 2 days ahead — exactly what
  senate-daily-schedule was enabled for. The 8/16 and 8/17 "0 items /
  0 suppressed" digests reflect genuine weekend/Monday-morning-of-recess
  silence; the sources returned nothing new because nothing was posted.
  Real signal test defers to ~Sep 2 when Congress returns.
- **Multi-machine problem is real but not blocking.** The launchd plist is
  installed only on the Air; if the Air is closed on a Tuesday, no digest for
  Tuesday (launchd's wake-catchup helps if the Air wakes before Wed 7:03).
  Notification path solves the "how do I see it when it fires" question,
  not the "what if the Air doesn't fire" question. Deferred.
- **Content-hash idempotency is right for this shape.** Date-only keying would
  suppress legitimate re-notification when a mid-day re-run appends new
  content via `write_digest`'s "Later run" mechanism. Content-hash keying
  handles both cases correctly: identical content = skip, appended new items =
  re-send with the full updated digest.

## Decisions Made

- **Ship email as the transport**, not `open`-file / Notification Center /
  Slack / GH Issue. Reasoning: reaches Dan anywhere (phone), one-way (no
  interactive dependency), Gmail SMTP is minimum-viable infra, works with
  existing `.env.local` credential convention.
- **Opt-in via env vars, not always-on.** Notification is off by default
  because a fresh clone shouldn't spam email until Dan explicitly configures.
  Missing any of the 5 required vars = `sender_from_env` returns None =
  `notify: skipped:no-config` in the log, digest still written.
- **`run_watcher` return type change** from `Path` to
  `RunResult(digest_path, has_new_content)`. Named-tuple, backward-compatible
  via two `.digest_path` unwraps in test helpers. Beats re-parsing the
  rendered digest to guess whether it had content.
- **Notify failure never kills the cron run.** Try/except in `main()` around
  `maybe_notify`, logs to stderr on any exception. Digest is already written
  by the time notify runs, and `notified.json` is not touched on failure —
  next run naturally retries.
- **Fixed the .worktrees/ convention.** STATUS 2026-08-04 noted the
  sibling-worktree placement as a deferred fix; this session created the
  first nested `.worktrees/` per the using-git-worktrees skill and added
  `.worktrees/` + `data/watcher-notified.json` to `.gitignore` (commit
  `0a6db9c`).

## Results

- **PR #12** — <https://github.com/danparshall/policy-levers/pull/12> — merged
  as `28b23ab` (merge commit) with `71c8699` (feature commit) underneath.
- **New module**: `src/watcher/notify.py` (166 LoC).
- **New tests**: `tests/test_notify.py` (12 tests). Total 108/108 green
  (was 96), ruff check + format clean.
- **CLI additions**: `--no-notify`, `--notified-state-path`. Documented in
  `src/watcher/README.md` under new "Email notifications" section.
- **Follow-up commit**: `0a6db9c` chore(gitignore) — `.worktrees/` +
  `data/watcher-notified.json`.

No files in `results/` — the artefact is the shipped code, not analysis output.

## Open Questions

- **Real send not yet tested.** Needs Dan to generate a Gmail app password at
  <https://myaccount.google.com/apppasswords> and add five vars to `.env.local`.
  Smoke plan: `uv run watcher --include-backlog 30 --sources rep-trahan-press`
  (a source with guaranteed content) → verify email arrives → re-run →
  verify `notify: skipped:same-hash`.
- **Notification body format.** Current design mails the full digest text as
  plaintext. Considered: (a) subject line with item counts for at-a-glance
  triage (`[leg-watcher] 20260817 — 3 items`), (b) HTML formatting. Both are
  nice-to-haves; deferred until the tool has produced enough real signal to
  know what's actually annoying in the inbox.
- **Multi-machine redundancy.** If the Air is closed, no digest for that day.
  Options considered but deferred: install launchd on tarragon too (need to
  decide canonical state.json), commit digests to a private-branch (loses
  real-time push).
- **Issue #7** `[2026-08-18]` keyword retune fires today (2026-08-18). Skill
  recommendation is to snooze it to ~2026-09-09 since we haven't had a real
  week of digest signal yet (all quiet recess). Dan's call.
- **Fired reminder #5** (FRONTIER outreach) untouched — Dan's call to
  close/snooze.
