import numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from race_lib import noinfo
combos = [(2, 0.5), (2, 1.0), (5, 0.5), (5, 1.0)]

lams = [0, 0.25, 0.5, 0.75, 1.0, 1.5]
fig, ax = plt.subplots(figsize=(6, 4))
for n, e in combos:
    ax.plot(lams, [noinfo(n, e, l, 0)[1] for l in lams], "o-", label=f"n={n}, e={e}")
ax.set(xlabel="lambda (talent sensitivity to relative safety)", ylabel="P(disaster)", title="Talent mobility as a deviation tax (no-info, gamma=0)")
ax.legend(); fig.tight_layout(); fig.savefig("plot_C_talent_lever.png", dpi=130); print("C done")
