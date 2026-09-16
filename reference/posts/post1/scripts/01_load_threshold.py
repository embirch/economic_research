"""Step 01: load the four Economic Index waves and apply the 200-conversation threshold.

What this does
  1. Reads the country-level rows from each release (the files are 'long': one row per
     country x facet x variable x cluster, with a single 'value' column).
  2. Finds each country's conversation count (usage_count) and keeps countries with >= 200,
     exactly as Anthropic's own code does (MIN_OBSERVATIONS_COUNTRY = 200).
  3. Pulls each country's collaboration shares (directive, feedback loop, task iteration,
     learning, validation, none) and computes automation = directive + feedback loop.
  4. Writes one tidy table per wave to data/processed/, and a combined one.
Why
  Everything downstream needs a clean, thresholded, per-country table with the same
  columns in every wave. Building it once, with checks, means later steps cannot be wrong
  because of a bad load.
Vocabulary
  wave  = one data release (Aug 2025, Nov 2025, Feb 2026, Apr 2026, May 2026)
  facet = the kind of thing a row describes ('collaboration', 'country', ...)
  share = percentage of a country's conversations
"""
import pandas as pd, numpy as np, os, json
RAW = "data/raw"; OUT = "data/processed"; os.makedirs(OUT, exist_ok=True)
MIN_OBS = 200                      # Anthropic's threshold for countries
PATTERNS = ["directive", "feedback loop", "task iteration", "learning", "validation", "none"]

def load_long(path, wave):
    """Waves 1-3 share one long schema. Read with keep_default_na=False so Namibia ('NA') survives."""
    df = pd.read_csv(path, keep_default_na=False, low_memory=False,
                     usecols=["geo_id", "geography", "facet", "variable", "cluster_name", "value"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    c = df[df["geography"] == "country"]
    # conversation counts per country
    cnt = c[(c["facet"] == "country") & (c["variable"] == "usage_count")][["geo_id", "value"]]
    cnt = cnt.rename(columns={"value": "usage_count"})
    # collaboration shares per country (one row per pattern)
    col = c[(c["facet"] == "collaboration") & (c["variable"] == "collaboration_pct")]
    col = col[col["cluster_name"].isin(PATTERNS)]
    wide = col.pivot_table(index="geo_id", columns="cluster_name", values="value", aggfunc="first")
    wide = wide.reindex(columns=PATTERNS)            # same column order every wave
    out = cnt.merge(wide, left_on="geo_id", right_index=True, how="left")
    out["wave"] = wave
    return out

def load_wide_v6(path):
    """June 2026 has a wide schema: metric_id names the quantity; two months (Apr, May)."""
    df = pd.read_csv(path, keep_default_na=False, low_memory=False,
                     usecols=["geo_id", "geo_level", "category_name", "metric_id", "value", "date_start"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    c = df[(df["geo_level"] == "country") & (df["category_name"] == "overall")]
    # June 2026 publishes no per-country conversation count: the file is already limited to
    # countries above Anthropic's floor (121 curated countries), so we mark them all as above threshold.
    keep = {"collaboration_directive_pct": "directive", "collaboration_feedback_loop_pct": "feedback loop",
            "collaboration_task_iteration_pct": "task iteration", "collaboration_learning_pct": "learning",
            "collaboration_validation_pct": "validation", "collaboration_none_pct": "none"}
    c = c[c["metric_id"].isin(keep)]
    wide = c.pivot_table(index=["geo_id", "date_start"], columns="metric_id", values="value", aggfunc="first")
    wide = wide.rename(columns=keep).reset_index()
    wide["wave"] = wide["date_start"].map({"2026-04-01": "2026-04", "2026-05-01": "2026-05"})
    wide["usage_count"] = np.nan            # not published for June 2026
    return wide[["geo_id", "usage_count"] + PATTERNS + ["wave"]]

waves = [
    load_long(f"{RAW}/release_2025_09_15/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv", "2025-08"),
    load_long(f"{RAW}/release_2026_01_15/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv", "2025-11"),
    load_long(f"{RAW}/release_2026_03_24/aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv", "2026-02"),
    load_wide_v6(f"{RAW}/release_2026_06_26/aei_claude_ai_2026-06-26.csv"),
]
allw = pd.concat(waves, ignore_index=True)
allw["usage_count"] = pd.to_numeric(allw["usage_count"], errors="coerce")
for p in PATTERNS: allw[p] = pd.to_numeric(allw[p], errors="coerce")
allw["automation"] = allw["directive"] + allw["feedback loop"]                      # share of all conversations
allw["automation_classified"] = allw["automation"] / allw[["directive","feedback loop","task iteration","learning","validation"]].sum(axis=1) * 100   # Anthropic's base
allw["augmentation"] = allw[["task iteration", "learning", "validation"]].sum(axis=1, min_count=1)
allw["above_threshold"] = (allw["usage_count"] >= MIN_OBS) | allw["wave"].isin(["2026-04", "2026-05"])   # June waves pre-filtered by Anthropic

# ---- write outputs
allw.to_csv(f"{OUT}/01_collab_by_country_all_waves.csv", index=False)
kept = allw[allw["above_threshold"] & allw["automation"].notna()]
kept.to_csv(f"{OUT}/01_collab_by_country_thresholded.csv", index=False)

# ---- report + check block
summary = allw.groupby("wave").agg(countries_in_file=("geo_id", "nunique"),
                                   above_200=("above_threshold", "sum"),
                                   with_automation=("automation", lambda s: s.notna().sum())).reset_index()
print(summary.to_string(index=False))
print("\nSpot check (India, Denmark, Singapore), Aug 2025:")
codes = {"2025-08": ["IND", "DNK", "SGP"]}
print(kept[(kept.wave == "2025-08") & (kept.geo_id.isin(codes["2025-08"]))][["geo_id", "usage_count", "directive", "feedback loop", "automation", "augmentation"]].to_string(index=False))

expected = {"2025-08": 115, "2025-11": 119, "2026-02": 119, "2026-04": 114, "2026-05": 121}   # from the data audit
got = dict(zip(summary.wave, summary.above_200))
for w, n in expected.items():
    assert abs(got[w] - n) <= 2, f"wave {w}: {got[w]} countries above threshold, audit said {n}"
share_sum = (kept[PATTERNS].sum(axis=1))
assert share_sum.between(85, 101).all(), f"pattern shares should sum to ~100 (unclassified excluded); range {share_sum.min():.1f}-{share_sum.max():.1f}"
assert kept["automation"].between(0, 100).all()
print(f"\nCHECK OK: thresholded rows = {len(kept)}; pattern shares sum between {share_sum.min():.1f} and {share_sum.max():.1f}")
