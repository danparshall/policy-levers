# Research Log: loc-abilities

Created: 2026-07-07
Purpose: Map safety-relevant capability taxonomies (Shevlane, lab RSPs, Bengio IAISR) against general-intelligence decomposition (ADeLe) to identify coverage gaps for LOC risk.

---

(Sessions logged here, newest first)

## 2026-07-29 — Habryka exchange: does datacenter visibility obviate hardware verification?

Convo: `convos/distributed-training-habryka.md`. Retrieval + argument-testing session, no new research. Habryka argued on Twitter that verified chips are unnecessary because frontier runs are $10B+ operations with a footprint visible from space. Pulled Rahman 2026 (2605.29359) and the 7/14 survey to test it.

### Provisional Findings

- His claim holds for *frontier* runs today, and Heim & Pilz hold roughly his position in our own library. It does not hold for the legal thresholds actually on the books: EU AI Act's 10^25 is ~$31M and 10^26 is $3.8B across 4,706 nodes of ≤16 H100-equivalents, which is by construction not a visible facility.
- The argument is self-undermining in a specific way — Rahman rates traffic monitoring ineffective and chip tracking effective, so relying on datacenter observability bets the regime on the co-location assumption that Decoupled DiLoCo is engineering away.
- **New this session: tracking ≠ attestation.** Tracking is custody (evasion detection, export-control compliance); attestation is proving what executed on the device (audit provenance). The 7/14 material did not separate these, and the distinction matters for any public claim about what hardware measures buy. Ties to the §112 audited-artifact-provenance thread on `gaaia-analysis`.
- Rahman's effective-countermeasure list is broader than chip tracking alone (also whistleblower programs, unregistered-hardware limits, conventional intelligence work). Don't overclaim chip tracking as the sole survivor.
- Decoupled DiLoCo is DeepMind coordinating its own runs, so it is a trend-line citation, not evidence of clandestine capability. Covenant-72B (2603.08163) and Consilience are the over-the-open-internet citations.

### Results

- None. Two-tweet reply shipped; substance captured in the convo file.

### Next Steps

- Develop the compliant-vs-defector reframe (most governance value sits in the compliant case *because* the defector case is small and covered by intelligence work) — Habryka's most likely counter, and it generalises past this thread.
- Decide whether the tracking/attestation split belongs in the 7/14 survey's governance section or in the `gaaia-analysis` §112 provenance material.

## 2026-07-14 — Distributed-training methods survey + Rahman 2026 ingest

Convo: `convos/20260714_distributed_training_survey.md`. DP requested a survey of new distributed-training methods; filed as `results/20260714_distributed_training_methods.md`. Four threads: DiLoCo family maturation (scaling laws 2503.09799; Streaming; Decoupled DiLoCo 2604.21428 breaking synchrony itself, DeepMind production), compression (DisTrO 1-bit, SparseLoCo), decentralised proof-of-scale runs (INTELLECT-1/2/3, Consilience 40B at 20T tokens over internet, Covenant-72B trustless peers), and async-RL systems (AReaL, DORA, ProRL Agent) whose loose coupling makes post-training the easy-to-decentralise phase.

Rahman (2026, arXiv 2605.29359) ingested to the main paper library (commit f7a78bd on `main`; full Protocol A summary in root `PAPER_SUMMARIES.md`). Headline: Scher/EU-AI-Act/SB-53 thresholds evadable for $1.6M/$31M/$3.8B of sub-monitoring hardware at ~3x cost premium; effective countermeasures are chip tracking + whistleblowing (Stop Stealing Our Chips Act hook), NOT bandwidth caps or traffic monitoring.

Standing correction for this line: the network-fingerprint detection idea from earlier conversations should be treated as undercut. Replica divergence, not communication, is the binding efficiency penalty, and 1-bit compressed sub-hourly syncs no longer present a distinctive traffic signature. Rahman rates traffic monitoring ineffective outright. LOC-relevant angle: distributed training erodes detectability and shutdownability (Krys 2507.07765), i.e. the infrastructure assumptions behind capability-threshold governance, which is the same gap-coverage question this line studies on the taxonomy side.

Next steps: verify SparseLoCo figures before any external use of the survey; consider ingesting Krys 2507.07765; decide whether the taxonomy crosswalk needs a detectability axis; DP to check whether Robi Rahman is still DC-local before assuming correspondence-only.

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

### Addendum (later same day) — papers ingested + essay structure locked

IAISR Fig 2.5 gap **closed**: both editions now in `papers/` (2025 = arXiv:2501.17805, 2026 = arXiv:2602.21012). Read Fig 2.5 directly from the 2025 PDF (p.~102) — it is a **tree**, not a flat triad: Loss of control → {Active, Passive}; Active → {Intentional active, Unintentional active}. Shah's triad uses IAISR's verbatim *leaf* labels but flattens the two-axis tree. Note in `CITATIONS.md` tightened accordingly.

Structural-tier sources ingested for the essay's §4 (structural) argument:
- **TASRA** (Critch & Russell 2023, arXiv:2306.06924) — canonical societal-scale taxonomy, six types on an **accountability** axis. Third distinct organizing principle (vs Shah's mitigation axis, IAISR's active/passive) → itself evidence no canonical taxonomy exists.
- **AI Risk Repository** (Slattery et al., *Patterns* 2026, doi:10.1016/j.patter.2026.101517; preprint arXiv:2408.12622) — **1,725 risks / 74 frameworks / 7 domains / 24 subdomains**; economic tier = domain 6 "Socioeconomic & Environmental." Its stated motivation (inconsistent AI-risk terminology) *is* the essay's thesis — usable in the opener, not just the structural bullet. Use "over 1,700 risks" in the draft (not "1,600+ structural"; most of the 1,725 aren't structural).

**Essay structure locked (MATS Chang-track, terminology prompt).** Spine: AGI/ASI fine for conversation, useless for governance, because a scalar presupposes the measure→action map is a *function*, and past deployment-aware agency it's an adversarial *game*. Uses Shah's four categories as the tier structure with the **gateability asymmetry** made explicit:
- Misuse → capability-score-gateable (thermostat; uplift → ceiling; propensity stipulated).
- Mistakes → reliability-score-gateable on a *different* axis (QA/deployment-fitness; tolerable error rate *falls* as autonomy rises); a footnote, not a pillar.
- Misalignment → **not** score-gateable (smoke alarm; one-directional, never an all-clear). The covariance-across-time signal is the best available instrument, near-term only. **1-and-3, NOT 2-and-2** — only misuse is capability-gateable; an earlier "two are gateable" phrasing was wrong and would concede the thesis.
- Structural → mostly unmeasured (TASRA + AI Risk Repository as cites); economics + multi-agent/emergent + epistemic erosion + passive-LOC, with gradual disempowerment (Kulveit) as the cross-cutting dynamic.
Close = four-vocabulary proposal (capability/uplift · autonomy/reliability · control · systemic-risk), tied to which tiers have technical vs policy vs no solutions; submarine callback (spec sheet works because sub has no goals + built to mission requirements). Anti-unification IS the proposal — do not end on a single unified metric.
Shah verified to **exclude economics by design** (structural risks explicitly out of scope, §2.1) → don't use Shah as the frame for the economic tier; use IAISR's systemic-risk category there.

Files touched this addendum: `papers/` (+4 PDFs across both sub-sessions: IAISR 2025/2026, TASRA, AI Risk Repository), `PAPER_INDEX.md`, `references.bib` (+2 here), `CITATIONS.md`.

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
