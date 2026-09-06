# 20260906_racing_precipice_model

**Date:** 2026-09-06
**Branch:** main
**Surface:** claude.ai

## Summary
Dan added Armstrong/Bostrom/Shulman 2013 "Racing to the Precipice" and asked how realistic the model is, how to improve it, and what it says about treaties with and without verification. First pass: the model has no observable action variable and is one-shot, so verification is outside its expressive range; unverified treaties in-model are cheap talk acting only through enmity e. Dan's objections to the structure: capability and alignment are near-neighbors (human-modeling is necessary-not-sufficient for inner alignment); c − s subtracts incompatible quantities; the paper's s is really "Control" and it costs race time.

We rebuilt the model with a multiplicative race score c(1−s) (safety as effort share), then added a talent-feedback term (relative safety attracts researchers, per Anthropic-poaching-from-OpenAI) and a capability-dependent hazard. Solved no-info and private regimes numerically (best-response iteration), public regime analytically for the base case. Then checked the three follow-on papers Dan added concurrently (Askell/Brundage/Hadfield 2019, Naudé & Dimitri 2020, Han et al. 2020) for prior art.

## Topics Explored
- Realism critique of ABS 2013: 1:1 safety/capability exchange rate; binary terminal disaster with known probability; one-shot; flat symmetric structure (no nested labs-in-states, e>1 out of scope); no safety spillovers.
- ABS gets right: public-info s_top = Δ/e is Aschenbrenner's "a lead lets you afford safety" a decade early; regime assignment matters (2013 was no-info, today is roughly public-info ⇒ model points at *leaders in close races*, not laggards).
- Multiplicative reformulation and its comparative statics.
- Talent channel: relative, not absolute; bites only on the deviation margin; requires s to be perceived (employees as inspectors).
- Catch-up bonus: irrelevant to no-info/private (monotone relabeling of c); bites only in public regime by compressing ratios.
- Prior-art check against the three new papers.

## Provisional Findings
- **µ vanishes under multiplicative score.** No-info s* = 1/(1+e(n−1)); private-info ODE has the same constant as its only bounded solution, so private = no-info and the paper's private-info information hazard disappears. The lever that replaces µ is dispersion of capability *ratios* (fixed by n for uniform draws; would be a real parameter under lognormal). Public info marginally worse at e=0.5, identical at e=1.
- **Multiplicative model is grimmer and flatter**: a lead is never unassailable; leader sits at the laggard's indifference point; e and n are the only levers.
- **Exact risk compensation under no-info**: P(disaster) = e(n−1)/(1+e(n−1)) for *any* hazard multiplier (Peltzman effect; H̄ cancels in the FOC). Hazard-side interventions (safety R&D, better tooling) are fully compensated; incentive-side ones (e, n, deviation costs) are not. Caveats: exact only because disaster is linear in s; continuous-choice phenomenon (Han et al.'s binary SAFE/UNSAFE can't compensate); **under private information it does NOT hold** — plot B shows P(dis) falling with γ, roughly half the hazard benefit survives. (Claude initially said "approximately holds" from one data point; corrected by plot B.)
- **Talent feedback is the largest lever found**: ~40% reduction in P(dis) at λ=1, near-linear in λ, no saturation in range. Survives compensation because it's a deviation tax. Policy handle: labor mobility (non-competes, visas, vesting) and whistleblower protection are verification infrastructure because they make λ>0. FRONTIER dropping the whistleblower title reads differently through this lens.
- **Capability-dependent hazard + private info**: laggards go to s=0 (not dangerous, don't bother), leaders keep 0.3–0.5. "Who to worry about" points at leaders even in private regime; consistent with July 2026 incidents (both at frontier labs).
- **Compute-verification tension** (from first pass): compute is a capability proxy; in ABS, capability transparency is the information hazard; a compute-accounting treaty raises detection on the s-floor and moves toward public-capability regime simultaneously. Net sign depends on e. Not seen in Baker/Scher verification literature.
- **Sharpest staffer sentence** (first pass): without verification there is no trigger for any grim-trigger strategy, since disaster can't be the trigger; the game collapses to one-shot no matter how many years it runs.
- **Prior art**: Naudé & Dimitri has no safety variable (can't have µ-independence). Han et al. is multiplicative in speed but safety is binary, so no compensation margin; BUT they already have a monitoring probability p_fo (= our (s_min, p, D) with D pinned to one round's payoff). Their late-DSAI "lower monitoring" claim rests on assuming unsafe development yields more per-round welfare — examine before repeating. Askell et al. is prose over a PD. Han group's 2026 human-subjects paper (arXiv 2607.26034) is evidence for laggards-cut-corners. Distinguish "who cuts corners" (laggards, empirically) from "who causes disasters" (leaders, if hazard scales with capability).

## Decisions Made
- Convo name confirmed: 20260906_racing_precipice_model.
- Working order agreed: (1) private-info version of the talent plot; (2) add treaty term (s_min, p, D) and ask whether verification penalties survive compensation like λ or get eaten like hazard shifts; (3) Dan's content-verification post (canaryinstitute.ai/blog/cant-trust-then-verify/) as a different observable from compute.
- Dan's next-factor list (queued, not yet modeled): outcome uncertainty (choice yields a draw, not a known s); laggards have larger step size; second-place takes bigger risks to catch up; relative status is uncertain and *perceived* gap creates desperation.

## Results
- `results/20260906_race_models/` — README (model spec + analytic results), solvers, plot B (risk compensation vs γ), plot C (talent lever vs λ).

## Open Questions
- Does compensation hold in the additive (ABS) model? Suspect not (µ enters deviation gain).
- Does the (s_min, p, D) treaty term survive compensation?
- n=2 private-info bump at γ=0.5 in plot B: real or solver noise?
- Lognormal capabilities: does ratio dispersion become the honest replacement for µ?
- Talent term modeling choice: deviator's effect on others' s̄ included; alternatives exist.
- Which of Dan's four queued factors actually move the equilibrium?
