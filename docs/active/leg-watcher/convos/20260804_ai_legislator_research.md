# 2026-08-04 — AI-legislator research (pivot from Phase 8 execution)

**Line:** `leg-watcher` (worktree `~/code/policy-levers-leg-watcher`)
**Preceding session:** [`20260804_leg_watcher_green_execution.md`](20260804_leg_watcher_green_execution.md) — closed Phases 1–7 GREEN with 75/75 tests passing.
**Handoff-in:** Execute Phase 8 (config population + README + fixture replacement + live smoke).

## What happened

Dan pivoted from Phase 8 execution before it started, asking for research on **which Senators / Reps / committees the watcher should be tuned to** — the natural upstream of the "Senate-member rows placeholder-disabled" TODO in the plan. Kicked off a general-purpose research subagent grounded in Dan's currently-tracked legislators + the "press-page-first workflow" criterion (the GAAIA failure mode the tool is built to catch).

## Provisional findings

- **Two high-yield senators are missing from Dan's tracking:**
  - **Sen. Mark Warner (D-VA)** rolled out a 4-bill "Framework for America's AI Future" July 21–22, 2026 via press page + Axios exclusive.
  - **Sen. Marsha Blackburn (R-TN)** released the TRUMP AMERICA AI Act **as a discussion draft on her press page** March 18–19, 2026 — literally the GAAIA failure mode the tool is designed for.
- **John Curtis (R-UT)**, freshman senator, has made AI a signature issue (3 bills in ~18 months) — the clearest new voice of 2026.
- **Josh Hawley (R-MO)** runs a high-volume AI press page (LEAD Act, Blumenthal-Hawley framework, Warner-Hawley jobs bill, deepfake letters).
- **FRONTIER Act now has a bill number: H.R. 9925** (introduced 2026-07-23). Closes the tracked-bills TODO.
- **Peters clarification (verified from local bill artifacts):** the "Peters" cited as GAAIA / FRONTIER cosponsor across Dan's notes is **Rep. Scott Peters (D-CA-50)** — verified against `bills/frontier-act/README.md`, both press releases, and `bills/obernolte-trahan/README.md`. Gary Peters (D-MI, HSGAC ranking) is a separate person; both are legitimate to track but for different reasons.
- **Framing correction:** Obernolte chairs House Science's Research & Technology *subcommittee*, not the full committee. Babin (R-TX-36) holds the full-committee gavel. STATUS.md 2026-07-18 already references Babin correctly, so Dan's notes are internally inconsistent — cleanup at merge.

## Decisions this session

- Senate watch list expanded past the plan's "4–6" figure to **8 rows** per Dan's preference to keep the "important-even-if-annoying ones (Cruz, Schumer)" alongside the high-signal drafters. Final list: Warner, Blackburn, Cruz, Curtis, Hawley, Rounds, Schumer, Gary Peters. Some rows will run at lower priority — Phase-8 sources.yaml will encode this via `enabled` and optional scoring differences per row.
- **Todd Young** demoted to committee-feed-only coverage (his AI content flows through cosponsorship, not his own press page).
- Hold-for-later shortlist (Schiff, Coons, Sanders, Cassidy, Hickenlooper, Schatz) captured for future enablement.
- Committees ranked into three tiers (high / medium / low-hit-rate-but-critical).

## Artifacts

- `results/20260804_ai_legislators_shortlist.md` — full punch list + citations + Peters verification, ready to consume as the Phase 8 config-population reference.

## Next steps

- Answer the two fired reminders (#3 leg-watcher-build; #5 FRONTIER outreach) — pending Dan's decision.
- Phase 8 execution when Dan is ready to resume the handoff.
- Consider a cleanup pass at merge for the two doc-hygiene items (Obernolte-subcommittee vs full-committee framing; Peters ambiguity across STATUS.md).
