"""gender1 · script 07 · triangulation (exploratory, labelled): Spearman rank correlation between the EU27 ordering by the
Eurostat overall gap and OpenAI Signals' feminine share of ChatGPT messages by country, June 2025.

Leg (ii), Henseke's work-adoption gap by country, is dropped by rule: the paper publishes the country gaps only as a figure
image (its Figure 2), and the programme's figure-values ruling forbids reading numbers off a chart. Logged in the notebook.
"""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gender1_common import *
from scipy.stats import spearmanr

G = json.load(open(os.path.join(PROC, "gaps.json"))); overall = G["overall"]
SIG = os.path.join(REPO, "data", "cache", "openai_signals", "csv", "public_release_csv", "share_of_messages_by_gender_country_month.csv")
fem = {}
for r in csv.DictReader(open(SIG, encoding="cp1252")):
    if r["month"] == "2025-06-01" and r["typical_name_gender"] == "feminine":
        fem[r["country"]] = float(r["share_of_messages"])
code = {g: ("GR" if g == "EL" else g) for g in EU27}
pairs = [(g, overall[g]["I_IUAI|PC_IND"]["gap"], fem[code[g]]) for g in EU27 if code[g] in fem]
gaps = [p[1] for p in pairs]; shares = [p[2] for p in pairs]
rho, pval = spearmanr(gaps, shares)
# also against the ratio (a smaller p_F/p_M is a larger male lead; expect a positive correlation with the feminine share)
ratios = [overall[g]["I_IUAI|PC_IND"]["ratio"] for g, _, _ in pairs]
rho_r, pval_r = spearmanr(ratios, shares)
out = {"leg_i": {"source": "OpenAI Signals share_of_messages_by_gender_country_month.csv, feminine, 2025-06-01", "N": len(pairs), "missing_eu27": [g for g in EU27 if code[g] not in fem],
                 "spearman_gap_vs_feminine_share": rho, "p_value_gap": pval, "spearman_ratio_vs_feminine_share": rho_r, "p_value_ratio": pval_r,
                 "expected_sign": "negative for the gap (a larger male lead in the survey should go with a smaller feminine share of messages), positive for the ratio",
                 "values": [{"geo": g, "gap": a, "feminine_share": b} for g, a, b in pairs],
                 "caveats": "name-inferred gender; message share, not people; consumer ChatGPT; a share of messages within a country, not a use rate; exploratory, in no rule"},
       "leg_ii": {"status": "dropped by rule", "reason": "Henseke (2026) Figure 2 gives the country gender gaps only as an image; the figure-values ruling forbids reading values off a chart; no table is published"}}
write_json("triangulation.json", out)
assert len(pairs) == 26 and out["leg_i"]["missing_eu27"] and -1 <= rho <= 1
print(f"Signals leg: N={len(pairs)} (missing {out['leg_i']['missing_eu27']}); Spearman gap vs feminine share {rho:+.3f} (p={pval:.3f}); ratio vs feminine share {rho_r:+.3f} (p={pval_r:.3f})")
print("Henseke leg: dropped by rule (figure-only values)")
print("CHECKS PASSED")
