# leg-watcher v1.1 press-page enable — execution

**Date:** 2026-08-11
**Branch:** leg-watcher
**Machine:** Dans-MacBook-Air
**Commits:** `dc63b4c` → `75125f1` (6 commits, all pushed)

## Summary

Executed Phases 1–4 of `plans/20260811_leg_watcher_v11_press_page_enable.md`.
The watcher went from 4 enabled sources to **18**, crossing the plan's "useful
tool" line: every FRONTIER sponsor with a watchable page is now on the live
wire, including Trahan — the literal GAAIA-catcher the whole build was named
for. Dan called stop-at-Phase-4; Phases 5–6 (cron-readiness polish) are
deferred with a pointer in issue #8.

The session's central empirical lesson: **entry counts lie**. The Phase 1 probe
scored 11 member/committee RSS feeds as live (200 + non-empty), but Phase 2
fixture capture showed most were the *wrong feed* — the evo-Drupal House sites
serve a featured-content/videos/photo-caption feed at `/rss.xml`, not press
releases, and Curtis's Senate feed contains exactly one 2022 lorem-ipsum "Test
Post." Only capture-level verification (read the actual items) separates a live
press feed from a live decoy. The plan's fixture-first discipline caught all of
it before anything was enabled.

Phase 3 recovered most of the RSS losses via html_diff: three shared CMS
shapes (evo-Drupal h3/h5 variants, Senate PageList) cover 9 offices with just
three selector sets, at the cost of three new date formats in the adapter
(`%m/%d/%Y`, `%m.%d.%Y`, weekday-prefixed) plus ordinal-suffix stripping —
each TDD'd RED→GREEN against real fixtures.

## Topics Explored

- Phase 1 RSS probe (all 22 disabled sources × 3–7 candidate URL patterns)
- Phase 2 fixture captures exposing wrong-content feeds; enable of the 4 real
  ones (Trahan, Franklin, Hawley, Schumer/caucus)
- Phase 3 selector hunts across 13 office pages; three shared CMS shapes
  identified; 9 offices enabled, 4 terminal verdicts
- Phase 4: senate.gov floor schedule enabled; majorityleader.gov weekly
  schedule found moved (old URL 404s) and unparseable (Telerik prose paste)
- Full-registry smoke run from clean state (18 sources, recess week)

## Provisional Findings

- **Entry-count probes cannot validate press feeds.** 200 + entries>0 admitted
  7 wrong-content feeds; only item-level capture review caught them.
- **CMS clusters make selector work cheap.** evo-Drupal (Obernolte, Houchin,
  Stevens = h3 variant; Subramanyam = h5), Senate PageList (Cruz, Rounds,
  Peters-MI), Fireside RSS (Trahan, Franklin), WordPress RSS (Hawley, caucus
  feed), WP/Elementor html (Warner), bespoke-static (Blackburn). Six shapes
  cover 15 of the 18 enabled sources.
- **Date-format drift is the main adapter cost of breadth**: DATE_FORMATS grew
  from 3 to 7 entries + ordinal stripping. All additions pinned by real-fixture
  tests.
- **Live-wire signal is real even in recess**: full smoke surfaced Trahan's
  FRONTIER coalition release (tracked-bill pin), the Senate 8/13 pro forma
  session (Time-critical), Hawley AI-surveillance [13], Warner AI-oversight
  [7], Rounds quantum [5]; 70 noise items suppressed; zero source-health
  warnings.
- **Schumer caucus feed scores below threshold for floor wrap-ups** — the
  floor-signal value of that feed depends on the Phase 7 keyword retune
  (noted in issue #7).

## Decisions Made

- **Stop at Phase 4** (Dan): Phases 5–6 deferred; pointer added to issue #8.
- **Batched one commit for Franklin+Hawley+Schumer** (deviation from the
  plan's per-source commits; rationale + source ids in commit `48dddc1`).
- Terminal verdicts (config comments carry evidence): rep-scott-peters-ca
  (JS shell), sen-curtis (no listing dates + dead feed), rep-lofgren
  (unreliable dates), rep-foushee (flat siblings), majority-leader-lookahead
  (prose paste; URL updated to current location), committee RSS rows
  (Commerce/Judiciary/Science/E&C: no feeds exist; HSGAC: real feed, empty
  during recess — re-probe in September).
- Follow-up issues opened: #7 `[2026-08-18]` keyword retune; #8 v1.2 source
  gaps + Phases 5–6 pointer.
- Reminder #5 (FRONTIER outreach): skipped again this session (Dan).

## Results

- 6 commits on `leg-watcher`: `dc63b4c` (Phase 1 config), `07d80eb` (Trahan),
  `3e9ffc2` (probe-correction reversion), `48dddc1` (3 RSS enables),
  `140aea3` (3 html_diff enables + 2 date formats), `cc211e2` (6 html_diff
  enables + dotted dates), `75125f1` (Senate floor + weekday dates).
- 93/93 tests, ruff clean. 11 new REAL fixtures with provenance rows.
- Digest output is regenerable (`uv run watcher --include-backlog 14`); the
  smoke digest content is quoted in STATUS.md's session entry.

## Open Questions

- **Merge to main?** Plan Q4 — the tool now does what issue #3 promised
  (RESEARCH_LOG previously said "close #3 after v1.1 Phase 4 lands"). Not
  raised for decision this session; Dan's call, never merge without explicit
  request.
- Whether Schumer's caucus feed earns its keep post-retune (plan Q2).
- HSGAC re-probe once Congress returns (~9/1) — will the feed populate?
- Pagination (Phase 5) becomes urgent when session resumes and bill volume
  jumps; EmptyFeed (Phase 6) noise is visible right now during recess.
