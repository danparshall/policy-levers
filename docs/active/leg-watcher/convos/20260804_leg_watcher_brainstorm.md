# Leg-Watcher Brainstorm

**Date:** 2026-08-04
**Branch:** leg-watcher
**Machine:** Dans-MacBook-Air

## Summary

Kickoff session for the `leg-watcher` research line, working from [issue #3](https://github.com/danparshall/policy-levers/issues/3) ("build legislative watcher — bills, drafts, markups, floor", filed 2026-07-18). The motivating failure is documented in the ticket: GAAIA was a discussion draft (never on congress.gov) discovered ~1 month late, while H.R. 9363's markup and suspension-calendar timing were publicly visible in advance through feeds we weren't watching. Goal: the next GAAIA costs a day, not a month.

We ran the brainstorming skill over the ticket's v1 scope. Dan expanded scope beyond the ticket's House-centric five components to include Senate depth (the ticket predates the FRONTIER Act ingest and the current Senate-relevance of the landscape). Three architectures were compared (config-driven source-registry pipeline / ticket-literal component scripts / thin glue over external alerting); Dan chose the source-registry pipeline. Design was presented in five sections (layout+flow, Item model+adapters, state+idempotence, scoring+digest, testing+backtest); Dan validated sections 1–3 explicitly and deferred remaining details ("I'm gonna defer to you on the details here") from section 4 onward.

Outcome: implementation plan written for execution by a fresh agent (Dan: "create the plan first and then fresh agent will execute").

## Topics Explored

- Scope refresh vs the 7/18 ticket: FRONTIER Act (7/24) postdates it; keyword set and tracked-bills list stale
- Senate surfaces: committee press/hearings pollability vs individual-office fetch-and-diff cost vs floor-signal yield (UC/hotline largely invisible to public feeds)
- Run model: manual vs scheduled cloud routine vs manual-but-cron-ready
- Intelligence layer: deterministic keywords vs LLM triage vs hybrid
- Architecture alternatives and the shared fetch→diff→score primitive (echo of the 7/31 hackathon "shared engine" observation)

## Provisional Findings

- Most of the watcher's sources reduce to four adapter shapes (congress.gov API, RSS, HTML-diff of press pages, structured scrapes of docs.house.gov/floor pages) — so breadth is config rows, not code
- Senate floor signals are structurally low-yield for AI bills (no suspension-calendar analog; UC/hotline invisible until done); included in v1 anyway per Dan's call after explicit pushback
- The press-feed (HTML-diff) layer is the only discussion-draft catcher in the architecture — the GAAIA failure mode lives there, not in the API poller

## Decisions Made

- **Scope (expanded from ticket):** ticket's five House components + Senate Commerce press & hearing notices + HSGAC + targeted senator press feeds (4–6 named offices) + Senate floor signals
- **Architecture:** source-registry pipeline — normalized `Item` model, four adapter types, `sources.yaml` registry, shared state/scorer/digest
- **Run model:** manual/session-start invocation, but cron-ready (idempotent, non-interactive) so a scheduled routine is a later flip
- **Scoring:** deterministic keywords in v1 (reproducible, free, testable); LLM triage deferred to v2
- **Reminder #5** (FRONTIER outreach, fired 7/25): skipped again this session
- Plan: [`plans/20260804_leg_watcher_v1_plan.md`](../plans/20260804_leg_watcher_v1_plan.md)

## Results

- None (design session; the plan doc is the artifact)

## Session continuation: RED phase (same day)

After plan approval, Dan asked this session to write the tests ("fresh agent will execute"
became "fresh agent executes GREEN"). Completed per the TDD skill:

- **Phase 0 shipped** (commit `500b09f`): `.python-version` (3.12), `pyproject.toml` (uv,
  hatchling, `watcher` CLI entry point), venv, package skeleton, harness test green.
- **RED suite shipped** (commit `86482cf`): 60 failing tests across
  models/config/state/scoring/digest/orchestrator/adapters + `test_backtest_june2026.py`
  (the issue-#3 acceptance criterion). Fixtures: 1 real capture
  (docs.house.gov SY00 meeting feed — schema authority, includes a genuine markup item),
  8 constructed + provenance-flagged in `tests/fixtures/README.md`.
- **Quality-review subagent finding (important):** the scoring tests and backtest were
  jointly unsatisfiable — a zero-keyword "Full Committee Markup" would have been
  threshold-suppressed. Resolution pinned as new contract: event kinds
  (markup/floor/hearing) bypass the score threshold. Also added: tracked-bill matching
  via bill-id-in-uid, `{"bill":{...}}` detail-endpoint parse path, malformed-input
  tests for all four adapters, digest wall-clock leak guard.
- **Plan amended in place** to match pinned contracts (guid-derived uids for meeting items,
  state simplified to seen-UIDs + failure counts [no snapshots], triage rules).
- **RED verified:** pytest fails on `ModuleNotFoundError: watcher.models` (the missing
  feature); ruff + byte-compile clean, so failures are not test defects.
- Fixture-capture recon: house.gov member/committee press pages serve JS shells to curl —
  live selector capture requires a browser-grade fetch at Phase 8; docs.house.gov
  `RSS.ashx?Code=SY00`/`IF00` works headlessly and is the reliable structured surface.

**Handoff to the executing agent:** work in `~/code/policy-levers-leg-watcher` (do NOT
create a new worktree); follow `docs/active/leg-watcher/plans/20260804_leg_watcher_v1_plan.md`
from Phase 1, making the committed RED suite pass phase by phase; the June-2026 backtest
is the finish line. Blockers only at Phase 8: congress.gov API key + Dan's senator list.

## Open Questions

- Which 4–6 senator press feeds seed the targeted list (Rounds, Heinrich, Young, Alsobrooks are candidates from Hill-day contacts; not yet chosen)
- Whether digest commits should land on main or the branch once the tool runs regularly (deferred until it runs)
- Issue #3's title uses the pre-convention `TASK [remind ...]` prefix — normalize or strip once work is underway
- Whether state should eventually be committed for cross-machine continuity (deliberately deferred; single-machine v1)
- `data/` symlink deferred: main's `data/raw`+`data/processed` are empty scaffolding (`.gitkeep` only), and symlinking would dirty git status against the tracked `.gitkeep`s; revisit if this line starts producing checkpoints
