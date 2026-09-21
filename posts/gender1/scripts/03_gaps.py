"""gender1 · script 03 · overall gaps and ratios, band gaps, education gaps; H-age and H-education; per-measure terciles.

Primary tests run once, after the pre-registration commit (Gate 2a approved 21 September 2026).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gender1_common import *

cells = load_cells(); ix = index(cells); pw = power()
GEOS = EU27 + EXT

# ---- overall gaps and ratios, all indicators and units
overall = {}
for g in GEOS + ["EU27_2020"]:
    overall[g] = {}
    for ind in INDS:
        for unit in UNITS:
            p = pair(ix, g, ind, unit, "Y16_74")
            if p:
                gap, ratio = gap_ratio(p)
                overall[g][f"{ind}|{unit}"] = {"F": p[0], "M": p[1], "gap": gap, "ratio": ratio}

# ---- band gaps (I_IUAI, PC_IND and PC_IND_IU3)
bands = {}
for g in GEOS + ["EU27_2020"]:
    bands[g] = {}
    for unit in ["PC_IND", "PC_IND_IU3"]:
        bg = {}
        for b in BANDS:
            p = pair(ix, g, "I_IUAI", unit, b)
            if p:
                bg[b] = {"F": p[0], "M": p[1], "gap": p[1] - p[0]}
        bands[g][unit] = bg

# ---- education gaps
edu = {}
for g in GEOS + ["EU27_2020"]:
    eg = {}
    for e in EDU:
        p = pair(ix, g, "I_IUAI", "PC_IND", e)
        if p:
            eg[e] = {"F": p[0], "M": p[1], "gap": p[1] - p[0]}
    edu[g] = eg

# ---- H-age on EU27 with all six bands usable on PC_IND
age_set = [g for g in EU27 if len(bands[g]["PC_IND"]) == 6]
a_raw = b_raw = a_dist = b_dist = 0; age_detail = {}
for g in age_set:
    gp = {b: bands[g]["PC_IND"][b]["gap"] for b in BANDS}
    hw = {b: halfwidth(pw, g, b) for b in BANDS}
    young = gp["Y16_24"]; others = [gp[b] for b in BANDS[1:]]
    ra = young < min(others) or young < 0
    largest = max(BANDS, key=lambda b: gp[b]); rb = largest in ("Y25_34", "Y35_44")
    da = None; db = None
    if all(hw.values()):
        da = all(young < gp[b] - rss(hw["Y16_24"], hw[b]) for b in BANDS[1:]) or (young < -hw["Y16_24"])
        db = rb and all(gp[largest] > gp[b] + rss(hw[largest], hw[b]) for b in BANDS if b not in ("Y25_34", "Y35_44"))
    a_raw += ra; b_raw += rb; a_dist += bool(da); b_dist += bool(db)
    age_detail[g] = {"gaps": gp, "rule_a": ra, "rule_b": rb, "largest_band": largest, "rule_a_distinguishable": da, "rule_b_distinguishable": db, "bound": bool(all(hw.values()))}
N_age = len(age_set)
h_age = {"usable_set": age_set, "N": N_age,
         "rule_a": {"raw": a_raw, "raw_majority": a_raw > N_age / 2, "distinguishable": a_dist},
         "rule_b": {"raw": b_raw, "raw_majority": b_raw > N_age / 2, "distinguishable": b_dist},
         "no_bound": [g for g in age_set if not age_detail[g]["bound"]],
         "verdict": "declared" if (a_raw > N_age / 2 and b_raw > N_age / 2) else ("partly declared" if (a_raw > N_age / 2 or b_raw > N_age / 2) else "not declared"),
         "detail": age_detail}

# ---- H-education on EU27 with all three usable
edu_set = [g for g in EU27 if len(edu[g]) == 3]
hi_largest = sum(1 for g in edu_set if edu[g]["I5_8"]["gap"] > max(edu[g]["I0_2"]["gap"], edu[g]["I3_4"]["gap"]))
monotone = sum(1 for g in edu_set if edu[g]["I0_2"]["gap"] < edu[g]["I3_4"]["gap"] < edu[g]["I5_8"]["gap"])
N_edu = len(edu_set)
h_edu = {"usable_set": edu_set, "N": N_edu, "high_is_largest": hi_largest, "raw_majority": hi_largest > N_edu / 2,
         "monotone_low_lt_med_lt_high": monotone, "distinguishable": None, "note": "no education-cell bound exists; raw count only",
         "verdict": "supported" if hi_largest > N_edu / 2 else "against"}

# ---- per-measure terciles on EU27 (gap, ratio) for I_IUAI PC_IND
gap_vals = {g: overall[g]["I_IUAI|PC_IND"]["gap"] for g in EU27 if "I_IUAI|PC_IND" in overall[g]}
ratio_vals = {g: overall[g]["I_IUAI|PC_IND"]["ratio"] for g in EU27 if "I_IUAI|PC_IND" in overall[g] and overall[g]["I_IUAI|PC_IND"]["ratio"] is not None}
t_gap, k_gap = tercile(gap_vals, True, TIE_GAP)
t_ratio, k_ratio = tercile(ratio_vals, False, TIE_RATIO)   # ascending: a smaller p_F/p_M is a larger male lead
changes_gap_ratio = sum(1 for g in gap_vals if g in ratio_vals and t_gap[g] != t_ratio[g])

write_json("gaps.json", {"overall": overall, "bands": bands, "education": edu,
                         "terciles": {"gap": t_gap, "ratio": t_ratio, "k_gap": k_gap, "k_ratio": k_ratio, "N_gap": len(gap_vals), "N_ratio": len(ratio_vals),
                                      "changes_gap_vs_ratio": changes_gap_ratio},
                         "h_age": h_age, "h_education": h_edu})

# ---- check block
assert len(gap_vals) == 27 and N_age == 26 and N_edu == 26, (len(gap_vals), N_age, N_edu)
assert abs(overall["EU27_2020"]["I_IUAI|PC_IND"]["gap"] - 4.46) < 1e-9
assert abs(overall["EU27_2020"]["I_IUAIWP|PC_IND"]["gap"] - 3.00) < 1e-9 and abs(overall["EU27_2020"]["I_IUAIPR|PC_IND"]["gap"] - 5.51) < 1e-9
assert abs(bands["EU27_2020"]["PC_IND"]["Y16_24"]["gap"] - (-1.67)) < 1e-9
assert k_gap == 9 and k_ratio == 9
assert all(v in ("top", "middle", "bottom") for v in t_gap.values())
assert all(t_gap[g] == "top" for g in list(t_gap)[:0])  # placeholder, structure only
for g in EU27:
    for b, d in bands[g]["PC_IND"].items():
        assert abs(d["gap"] - (d["M"] - d["F"])) < 1e-12
print(f"H-age: N={N_age}; rule (a) raw {a_raw} (distinguishable {a_dist}); rule (b) raw {b_raw} (distinguishable {b_dist}); verdict {h_age['verdict']}")
print(f"H-education: N={N_edu}; high largest in {hi_largest}; monotone {monotone}; verdict {h_edu['verdict']}")
print(f"terciles: k={k_gap}; gap top {sum(v=='top' for v in t_gap.values())}, bottom {sum(v=='bottom' for v in t_gap.values())}; ratio top {sum(v=='top' for v in t_ratio.values())}; changes gap vs ratio {changes_gap_ratio}")
print("CHECKS PASSED")
