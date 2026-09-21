"""Referee re-derivation · gender1 · results stage · supplementary checks.

(1) The H-composition count under the two readings of the registered class rule: per-measure tercile over each
    measure's own usable set (gap: 27; standardised: 26), counted on the intersection [the text's literal reading];
    or both terciles recomputed on the 26 with a standardised gap [the analyst's script 05]. Same for ratio-vs-standardised.
(2) The persistent class rule under a null of one common true gap, with the registered k = round(N/3) and tie rule,
    each country's own SRS bound from power_rules.json, ratio and standardised gap simulated from the same draws.
(3) H-work: the sign of work − private under the among-users denominator, and the joint count.
(4) Rule (a) of H-age: how much of the count is the negative-at-16–24 clause alone.
No import from the analyst's scripts.
"""
import csv, json, math, os, random
from statistics import median
HERE = os.path.dirname(os.path.abspath(__file__)); POST = os.path.dirname(os.path.dirname(HERE)); REPO = os.path.dirname(os.path.dirname(POST))
TSV = os.path.join(REPO, "data", "cache", "eurostat", "isoc_ai_iaiu.tsv")
PW = json.load(open(os.path.join(POST, "data", "processed", "power_rules.json")))
EU27 = sorted("AT BE BG HR CY CZ DK EE FI FR DE EL HU IE IT LV LT LU MT NL PL PT RO SK SI ES SE".split())
BANDS = ["Y16_24", "Y25_34", "Y35_44", "Y45_54", "Y55_64", "Y65_74"]
W = PW["eu27_age_weights"]
out = []
def say(*a): s = " ".join(str(x) for x in a); print(s); out.append(s)

cell = {}
for row in csv.reader(open(TSV, encoding="utf-8"), delimiter="\t"):
    if row[0].startswith("freq"): continue
    _, grp, ind, unit, geo = row[0].split(","); tok = row[1].strip().split()
    cell[(geo, ind, unit, grp)] = (None if tok[0] == ":" else float(tok[0]), tok[1] if len(tok) > 1 and tok[0] != ":" else "")
def usable(k): v = cell.get(k); return v is not None and v[0] is not None and v[1] != "u"
def pair(geo, ind, unit, suf):
    kf, km = (geo, ind, unit, "F_" + suf), (geo, ind, unit, "M_" + suf)
    return (cell[kf][0], cell[km][0]) if usable(kf) and usable(km) else None
def tercile(vals, larger=True, tie=0.1):
    items = sorted(vals.items(), key=(lambda kv: -kv[1]) if larger else (lambda kv: kv[1])); N = len(items); k = int(round(N / 3))
    tc, bc = items[k][1], items[N - k - 1][1]
    return {g: ("top" if (i < k and abs(v - tc) > tie) else ("bottom" if (i >= N - k and abs(v - bc) > tie) else "middle")) for i, (g, v) in enumerate(items)}

crude = {g: pair(g, "I_IUAI", "PC_IND", "Y16_74")[1] - pair(g, "I_IUAI", "PC_IND", "Y16_74")[0] for g in EU27}
rat = {g: pair(g, "I_IUAI", "PC_IND", "Y16_74")[0] / pair(g, "I_IUAI", "PC_IND", "Y16_74")[1] for g in EU27}
age_set = [g for g in EU27 if all(pair(g, "I_IUAI", "PC_IND", b) for b in BANDS)]
std = {g: sum(W[b] * (pair(g, "I_IUAI", "PC_IND", b)[1] - pair(g, "I_IUAI", "PC_IND", b)[0]) for b in BANDS) for g in age_set}

say("== (1) H-composition under the two readings of the registered rule ==")
t_gap27 = tercile(crude); t_rat27 = tercile(rat, False, 0.01); t_std = tercile(std)
t_gap26 = tercile({g: crude[g] for g in age_set}); t_rat26 = tercile({g: rat[g] for g in age_set}, False, 0.01)
A = sorted(g for g in age_set if t_gap27[g] != t_std[g]); B = sorted(g for g in age_set if t_gap26[g] != t_std[g])
say(f"  crude vs standardised — literal reading (gap tercile over 27, counted on the 26): {len(A)} {A}")
say(f"  crude vs standardised — analyst's script 05 (crude tercile recomputed on the 26): {len(B)} {B}")
say(f"  the difference is FR: 10th of 27 on the crude gap (middle; cut 4.53 = FR's own value) but 9th of 26 (top; cut AT 4.25). FR's standardised tercile is middle either way.")
C = sorted(g for g in age_set if t_rat27[g] != t_std[g]); Dd = sorted(g for g in age_set if t_rat26[g] != t_std[g])
say(f"  ratio vs standardised — ratio tercile over 27 (analyst's script 05): {len(C)} {C}")
say(f"  ratio vs standardised — ratio tercile recomputed on the 26: {len(Dd)} {Dd}")
say(f"  gap vs ratio (both over 27, no ambiguity): {sum(1 for g in EU27 if t_gap27[g] != t_rat27[g])}")
say("  => script 05 applies one reading to crude-vs-standardised (recompute on 26) and the other to ratio-vs-standardised (27 vs 26). Verdict unchanged under either (≤ 8).")

say("\n== (2) Persistent class rule under a null of ONE common true gap; registered k and tie rule; own SRS bounds ==")
# Every country: true male rate = EU band rate + 2, female = band rate − 2 in every band (one common true gap of 4 points, no
# composition difference). Band rates drawn under SRS with n/2 per sex and EU band shares (A1, A3, A4). Crude = Σ w_b p_b plus a
# small country-specific composition term (the country's own sex-specific age structure), standardised = Σ w_b p_b, ratio from the
# crude rates. The three measures are therefore the same draws re-expressed, as the published cells are.
random.seed(11)
gs = age_set; eb = PW["eu27_band_rates_pct"]
def se_rate(p, n): return math.sqrt(p * (100 - p) / n)
for comp_sd in (0.0, 0.5, 1.0):
    R = 3000; L = S = dL = dS = 0; hist = {}
    for _ in range(R):
        gap = {}; rat = {}; sd = {}
        for g in gs:
            c = PW["countries"][g]; n2 = c["n"] / 2; sM = sF = 0.0
            for b in BANDS:
                nb = n2 * W[b]; pb = eb[b]
                sM += W[b] * (pb + 2 + random.gauss(0, se_rate(pb, nb))); sF += W[b] * (pb - 2 + random.gauss(0, se_rate(pb, nb)))
            comp = random.gauss(0, comp_sd)
            gap[g] = sM - sF + comp; rat[g] = (sF - comp / 2) / (sM + comp / 2); sd[g] = sM - sF
        t1 = tercile(gap); t2 = tercile(rat, False, 0.01); t3 = tercile(sd)
        items = sorted(gap.values(), reverse=True); tc, bc = items[9], items[-10]
        l = [g for g in gs if t1[g] == t2[g] == t3[g] == "top"]; s = [g for g in gs if t1[g] == t2[g] == t3[g] == "bottom"]
        L += len(l); S += len(s); hist[len(l) + len(s)] = hist.get(len(l) + len(s), 0) + 1
        dL += sum(1 for g in l if abs(gap[g] - tc) > PW["countries"][g]["gap_halfwidth95_pp"]); dS += sum(1 for g in s if abs(gap[g] - bc) > PW["countries"][g]["gap_halfwidth95_pp"])
    say(f"  composition term sd {comp_sd}: null mean large-gap {L/R:.2f}, small-gap {S/R:.2f} of 26 (observed 6 and 7); P(large+small >= 13) = {sum(v for k, v in hist.items() if k >= 13)/R:.2f}; mean distinguishable large {dL/R:.2f}, small {dS/R:.2f} (observed 2 and 4)")
say("  => the class COUNTS (6 / 7 / 13) are what one common gap plus sampling noise produces; the distinguishable MARKS (DK, PL; EE, HR, LT, SI) are not.")

say("\n== (3) H-work: joint sign on both denominators ==")
w = {g: (pair(g, "I_IUAIWP", "PC_IND", "Y16_74")[1] - pair(g, "I_IUAIWP", "PC_IND", "Y16_74")[0]) - (pair(g, "I_IUAIPR", "PC_IND", "Y16_74")[1] - pair(g, "I_IUAIPR", "PC_IND", "Y16_74")[0]) for g in EU27}
u = {g: (pair(g, "I_IUAIWP", "PC_IND_IUAI", "Y16_74")[1] - pair(g, "I_IUAIWP", "PC_IND_IUAI", "Y16_74")[0]) - (pair(g, "I_IUAIPR", "PC_IND_IUAI", "Y16_74")[1] - pair(g, "I_IUAIPR", "PC_IND_IUAI", "Y16_74")[0]) for g in EU27}
say(f"  work > private among all individuals: {sorted(g for g in EU27 if w[g] > 0)}; among users: {sorted(g for g in EU27 if u[g] > 0)}; both: {sorted(g for g in EU27 if w[g] > 0 and u[g] > 0)}")
say(f"  work gap and private gap, EU27 medians: work {median(pair(g,'I_IUAIWP','PC_IND','Y16_74')[1]-pair(g,'I_IUAIWP','PC_IND','Y16_74')[0] for g in EU27):.2f}, private {median(pair(g,'I_IUAIPR','PC_IND','Y16_74')[1]-pair(g,'I_IUAIPR','PC_IND','Y16_74')[0] for g in EU27):.2f}")
say(f"  private-use rates, EU27 aggregate: F {pair('EU27_2020','I_IUAIPR','PC_IND','Y16_74')[0]} M {pair('EU27_2020','I_IUAIPR','PC_IND','Y16_74')[1]}; work-use: F {pair('EU27_2020','I_IUAIWP','PC_IND','Y16_74')[0]} M {pair('EU27_2020','I_IUAIWP','PC_IND','Y16_74')[1]} — the work base rate is about half the private base rate, so equal ratios would give a smaller work gap in points")
say(f"  ratio form: EU27 private p_F/p_M {pair('EU27_2020','I_IUAIPR','PC_IND','Y16_74')[0]/pair('EU27_2020','I_IUAIPR','PC_IND','Y16_74')[1]:.3f}, work {pair('EU27_2020','I_IUAIWP','PC_IND','Y16_74')[0]/pair('EU27_2020','I_IUAIWP','PC_IND','Y16_74')[1]:.3f}")
rw = {g: pair(g, "I_IUAIWP", "PC_IND", "Y16_74")[0] / pair(g, "I_IUAIWP", "PC_IND", "Y16_74")[1] for g in EU27}; rp = {g: pair(g, "I_IUAIPR", "PC_IND", "Y16_74")[0] / pair(g, "I_IUAIPR", "PC_IND", "Y16_74")[1] for g in EU27}
say(f"  countries where the work RATIO shows the larger male lead (rw < rp): {sum(1 for g in EU27 if rw[g] < rp[g])} of 27 — an unregistered check, reported for the red team only")

say("\n== (4) H-age rule (a): the two clauses ==")
bg = {g: {b: pair(g, "I_IUAI", "PC_IND", b)[1] - pair(g, "I_IUAI", "PC_IND", b)[0] for b in BANDS} for g in age_set}
neg = [g for g in age_set if bg[g]["Y16_24"] < 0]; small = [g for g in age_set if bg[g]["Y16_24"] < min(bg[g][b] for b in BANDS[1:])]
say(f"  negative at 16–24: {len(neg)}; smallest of six: {len(small)}; negative but not smallest: {sorted(set(neg)-set(small))}; smallest but not negative: {sorted(set(small)-set(neg))}")
say(f"  16–24 gap by country: " + ", ".join(f"{g} {bg[g]['Y16_24']:+.1f}" for g in sorted(age_set, key=lambda g: bg[g]['Y16_24'])))
say(f"  16–24 female and male rates, EU27: F {pair('EU27_2020','I_IUAI','PC_IND','Y16_24')[0]} M {pair('EU27_2020','I_IUAI','PC_IND','Y16_24')[1]}")
say(f"  65–74 holds the largest gap in {sum(1 for g in age_set if max(BANDS, key=lambda b: bg[g][b]) == 'Y65_74')} of 26; 65–74 rates EU27 F {pair('EU27_2020','I_IUAI','PC_IND','Y65_74')[0]} M {pair('EU27_2020','I_IUAI','PC_IND','Y65_74')[1]} (ratio {pair('EU27_2020','I_IUAI','PC_IND','Y65_74')[0]/pair('EU27_2020','I_IUAI','PC_IND','Y65_74')[1]:.2f})")
say(f"  band ratios p_F/p_M, EU27: " + ", ".join(f"{b} {pair('EU27_2020','I_IUAI','PC_IND',b)[0]/pair('EU27_2020','I_IUAI','PC_IND',b)[1]:.2f}" for b in BANDS))
open(os.path.join(HERE, "referee_results_gender1_supp.out.txt"), "w").write("\n".join(out) + "\n")
