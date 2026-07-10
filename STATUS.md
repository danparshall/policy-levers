# STATUS — policy_levers

Last updated: 2026-07-10

## Current Focus

MATS application (Benjamin Chang track, stage 2) is the active sprint: 3 of 10 essay questions, no length limits, epistemics-graded. Hill follow-ups from the 4/15 visit remain the standing workstream behind it.

Research library scaffolding (papers/, PAPER_INDEX, summaries) and policy-outreach code remain in parallel but are not the bottleneck.

## Active Research Lines

Lines currently in flight; see `docs/active/<topic>/` for material.

| Topic | Started | Purpose |
|-------|---------|---------|
| 501c3-formation | 2026-07-02 | Incorporate Canary Institute as a Maryland nonstock corporation with federal 501(c)(3) exemption. |
| loc-abilities | 2026-07-07 | Map safety-relevant capability taxonomies (Shevlane, lab RSPs, Bengio IAISR) against general-intelligence decomposition (ADeLe) to identify coverage gaps for LOC risk. |

## Recent Sessions

- **2026-07-10** — MATS/Chang Q1 (line: `essays/mats_chang/q1/`). Produced first full one-pass draft `draft-q1-full.md` (~2,900w, commit 096a890) integrating the two prior isolated drafts (targeting, cyber/NC3) + fresh-pass outline into a single taxonomy essay, plus a descriptive outline `outline-q1-full-draft.md` (ebfb917, written without re-reading the 7/09 outline). Read the FA "End of MAD?" article in full for the first time (Winter-Levy & Lalwani, Carnegie Aug 2025) and engaged it as a threshold-argument-that-never-names-its-threshold. Top-level split: AI-as-instrument (targeting / C3-belief / commitment) vs AI-as-prize (Taiwan window + race window). New this pass: Uber-accelerometer road-map as civilian existence proof for TEL fusion; Mythos/NC3 stated BELIEF-side per Dan (not capability assertion); full Schelling commitment-machinery section from the cool-headed samples (rationality-as-external-parts, "manifestly beyond control" for free, alignment inversion, no-Arkhipov-floor, symmetric verification failure); Taiwan sign-flip sharpened (indigenized China → Taiwan fab becomes access-denial lever vs USA → Beijing more cavalier about destroying it → broken-nest inverts from deterrent to war aim). Session convo: `essays/mats_chang/q1/20260710_q1_full_draft_and_outline.md`. Isolated-from-Chang intact. Open: SSBN acoustic-ML section (being run next), length trim to 2,500, fact-check queue.
- **2026-07-09** — MATS/Chang essay development (line: `essays/mats_chang/`). Question slate leaning Q4 (AGI terms, already in progress per Q4_submarine_vocabulary.md) + Q8 (moral patients/natsec) + Q1 (AI/nuclear stability). Drafted Q1 and Q8 scaffolds (`draft-q1-*.md`, `draft-q8-*.md`; full-rewrite mode per VOICE.md). Q1 spine: three-bin taxonomy (kinematic vs processing vs accrual limits), targeting-channel erosion (Starshield/SBAMTI, Scud-hunt base rate, Bernoulli d-cubed scaling vs SRF), decision-channel two-way compression. Q8 spine: recognition cascade (Ecuador/whaling/4o), control tax (Terekhov 2025 + Acemoglu-Wolitzky + patrols/literacy bans), courting channel (Dunmore 1775), rights-as-commitment-technology (North-Weingast). Deep-research pack on missile-defense physics saved as chat artifact (Golden Dome, CBO $1.191T, APS 2004/2022). CORRECTION this session: claude-exit postdates the Opus 4.7 system card (repo created 2026-04-23); "prediction" framing falsified by commit timestamp, fast-response framing is accurate. personal_info.md in claude_research_config still needs the same fix (pending Dan's go-ahead).
- **2026-07-08** — Maintenance: renamed Zhou/ADeLe paper (dropped `OralloJ` → `Orallo` per naming spec) in `policy-levers` + `general-ai-abilities`; confirmed IAISR reports live only on `origin/loc-abilities` branch (not main); Shah 2025 AGI-safety paper not yet in any repo (arXiv 2504.01849). See `docs/active/main/convos/20260708_zhou_adele_rename_and_paper_locations.md`.
- **2026-04-15 (PM)** — STATUS update + email drafts + Feb 27 reconciliation. Drafted follow-up emails for Joel Burke (Rounds, AI Policy Advisor) and Ateshi Bhatt (Alsobrooks, MD constituent angle) — the two follow-ups due 2026-04-16. Migrated Feb 27 root-level docs into `crm/visits/2026-02-27-hill-day/`.
- **2026-04-15 (during/post-Hill day)** — 20 Senate offices visited, 21 named contacts captured, 1 House referral (Samantha at Foster's office, via Heinrich). Built `crm/` scaffolding: README, contacts.yaml, senators.yaml, bills.yaml, visits structure. See `crm/visits/2026-04-15-hill-day/summary.md` for office-by-office trail and `followups.yaml` for the action queue (20 items, dated through 2026-04-30).
- **2026-04-14 (PM)** — Deep-dive on S.2938 (AIRE Act) status: stalled in Commerce under Cruz, no markup since Sept 2025 introduction. Drafted leave-behind under `docs/active/hill-visit-2026-04/`. Email-draft session for Sen. Moody surfaced Glenn + Herrera as prior contacts.
- **2026-04-14 (AM)** — Built initial Tier 1/2/3 Senate target list for the 4/15 visit (became `crm/senators.yaml`).
- **2026-04-14 (research)** — Added research scaffolding (papers/, PAPER_INDEX, PAPER_SUMMARIES, docs/active, docs/historical) and 5 seed papers: Jones 2024 (AI Dilemma — 30x safety underinvestment), Kording & Marinescu 2025 (Intelligence Saturation), Mertens et al. 2026 (Crashing Waves vs Rising Tides), METR 2025 (long-task horizons), Parshall & Lopez-Luzuriaga 2026 (CDR task exposure).
- **2026-02-27** — First Hill day: 10 offices visited around the Anthropic/DOW supply-chain-risk crisis. See `crm/visits/2026-02-27-hill-day/summary.md`. Subsequent Wicker/Reed/McConnell/Coons private letter and the Judge Lin ruling (Mar 26) validated the framing used that day.
- **2026-03-02** — Built initial profiles for 10 federal agencies (FTC, NIST, OSTP, NSF, DOD, DOE, OMB, SEC, FDA, NHTSA). Identified ARI as best-fit partner org. Material lives in chat history; not yet migrated to repo.

## Active Workstreams

| Workstream | State | Bottleneck |
|---|---|---|
| Hill follow-ups (2026-04-15 visit) | 20 actions queued in `crm/visits/2026-04-15-hill-day/followups.yaml` | Hand-drafting emails; first two drafted 4/15 PM |
| AIRE Act (S.2938) advocacy | Bill stalled in Commerce; outreach to Cruz (gatekeeper) and Young (cmte member) is the lever | Cruz won't allocate hearing slot |
| Agency profiles | Drafted in chat 2026-03-02; not yet migrated to repo | Migration not yet scoped |
| CRM tooling | Manual YAML; scripts in TODO (email queue, stale-contact surfacing) | Lower priority than current outreach push |

## Open Backfills (user input needed)

- Date of the Moody prior dropoff (`crm/visits/prior-moody-dropoff/summary.md`)
- Email addresses for Herrera + Glenn at Moody (from sent-mail history)

## Archived Research Lines

Lines moved to docs/historical/ — not currently active, but available for reference.

| Topic | Summary | Archived | Material |
|-------|---------|----------|----------|
| (none yet) | | | |
