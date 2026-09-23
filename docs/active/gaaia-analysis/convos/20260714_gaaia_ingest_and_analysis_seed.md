# GAAIA ingest + analysis-branch seed

**Date:** 2026-07-14 → 2026-07-16 (session started 07-14, YOLO/AFK, branched to `gaaia-analysis` and finished 07-16)
**Branch:** `gaaia-analysis` (created 07-16 off `main` at `2fab869`)

## Summary

Dan handed off the Obernolte-Trahan Great American AI Act (GAAIA)
discussion draft on 2026-07-14 (269pp, released 2026-06-04, no bill
number yet) with instructions to chunk by section, run subagents per
chunk, and push each chunk + summary as they come in. He was AFK in
YOLO mode, so decisions the prior session had flagged as
open-questions-for-Dan were resolved by his opening message
(`bills/<bill_name>/` layout, section-level chunking, incremental
push) and, where not answered, by the handoff doc's recommendation
posture.

The session ran on `main` for the ingest (46 sections chunked, per-
section subagent summaries in 10 batches, commit+push per batch), then
Dan asked at the end of the day to move the drafting-bugs + structural
findings out of the chat summary into a `NOTES.md` doc on a
`gaaia-analysis` branch — done as the last piece of work.

Throughout the ingest, a concurrent session on Dan's other machine was
producing an `OVERVIEW.md` in the same folder, consuming the per-
section summaries as they landed (one of their commits was a
correction: "gaaia OVERVIEW: fix §111 enforcement (opt-in state AGs
can sue, §111(i)(3)); was misread as federal-only"). No merge
conflicts — different lanes, rebase-then-push worked cleanly each
batch.

## Topics Explored

- Bill structure: 4 titles (Frontier AI Governance, Workforce,
  Cybersecurity, R&D + International), 13 subtitles, 46 top-level
  `SEC. NNN.` headers in the body
- Split-script authoring — regex `^\s*\d+\s+SEC\.\s+(\d+)\.\s+(.+?)\s*$`
  correctly rejected the inserted `''SEC.` headers (§ 5304 inside § 102,
  § 5107 inside § 422, §§ 5601-5605 inside § 423) as being amendments-to-
  other-Acts rather than top-level GAAIA sections
- Trahan-office section-by-section vs bill body reconciliation — 13+
  drafting inconsistencies surfaced
- 46 per-section summaries via parallel `general-purpose` subagents,
  each with a shared `_TEMPLATE.md` style guide and explicit push-back
  instructions

## Provisional Findings

Load-bearing findings (fuller inventory in `../NOTES.md`):

- Bill has real teeth in specific places: § 113 whistleblower shield
  (AIR21-style burden-shifting, fee-shifting, 2× back pay, contractor
  coverage), § 252 prediction-interval employment forecasts at 20-80%
  intervals, § 245 automation benchmarks with training-data-contamination
  guardrails, § 422 interpretability × 3 in statutory priority list,
  § 111 transparency + $1M/day + state-AG opt-in.
- Bill has structural gaps: Labor systematically under-resourced vs
  Commerce/CAISI ($6M/5yr for 20 experts vs uncapped headcount +
  $100M/yr + fee auth); measurement funded but not wired into decisions;
  § 112 IVO regime replicates FAA/Boeing DER capture surface (developer
  pays, no rotation, no cooling-off, near-absolute immunity); no
  fallback if no IVO exists in a technical area.
- Discussion draft has real bugs to fix: § 421 references EO 14110
  (rescinded Jan 2025); § 423 codifies NAIRR with zero appropriation
  (only donations); § 131 mail/wire AI-clause fine capped LOWER than
  non-AI base cap; § 111(g)(2) 24hr report routes to law enforcement
  (sec-by-sec says CAISI, no interagency forward mechanism);
  § 253(f)(2) cross-references Definitions section (§ 101) when § 241
  is intended.
- Three-year sunset alignment on §§ 111, 112, 121 is deliberate —
  forces Congress back to preemption + federal obligations
  simultaneously. Feature to defend, not weakness to fix.

## Decisions Made

- Bill lives at top-level `bills/obernolte-trahan/` (Dan's format
  answer: "bills/bill_name/ is a great format")
- Chunk by top-level `SEC.` header (Dan's answer: "chunk by section so
  we can handle it cleanly")
- Analytical layer lives on `gaaia-analysis` branch under
  `docs/active/gaaia-analysis/`; bill text stays on main
- Handoff doc from prior session (`handoff_obernolte-trahan-bill.md`)
  preserved in the scaffold commit — was previously untracked

## Results

Session outputs (all pushed):

- **On `main`** (commits 94531e9 through b853d86):
  - `bills/obernolte-trahan/gaaia_discussion_draft_2026-06-04.pdf` +
    text extract + section-by-section + FAQ + press release
  - `bills/obernolte-trahan/sections/sec-NNN-slug.md` × 46 (chunked bill body)
  - `bills/obernolte-trahan/summaries/sec-NNN-slug.md` × 46 (Canary
    per-section summaries) + `_TEMPLATE.md`
  - `bills/obernolte-trahan/SECTION_MANIFEST.md`
  - `bills/obernolte-trahan/README.md` (folder intro, sponsor framing,
    drafting-inconsistency notes, provenance)
  - `crm/bills.yaml` — `gaaia_draft_2026_06:` entry per s2938 schema
  - `handoff_obernolte-trahan-bill.md` at repo root (preserved)
- **Merged into main by concurrent session on other machine**:
  - `bills/obernolte-trahan/OVERVIEW.md` (descriptive per-title
    overview, cross-referencing my per-section summaries)
- **On `gaaia-analysis`** (commit 1ecce8f):
  - `docs/active/gaaia-analysis/NOTES.md` — 5-section analytical
    document: (1) drafting bugs, (2) structural findings, (3) positive
    teeth, (4) open questions, (5) suggested next actions
  - `docs/active/gaaia-analysis/RESEARCH_LOG.md`
  - Scaffold: `convos/`, `plans/`, `results/`

## Open Questions

Not resolved this session — for Dan's next iteration:

- Which drafting bugs go in the public-comment letter to
  `GAAIA@mail.house.gov`, and what's the letter's overall stance?
  (§ 5 of `NOTES.md` suggests § 421 dead EO, § 423 NAIRR appropriation,
  § 131 fine cap, § 111 24hr routing, § 253 wrong xref as the primary
  set — Dan's call.)
- Canary's stated position on the § 121 preemption trade — this is
  the vote-shape issue for progressive-Dem staff. Need a view before
  Hill visits.
- $500M revenue threshold vs compute-based thresholds — is the revenue
  cut the right regulatory gate?
- NAIRR frontier-carveout — accept as-is + separate safety-research
  authority, or amend NAIRR to add a frontier safety channel?
- GAAIA vs S.2938 (AIRE Act) composition — the two are complementary
  but not identical; how they interact matters for Canary's
  positioning on both.

Working-tree note: `essays/mats_chang/q1/Q1_MAD_about_AI.md` had a
1-line uncommitted change at end of this session, unrelated to
`gaaia-analysis` — left in place for the concurrent session on the
other machine that owns that line.
