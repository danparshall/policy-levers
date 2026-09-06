"""Shared solver for the multiplicative AI race model (see README in this dir).
score_i = c_i*(1-s_i)*(1+lam*(s_i - sbar_others)); winner = argmax.
disaster | winner = (1-s_w)*c_w**gamma.  payoffs: own success 1, other's 1-e, disaster 0.
"""
import numpy as np
rng = np.random.default_rng(1)

def payoff_dev(c, s_dev, s_oth, e, lam, gamma):
    N, n = c.shape
    if np.isscalar(s_dev): s_dev = np.full(N, s_dev)
    all_s = np.concatenate([s_dev[:, None], s_oth], 1)
    sbar_me = s_oth.mean(1)
    sbar_oth = (all_s.sum(1, keepdims=True) - s_oth) / (n - 1)
    my = c[:, 0] * (1 - s_dev) * (1 + lam * (s_dev - sbar_me))
    oth = c[:, 1:] * (1 - s_oth) * (1 + lam * (s_oth - sbar_oth))
    win = my > oth.max(1)
    j = oth.argmax(1); idx = np.arange(N)
    succ_me = 1 - (1 - s_dev) * c[idx, 0] ** gamma
    succ_j = 1 - (1 - s_oth[idx, j]) * c[idx, 1:][idx, j] ** gamma
    return np.where(win, succ_me, (1 - e) * succ_j).mean()

def noinfo(n, e, lam, gamma, N=20000, iters=12, S=np.linspace(0, 1, 41)):
    s = 0.5
    for _ in range(iters):
        c = rng.uniform(0, 1, (N, n)); s_oth = np.full((N, n - 1), s)
        best = max(S, key=lambda sd: payoff_dev(c, sd, s_oth, e, lam, gamma))
        s = 0.5 * s + 0.5 * best
    c = rng.uniform(0, 1, (N, n)); w = c.argmax(1)   # symmetric s: max c wins
    return s, ((1 - s) * c[np.arange(N), w] ** gamma).mean()

def private(n, e, lam, gamma, N=20000, iters=10, G=10, S=np.linspace(0, 1, 41)):
    grid = np.linspace(0.05, 0.95, G); sf = np.full(G, 0.5)
    for _ in range(iters):
        c = rng.uniform(0, 1, (N, n)); s_oth = np.interp(c[:, 1:], grid, sf)
        new = np.empty(G)
        for gi, cg in enumerate(grid):
            cc = c.copy(); cc[:, 0] = cg
            new[gi] = max(S, key=lambda sd: payoff_dev(cc, sd, s_oth, e, lam, gamma))
        sf = 0.5 * sf + 0.5 * new
    c = rng.uniform(0, 1, (N, n)); s_all = np.interp(c, grid, sf)
    scr = c * (1 - s_all) * (1 + lam * (s_all - (s_all.sum(1, keepdims=True) - s_all) / (n - 1)))
    w = scr.argmax(1); idx = np.arange(N)
    return sf, ((1 - s_all[idx, w]) * c[idx, w] ** gamma).mean()
