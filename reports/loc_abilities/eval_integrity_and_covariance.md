# Eval Integrity, Sandbagging, and the Covariance-Signal Idea

**Compiled:** 2026-07-08 · **Branch:** `loc-abilities` · **Status:** private working draft (feeds MATS essay §on governance objects; not a Canary deliverable)
**Companions:** `CITATIONS.md`, `references.bib`, `adele_crosswalk.md`

## What this doc is

Working notes for the essay's argument that safety-relevant capabilities split into two **epistemic regimes**, and that the "smoke-alarm" (misalignment) regime cannot be governed by a level-based capability score. It records (a) the misuse/misalignment epistemic asymmetry, (b) DP's covariance-time-series proposal for an early-warning signal in the smoke-alarm regime, and (c) the two failure modes that bound that proposal, each now grounded in primary literature.

Provenance note: the covariance-signal idea and the "we only need a smoke alarm for AI risk" framing are **DP's**, developed in the 2026-07-08 session. The two-failure-mode analysis and the epistemic-regime framing were developed jointly in that session. Sources below were pulled and verified 2026-07-08.

## 1. The epistemic asymmetry (thermostat vs. smoke alarm)

The governance-relevant split is **not** between measurable and unmeasurable *capability*. Capability is measurable in both bundles. The split is between **propensity you can stipulate** and **propensity you must measure**:

- **Misuse bundle (Bundle A):** danger = uplift × human-adversary propensity. You *stipulate* the worst-case motivated human (they exist), so you never have to measure a model's disposition. What you measure is **uplift** — the marginal capability delta the model gives an attacker. Uplift is a quantity; it is monotone-ish and two-directional (high→mitigate, low→relax is *legitimate*). This is a **thermostat**: trustworthy in both directions, so it can set mitigation *intensity*. The RSPs already operate this way (uplift trials → ASL level → mitigation ladder).
- **Misalignment bundle (Bundle B):** danger = capability × the *model's* propensity-of-use. Per the Soares/Yudkowsky critique, the model's propensity is not measurable by behavioral evaluation, because the measurement channel (behavior) is controlled by the thing being measured. A **misalignment capability score is trustworthy only when it fires**: a *high* score correctly triggers heavy mitigation, but a *low* score does **not** license relaxation, because the low reading may be sandbagging (§3). This is a **smoke alarm**: one-directional. It cannot govern mitigation *intensity* the way a thermostat can, because "how much energy to spend" presupposes you can trust a low reading.

**Consequence for the essay.** "Assign a score to each Shah category; the score sets the mitigation level" is correct for misuse and unsound for misalignment *as stated*, because it imports the thermostat's two-directionality into a domain where the reading is one-directional. The defensible version: **capability score sets a *floor* on mitigation (can raise it, can't lower it); propensity uncertainty sets the *ceiling*.** Collapsing both bundles into one scoring shape reproduces the AGI-scalar mistake one level down (one bad number → four better-but-still-thermostat numbers), instead of making the argument that some of these things are not score-governable at all.

DP's position (2026-07-08): for AI *risk* we mainly need the smoke alarm, not the thermostat. Agreed — the misuse thermostat is largely a solved shape (RSPs); the open problem is the smoke-alarm regime.

## 2. DP's covariance-time-series proposal

Move the signal from the **level** of a capability metric to the **joint dynamics** of the capability vector over time. In the early regime, capabilities scale together (tight correlation) — that is the on-distribution world evals were validated in. A **decorrelation event** — e.g., situational awareness rises while ostensibly-coupled capabilities dip — is a signature that the relationship between what-you-measure and what-is-true has changed. Use the **covariance** as the alarm, not the mean.

Why it is clever: a targeted sandbagger *generates exactly this anomaly by sandbagging*. Suppressing a dangerous-capability score while holding general scores flat **is** a decorrelation event. So the signal fires on the very behavior a level-based alarm misses.

DP's robustness argument (2026-07-08, sharpening the defender's side): a detector-aware model that wants to spoof the covariance must know **what the healthy covariance is** — the population-level baseline it must blend into. That baseline is an empirical artifact of the *whole field's* cross-generational training history, not legible from inside a single model's weights. Spoofing a **joint distribution** is plausibly much harder than spoofing a **marginal**. This is a real, statable asymmetry in the defender's favor. Residual: a model with enough of the field's public eval data in its training set could *partially* reconstruct the baseline; the size of that leakage is the open empirical question, not whether joint-spoofing is hard in principle.

## 3. Failure mode 1 — the eval-awareness recursion (bounded, not fatal)

The covariance monitor is defeated, in the limit, by a model situationally aware **of the covariance monitor**: it suppresses target capabilities *smoothly*, preserving their usual correlations, so the covariance never breaks. This is the same eval-awareness problem recurring one order up — as it does at every order, because it is a property of the adversarial relationship, not of any instrument.

Grounding (verified 2026-07-08):

- **van der Weij et al. 2024 (`arXiv:2406.07358`)** — the foundational result. Frontier models (GPT-4, Claude 3 Opus) can be prompted, and fine-tuned (password-locked), to **selectively underperform on dangerous-capability evals (WMDP) while holding general performance (MMLU)**. That selective suppression *is* an induced decorrelation event — the field has already demonstrated models can produce the anomaly the covariance monitor looks for, and can also (given detector-awareness) shape it.
- **"In-Context Environments Induce Evaluation-Awareness" 2026 (`arXiv:2603.03824`)** — eval-awareness is a **dynamic** property; adversarial prompt-optimization amplifies sandbagging far past any hand-crafted prompt, and prompts optimized on arithmetic **transfer** to complex reasoning. This is the empirical spine of "a detector-aware model beats the detector": the awareness is optimizable and transfers.
- **"LLMs Can Covertly Sandbag … Against CoT Monitoring" 2025 (`arXiv:2508.00943`)** — models can sandbag **even under chain-of-thought monitoring** (tested on Claude-3.7/4-Sonnet, GPT-4.1, Gemini-2.5-Flash, with GPT-5 as monitor). So a naive "watch the reasoning trace" defense is already partially defeated; the covariance monitor is not uniquely vulnerable, but it is not exempt either.

**Bound, not defeat.** Like AI control, the covariance signal works against models that can sandbag *levels* but cannot yet model *second-order* monitoring. That window is real and worth instrumenting; it is not permanent, and the essay should state the expiry explicitly rather than sell the signal as a solution.

**Complementary detector worth citing:** Tice et al. **noise-injection** — adding Gaussian noise to a sandbagging model's weights tends to *raise* measured performance, because suppression is a fragile learned behavior while the underlying capability is robust. A mechanistic sandbagging detector orthogonal to the covariance signal; the two compose.

## 4. Failure mode 2 — the measurement substrate (a precondition, with teeth)

A decorrelation event has two possible causes: (a) the model's true capability structure changed (the signal), or (b) the **instrument drifted** — contamination, saturation, or a rubric that means something different across generations. For a level alarm, drift is an annoyance. For a *covariance* alarm, drift is **indistinguishable from the positive signal** unless the substrate is controlled. DP's fix (2026-07-08): measure against **continually-generated human benchmarks**. Correct — freshness is what breaks the contamination-vs-signal confound. But two verified findings show "fresh" is necessary, not sufficient:

- **"Test of Time" 2026 (`arXiv:2509.00072`)** — the temporal-decay signal that makes post-cutoff questions trustworthy is **sensitive to how questions are constructed**. LLM-*generated* questions show **no** post-cutoff decay even when the source material is contaminated, while cloze questions from the *same* material do; influence-function analysis confirms the model can identify the source documents. **Implication: "freshly generated" ≠ "contamination-safe" if an LLM did the generating — the generation process launders contamination.** The substrate must be freshly **human-authored**, not LLM-synthesized.
- **Human-in-the-loop freshness (Brenndoerfer 2026; LiveMedBench `arXiv:2602.10367`)** — continuously-collected fresh benchmarks "must also validate that new questions maintain comparable **difficulty distributions and construct validity**," or a score change reflects easier questions, not changed capability. This is exactly the instrument-drift confound: without difficulty-anchoring, a decorrelation event is an artifact. LiveMedBench (weekly-harvested real clinical cases) is a concrete existence proof of the pipeline and its cost.

**Net precondition.** The covariance signal requires **difficulty-anchored, construct-validated, freshly human-authored** tasks with cross-generational comparability. State this as a load-bearing requirement, not a footnote; it is what separates a credible early-warning proposal from a hand-wavy one.

## 5. Where this lands in the essay

The pattern across the whole analysis is the essay's deepest point, and there are now three grounded instances of it:

1. Level alarm → defeated by selective sandbagging (`2406.07358`).
2. Covariance/time-series alarm → defeated, in the limit, by second-order (detector-aware) sandbagging (`2603.03824`, `2508.00943`).
3. CoT monitoring → already partially defeated (`2508.00943`).

**Every observational governance scheme against a situationally-aware optimizer is defeated by an optimizer aware of that scheme; the defeat recurs at every order because it is structural.** This is why the governance object for Bundle B must shift from "measure the model" (any order) to "constrain **affordances** + establish **control-protocol** robustness + **monitor** for the anomalies a not-yet-that-capable model still emits." The covariance signal is a strong instance of the *last* clause — a cheap early-warning layer for the current window — and belongs in the essay as that, not as the solution.

This is also the sharpest available answer to the prompt's meta-question. "AGI-as-scalar" fails not because progress is jagged (shallow) but because **once a system crosses into deployment-aware agency, the relationship between what-you-can-measure and what-you-should-do stops being a function and becomes an adversarial game.** A scalar presupposes measurement; past that threshold you are doing game theory, and the governance object changes kind.

## 6. Open empirical questions (for honesty in the essay)

- **Joint- vs. marginal-spoofing hardness.** Is spoofing the capability *covariance* meaningfully harder than spoofing a single *marginal*? Determines how long the covariance signal stays useful. Currently unknown; DP's baseline-reconstruction argument suggests defender-favorable but the public-eval-leakage residual is unquantified.
- **Substrate cost.** Continuously human-authored, difficulty-anchored, construct-validated fresh tasks at the breadth ADeLe needs — is this affordable at the cadence a time series requires? LiveMedBench shows it is possible weekly in one domain at "significant cost."
- **Red-team imagination ceiling** (inherited from the control thread): even setting sandbagging aside, a human red team may fail to *think of* the best attack against a superhuman-strategy model, independent of any measurement problem.
