import sys, json, time
from noisy_lib import solve
sigmas = [0, 0.05, 0.1, 0.2, 0.4, 0.8, 1.2] if float(sys.argv[2] if len(sys.argv)>2 else 0) > 0 else [0, 0.025, 0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.6, 0.8, 1.2]
e = float(sys.argv[1]); delta = float(sys.argv[2]) if len(sys.argv) > 2 else 0
key = f"e={e},delta={delta}"
try: d = json.load(open("plot_D_data.json"))
except FileNotFoundError: d = {}
d.setdefault(key, {})
for sg in sigmas:
    if str(sg) in d[key]: continue
    t = time.time(); sf, p = solve(sg, e, 0, delta); d[key][str(sg)] = p
    print(key, sg, round(p, 3), f"{time.time()-t:.0f}s", flush=True)
    json.dump(d, open("plot_D_data.json", "w"), indent=1)
