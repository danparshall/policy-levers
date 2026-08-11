# RESEARCH_LOG — leg-watcher

Branch: `leg-watcher` (worktree: `~/code/policy-levers-leg-watcher`)
Originating ticket: [issue #3](https://github.com/danparshall/policy-levers/issues/3) — build legislative watcher (bills, drafts, markups, floor)

Goal: the next GAAIA costs a day, not a month. GAAIA was a discussion draft (never on congress.gov) discovered ~1 month late; H.R. 9363's markup and suspension-calendar timing were publicly visible in advance through feeds we weren't watching.

## Sessions (newest first)

## Session: 2026-08-11 — leg_watcher_finish_dev_branch

### Topics Explored
- Pre-merge review pass on the leg-watcher branch (Dan's call after prior session left the merge decision with him). Ran the `finishing-a-development-branch` skill: pytest, ruff format, ruff check, `nori-code-reviewer` + test-hygiene agent, then triage and PR.

### Provisional Findings
- **`ruff format` had never been run on this branch** — prior sessions ran `ruff check` (lint) only. Applying `ruff format` produced 15 mechanical Black-style reflows, no behavior change. Now committed and clean.
- Three real bugs the tests didn't catch, all narrow: (a) broken f-string in `build_sources` bad-mode error (`sources.py:274-275`); (b) `resp.json()` unwrapped in `CongressApiTrackedSource.fetch` (`sources.py:151-165`) — one non-JSON detail response would kill the whole tracked-bills fetch; (c) dead keyword `"third-party evaluat"` in `keywords.yaml:77` (`\b` anchors can't fire mid-word). All fixed and pinned by regression tests in `tests/test_sources.py`.
- Larger reliability + coverage gaps found (per-item failures killing sources, HTTP retry/rate-limit discipline, unbounded `seen_uids`, atomic digest write, sources.py HTTP-layer untested, corrupted-state.json untested, `parse_bill_detail` malformed-payload untested, etc.) — real but scope-heavy; filed as issue #9 for a v1.3 pass.

### Results
- 96/96 tests pass (was 93 → +3 regression tests), `ruff check` + `ruff format --check` both clean.
- Commits: `440fa1a` (format sweep) → `2e93d43` (three bug fixes + tests). This finish-convo commit follows.
- Follow-up: **issue #9** batches the un-landed review findings.
- Convo: `convos/20260811_leg_watcher_finish_dev_branch.md`

### Next Steps
- PR to main (this session).
- **Issue #3 close** — the v1.1 delivered on what #3 asked for; this merge is the landing. Closing with a link to the merged PR is the natural move, Dan's call.
- **docs/active/leg-watcher/ archive** — deferred; this was the dev-branch flow, not the research-branch flow. Separate `git mv` when Dan is ready.
- **Doc-hygiene cleanup carried again** — Obernolte subcommittee-vs-full-committee framing; unqualified "Peters" in STATUS.md.

## Session: 2026-08-11 — leg_watcher_v11_press_enable_execution

### Topics Explored
- Executed v1.1 plan Phases 1–4 (`plans/20260811_leg_watcher_v11_press_page_enable.md`): RSS probe across all 22 disabled sources → RSS enables → html_diff selector hunts → floor lookahead. Dan called stop-at-Phase-4; Phases 5–6 deferred to issue #8.
- Watcher went **4 → 18 enabled sources**; full-registry smoke from clean state surfaced Trahan's FRONTIER coalition release (tracked pin), Senate 8/13 pro forma (Time-critical), Hawley [13] / Warner [7] / Rounds [5] AI items, 70 suppressed, zero source-health warnings.

### Provisional Findings
- **Entry counts lie**: the probe scored 11 feeds live, but fixture capture showed 7 were wrong-content (evo-Drupal `/rss.xml` = featured-content/videos/photo-captions, not press; Curtis's feed = one 2022 lorem-ipsum "Test Post"). Only item-level review validates a press feed.
- Six CMS shapes cover 15 of 18 enabled sources (evo-Drupal h3/h5, Senate PageList, Fireside RSS, WordPress RSS, WP/Elementor html, Blackburn bespoke-static); DATE_FORMATS grew 3 → 7 (+ ordinal stripping), all TDD'd on real fixtures.
- Terminal verdicts with evidence in config comments: Scott Peters (JS shell), Curtis + Lofgren (no reliable listing dates), Foushee (flat siblings, no containers), majority-leader (Telerik prose paste; URL had also moved), committee RSS (none exist; HSGAC feed real but recess-empty).
- Schumer caucus-feed floor wrap-ups score below keyword threshold — retune dependency, noted in issue #7.

### Results
- 6 commits `dc63b4c`→`75125f1`, all pushed. 93/93 tests, ruff clean. 11 new REAL fixtures with provenance rows.
- Convo: `convos/20260811_leg_watcher_v11_press_enable_execution.md`
- Issues opened: #7 `[2026-08-18]` keyword retune (Phase 7); #8 v1.2 source gaps + Phases 5–6 pointer.

### Next Steps
- Phase 7 keyword retune after a real week of digests (issue #7 fires 8/18).
- Phases 5–6 (pagination + EmptyFeed) before daily-cron use; pagination becomes urgent when recess ends ~9/1 (issue #8).
- Re-probe HSGAC `/feed/` when Congress returns.
- **Merge decision (plan Q4)**: tool now does what issue #3 promised — close #3 + merge is Dan's call.
- Doc-hygiene cleanup at merge (carried): Obernolte subcommittee framing; unqualified "Peters" in STATUS.md.

## Session: 2026-08-04 — leg_watcher_phase8_execution

### Topics Explored
- Executed Phase 8 against the 2026-08-04 shortlist picks: populated `config/{sources,keywords}.yaml`, wrote `src/watcher/sources.py` with 6 Source classes + HTTP helper, wired `run.py:main()` (argparse CLI + dotenv loading), shipped `src/watcher/README.md`.
- Live smoke run (`uv run watcher --include-backlog 14`) exposed two real production quirks the constructed fixtures never exercised — fixed both with TDD.
- Replaced two constructed fixtures with real congress.gov API captures; also captured a fresh SY00 XML including a real empty-stub item.
- Wayback CDX search for the Trahan press page 2026 snapshots — nothing archived, documented as terminal (not fetchable).

### Provisional Findings
- `docs.house.gov` meeting feeds emit `<item><guid>0</guid><title></title>...</item>` section-separator stubs. `parse_meeting_feed` was raising `SourceError` on the empty description, killing the whole SY00 fetch. New `_is_stub()` guard skips them. Pinned by `test_empty_stub_items_are_skipped`.
- `/v3/bill/{congress}` returns "Reserved for the Speaker." placeholder rows with `latestAction: null`. `parse_bill_list` was raising `SourceError` on the whole fetch. Now skips. Pinned by `test_reserved_for_speaker_placeholder_bills_are_skipped`.
- `_bill_to_item` now falls back to `legislationUrl` (human-facing, detail-endpoint only) when `url` (API-endpoint, list-only) is empty — tracked-bills digest lines now render real `congress.gov/bill/...` URLs instead of empty parens.
- H.R. 9363's real title is "AI Security and Innovation Act" (constructed fixture had a placeholder). Existing test assertions on date + body_excerpt keyword survived the real-fixture swap without rewrite.
- Smoke digest pins H.R. 9925 (FRONTIER Act) via bill-id-in-uid match, surfaces four Science + E&C markups/hearings, and scores K-12 AI Literacy and Readiness Act at 8. Idempotence-check second run predicts keyword noise from broad "workforce"/"innovation" tokens (30 items surfaced from labor/healthcare bills) — expected per plan; retune YAML after a real week.

### Results
- Commit `b20a034` on `leg-watcher` (14 files, +1090/-50): `config/sources.yaml` (new), `config/keywords.yaml` (new), `src/watcher/sources.py` (new), `src/watcher/README.md` (new), `src/watcher/run.py` (real `main()`), 2 adapter fixes, 3 fixture updates + 2 new tests, `.gitignore` adds `digests/`. 77/77 tests pass, ruff clean, pushed.
- Convo: `convos/20260804_leg_watcher_phase8_execution.md`

### Next Steps
- **Plan written 2026-08-11:** `plans/20260811_leg_watcher_v11_press_page_enable.md` — the "make it useful, not just functional" pass. Enables the ~22 disabled press-page rows, floor lookahead, plus two smoke-caught polish items. Live probe overturned the JS-rendering pessimism — Trahan has RSS, Warner + Blackburn are static HTML.
- Reminder #5 (FRONTIER outreach) still open — separate workstream from the leg-watcher build.
- Doc-hygiene cleanup at merge: Obernolte subcommittee-vs-full-committee framing; unqualified "Peters" in GAAIA-cosponsor context.
- Issue #3 (leg-watcher build): Phase 8 satisfied the "build" clause literally; the v1.1 plan is what turns it into the GAAIA-catcher the ticket implied. Close after v1.1 Phase 4 lands.

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
