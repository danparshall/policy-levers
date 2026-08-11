# AI-legislator research (pivot from Phase 8 execution)

**Date:** 2026-08-04
**Branch:** leg-watcher
**Machine:** Dans-MacBook-Air

**Preceding session:** [`20260804_leg_watcher_green_execution.md`](20260804_leg_watcher_green_execution.md) — closed Phases 1–7 GREEN with 75/75 tests passing.
**Handoff-in:** Execute Phase 8 (config population + README + fixture replacement + live smoke).

## Summary

Session opened on a handoff to execute Phase 8 (populate `config/sources.yaml`, write `src/watcher/README.md`, replace constructed fixtures with real captures, live smoke run). Dan pivoted immediately, asking instead for research on **which Senators, Reps, and committees** the watcher should actually be tuned to — the natural upstream question of the "Senate-member rows placeholder-disabled" TODO in the plan. That's the axis of "watchability" the plan left open, and picking blind would compound at every future run.

The bulk of the session was a delegated web-research pass by a general-purpose subagent, grounded in Dan's currently-tracked legislators + the press-page-first "watchable" criterion (the GAAIA failure mode the tool is built to catch). The agent came back with two surprises Dan wasn't tracking (Warner's July 2026 4-bill framework rollout; Blackburn's March 2026 TRUMP AMERICA AI Act as a press-page discussion draft — exact GAAIA failure mode), a freshman signature-issue senator (Curtis), a high-volume press-page contributor (Hawley), and a name-disambiguation catch: "Peters" in the GAAIA/FRONTIER cosponsor context is Rep. **Scott** Peters (D-CA-50), not Sen. **Gary** Peters (D-MI). Both are legitimate to track for different reasons; STATUS.md just needs disambiguation. Also picked up: FRONTIER Act now numbered **H.R. 9925**, closing a tracked-bills TODO.

Dan's decision on the shortlist expanded past the plan's "4–6" figure to 8 senator rows, keeping the "important-even-if-annoying ones" (Cruz as Commerce chair/gatekeeper; Schumer as Minority Leader signal) alongside the high-signal drafters. Todd Young demoted to committee-feed-only. Session then wrapped up practical setup: the congress.gov API key had already been placed in `~/code/policy-levers/.env.local` earlier in the day; I symlinked it into the worktree per Dan's convention, mirrored to `~/xfer/envs/policy-levers/` via `collect_envs.py`, and updated the plan doc from `.env` → `.env.local`. Noted that the mirror also created a duplicate `~/xfer/envs/policy-levers-leg-watcher/` folder because the worktree was created as a sibling of the main repo (`~/code/policy-levers-leg-watcher/`) rather than nested under it (`~/code/policy-levers/.worktrees/leg-watcher/`) per the `using-git-worktrees` skill. Dan diagnosed this as a prior-session mistake; deferred the fix.

## Topics Explored

- The "which offices" upstream question that Phase 8 leaves to Dan
- Press-page-first workflow as the "watchable" criterion (differentiating drafters from talkers)
- Verification of the Peters ambiguity against local `bills/` artifacts
- The Obernolte "Science chair vs subcommittee chair" framing in Dan's notes
- Committee tiering (high / medium / low-hit-rate-but-critical) for the source registry
- `.env.local` convention: canonical file in main worktree, symlinked into worktrees, mirrored to `~/xfer/envs/` via `collect_envs.py`
- Worktree location convention (`.worktrees/<branch>/` inside the repo) and the side-effect when it's not followed

## Provisional Findings

- **Two high-yield senators are missing from Dan's tracking:**
  - **Sen. Mark Warner (D-VA)** rolled out a 4-bill "Framework for America's AI Future" July 21–22, 2026 via press page + Axios exclusive (Data Center Tax Accountability & Disclosure Act, AI AGENT Act, Secure AI Development Act, Safeguarding Against Fabricated Exploitation Act). Also Intel vice-chair.
  - **Sen. Marsha Blackburn (R-TN)** released the TRUMP AMERICA AI Act **as a discussion draft on her press page** March 18–19, 2026 — literally the GAAIA failure mode the tool is designed for. Also NO FAKES co-lead.
- **John Curtis (R-UT)**, freshman senator (Romney seat), has made AI a signature issue (3 bills already: SAFE KIDS Act, AI Labeling Act, CLEAR Act).
- **Josh Hawley (R-MO)** runs a high-volume AI press page (LEAD Act w/ Durbin, Blumenthal-Hawley framework, Warner-Hawley jobs bill, deepfake letters).
- **FRONTIER Act now has a bill number: H.R. 9925** (Obernolte 2026-07-23 press release). Closes the "FRONTIER Act once numbered" TODO in `config/sources.yaml` tracked-bills block.
- **Peters clarification (verified from local bill artifacts):** the "Peters" cited as GAAIA / FRONTIER cosponsor across Dan's notes is **Rep. Scott Peters (D-CA-50)** — verified against `bills/frontier-act/README.md`, `bills/frontier-act/press_release_2026-07-23.html`, `bills/obernolte-trahan/README.md`, and `bills/obernolte-trahan/press_release_2026-06-04.txt`. Gary Peters (D-MI, HSGAC ranking) is a separate person; both are legitimate to track but for different reasons.
- **Framing correction:** Obernolte chairs House Science's Research & Technology *subcommittee*, not the full committee. Babin (R-TX-36) holds the full-committee gavel. STATUS.md 2026-07-18 already references Babin correctly in one place, so Dan's notes are internally inconsistent — cleanup at merge.
- **Worktree location:** the leg-watcher worktree lives at `~/code/policy-levers-leg-watcher/` (sibling of main), which caused `~/xfer/envs/collect_envs.py` to mirror it as if it were a separate repo. The `using-git-worktrees` skill's convention is `<repo-root>/.worktrees/<branch-name>/` — invisible to `~/code/*` iteration.

## Decisions Made

- **Senate watch list expanded to 8 rows** per Dan's preference to keep the "important-even-if-annoying ones (Cruz, Schumer)" alongside the high-signal drafters. Final list: Warner, Blackburn, Cruz, Curtis, Hawley, Rounds, Schumer, Gary Peters. Some rows will run at lower priority — Phase-8 `sources.yaml` will encode this via `enabled` and optional scoring differences per row.
- **Todd Young** demoted to committee-feed-only coverage (his AI content flows through cosponsorship, not his own press page).
- Hold-for-later shortlist (Schiff, Coons, Sanders, Cassidy, Hickenlooper, Schatz) captured for future enablement.
- Committees ranked into three tiers (high / medium / low-hit-rate-but-critical).
- **Plan doc updated** from `.env` → `.env.local` (commit `82c3dd3`) to match Dan's convention.
- **`.env.local` setup**: symlink at `~/code/policy-levers-leg-watcher/.env.local → ../policy-levers/.env.local`; mirrored to `~/xfer/envs/policy-levers/.env.local` via `collect_envs.py`. Key already placed by Dan earlier in the day.
- **Worktree relocation deferred** — pragmatic call to not move a live worktree mid-branch; the misplacement will resolve itself when the branch merges and the worktree is cleaned up.

## Results

- [`results/20260804_ai_legislators_shortlist.md`](../results/20260804_ai_legislators_shortlist.md) — full punch list + citations + Peters verification, ready to consume as the Phase 8 config-population reference.

## Open Questions

- **Fired reminders #3 and #5** still awaiting Dan's decision (close/snooze/skip). #3 is the leg-watcher build ticket (presumably closes when Phase 8 lands); #5 is FRONTIER outreach (10d old, real work).
- **Worktree relocation** — leave-and-clean-up-on-branch-finish is the deferred choice, but if Dan wants to fix now the ~5-min sequence is: `git worktree move` → fix symlink → edit 2 plan-doc lines → `rm -r ~/xfer/envs/policy-levers-leg-watcher/` → rerun `collect_envs.py`.
- **`collect_envs.py` hardening** — patch to skip git worktrees (check `.git` file vs. directory, or dedupe by `Path.resolve()`) would prevent this class of issue for future worktrees. Not urgent; not yet done.
- **Doc-hygiene cleanup at merge** — Obernolte subcommittee-vs-full-committee framing; Peters ambiguity across STATUS.md sessions.
- **Phase 8 execution** — ready to resume (picks grounded, API key in place, FRONTIER bill number known).
