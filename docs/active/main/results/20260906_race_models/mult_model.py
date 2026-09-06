"""Additive (Armstrong-Bostrom-Shulman) vs multiplicative race models.
Multiplicative: score = c*(1-s); s = fraction of effort on safety; success prob = s.
"""
import numpy as np
rng = np.random.default_rng(0)

def additive(n, e, mu, N=400_000):
    c = rng.uniform(0, mu, (N, n))
    # no info
    s0 = min(1, mu/(e*n)); p_no = 1 - s0
    # private: s(x)=min(1, x/(en-e+1)); winner = max c
    x = c.max(1); p_pr = (1 - np.minimum(1, x/(e*n-e+1))).mean()
    # public: s_top = min(1, delta/e)
    cs = np.sort(c, 1); d = cs[:, -1] - cs[:, -2]; p_pu = (1 - np.minimum(1, d/e)).mean()
    return p_no, p_pr, p_pu

def multiplicative(n, e, mu, N=400_000):
    c = rng.uniform(0, mu, (N, n))
    k = 1 + e*(n-1)
    p_no = 1 - 1/k          # derived: s = 1/(1+e(n-1)), mu-independent
    p_pr = p_no             # private-info ODE gives the same constant s
    cs = np.sort(c, 1); r = cs[:, -1]/cs[:, -2]  # capability ratio top/second
    s_top = (r-1)/(r-1+e)
    p_pu = (1 - s_top).mean()
    return p_no, p_pr, p_pu

print(f"{'n':>2} {'e':>4} {'mu':>4} | additive no/priv/pub  | multiplicative no/priv/pub")
for n in (2, 5):
    for e in (0.5, 1.0):
        for mu in (0.5, 1, 2, 5):
            a = additive(n, e, mu); m = multiplicative(n, e, mu)
            print(f"{n:>2} {e:>4} {mu:>4} | {a[0]:.2f} {a[1]:.2f} {a[2]:.2f}       | {m[0]:.2f} {m[1]:.2f} {m[2]:.2f}")
