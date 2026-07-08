# Research Log: loc-abilities

Created: 2026-07-07
Purpose: Map safety-relevant capability taxonomies (Shevlane, lab RSPs, Bengio IAISR) against general-intelligence decomposition (ADeLe) to identify coverage gaps for LOC risk.

---

(Sessions logged here, newest first)

## 2026-07-08 — Citations + first-pass ADeLe crosswalk (convo: citations-and-adele-crosswalk)

Delivered the two items requested: (1) a verified citation set for the LOC-taxonomy sources, (2) a first-pass ADeLe×LOC crosswalk. Output in `reports/loc_abilities/`: `CITATIONS.md`, `references.bib`, `adele_crosswalk.md`, `crosswalk_matrix.csv`.

Key verifications / corrections captured this session:
- ADeLe = Zhou et al. 2025, "General Scales Unlock AI Evaluation…", arXiv:2503.06378 (26 authors, Lexin Zhou first; 18 rubrics scored 0–5; UG is computed, not a rubric). Nature version reported but UNVERIFIED — cite arXiv.
- Tolan is **2021** (JAIR v71), not 2019.
- FMF Jan-2025 brief is actually dated **Dec 2024** and taxonomizes **evaluations** (methodology×objective), not capabilities — not a peer of Shevlane/RSPs.
- OpenAI PF v2 **dropped Persuasion**; current tracked categories: Bio/Chem, Cyber, AI Self-Improvement. DeepMind FSF 3.1 **added** a Harmful-manipulation CCL. Divergent treatment of the same capability = a finding.
- Lab frameworks converged on CBRN + Cyber + AI-R&D/autonomy as capability thresholds; deception/situational-awareness moved to a separate misalignment track.
- Shah 2025 (arXiv:2504.01849) risk split is **four-way** (misuse/misalignment/mistakes/structural), not three.

Crosswalk finding (my read, walled in the doc): 8 direct / 32 enabler / 169 absent cells. Every direct cell runs through a Knowledge dim or the MS/CEe social-expression pair. **Five capabilities have zero direct ADeLe measure** — long-horizon planning, deployment-aware situational awareness, self-proliferation/ARA, autonomous horizon, scheming — i.e. the agentic/temporal/deployment/propensity cluster. Argued the gap is **structural** (ADeLe scores task-demand, not model-capability/propensity), and that VO is a *false cognate* for METR's horizon (measures human task-time, not model endurance). Flagged the predictive-vs-measurement distinction as the live crux the essay must not conflate.

Open for next session:
- Decide propensity in/out of the matrix (PLAN open-q #2) — currently included as one flagged column.
- Read IAISR §2.5 directly for the verbatim LOC triad before quoting.
- Confirm ADeLe Nature citation; confirm Burnell full author list.
- Ingest Shevlane + FMF PDFs into `papers/` per naming convention (PLAN immediate-next-step #1).


## 2026-07-07 — Line created (session started as MATS essay dictation)

Origin: this line was cut mid-session while dictating the MATS Benjamin Chang track essay on AGI/ASI terminology. The essay's argument depends on a claim about which of ADeLe's 18 rubrics are safety-relevant, which turned out to require a separate report to answer properly. `plans/PLAN.md` scaffolds that report.

Immediate parent use: MATS essay due 2026-07 (see chat, no branch yet for the essay itself).

Follow-ons flagged:
- Read FMF Jan 2025 taxonomy directly.
- Verify current versions of Anthropic RSP, OpenAI PF, DeepMind FSF at ship time.
- Cross-check IAISR 2026 §2.5 for the LOC decomposition graphic.
