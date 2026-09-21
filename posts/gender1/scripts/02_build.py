"""gender1 · script 02 · load, validate, coverage, and the published-headline ingestion check.

No gap is computed here except the EU27 aggregate's, which is disclosed and is the ingestion check.
"""
import csv, hashlib, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gender1_common import *

cells = load_cells(); ix = index(cells)
sha = hashlib.sha256(open(TSV, "rb").read()).hexdigest()

# ---- validation
keys = [(c["geo"], c["ind"], c["unit"], c["grp"]) for c in cells]
assert len(keys) == len(set(keys)), "duplicate keys"
assert all(0 <= c["value"] <= 100 for c in cells if c["value"] is not None), "value out of range"
assert set(c["flag"] for c in cells) <= {"", "u"}, f"unexpected flags {set(c['flag'] for c in cells)}"
geos = sorted(set(c["geo"] for c in cells))
assert set(EU27) <= set(geos) and set(EXT) <= set(geos) and set(AGG) <= set(geos), "geography sets"

# ---- coverage: usable pairs by (indicator, unit, suffix) for EU27, extension, all 35
suffixes = ["Y16_74"] + BANDS + EDU
cov = []
for ind in INDS:
    for unit in UNITS:
        for s in suffixes:
            eu = sum(1 for g in EU27 if pair(ix, g, ind, unit, s)); ex = sum(1 for g in EXT if pair(ix, g, ind, unit, s))
            cov.append(dict(indicator=ind, unit=unit, group=s, eu27_usable_pairs=eu, extension_usable_pairs=ex, all35=eu + ex))
os.makedirs(PROC, exist_ok=True)
with open(os.path.join(PROC, "coverage.csv"), "w") as fh:
    w = csv.DictWriter(fh, fieldnames=list(cov[0].keys())); w.writeheader(); w.writerows(cov)
complete_age = {g: all(pair(ix, g, "I_IUAI", "PC_IND", b) for b in BANDS) for g in EU27 + EXT + ["EU27_2020"]}

# ---- tidy cells file
with open(os.path.join(PROC, "cells.csv"), "w") as fh:
    w = csv.DictWriter(fh, fieldnames=["geo", "ind", "unit", "grp", "value", "flag", "usable"]); w.writeheader(); w.writerows(cells)

# ---- EU27 headline reproduction (disclosed values)
eu = {s: ix[("EU27_2020", "I_IUAI", "PC_IND", s)]["value"] for s in ["IND_TOTAL", "F_Y16_74", "M_Y16_74"]}
facts = {"tsv_sha256": sha, "cells": len(cells), "usable_cells": sum(c["usable"] for c in cells),
         "flag_u": sum(c["flag"] == "u" for c in cells), "missing": sum(c["value"] is None for c in cells),
         "geographies": geos, "eu27_headline": eu,
         "published_headline": {"overall": 33, "men": 35, "women": 30, "source": "Eurostat news 16 Dec 2025; Statistics Explained"},
         "complete_age_sets": {"eu27": sorted(g for g in EU27 if complete_age[g]), "extension": sorted(g for g in EXT if complete_age[g])},
         "incomplete_age_sets": sorted(g for g in EU27 + EXT if not complete_age[g])}
write_json("build_facts.json", facts)

# ---- check block
assert facts["cells"] == 39006 and facts["flag_u"] == 6699, (facts["cells"], facts["flag_u"])
assert round(eu["IND_TOTAL"]) == 33 and round(eu["M_Y16_74"]) == 35 and round(eu["F_Y16_74"]) == 30, eu
assert abs(eu["F_Y16_74"] - 30.45) < 1e-9 and abs(eu["M_Y16_74"] - 34.91) < 1e-9, eu
assert len(facts["complete_age_sets"]["eu27"]) == 26 and "IE" in facts["incomplete_age_sets"], facts["incomplete_age_sets"]
assert set(facts["incomplete_age_sets"]) == {"IE", "MK", "RS"}, facts["incomplete_age_sets"]
assert sum(1 for g in EU27 if pair(ix, g, "I_IUAI", "PC_IND", "Y16_74")) == 27
print(f"cells {facts['cells']}, usable {facts['usable_cells']}, flagged {facts['flag_u']}, missing {facts['missing']}")
print(f"EU27 headline reproduced: overall {eu['IND_TOTAL']} (published 33), men {eu['M_Y16_74']} (35), women {eu['F_Y16_74']} (30)")
print(f"complete sex-by-age sets: EU27 {len(facts['complete_age_sets']['eu27'])}/27, extension {len(facts['complete_age_sets']['extension'])}/8; incomplete {facts['incomplete_age_sets']}")
print("CHECKS PASSED")
