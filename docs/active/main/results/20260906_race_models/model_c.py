"""Model C: multiplicative race + talent feedback + capability-dependent hazard.
score_i = c_i*(1-s_i)*(1+lam*(s_i - sbar_others)); winner = argmax score.
disaster | winner i = (1-s_i)*(c_i/mu)^gamma.  utilities: own success 1, other 1-e, disaster 0.
Symmetric Nash via best-response iteration (no-info: scalar s; private: s(c) on grid).
mu = 1 WLOG (multiplicative form is scale-free).
"""
import numpy as np
rng = np.random.default_rng(1)
N = 40_000
S = np.linspace(0, 1, 41)

def draw(n): return rng.uniform(0, 1, (N, n))

def payoff_dev(c, s_dev_score, s_dev_haz, s_oth, e, lam, gamma):
    """Expected utility of team 0 deviating to s_dev while others play s_oth (array (N,n-1))."""
    n = c.shape[1]
    sbar_oth = s_oth.mean(1)
    my = c[:, 0]*(1-s_dev_score)*(1+lam*(s_dev_score - sbar_oth))
    # others' sbar includes deviator + rest; approximate by mean of all incl deviator
    all_s = np.concatenate([np.full((N,1), s_dev_score), s_oth], 1) if np.isscalar(s_dev_score) else np.concatenate([s_dev_score[:,None], s_oth],1)
    sbar_for_j = (all_s.sum(1, keepdims=True) - s_oth)/(n-1)
    oth = c[:, 1:]*(1-s_oth)*(1+lam*(s_oth - sbar_for_j))
    win = my > oth.max(1)
    succ_me = 1 - (1-s_dev_haz)*c[:,0]**gamma
    j = oth.argmax(1); cj = c[np.arange(N), 1:][np.arange(N), j]; sj = s_oth[np.arange(N), j]
    succ_j = 1 - (1-sj)*cj**gamma
    return np.where(win, succ_me, (1-e)*succ_j).mean()

def noinfo(n, e, lam, gamma, iters=15):
    s = 0.5
    for _ in range(iters):
        c = draw(n); s_oth = np.full((N, n-1), s)
        best = max(S, key=lambda sd: payoff_dev(c, sd, sd, s_oth, e, lam, gamma))
        s = 0.5*s + 0.5*best
    c = draw(n); s_oth = np.full((N,n-1), s)
    # disaster prob at equilibrium: winner's (1-s)c^gamma
    scr = c*(1-s); w = scr.argmax(1); cw = c[np.arange(N), w]
    return s, ((1-s)*cw**gamma).mean()

def private(n, e, lam, gamma, iters=12, G=12):
    grid = np.linspace(0.025, 0.975, G); sfun = np.full(G, 0.5)
    def interp(x, f): return np.interp(x, grid, f)
    for _ in range(iters):
        c = draw(n); s_oth = interp(c[:,1:], sfun)
        new = np.empty(G)
        for gi, cg in enumerate(grid):
            cc = c.copy(); cc[:,0] = cg
            new[gi] = max(S, key=lambda sd: payoff_dev(cc, sd, sd, s_oth, e, lam, gamma))
        sfun = 0.5*sfun + 0.5*new
    c = draw(n); s_all = interp(c, sfun); scr = c*(1-s_all); w = scr.argmax(1)
    idx = np.arange(N); dis = ((1-s_all[idx, w])*c[idx, w]**gamma).mean()
    return sfun, dis

print("no-info:  (n,e,lam,gamma) -> s*, P(disaster)")
for n in (2,5):
  for e in (0.5,1.0):
    for lam in (0, 0.5, 1.0):
      for gamma in (0,1):
        s, d = noinfo(n,e,lam,gamma)
        print(f"  n={n} e={e} lam={lam:<3} gamma={gamma}: s*={s:.2f}  P(dis)={d:.2f}")
print("\nprivate info (lam=0): s(c) at c=0.1,0.5,0.9 and P(disaster)")
for n in (2,5):
  for e in (0.5,1.0):
    for gamma in (0,1):
        sf, d = private(n,e,0,gamma)
        print(f"  n={n} e={e} gamma={gamma}: s(0.1)={np.interp(0.1,np.linspace(0.025,0.975,20),sf):.2f} s(0.5)={np.interp(0.5,np.linspace(0.025,0.975,20),sf):.2f} s(0.9)={np.interp(0.9,np.linspace(0.025,0.975,20),sf):.2f}  P(dis)={d:.2f}")
