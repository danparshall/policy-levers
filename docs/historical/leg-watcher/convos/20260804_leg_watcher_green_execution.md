# Leg-Watcher GREEN Execution (Phases 1–7)

**Date:** 2026-08-04
**Branch:** leg-watcher
**Machine:** Dans-MacBook-Air  <!-- fresh agent handoff, same day as the brainstorm/RED session -->

## Summary

Fresh agent picked up the handoff from `20260804_leg_watcher_brainstorm.md` and executed
Phases 1–7 of the implementation plan (`plans/20260804_leg_watcher_v1_plan.md`), turning
the committed RED test suite (60 failing tests from `86482cf`) fully GREEN, phase by
phase, one commit per phase. The June-2026 backtest — issue #3's acceptance criterion —
passes. No fixtures or test contracts were changed to fit the code; two design questions
underdetermined by the tests are called out in Decisions Made below.

Work landed in the existing worktree `~/code/policy-levers-leg-watcher` per handoff
(no new worktree). Six commits pushed to `origin/leg-watcher`: one per phase, plus a
combined Phase 6+7 commit that also swept the remaining ruff warnings in leg-watcher
code. Final state: **75 / 75 tests pass, `ruff check src/watcher tests` clean.**

Phase 8 (source-registry population, live smoke run, `src/watcher/README.md`) was
NOT started — its blockers are external (Dan owes a congress.gov API key and the
4–6 senator office picks) per the plan's Prerequisites section.

## Topics Explored

- Phase-by-phase GREEN implementation against the committed RED suite: `models` +
  `config` → `state` → `scoring` → four `adapters` → `digest` → `run` orchestrator →
  June-2026 backtest.
- Two contract details underdetermined by the tests, decided in place (see below).
- Ruff sweep on new code + one stray import-order fix on `tests/test_digest.py`
  (the only leg-watcher-scoped ruff finding outside my new files).

## Provisional Findings

- The plan's pre-authored RED suite was internally consistent — no test rewrites
  needed once the two "underdetermined" decisions below were made.
- `write_digest`'s append-with-"Later run" contract composes cleanly with the
  orchestrator's "skip write when nothing new" rule to give exact-file-equality
  on same-day re-runs (`test_second_run_same_day_adds_nothing`) while still
  producing a readable digest on the empty-baseline case
  (`test_baseline_without_backlog_digests_nothing_new`).
- `date.fromisoformat` (not `datetime.strptime`) is the right sanity-check for
  the `today` arg in `rss.parse_feed` — sidesteps the DTZ007 ruff warning
  without a `# noqa`.

## Decisions Made

Two contract calls the RED tests underdetermined, decided in place. Both fell out
of trying to make jointly-unsatisfiable-looking assertions pass without changing
the tests:

1. **`kind_boost` is a relevance amplifier, not a base score.** Naïvely adding
   `kind_boost[press]=1` to a zero-keyword-hit press item gives 1 — but
   `test_short_allcaps_term_requires_word_boundary` requires the score to be
   exactly 0 for `"He said aid to Bahrain requires brainstorming"` (kind=press
   default). So `kind_boost` is only added when there is at least one keyword hit;
   a road-renaming press release stays at 0 and can't sneak above threshold on
   kind alone. `test_kind_boost_applied` still passes because it only cares
   about the *difference* between two same-title items of different kinds.

2. **Orchestrator skips `write_digest` on empty-content re-runs iff the digest
   file already exists.** Necessary for `test_second_run_same_day_adds_nothing`
   (byte-equality on repeat), and combined with "still write on first run even
   if empty" it satisfies `test_baseline_without_backlog_digests_nothing_new`
   (`.read_text()` needs the file to exist).

Also confirmed the plan's pinned contracts held cleanly:
- Event kinds bypass the score threshold (from the RED-phase review).
- Tracked-bill matching fires on bill-id-in-uid via `item.uid.split("-")` token
  membership — no false positives from hash uids because the token set for a
  16-hex-char uid is a single token that won't equal `hr9363` / `gaaia` / etc.
- State-save happens AFTER `write_digest` in the orchestrator; the crash-inject
  test verifies items re-surface on the next run.

## Results

- Six commits on `leg-watcher` (all pushed to `origin/leg-watcher`):
  - `c63b973` Phase 1 GREEN: models + config loaders (9/9 pass)
  - `df2a0e6` Phase 2 GREEN: state store (7/7 pass)
  - `b1ef37c` Phase 3 GREEN: keyword scoring + triage (15/15 pass)
  - `35fad1e` Phase 4 GREEN: four adapters (21/21 pass)
  - `9268f68` Phase 5 GREEN: digest render + write (10/10 pass)
  - `97d716e` Phase 6+7 GREEN: orchestrator + backtest (12/12 pass) + ruff sweep
- Backtest specifically (5 tests): GAAIA press item on release day (2026-06-04),
  H.R. 9363 at introduction (2026-06-18), 6/25 Science markup surfaced in
  advance, both tracked items pinned above Time-critical, day-after run quiet.
- Full suite: **75/75 pass, `ruff check src/watcher tests` clean.**

## Open Questions

- **Phase 8 blockers (unchanged from brainstorm handoff):** Dan owes a
  congress.gov API key (`.env: CONGRESS_API_KEY`) and the 4–6 senator office
  picks for the placeholder-disabled rows in `sources.yaml`.
- **Selector reality check** will come at Phase 8 — the constructed fixtures
  (member_press.html, floor_lookahead.html, committee_rss.xml, trahan_press_june2026.html)
  need to be replaced with live captures per the provenance table in
  `tests/fixtures/README.md`. Any assertion-vs-real-payload gaps found then are
  fixture bugs, not code bugs (per the "Rules" note in that README).
- **Reminder #5 (FRONTIER outreach, fired 7/25)** — still open, not touched this
  session; same status as after the brainstorm.
