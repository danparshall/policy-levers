"""Plot C2: talent lever under private information (each team knows own c). Saves data to json for later re-plotting."""
import sys, json, numpy as np
from race_lib import private, noinfo
lams = [0, 0.25, 0.5, 0.75, 1.0, 1.5]
combos = [(2, 0.5), (2, 1.0), (5, 0.5), (5, 1.0)]
which = [int(i) for i in sys.argv[1:]] or range(len(combos))
out = {}
for i in which:
    n, e = combos[i]
    out[f"{n},{e}"] = {"private": [float(private(n, e, l, 0)[1]) for l in lams],
                       "noinfo": [float(noinfo(n, e, l, 0)[1]) for l in lams]}
    print(n, e, out[f"{n},{e}"], flush=True)
try: old = json.load(open("plot_C2_data.json"))
except FileNotFoundError: old = {}
old.update(out); old["lams"] = lams
json.dump(old, open("plot_C2_data.json", "w"), indent=1)
