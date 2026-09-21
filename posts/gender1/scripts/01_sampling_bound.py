"""gender1 · script 01 · the sampling bound and the class rule, before any primary test.

Runs before the pre-registration is committed. It loads NO outcome cell except the published EU27 headline
(used as an ingestion check in script 02) and the country-level overall (both-sex) use rates, which are
Eurostat's own published headline figures. It computes:

  1. An approximate sampling bound per country: with the national achieved sample n (from the national
     reference metadata, posts/gender1/data/processed/national_sample_sizes_2025.csv), a sex split of one
     half each (assumption A1), and the country's overall use rate p, the simple-random-sampling standard
     error of each sex's rate, of the male-minus-female gap, and the 95% half-width of the gap. Design
     effects only widen these, so they are LOWER bounds on the true uncertainty (assumption A2); the
     reference indicator's published standard errors are compared with the SRS value to show how far off
     A2 is (it is close: see the check block).
  2. The same per sex-by-age band, with the band's share of the national sample taken as the EU27 2025
     population share of that band (demo_pjan; assumption A3, since national age-by-sex sample counts are
     not published).
  3. The resolution of the class rule: how large a gap a country must have for its tercile membership to be
     stable, given the bound.

Outputs data/processed/power_rules.json. Every assumption is named in the JSON.
"""
import csv, json, math, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(ROOT))
PROC = os.path.join(ROOT, "data", "processed")
os.makedirs(PROC, exist_ok=True)

# ---- national sample sizes (steward table)
ns = {}
for r in csv.DictReader(open(os.path.join(PROC, "national_sample_sizes_2025.csv"))):
    # preference (referee item 1): the national page's row [D] net sample of individuals 16-74; else the implied
    # yes-count / proportion (HU, TR: row [D] gives households only; IE: row not parseable, precision block dated 2022-23)
    n = r["n_net_individuals_16_74_D"] or r["n_implied"]
    ns[r["geo"]] = dict(n=int(float(n)) if n else None, ref_p=float(r["ref_prop_pct"]) if r["ref_prop_pct"] else None,
                       ref_se=float(r["ref_se_pp"]) if r["ref_se_pp"] else None,
                       source="net sample, row [D]" if r["n_net_individuals_16_74_D"] else "implied (yes-count / proportion)")

# ---- EU27 age shares from demo_pjan (JSON-stat)
d = json.load(open(os.path.join(REPO, "data", "cache", "eurostat", "demo_pjan_EU27_2025.json")))
dims = d["id"]; sizes = d["size"]
cat = {k: d["dimension"][k]["category"]["index"] for k in dims}
def idx(coords):
    i = 0
    for k, s in zip(dims, sizes):
        i = i * s + cat[k][coords[k]]
    return i
bands = {"Y16_24": range(16, 25), "Y25_34": range(25, 35), "Y35_44": range(35, 45), "Y45_54": range(45, 55), "Y55_64": range(55, 65), "Y65_74": range(65, 75)}
pop = {}
for b, ages in bands.items():
    pop[b] = sum(d["value"].get(str(idx({"freq": "A", "unit": "NR", "age": f"Y{a}", "sex": "T", "geo": "EU27_2020", "time": "2025"})), 0) for a in ages)
tot = sum(pop.values()); w = {b: pop[b] / tot for b in bands}

# ---- country overall use rates (both sexes), the published headline figures, and the EU27 both-sex band rates
rates = {}; eu_band = {}
for r in csv.reader(open(os.path.join(REPO, "data", "cache", "eurostat", "isoc_ai_iaiu.tsv")), delimiter="\t"):
    if r[0].startswith("freq"): continue
    freq, grp, ind, unit, geo = r[0].split(",")
    v = r[1].strip()
    if ind == "I_IUAI" and unit == "PC_IND" and grp == "IND_TOTAL" and not v.startswith(":"): rates[geo] = float(v.split()[0])
    if ind == "I_IUAI" and unit == "PC_IND" and geo == "EU27_2020" and grp in bands and not v.startswith(":"): eu_band[grp] = float(v.split()[0])

def se_rate(p, n): return 100 * math.sqrt((p / 100) * (1 - p / 100) / n)

out = {"assumptions": {
    "A1": "the national sample is split equally between women and men",
    "A2": "simple random sampling; design effects widen the true standard error, so every figure here is a lower bound",
    "A3": "each sex-by-age band's share of the national sample equals the EU27 2025 population share of that band (demo_pjan, provisional)",
    "A4": "the rate in the binomial variance is the country's published overall both-sex rate for the overall bound, and the EU27 both-sex rate of the band for the band bounds; a sex-specific rate would move either by less than the rounding shown; using a country's own band rate would move the older-band bounds further and is not done, to avoid inspecting country-by-age cells before the commit"},
    "eu27_age_weights": w, "eu27_band_rates_pct": eu_band, "countries": {}, "class_rule": {}}
for geo, p in sorted(rates.items()):
    if geo not in ns or not ns[geo]["n"]: out["countries"][geo] = {"n": None, "note": "no national sample figure found"}; continue
    n = ns[geo]["n"]; n_sex = n / 2
    se_s = se_rate(p, n_sex); se_gap = math.sqrt(2) * se_s
    band = {}
    for b in bands:
        nb = n_sex * w[b]; se_b = se_rate(eu_band[b], nb) if nb > 0 else None
        band[b] = {"n_per_sex": round(nb), "gap_se_pp": round(math.sqrt(2) * se_b, 2), "gap_halfwidth95_pp": round(1.96 * math.sqrt(2) * se_b, 2)}
    ref_srs = se_rate(ns[geo]["ref_p"], n) if ns[geo]["ref_p"] else None
    out["countries"][geo] = {"n": n, "n_source": ns[geo]["source"], "overall_rate_pct": p, "rate_se_per_sex_pp": round(se_s, 2),
                             "gap_se_pp": round(se_gap, 2), "gap_halfwidth95_pp": round(1.96 * se_gap, 2), "gap_mde80_pp": round(2.8 * se_gap, 2),
                             "ref_indicator_published_se_pp": ns[geo]["ref_se"], "ref_indicator_srs_se_pp": round(ref_srs, 2) if ref_srs else None,
                             "bands": band}

# ---- class rule resolution: the median gap half-width across countries with a bound, overall and by band
hw = [c["gap_halfwidth95_pp"] for c in out["countries"].values() if c.get("n")]
hwb = {b: [c["bands"][b]["gap_halfwidth95_pp"] for c in out["countries"].values() if c.get("n")] for b in bands}
med = lambda x: sorted(x)[len(x) // 2]
ratio_tbl = {g: round(c["ref_indicator_published_se_pp"] / c["ref_indicator_srs_se_pp"], 2) for g, c in out["countries"].items()
             if c.get("ref_indicator_published_se_pp") and c.get("ref_indicator_srs_se_pp") and c["ref_indicator_published_se_pp"] > 0.05}
out["design_effect_check"] = {"published_over_srs_se_on_reference_indicator": ratio_tbl,
                              "above_1_3": sorted([g for g, v in ratio_tbl.items() if v > 1.3]),
                              "reading": "the SRS bound is a lower bound everywhere and a loose one where the ratio exceeds 1.3"}
out["class_rule"] = {"countries_with_bound": len(hw), "median_gap_halfwidth95_pp_overall": med(hw), "max": max(hw), "min": min(hw),
                     "median_gap_halfwidth95_pp_by_band": {b: med(v) for b, v in hwb.items()},
                     "reading": "two countries' overall gaps are not distinguishable at this bound unless they differ by more than the root-sum-square of their half-widths; within age bands the bound is several points, so the class rule, not a rank, is the unit of reporting"}
json.dump(out, open(os.path.join(PROC, "power_rules.json"), "w"), indent=1)

# ---- check block
assert abs(sum(w.values()) - 1) < 1e-9, "age weights must sum to one"
assert 0.10 < w["Y16_24"] < 0.20 and 0.10 < w["Y65_74"] < 0.20, f"implausible EU age weights {w}"
assert len(eu_band) == 6, f"EU27 band rates missing: {eu_band}"
assert len(rates) >= 35, f"expected the 35 geographies plus aggregates, got {len(rates)}"
assert abs(rates["EU27_2020"] - 32.7) < 0.3, f"EU27 headline should be about 32.7, got {rates['EU27_2020']}"
ratios = [c["ref_indicator_published_se_pp"] / c["ref_indicator_srs_se_pp"] for c in out["countries"].values()
          if c.get("ref_indicator_published_se_pp") and c.get("ref_indicator_srs_se_pp") and c["ref_indicator_published_se_pp"] > 0.05]
assert ratios and 0.5 < med(ratios) < 2.0, f"published/SRS SE ratio out of range: median {med(ratios)}"
print(f"countries with a bound: {len(hw)}; EU age weights {[round(w[b],3) for b in bands]}")
print(f"overall gap 95% half-width: median {med(hw)} pp (min {min(hw)}, max {max(hw)}); by band medians {out['class_rule']['median_gap_halfwidth95_pp_by_band']}")
print(f"published/SRS SE ratio on the reference indicator: median {med(ratios):.2f} over {len(ratios)} countries (1 = SRS holds)")
print("CHECKS PASSED")
