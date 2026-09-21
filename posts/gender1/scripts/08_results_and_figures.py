"""gender1 · script 08 · results.json (every number the post may cite) and the five registered figures with captions."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gender1_common import *
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

L = lambda n: json.load(open(os.path.join(PROC, n)))
B, G, S, D, T, P, I2 = L("build_facts.json"), L("gaps.json"), L("standardise.json"), L("denominators_purposes.json"), L("triangulation.json"), L("power_rules.json"), L("second_implementation.json")
FIG = os.path.join(OUT, "figures"); os.makedirs(FIG, exist_ok=True)
NAME = {"AT": "Austria", "BE": "Belgium", "BG": "Bulgaria", "HR": "Croatia", "CY": "Cyprus", "CZ": "Czechia", "DK": "Denmark", "EE": "Estonia", "FI": "Finland", "FR": "France", "DE": "Germany", "EL": "Greece", "HU": "Hungary", "IE": "Ireland", "IT": "Italy", "LV": "Latvia", "LT": "Lithuania", "LU": "Luxembourg", "MT": "Malta", "NL": "Netherlands", "PL": "Poland", "PT": "Portugal", "RO": "Romania", "SK": "Slovakia", "SI": "Slovenia", "ES": "Spain", "SE": "Sweden", "AL": "Albania", "BA": "Bosnia and Herzegovina", "CH": "Switzerland", "MK": "North Macedonia", "NO": "Norway", "RS": "Serbia", "TR": "Türkiye", "XK": "Kosovo", "EU27_2020": "EU27"}
ov = G["overall"]; cls = S["classes_eu27"]

# ---------------- Figure 1: rates and signed gaps, EU27, with classes
order = sorted(EU27, key=lambda g: ov[g]["I_IUAI|PC_IND"]["gap"])
fig, ax = plt.subplots(1, 2, figsize=(11, 8.5), gridspec_kw={"width_ratios": [1.4, 1]})
y = np.arange(len(order))
ax[0].barh(y, [ov[g]["I_IUAI|PC_IND"]["M"] for g in order], color="#4a6fa5", alpha=.85, height=.38, label="men")
ax[0].barh(y - .4, [ov[g]["I_IUAI|PC_IND"]["F"] for g in order], color="#c8553d", alpha=.85, height=.38, label="women")
ax[0].set_yticks(y - .2); ax[0].set_yticklabels([NAME[g] for g in order], fontsize=8); ax[0].set_xlabel("used generative AI in the last three months,\n% of individuals aged 16–74", fontsize=9); ax[0].legend(loc="lower center", bbox_to_anchor=(0.5, -0.115), ncol=2, frameon=False, fontsize=8)
ax[0].axvline(ov["EU27_2020"]["I_IUAI|PC_IND"]["M"], color="#4a6fa5", lw=.8, ls=":"); ax[0].axvline(ov["EU27_2020"]["I_IUAI|PC_IND"]["F"], color="#c8553d", lw=.8, ls=":")
colors = {"large-gap": "#4a6fa5", "small-gap": "#c8553d", "reversed": "#c8553d", "not distinguishable": "#9a9a9a", "not classifiable": "#d0d0d0"}
gaps = [ov[g]["I_IUAI|PC_IND"]["gap"] for g in order]
ax[1].barh(y - .2, gaps, color=[colors[cls[g]["class"]] for g in order], height=.7)
for i, g in enumerate(order):
    hw = cls[g]["halfwidth"]
    if hw: ax[1].plot([gaps[i] - hw, gaps[i] + hw], [i - .2, i - .2], color="black", lw=.8)
    if cls[g]["distinguishable"]: ax[1].text(gaps[i] + (hw or 0) + .2 if gaps[i] >= 0 else gaps[i] - (hw or 0) - .2, i - .2, "●", va="center", ha="left" if gaps[i] >= 0 else "right", fontsize=6)
ax[1].axvline(0, color="black", lw=.8); ax[1].axvline(ov["EU27_2020"]["I_IUAI|PC_IND"]["gap"], color="grey", lw=.8, ls=":")
ax[1].set_yticks([]); ax[1].set_xlabel("men minus women, points\n(bar colour: class; line: SRS 95% bound; ●: survives the bound)", fontsize=9)
ax[1].set_title("The gap, with its class", fontsize=10); ax[0].set_title("Use by sex", fontsize=10)
plt.tight_layout(); plt.savefig(os.path.join(FIG, "fig1_rates_and_gaps.png"), dpi=160); plt.close()

# ---------------- Figure 2: country-by-age heatmap of gaps
age_set = G["h_age"]["usable_set"]; order2 = sorted(age_set, key=lambda g: ov[g]["I_IUAI|PC_IND"]["gap"])
M = np.array([[G["bands"][g]["PC_IND"][b]["gap"] for b in BANDS] for g in order2])
fig, ax = plt.subplots(figsize=(7.5, 9))
im = ax.imshow(M, cmap="RdBu_r", vmin=-12, vmax=12, aspect="auto")
ax.set_xticks(range(6)); ax.set_xticklabels(["16–24", "25–34", "35–44", "45–54", "55–64", "65–74"]); ax.set_yticks(range(len(order2))); ax.set_yticklabels([NAME[g] for g in order2], fontsize=8)
for i in range(len(order2)):
    for j in range(6): ax.text(j, i, ("0" if round(M[i, j]) == 0 else f"{M[i, j]:+.0f}"), ha="center", va="center", fontsize=6.5, color="black" if abs(M[i, j]) < 8 else "white")
eu = [G["bands"]["EU27_2020"]["PC_IND"][b]["gap"] for b in BANDS]
ax.set_title("Men minus women, points, by age band (EU27 profile: " + ", ".join(f"{v:+.1f}" for v in eu) + ")", fontsize=9)
plt.colorbar(im, ax=ax, fraction=.03, label="percentage points"); plt.tight_layout(); plt.savefig(os.path.join(FIG, "fig2_country_by_age.png"), dpi=160); plt.close()

# ---------------- Figure 3: purposes, participation vs among users
fig, ax = plt.subplots(1, 3, figsize=(12, 7), sharey=True)
gs = order   # one common order for all three panels: the overall gap, as Figures 1 and 2 (referee item 1)
yy = np.arange(len(gs))
for k, (name, title) in enumerate([("private", "Private use"), ("work", "Work use"), ("education", "Formal education")]):
    part = D["purposes"][name]["participation"]["values"]; among = D["purposes"][name]["among_users"]["values"]
    ax[k].scatter([part.get(g, np.nan) for g in gs], yy, color="#4a6fa5", s=18, label="of all individuals")
    ax[k].scatter([among.get(g, np.nan) for g in gs], yy, color="#c8553d", s=18, marker="s", label="of AI users")
    ax[k].axvline(0, color="black", lw=.8); ax[k].set_title(title, fontsize=10)
    ax[k].set_xlabel("men minus women, points")
ax[0].set_yticks(yy); ax[0].set_yticklabels([NAME[g] for g in gs], fontsize=7)
ax[0].legend(fontsize=8, loc="lower right"); plt.tight_layout(); plt.savefig(os.path.join(FIG, "fig3_purposes.png"), dpi=160); plt.close()

# ---------------- Figure 4: crude vs standardised
comp = S["h_composition"]["usable_set"]
fig, ax = plt.subplots(figsize=(6.5, 6.5))
xs = [S["standardised"][g]["crude_gap"] for g in comp]; ys = [S["standardised"][g]["std_gap"] for g in comp]
ax.scatter(xs, ys, color=["#c8553d" if g in S["h_composition"]["changed"] else "#4a6fa5" for g in comp], s=28)
for g, x0, y0 in zip(comp, xs, ys): ax.annotate(g, (x0, y0), fontsize=7, xytext=(3, 3), textcoords="offset points")
lim = [min(xs + ys) - 1, max(xs + ys) + 1]; ax.plot(lim, lim, color="grey", lw=.8, ls=":"); ax.axhline(0, color="black", lw=.6); ax.axvline(0, color="black", lw=.6)
ax.set_xlabel("crude gap, men minus women, points"); ax.set_ylabel("gap under the EU27 age structure, points"); ax.set_title(f"Age standardisation moves {S['h_composition']['tercile_changes_registered_reading']} or {len(S['h_composition']['changed'])} of {len(comp)} countries across a tercile cut (red: either reading)", fontsize=9)
plt.tight_layout(); plt.savefig(os.path.join(FIG, "fig4_crude_vs_standardised.png"), dpi=160); plt.close()

# ---------------- Figure 5: internet-composition share by band
fig, ax = plt.subplots(figsize=(7, 4.5))
cset = [g for g in EU27 if len(D["internet"][g]["bands"]) == 6]
for g in cset: ax.plot(range(6), [D["internet"][g]["bands"][b]["composition_share"] for b in BANDS], color="grey", alpha=.35, lw=.8)
ax.plot(range(6), [D["internet_composition_band_medians"][b] for b in BANDS], color="#c8553d", lw=2.2, marker="o", label="median of countries")
ax.plot(range(6), [D["internet"]["EU27_2020"]["bands"][b]["composition_share"] for b in BANDS], color="#4a6fa5", lw=2, marker="s", label="EU27")
ax.axhline(0, color="black", lw=.8); ax.set_xticks(range(6)); ax.set_xticklabels(["16–24", "25–34", "35–44", "45–54", "55–64", "65–74"]); ax.set_ylabel("gap (all individuals) minus\ngap (internet users), points", fontsize=9); ax.legend(fontsize=8)
plt.tight_layout(); plt.savefig(os.path.join(FIG, "fig5_internet_composition.png"), dpi=160); plt.close()

# ---------------- results.json
eu_o = ov["EU27_2020"]
def cls_list(c): return sorted(g for g, v in cls.items() if v["class"] == c)
res = {"post": "gender1", "question": "Where is the gender gap in generative AI use widest, and how much of that is measurement?", "generated": __import__("time").strftime("%Y-%m-%dT%H:%M:%SZ", __import__("time").gmtime()),
       "prereg": "posts/gender1/prereg/prereg.md (revision 2, content 6050e38, committed c128906; opens applied 625440e)",
       "data": {"tsv_sha256": B["tsv_sha256"], "cells": B["cells"], "flagged_u": B["flag_u"], "missing": B["missing"]},
       "eu27": {"overall": eu_o["I_IUAI|PC_IND"], "internet_users": eu_o.get("I_IUAI|PC_IND_IU3"), "purposes_participation": {k: eu_o[f"{i}|PC_IND"] for k, i in [("private", "I_IUAIPR"), ("work", "I_IUAIWP"), ("education", "I_IUAIFE")]},
                "purposes_among_users": {k: eu_o[f"{i}|PC_IND_IUAI"] for k, i in [("private", "I_IUAIPR"), ("work", "I_IUAIWP"), ("education", "I_IUAIFE")]},
                "age_profile_gap": {b: G["bands"]["EU27_2020"]["PC_IND"][b]["gap"] for b in BANDS}, "age_profile_rates": G["bands"]["EU27_2020"]["PC_IND"],
                "age_profile_ratio": {b: G["bands"]["EU27_2020"]["PC_IND"][b]["F"] / G["bands"]["EU27_2020"]["PC_IND"][b]["M"] for b in BANDS},
                "education_profile": G["education"]["EU27_2020"], "standardised": S["standardised"]["EU27_2020"], "published_headline": B["published_headline"]},
       "countries": {g: {"name": NAME[g], "overall": ov[g].get("I_IUAI|PC_IND"), "internet_users": ov[g].get("I_IUAI|PC_IND_IU3"), "class": cls.get(g), "bands": G["bands"][g]["PC_IND"], "education": G["education"][g],
                         "standardised": S["standardised"].get(g), "purposes": {k: ov[g].get(f"{i}|PC_IND") for k, i in [("private", "I_IUAIPR"), ("work", "I_IUAIWP"), ("education", "I_IUAIFE")]},
                         "purposes_among_users": {k: ov[g].get(f"{i}|PC_IND_IUAI") for k, i in [("private", "I_IUAIPR"), ("work", "I_IUAIWP"), ("education", "I_IUAIFE")]},
                         "internet_composition": D["internet"].get(g), "bound": P["countries"].get(g)} for g in EU27},
       "extension": {g: {"name": NAME[g], "overall": ov[g].get("I_IUAI|PC_IND"), "class": S["classes_extension"].get(g), "bands": G["bands"][g]["PC_IND"], "standardised": S["standardised"].get(g), "bound": P["countries"].get(g)} for g in EXT},
       "tests": {"H_work": {k: v for k, v in D["h_work"].items() if k != "detail"}, "H_age": {k: v for k, v in G["h_age"].items() if k != "detail"}, "H_education": G["h_education"], "H_composition": {k: v for k, v in S["h_composition"].items() if k != "changes_pp"}},
       "classes": {"counts": S["class_counts"], "counts_distinguishable": S["class_counts_distinguishable"], "large_gap": cls_list("large-gap"), "small_gap": cls_list("small-gap"), "reversed_on_both_denominators": sorted(g for g, v in cls.items() if v["reversed_both_denominators"]),
                   "reversed_on_pc_ind": sorted(g for g in EU27 if ov[g]["I_IUAI|PC_IND"]["gap"] < 0), "not_classifiable": cls_list("not classifiable"), "cuts": S["cuts"], "sign_beyond_bound": S["sign_beyond_bound"],
                   "tercile_changes": {"gap_vs_ratio": G["terciles"]["changes_gap_vs_ratio"], "crude_vs_standardised_analyst_reading": S["h_composition"]["tercile_changes"], "crude_vs_standardised_registered_reading": S["h_composition"]["tercile_changes_registered_reading"],
                                       "ratio_vs_standardised_registered_reading": S["changes_ratio_vs_std"], "ratio_vs_standardised_recut_26": S["changes_ratio_vs_std_recut_26"]}},
       "purposes": {k: {"participation": {kk: vv for kk, vv in v["participation"].items() if kk != "values"}, "among_users": {kk: vv for kk, vv in v["among_users"].items() if kk != "values"}, "sign_flips": v["sign_flips_between_denominators"]} for k, v in D["purposes"].items()},
       "internet_composition": {"band_medians": D["internet_composition_band_medians"], "N": D["internet_set_N"], "eu27": D["internet"]["EU27_2020"], "eu27_decomposition": D["internet_decomposition_eu27"],
                                "over_one_point_by_band": {b: sum(1 for g in EU27 if b in D["internet"][g]["bands"] and abs(D["internet"][g]["bands"][b]["composition_share"]) > 1) for b in BANDS},
                                "reading": "a difference of gaps on two denominators; where internet use is below 100% its sign is a rescaling of the internet-user gap, not a composition that favours women; the sex difference in implied internet use is at most 1.1 points in any band at EU27 level and moves the gap by under 0.3 points"},
       "sets": D["sets"], "flagged_appendix_rows": len(D["flagged_appendix"]), "bound": {"assumptions": P["assumptions"], "class_rule": P["class_rule"], "design_effect_check": P["design_effect_check"]},
       "second_implementation": I2, "triangulation": {"leg_i": {k: v for k, v in T["leg_i"].items() if k != "values"}, "leg_ii": T["leg_ii"]},
       "deviations": [{"id": "D3", "what": "H-composition's crude tercile re-cut on the 26 geographies with a standardised gap (analyst's reading) rather than the registered literal reading (crude tercile over all 27, compared on the intersection); both counts reported", "effect": "3 changes (CZ, FR, LV) against 2 (CZ, LV); verdict supported under either; distinguishable 0 under either"},
                      {"id": "D4", "what": "an unregistered exploratory addition: the Spearman of the ratio against the feminine message share, beside the registered gap correlation; scipy p-values stored under not-for-citation keys", "effect": "no rule touched; nothing citable added"},
                      {"id": "D1", "what": "class-rule precedence: a geography in the bottom tercile on all three measures that is also reversed on both denominators is classed small-gap, with its reversed flag reported beside it (the registered rule lists both classes without precedence)", "effect": "no count changes; the reversed set is reported as a flag"},
                      {"id": "D2", "what": "triangulation leg (ii) dropped: Henseke's country gaps are published only as a figure image", "effect": "one exploratory leg fewer"}]}
write_json("results.json", res)
figs = {"fig1": {"file": "outputs/figures/fig1_rates_and_gaps.png", "script": "scripts/08_results_and_figures.py", "caption": "**In every EU country but five, men were more likely than women to have used generative AI in the three months before their 2025 interview; the gap runs from about −2 to +9 points, and 13 of 27 countries sit in the same tercile on all three measures (6 large-gap, 7 small-gap).** The male lead exceeds the country's sampling bound in 17 of the 22 countries where men lead; none of the five female leads does. Plotted, left: the share of individuals aged 16–74 who used generative AI in the three months before the interview, by sex, EU member states, 2025 ICT survey (dotted lines: EU27 men and women). Right: men minus women in percentage points; bar colour is the persistent class under the registered rule (blue large-gap, red small-gap, grey not distinguishable, light grey not classifiable); the black line is the simple-random-sampling 95% bound from the national net sample, a lower bound; ● marks a class whose gap lies further than the bound from the tercile cut, not a lead distinguishable from zero. Source: Eurostat isoc_ai_iaiu, PC_IND; N = 27."},
        "fig2": {"file": "outputs/figures/fig2_country_by_age.png", "script": "scripts/08_results_and_figures.py", "caption": "**Among 16-to-24-year-olds women lead in 20 of 26 countries; from 25 upward men lead in 17 to 22 of 26 depending on the band, and no single band holds the largest gap in a majority of countries.** Plotted: men minus women in points, by six age bands, for the 26 EU members with all twelve sex-by-age cells published and unflagged (Ireland lacks a usable 16–24 pair). Rows sorted by the overall gap. Cell values are the published differences; median band half-widths under simple random sampling run from about 4 points at 65–74 to 8 at 16–24, and exceed 10 for the smallest samples, so single cells are not distinguishable from their neighbours. Source: Eurostat isoc_ai_iaiu, PC_IND."},
        "fig3": {"file": "outputs/figures/fig3_purposes.png", "script": "scripts/08_results_and_figures.py", "caption": "**The male lead is in private and work use; for formal education the gap runs the other way in most countries, and more so among users.** Plotted: men minus women in points for each purpose, on two denominators: all individuals 16–74 (circles) and recent generative-AI users (squares). Purposes are multi-select and do not sum to overall use. EU members with usable pairs; N = 27 for each purpose on the all-individual denominator. Source: Eurostat isoc_ai_iaiu."},
        "fig4": {"file": "outputs/figures/fig4_crude_vs_standardised.png", "script": "scripts/08_results_and_figures.py", "caption": "**Applying the EU27 age structure to every country lowers the gap in 25 of 26 and moves two or three across a tercile cut, depending on whether the crude tercile is cut on all 27 countries or on the 26 with a standardised gap.** Plotted: each country's crude gap (x) against its gap after direct age standardisation with the EU27 2025 sex-pooled population weights (y); the dotted line is equality; red marks a country whose tercile differs between the two. Standardisation is defined only where all twelve band cells are usable (26 of 27; Ireland excluded). Source: Eurostat isoc_ai_iaiu and demo_pjan."},
        "fig5": {"file": "outputs/figures/fig5_internet_composition.png", "script": "scripts/08_results_and_figures.py", "caption": "**None of the gender gap is an internet-use gap: the sex difference in recent internet use is at most 1.1 points in any age band and moves the gap by under 0.3 points, and measuring among internet users instead of all individuals changes the gap by under a point at the median in every band.** The negative values are a rescaling of the internet-user gap onto a smaller base, not a composition that favours women; only at 65–74, where about a fifth of people are not recent internet users, does the rescaling exceed a point in ten countries. Plotted: the gap among all individuals minus the gap among recent internet users, by age band, one grey line per EU member with all six bands usable (26), the red line the median across them, the blue line the EU27 aggregate. Source: Eurostat isoc_ai_iaiu, PC_IND and PC_IND_IU3."}}
json.dump(figs, open(os.path.join(OUT, "figures.json"), "w"), indent=1)

# ---- check block
assert all(os.path.exists(os.path.join(ROOT, f["file"])) for f in figs.values())
assert res["tests"]["H_work"]["N"] == 27 and res["tests"]["H_age"]["N"] == 26 and res["tests"]["H_composition"]["N"] == 26
assert sum(res["classes"]["counts"].values()) == 27
assert I2["max_abs_difference"] < 1e-9
print("results.json written:", len(json.dumps(res)) // 1000, "KB; figures:", list(figs))
print("classes:", res["classes"]["counts"], "| large:", res["classes"]["large_gap"], "| small:", res["classes"]["small_gap"], "| reversed both:", res["classes"]["reversed_on_both_denominators"])
print("CHECKS PASSED")
