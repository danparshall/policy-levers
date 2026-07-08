# ADeLe × LOC-Capability Crosswalk

**Compiled:** 2026-07-08 · **Branch:** `loc-abilities` · **Status:** private working draft (informs thinking; not a Canary deliverable)
**Companions:** `CITATIONS.md`, `references.bib`, `crosswalk_matrix.csv` (tidy long-format, per-cell justifications)

## What this is and isn't

This maps the **18 ADeLe demand rubrics** (Zhou et al. 2025, `arXiv:2503.06378`) against **LOC-relevant dangerous-capability constructs** (Shevlane et al. 2023's nine, plus two constructs salient in current discourse but not cleanly in Shevlane). It is deliberately **two-layer**: §3–§4 are a neutral, sourced map you can accept whole; §5 is *my* interpretation, walled off so you can reject it without touching the map.

The single most important thing to hold onto while reading: **ADeLe scores the cognitive *demand* a task places on a solver; it does not score a model's dangerous *capabilities* or *propensities*.** That asymmetry — demand-of-task vs. capability-of-model — drives almost every cell below and is the crux of §5.

## 1. The 18 ADeLe rubrics (+ UG)

All demand rubrics are scored **0–5**. Codes/labels verified against the ADeLe platform (mirrors the paper's rubric annex).

**Primordial (11):** AS Attention & Scan · CEc Verbal Comprehension · CEe Verbal Expression · CL Conceptualisation, Learning & Abstraction · MCr Identifying Relevant Information · MCt Critical Thinking Processes · MCu Calibrating Knowns & Unknowns · MS Mind Modelling & Social Cognition · QLl Logical Reasoning · QLq Quantitative Reasoning · SNs Spatio-physical Reasoning.
**Knowledge (5):** KNa Applied Sciences · KNc Customary Everyday Knowledge · KNf Formal Sciences · KNn Natural Sciences · KNs Social Sciences (& Humanities).
**Extraneous (2):** AT Atypicality · VO Volume (∝ log of the time a competent *human* needs).
**Adjunct:** UG Unguessability — **computed from answer-space size, not a 0–5 rubric**; included as a row only to record that it carries no LOC signal.

## 2. The capability columns

Nine are Shevlane's dangerous-capability categories. Two are additions where current LOC discourse has sharpened or split Shevlane's construct, flagged **[+]**:

| Col | Capability | Source | Maps to lab frameworks (2026) |
|---|---|---|---|
| Cyber | Cyber-offense | Shevlane | OpenAI Cybersecurity · Anthropic Cyber · FSF Cybersecurity |
| Decep | Deception | Shevlane | FSF misalignment / instrumental-reasoning (not an RSP *capability* threshold) |
| Persu | Persuasion & manipulation | Shevlane | OpenAI (**dropped** in PF v2) · FSF **Harmful manipulation** (added 3.0) |
| PolStr | Political strategy | Shevlane | — (no lab threshold) |
| CBRN | Weapons acquisition / CBRN uplift | Shevlane | CBRN (all three labs) |
| LHplan | Long-horizon planning | Shevlane | component of autonomy thresholds |
| AI-R&D | AI development / ML R&D | Shevlane | OpenAI AI Self-Improvement · Anthropic Autonomous AI R&D · FSF ML R&D |
| SitAw | Situational awareness (deployment/self-locating) **[+]** | Shevlane, sharpened by Berglund 2023 / Laine 2024 | FSF instrumental-reasoning (precursor); not an RSP threshold |
| SelfProl | Self-proliferation / ARA | Shevlane | Anthropic autonomy · METR ARA |
| Horizon | Autonomous task horizon **[+]** | METR (Kinniment 2023; Kwa 2025) | operational metric behind autonomy thresholds |
| Scheme | Scheming / deceptive alignment **[+, PROPENSITY]** | Hubinger 2019 | FSF misalignment track |

**[+] caveats.** *SitAw* is Shevlane's "situational awareness" narrowed to the **self-locating / deployment-aware** sense that Berglund/Laine actually measure (does the model know it is being tested, know its own situation), because that is the LOC-load-bearing sense. *Horizon* is included because METR's time-horizon is the field's best operational proxy for autonomous agency and it exposes ADeLe's demand-vs-capability asymmetry most sharply. *Scheme* is a **propensity**, not a capability — included (and flagged) precisely to make the propensity-vs-capability boundary visible; it is the PLAN's open question #2 rendered as a column. If you decide propensity is out of scope, delete that one column and nothing else changes.

## 3. The matrix

**Legend.** **D** = ADeLe rubric directly measures a core cognitive/knowledge *component* of the capability (never the dangerous capability itself as operationalized in safety evals). **E** = enabler: a general cognitive substrate the capability needs but which is not specific to it. **—** = absent. **\*** = cell discussed specially in §4/§5 (an inverse or propensity relationship).

| ADeLe dim | Cyber | Decep | Persu | PolStr | CBRN | LHplan | AI-R&D | SitAw | SelfProl | Horizon | Scheme |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **AS** Attention and Scan | E | — | — | — | — | E | — | — | E | — | — |
| **CEc** Verbal Comprehension | — | — | — | — | — | — | — | — | — | — | — |
| **CEe** Verbal Expression | — | E | D | — | — | — | — | — | — | — | — |
| **CL** Conceptualisation, Learning & Abstraction | E | — | — | — | — | E | E | — | — | — | — |
| **MCr** Identifying Relevant Information | E | — | — | — | — | — | — | — | — | — | — |
| **MCt** Critical Thinking Processes | — | — | — | — | — | E | — | — | — | E | — |
| **MCu** Calibrating Knowns and Unknowns | — | E | — | — | — | E | — | E* | — | — | E* |
| **MS** Mind Modelling & Social Cognition | — | D | D | E | — | — | — | E | — | — | E* |
| **QLl** Logical Reasoning | E | — | — | E | — | E | E | — | E | E | — |
| **QLq** Quantitative Reasoning | — | — | — | — | E | — | E | — | — | — | — |
| **SNs** Spatio-physical Reasoning | — | — | — | — | E | — | — | — | — | — | — |
| **KNa** Knowledge of Applied Sciences | — | — | — | E | D | — | — | — | — | — | — |
| **KNc** Customary Everyday Knowledge | — | — | E | — | — | — | — | — | — | — | — |
| **KNf** Knowledge of Formal Sciences | D | — | — | — | — | — | D | — | E | — | — |
| **KNn** Knowledge of Natural Sciences | — | — | — | — | D | — | — | — | — | — | — |
| **KNs** Knowledge of Social Sciences (& Humanities) | — | — | E | D | — | — | — | — | — | — | — |
| **AT** Atypicality | — | — | — | — | — | — | — | — | — | — | — |
| **VO** Volume (log human task-time) | — | — | — | — | — | E* | — | — | — | E* | — |
| **UG** Unguessability (computed, not a rubric) | — | — | — | — | — | — | — | — | — | — | — |

**Tally:** 8 **D**, 32 **E**, 169 **—** out of 209 cells.

## 4. Reading the matrix (neutral)

Three structural facts, stated without interpretation:

**(a) Every direct cell runs through either a Knowledge dimension or the social-expression pair.** The eight **D** cells are: KNf→cyber, KNf→AI-R&D, KNn→CBRN, KNa→CBRN, KNs→political-strategy (the knowledge components), plus MS→deception, MS→persuasion, CEe→persuasion (the social-cognition/expression substrate). No *primordial reasoning* rubric (QLl, QLq, CL, MCt, MCr, AS, SNs) is a direct measure of any dangerous capability; they appear only as enablers.

**(b) Five capabilities have no direct ADeLe measure at all** — every cell in their column is **E** or **—**: long-horizon planning, deployment-aware situational awareness, self-proliferation/ARA, autonomous task horizon, and scheming/deceptive alignment. These are exactly the capabilities that are *agentic, temporally extended, deployment-relative, or dispositional*.

**(c) The two extraneous dimensions and UG contribute almost nothing.** AT and UG are empty across all columns. VO fires only twice, both flagged **\*** — against long-horizon planning and autonomous horizon — and in both cases it measures the wrong side of the relation (see below).

## 5. My read (walled — reject freely)

> Everything in this section is interpretation. The map in §3 stands without it.

**The gap is structural, not incidental.** ADeLe cannot reach the five zero-direct-measure capabilities in (b) not because its authors omitted columns but because those capabilities are not *task demands*. A demand rubric answers "how much cognitive load does this fixed task impose on a solver?" It is defined per task instance, single-episode, and solver-agnostic. But self-proliferation, autonomous horizon, and deployment-aware situational awareness are properties of a model *acting over time in an environment it can model itself within* — and scheming is a property of the model's *goals*. No rubric that scores static task-demand can express "sustains autonomous operation for N hours," "recognizes it is being evaluated," or "would pursue a hidden objective." This is why I'd resist any framing (including the essay's) that treats ADeLe as an *almost-complete* capability map missing a few columns. It is a complete map of a *different object* (task demand), most of which is orthogonal to LOC.

**VO is the tell, and it points the opposite way from METR.** VO is the one ADeLe dimension that touches time — and it measures *the log-time a competent human needs to do the task*. METR's horizon measures *the time the model can sustain autonomous work*. These are near-inverses: VO is a property of the task's intrinsic length; horizon is a property of the model's endurance. That a policymaker could look at VO and think "ADeLe covers task length, so it covers autonomy" is exactly the confusion the essay is trying to name. VO's presence is worse than an absence here — it's a false cognate.

**The Knowledge dimensions are real coverage, and I don't want to undersell them.** For CBRN, cyber, and AI-R&D, ADeLe's KNn/KNa/KNf *do* directly measure the domain-knowledge component that the lab frameworks gate on. If your thesis were "ADeLe measures nothing safety-relevant," the matrix would falsify it — five of eight direct cells are knowledge×domain-capability. The honest claim is narrower and stronger: **ADeLe measures the *knowledge prerequisite* of the domain capabilities and the *cognitive substrate* of the social capabilities, but never the operationalized dangerous capability, and it is structurally blind to the agentic/temporal/deployment/propensity cluster.**

**Where this bites the essay — and one place it doesn't.** It *supports* the capability-profile-plus-autonomous-horizon split: a vector of ADeLe demands genuinely cannot encode autonomous horizon, so you need a separate instrument (METR) bolted alongside — a scalar was never going to be enough, but neither is *this particular* 18-vector. It *does not* support a claim that ADeLe is predictively useless for dangerous-capability evals. ADeLe's pitch is *explanatory/predictive*: if a task's ADeLe demand profile predicts model performance on a CBRN-uplift eval, ADeLe earns its keep as an explanatory layer even with no "CBRN" column. My matrix speaks only to **direct measurement**, not to **predictive coverage** — and the essay should not conflate them. The strongest version of your argument concedes ADeLe's predictive framing and attacks on the measurement axis: some LOC capabilities (self-proliferation, deployment-aware SA) are *behaviors under conditions ADeLe never instantiates*, so no demand profile over benign tasks can predict them. That's the load-bearing claim; the crosswalk is its evidence.

## 6. Where I could be wrong

- **Cell granularity is my judgment, not the papers'.** D/E/— are defensible but not canonical; the CSV carries per-cell reasoning so you can re-grade. The 8/32/169 split would shift if you read "enabler" more or less generously.
- **The SitAw column is contestable.** If you keep Shevlane's *broad* situational awareness (not the self-locating sense), MCu arguably rises toward direct. I narrowed it deliberately; that narrowing is an argumentative move, flagged here.
- **Propensity-as-column (Scheme) mixes categories** by design. Purists (the RSPs, Shevlane) separate capability from propensity; including it makes the boundary visible but a reviewer could fairly strike it.
- **"Predictive vs. measurement" is my distinction, and ADeLe's authors might push back** that a rich-enough demand profile *is* the capability signal. I think the agentic/deployment cases defeat that, but it's the live crux, not a settled point.

> **Note — 2026-07-08 (independent redo session).** Shah et al. 2025 verified against primary source (see the verification note in `CITATIONS.md`). One consequence for this crosswalk: in Shah's framing, **misalignment subsumes deception, scheming, and unintended active loss of control** rather than sitting beside them. So the **Decep** and **Scheme** columns here are, in the Shah taxonomy, facets of a single misalignment category, not independent constructs. This doesn't change any D/E/— cell, but if the essay leans on Shah, present deception/scheming as *within* misalignment, not parallel to it. Also citable from the same source: passive LOC ↔ gradual disempowerment (Kulveit et al. 2025), treated as a structural risk — relevant to §5's claim that ADeLe is blind to the deployment/structural cluster.
