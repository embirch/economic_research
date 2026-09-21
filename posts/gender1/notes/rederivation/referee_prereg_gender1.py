"""Referee re-derivation for the gender1 pre-registration review (21 September 2026).

Reads ONLY what the review point permits: the EU27_2020 aggregate cells, the country both-sex overall rates
(IND_TOTAL / I_IUAI / PC_IND), the usability status (missing or flagged `u`) of sex-specific cells, the
national sample sizes and the demo_pjan JSON. It never loads the VALUE of any sex-specific cell below the
EU27 aggregate: the `usable()` helper returns a boolean and the value string is discarded.

Sections
  A  EU27 2025 age weights from demo_pjan (own indexing of the JSON-stat cube)
  B  sampling bound for IT, DE, MT from the committed sample-size table, and with the net sample [D]
     read from the national reference-metadata pages (sensitivity)
  C  coverage counts for the registered rules (usable pairs; no values)
  D  the disclosed EU27 values, checked against the aggregate cells
  E  what the count rules do under a null of no pattern and under the disclosed EU27 profile
     (simulation with the per-country SRS bound; both-sex rates and bounds only)
  F  the band-level consequence of assumption A4 (overall rate used in every band), from EU27 band rates
"""
import csv, json, math, os, random, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
POST = os.path.dirname(os.path.dirname(HERE))
REPO = os.path.dirname(os.path.dirname(POST))
TSV = os.path.join(REPO, "data", "cache", "eurostat", "isoc_ai_iaiu.tsv")
PJAN = os.path.join(REPO, "data", "cache", "eurostat", "demo_pjan_EU27_2025.json")
NS = os.path.join(POST, "data", "processed", "national_sample_sizes_2025.csv")
PR = os.path.join(POST, "data", "processed", "power_rules.json")
OUT = open(os.path.join(HERE, "referee_prereg_gender1.out.txt"), "w")


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    OUT.write(s + "\n")


EU = "EU27_2020"
EU27 = "AT BE BG CY CZ DE DK EE EL ES FI FR HR HU IE IT LT LU LV MT NL PL PT RO SE SI SK".split()
EXT = "AL BA CH MK NO RS TR XK".split()
BANDS = ["Y16_24", "Y25_34", "Y35_44", "Y45_54", "Y55_64", "Y65_74"]
EDU = ["I0_2", "I3_4", "I5_8"]

# ---------------------------------------------------------------- load the TSV into a status map and a permitted-value map
status = {}   # (grp, ind, unit, geo) -> True if usable (non-missing, not flagged u)
permitted = {}  # values for EU27 cells and for both-sex country cells only
for r in csv.reader(open(TSV), delimiter="\t"):
    if r[0].startswith("freq"):
        continue
    _, grp, ind, unit, geo = r[0].split(",")
    raw = r[1].strip()
    missing = raw.startswith(":")
    flagged = raw.endswith("u")
    status[(grp, ind, unit, geo)] = (not missing) and (not flagged)
    if not missing and (geo == EU or not grp.startswith(("F_", "M_"))):
        permitted[(grp, ind, unit, geo)] = float(raw.split()[0])

geos_all = sorted({k[3] for k in status})
countries36 = [g for g in geos_all if g != "EA"]  # the brief's 36 = 35 geographies + EU27_2020
assert len(geos_all) == 37 and len(countries36) == 36
assert sorted(EU27 + EXT + [EU]) == sorted(countries36)


def usable(grp, ind="I_IUAI", unit="PC_IND", geo=None):
    return status.get((grp, ind, unit, geo), False)


def pair_usable(suffix, ind="I_IUAI", unit="PC_IND", geo=None):
    return usable("F_" + suffix, ind, unit, geo) and usable("M_" + suffix, ind, unit, geo)


# ================================================================ A · age weights
say("=== A · EU27 2025 age weights from demo_pjan (own code)")
d = json.load(open(PJAN))
dims, sizes = d["id"], d["size"]
cat = {k: d["dimension"][k]["category"]["index"] for k in dims}
strides = {}
s = 1
for k, n in zip(reversed(dims), reversed(sizes)):
    strides[k] = s
    s *= n


def cell(coords):
    i = sum(strides[k] * cat[k][coords[k]] for k in dims)
    return d["value"].get(str(i))


pop = {}
for b in BANDS:
    lo, hi = int(b[1:3]), int(b[4:6])
    vals = [cell({"freq": "A", "unit": "NR", "age": f"Y{a}", "sex": "T", "geo": EU, "time": "2025"}) for a in range(lo, hi + 1)]
    assert all(v is not None for v in vals), b
    pop[b] = sum(vals)
tot = sum(pop.values())
w = {b: pop[b] / tot for b in BANDS}
pr = json.load(open(PR))
say("population 16-74 (T):", f"{tot:,.0f}")
for b in BANDS:
    say(f"  {b}: pop {pop[b]:>12,.0f}  weight {w[b]:.6f}  power_rules {pr['eu27_age_weights'][b]:.6f}  diff {abs(w[b]-pr['eu27_age_weights'][b]):.1e}")
say("sum of weights:", f"{sum(w.values()):.12f}", "| status flags in file:", sorted(set(d.get("status", {}).values())))
say("prereg's rounded weights (0.131, 0.158, 0.179, 0.189, 0.188, 0.155):", [round(w[b], 3) for b in BANDS])
# sex check: T = M + F per age
mf_ok = all(abs(cell({"freq": "A", "unit": "NR", "age": f"Y{a}", "sex": "T", "geo": EU, "time": "2025"})
                - cell({"freq": "A", "unit": "NR", "age": f"Y{a}", "sex": "M", "geo": EU, "time": "2025"})
                - cell({"freq": "A", "unit": "NR", "age": f"Y{a}", "sex": "F", "geo": EU, "time": "2025"})) < 1 for a in range(16, 75))
say("T = M + F at every single age:", mf_ok)
# female share by band (relevant to assumption A1 "half per sex")
for b in BANDS:
    lo, hi = int(b[1:3]), int(b[4:6])
    f = sum(cell({"freq": "A", "unit": "NR", "age": f"Y{a}", "sex": "F", "geo": EU, "time": "2025"}) for a in range(lo, hi + 1))
    say(f"  female share of population {b}: {f/pop[b]:.3f}")

# ================================================================ B · sampling bound
say("\n=== B · sampling bound for IT, DE, MT")
ns = {}
for r in csv.DictReader(open(NS)):
    n = r["n_individuals_16_74_achieved"] or r["n_implied"]
    ns[r["geo"]] = int(float(n)) if n else None
rate = {g: permitted.get(("IND_TOTAL", "I_IUAI", "PC_IND", g)) for g in countries36}


def bound(p, n):
    """p in %, n total; half per sex; SRS. Returns (se per sex, se gap, 95% half-width, 2.8*se)."""
    q = p / 100
    se = 100 * math.sqrt(q * (1 - q) / (n / 2))
    seg = math.sqrt(2) * se
    return se, seg, 1.96 * seg, 2.8 * seg


# net sample of individuals aged 16-74, row [D] of section 13.3.3.1.1 of the national reference metadata
# (isoc_i_simsih2_<cc>.htm, fetched by the referee 21 Sep 2026; parsed in /tmp, transcribed here by hand)
netD = {"AT": 5550, "BE": 6081, "BG": 7272, "CY": 3275, "CZ": 4494, "DE": 12701, "DK": 3876, "EE": 3866, "EL": 3440,
        "ES": 14251, "FI": 3023, "FR": 11513, "HR": 3116, "IT": 31536, "LT": 4389, "LU": 2514, "LV": 5237, "MT": 1725,
        "NL": 5603, "PL": 10013, "PT": 8261, "RO": 14987, "SE": 4450, "SI": 2859, "SK": 3225,
        "AL": 4702, "BA": 5814, "CH": 2767, "NO": 2071, "RS": 2633}
# not read from [D]: HU (households only: 6,262), TR (household addresses: 11,924), IE (row not parseable;
# reference-indicator block cites the 2022 questionnaire and INFOSOC_HHNSI_A_2023_IE), MK and XK (no page).
for g in ["IT", "DE", "MT"]:
    se, seg, hw, mde = bound(rate[g], ns[g])
    c = pr["countries"][g]
    say(f"{g}: n(csv)={ns[g]:,} p={rate[g]} -> se/sex {se:.2f} gap-se {seg:.2f} half-width {hw:.2f} mde80 {mde:.2f}"
        f" | power_rules: {c['rate_se_per_sex_pp']} {c['gap_se_pp']} {c['gap_halfwidth95_pp']} {c['gap_mde80_pp']}")
    se2, seg2, hw2, _ = bound(rate[g], netD[g])
    say(f"     with net sample [D]={netD[g]:,}: half-width {hw2:.2f}")
say("\nsample-size table against the national pages (net individuals 16-74, row [D]):")
say(f"{'geo':4} {'csv n':>7} {'src':>8} {'net[D]':>7} {'ratio':>6}  half-width csv -> [D]")
flag_rows = []
for g in sorted(netD):
    if g not in ns or ns[g] is None:
        hw2 = bound(rate[g], netD[g])[2] if rate.get(g) else float("nan")
        say(f"{g:4} {'-':>7} {'none':>8} {netD[g]:>7,} {'-':>6}  (no bound in power_rules)  -> {hw2:.2f}")
        flag_rows.append(g)
        continue
    src = "achieved" if g in ("CZ", "IT") else "implied"
    ratio = ns[g] / netD[g]
    hw1 = bound(rate[g], ns[g])[2]
    hw2 = bound(rate[g], netD[g])[2]
    mark = "  <-- " if abs(ratio - 1) > 0.10 else ""
    say(f"{g:4} {ns[g]:>7,} {src:>8} {netD[g]:>7,} {ratio:>6.2f}  {hw1:.2f} -> {hw2:.2f}{mark}")
    if abs(ratio - 1) > 0.10:
        flag_rows.append(g)
say("rows off by more than 10%, or missing a bound:", flag_rows)
# published SE / SRS SE on the reference indicator, my own computation
say("\nreference indicator: published SE / SRS SE (own computation from the csv)")
ratios = {}
for r in csv.DictReader(open(NS)):
    g = r["geo"]
    if r["ref_prop_pct"] and r["ref_se_pp"] and ns.get(g):
        p, se_pub = float(r["ref_prop_pct"]), float(r["ref_se_pp"])
        if se_pub > 0.05:
            srs = 100 * math.sqrt((p / 100) * (1 - p / 100) / ns[g])
            ratios[g] = se_pub / srs
say("median", f"{statistics.median(ratios.values()):.2f}", "over", len(ratios), "| IT", f"{ratios['IT']:.2f}", "DE", f"{ratios['DE']:.2f}",
    "MT", f"{ratios['MT']:.2f}", "RO", f"{ratios['RO']:.2f}", "| >1.3:", {g: round(v, 2) for g, v in ratios.items() if v > 1.3})
# the same ratio with the net sample [D] where the csv's n is off by >10%: a corroboration of the [D] figure
for r in csv.DictReader(open(NS)):
    g = r["geo"]
    if g in ("CZ", "LU", "SE", "PT", "AL") and r["ref_prop_pct"] and r["ref_se_pp"] and g in netD:
        p, se_pub = float(r["ref_prop_pct"]), float(r["ref_se_pp"])
        srs = 100 * math.sqrt((p / 100) * (1 - p / 100) / netD[g])
        say(f"  {g}: published/SRS with csv n = {ratios.get(g, float('nan')):.2f}; with net [D] n = {se_pub/srs:.2f}"
            + ("  (LU and SE report the yes-count equal to the net sample, so 'implied' n = n / proportion overstates n)" if g in ("LU", "SE") else ""))

# ================================================================ C · coverage counts (no values read)
say("\n=== C · coverage for the registered rules (usable = non-missing and not flagged u)")
ov = [g for g in countries36 if pair_usable("Y16_74", geo=g)]
say("overall usable pairs I_IUAI PC_IND:", len(ov), "of", len(countries36))
ov_iu3 = [g for g in countries36 if pair_usable("Y16_74", unit="PC_IND_IU3", geo=g)]
say("overall usable pairs I_IUAI PC_IND_IU3 (reversed rule's second leg):", len(ov_iu3), "of 36")
complete = [g for g in countries36 if all(pair_usable(b, geo=g) for b in BANDS)]
incomplete = [g for g in countries36 if g not in complete]
say("all twelve sex-by-age cells usable I_IUAI PC_IND:", len(complete), "of 36; incomplete:", incomplete)
say("  EU27 members with all twelve:", len([g for g in complete if g in EU27]), "of 27; extension:", len([g for g in complete if g in EXT]), "of 8")
for g in incomplete:
    say("  ", g, "missing or flagged band pairs:", [b for b in BANDS if not pair_usable(b, geo=g)])
complete_iu3 = [g for g in EU27 if all(pair_usable(b, unit="PC_IND_IU3", geo=g) for b in BANDS)]
say("EU27 with all twelve band pairs on PC_IND_IU3 (internet-composition share by band):", len(complete_iu3), "of 27")
for b in BANDS:
    say(f"  band {b}: EU27 usable pairs PC_IND {sum(pair_usable(b, geo=g) for g in EU27)}, PC_IND_IU3 {sum(pair_usable(b, unit='PC_IND_IU3', geo=g) for g in EU27)}")
hw_set = [g for g in EU27 if pair_usable("Y16_74", "I_IUAIWP", geo=g) and pair_usable("Y16_74", "I_IUAIPR", geo=g)]
say("H-work usable EU27 (work and private pairs, PC_IND):", len(hw_set), "of 27; excluded:", [g for g in EU27 if g not in hw_set])
hw_set_u = [g for g in EU27 if pair_usable("Y16_74", "I_IUAIWP", "PC_IND_IUAI", g) and pair_usable("Y16_74", "I_IUAIPR", "PC_IND_IUAI", g)]
say("H-work secondary (PC_IND_IUAI) usable EU27:", len(hw_set_u), "of 27")
he_set = [g for g in EU27 if all(pair_usable(e, geo=g) for e in EDU)]
say("H-education usable EU27 (three education pairs, PC_IND):", len(he_set), "of 27; excluded:", [g for g in EU27 if g not in he_set])
for ind in ["I_IUAIPR", "I_IUAIWP", "I_IUAIFE"]:
    n_c = sum(all(pair_usable(b, ind, "PC_IND", g) for b in BANDS) for g in EU27)
    say(f"robustness 8, purpose {ind}: EU27 geographies with all twelve band pairs usable = {n_c} (rule needs >= 15)")
    say(f"   per band: {[sum(pair_usable(b, ind, 'PC_IND', g) for g in EU27) for b in BANDS]}")
# sample-size bound availability against the registered sets
say("EU27 members with a bound in power_rules.json:", len([g for g in EU27 if pr["countries"].get(g, {}).get("n")]), "of 27; without:",
    [g for g in EU27 if not pr["countries"].get(g, {}).get("n")])
say("extension with a bound:", [g for g in EXT if pr["countries"].get(g, {}).get("n")], "without:", [g for g in EXT if not pr["countries"].get(g, {}).get("n")])

# ================================================================ D · disclosed EU27 values
say("\n=== D · the disclosed EU27 aggregate values, from the aggregate cells")


def eu(grp, ind="I_IUAI", unit="PC_IND"):
    return permitted.get((grp, ind, unit, EU))


say("headline both sexes 16-74:", eu("IND_TOTAL"), "| women", eu("F_Y16_74"), "| men", eu("M_Y16_74"), "| gap", round(eu("M_Y16_74") - eu("F_Y16_74"), 2))
for ind, lab in [("I_IUAIPR", "private"), ("I_IUAIWP", "work"), ("I_IUAIFE", "education")]:
    say(f"  purpose {lab:9} PC_IND gap: {eu('M_Y16_74', ind) - eu('F_Y16_74', ind):.2f}   (F {eu('F_Y16_74', ind)}, M {eu('M_Y16_74', ind)})")
say("  education among AI users (PC_IND_IUAI): F", eu("F_Y16_74", "I_IUAIFE", "PC_IND_IUAI"), "M", eu("M_Y16_74", "I_IUAIFE", "PC_IND_IUAI"))
prof = [round(eu("M_" + b) - eu("F_" + b), 2) for b in BANDS]
say("  age profile of the gap:", prof)
say("  education profile of the gap:", [round(eu("M_" + e) - eu("F_" + e), 2) for e in EDU])
say("  both-sex band rates (for section F):", {b: eu(b) for b in BANDS})
# crude vs standardised at EU level is NOT computed for any country; at EU level it is the identity check only
std_m = sum(w[b] * eu("M_" + b) for b in BANDS)
std_f = sum(w[b] * eu("F_" + b) for b in BANDS)
say(f"  EU27 standardised with its own weights: M {std_m:.2f} F {std_f:.2f} (published M {eu('M_Y16_74')} F {eu('F_Y16_74')}; the survey's household population differs from demo_pjan, so equality is not expected)")

# ================================================================ E · the count rules under a null and under the EU profile
say("\n=== E · count rules: expected raw counts under a null of no pattern and under the disclosed EU27 profile")
random.seed(20260921)
R = 20000
eu_gap = eu("M_Y16_74") - eu("F_Y16_74")
# per-country gap SE (overall and per band) from the committed power_rules.json, EU27 members with a bound
mem = [g for g in EU27 if pr["countries"].get(g, {}).get("n")]
se_ov = {g: pr["countries"][g]["gap_se_pp"] for g in mem}
se_b = {g: {b: pr["countries"][g]["bands"][b]["gap_se_pp"] for b in BANDS} for g in mem}


def sim_age(true_profile):
    a_cnt = b_cnt = 0
    for _ in range(R):
        na = nb = 0
        for g in mem:
            draw = [true_profile[i] + random.gauss(0, se_b[g][BANDS[i]]) for i in range(6)]
            if draw[0] == min(draw) or draw[0] < 0:
                na += 1
            if max(draw) in (draw[1], draw[2]):
                nb += 1
        a_cnt += na
        b_cnt += nb
    return a_cnt / R, b_cnt / R


N = len(mem)
say(f"EU27 members with a bound: {N}; majority = {N//2+1}")
null_a, null_b = sim_age([eu_gap] * 6)
say(f"H-age under a null of six equal true band gaps ({eu_gap:.1f} pp) with the band bounds: expected count satisfying (a) {null_a:.1f}, (b) {null_b:.1f} of {N}")
alt_a, alt_b = sim_age(prof)
say(f"H-age if every country had the EU27 profile {prof}: expected count (a) {alt_a:.1f}, (b) {alt_b:.1f} of {N}")


def p_majority(true_profile, which):
    hits = 0
    for _ in range(R // 4):
        n_ok = 0
        for g in mem:
            draw = [true_profile[i] + random.gauss(0, se_b[g][BANDS[i]]) for i in range(6)]
            ok = (draw[0] == min(draw) or draw[0] < 0) if which == "a" else (max(draw) in (draw[1], draw[2]))
            n_ok += ok
        hits += n_ok > N / 2
    return hits / (R // 4)


say(f"  P(raw majority) for (a): null {p_majority([eu_gap]*6, 'a'):.3f}, EU profile {p_majority(prof, 'a'):.3f}")
say(f"  P(raw majority) for (b): null {p_majority([eu_gap]*6, 'b'):.3f}, EU profile {p_majority(prof, 'b'):.3f}")
# H-work: difference of two gaps; under the null P(work > private) = 1/2 per country
from math import comb
def p_bin_ge(n, k, p=0.5):
    return sum(comb(n, j) * p**j * (1-p)**(n-j) for j in range(k, n + 1))
say(f"H-work under a null of equal work and private gaps: P(country shows work > private) = 1/2; P(raw majority of {len(hw_set)}) = {p_bin_ge(len(hw_set), len(hw_set)//2+1):.3f}")
# under the EU profile (work 3.0, private 5.5) with the difference-of-gaps SE ~ sqrt(2) x overall gap SE (independence, conservative)
pw = 0
for g in mem:
    sed = math.sqrt(2) * se_ov[g]
    z = (eu("M_Y16_74", "I_IUAIWP") - eu("F_Y16_74", "I_IUAIWP") - (eu("M_Y16_74", "I_IUAIPR") - eu("F_Y16_74", "I_IUAIPR"))) / sed
    pw += 0.5 * (1 + math.erf(z / math.sqrt(2)))
say(f"  if every country had the EU27 purpose gaps (work-private = {eu('M_Y16_74','I_IUAIWP')-eu('F_Y16_74','I_IUAIWP')-(eu('M_Y16_74','I_IUAIPR')-eu('F_Y16_74','I_IUAIPR')):.2f}): expected count work > private = {pw:.1f} of {N}")
say(f"H-education under a null of three equal gaps: P(high is largest) = 1/3; P(raw majority of {len(he_set)}) = {p_bin_ge(len(he_set), len(he_set)//2+1, 1/3):.3f}")
say(f"H-composition: 'at most one third' of 26 = at most {26//3} changes; 'more than one third' = {26//3+1} or more")

# the class rule under a pure-noise null: all EU27 countries share one true gap; how many land in a tercile on all three measures?
say("\nclass rule under a null of one common true gap (4.0 pp) and each country's own SRS noise (gap, ratio = 1 - gap/p_M, standardised = gap + small age term):")
large = small = 0
p_m = {g: rate[g] + eu_gap / 2 for g in mem}  # both-sex rate plus half the EU gap as a stand-in male rate (permitted inputs only)
for _ in range(R // 4):
    gaps = {g: 4.0 + random.gauss(0, se_ov[g]) for g in mem}
    ratio = {g: 1 - gaps[g] / p_m[g] for g in mem}
    std = {g: gaps[g] + random.gauss(0, 0.3) for g in mem}   # standardised differs from crude by a small age-structure term
    k = len(mem) // 3
    top = lambda dct, rev: set(sorted(dct, key=dct.get, reverse=rev)[:k])
    L = top(gaps, True) & top({g: -ratio[g] for g in mem}, True) & top(std, True)
    S = top(gaps, False) & top({g: -ratio[g] for g in mem}, False) & top(std, False)
    large += len(L)
    small += len(S)
say(f"  expected number classed large-gap {large/(R//4):.1f}, small-gap {small/(R//4):.1f} of {N} when NO country differs from another")
say("  (if the three measures were independent the expectation would be", f"{N*(1/3)**3:.1f})")

# ================================================================ F · assumption A4 at band level
say("\n=== F · A4 at band level: overall rate vs EU27 band rate in the binomial variance")
p_all = eu("IND_TOTAL")
for b in BANDS:
    pb = eu(b)
    f = math.sqrt(pb * (100 - pb) / (p_all * (100 - p_all)))
    say(f"  {b}: EU27 both-sex rate {pb:5.2f} vs overall {p_all}; true SRS half-width / stated = {f:.2f}")
OUT.close()
