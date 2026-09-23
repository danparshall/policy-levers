# gaaia-analysis — research log

Analytical layer on top of `bills/obernolte-trahan/`. Bill text and per-
section chunks + Canary summaries live on main under
`bills/obernolte-trahan/`. Cross-section analysis, feedback-letter
material, and stance-taking live on this branch.

Newest entries first.

## Sessions

### 2026-07-14 → 2026-07-16 — GAAIA ingest + analysis-branch seed

**Convo:** `convos/20260714_gaaia_ingest_and_analysis_seed.md`

**What:** Ingested Obernolte-Trahan Great American AI Act discussion
draft on main (commits 94531e9 → b853d86 on 2026-07-14): scaffolded
`bills/obernolte-trahan/`, chunked bill body into 46 per-section files,
ran subagents to summarize each section (10 batches, commit+push per
batch), added `crm/bills.yaml` entry. Concurrent session on Dan's other
machine added `OVERVIEW.md` on main. Then on 2026-07-16, per Dan's
request, created branch `gaaia-analysis` off `main` at 2fab869, added
`STATUS.md` row on main for the new research line before switching,
scaffolded `docs/active/gaaia-analysis/` with `convos/`, `plans/`,
`results/` subdirs, wrote `NOTES.md` seeded from the summary-pass
findings.

**NOTES.md structure:**
1. Drafting bugs to flag to `GAAIA@mail.house.gov` — 15 items, ordered
   by materiality. Top set: § 421 dead-EO ref, § 423 NAIRR zero
   appropriation, § 131 AI-clause fine cap bug, § 111(g)(2) 24hr
   routing, § 253(f)(2) wrong cross-reference.
2. Structural findings — pattern-level issues: Labor under-resourced
   vs Commerce; measurement not wired to decisions; § 112 IVO capture
   surface + no fallback; 3-year sunset alignment on §§ 111/112/121 is
   deliberate (defend, don't fix); NAIRR eligibility carves out
   frontier developers; § 301 CISA 2015 reauth is a legislative
   hitchhike.
3. Positive findings — where the bill has real teeth: § 113
   whistleblower, § 252 prediction intervals, § 245 contamination
   guardrails, § 422 interpretability × 3 in statutory priority list,
   § 131 base fraud-fine raise.
4. Open questions — where Canary needs to form a view: $500M vs
   compute threshold, § 141 vs safety-side tension, § 111 risk-threshold
   floor, § 121 sunset revival mechanics, NAIRR safety-research access.
5. Next actions (user decision).

**Not done in this session:**
- Draft public comment letter for `GAAIA@mail.house.gov`
- One-pager for Hill visits
- Position on § 121 preemption trade
- Cross-comparison of GAAIA vs S.2938 (AIRE Act) enforcement architecture

**Convos this session:** None — NOTES.md was written directly from prior
session's summary-pass artifacts without a separate discussion doc.
When Dan is back and starts iterating on positions or feedback-letter
drafting, that becomes a convo under `convos/`.
