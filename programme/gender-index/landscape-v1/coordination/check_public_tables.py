"""Reproduce selected table cells from locally saved primary HTML pages.

Usage: python3 check_public_tables.py /path/to/snapshot-directory
Public pages are saved outside Git; source hashes and selected aggregates are retained.
"""
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import sys

PINS = {
    "canada-cswc": ("fd0612e4e13b928faf260d23d4181bce5919c196585abc401bd74fda83acaded", "https://www150.statcan.gc.ca/n1/pub/75-006-x/2026001/article/00007-eng.htm"),
    "pew-gender": ("45f21a74d464d9927a54fc17576b255160a1f8c033e27fb155e3c1e738d88a41", "https://www.pewresearch.org/internet/2026/06/17/the-gender-gap-in-ai/"),
    "brazil-m1": ("7eb17e218305e4a84e95574433c8b12d15f418ce6e2d682202abdbb5492152ed", "https://www.cetic.br/pt/tics/domicilios/2025/individuos/M1/"),
}


class Tables(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tables, self.table, self.row, self.cell = [], None, None, None

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            if self.table is not None:
                raise ValueError("Nested table requires a new parser audit")
            self.table = []
        if self.table is not None and tag == "tr":
            self.row = []
        if self.row is not None and tag in ["td", "th"]:
            self.cell = []

    def handle_data(self, text):
        if self.cell is not None:
            self.cell.append(text)

    def handle_endtag(self, tag):
        if tag in ["td", "th"] and self.cell is not None:
            self.row.append(" ".join("".join(self.cell).split()))
            self.cell = None
        if tag == "tr" and self.row is not None:
            self.table.append(self.row)
            self.row = None
        if tag == "table" and self.table is not None:
            self.tables.append(self.table)
            self.table = None


def extract(directory):
    tables, sources = {}, {}
    for name, (expected, url) in PINS.items():
        raw = (directory / (name + ".html")).read_bytes()
        actual = hashlib.sha256(raw).hexdigest()
        if actual != expected:
            raise ValueError(f"Page vintage changed: {name}; re-audit before accepting")
        parser = Tables()
        parser.feed(raw.decode("utf-8"))
        tables[name] = parser.tables
        sources[name] = {"url": url, "sha256": actual, "bytes": len(raw), "checked": "2026-10-01"}
    pew = [r for r in tables["pew-gender"][0] if r and r[0] == "2026"]
    if pew != [["2026", "49", "50", "47"]]:
        raise ValueError("Pew headline row differs from independently read published table")
    br = tables["brazil-m1"][0]
    male = [r for r in br if "Masculino" in r]
    female = [r for r in br if "Feminino" in r]
    if male != [["SEXO", "Masculino", "35", "64", "1", "0"]] or female != [["Feminino", "30", "69", "1", "0"]]:
        raise ValueError("Brazil sex rows differ from the published table")
    ca = [r for r in tables["canada-cswc"][7] if r and r[0] in ["Female+ (ref.)", "Male+"]]
    if ca != [["Female+ (ref.)", "1.00", "... not applicable", "... not applicable"], ["Male+", "1.15 Table A.1 Note *", "1.02", "1.29"]]:
        raise ValueError("Canadian model row differs from the published table")
    return {"sources": sources,
            "pew_ever_chatbot_use": {"table": "Men, women are now equally likely to say they use chatbots; 2026 row",
                "population": "US noninstitutionalised adults 18+", "fieldwork": "2026-02-17 to 2026-02-23",
                "denominator": "all adults of each reported category", "percent": {"Men": 50, "Women": 47},
                "limits": "Ever use; not past-three-month prevalence. Pew describes the shares as similar; not proof of exact equality. No new significance test here."},
            "brazil_m1_use": {"table": "M1; SEXO rows; Sim column", "percent": {"Masculino": 35, "Feminino": 30},
                "denominator": "internet users", "limits": "Provider's rounded published cells; questionnaire/reference-window and precision checks required before integration."},
            "canada_adjusted_model": {"table": "Table A.1; Gender", "reference": "Female+", "comparison": "Male+",
                "odds_ratio": "1.15", "ci95_lower": "1.02", "ci95_upper": "1.29",
                "limits": "Adjusted association, not a probability difference or causal effect. Plus labels include redistributed nonbinary respondents for confidentiality. Crude percentages of 22/22 are from narrative, not this model."}}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    data = extract(Path(sys.argv[1]))
    output = Path(__file__).with_name("published-table-checks.json")
    output.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print("PASS: Brazil and Pew percentages and Canadian model cells match independent primary-page checks.")
