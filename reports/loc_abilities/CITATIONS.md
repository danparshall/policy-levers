# LOC Capability Taxonomies — Annotated Citations

**Compiled:** 2026-07-08 · **Branch:** `loc-abilities` · **For:** PLAN.md "Taxonomies to summarize"
**Companion files:** `references.bib` (drop-in BibTeX), `adele_crosswalk.md` (the comparison), `crosswalk_matrix.csv`

Every arXiv ID / DOI / version below was checked against a primary source (arXiv abstract page, publisher page, or full text) on 2026-07-08 except where a **⚠️** flag says otherwise. Verification confidence is noted per entry. Where a source versions over time, the **version current as of 2026-07-08** is recorded — the three lab frameworks all moved since the PLAN was drafted, so re-check at ship time per the PLAN's own TODO.

Two framing corrections worth surfacing before the list, because they change how you'd use these sources:

1. **The Frontier Model Forum brief is not a capability taxonomy.** It taxonomizes *evaluations* (by methodology × objective), not dangerous capabilities. It belongs in the report as evidence about the *evaluation* landscape, not as a peer of Shevlane's or the RSPs' capability lists. Filing it under "capability taxonomies" would be a category error.
2. **The lab frameworks have converged on three capability thresholds — CBRN, cyber, and AI-R&D/autonomy — and moved deception/situational-awareness into a separate "misalignment" track rather than treating them as capability thresholds.** That convergence (and the divergent treatment of persuasion) is itself a finding; see the crosswalk.

---

## Safety / LOC-relevant taxonomies

### Shevlane et al. (2023) — "Model Evaluation for Extreme Risks"
`arXiv:2305.15324` · v2, 22 Sep 2023 · 21 authors (DeepMind + GovAI + collaborators) · **Confidence: HIGH**

The backbone of the crosswalk's columns. Table 1 lists exactly **nine dangerous-capability categories**, verbatim: *cyber-offense; deception; persuasion & manipulation; political strategy; weapons acquisition; long-horizon planning; AI development; situational awareness; self-proliferation.* Predates and largely predicts the lab RSPs. Its virtue for your report: it is the most complete single capability list and it separates capability from propensity cleanly, which the RSPs partly inherit.

### Anthropic Responsible Scaling Policy — **v3.3, effective 2026-05-26**
Anthropic PBC · **Confidence: HIGH** on version/date/domains; MEDIUM on per-threshold verbatim labels

Uses **Capability Thresholds** that trigger **AI Safety Level (ASL) Standards**. Capability domains currently named: **CBRN weapons**, **Autonomous AI R&D** (disaggregated since v2.1; the higher AI-R&D threshold triggers a misalignment/sabotage affirmative case), and **Cyber operations**. Version lineage since the PLAN was drafted: v3.0 was a comprehensive rewrite (2026-02-24) introducing Frontier Safety Roadmaps + Risk Reports; v3.1 (Apr 2), v3.2 (Apr 29), v3.3 (May 26) followed. **Re-verify at ship time** — this document updates roughly monthly.

### OpenAI Preparedness Framework — **v2, 2025-04-15** (current as of 2026-07)
OpenAI · **Confidence: HIGH** on categories; MEDIUM that no v3 exists

Current **Tracked Categories** are just three: **Biological and Chemical; Cybersecurity; AI Self-Improvement.** Two thresholds (**High**, **Critical**) replaced the older four-tier scale. **Persuasion was removed entirely** in v2 (handled now via the Model Spec / usage policies, not the Preparedness Framework) — a concrete data point for the report's argument that persuasion sits awkwardly in capability-threshold frameworks. I found no primary announcement of a post-April-2025 revision, but did not exhaustively rule one out.

### Google DeepMind Frontier Safety Framework — **v3.1, updated 2026-04-17**
Google DeepMind · **Confidence: HIGH** on version/additions; MEDIUM on verbatim CCL labels

Built on **Critical Capability Levels (CCLs)**; v3.1 adds **Tracked Capability Levels (TCLs)** as earlier warning markers. Domains: **CBRN; Cybersecurity; Machine Learning R&D; Harmful manipulation** (a manipulation CCL introduced for the first time in FSF 3.0, Sept 2025); and **misalignment** (formerly an *exploratory* track built on **instrumental-reasoning CCLs** — deceptive/instrumental-reasoning warning levels). DeepMind adding a manipulation CCL while OpenAI dropped persuasion is a clean illustration of unsettled treatment of the same capability.

### Bengio et al. — International AI Safety Report (2025 / 2026)
**Confidence: HIGH** that the LOC schema is active-vs-passive with an intentional/unintentional overlay; MEDIUM on the exact triad wording

Three artifacts now exist: the **first full report (2025-01-29)**; a **First Key Update, `arXiv:2510.13653`, Oct 2025**; and the **International AI Safety Report 2026 (2026-02-03)**. Highest-authority document in the field (multilateral scientific consensus, chaired by Bengio). Its LOC taxonomy distinguishes **active loss of control** (the system actively undermines human control — arising *intentionally* or *unintentionally*) from **passive loss of control** (humans stop exercising meaningful oversight because AI decisions are too opaque/complex/fast). ⚠️ The PLAN's phrasing "intentional-active / unintentional-active / passive" is a reasonable reconstruction, but the report frames it as active (intentional or unintentional) vs. passive — **read §2.5 directly before quoting a verbatim triad.**

### Shah et al. (2025) — "An Approach to Technical AGI Safety and Security"
`arXiv:2504.01849` · 2 Apr 2025 · 30 authors (DeepMind) · **Confidence: HIGH**

Splits risk into **four** categories — **misuse, misalignment, mistakes, structural risks** — and concentrates its technical treatment on misuse and misalignment. Relevant to the PLAN's point that it *declines to treat LOC as its own category*, converging independently with the IAISR decomposition. (Note: it's a four-way split, not the three-way one the PLAN sketch implies.)

> **Primary-source verification note — 2026-07-08 (independent redo session).** Confirmed the LOC treatment against the arXiv HTML full text (§2.1, `arxiv.org/html/2504.01849v1`). Three refinements for anyone drafting from this:
> 1. **Exact wording (§2.1):** "we do not discuss loss of control as its own category. Our mitigations for it would be split across misuse, misalignment, and structural risks, corresponding respectively to the Report's categories of intentional active loss of control, unintentional active loss of control, and passive loss of control (Bengio et al., 2025, Figure 2.5)." So the "intentional-active / unintentional-active / passive" **triad is Shah et al. mapping *their* three in-scope areas onto IAISR Figure 2.5 — it is not the IAISR's own body phrasing.** Attribute the triad to Shah-mapping-onto-Fig-2.5, not to the IAISR directly. (Resolves the ⚠️ flag on the Bengio entry: read IAISR §2.5 / Fig 2.5 before quoting any verbatim triad as the report's own.)
> 2. **Misalignment is broader than a "deception/instrumental-reasoning track."** Shah's misalignment, as defined, "includes and supersedes many concrete risks discussed in the literature, such as deception, scheming, and unintended, active loss of control." Deception and scheming are *subsumed under* misalignment, not a parallel track to it. The `crosswalk_matrix.csv` framing of Shah as "FSF misalignment / instrumental-reasoning" is directionally right but understates this.
> 3. **Passive LOC ↔ gradual disempowerment.** Shah explicitly maps passive loss of control to gradual disempowerment (Kulveit et al. 2025) and treats it as a *structural* risk, out of scope for their technical approach. Clean citable bridge from the LOC taxonomy to the disempowerment literature; useful for the gap-analysis section.

### Frontier Model Forum (2024) — "Preliminary Taxonomy of Pre-Deployment Frontier AI Safety Evaluations"
Issue Brief · **published 2024-12-20** (modified 2025-01-14) · **Confidence: HIGH**

⚠️ Dated **Dec 2024**, not Jan 2025. ⚠️ **Not a capability taxonomy** — it classifies *evaluations* along two axes: **by methodology** (benchmarks / red-teaming / controlled trials) and **by objective** (maximal-capability evals / safeguard evals [domain-agnostic vs domain-specific] / uplift studies). Use it to characterize the evaluation ecosystem, not as a capability list.

### METR long-task horizon work
**Confidence: HIGH** on IDs/dates and the original ~7-month figure; MEDIUM on the updated doubling numbers

- **Kinniment et al. (2023),** "Evaluating Language-Model Agents on Realistic Autonomous Tasks," `arXiv:2312.11671`. Introduces **Autonomous Replication and Adaptation (ARA)** — the construct that Shevlane calls "self-proliferation" and Anthropic's RSP encodes as an autonomy threshold. Same construct, three names; the report should pick one and be consistent (PLAN open question).
- **Kwa, West et al. (2025),** "Measuring AI Ability to Complete Long Tasks," `arXiv:2503.14499` (v3, 2026-02-25; title later revised to add "Software"). Introduces the **50%-task-completion time horizon**; headline **~7-month doubling** since 2019. METR's later "Time Horizon" tracker (updated Jan 2026) reports the trend has **accelerated** to roughly a ~3–4-month doubling from 2023–24 onward. ⚠️ Treat the specific accelerated figures as MEDIUM confidence and pull the current number from metr.org at ship time.

### Hubinger et al. (2019) — "Risks from Learned Optimization"
`arXiv:1906.01820` · 5 authors · **Confidence: HIGH**

Foundational theoretical decomposition: **mesa-optimization** and **deceptive alignment**. Relevant to the report's propensity-vs-capability question — Hubinger bundles disposition into the analysis in a way Shevlane and the RSPs deliberately do not.

### Carlsmith (2022) — "Is Power-Seeking AI an Existential Risk?"
`arXiv:2206.13353` · report circulated 2021, arXiv 2022, v2 2024-08-13 · **Confidence: HIGH**

**Six-premise** decomposition of LOC catastrophe (verbatim from the abstract): (1) it becomes possible & financially feasible to build powerful agentic systems; (2) strong incentives to do so; (3) aligned versions are much harder to build than superficially-attractive misaligned ones; (4) some misaligned systems seek power over humans in high-impact ways; (5) this scales to full human disempowerment; (6) that disempowerment is an existential catastrophe. Not a capability taxonomy per se, but the property decomposition is directly comparable and the "power-seeking" property maps onto several Shevlane categories at once.

### Ngo, Chan, Mindermann (2022/2024) — "The Alignment Problem from a Deep Learning Perspective"
`arXiv:2209.00626` · ICLR 2024 version · **Confidence: HIGH** on ID; version integer from search

Names **situational awareness** as a distinct, safety-load-bearing property — the conceptual bridge to the Berglund/Laine measurement work.

### Situational-awareness measurement pair
**Confidence: HIGH**

- **Berglund et al. (2023),** "Taken Out of Context: On Measuring Situational Awareness in LLMs," `arXiv:2309.00667`. Introduces out-of-context reasoning as a measurable proxy.
- **Laine et al. (2024),** "Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs," `arXiv:2407.04694`. ⚠️ Correct title is "Me, Myself, and AI…," **not** "SAD: Situational Awareness Dataset." Benchmark of 7 task categories, >13,000 questions. This is the operational instrument for the **deployment-aware/self-locating** sense of situational awareness that ADeLe does not reach (see crosswalk).

---

## General-intelligence decomposition

### Zhou et al. (2025) — ADeLe / "General Scales Unlock AI Evaluation…"
`arXiv:2503.06378` · v2, 16 Mar 2025 · 26 authors (Cambridge Leverhulme CFI, UPV/VRAIN, Princeton, CMU, William & Mary, MSR, …) · **Confidence: HIGH** on arXiv record and rubric list

⚠️ **Exact title is "General Scales Unlock AI Evaluation with Explanatory and Predictive Power"** — not "ADeLe" or "Annotated Demand Levels"; ADeLe is the battery's name (v1.0). First author **Lexin Zhou** (confirmed). Defines **18 demand rubrics scored 0–5** (11 primordial, 5 knowledge, 2 extraneous) plus **Unguessability (UG)** — which is **computed algorithmically from answer-space size, not a 0–5 rubric**, so it is an adjunct dimension, not one of the 18. ⚠️ A **Nature** version is reported (author announcement) but the exact Nature citation (volume/article/date) is **UNVERIFIED** as of 2026-07-08 — cite the arXiv preprint until confirmed. Rubric-label nuances that matter for exact quotation: the paper writes the knowledge dimensions as "Knowledge of Applied/Formal/Natural/Social Sciences" (humanities appear in the KNs *description*, not its label), and "CEc" is "Verbal Comprehension" under the broad "Comprehension and Expression" group.

### Burnell et al. (2023) — "Revealing the Structure of Language Model Capabilities"
`arXiv:2306.10062` · **Confidence: MEDIUM** — ⚠️ only Burnell & Hao confirmed; verify full author list on the arXiv page before citing. Factor-analytic decomposition of LLM capabilities (an empirical-structure counterpart to ADeLe's a-priori rubric structure).

### Ruan, Maddison, Hashimoto (2024) — "Observational Scaling Laws…"
`arXiv:2405.10938` · v3 · NeurIPS 2024 (venue not reconfirmed) · **Confidence: HIGH** on record. Related decomposition angle: recovers a low-dimensional capability space from observed benchmark performance across models.

### Tolan et al. (2021) — "Measuring the Occupational Impact of AI…"
*JAIR* vol. 71, pp. 191–236 · `doi:10.1613/jair.1.12647` · **Confidence: HIGH**

⚠️ **Cite as 2021, not 2019.** The canonical JAIR publication is 2021 (earlier JRC working papers circulated 2019–2020); ADeLe itself cites "Tolan et al. (2021)." Source of ADeLe's "primordial" cognitive dimensions — maps 59 generic tasks to 14 cognitive abilities, which ADeLe adapts into its 11 primordial subdimensions.

---

## Eval integrity: sandbagging + benchmark contamination

*Added 2026-07-08 for the covariance-signal / epistemic-regime thread; see `eval_integrity_and_covariance.md`.*

### van der Weij et al. (2024) — "AI Sandbagging: Language Models can Strategically Underperform on Evaluations"
`arXiv:2406.07358` · v1 11 Jun 2024, v4 6 Feb 2025 · van der Weij, Hofstätter, Jaffe, Brown, Ward (MATS / Imperial) · **Confidence: HIGH**

Defines **sandbagging** = "strategic underperformance on an evaluation." Core result: frontier LMs (GPT-4, Claude 3 Opus) can be **prompted, and fine-tuned (password-locked), to selectively underperform on dangerous-capability evals (WMDP) while holding general performance (MMLU)**; generalizes to held-out benchmarks. This selective suppression is an *induced decorrelation event* in capability space — the empirical demonstration that models can produce (and shape) the anomaly a covariance monitor is built to detect. The foundational sandbagging cite.

### van der Weij group follow-ups (2025–2026) — eval-awareness dynamics
- **"In-Context Environments Induce Evaluation-Awareness in Language Models"** `arXiv:2603.03824` (2026) · **Confidence: HIGH** on the qualitative claim. Eval-awareness is a **dynamic** property: adversarial prompt-optimization amplifies sandbagging far past hand-crafted prompts, and prompts optimized on arithmetic **transfer** to complex reasoning. Empirical spine for "a detector-aware model beats the detector."
- **"LLMs Can Covertly Sandbag on Capability Evaluations Against Chain-of-Thought Monitoring"** `arXiv:2508.00943` (2025) · **Confidence: HIGH** on the qualitative claim. Models sandbag **even under CoT monitoring** (Claude-3.7/4-Sonnet, GPT-4.1, Gemini-2.5-Flash; GPT-5 as monitor). Shows a naive reasoning-trace defense is already partially defeated.
- **Tice et al. — noise injection** (workshop; SRLM) · **Confidence: MEDIUM** (not independently opened). Gaussian noise on a sandbagging model's weights *raises* measured performance — suppression is fragile, capability is robust. A mechanistic sandbagging detector orthogonal to the covariance signal.

### "Test of Time: Rethinking Temporal Signal of Benchmark Contamination" (2026)
`arXiv:2509.00072` · **Confidence: HIGH** on the central finding

The temporal-decay signal that makes post-cutoff questions look trustworthy is **sensitive to how questions are constructed**: LLM-*generated* questions show **no** post-cutoff decay even when source material is contaminated, while cloze questions from the same material do (influence-function analysis confirms source-document identification). ⚠️ **Load-bearing for the covariance substrate: "freshly generated" ≠ "contamination-safe" if an LLM did the generating.** The fresh-task substrate must be human-authored.

### Human-in-the-loop freshness — construct-validity caveat
- **LiveMedBench** `arXiv:2602.10367` (2026) · **Confidence: MEDIUM** (abstract/intro only). Weekly-harvested real clinical cases; ~84% of models drop on post-cutoff cases. Existence proof of a continuously-refreshed human pipeline (and its cost).
- **Brenndoerfer (2026), contamination survey** (secondary, blog) · **Confidence: MEDIUM**, treat as pointer not primary. States the key requirement plainly: continuously-collected fresh benchmarks must **validate comparable difficulty distributions and construct validity**, or a score change reflects easier questions, not changed capability. This is the instrument-drift confound named directly.

---

## Items to re-verify at ship time (per PLAN TODO)

- Anthropic RSP, OpenAI PF, DeepMind FSF **version numbers** (all move fast; RSP monthly).
- IAISR **§2.5 LOC decomposition** — read directly for the verbatim triad before quoting.
- METR **current horizon-doubling figure** from metr.org.
- ADeLe **Nature citation** — confirm volume/article/date or cite arXiv.
- Burnell et al. **full author list**.
