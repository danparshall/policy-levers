# Citations and ADeLe crosswalk

**Date:** 2026-07-08
**Branch:** loc-abilities
**Surface:** Cowork (desktop app) — NOT claude.ai web Chat. See note under Decisions.
**Convo name:** citations-and-adele-crosswalk

## Summary

First working session on the `loc-abilities` line since it was cut from the MATS essay. Scope was a subset of `plans/PLAN.md`: (1) collect and verify citations for the LOC-taxonomy sources so they can be added to `papers/` later, and (2) make a first attempt at the ADeLe×LOC crosswalk. Both delivered to `reports/loc_abilities/` (`CITATIONS.md`, `references.bib`, `adele_crosswalk.md`, `crosswalk_matrix.csv`) and committed here (commit `fab246b`).

Citation collection was done via two parallel research sub-agents (safety-side sources; general-intelligence-decomposition sources + ADeLe rubric extraction), then the two highest-stakes arXiv records (ADeLe `2503.06378`, Shah `2504.01849`) were re-verified directly against arXiv. The crosswalk cell assignments were encoded in a small Python script so the D/E/absent logic is inspectable and re-gradable rather than asserted in prose.

The back half of the session was a meta-thread: Dan noticed files had appeared "locally" and realized this session was running in **Cowork**, not the claude.ai web Chat interface his claude_researcher workflow was designed for. Clarified that the GitHub side ran identically (clone-with-PAT → commit → push) but Cowork adds a local sandbox shell and a local outputs folder that web Chat lacks. This convo summary exists because the raw Cowork transcript will not appear in the web chat list, so the durable reasoning needs to live on the branch.

## Topics Explored

- Verification of ~16 LOC-taxonomy and gen-intelligence-decomposition citations (arXiv IDs, versions, dates, category lists), with current 2026 versions of the three lab frameworks.
- Exact extraction of ADeLe's 18 demand rubrics (0–5) + UG, checked against the ADeLe platform.
- Construction of an 18-dimension × 11-capability crosswalk (Shevlane's 9 categories + autonomous-horizon [METR] + scheming/deceptive-alignment [propensity]).
- Where the crosswalk supports vs. does not support the MATS essay's capability-profile + autonomous-horizon argument.
- Environment/workflow mechanics: Cowork vs. web Chat, local vs. GitHub artifacts, why this transcript is invisible to the web interface, and how the trackers-as-source-of-truth design insulates the work from that.

## Provisional Findings

- **Crosswalk tally: 8 direct / 32 enabler / 169 absent** (out of 209 cells). Every "direct" cell runs through either a Knowledge dimension (KNf/KNn/KNa/KNs → the knowledge component of cyber/CBRN/AI-R&D/political-strategy) or the MS/CEe social-expression pair (→ deception/persuasion). No primordial *reasoning* rubric directly measures any dangerous capability.
- **Five capabilities have zero direct ADeLe measure:** long-horizon planning, deployment-aware situational awareness, self-proliferation/ARA, autonomous task horizon, scheming. These are exactly the agentic / temporally-extended / deployment-relative / dispositional capabilities.
- Provisional interpretation (walled in `adele_crosswalk.md` §5): the gap is **structural, not incidental** — ADeLe scores task-*demand*, not model-*capability*-or-*propensity*, so it is constitutionally blind to that cluster. VO ("Volume", log human task-time) is a **false cognate** for METR's autonomous horizon: it measures the wrong side of the relation (human task length vs. model endurance).
- The claim above is about **direct measurement**, not **predictive coverage** — a distinction the essay must not conflate. ADeLe's authors would fairly argue a demand profile can *predict* dangerous-capability-eval performance without a dedicated column. The strongest version of the essay's argument concedes the predictive framing and attacks on measurement (self-proliferation / deployment-aware SA are behaviors under conditions ADeLe never instantiates).

Citation-level corrections captured (details in `CITATIONS.md`):
- ADeLe title is "General Scales Unlock AI Evaluation with Explanatory and Predictive Power" (arXiv:2503.06378); UG is computed, not a 0–5 rubric; a Nature version is reported but its citation is UNVERIFIED.
- Tolan is **2021** (JAIR v71), not 2019.
- FMF "taxonomy" (dated **Dec 2024**, not Jan 2025) taxonomizes **evaluations**, not capabilities — not a peer of Shevlane/RSPs.
- OpenAI PF v2 **dropped Persuasion**; DeepMind FSF 3.0 **added** a Harmful-manipulation CCL — divergent treatment of the same capability.
- Shah 2025 risk split is **four-way** (misuse/misalignment/mistakes/structural).

## Decisions Made

- Crosswalk built as **descriptive matrix + walled interpretation** ("both, layered"), per Dan's call, since this is a **private thinking document**, not a Canary-facing deliverable. Field terms of art used directly (no "AI Policy" euphemism substitution) because nothing here is external.
- Deliverable = **two docs + BibTeX + machine-readable CSV** (Dan chose "add machine-readable matrix").
- **Propensity** included as one flagged column (`Scheme`) to make the capability/propensity boundary visible — this is PLAN open-question #2 rendered as a column; can be struck if propensity is ruled out of scope.
- **Surface note:** session ran in Cowork. RESEARCHER.md assumes `/home/claude/` is writable; the Cowork sandbox blocks it, so clones were done under `/tmp` with a blobless sparse checkout (repo is 110 MB, full clone times out). On claude.ai web the documented `/home/claude/` paths work as written — no change needed to the workflow.

## Results

- `reports/loc_abilities/CITATIONS.md` — annotated, verified bibliography.
- `reports/loc_abilities/references.bib` — drop-in BibTeX.
- `reports/loc_abilities/adele_crosswalk.md` — matrix + narrative + walled interpretation.
- `reports/loc_abilities/crosswalk_matrix.csv` — tidy long-format, per-cell justifications.

## Open Questions

- Propensity in or out of the taxonomy (PLAN open-q #2). Currently in, as one flagged column.
- Read IAISR §2.5 directly for the verbatim active/passive LOC triad before quoting.
- Confirm the ADeLe **Nature** citation (volume/article/date) or keep citing arXiv.
- Confirm Burnell et al. full author list on arXiv.
- Predictive-vs-measurement: is ADeLe's demand profile predictive of dangerous-capability-eval scores? Empirical question the crosswalk cannot answer; would materially strengthen or weaken the essay.
- Next PLAN step: ingest Shevlane + FMF PDFs into `papers/` under the naming convention.
