#!/usr/bin/env python3
"""Reproducible source checks for the Eurostat generative-AI tables.

Data-steward pilot, 1 October 2026. Verification only: this script checks the
internal consistency of published Eurostat aggregate cells. It produces no
index output, no gender-gap estimate and no ranking.

Usage:
    mkdir -p /tmp/eurostat && cd /tmp/eurostat
    for t in isoc_ai_iaiu isoc_ai_iaiuxr; do
      curl -sSL -o $t.tsv \
        "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/$t/?format=TSV&compressed=false"
    done
    python3 checks.py /tmp/eurostat

Expected SHA-256 at retrieval 2026-10-01 (see eurostat-profile.md section 7):
    isoc_ai_iaiu.tsv    7f668f7be9aaefaa5662ab2ab059875de8ccbe050c5c38a8de4b2c33a96896ab
    isoc_ai_iaiuxr.tsv  8901c5c90b8661e23f609f406d59889efcbc740b09b8639ca9cea48b5eda8ef4
A different hash is not an error; record the new hash and date and rerun.
"""

import collections
import hashlib
import pathlib
import re
import sys

VALUE = re.compile(r"^(:|-?[0-9.]+)\s*([a-z]*)$")
REASONS = [
    "I_IUAIX_NUNN",
    "I_IUAIX_NUUNK",
    "I_IUAIX_NUUSE",
    "I_IUAIX_NUSEC",
    "I_IUAIX_NUOTH",
]
PURPOSES = ["I_IUAIPR", "I_IUAIWP", "I_IUAIFE"]


def load(path):
    """Return {(ind_type, indic_is, unit, geo): (value_or_None, flag)}."""
    cells = {}
    with open(path) as handle:
        handle.readline()  # header: single period, 2025
        for line in handle:
            key, raw = line.rstrip("\n").split("\t")
            _freq, ind_type, indic, unit, geo = key.split(",")
            match = VALUE.match(raw.strip())
            if match is None:
                raise ValueError(f"unparsed cell {raw!r} in {path}")
            number, flag = match.groups()
            cells[(ind_type, indic, unit, geo)] = (
                None if number == ":" else float(number),
                flag,
            )
    return cells


def value(cells, *key):
    cell = cells.get(key)
    return None if cell is None else cell[0]


def check_purpose_denominator(use):
    """C1: PC_IND_IUAI purpose cell == 100 * purpose PC_IND / use PC_IND."""
    worst, count, outliers = 0.0, 0, []
    for ind_type, indic, unit, geo in list(use):
        if unit != "PC_IND_IUAI" or indic not in PURPOSES:
            continue
        ratio = value(use, ind_type, indic, "PC_IND_IUAI", geo)
        numer = value(use, ind_type, indic, "PC_IND", geo)
        denom = value(use, ind_type, "I_IUAI", "PC_IND", geo)
        if None in (ratio, numer, denom) or denom == 0:
            continue
        diff = abs(100 * numer / denom - ratio)
        count += 1
        worst = max(worst, diff)
        if diff > 0.6:
            outliers.append((ind_type, indic, geo, round(diff, 2)))
    return count, worst, outliers


def check_internet_denominator(use):
    """C3: PC_IND_IU3 consistent with the internet-user share implied by I_IUAI."""
    worst, count = 0.0, 0
    for indic in ["I_IUAI"] + PURPOSES:
        for ind_type, measure, unit, geo in list(use):
            if measure != indic or unit != "PC_IND":
                continue
            all_ind = value(use, ind_type, indic, "PC_IND", geo)
            among_iu = value(use, ind_type, indic, "PC_IND_IU3", geo)
            ref_all = value(use, ind_type, "I_IUAI", "PC_IND", geo)
            ref_iu = value(use, ind_type, "I_IUAI", "PC_IND_IU3", geo)
            if None in (all_ind, among_iu, ref_all, ref_iu) or 0 in (ref_iu, among_iu):
                continue
            internet_share = 100 * ref_all / ref_iu
            count += 1
            worst = max(worst, abs(100 * all_ind / internet_share - among_iu))
    return count, worst


def check_nonuse_base(use, nonuse):
    """C2: can the published non-user base be reconstructed from the use table?

    Reconstructed base = (recent internet users) - (generative-AI users),
    both as a percentage of all individuals. Reported as a discrepancy, not
    forced to agree.
    """
    worst, count, by_geo = 0.0, 0, collections.Counter()
    headline_worst = 0.0
    sex_types = sorted({k[0] for k in use if k[0].startswith(("M_", "F_"))})
    geos = sorted({k[3] for k in use})
    for ind_type in sex_types:
        for geo in geos:
            all_ind = value(use, ind_type, "I_IUAI", "PC_IND", geo)
            among_iu = value(use, ind_type, "I_IUAI", "PC_IND_IU3", geo)
            if None in (all_ind, among_iu) or 0 in (all_ind, among_iu):
                continue
            base = 100 * all_ind / among_iu - all_ind
            if base <= 0:
                continue
            for reason in REASONS:
                numer = value(nonuse, ind_type, reason, "PC_IND", geo)
                ratio = value(nonuse, ind_type, reason, "PC_IND_IUAIX", geo)
                if None in (numer, ratio):
                    continue
                diff = abs(100 * numer / base - ratio)
                count += 1
                worst = max(worst, diff)
                if diff > 1.0:
                    by_geo[geo] += 1
                if ind_type in ("M_Y16_74", "F_Y16_74"):
                    headline_worst = max(headline_worst, diff)
    return count, worst, headline_worst, by_geo


def check_reason_exclusivity(nonuse, geo="EU27_2020"):
    """C4: the five main reasons are single-response and sum to about 100%."""
    out = {}
    for ind_type in ("IND_TOTAL", "M_Y16_74", "F_Y16_74"):
        parts = [value(nonuse, ind_type, r, "PC_IND_IUAIX", geo) for r in REASONS]
        out[ind_type] = None if any(p is None for p in parts) else round(sum(parts), 2)
    return out


def describe(cells, name):
    states = collections.Counter()
    for number, flag in cells.values():
        if number is None:
            states[f"missing(:{flag or ''})"] += 1
        elif flag:
            states[f"numeric flag '{flag}'"] += 1
        else:
            states["numeric unflagged"] += 1
    geos = sorted({k[3] for k in cells})
    types = sorted({k[0] for k in cells})
    print(f"\n{name}: {len(cells)} cells, {len(geos)} geo codes, {len(types)} ind_type codes")
    print(f"  sex-specific ind_type codes: "
          f"M_* {sum(1 for t in types if t.startswith('M_'))}, "
          f"F_* {sum(1 for t in types if t.startswith('F_'))}")
    print(f"  cell states: {dict(states)}")


def main(directory):
    directory = pathlib.Path(directory)
    use_path = directory / "isoc_ai_iaiu.tsv"
    nonuse_path = directory / "isoc_ai_iaiuxr.tsv"
    for path in (use_path, nonuse_path):
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        print(f"{path.name}: {path.stat().st_size} bytes, sha256 {digest}")

    use, nonuse = load(use_path), load(nonuse_path)
    describe(use, "isoc_ai_iaiu")
    describe(nonuse, "isoc_ai_iaiuxr")

    count, worst, outliers = check_purpose_denominator(use)
    print(f"\nC1 purpose/user denominator: n={count}, max abs diff {worst:.3f} pp, "
          f"{len(outliers)} above 0.6 pp {outliers}")

    count, worst = check_internet_denominator(use)
    print(f"C3 internet-user denominator: n={count}, max abs diff {worst:.3f} pp")

    count, worst, headline, by_geo = check_nonuse_base(use, nonuse)
    print(f"C2 non-user base reconstruction: n={count}, max abs diff {worst:.3f} pp, "
          f"headline M/F max {headline:.3f} pp")
    print(f"   cells above 1 pp by geo: {dict(by_geo)}")
    print("   -> use the published PC_IND_IUAIX cells; do not reconstruct the base.")

    print(f"C4 main-reason exclusivity (EU27, % of non-user base): "
          f"{check_reason_exclusivity(nonuse)}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
