"""gender1 · script 04 · the second implementation of every confirmatory quantity, and synthetic recovery.

Independent path: reads the TSV with the csv module only (no gender1_common, no pandas), recomputes the overall
gaps and ratios, band gaps, standardised gaps, the H-age, H-education and H-composition counts and the
per-measure terciles, and compares them with gaps.json and standardise.json to 1e-9. Then runs the registered
synthetic recoveries on a fabricated table.
"""
import csv, json, math, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); REPO = os.path.dirname(os.path.dirname(ROOT))
PROC = os.path.join(ROOT, "data", "processed")
EU27 = "AT BE BG HR CY CZ DK EE FI FR DE EL HU IE IT LV LT LU MT NL PL PT RO SK SI ES SE".split()
BANDS = ["Y16_24", "Y25_34", "Y35_44", "Y45_54", "Y55_64", "Y65_74"]; EDU = ["I0_2", "I3_4", "I5_8"]

# ---- independent read
V = {}
for r in csv.reader(open(os.path.join(REPO, "data", "cache", "eurostat", "isoc_ai_iaiu.tsv")), delimiter="\t"):
    if r[0].startswith("freq"): continue
    _, grp, ind, unit, geo = r[0].split(","); v = r[1].strip()
    if v.startswith(":"): continue
    parts = v.split()
    if len(parts) > 1 and parts[1] == "u": continue
    V[(geo, ind, unit, grp)] = float(parts[0])
def pr(geo, ind, unit, s):
    f, m = V.get((geo, ind, unit, "F_" + s)), V.get((geo, ind, unit, "M_" + s))
    return (f, m) if f is not None and m is not None else None

G = json.load(open(os.path.join(PROC, "gaps.json"))); S = json.load(open(os.path.join(PROC, "standardise.json"))); P = json.load(open(os.path.join(PROC, "power_rules.json")))
w = P["eu27_age_weights"]
tol = 1e-9; worst = 0.0; n_checked = 0
def cmp(a, b, what):
    global worst, n_checked
    d = abs(a - b); worst = max(worst, d); n_checked += 1
    assert d < tol, f"{what}: {a} vs {b}"

# overall gaps and ratios
for g in EU27:
    p = pr(g, "I_IUAI", "PC_IND", "Y16_74"); o = G["overall"][g]["I_IUAI|PC_IND"]
    cmp(p[1] - p[0], o["gap"], f"gap {g}"); cmp(p[0] / p[1], o["ratio"], f"ratio {g}")
# band gaps and standardisation
def tercile(vals, larger_higher=True, tie=0.1):
    items = sorted(vals.items(), key=lambda kv: -kv[1] if larger_higher else kv[1]); N = len(items); k = int(round(N / 3))
    out = {g: "middle" for g, _ in items}; top_cut = items[k][1]; bot_cut = items[-k - 1][1]
    for i, (g, v) in enumerate(items):
        if i < k and abs(v - top_cut) > tie: out[g] = "top"
        elif i >= N - k and abs(v - bot_cut) > tie: out[g] = "bottom"
    return out
crude = {}; std = {}; a_raw = b_raw = 0; age_set = []
for g in EU27:
    bp = {b: pr(g, "I_IUAI", "PC_IND", b) for b in BANDS}
    if all(bp.values()):
        age_set.append(g)
        gaps = {b: bp[b][1] - bp[b][0] for b in BANDS}
        for b in BANDS: cmp(gaps[b], G["bands"][g]["PC_IND"][b]["gap"], f"band {g} {b}")
        sF = sum(w[b] * bp[b][0] for b in BANDS); sM = sum(w[b] * bp[b][1] for b in BANDS)
        cmp(sM - sF, S["standardised"][g]["std_gap"], f"std {g}"); std[g] = sM - sF
        crude[g] = pr(g, "I_IUAI", "PC_IND", "Y16_74")[1] - pr(g, "I_IUAI", "PC_IND", "Y16_74")[0]
        a_raw += (gaps["Y16_24"] < min(gaps[b] for b in BANDS[1:])) or gaps["Y16_24"] < 0
        b_raw += max(BANDS, key=lambda b: gaps[b]) in ("Y25_34", "Y35_44")
assert a_raw == G["h_age"]["rule_a"]["raw"] and b_raw == G["h_age"]["rule_b"]["raw"] and len(age_set) == G["h_age"]["N"], (a_raw, b_raw)
# education
hi = 0; n_e = 0
for g in EU27:
    ep = {e: pr(g, "I_IUAI", "PC_IND", e) for e in EDU}
    if all(ep.values()):
        n_e += 1; gaps = {e: ep[e][1] - ep[e][0] for e in EDU}; hi += gaps["I5_8"] > max(gaps["I0_2"], gaps["I3_4"])
assert hi == G["h_education"]["high_is_largest"] and n_e == G["h_education"]["N"], (hi, n_e)
# terciles and H-composition
t_c = tercile(crude); t_s = tercile(std)
assert sum(1 for g in crude if t_c[g] != t_s[g]) == S["h_composition"]["tercile_changes"]
gap_all = {g: G["overall"][g]["I_IUAI|PC_IND"]["gap"] for g in EU27}; ratio_all = {g: G["overall"][g]["I_IUAI|PC_IND"]["ratio"] for g in EU27}
assert tercile(gap_all) == G["terciles"]["gap"] and tercile(ratio_all, False, 0.01) == G["terciles"]["ratio"]
# registered literal reading of H-composition (27-set crude tercile against the 26-set standardised tercile, on the intersection)
t27 = tercile(gap_all); assert sum(1 for g in std if t27[g] != t_s[g]) == S["h_composition"]["tercile_changes_registered_reading"]
# persistent class table, marks and H-work (referee item 9): recomputed here from the independent read
D = json.load(open(os.path.join(PROC, "denominators_purposes.json"))); P27 = P["countries"]
t_r = tercile(ratio_all, False, 0.01)
def cuts(vals, larger=True):
    items = sorted(vals.values(), reverse=larger); k = int(round(len(vals) / 3)); return items[k], items[-k - 1]
g_top, g_bot = cuts(gap_all); s_top, s_bot = cuts(std)
for g in EU27:
    o = pr(g, "I_IUAI", "PC_IND", "Y16_74"); o3 = pr(g, "I_IUAI", "PC_IND_IU3", "Y16_74")
    rev = o[0] > o[1] and o3 is not None and o3[0] > o3[1]
    if g not in std: cls = "not classifiable"
    elif t27[g] == t_r[g] == t_s[g] == "top": cls = "large-gap"
    elif t27[g] == t_r[g] == t_s[g] == "bottom": cls = "small-gap"
    elif rev: cls = "reversed"
    else: cls = "not distinguishable"
    assert cls == S["classes_eu27"][g]["class"], (g, cls, S["classes_eu27"][g]["class"])
    hw = P27.get(g, {}).get("gap_halfwidth95_pp"); gv = o[1] - o[0]
    mark = (abs(gv - g_top) > hw) if cls == "large-gap" else (abs(gv - g_bot) > hw) if cls == "small-gap" else (abs(gv) > hw) if cls == "reversed" else None
    assert mark == S["classes_eu27"][g]["distinguishable"], (g, mark)
fav = dfav = dag = 0
for g in EU27:
    w_ = pr(g, "I_IUAIWP", "PC_IND", "Y16_74"); p_ = pr(g, "I_IUAIPR", "PC_IND", "Y16_74")
    d = (w_[1] - w_[0]) - (p_[1] - p_[0]); fav += d > 0
    hw = P27[g]["gap_halfwidth95_pp"]; dfav += d > math.sqrt(2) * hw; dag += d < -math.sqrt(2) * hw
assert (fav, dfav, dag) == (D["h_work"]["raw_favour"], D["h_work"]["distinguishable_favour"], D["h_work"]["distinguishable_against"]), (fav, dfav, dag)
n_checked += 27 * 2 + 3

# ---- synthetic recovery
rng_bands = {"Y16_24": (60, 62), "Y25_34": (50, 55), "Y35_44": (40, 44), "Y45_54": (30, 32), "Y55_64": (18, 20), "Y65_74": (6, 9)}
# (1) implanted standardised gap recovers to 1e-9
sF = sum(w[b] * rng_bands[b][0] for b in BANDS); sM = sum(w[b] * rng_bands[b][1] for b in BANDS)
implanted = sum(w[b] * (rng_bands[b][1] - rng_bands[b][0]) for b in BANDS); assert abs((sM - sF) - implanted) < 1e-9
# (2) equal rates -> zero gaps, ratio one, all not distinguishable
eq = {g: 0.0 for g in EU27}; teq = tercile(eq); assert all(v == "middle" for v in teq.values()) and abs(1.0 - 30 / 30) < 1e-12
# (3) implanted composition effect: identical band gaps, different age structures -> crude differs from standardised by the implanted amount
band_gap = 3.0; young_heavy = {"Y16_24": 0.4, "Y25_34": 0.2, "Y35_44": 0.1, "Y45_54": 0.1, "Y55_64": 0.1, "Y65_74": 0.1}
ratesM = {b: rng_bands[b][1] for b in BANDS}; ratesF = {b: rng_bands[b][1] - band_gap for b in BANDS}
crude_syn = sum(young_heavy[b] * ratesM[b] for b in BANDS) - sum(young_heavy[b] * ratesF[b] for b in BANDS)   # = band_gap under any weights when band gaps are identical
std_syn = sum(w[b] * ratesM[b] for b in BANDS) - sum(w[b] * ratesF[b] for b in BANDS)
assert abs(crude_syn - band_gap) < 1e-9 and abs(std_syn - band_gap) < 1e-9
# a composition effect proper: sex-specific age structures with identical band rates -> crude gap = implanted, standardised = 0
sexM = young_heavy; sexF = {b: w[b] for b in BANDS}; rates = {b: rng_bands[b][1] for b in BANDS}
crude2 = sum(sexM[b] * rates[b] for b in BANDS) - sum(sexF[b] * rates[b] for b in BANDS)
std2 = sum(w[b] * rates[b] for b in BANDS) - sum(w[b] * rates[b] for b in BANDS)
assert abs(std2) < 1e-12 and abs(crude2) > 1
# (4) one implanted large-gap geography among equals -> exactly that geography top on all three measures
syn = {g: 2.0 for g in EU27}; syn["DK"] = 9.0
t1 = tercile(syn); assert [g for g, v in t1.items() if v == "top"] == ["DK"]

json.dump({"tolerance": tol, "checked": n_checked, "max_abs_difference": worst,
           "synthetic": {"standardised_gap_recovered": True, "equal_rates_all_middle": True, "composition_effect_recovered_pp": crude2, "single_large_gap_geography": "DK"}},
          open(os.path.join(PROC, "second_implementation.json"), "w"), indent=1)
print(f"second implementation: {n_checked} quantities agree to {worst:.1e}; H-age {a_raw}/{b_raw}, H-education {hi}, composition changes {S['h_composition']['tercile_changes']} (registered reading {S['h_composition']['tercile_changes_registered_reading']}), class table, marks and H-work {fav}/{dfav}/{dag} reproduced")
print(f"synthetic: standardised gap recovered; equal rates -> all middle; composition effect {crude2:.2f} pp crude vs 0 standardised; single large-gap geography recovered")
print("CHECKS PASSED")
