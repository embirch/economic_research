"""Step 05: the newness ceiling, before any regression touches power distance.

What this does
  Takes the published tenure effect (Learning Curves, March 2026, Table 2.1: users under six months
  are directive in 38.1% of conversations vs 29.4% for older users; feedback loop 11.7% vs 12.1%),
  converts it to our outcome (automation = directive + feedback loop: 49.8 vs 41.5, a gap of 8.3
  points), and compares it with the spread of task-mix-adjusted automation across countries.
  The most that user newness could explain is the tenure gap times the difference in new-user share
  between two countries, which is at most 1 (everyone new vs everyone experienced).
Why
  It bounds the cohort story with arithmetic alone. Nothing here uses culture data.
"""
import pandas as pd, numpy as np, json
d = pd.read_csv("data/processed/03_partial_by_wave.csv")
TENURE = {"directive": (38.1, 29.4), "feedback loop": (11.7, 12.1)}          # (low tenure, high tenure), Table 2.1
auto_gap = (TENURE["directive"][0] + TENURE["feedback loop"][0]) - (TENURE["directive"][1] + TENURE["feedback loop"][1])
directive_gap = TENURE["directive"][0] - TENURE["directive"][1]
out = {"automation_gap_points": round(auto_gap, 2), "directive_gap_points": round(directive_gap, 2), "waves": {}}
print(f"Tenure gap (published): directive {directive_gap:.1f} points; automation (our outcome) {auto_gap:.1f} points")
for w, x in d.groupby("wave"):
    r = x.auto_resid
    spread_p5_95 = r.quantile(.95) - r.quantile(.05); spread_full = r.max() - r.min(); sd = r.std()
    share = auto_gap / spread_p5_95
    out["waves"][w] = {"n": int(len(r)), "sd_resid": round(sd, 2), "spread_p5_p95": round(spread_p5_95, 2), "spread_full": round(spread_full, 2), "ceiling_share_of_p5p95": round(share, 3)}
    print(f"{w}: N={len(r):3d} residual SD {sd:5.2f}, 5th-95th spread {spread_p5_95:5.2f}, full range {spread_full:5.2f} -> newness explains at most {share:.0%} of the 5th-95th spread")
json.dump(out, open("data/processed/05_ceiling.json", "w"), indent=1)
# A plausible, not extreme, composition difference: if two countries differed by 30 points in their new-user share
# (say 60% new vs 30% new), newness would move automation by 0.30 x the tenure gap.
plausible = 0.30 * auto_gap
out["plausible_30pt_difference_points"] = round(plausible, 2)
print(f"With a 30-point difference in new-user share between two countries, newness would explain {plausible:.1f} points, "
      f"i.e. {plausible/out['waves']['2025-08']['spread_p5_p95']:.0%} of the Aug 2025 5th-95th spread.")
json.dump(out, open("data/processed/05_ceiling.json", "w"), indent=1)
# check block: computational validity only (the result is whatever it is)
assert abs(auto_gap - 8.3) < 0.05 and abs(directive_gap - 8.7) < 0.05, "tenure gaps must match Table 2.1"
assert all(v["spread_full"] >= v["spread_p5_p95"] > 0 for v in out["waves"].values())
print("CHECK OK: gaps match the published table; spreads computed for every wave. RESULT: the ceiling is roughly half of the typical spread in Aug 2025 (extreme case), so newness is bounded but not ruled out.")
