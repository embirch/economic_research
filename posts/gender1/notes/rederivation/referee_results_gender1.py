"""Referee re-derivation · gender1 · results stage · 2026-09-21.

Independent of the analyst's scripts: nothing is imported from posts/gender1/scripts. Reads the official TSV
(data/cache/eurostat/isoc_ai_iaiu.tsv, sha256 7f668f7b…), the demo_pjan JSON-stat cube (for the age weights,
recomputed here and compared with power_rules.json), power_rules.json (the registered sampling bound, which the
pre-registration names as the source of every distinguishable mark), and the OpenAI Signals CSV (leg i).

Re-derives, from the pre-registration's text (revision 2, content 6050e38):
  A. EU27 headline and purpose gaps.
  B. H-age rule (a) and rule (b) raw and distinguishable counts on the 26 EU members with all twelve cells.
  C. H-education "high is the largest" and the monotone count on the 26 EU members with all three pairs.
  D. Standardised gaps for DE, IT, MT (and all 26), the per-measure terciles with k = round(N/3) and the 0.1 /
     0.01 tie rule, and the H-composition tercile-change count with its distinguishable count.
  E. The persistent class table (large / small / reversed / not classifiable / not distinguishable) with the
     distinguishable marks, and the gap-vs-ratio and ratio-vs-standardised change counts.
  F. H-work raw and distinguishable counts, the among-users form, the purpose sign counts, the internet-composition
     medians, the sets medians, the flagged-appendix row count, and the Signals Spearman.
  G. Every caption number in outputs/figures.json.
Then compares each figure with results.json and prints MATCH or the discrepancy.
"""
import csv, hashlib, json, math, os, sys
from statistics import median

HERE = os.path.dirname(os.path.abspath(__file__))
POST = os.path.dirname(os.path.dirname(HERE))
REPO = os.path.dirname(os.path.dirname(POST))
TSV = os.path.join(REPO, "data", "cache", "eurostat", "isoc_ai_iaiu.tsv")
PJAN = os.path.join(REPO, "data", "cache", "eurostat", "demo_pjan_EU27_2025.json")
SIG = os.path.join(REPO, "data", "cache", "openai_signals", "csv", "public_release_csv", "share_of_messages_by_gender_country_month.csv")
RES = json.load(open(os.path.join(POST, "data", "processed", "results.json")))
PW = json.load(open(os.path.join(POST, "data", "processed", "power_rules.json")))
FIGS = json.load(open(os.path.join(POST, "outputs", "figures.json")))

EU27 = sorted("AT BE BG HR CY CZ DK EE FI FR DE EL HU IE IT LV LT LU MT NL PL PT RO SK SI ES SE".split())
EXT = sorted("AL BA CH MK NO RS TR XK".split())
BANDS = ["Y16_24", "Y25_34", "Y35_44", "Y45_54", "Y55_64", "Y65_74"]
EDU = ["I0_2", "I3_4", "I5_8"]

report = []
def say(*a):
    s = " ".join(str(x) for x in a); print(s); report.append(s)
n_match = n_mismatch = 0
def check(label, mine, theirs, tol=1e-9):
    global n_match, n_mismatch
    if isinstance(mine, (int, float)) and isinstance(theirs, (int, float)) and not isinstance(mine, bool):
        ok = abs(mine - theirs) <= tol
    else:
        ok = mine == theirs
    n_match += ok; n_mismatch += (not ok)
    say(f"  [{'MATCH' if ok else 'MISMATCH'}] {label}: mine={mine!r} results.json={theirs!r}")
    return ok

# ------------------------------------------------------------------ raw read
sha = hashlib.sha256(open(TSV, "rb").read()).hexdigest()
say(f"TSV sha256 {sha[:8]}… (pre-registration: 7f668f7b…) {'OK' if sha.startswith('7f668f7b') else 'WRONG FILE'}")
say(f"results.json data.tsv_sha256 {'agrees' if RES['data']['tsv_sha256'] == sha else 'DISAGREES'}")
cell = {}   # (geo, ind, unit, grp) -> (value or None, flag)
with open(TSV, encoding="utf-8") as fh:
    rd = csv.reader(fh, delimiter="\t"); header = next(rd)
    assert header[0].startswith("freq,ind_type,indic_is,unit,geo") and header[1].strip() == "2025", header
    for row in rd:
        freq, grp, ind, unit, geo = row[0].split(",")
        tok = row[1].strip().split()
        if tok[0] == ":":
            cell[(geo, ind, unit, grp)] = (None, " ".join(tok[1:]))
        else:
            cell[(geo, ind, unit, grp)] = (float(tok[0]), tok[1] if len(tok) > 1 else "")
say(f"cells read {len(cell)}; flagged u {sum(1 for v in cell.values() if v[1] == 'u')}; missing {sum(1 for v in cell.values() if v[0] is None)}")
check("data.cells", len(cell), RES["data"]["cells"]); check("data.flagged_u", sum(1 for v in cell.values() if v[1] == 'u'), RES["data"]["flagged_u"]); check("data.missing", sum(1 for v in cell.values() if v[0] is None), RES["data"]["missing"])

def usable(k):
    v = cell.get(k); return v is not None and v[0] is not None and v[1] != "u"
def pair(geo, ind, unit, suf):
    kf, km = (geo, ind, unit, "F_" + suf), (geo, ind, unit, "M_" + suf)
    return (cell[kf][0], cell[km][0]) if usable(kf) and usable(km) else None
def gap(p): return p[1] - p[0]
def ratio(p): return p[0] / p[1] if p[1] else None

# ------------------------------------------------------------------ A. EU27 headline and purpose gaps
say("\n== A. EU27 aggregate (disclosed values; ingestion check) ==")
EU = "EU27_2020"
tot = cell[(EU, "I_IUAI", "PC_IND", "IND_TOTAL")][0]
o = pair(EU, "I_IUAI", "PC_IND", "Y16_74")
say(f"EU27 overall: total {tot}, women {o[0]}, men {o[1]}, gap {gap(o):.2f} (published 33 / 30 / 35)")
check("eu27.overall.gap", gap(o), RES["eu27"]["overall"]["gap"]); check("eu27.overall.F", o[0], RES["eu27"]["overall"]["F"]); check("eu27.overall.M", o[1], RES["eu27"]["overall"]["M"])
assert round(tot) == 33 and round(o[0]) == 30 and round(o[1]) == 35
for name, ind in [("private", "I_IUAIPR"), ("work", "I_IUAIWP"), ("education", "I_IUAIFE")]:
    p = pair(EU, ind, "PC_IND", "Y16_74"); q = pair(EU, ind, "PC_IND_IUAI", "Y16_74")
    say(f"EU27 {name}: participation F {p[0]} M {p[1]} gap {gap(p):.2f}; among users F {q[0]} M {q[1]} gap {gap(q):.2f}")
    check(f"eu27.purposes_participation.{name}.gap", gap(p), RES["eu27"]["purposes_participation"][name]["gap"])
    check(f"eu27.purposes_among_users.{name}.gap", gap(q), RES["eu27"]["purposes_among_users"][name]["gap"])
iu = pair(EU, "I_IUAI", "PC_IND_IU3", "Y16_74"); check("eu27.internet_users.gap", gap(iu), RES["eu27"]["internet_users"]["gap"])
eu_bands = {b: gap(pair(EU, "I_IUAI", "PC_IND", b)) for b in BANDS}
for b in BANDS: check(f"eu27.age_profile_gap.{b}", eu_bands[b], RES["eu27"]["age_profile_gap"][b])
for e in EDU: check(f"eu27.education_profile.{e}.gap", gap(pair(EU, "I_IUAI", "PC_IND", e)), RES["eu27"]["education_profile"][e]["gap"])

# ------------------------------------------------------------------ weights from demo_pjan, independently
say("\n== Age weights from demo_pjan (own indexing of the JSON-stat cube) ==")
D = json.load(open(PJAN))
dims = D["id"]; size = D["size"]
idx = {d: D["dimension"][d]["category"]["index"] for d in dims}
def flat(coords):
    i = 0
    for d, n in zip(dims, size): i = i * n + idx[d][coords[d]]
    return i
def pop(sex, age):
    return D["value"][str(flat({"freq": "A", "unit": "NR", "age": f"Y{age}", "sex": sex, "geo": "EU27_2020", "time": "2025"}))]
band_of = lambda a: BANDS[0] if a <= 24 else BANDS[min(5, 1 + (a - 25) // 10)]
tot_by_band = {b: 0 for b in BANDS}
for a in range(16, 75):
    assert abs(pop("T", a) - pop("M", a) - pop("F", a)) < 1e-6
    tot_by_band[band_of(a)] += pop("T", a)
N16_74 = sum(tot_by_band.values()); W = {b: tot_by_band[b] / N16_74 for b in BANDS}
say("weights", {b: round(W[b], 6) for b in BANDS}, "sum", round(sum(W.values()), 12), "flags", sorted(set(D.get("status", {}).values())))
for b in BANDS: check(f"power_rules.eu27_age_weights.{b}", W[b], PW["eu27_age_weights"][b])

# ------------------------------------------------------------------ B. H-age
say("\n== B. H-age (EU27 members with all twelve sex-by-age cells usable on I_IUAI PC_IND) ==")
def hw(geo, band=None):
    c = PW["countries"].get(geo) or {}
    if not c.get("n"): return None
    return c["bands"][band]["gap_halfwidth95_pp"] if band else c["gap_halfwidth95_pp"]
rss = lambda a, b: math.sqrt(a * a + b * b)
age_set = [g for g in EU27 if all(pair(g, "I_IUAI", "PC_IND", b) for b in BANDS)]
say(f"usable set N={len(age_set)}; excluded: {sorted(set(EU27) - set(age_set))}")
bg = {g: {b: gap(pair(g, "I_IUAI", "PC_IND", b)) for b in BANDS} for g in age_set}
a_raw = sum(1 for g in age_set if bg[g]["Y16_24"] < min(bg[g][b] for b in BANDS[1:]) or bg[g]["Y16_24"] < 0)
b_raw = sum(1 for g in age_set if max(BANDS, key=lambda b: bg[g][b]) in ("Y25_34", "Y35_44"))
a_dist = sum(1 for g in age_set if all(bg[g]["Y16_24"] < bg[g][b] - rss(hw(g, "Y16_24"), hw(g, b)) for b in BANDS[1:]) or bg[g]["Y16_24"] < -hw(g, "Y16_24"))
def b_dist_one(g):
    L = max(BANDS, key=lambda b: bg[g][b])
    return L in ("Y25_34", "Y35_44") and all(bg[g][L] > bg[g][b] + rss(hw(g, L), hw(g, b)) for b in BANDS if b not in ("Y25_34", "Y35_44"))
b_dist = sum(1 for g in age_set if b_dist_one(g))
say(f"rule (a) raw {a_raw} of {len(age_set)} (majority {a_raw > len(age_set)/2}); distinguishable {a_dist}")
say(f"rule (b) raw {b_raw} of {len(age_set)} (majority {b_raw > len(age_set)/2}); distinguishable {b_dist}")
verdict = "declared" if (a_raw > 13 and b_raw > 13) else ("partly declared" if (a_raw > 13 or b_raw > 13) else "not declared")
check("tests.H_age.N", len(age_set), RES["tests"]["H_age"]["N"]); check("tests.H_age.rule_a.raw", a_raw, RES["tests"]["H_age"]["rule_a"]["raw"])
check("tests.H_age.rule_a.distinguishable", a_dist, RES["tests"]["H_age"]["rule_a"]["distinguishable"]); check("tests.H_age.rule_b.raw", b_raw, RES["tests"]["H_age"]["rule_b"]["raw"])
check("tests.H_age.rule_b.distinguishable", b_dist, RES["tests"]["H_age"]["rule_b"]["distinguishable"]); check("tests.H_age.verdict", verdict, RES["tests"]["H_age"]["verdict"])
no_bound = [g for g in age_set if hw(g) is None]; check("tests.H_age.no_bound", no_bound, RES["tests"]["H_age"]["no_bound"])
# decomposition of rule (a): negative at 16-24 vs smallest-but-positive
neg_young = sum(1 for g in age_set if bg[g]["Y16_24"] < 0); smallest_young = sum(1 for g in age_set if bg[g]["Y16_24"] < min(bg[g][b] for b in BANDS[1:]))
say(f"  decomposition: 16–24 gap negative in {neg_young}; 16–24 smallest of six in {smallest_young}; either {a_raw}")
largest_band = {b: sum(1 for g in age_set if max(BANDS, key=lambda x: bg[g][x]) == b) for b in BANDS}
say(f"  largest-band distribution over the 26: {largest_band}")
pos_by_band = {b: sum(1 for g in age_set if bg[g][b] > 0) for b in BANDS}
say(f"  men lead (gap>0) by band over the 26: {pos_by_band}")
say(f"  countries satisfying (a): {[g for g in age_set if bg[g]['Y16_24'] < min(bg[g][b] for b in BANDS[1:]) or bg[g]['Y16_24'] < 0]}")
say(f"  countries failing (a): {[g for g in age_set if not (bg[g]['Y16_24'] < min(bg[g][b] for b in BANDS[1:]) or bg[g]['Y16_24'] < 0)]}")
say(f"  (a)-distinguishable: {[g for g in age_set if all(bg[g]['Y16_24'] < bg[g][b] - rss(hw(g,'Y16_24'), hw(g,b)) for b in BANDS[1:]) or bg[g]['Y16_24'] < -hw(g,'Y16_24')]}")
say(f"  (b)-distinguishable: {[g for g in age_set if b_dist_one(g)]}")
band_hw_all = {b: sorted(hw(g, b) for g in age_set) for b in BANDS}
say(f"  band half-width range over the 26 (min..max): " + "; ".join(f"{b} {band_hw_all[b][0]:.1f}..{band_hw_all[b][-1]:.1f}" for b in BANDS))
say(f"  band half-width medians over the 26: " + "; ".join(f"{b} {median(band_hw_all[b]):.2f}" for b in BANDS))

# ------------------------------------------------------------------ C. H-education
say("\n== C. H-education (EU27 members with all three education pairs usable) ==")
edu_set = [g for g in EU27 if all(pair(g, "I_IUAI", "PC_IND", e) for e in EDU)]
say(f"usable set N={len(edu_set)}; excluded: {sorted(set(EU27) - set(edu_set))}")
eg = {g: {e: gap(pair(g, "I_IUAI", "PC_IND", e)) for e in EDU} for g in edu_set}
hi = sum(1 for g in edu_set if eg[g]["I5_8"] > max(eg[g]["I0_2"], eg[g]["I3_4"]))
mono = sum(1 for g in edu_set if eg[g]["I0_2"] < eg[g]["I3_4"] < eg[g]["I5_8"])
say(f"high is largest in {hi} of {len(edu_set)} (majority {hi > len(edu_set)/2}); monotone low<med<high in {mono}")
check("tests.H_education.N", len(edu_set), RES["tests"]["H_education"]["N"]); check("tests.H_education.high_is_largest", hi, RES["tests"]["H_education"]["high_is_largest"])
check("tests.H_education.monotone", mono, RES["tests"]["H_education"]["monotone_low_lt_med_lt_high"])
largest_edu = {e: sum(1 for g in edu_set if max(EDU, key=lambda x: eg[g][x]) == e) for e in EDU}
say(f"  largest-group distribution: {largest_edu}; high smallest of three in {sum(1 for g in edu_set if eg[g]['I5_8'] < min(eg[g]['I0_2'], eg[g]['I3_4']))}")
say(f"  median gaps: low {median(eg[g]['I0_2'] for g in edu_set):.2f}, medium {median(eg[g]['I3_4'] for g in edu_set):.2f}, high {median(eg[g]['I5_8'] for g in edu_set):.2f}")
say(f"  HR education cells: " + ", ".join(f"{e}: F {cell[('HR','I_IUAI','PC_IND','F_'+e)]} M {cell[('HR','I_IUAI','PC_IND','M_'+e)]}" for e in EDU))

# ------------------------------------------------------------------ D. standardisation, terciles, H-composition
say("\n== D. Standardisation (EU27 2025 pooled weights), per-measure terciles, H-composition ==")
def tercile(vals, larger_lead_is_higher=True, tie=0.1):
    """Registered rule: rank so a larger male lead is higher; k = round(N/3); top = k highest, bottom = k lowest,
    excluding any geography within `tie` of the (k+1)-th value from that end."""
    items = sorted(vals.items(), key=(lambda kv: -kv[1]) if larger_lead_is_higher else (lambda kv: kv[1]))
    N = len(items); k = int(round(N / 3))
    top_cut = items[k][1]; bot_cut = items[N - k - 1][1]
    out = {}
    for i, (g, v) in enumerate(items):
        if i < k and abs(v - top_cut) > tie: out[g] = "top"
        elif i >= N - k and abs(v - bot_cut) > tie: out[g] = "bottom"
        else: out[g] = "middle"
    return out, k, top_cut, bot_cut
crude = {g: gap(pair(g, "I_IUAI", "PC_IND", "Y16_74")) for g in EU27}
rat = {g: ratio(pair(g, "I_IUAI", "PC_IND", "Y16_74")) for g in EU27}
std = {}
for g in age_set:
    sF = sum(W[b] * pair(g, "I_IUAI", "PC_IND", b)[0] for b in BANDS); sM = sum(W[b] * pair(g, "I_IUAI", "PC_IND", b)[1] for b in BANDS)
    std[g] = sM - sF
for g in ["DE", "IT", "MT"]:
    say(f"  {g}: crude {crude[g]:.2f}, standardised {std[g]:.4f}, change {std[g]-crude[g]:+.2f}")
    check(f"countries.{g}.standardised.std_gap", std[g], RES["countries"][g]["standardised"]["std_gap"])
    check(f"countries.{g}.overall.gap", crude[g], RES["countries"][g]["overall"]["gap"])
for g in age_set: check(f"countries.{g}.standardised.std_gap", std[g], RES["countries"][g]["standardised"]["std_gap"]) if g not in ("DE", "IT", "MT") else None
eu_sF = sum(W[b] * pair(EU, "I_IUAI", "PC_IND", b)[0] for b in BANDS); eu_sM = sum(W[b] * pair(EU, "I_IUAI", "PC_IND", b)[1] for b in BANDS)
say(f"  EU27: crude {gap(o):.2f}, standardised {eu_sM-eu_sF:.4f}"); check("eu27.standardised.std_gap", eu_sM - eu_sF, RES["eu27"]["standardised"]["std_gap"])
lowered = sum(1 for g in age_set if std[g] < crude[g]); say(f"  standardisation lowers the gap in {lowered} of {len(age_set)}; raises it in {[g for g in age_set if std[g] > crude[g]]}")
changes_pp = sorted(std[g] - crude[g] for g in age_set); say(f"  change in points: median {median(changes_pp):.2f} (lower-median per script {changes_pp[len(age_set)//2]:.2f}), min {changes_pp[0]:.2f}, max {changes_pp[-1]:.2f}")
check("tests.H_composition.median_change_pp (script uses sorted[N//2])", changes_pp[len(age_set) // 2], RES["tests"]["H_composition"]["median_change_pp"])
t_crude26, k26, tc_top, tc_bot = tercile({g: crude[g] for g in age_set}); t_std26, ks, ts_top, ts_bot = tercile(std)
changed = sorted(g for g in age_set if t_crude26[g] != t_std26[g])
say(f"  H-composition: k={k26}; crude cuts (top/bottom) {tc_top:.2f}/{tc_bot:.2f}; standardised cuts {ts_top:.3f}/{ts_bot:.3f}; tercile changes {len(changed)} {changed}")
for g in changed: say(f"    {g}: crude {crude[g]:.2f} [{t_crude26[g]}] -> standardised {std[g]:.3f} [{t_std26[g]}]; overall half-width {hw(g)}")
# distinguishable change: both values further than the overall half-width from the (k+1)-th value they cross
def dist_change(g):
    h = hw(g)
    if h is None: return None
    cross = {("top", "middle"): (tc_top, ts_top), ("middle", "top"): (tc_top, ts_top), ("bottom", "middle"): (tc_bot, ts_bot), ("middle", "bottom"): (tc_bot, ts_bot)}
    cc, cs = cross[(t_crude26[g], t_std26[g])]
    return abs(crude[g] - cc) > h and abs(std[g] - cs) > h
dch = [g for g in changed if dist_change(g)]
check("tests.H_composition.N", len(age_set), RES["tests"]["H_composition"]["N"]); check("tests.H_composition.k", k26, RES["tests"]["H_composition"]["k"])
check("tests.H_composition.tercile_changes", len(changed), RES["tests"]["H_composition"]["tercile_changes"]); check("tests.H_composition.changed", changed, sorted(RES["tests"]["H_composition"]["changed"]))
check("tests.H_composition.distinguishable_changes", len(dch), RES["tests"]["H_composition"]["distinguishable_changes"])
check("tests.H_composition.raw_verdict", "supported" if len(changed) <= 8 else "against", RES["tests"]["H_composition"]["raw_verdict"])
# ties: geographies excluded from a tercile by the tie rule
def tie_excluded(vals, larger=True, tie=0.1):
    items = sorted(vals.items(), key=(lambda kv: -kv[1]) if larger else (lambda kv: kv[1])); N = len(items); k = int(round(N / 3))
    return [g for i, (g, v) in enumerate(items) if (i < k and abs(v - items[k][1]) <= tie) or (i >= N - k and abs(v - items[N-k-1][1]) <= tie)]
say(f"  tie-rule exclusions: crude(26) {tie_excluded({g: crude[g] for g in age_set})}; std {tie_excluded(std)}; gap(27) {tie_excluded(crude)}; ratio(27) {tie_excluded(rat, False, 0.01)}")

# ------------------------------------------------------------------ E. persistent class table
say("\n== E. Persistent class table (EU27; gap and ratio terciles on 27, standardised on 26) ==")
t_gap27, kg, g_top, g_bot = tercile(crude); t_rat27, kr, r_top, r_bot = tercile(rat, False, 0.01)
say(f"  k gap {kg}, cuts {g_top:.2f}/{g_bot:.2f}; k ratio {kr}, cuts {r_top:.4f}/{r_bot:.4f}")
check("classes.cuts.gap", [g_top, g_bot], RES["classes"]["cuts"]["gap"]); check("classes.cuts.ratio", [r_top, r_bot], RES["classes"]["cuts"]["ratio"]); check("classes.cuts.std", [ts_top, ts_bot], RES["classes"]["cuts"]["std"])
classes = {}; marks = {}
for g in EU27:
    p1 = pair(g, "I_IUAI", "PC_IND", "Y16_74"); p3 = pair(g, "I_IUAI", "PC_IND_IU3", "Y16_74")
    rev = p1[0] > p1[1] and p3 is not None and p3[0] > p3[1]
    if g not in std: c = "not classifiable"
    elif t_gap27[g] == t_rat27[g] == t_std26.get(g) == "top": c = "large-gap"
    elif t_gap27[g] == t_rat27[g] == t_std26.get(g) == "bottom": c = "small-gap"
    elif rev: c = "reversed"
    else: c = "not distinguishable"
    h = hw(g)
    m = None
    if c == "large-gap": m = abs(crude[g] - g_top) > h
    elif c == "small-gap": m = abs(crude[g] - g_bot) > h
    elif c == "reversed": m = abs(crude[g]) > h
    classes[g] = (c, rev); marks[g] = m
    # who satisfies both small-gap and reversed (the D1 precedence question)
counts = {c: sum(1 for v in classes.values() if v[0] == c) for c in ["large-gap", "small-gap", "reversed", "not distinguishable", "not classifiable"]}
dcounts = {c: sum(1 for g in EU27 if classes[g][0] == c and marks[g]) for c in ["large-gap", "small-gap", "reversed"]}
say(f"  counts {counts}; distinguishable {dcounts}")
for c in counts: check(f"classes.counts.{c}", counts[c], RES["classes"]["counts"][c])
for c in dcounts: check(f"classes.counts_distinguishable.{c}", dcounts[c], RES["classes"]["counts_distinguishable"][c])
check("classes.large_gap", sorted(g for g in EU27 if classes[g][0] == "large-gap"), RES["classes"]["large_gap"])
check("classes.small_gap", sorted(g for g in EU27 if classes[g][0] == "small-gap"), RES["classes"]["small_gap"])
check("classes.reversed_on_both_denominators", sorted(g for g in EU27 if classes[g][1]), RES["classes"]["reversed_on_both_denominators"])
check("classes.reversed_on_pc_ind", sorted(g for g in EU27 if crude[g] < 0), RES["classes"]["reversed_on_pc_ind"])
check("classes.not_classifiable", sorted(g for g in EU27 if classes[g][0] == "not classifiable"), RES["classes"]["not_classifiable"])
both = [g for g in EU27 if classes[g][0] == "small-gap" and classes[g][1]]
say(f"  D1 precedence: small-gap AND reversed-on-both = {both}; if reversed took precedence the table would read small-gap {counts['small-gap']-len(both)}, reversed {len(both)}")
for g in EU27:
    say(f"    {g}: gap {crude[g]:+.2f} [{t_gap27[g]}], ratio {rat[g]:.3f} [{t_rat27[g]}], std {std.get(g, float('nan')):+.2f} [{t_std26.get(g)}], hw {hw(g)} -> {classes[g][0]}{' (reversed both)' if classes[g][1] else ''}{' ●' if marks[g] else ''}")
    check(f"countries.{g}.class.class", classes[g][0], RES["countries"][g]["class"]["class"])
    check(f"countries.{g}.class.distinguishable", marks[g], RES["countries"][g]["class"]["distinguishable"])
chg_gr = sum(1 for g in EU27 if t_gap27[g] != t_rat27[g]); chg_rs = sum(1 for g in age_set if t_rat27[g] != t_std26[g])
say(f"  tercile changes: gap vs ratio {chg_gr} of 27 {[g for g in EU27 if t_gap27[g] != t_rat27[g]]}; ratio vs standardised {chg_rs} of 26; crude(26) vs standardised {len(changed)}")
check("classes.tercile_changes.gap_vs_ratio", chg_gr, RES["classes"]["tercile_changes"]["gap_vs_ratio"]); check("classes.tercile_changes.ratio_vs_standardised", chg_rs, RES["classes"]["tercile_changes"]["ratio_vs_standardised"])
# note: crude tercile on 27 (class table) vs crude tercile on 26 (H-composition) — do they differ for anyone?
diff27_26 = [g for g in age_set if t_gap27[g] != t_crude26[g]]
say(f"  crude tercile on 27 differs from crude tercile on 26 for: {diff27_26} (cuts 27: {g_top:.2f}/{g_bot:.2f}; 26: {tc_top:.2f}/{tc_bot:.2f})")
say(f"  EU27 gap range: min {min(crude.values()):+.2f} ({min(crude, key=crude.get)}), max {max(crude.values()):+.2f} ({max(crude, key=crude.get)}); median {median(crude.values()):.2f}")
# how many class assignments survive the bound at all (any pairwise)
say(f"  distinguishable marks: large {[g for g in EU27 if classes[g][0]=='large-gap' and marks[g]]}, small {[g for g in EU27 if classes[g][0]=='small-gap' and marks[g]]}")
# (the null check of the class rule is in referee_results_gender1_supp.py §2)

# ------------------------------------------------------------------ F. H-work, purposes, internet composition, sets, flagged, Signals
say("\n== F. H-work (EU27, PC_IND) ==")
work_set = [g for g in EU27 if pair(g, "I_IUAIWP", "PC_IND", "Y16_74") and pair(g, "I_IUAIPR", "PC_IND", "Y16_74")]
d = {g: gap(pair(g, "I_IUAIWP", "PC_IND", "Y16_74")) - gap(pair(g, "I_IUAIPR", "PC_IND", "Y16_74")) for g in work_set}
fav = sum(1 for g in work_set if d[g] > 0); dfav = sum(1 for g in work_set if d[g] > math.sqrt(2) * hw(g)); dag = sum(1 for g in work_set if d[g] < -math.sqrt(2) * hw(g))
say(f"N={len(work_set)}; work gap > private gap in {fav} {[g for g in work_set if d[g] > 0]}; distinguishable in favour {dfav}, against {dag} {[g for g in work_set if d[g] < -math.sqrt(2)*hw(g)]}")
say(f"  the other way (private > work) in {len(work_set)-fav}; 19-of-27 threshold in either direction: {'yes' if fav >= 19 or len(work_set)-fav >= 19 else 'no'} (against count {len(work_set)-fav})")
say(f"  median work−private {median(d.values()):.2f}; EU27 {gap(pair(EU,'I_IUAIWP','PC_IND','Y16_74')) - gap(pair(EU,'I_IUAIPR','PC_IND','Y16_74')):.2f}")
check("tests.H_work.N", len(work_set), RES["tests"]["H_work"]["N"]); check("tests.H_work.raw_favour", fav, RES["tests"]["H_work"]["raw_favour"])
check("tests.H_work.distinguishable_favour", dfav, RES["tests"]["H_work"]["distinguishable_favour"]); check("tests.H_work.distinguishable_against", dag, RES["tests"]["H_work"]["distinguishable_against"])
check("tests.H_work.verdict", "against" if not fav > len(work_set) / 2 else "supported", RES["tests"]["H_work"]["verdict"])
au = {g: gap(pair(g, "I_IUAIWP", "PC_IND_IUAI", "Y16_74")) - gap(pair(g, "I_IUAIPR", "PC_IND_IUAI", "Y16_74")) for g in EU27 if pair(g, "I_IUAIWP", "PC_IND_IUAI", "Y16_74") and pair(g, "I_IUAIPR", "PC_IND_IUAI", "Y16_74")}
check("tests.H_work.among_users_favour", sum(1 for v in au.values() if v > 0), RES["tests"]["H_work"]["among_users_favour"]); check("tests.H_work.among_users_N", len(au), RES["tests"]["H_work"]["among_users_N"])
say("\n== F2. Purposes: sign counts on the two denominators ==")
for name, ind in [("private", "I_IUAIPR"), ("work", "I_IUAIWP"), ("education", "I_IUAIFE")]:
    part = {g: gap(pair(g, ind, "PC_IND", "Y16_74")) for g in EU27 if pair(g, ind, "PC_IND", "Y16_74")}
    amg = {g: gap(pair(g, ind, "PC_IND_IUAI", "Y16_74")) for g in EU27 if pair(g, ind, "PC_IND_IUAI", "Y16_74")}
    pp, pn = sum(v > 0 for v in part.values()), sum(v < 0 for v in part.values()); ap, an = sum(v > 0 for v in amg.values()), sum(v < 0 for v in amg.values())
    flips = sum(1 for g in part if g in amg and (part[g] > 0) != (amg[g] > 0))
    say(f"  {name}: participation N {len(part)} +{pp}/−{pn} median {median(part.values()):.2f}; among users N {len(amg)} +{ap}/−{an} median {median(amg.values()):.2f}; sign flips {flips}")
    R = RES["purposes"][name]
    check(f"purposes.{name}.participation.positive", pp, R["participation"]["positive"]); check(f"purposes.{name}.participation.negative", pn, R["participation"]["negative"])
    check(f"purposes.{name}.among_users.positive", ap, R["among_users"]["positive"]); check(f"purposes.{name}.among_users.negative", an, R["among_users"]["negative"]); check(f"purposes.{name}.sign_flips", flips, R["sign_flips"])
    check(f"purposes.{name}.participation.median_gap (script: sorted[N//2])", sorted(part.values())[len(part) // 2], R["participation"]["median_gap"])
    if name == "education": say(f"    education participation positive in {[g for g in part if part[g] > 0]}; among users positive in {[g for g in amg if amg[g] > 0]}")
say("\n== F3. Internet-composition share by band (gap on PC_IND − gap on PC_IND_IU3) ==")
ic_set = [g for g in EU27 if all(pair(g, "I_IUAI", "PC_IND", b) and pair(g, "I_IUAI", "PC_IND_IU3", b) for b in BANDS)]
ic = {g: {b: gap(pair(g, "I_IUAI", "PC_IND", b)) - gap(pair(g, "I_IUAI", "PC_IND_IU3", b)) for b in BANDS} for g in ic_set}
say(f"  N={len(ic_set)}; excluded {sorted(set(EU27)-set(ic_set))}")
for b in BANDS:
    vals = sorted(ic[g][b] for g in ic_set); m_script = vals[len(vals) // 2]
    over1 = sum(1 for v in vals if abs(v) > 1); over1_neg = sum(1 for v in vals if v < -1)
    say(f"  {b}: median (script sorted[N//2]) {m_script:+.2f}, true median {median(vals):+.2f}, |share|>1 in {over1} countries (below −1 in {over1_neg}), min {vals[0]:+.2f} max {vals[-1]:+.2f}")
    check(f"internet_composition.band_medians.{b}", m_script, RES["internet_composition"]["band_medians"][b])
check("internet_composition.N", len(ic_set), RES["internet_composition"]["N"])
eu_ic = {b: eu_bands[b] - gap(pair(EU, "I_IUAI", "PC_IND_IU3", b)) for b in BANDS}; say(f"  EU27 composition share by band: { {b: round(v, 2) for b, v in eu_ic.items()} }")
say("\n== F4. Sets, flagged appendix ==")
ext_g = {g: gap(pair(g, "I_IUAI", "PC_IND", "Y16_74")) for g in EXT if pair(g, "I_IUAI", "PC_IND", "Y16_74")}
say(f"  EU27 median gap {sorted(crude.values())[13]:.2f}; extension N {len(ext_g)} median (sorted[N//2]) {sorted(ext_g.values())[len(ext_g)//2]:.2f}, reversed {sorted(g for g,v in ext_g.items() if v<0)}; all35 median {sorted(list(crude.values())+list(ext_g.values()))[(27+len(ext_g))//2]:.2f}")
check("sets.eu27.median", sorted(crude.values())[13], RES["sets"]["eu27"]["median"]); check("sets.extension.N", len(ext_g), RES["sets"]["extension"]["N"]); check("sets.extension.reversed", sorted(g for g, v in ext_g.items() if v < 0), RES["sets"]["extension"]["reversed"])
flagged = 0
for g in EU27 + EXT:
    for ind in ["I_IUAI", "I_IUAIPR", "I_IUAIWP", "I_IUAIFE"]:
        for unit in ["PC_IND", "PC_IND_IU3", "PC_IND_IUAI"]:
            f = cell.get((g, ind, unit, "F_Y16_74")); m = cell.get((g, ind, unit, "M_Y16_74"))
            if f and m and f[0] is not None and m[0] is not None and (f[1] == "u" or m[1] == "u"): flagged += 1
check("flagged_appendix_rows", flagged, RES["flagged_appendix_rows"])
say(f"  overall pairs with a value but a u flag on either cell: {flagged}")
say("\n== F5. Triangulation leg (i): OpenAI Signals feminine share, June 2025 ==")
fem = {}
with open(SIG, encoding="cp1252") as fh:
    for r in csv.DictReader(fh):
        if r["month"] == "2025-06-01" and r["typical_name_gender"] == "feminine": fem[r["country"]] = float(r["share_of_messages"])
code = lambda g: "GR" if g == "EL" else g
tri = [(g, crude[g], fem[code(g)]) for g in EU27 if code(g) in fem]
def spearman(x, y):
    def rank(v):
        s = sorted(range(len(v)), key=lambda i: v[i]); r = [0] * len(v); i = 0
        while i < len(s):
            j = i
            while j + 1 < len(s) and v[s[j + 1]] == v[s[i]]: j += 1
            for t in range(i, j + 1): r[s[t]] = (i + j) / 2 + 1
            i = j + 1
        return r
    rx, ry = rank(x), rank(y); n = len(x); mx, my = sum(rx) / n, sum(ry) / n
    return sum((a - mx) * (b - my) for a, b in zip(rx, ry)) / math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))
rho = spearman([t[1] for t in tri], [t[2] for t in tri]); rho_r = spearman([rat[t[0]] for t in tri], [t[2] for t in tri])
say(f"  N={len(tri)}; missing {[g for g in EU27 if code(g) not in fem]}; Spearman gap vs feminine share {rho:+.4f}; ratio vs feminine share {rho_r:+.4f}")
check("triangulation.leg_i.N", len(tri), RES["triangulation"]["leg_i"]["N"]); check("triangulation.leg_i.spearman_gap", rho, RES["triangulation"]["leg_i"]["spearman_gap_vs_feminine_share"], 1e-9)
check("triangulation.leg_i.spearman_ratio", rho_r, RES["triangulation"]["leg_i"]["spearman_ratio_vs_feminine_share"], 1e-9)
# is the Signals column a share of messages *within country* between feminine and masculine, i.e. does fem + masc = 1?
masc = {}
with open(SIG, encoding="cp1252") as fh:
    for r in csv.DictReader(fh):
        if r["month"] == "2025-06-01" and r["typical_name_gender"] == "masculine": masc[r["country"]] = float(r["share_of_messages"])
sums = [fem[c] + masc[c] for c in fem if c in masc]; say(f"  Signals: feminine+masculine sums to 1 within country? min {min(sums):.3f} max {max(sums):.3f} (a third category would make it <1)")
say(f"  Signals feminine share, EU26: min {min(t[2] for t in tri):.3f} max {max(t[2] for t in tri):.3f}")

# ------------------------------------------------------------------ G. captions
say("\n== G. Caption sentences in outputs/figures.json against my numbers ==")
say(f"fig1: 'in every EU country but five' -> reversed on PC_IND {len([g for g in EU27 if crude[g] < 0])} {[g for g in EU27 if crude[g] < 0]}; 'about −2 to +9' -> {min(crude.values()):+.2f}..{max(crude.values()):+.2f}; 'class is stable across measures for only 13 of 27' -> large+small = {counts['large-gap']+counts['small-gap']} (note: 'not distinguishable' is also {counts['not distinguishable']})")
pos_beyond = [g for g in EU27 if crude[g] > 0 and crude[g] > hw(g)]; neg_beyond = [g for g in EU27 if crude[g] < 0 and -crude[g] > hw(g)]
say(f"fig1 (bound): of the 22 positive overall gaps, {len(pos_beyond)} exceed the country's own SRS half-width {sorted(set(g for g in EU27 if crude[g] > 0) - set(pos_beyond))} do not; of the 5 negative, {len(neg_beyond)} exceed it {neg_beyond}; sign not distinguishable from zero at the bound in {27 - len(pos_beyond) - len(neg_beyond)}")
say(f"fig2: 'women lead in 20 of 26 at 16–24' -> negative 16–24 gaps {neg_young}; 'from 25 upward men lead in 17 to 22 of 26' -> {[pos_by_band[b] for b in BANDS[1:]]}; 'no single band holds the largest gap in a majority' -> max over bands {max(largest_band.values())} of 26; 'band half-widths 4 to 8 points' -> medians {[round(median(band_hw_all[b]),1) for b in BANDS]}, full range {min(v[0] for v in band_hw_all.values()):.1f}..{max(v[-1] for v in band_hw_all.values()):.1f}")
say(f"fig3: education participation negative in {sum(1 for g in EU27 if gap(pair(g,'I_IUAIFE','PC_IND','Y16_74'))<0)} of 27, among users negative in {sum(1 for g in EU27 if gap(pair(g,'I_IUAIFE','PC_IND_IUAI','Y16_74'))<0)} of 27; private positive {sum(1 for g in EU27 if gap(pair(g,'I_IUAIPR','PC_IND','Y16_74'))>0)}, work positive {sum(1 for g in EU27 if gap(pair(g,'I_IUAIWP','PC_IND','Y16_74'))>0)}")
say(f"fig4: 'lowers the gap in 25 of 26' -> {lowered}; 'moves three across a tercile cut' -> {len(changed)}")
say(f"fig5: 'under a point at the median in every band' -> max |median| {max(abs(median(ic[g][b] for g in ic_set)) for b in BANDS):.2f}; 'more than a point in ten countries only at 65–74' -> |share|>1 by band {[sum(1 for g in ic_set if abs(ic[g][b])>1) for b in BANDS]}")

say(f"\n== Summary: {n_match} matches, {n_mismatch} mismatches against results.json ==")
open(os.path.join(HERE, "referee_results_gender1.out.txt"), "w").write("\n".join(report) + "\n")
