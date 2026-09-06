<!-- Generated during: convos/20260906_racing_precipice_model.md -->
# Race-model extensions of Armstrong/Bostrom/Shulman 2013

## Model (one shot, n teams)
1. Capabilities c_i ~ iid Uniform[0, 1] (multiplicative form is scale-free; µ=1 WLOG).
2. Each team picks a safety share s_i ∈ [0,1] (fraction of effort spent on control rather than capability).
3. Race score: score_i = c_i · (1 − s_i) · (1 + λ(s_i − s̄_others)).  λ = talent feedback (safer-than-peers labs attract researchers). λ=0 is the plain multiplicative model.  ABS 2013 uses c_i − s_i.
4. Highest score wins.
5. Disaster | winner = (1 − s_w) · c_w^γ.  γ=0 is the ABS hazard; γ=1 makes more capable systems proportionally more dangerous.
6. Payoffs: 1 own success, 1−e other's success, 0 disaster.  e = enmity.

Information regimes: no-info (scalar s), private (s(c)), public (only solved analytically for λ=0, γ=0).

## Files
- `mult_model.py` — closed-form additive vs multiplicative comparison, all three regimes (first table in convo).
- `race_lib.py` — shared numerical solver (symmetric Nash via best-response iteration, Monte Carlo payoffs).
- `model_c.py` — original solver script (superseded by race_lib.py; kept for provenance).
- `plot_B_C.py`, `plot_C.py` — plot generators.
- `plot_B_risk_compensation.png` — s* and P(disaster) vs γ, no-info (solid) and private (dashed). Dotted references: e(n−1)/(1+e(n−1)).
- `plot_C_talent_lever.png` — P(disaster) vs λ, no-info, γ=0.

## Analytic results (multiplicative, λ=0, γ=0)
- No-info: s* = 1/(1+e(n−1)); P(dis) = e(n−1)/(1+e(n−1)). µ drops out.
- Private: ODE c·s' = 1 − s(1+e(n−1)); only bounded solution is the same constant. Private = no-info.
- Public: s_top = (r−1)/(r−1+e), r = c₁/c₂. For e=1, P(dis) = E[c₂/c₁] = (n−1)/n.
- No-info compensation (any hazard multiplier H): D = (1−s)H̄, FOC (1−D)e(n−1) = D ⇒ D independent of H. Exact only because disaster is linear in s.

Numerical caveats: N=20k–40k draws, safety grid 41 points, private-info grid 10–12 points; ±0.02 on probabilities.
