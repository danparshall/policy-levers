"""Noisy-signal regime, n=2.  Team i knows own c_i and sees y = c_j + N(0, sigma^2).
Policy s(c, gap) with gap = y - c (perceived deficit if positive).  sigma=0 -> public; sigma large -> private.
Desperation: win payoff x (1 + delta*max(0, gap)).  Multiplicative score, talent lam, hazard gamma=0.
"""
import numpy as np
from scipy.stats import norm
rng = np.random.default_rng(2)
CG = np.linspace(0.05, 0.95, 8)          # own capability grid
GG = np.linspace(-0.9, 0.9, 9)           # perceived gap grid
SS = np.linspace(0, 1, 21)

def policy(sf, c, gap):
    """bilinear interp of s on (CG, GG)."""
    from scipy.interpolate import RegularGridInterpolator
    f = RegularGridInterpolator((CG, GG), sf, bounds_error=False, fill_value=None)
    pts = np.stack([np.clip(c, CG[0], CG[-1]), np.clip(gap, GG[0], GG[-1])], -1)
    return np.clip(f(pts), 0, 1)

def posterior_cj(y, sigma, N):
    """sample other's capability given my signal y (prior U[0,1])."""
    if sigma == 0: return np.full(N, np.clip(y, 0, 1))
    cand = rng.uniform(0, 1, 4 * N); w = norm.pdf((y - cand) / sigma); w /= w.sum()
    return rng.choice(cand, N, p=w)

def cell_best(sf, cg, gap, sigma, e, lam, delta, N=20000):
    y = cg + gap; cj = posterior_cj(y, sigma, N)
    yj = cg + rng.normal(0, sigma, N) if sigma > 0 else np.full(N, cg)   # j's signal of me
    sj = policy(sf, cj, yj - cj)
    best, bv = 0.5, -1
    for s in SS:
        my = cg * (1 - s) * (1 + lam * (s - sj)); th = cj * (1 - sj) * (1 + lam * (sj - s))
        win = my > th
        v = np.where(win, s * (1 + delta * max(0, gap)), (1 - e) * sj).mean()
        if v > bv: bv, best = v, s
    return best

def solve(sigma, e, lam=0, delta=0, iters=16):
    sf = np.full((len(CG), len(GG)), 0.5)
    for _ in range(iters):
        new = np.array([[cell_best(sf, cg, g, sigma, e, lam, delta) for g in GG] for cg in CG])
        sf = 0.5 * sf + 0.5 * new
    # equilibrium disaster
    N = 200_000; c = rng.uniform(0, 1, (N, 2)); nz = rng.normal(0, sigma, (N, 2))
    g0 = (c[:, 1] + nz[:, 0]) - c[:, 0]; g1 = (c[:, 0] + nz[:, 1]) - c[:, 1]
    s0 = policy(sf, c[:, 0], g0); s1 = policy(sf, c[:, 1], g1)
    sc0 = c[:, 0] * (1 - s0) * (1 + lam * (s0 - s1)); sc1 = c[:, 1] * (1 - s1) * (1 + lam * (s1 - s0))
    sw = np.where(sc0 > sc1, s0, s1)
    return sf, float((1 - sw).mean())
