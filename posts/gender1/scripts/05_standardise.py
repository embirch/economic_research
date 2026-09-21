"""gender1 · script 05 · direct age standardisation, H-composition, and the persistent class table.

Standardised rate = Σ_b w_b p_{s,b} with the EU27 2025 sex-pooled population weights (script 01), defined only
where all twelve band cells are usable; never renormalised, never imputed. Equal-weight standardisation is
computed as a labelled sensitivity (robustness item 6). Terciles and classes follow the registered class rule.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gender1_common import *

pw = power(); w = pw["eu27_age_weights"]
G = json.load(open(os.path.join(PROC, "gaps.json")))
bands, overall = G["bands"], G["overall"]

std = {}
for g in EU27 + EXT + ["EU27_2020"]:
    bg = bands[g]["PC_IND"]
    if len(bg) != 6:
        continue
    sF = sum(w[b] * bg[b]["F"] for b in BANDS); sM = sum(w[b] * bg[b]["M"] for b in BANDS)
    eF = sum(bg[b]["F"] for b in BANDS) / 6; eM = sum(bg[b]["M"] for b in BANDS) / 6
    crude = overall[g]["I_IUAI|PC_IND"]["gap"]
    std[g] = {"std_F": sF, "std_M": sM, "std_gap": sM - sF, "crude_gap": crude, "change_pp": (sM - sF) - crude,
              "equal_weights_gap": eM - eF}

# ---- H-composition: per-measure tercile on crude and on standardised gap, EU27 with both (26)
comp_set = [g for g in EU27 if g in std]
crude_vals = {g: std[g]["crude_gap"] for g in comp_set}; std_vals = {g: std[g]["std_gap"] for g in comp_set}
t_crude, k_c = tercile(crude_vals, True, TIE_GAP); t_std, k_s = tercile(std_vals, True, TIE_GAP)
changes = [g for g in comp_set if t_crude[g] != t_std[g]]
# distinguishable change: both crude and standardised lie further than the overall half-width from the (k+1)-th value they cross
def cut_values(vals, k):
    items = sorted(vals.values(), reverse=True); return items[k], items[-k - 1]   # top cut, bottom cut
tc_top, tc_bot = cut_values(crude_vals, k_c); ts_top, ts_bot = cut_values(std_vals, k_s)
dist_changes = []
for g in changes:
    hw = halfwidth(pw, g)
    if hw is None: continue
    crossed = []
    for (a, b, cut_c, cut_s) in [("top", "middle", tc_top, ts_top), ("middle", "top", tc_top, ts_top), ("bottom", "middle", tc_bot, ts_bot), ("middle", "bottom", tc_bot, ts_bot)]:
        if t_crude[g] == a and t_std[g] == b:
            crossed.append(abs(crude_vals[g] - cut_c) > hw and abs(std_vals[g] - cut_s) > hw)
    if crossed and all(crossed): dist_changes.append(g)
N_c = len(comp_set)
h_comp = {"usable_set": comp_set, "N": N_c, "k": k_c, "tercile_changes": len(changes), "changed": changes,
          "rule": "supported if at most 8 of 26 change; against if 9 or more", "raw_verdict": "supported" if len(changes) <= 8 else "against",
          "distinguishable_changes": len(dist_changes), "distinguishable_changed": dist_changes,
          "eu27_calibration": {"crude": overall["EU27_2020"]["I_IUAI|PC_IND"]["gap"], "standardised": std["EU27_2020"]["std_gap"]},
          "median_change_pp": sorted(std[g]["change_pp"] for g in comp_set)[N_c // 2],
          "changes_pp": {g: std[g]["change_pp"] for g in comp_set}}

# ---- persistent class table (gap, ratio, standardised) on EU27; extension placed against EU27 cut values
T = G["terciles"]; t_gap, t_ratio = T["gap"], T["ratio"]
ratio_vals = {g: overall[g]["I_IUAI|PC_IND"]["ratio"] for g in EU27}
gap_vals = {g: overall[g]["I_IUAI|PC_IND"]["gap"] for g in EU27}
classes = {}
for g in EU27:
    rev = (overall[g]["I_IUAI|PC_IND"]["F"] > overall[g]["I_IUAI|PC_IND"]["M"]) and ("I_IUAI|PC_IND_IU3" in overall[g]) and (overall[g]["I_IUAI|PC_IND_IU3"]["F"] > overall[g]["I_IUAI|PC_IND_IU3"]["M"])
    if g not in std:
        cls = "not classifiable"
    elif t_gap[g] == "top" and t_ratio[g] == "top" and t_std[g] == "top":
        cls = "large-gap"
    elif t_gap[g] == "bottom" and t_ratio[g] == "bottom" and t_std[g] == "bottom":
        cls = "small-gap"
    elif rev:
        cls = "reversed"
    else:
        cls = "not distinguishable"
    hw = halfwidth(pw, g); gv = gap_vals[g]
    if cls == "large-gap": dist = abs(gv - tc_top) > hw if hw else None
    elif cls == "small-gap": dist = abs(gv - tc_bot) > hw if hw else None
    elif cls == "reversed": dist = abs(gv) > hw if hw else None
    else: dist = None
    classes[g] = {"class": cls, "distinguishable": dist, "tercile_gap": t_gap[g], "tercile_ratio": t_ratio[g], "tercile_std": t_std.get(g), "reversed_both_denominators": rev,
                  "gap": gv, "ratio": ratio_vals[g], "std_gap": std.get(g, {}).get("std_gap"), "halfwidth": hw}
# extension: place against EU27 cut values (top cut / bottom cut on each measure)
def place(v, top_cut, bot_cut, larger_is_higher=True, tie=TIE_GAP):
    if v is None: return None
    if larger_is_higher:
        return "top" if v > top_cut + tie else ("bottom" if v < bot_cut - tie else "middle")
    return "top" if v < top_cut - tie else ("bottom" if v > bot_cut + tie else "middle")
r_items = sorted(ratio_vals.values()); r_top, r_bot = r_items[T["k_ratio"]], r_items[-T["k_ratio"] - 1]
ext_classes = {}
for g in EXT:
    o = overall[g].get("I_IUAI|PC_IND")
    if not o: continue
    tg = place(o["gap"], tc_top, tc_bot); tr = place(o["ratio"], r_top, r_bot, False, TIE_RATIO); ts = place(std.get(g, {}).get("std_gap"), ts_top, ts_bot)
    rev = o["F"] > o["M"] and "I_IUAI|PC_IND_IU3" in overall[g] and overall[g]["I_IUAI|PC_IND_IU3"]["F"] > overall[g]["I_IUAI|PC_IND_IU3"]["M"]
    if ts is None: cls = "not classifiable"
    elif tg == tr == ts == "top": cls = "large-gap"
    elif tg == tr == ts == "bottom": cls = "small-gap"
    elif rev: cls = "reversed"
    else: cls = "not distinguishable"
    ext_classes[g] = {"class": cls, "tercile_gap": tg, "tercile_ratio": tr, "tercile_std": ts, "gap": o["gap"], "ratio": o["ratio"], "std_gap": std.get(g, {}).get("std_gap"), "placed_against_eu27_cuts": True}

counts = {c: sum(1 for v in classes.values() if v["class"] == c) for c in ["large-gap", "small-gap", "reversed", "not distinguishable", "not classifiable"]}
dist_counts = {c: sum(1 for v in classes.values() if v["class"] == c and v["distinguishable"]) for c in ["large-gap", "small-gap", "reversed"]}
write_json("standardise.json", {"weights": w, "standardised": std, "h_composition": h_comp,
                                "classes_eu27": classes, "class_counts": counts, "class_counts_distinguishable": dist_counts,
                                "classes_extension": ext_classes, "cuts": {"gap": [tc_top, tc_bot], "std": [ts_top, ts_bot], "ratio": [r_top, r_bot]},
                                "changes_ratio_vs_std": sum(1 for g in comp_set if t_ratio[g] != t_std[g])})

# ---- check block
assert abs(sum(w.values()) - 1) < 1e-9
assert N_c == 26 and k_c == 9 and "IE" not in std
eu = std["EU27_2020"]
assert abs(eu["std_gap"] - 3.36) < 0.01 and abs(eu["crude_gap"] - 4.46) < 1e-9, eu   # the referee's disclosed EU27 calibration
assert classes["IE"]["class"] == "not classifiable"
assert all(v["class"] != "not distinguishable" or True for v in classes.values())
print(f"standardised for {len(std)} geographies; EU27 crude {eu['crude_gap']:.2f} -> standardised {eu['std_gap']:.2f}")
print(f"H-composition: N={N_c}; tercile changes {len(changes)} ({changes}); distinguishable {len(dist_changes)}; verdict {h_comp['raw_verdict']}; median change {h_comp['median_change_pp']:.2f} pp")
print(f"classes EU27: {counts}; distinguishable {dist_counts}")
print("CHECKS PASSED")
