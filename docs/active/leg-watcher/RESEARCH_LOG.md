# RESEARCH_LOG — leg-watcher

Branch: `leg-watcher` (worktree: `~/code/policy-levers-leg-watcher`)
Originating ticket: [issue #3](https://github.com/danparshall/policy-levers/issues/3) — build legislative watcher (bills, drafts, markups, floor)

Goal: the next GAAIA costs a day, not a month. GAAIA was a discussion draft (never on congress.gov) discovered ~1 month late; H.R. 9363's markup and suspension-calendar timing were publicly visible in advance through feeds we weren't watching.

## Sessions (newest first)

## Session: 2026-08-04 — ai_legislator_research

### Topics Explored
- Pivoted from Phase 8 execution to research on which senators / reps / committees the watcher should be tuned to (the natural upstream of the "Senate-member rows placeholder-disabled" Phase 8 TODO)
- General-purpose research subagent, grounded in Dan's current tracking + the press-page-first "watchable" criterion
- Verified the Peters ambiguity against local `bills/` artifacts
- `.env.local` setup (canonical file in main worktree, symlinked into worktree, mirrored to `~/xfer/envs/` via `collect_envs.py`) — plan doc updated from `.env` → `.env.local` (commit `82c3dd3`)
- Worktree location convention — leg-watcher worktree lives at sibling path `~/code/policy-levers-leg-watcher/` instead of `<repo>/.worktrees/leg-watcher/` per the skill, which caused `collect_envs.py` to mirror it as a separate repo

### Provisional Findings
- **Warner (D-VA)** and **Blackburn (R-TN)** are the two biggest additions Dan is not currently tracking. Blackburn released a comprehensive AI framework as a press-page discussion draft in March 2026 — the exact GAAIA failure mode.
- **Curtis (R-UT)** freshman with three AI bills already; **Hawley (R-MO)** runs a high-volume AI press page.
- **FRONTIER Act = H.R. 9925** (Obernolte press release surfaced by the research; closes the tracked-bills TODO in `config/sources.yaml`).
- **"Peters" as GAAIA / FRONTIER cosponsor = Rep. Scott Peters (D-CA-50)** — verified against local `bills/frontier-act/README.md`, both press releases, and `bills/obernolte-trahan/README.md`. Gary Peters (D-MI) is Senate HSGAC ranking — separate person.
- Obernolte chairs Science's Research & Technology *subcommittee*, not the full committee (Babin holds the gavel). Dan's STATUS.md is internally inconsistent on this and worth a cleanup pass at merge.
- Worktree misplacement (sibling vs nested) is a prior-session mistake; safe to defer the fix until branch merges and the worktree gets cleaned up.

### Results
- `results/20260804_ai_legislators_shortlist.md` — punch list with per-senator rationale + press URLs + committee tiering + sources, ready to consume as the Phase 8 config-population reference.
- Dan-directed Senate watch list finalized to **8 rows**: Warner, Blackburn, Cruz, Curtis, Hawley, Rounds, Schumer, Gary Peters (annoying-but-important kept alongside high-signal drafters; some to run at lower priority in `enabled`/scoring terms).
- Todd Young demoted to committee-feed-only coverage.
- `.env.local` setup in place (key already pasted by Dan pre-session in `~/code/policy-levers/.env.local`; symlinked to worktree; mirrored to `~/xfer/envs/policy-levers/`).
- Full convo: `convos/20260804_ai_legislator_research.md`

### Next Steps
- Fired reminders #3 (leg-watcher build) and #5 (FRONTIER outreach) pending Dan's close/snooze/skip decision.
- Phase 8 execution (config/sources.yaml population, README, live smoke) — resumeable now (picks grounded, API key in place, FRONTIER bill number = H.R. 9925 known).
- Optional: patch `collect_envs.py` to skip git worktrees (dedupe by `Path.resolve()` or check `.git` file vs. dir) — prevents this class of issue for future worktrees.
- Doc-hygiene cleanup at merge: Obernolte subcommittee-vs-full-committee framing; Peters ambiguity across STATUS.md sessions.

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
