"""Shared loaders and the registered rules for posts/gender1 (prereg revision 2, content 6050e38).

Nothing here computes a result; scripts import it so that every script applies the same definitions.
"""
import csv, json, math, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(ROOT))
CACHE = os.path.join(REPO, "data", "cache", "eurostat")
PROC = os.path.join(ROOT, "data", "processed")
OUT = os.path.join(ROOT, "outputs")
TSV = os.path.join(CACHE, "isoc_ai_iaiu.tsv")

EU27 = "AT BE BG HR CY CZ DK EE FI FR DE EL HU IE IT LV LT LU MT NL PL PT RO SK SI ES SE".split()
EXT = "AL BA CH MK NO RS TR XK".split()
AGG = ["EU27_2020", "EA"]
BANDS = ["Y16_24", "Y25_34", "Y35_44", "Y45_54", "Y55_64", "Y65_74"]
EDU = ["I0_2", "I3_4", "I5_8"]
INDS = ["I_IUAI", "I_IUAIPR", "I_IUAIWP", "I_IUAIFE"]
UNITS = ["PC_IND", "PC_IND_IU3", "PC_IND_IUAI"]
TIE_GAP, TIE_RATIO = 0.1, 0.01


def load_cells():
    """Long table of every published cell: dicts with geo, ind, unit, grp, value (float or None), flag, usable."""
    cells = []
    with open(TSV, encoding="utf-8") as fh:
        for r in csv.reader(fh, delimiter="\t"):
            if r[0].startswith("freq"):
                continue
            freq, grp, ind, unit, geo = r[0].split(",")
            v = r[1].strip()
            if v.startswith(":"):
                value, flag = None, (v[1:].strip() or "")
            else:
                parts = v.split()
                value, flag = float(parts[0]), (parts[1] if len(parts) > 1 else "")
            cells.append(dict(geo=geo, ind=ind, unit=unit, grp=grp, value=value, flag=flag,
                              usable=(value is not None and flag != "u")))
    return cells


def index(cells):
    return {(c["geo"], c["ind"], c["unit"], c["grp"]): c for c in cells}


def pair(ix, geo, ind, unit, suffix):
    """Female and male cells for a group suffix; returns (pF, pM) if both usable, else None."""
    f = ix.get((geo, ind, unit, "F_" + suffix)); m = ix.get((geo, ind, unit, "M_" + suffix))
    if f and m and f["usable"] and m["usable"]:
        return f["value"], m["value"]
    return None


def gap_ratio(p):
    pF, pM = p
    return pM - pF, (pF / pM if pM else None)


def power():
    return json.load(open(os.path.join(PROC, "power_rules.json")))


def halfwidth(pw, geo, band=None):
    c = pw["countries"].get(geo, {})
    if not c.get("n"):
        return None
    return c["bands"][band]["gap_halfwidth95_pp"] if band else c["gap_halfwidth95_pp"]


def tercile(values, larger_male_lead_is_higher=True, tie=TIE_GAP):
    """Registered per-measure tercile. values: {geo: v} over usable geographies. Returns {geo: 'top'|'bottom'|'middle'}.
    Ranking: larger male lead ranks higher (gap descending; ratio ascending handled by the caller passing the sign)."""
    items = sorted(values.items(), key=lambda kv: -kv[1] if larger_male_lead_is_higher else kv[1])
    N = len(items); k = int(round(N / 3))
    out = {g: "middle" for g, _ in items}
    if k == 0 or N < 3:
        return out, k
    top_cut = items[k][1]      # the (k+1)-th value from the top
    bot_cut = items[-k - 1][1] # the (k+1)-th value from the bottom
    for i, (g, v) in enumerate(items):
        if i < k and abs(v - top_cut) > tie:
            out[g] = "top"
        elif i >= N - k and abs(v - bot_cut) > tie:
            out[g] = "bottom"
    return out, k


def rss(a, b):
    return math.sqrt(a * a + b * b)


def write_json(name, obj):
    os.makedirs(PROC, exist_ok=True)
    json.dump(obj, open(os.path.join(PROC, name), "w"), indent=1)
