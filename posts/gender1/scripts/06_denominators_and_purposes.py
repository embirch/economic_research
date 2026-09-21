"""gender1 · script 06 · purposes (H-work), the internet-user denominator and the internet-composition share, purposes among users,
flagged-cell appendix, EU27 against extension.
"""
import json, os, sys, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gender1_common import *

cells = load_cells(); ix = index(cells); pw = power()
G = json.load(open(os.path.join(PROC, "gaps.json"))); overall, bands = G["overall"], G["bands"]

# ---- H-work on EU27, PC_IND
work_set = [g for g in EU27 if "I_IUAIWP|PC_IND" in overall[g] and "I_IUAIPR|PC_IND" in overall[g]]
fav = dist_fav = dist_against = 0; detail = {}
for g in work_set:
    d = overall[g]["I_IUAIWP|PC_IND"]["gap"] - overall[g]["I_IUAIPR|PC_IND"]["gap"]
    hw = halfwidth(pw, g); thr = math.sqrt(2) * hw if hw else None
    f = d > 0; fav += f
    df = (thr is not None and d > thr); da = (thr is not None and d < -thr); dist_fav += df; dist_against += da
    detail[g] = {"gap_work": overall[g]["I_IUAIWP|PC_IND"]["gap"], "gap_private": overall[g]["I_IUAIPR|PC_IND"]["gap"], "work_minus_private": d, "favour": f, "distinguishable_favour": df, "distinguishable_against": da, "threshold": thr}
N_w = len(work_set)
h_work = {"usable_set": work_set, "N": N_w, "raw_favour": fav, "raw_majority": fav > N_w / 2, "threshold_19": fav >= 19,
          "distinguishable_favour": dist_fav, "distinguishable_against": dist_against, "no_bound": [g for g in work_set if halfwidth(pw, g) is None],
          "verdict": ("supported" if fav > N_w / 2 else "against"), "reading": ("not distinguishable from an even split" if fav < 19 and fav > N_w - 19 else ("beyond the 0.026 chance threshold (19 or more of 27 in favour, or 23 or more against, each one-sided 0.026 under an even split)" if fav >= 19 or fav <= N_w - 19 else "")),
          "one_sided_probability_of_realised_count_under_even_split": sum(math.comb(N_w, i) for i in range(0, fav + 1)) / 2 ** N_w if fav <= N_w / 2 else sum(math.comb(N_w, i) for i in range(fav, N_w + 1)) / 2 ** N_w,
          "among_users": {g: overall[g]["I_IUAIWP|PC_IND_IUAI"]["gap"] - overall[g]["I_IUAIPR|PC_IND_IUAI"]["gap"] for g in EU27 if "I_IUAIWP|PC_IND_IUAI" in overall[g] and "I_IUAIPR|PC_IND_IUAI" in overall[g]},
          "detail": detail}
h_work["among_users_favour"] = sum(1 for v in h_work["among_users"].values() if v > 0); h_work["among_users_N"] = len(h_work["among_users"])

# ---- purposes: participation gaps and among-users gaps, EU27 counts by sign
purposes = {}
for ind, name in [("I_IUAIPR", "private"), ("I_IUAIWP", "work"), ("I_IUAIFE", "education")]:
    part = {g: overall[g][f"{ind}|PC_IND"]["gap"] for g in EU27 if f"{ind}|PC_IND" in overall[g]}
    among = {g: overall[g][f"{ind}|PC_IND_IUAI"]["gap"] for g in EU27 if f"{ind}|PC_IND_IUAI" in overall[g]}
    purposes[name] = {"participation": {"N": len(part), "positive": sum(v > 0 for v in part.values()), "negative": sum(v < 0 for v in part.values()), "median_gap": statistics.median(part.values()), "values": part,
                                        "eu27": overall["EU27_2020"].get(f"{ind}|PC_IND")},
                      "among_users": {"N": len(among), "positive": sum(v > 0 for v in among.values()), "negative": sum(v < 0 for v in among.values()), "median_gap": statistics.median(among.values()), "values": among,
                                      "eu27": overall["EU27_2020"].get(f"{ind}|PC_IND_IUAI")},
                      "sign_flips_between_denominators": sum(1 for g in part if g in among and (part[g] > 0) != (among[g] > 0))}

# ---- internet-user denominator: overall and by band; internet-composition share
internet = {}
for g in EU27 + ["EU27_2020"]:
    o1 = overall[g].get("I_IUAI|PC_IND"); o3 = overall[g].get("I_IUAI|PC_IND_IU3")
    row = {"overall_gap_pc_ind": o1["gap"] if o1 else None, "overall_gap_iu3": o3["gap"] if o3 else None,
           "overall_composition_share": (o1["gap"] - o3["gap"]) if (o1 and o3) else None, "bands": {}}
    for b in BANDS:
        b1 = bands[g]["PC_IND"].get(b); b3 = bands[g]["PC_IND_IU3"].get(b)
        if b1 and b3: row["bands"][b] = {"gap_pc_ind": b1["gap"], "gap_iu3": b3["gap"], "composition_share": b1["gap"] - b3["gap"]}
    internet[g] = row
comp_set = [g for g in EU27 if len(internet[g]["bands"]) == 6]
band_medians = {b: statistics.median(internet[g]["bands"][b]["composition_share"] for g in comp_set) for b in BANDS}
# referee item 12: the decomposition gap_IND = r̄ (q_M − q_F) + q̄ (r_M − r_F), with r the implied internet-use rate p_IND / p_IU3 by sex and band (EU27)
decomp = {}
for b in BANDS:
    b1 = bands["EU27_2020"]["PC_IND"][b]; b3 = bands["EU27_2020"]["PC_IND_IU3"][b]
    rF, rM = b1["F"] / b3["F"], b1["M"] / b3["M"]; qF, qM = b3["F"], b3["M"]
    decomp[b] = {"implied_internet_use_F": rF, "implied_internet_use_M": rM, "rescaling_term": ((rF + rM) / 2) * (qM - qF) - (qM - qF), "internet_use_gap_term": ((qF + qM) / 2) * (rM - rF)}

# ---- flagged-cell appendix: overall pairs that would exist if flagged cells were allowed
flagged_appendix = []
for g in EU27 + EXT:
    for ind in INDS:
        for unit in UNITS:
            f = ix.get((g, ind, unit, "F_Y16_74")); m = ix.get((g, ind, unit, "M_Y16_74"))
            if f and m and f["value"] is not None and m["value"] is not None and (f["flag"] == "u" or m["flag"] == "u"):
                flagged_appendix.append({"geo": g, "ind": ind, "unit": unit, "F": f["value"], "M": m["value"], "gap": m["value"] - f["value"], "flags": f["flag"] + "/" + m["flag"]})

# ---- EU27 against the extension and the full 35, overall gap
ext_gaps = {g: overall[g]["I_IUAI|PC_IND"]["gap"] for g in EXT if "I_IUAI|PC_IND" in overall[g]}
eu_gaps = {g: overall[g]["I_IUAI|PC_IND"]["gap"] for g in EU27}
sets = {"eu27": {"N": 27, "median": statistics.median(eu_gaps.values()), "reversed": sorted(g for g, v in eu_gaps.items() if v < 0)},
        "extension": {"N": len(ext_gaps), "median": statistics.median(ext_gaps.values()), "reversed": sorted(g for g, v in ext_gaps.items() if v < 0)},
        "all35": {"N": 27 + len(ext_gaps), "median": statistics.median(list(eu_gaps.values()) + list(ext_gaps.values()))}}

write_json("denominators_purposes.json", {"h_work": h_work, "purposes": purposes, "internet": internet, "internet_composition_band_medians": band_medians,
                                          "internet_set_N": len(comp_set), "internet_decomposition_eu27": decomp, "flagged_appendix": flagged_appendix, "sets": sets})

# ---- check block
assert N_w == 27, N_w
assert abs(overall["EU27_2020"]["I_IUAIWP|PC_IND"]["gap"] - overall["EU27_2020"]["I_IUAIPR|PC_IND"]["gap"] - (-2.51)) < 1e-9
assert abs(purposes["education"]["among_users"]["eu27"]["gap"] - (26.77 - 30.53)) < 1e-9
assert len(comp_set) == 26
for name, p in purposes.items():
    for g in EU27:
        if g in p["participation"]["values"]:   # a purpose rate cannot exceed the overall rate (within rounding)
            assert overall[g][{"private": "I_IUAIPR", "work": "I_IUAIWP", "education": "I_IUAIFE"}[name] + "|PC_IND"]["M"] <= overall[g]["I_IUAI|PC_IND"]["M"] + 0.011
print(f"H-work: N={N_w}; work>private in {fav} (distinguishable in favour {dist_fav}, against {dist_against}); {h_work['reading']}; verdict {h_work['verdict']}; among users favour {h_work['among_users_favour']}/{h_work['among_users_N']}")
print("purposes (participation positive/negative, among users positive/negative, sign flips):", {k: (v['participation']['positive'], v['participation']['negative'], v['among_users']['positive'], v['among_users']['negative'], v['sign_flips_between_denominators']) for k, v in purposes.items()})
print(f"internet-composition share medians by band: { {b: round(v, 2) for b, v in band_medians.items()} }; flagged-appendix rows {len(flagged_appendix)}; sets {sets['eu27']['median']:.2f} / {sets['extension']['median']:.2f}")
print("CHECKS PASSED")
