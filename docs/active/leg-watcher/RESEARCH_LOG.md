# RESEARCH_LOG — leg-watcher

Branch: `leg-watcher` (worktree: `~/code/policy-levers-leg-watcher`)
Originating ticket: [issue #3](https://github.com/danparshall/policy-levers/issues/3) — build legislative watcher (bills, drafts, markups, floor)

Goal: the next GAAIA costs a day, not a month. GAAIA was a discussion draft (never on congress.gov) discovered ~1 month late; H.R. 9363's markup and suspension-calendar timing were publicly visible in advance through feeds we weren't watching.

## Sessions (newest first)

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
