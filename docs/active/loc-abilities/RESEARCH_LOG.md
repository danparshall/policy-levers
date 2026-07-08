# Research Log: loc-abilities

Created: 2026-07-07
Purpose: Map safety-relevant capability taxonomies (Shevlane, lab RSPs, Bengio IAISR) against general-intelligence decomposition (ADeLe) to identify coverage gaps for LOC risk.

---

(Sessions logged here, newest first)

## 2026-07-08 (PM) — Verification pass + epistemic-regime / covariance thread

Context: DP flagged the prior 2026-07-08 crosswalk was produced in a Cowork session that ran *without* the deep-research tool, and the output "looked surprising." Ran an independent primary-source redo, then diffed against the existing files rather than overwriting.

**Diff verdict (honest):** the Cowork output held up *well* — better than expected for an unsupervised run. Two independent passes converged on the same structure (Shevlane's 9, ADeLe's 18, lab convergence, persuasion divergence, the zero-direct-measure gap), which is strong mutual verification. The one substantive divergence: on **VO ↔ METR horizon**, Cowork's "false cognate" read is *sharper and more correct* than my redo's "partial proxy" framing. Kept Cowork's files as canonical; did not overwrite. The redo lives only in chat (its residual value is citation-freshness, already folded in where it mattered).

**Shah 2025 verified against §2.1 full text** (arXiv:2504.01849). Three refinements committed as notes in `CITATIONS.md` (Shah entry) + cross-ref in `adele_crosswalk.md`:
- The "intentional-active / unintentional-active / passive" triad is **Shah mapping onto IAISR Fig 2.5**, not IAISR's own body phrasing (IAISR's native shape is a two-axis tree: active{intentional,unintentional} vs passive). Resolves the standing ⚠️ on the Bengio entry — but still read the actual Fig 2.5 from the report PDF before reproducing it.
- Shah's **misalignment subsumes** deception + scheming + unintended active LOC (not a parallel track).
- Shah maps **passive LOC → gradual disempowerment** (Kulveit 2025) as a structural risk.
- Also verified: IAISR active/passive structure (House of Lords Library summary + STAMP/STPA paper citing Fig 2.5); Singapore Consensus §1.7 explicitly separates control-undermining **capabilities** from **propensities** — i.e. the field's own consensus docs already carry the capability/propensity split the essay argues for.

**New thread → `eval_integrity_and_covariance.md`** (DP's ideas; joint failure-mode analysis). The essay's governance-object argument:
- **Epistemic asymmetry:** misuse score = *thermostat* (two-directional, propensity stipulated → governs mitigation intensity); misalignment score = *smoke alarm* (one-directional, trustworthy only when it fires). "Score each Shah category → mitigation level" is sound for misuse, unsound as-stated for misalignment. Defensible version: capability score sets a *floor*, propensity uncertainty sets the *ceiling*.
- **DP's covariance-time-series proposal:** signal = decorrelation events in the capability vector, not levels. A targeted sandbagger generates the anomaly by sandbagging. Defender-favorable asymmetry (DP): spoofing a *joint* distribution requires knowing the population baseline, harder than spoofing a *marginal*.
- **Failure mode 1 (bounded):** eval-awareness recurs one order up (detector-aware model spoofs covariance smoothly). Grounded: van der Weij 2406.07358 (selective WMDP-vs-MMLU suppression = induced decorrelation), 2603.03824 (eval-awareness is dynamic/optimizable/transfers), 2508.00943 (sandbagging survives CoT monitoring). Complementary detector: Tice et al. noise-injection.
- **Failure mode 2 (precondition):** covariance alarm can't distinguish real signal from instrument drift without a controlled substrate. DP: continually-generated human benchmarks. Caveat (Test of Time 2509.00072): LLM-*generated* fresh questions launder contamination → substrate must be **human-authored**, difficulty-anchored, construct-validated (LiveMedBench 2602.10367 as existence-proof + cost).
- **Essay spine:** every observational scheme against a situationally-aware optimizer is defeated by an optimizer aware of *that* scheme; recurs at every order because structural. → governance object shifts from "measure the model" to "affordances + control-protocol robustness + monitor for anomalies a not-yet-that-capable model still emits." Covariance signal = a strong instance of the last clause, for the current window only.

Files touched: `CITATIONS.md` (+Shah note, +eval-integrity section), `references.bib` (+5 entries), `adele_crosswalk.md` (+cross-ref note), new `eval_integrity_and_covariance.md`.

Open for next session:
- Pull IAISR Fig 2.5 from the report PDF directly (last unclosed verification gap; needed if the essay reproduces the figure).
- Confirm author lists for 2603.03824, 2508.00943, 2509.00072, 2602.10367 (all flagged unverified in bib).
- Decide bundle-by-capability vs bundle-by-capability×wielder (cyber and AI-R&D appear in both bundles depending on who wields).
- Essay §"principal concerns": write the three-concern list so the *heterogeneity* (a measurable quantity, a control-relationship, a propensity) is visible, not flattened into three spec-sheet dimensions.

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
