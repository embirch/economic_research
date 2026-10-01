"""Read-only adapter from paper-one results to this edition's European module.

Usage: python3 import_europe.py /path/to/gender-gap-generative-ai
Writes only coordination/europe-published-cells.json beside this script.
Does not import or execute the article's code, regenerate prose, or alter its files.
"""
import csv
from decimal import Decimal
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
COMMIT = "669b9ac0d3d6dc4c35837ee3b09df284d1442e33"
PINS = {
    "data/raw/isoc_ai_iaiu.tsv": "7f668f7be9aaefaa5662ab2ab059875de8ccbe050c5c38a8de4b2c33a96896ab",
    "outputs/tables/country_overall.csv": "7cfb9a355920032e584e0d1682267bb798906f353ca89c033c1747180a3745ae",
    "outputs/tables/purposes.csv": "ce5d6d602d9aaf4cb494819dd8fb5f0d93355c76aebfb91840cb2a02d804e334",
}
EU27 = set("AT BE BG HR CY CZ DK EE FI FR DE EL HU IE IT LV LT LU MT NL PL PT RO SK SI ES SE".split())
QUESTIONS = {"I_IUAI": "Any use", "I_IUAIPR": "Private purposes", "I_IUAIWP": "Work purposes", "I_IUAIFE": "Formal education"}


def pinned_files(repo):
    files = {}
    for name, expected in PINS.items():
        # A fixed Git object is the edition input, even if Emily later edits her checkout.
        data = subprocess.check_output(["git", "show", f"{COMMIT}:{name}"], cwd=repo)
        if hashlib.sha256(data).hexdigest() != expected:
            raise ValueError(f"Pinned article object changed: {name}")
        files[name] = data.decode("utf-8-sig")
    return files


def extract(repo):
    files = pinned_files(repo)
    official = {}
    lines = csv.reader(io.StringIO(files["data/raw/isoc_ai_iaiu.tsv"]), delimiter="\t")
    header = next(lines)
    if [s.strip() for s in header] != ["freq,ind_type,indic_is,unit,geo\\TIME_PERIOD", "2025"]:
        raise ValueError("Unexpected source dimensions/year")
    for row in lines:
        key = tuple(row[0].split(","))
        if len(key) != 5 or key in official or len(row) != 2:
            raise ValueError("Malformed or duplicate official cell")
        official[key] = row[1].strip().split()
    output = []
    seen = set()
    for name in ["outputs/tables/country_overall.csv", "outputs/tables/purposes.csv"]:
        for row in csv.DictReader(io.StringIO(files[name])):
            if row["geo"] not in EU27 | {"EU27_2020"} or row["unit"] != "PC_IND":
                continue
            if row["year"] != "2025" or row["group"] != "Y16_74" or row["eligible"] != "True":
                raise ValueError("Unexpected paper eligibility")
            key = (row["geo"], row["indicator"])
            if key in seen or key[1] not in QUESTIONS:
                raise ValueError("Duplicate/unknown displayed pair")
            seen.add(key)
            values = {}
            for sex in ["M", "F"]:
                tokens = official[("A", sex + "_Y16_74", row["indicator"], "PC_IND", row["geo"])]
                if len(tokens) != 1 or row[sex + "_flag"]:
                    raise ValueError("Flagged/unavailable cell in proposed display")
                value = Decimal(row[sex + "_rate"])
                if value != Decimal(tokens[0]) or not 0 <= value <= 100:
                    raise ValueError("Published cell and article result disagree")
                values[sex] = value
            gap = values["M"] - values["F"]
            if abs(gap - Decimal(row["gap_pp"])) > Decimal("0.000000001"):
                raise ValueError("Existing article gap does not reproduce")
            output.append({"geo": row["geo"], "geography_type": "aggregate" if row["geo"] == "EU27_2020" else "country",
                           "indicator": row["indicator"], "measure": QUESTIONS[row["indicator"]],
                           "year": 2025, "population": "All individuals aged 16–74 in survey scope",
                           "unit": "PC_IND", "male_percent": str(values["M"]), "female_percent": str(values["F"]),
                           "existing_gap_pp": str(gap), "source_table": name})
    expected = {(geo, measure) for geo in EU27 | {"EU27_2020"} for measure in QUESTIONS}
    if seen != expected:
        raise ValueError("Unexpected eligible geographic/measure coverage")
    return {"source_id": "EU_USE", "sample_family": "EU_ICT_2025", "source_repository": "embirch/gender-gap-generative-ai",
            "source_commit": COMMIT, "source_hashes": PINS, "checked": "2026-10-01",
            "source_url": "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/isoc_ai_iaiu/?format=TSV&compressed=false",
            "attribution": "Eurostat; selected published cells and existing descriptive differences from Emily Birch's European paper.",
            "limits": "National fieldwork and instruments differ. No sampling intervals supplied for these displayed cells; gap precision unverified. The EU aggregate is not a country. Work-purpose use is among all individuals, not just workers. Purposes overlap. No welfare or causal interpretation.",
            "rows": output}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    result = extract(Path(sys.argv[1]))
    (HERE / "europe-published-cells.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(f"PASS: {len(result['rows'])} existing pairs match pinned official values and paper gaps; article repository read-only.")
