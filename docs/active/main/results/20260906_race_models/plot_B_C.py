import numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from race_lib import noinfo, private
combos = [(2, 0.5), (2, 1.0), (5, 0.5), (5, 1.0)]
# --- B: risk compensation vs gamma
gammas = [0, 0.5, 1, 1.5, 2]
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
for n, e in combos:
    ss, ds, dp = [], [], []
    for g in gammas:
        s, d = noinfo(n, e, 0, g); ss.append(s); ds.append(d)
        _, d2 = private(n, e, 0, g); dp.append(d2)
    ax[0].plot(gammas, ss, "o-", label=f"n={n}, e={e}")
    l, = ax[1].plot(gammas, ds, "o-", label=f"n={n}, e={e} (no-info)")
    ax[1].plot(gammas, dp, "s--", color=l.get_color(), alpha=.6, label=f"n={n}, e={e} (private)")
    ax[1].axhline(e*(n-1)/(1+e*(n-1)), color=l.get_color(), lw=.5, ls=":")
ax[0].set(xlabel="gamma (hazard steepness in capability)", ylabel="equilibrium safety share s*", title="Teams cut precaution as hazard falls")
ax[1].set(xlabel="gamma", ylabel="P(disaster)", title="...and disaster probability barely moves"); ax[1].legend(fontsize=7)
ax[0].legend(fontsize=8); fig.tight_layout(); fig.savefig("plot_B_risk_compensation.png", dpi=130)
print("B done")
# --- C: talent lever
lams = [0, 0.25, 0.5, 0.75, 1.0, 1.5]
fig, ax = plt.subplots(figsize=(6, 4))
for n, e in combos:
    ax.plot(lams, [noinfo(n, e, l, 0)[1] for l in lams], "o-", label=f"n={n}, e={e}")
ax.set(xlabel="lambda (talent sensitivity to relative safety)", ylabel="P(disaster)", title="Talent mobility as a deviation tax (no-info, gamma=0)")
ax.legend(); fig.tight_layout(); fig.savefig("plot_C_talent_lever.png", dpi=130); print("C done")
