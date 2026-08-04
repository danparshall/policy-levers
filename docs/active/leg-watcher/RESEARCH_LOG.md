# RESEARCH_LOG — leg-watcher

Branch: `leg-watcher` (worktree: `~/code/policy-levers-leg-watcher`)
Originating ticket: [issue #3](https://github.com/danparshall/policy-levers/issues/3) — build legislative watcher (bills, drafts, markups, floor)

Goal: the next GAAIA costs a day, not a month. GAAIA was a discussion draft (never on congress.gov) discovered ~1 month late; H.R. 9363's markup and suspension-calendar timing were publicly visible in advance through feeds we weren't watching.

## Sessions (newest first)

## Session: 2026-08-04 — leg_watcher_green_execution

### Topics Explored
- Fresh-agent GREEN execution of the plan Phases 1–7 against the committed RED suite
- Two contract details underdetermined by tests, decided in place (see convo)
- Ruff sweep on new code

### Provisional Findings
- Plan's RED suite was internally consistent — no test rewrites needed
- `kind_boost` is a relevance amplifier (only added when keyword_score > 0), not a base score — required by `test_short_allcaps_term_requires_word_boundary`
- Orchestrator skips `write_digest` on empty-content re-runs iff the digest file already exists — gives byte-equal same-day repeats while still writing a readable file on the empty-baseline first run
- `date.fromisoformat` cleaner than `datetime.strptime` for the `today` sanity check (dodges DTZ007 without a `# noqa`)

### Results
- Six commits on `leg-watcher` (all pushed): Phase 1 `c63b973` → Phase 2 `df2a0e6` → Phase 3 `b1ef37c` → Phase 4 `35fad1e` → Phase 5 `9268f68` → Phase 6+7 `97d716e`
- **75/75 tests pass, `ruff check src/watcher tests` clean**
- Backtest (issue #3 acceptance criterion) passes: GAAIA press item release-day, H.R. 9363 intro, 6/25 Science markup in advance, tracked items pinned, day-after run quiet
- Full convo: `convos/20260804_leg_watcher_green_execution.md`

### Next Steps
- **Phase 8** (blocked on Dan): congress.gov API key + 4–6 senator office picks; then populate `config/sources.yaml`, write `src/watcher/README.md`, do the live smoke run, and replace constructed fixtures with real captures per `tests/fixtures/README.md`
- Reminder #5 (FRONTIER outreach) still open — untouched this session

## Session: 2026-08-04 — leg_watcher_brainstorm

### Topics Explored
- Brainstormed v1 design from issue #3's scope; expanded to Senate depth (Commerce + HSGAC + targeted senator feeds + floor signals)
- Compared three architectures; chose config-driven source-registry pipeline (Item model, 4 adapter types, sources.yaml)
- Settled run model (manual, cron-ready) and scoring (deterministic keywords v1; LLM triage deferred)

### Provisional Findings
- Four adapter shapes cover all ~25 sources → breadth is config, not code
- HTML-diff press layer is the only discussion-draft catcher (the GAAIA failure mode); Senate floor signals low-yield but included per Dan
- Full detail: `convos/20260804_leg_watcher_brainstorm.md`

### Results
- Implementation plan: `plans/20260804_leg_watcher_v1_plan.md` (amended in place after RED-phase review)
- Phase 0 scaffolding (commit `500b09f`): Python 3.12 + uv + `watcher` package skeleton
- RED test suite (commit `86482cf`): 60 failing tests incl. the June-2026 backtest; fixtures with provenance README (1 real docs.house.gov capture, 8 constructed/flagged)
- New contracts pinned by review: event kinds bypass score threshold; tracked matching via bill-id-in-uid; state = seen-UIDs + failure counts (no snapshots)

### Next Steps
- Fresh agent: GREEN phases 1–8 in this worktree against the committed RED suite (backtest = finish line)
- Dan: congress.gov API key; pick the 4–6 senator press feeds (Phase 8 blockers only)
