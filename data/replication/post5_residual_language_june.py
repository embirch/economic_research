"""post5 (LL-18) feasibility: where the country not_classified residual lives (H4), the
country-state grain, the language claim and its two external substitutes, and the June cut C6.

Run from the repository root:
  python data/replication/post5_residual_language_june.py | tee data/replication/results/post5_residual_language_june.txt

Also writes data/replication/results/post5_residual_language_june.json. Fetches GeoNames
countryInfo.txt over the network (31,678 B on 2026-09-16).
"""
import json
import numpy as np
import pandas as pd
import re

NOV = "data/cache/release_2026_01_15/data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.parquet"
FEB = "data/cache/release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.parquet"
NOVA = "data/cache/release_2026_01_15/data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.parquet"
FEBA = "data/cache/release_2026_03_24/data/aei_raw_1p_api_2026-02-05_to_2026-02-12.parquet"
JUN = "data/cache/release_2026_06_26/data/aei_claude_ai_2026-06-26.parquet"
JUNA = "data/cache/release_2026_06_26/data/aei_1p_api_2026-06-26.parquet"
AUG = "data/cache/release_2025_09_15/data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv"
OUT = {}


def load(p):
    d = pd.read_parquet(p)
    d["level"] = d["level"].astype(str)
    return d


nov, feb = load(NOV), load(FEB)
waves = {"nov2025": nov, "feb2026": feb}

print("=" * 78)
print("Where the country not_classified residual lives (H4's confirmatory signature)")
print("=" * 78)
OUT["nc"] = {}
for w, df in waves.items():
    p = df[(df.geography == "country") & (df.facet == "human_only_ability") &
           (df.variable == "human_only_ability_pct")].pivot_table(index="geo_id", columns="cluster_name", values="value")
    u = df[(df.geography == "country") & (df.facet == "country") & (df.variable == "usage_count")] \
        .set_index("geo_id").value
    nc = p["not_classified"].dropna()
    cnts = u.reindex(nc.index)
    ge200 = cnts[cnts >= 200]
    print(f"{w}: {len(nc)} countries carry an explicit not_classified row; their usage_count: "
          f"min {cnts.min():.0f}, median {cnts.median():.0f}, max {cnts.max():.0f}; of those >=200: {len(ge200)} "
          f"{sorted(ge200.index)}")
    ge = u[u >= 200].drop(index=[i for i in ("not_classified", "NONE") if i in u.index])
    sub = p.reindex(ge.index)
    print(f"  over the {len(ge)} countries at or above 200: not_classified present in "
          f"{int(sub['not_classified'].notna().sum())}; yes+no sums to 100 in "
          f"{int((sub[['yes','no']].sum(axis=1).round(6) == 100).sum())} of {len(sub)}")
    OUT["nc"][w] = {"countries_with_nc": int(len(nc)), "nc_usage_min": float(cnts.min()),
                    "nc_usage_median": float(cnts.median()), "nc_usage_max": float(cnts.max()),
                    "nc_ge200": sorted(ge200.index), "ge200_n": int(len(ge)),
                    "ge200_with_nc": int(sub["not_classified"].notna().sum())}

print()
print("=" * 78)
print("country-state grain (not a cut in BRIEF section 8; reported for completeness)")
print("=" * 78)
OUT["country_state"] = {}
sets = {}
for w, df in waves.items():
    p = df[(df.geography == "country-state") & (df.facet == "human_only_ability") &
           (df.variable == "human_only_ability_pct")].pivot_table(index="geo_id", columns="cluster_name", values="value")
    # the totals facet at this grain is named 'country-state', and '<ISO2>-not_classified' units are pseudo-units
    u = df[(df.geography == "country-state") & (df.facet == "country-state") &
           (df.variable == "usage_count")].set_index("geo_id").value
    real = [g for g in p.index if not g.endswith("-not_classified")]
    p = p.loc[real]
    ge100 = u[(u >= 100) & (~u.index.str.endswith("-not_classified"))]
    both = sorted(set(p.index) & set(ge100.index))
    sets[w] = set(both)
    nc = int(p.loc[both, "not_classified"].notna().sum()) if "not_classified" in p else 0
    print(f"{w}: {len(p)} real units carry the facet; {len(ge100)} real units at or above 100 conversations; "
          f"{len(both)} carry both ({len([g for g in both if g.startswith('US-')])} US-*, "
          f"{len({g[:2] for g in both})} parents); explicit not_classified among them: {nc}")
    OUT["country_state"][w] = {"facet_units": int(len(p)), "ge100": int(len(ge100)), "both": len(both),
                               "us": len([g for g in both if g.startswith("US-")]),
                               "parents": len({g[:2] for g in both}), "nc_present": nc}
panel_cs = sets["nov2025"] & sets["feb2026"]
print(f"balanced country-state panel (facet and >=100 conversations in both waves): {len(panel_cs)} units, "
      f"{len({g[:2] for g in panel_cs})} parents, {len([g for g in panel_cs if g.startswith('US-')])} US")
OUT["country_state"]["panel"] = {"units": len(panel_cs), "parents": len({g[:2] for g in panel_cs}),
                                 "us": len([g for g in panel_cs if g.startswith("US-")])}

print()
print("=" * 78)
print("E1: is there any language column, value or metric in any release?")
print("=" * 78)
pat = re.compile(r"lang|english|locale|idioma|speech", re.I)
hits = {}
for name, path in [("nov_claude", NOV), ("nov_api", NOVA), ("feb_claude", FEB), ("feb_api", FEBA)]:
    d = pd.read_parquet(path)
    cols = {c: sorted({v for v in d[c].astype(str).unique() if pat.search(v)}) for c in
            ["geography", "facet", "variable", "platform_and_product"]}
    hits[name] = {k: v for k, v in cols.items() if v}
    print(f"{name}: columns {list(d.columns)}; structural matches {hits[name]}")
for name, path in [("jun_claude", JUN), ("jun_api", JUNA)]:
    d = pd.read_parquet(path)
    cols = {c: sorted({v for v in d[c].astype(str).unique() if pat.search(v)}) for c in
            ["geo_level", "category_name", "metric_id"]}
    hits[name] = {k: v for k, v in cols.items() if v}
    print(f"{name}: columns {list(d.columns)}; structural matches {hits[name]}")
aug = pd.read_csv(AUG, keep_default_na=False, nrows=5)
print("aug2025 columns:", list(aug.columns))
OUT["language"] = hits

# nearest substitutes for E1, both external to the Index
print("-- E1 substitute 1: GeoNames countryInfo.txt (live file, no version; CC BY 4.0)")
import io, urllib.request, hashlib
names = ["iso2", "iso3", "isonum", "fips", "country", "capital", "area", "population", "continent", "tld",
         "ccy", "ccyname", "phone", "pcfmt", "pcregex", "languages", "geonameid", "neighbours", "fips_eq"]
raw = urllib.request.urlopen("https://download.geonames.org/export/dump/countryInfo.txt").read()
print(f"   fetched {len(raw)} B, sha256 {hashlib.sha256(raw).hexdigest()}")
# TRAP: comment='#' truncates every row at the '#' inside the postal-code format column
lines = [l for l in raw.decode("utf-8").splitlines() if l and not l.startswith("#")]
ci = pd.read_csv(io.StringIO("\n".join(lines)), sep="\t", header=None, names=names, keep_default_na=False, dtype=str)
u_nov = nov[(nov.geography == "country") & (nov.facet == "country") & (nov.variable == "usage_count")].set_index("geo_id").value
u_feb = feb[(feb.geography == "country") & (feb.facet == "country") & (feb.variable == "usage_count")].set_index("geo_id").value
panel = sorted((set(u_nov[u_nov >= 200].index) & set(u_feb[u_feb >= 200].index)) - {"not_classified", "NONE"})
m = pd.DataFrame({"geo_id": panel}).merge(ci[["iso2", "country", "languages"]], left_on="geo_id", right_on="iso2", how="left")
print(f"   merge audit on ISO-2: rows in {len(m)}, matched {int(m.iso2.notna().sum())}, "
      f"unmatched {sorted(m.loc[m.iso2.isna(), 'geo_id'])}")
L = m.languages.fillna("")
en_any = L.str.split(",").apply(lambda x: any(t.strip().split("-")[0] == "en" for t in x))
en_first = L.str.split(",").str[0].str.split("-").str[0].eq("en")
print(f"   {len(ci)} rows in the source; English listed anywhere {int(en_any.sum())} of {len(m)}; "
      f"English listed first {int(en_first.sum())}: {sorted(m.loc[en_first, 'geo_id'])}")
OUT["geonames"] = {"rows": len(ci), "panel": len(m), "matched": int(m.iso2.notna().sum()),
                   "en_any": int(en_any.sum()), "en_first": int(en_first.sum()),
                   "en_first_ids": sorted(m.loc[en_first, "geo_id"]), "sha256": hashlib.sha256(raw).hexdigest()}

print("-- E1 substitute 2: Anthropic/enabling-independent-research, stanford_clusters.csv")
try:
    st = pd.read_csv("data/cache/supplementary/enabling_independent_research/stanford_clusters.csv",
                     keep_default_na=False, nrows=2)
    lang_cols = [c for c in st.columns if c.startswith("lang:")]
    ctry_cols = [c for c in st.columns if c.startswith("country:")]
    print(f"   {len(lang_cols)} lang:* columns and {len(ctry_cols)} country:* columns "
          f"({len(lang_cols)//2} languages, {len(ctry_cols)//2} countries), cluster grain, April-May 2026")
    OUT["stanford_lang"] = {"lang_cols": len(lang_cols), "country_cols": len(ctry_cols)}
except FileNotFoundError:
    print("   not cached; run python data/fetch/supplementary_anthropic.py")

print()
print("=" * 78)
print("June 2026 residual and comparability (cut C6)")
print("=" * 78)
j = pd.read_parquet(JUN)
d = j[(j.geo_level == "country") & (j.category_name == "overall")]
hoa = d[d.metric_id == "human_only_ability_pct"].pivot_table(index="geo_id", columns="date_start", values="value")
aui = d[d.metric_id == "usage_per_capita_index"].pivot_table(index="geo_id", columns="date_start", values="value")
both = hoa.dropna().index.intersection(aui.dropna().index)
print(f"countries with human_only_ability_pct and the AUI in both months: {len(both)}")
print(f"value precision: distinct decimals {sorted({len(str(v).split('.')[-1]) for v in d.value.head(5000)})[:5]}")
print(f"human_only_ability_pct range April {hoa.iloc[:, 0].min():.2f}-{hoa.iloc[:, 0].max():.2f}, "
      f"May {hoa.iloc[:, 1].min():.2f}-{hoa.iloc[:, 1].max():.2f}")
nc_metrics = [m for m in d.metric_id.unique() if "not_classified" in m or "unclassified" in m]
print("not_classified-like metrics at country/overall:", nc_metrics)
# is the June measure the yes share or the no share?
print("June global human_only_ability_pct:", j[(j.geo_id == 'GLOBAL') & (j.category_name == 'overall') &
                                               (j.metric_id == 'human_only_ability_pct')].set_index('date_start').value.to_dict())
# overlap with the long-wave panel
# overlap of the June country set with the two-wave panel (June ids are ISO-3)
iso = pd.read_csv("data/cache/release_2025_09_15/data/intermediate/iso_country_codes.csv",
                  keep_default_na=False, encoding="latin-1")
m3to2 = dict(zip(iso.iso_alpha_3, iso.iso_alpha_2))
jun2 = {m3to2.get(g, g) for g in hoa.dropna().index}
print(f"June countries with the measure in both months mapped to ISO-2: {len(jun2)}; "
      f"overlap with the 115-country panel: {len(jun2 & set(panel))}; "
      f"panel countries absent from June: {sorted(set(panel) - jun2)}")
print(f"Seychelles (SYC) anywhere in the June file: {'SYC' in set(j.geo_id)}")
OUT["june"] = {"both_metrics_both_months": int(len(both)), "nc_metrics": nc_metrics,
               "hoa_range_apr": [float(hoa.iloc[:, 0].min()), float(hoa.iloc[:, 0].max())],
               "overlap_with_panel": len(jun2 & set(panel)),
               "panel_absent_from_june": sorted(set(panel) - jun2)}

with open("data/replication/results/post5_residual_language_june.json", "w") as f:
    json.dump(OUT, f, indent=1, default=str)
print("\nwrote data/replication/results/post5_residual_language_june.json")
