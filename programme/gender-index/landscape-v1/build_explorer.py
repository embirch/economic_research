"""Validate reviewed edition inputs and build a standalone, offline explorer."""
import csv
from decimal import Decimal
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent


def attach_corpus(data):
    """Join every numbered HBS entry without turning entries into independent samples."""
    with (ROOT.parent / "evidence/hbs-corpus.csv").open(newline="") as handle:
        entries = list(csv.DictReader(handle))
    numbers = [int(row["hbs_entry"]) for row in entries]
    if sorted(numbers) != list(range(1, 77)):
        raise ValueError("HBS corpus must contain each May 2026 entry 1–76 exactly once")
    with (ROOT.parent / "evidence/source-register.csv").open(newline="") as handle:
        atlas_rows = list(csv.DictReader(handle))
    with (ROOT.parent / "evidence/literature.csv").open(newline="") as handle:
        literature_rows = list(csv.DictReader(handle))
    atlas = {row["indicator_id"]: row for row in atlas_rows}
    literature = {row["study_id"]: row for row in literature_rows}
    sources = {row["id"]: row for row in data["sources"]}
    if len(atlas) != len(atlas_rows) or len(literature) != len(literature_rows):
        raise ValueError("Duplicate register IDs")
    if set(atlas) != set(sources):
        raise ValueError("Source atlas and explorer have different coverage")
    for source in sources.values():
        source["hbs_entries"] = []
        source["hbs_roles"] = []
        source["hbs_mapping_notes"] = []
    for row in entries:
        n = int(row["hbs_entry"])
        expected = "Plotted adoption entry" if n <= 58 else "Narrative entry"
        if row["hbs_role"] != expected:
            raise ValueError(f"Incorrect review role for HBS entry {n}")
        if row["source_id"] not in sources or row["literature_id"] not in literature:
            raise ValueError(f"Unlinked HBS entry {n}")
        if not all(row[k].strip() for k in ["disposition", "relationship_note", "primary_check_status", "metadata_basis"]):
            raise ValueError(f"Missing review boundary for HBS entry {n}")
        for linked in filter(None, row["related_existing_ids"].split("|")):
            if linked not in atlas and linked not in literature:
                raise ValueError(f"Unknown related programme ID: {linked}")
        for linked in filter(None, row["related_hbs_entries"].split("|")):
            if int(linked) not in numbers:
                raise ValueError(f"Unknown related HBS entry: {linked}")
        if atlas[row["source_id"]]["sample_family"] != row["sample_family"]:
            raise ValueError(f"Inconsistent sample-family mapping for HBS entry {n}")
        if literature[row["literature_id"]]["sample_family"] != row["sample_family"]:
            raise ValueError(f"Inconsistent literature family for HBS entry {n}")
        validate_link(row["hbs_url"])
        source = sources[row["source_id"]]
        source["hbs_entries"].append(n)
        source["hbs_mapping_notes"].append(f"Entry {n}: {row['disposition']}. {row['relationship_note']}")
        if expected not in source["hbs_roles"]:
            source["hbs_roles"].append(expected)
    for source in sources.values():
        source["hbs_entry_ids"] = "|".join(str(n) for n in source["hbs_entries"])
        source["hbs_role_labels"] = "|".join(source["hbs_roles"])
        source["hbs_mapping"] = " ".join(source.pop("hbs_mapping_notes"))
    by_number = {int(row["hbs_entry"]): row for row in entries}
    if by_number[8]["source_id"] != by_number[56]["source_id"]:
        raise ValueError("Entries 8 and 56 must retain their shared publication")
    if by_number[63]["sample_family"] != by_number[75]["sample_family"]:
        raise ValueError("Nature survey publications must retain their shared sample lineage")
    data["corpus"] = {
        "entries": len(entries), "plotted": 58, "narrative": 18,
        "mapped_cards": len({row["source_id"] for row in entries}),
        "citation_records": len({row["literature_id"] for row in entries}),
        "other_cards": sum(not source["hbs_entries"] for source in sources.values()),
    }
    if data["counters"][2]["value"] != str(len(sources)):
        raise ValueError("Headline catalogue count is stale")


def validate_link(value, local_ok=False):
    url = urlparse(value)
    if url.scheme in {"https", "http"} and url.netloc:
        return
    if local_ok and not url.scheme and not url.netloc:
        if not url.path or (ROOT / url.path).is_file():
            return
    raise ValueError(f"Invalid or missing linked resource: {value}")


def validate(data):
    sources = data["sources"]
    ids = [s["id"] for s in sources]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate source IDs")
    with (ROOT.parent / "evidence/indicators.csv").open(newline="") as handle:
        starter = {r["indicator_id"] for r in csv.DictReader(handle)}
    if not starter <= set(ids):
        raise ValueError(f"Starter candidates missing from edition: {starter - set(ids)}")
    required = ["title", "geography", "period", "construct", "status", "use", "family",
                "population", "gender", "definition", "uncertainty", "access", "limit", "url", "verification"]
    for source in sources:
        if any(not isinstance(source.get(k), str) or not source[k].strip() for k in required):
            raise ValueError(f"Incomplete source card: {source['id']}")
        if not source["regions"] or not source["topics"]:
            raise ValueError("Missing filter tags")
        validate_link(source["url"])
    for module in data["modules"]:
        if module["source_id"] not in ids or any(len(r) != len(module["columns"]) for r in module["rows"]):
            raise ValueError("Invalid module provenance or row width")
        source = next(s for s in sources if s["id"] == module["source_id"])
        if source["status"].startswith("Review-derived"):
            raise ValueError("Review-derived metadata cannot supply a numerical panel")
        validate_link(module["url"])
    for item in data["findings"] + data["questions"]:
        for link in item["links"]:
            validate_link(link["url"], local_ok=True)
    eu = data["europe"]
    pinned = json.loads((ROOT / "coordination/europe-published-cells.json").read_text())
    if eu != pinned or len(eu["rows"]) != 112:
        raise ValueError("European display differs from verified adapter output")
    for row in eu["rows"]:
        if Decimal(row["male_percent"]) - Decimal(row["female_percent"]) != Decimal(row["existing_gap_pp"]):
            raise ValueError("European difference mismatch")
    uk = next(m for m in data["modules"] if m["source_id"] == "UK_DSIT_USE")
    cells = json.loads((ROOT / "coordination/dsit-published-cells.json").read_text())["rows"]
    expected = [[r["source_label"], r["published_percent"] + "%", f"{r['unweighted_base']:,}"]
                for r in cells if r["source_label"] != "TOTAL"]
    if uk["rows"] != expected:
        raise ValueError("UK display differs from the pinned published cells")
    published = json.loads((ROOT / "coordination/published-table-checks.json").read_text())
    by_source = {m["source_id"]: m for m in data["modules"]}
    expected_us = [[k, f"{v}%"] for k, v in published["pew_ever_chatbot_use"]["percent"].items()]
    if by_source["PEW_GENDER"]["rows"] != expected_us:
        raise ValueError("US display differs from the checked primary table")
    brazil = json.loads((ROOT.parent / "evidence/v1-audit-2026-10-01/checks/cetic-published-cells.json").read_text())
    br = brazil["tables"]["M1"]["measures"]
    expected_br = [[label, f"{br['proportion']['sex_rows'][sex][0]:.2f}",
                    f"±{br['margin_of_error']['sex_rows'][sex][0]:.2f}"]
                   for label, sex in [("Masculino", "Male"), ("Feminino", "Female")]]
    if by_source["BR_CETIC_USE"]["rows"] != expected_br:
        raise ValueError("Brazil display differs from the checked primary table")
    if by_source["CA_CSWC_WORK"]["rows"] != [["Women", "22%"], ["Men", "22%"]]:
        raise ValueError("Canada display differs from the independently read narrative")
    if any("Review pending" in json.dumps(s) for s in sources):
        raise ValueError("Unreviewed placeholder source cards remain")
    return len(sources)


def main():
    data = json.loads((ROOT / "edition-data.json").read_text())
    attach_corpus(data)
    count = validate(data)
    template = (ROOT / "explorer.template.html").read_text()
    if template.count("__EDITION_DATA__") != 1:
        raise ValueError("Expected one data placeholder")
    embedded = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c").replace("&", "\\u0026")
    result = template.replace("__EDITION_DATA__", embedded)
    (ROOT / "index.html").write_text(result)
    with (ROOT / "source-cards.csv").open("w", newline="") as handle:
        fields = ["id", "title", "geography", "period", "construct", "status", "use", "family",
                  "population", "gender", "definition", "uncertainty", "access", "limit", "url", "verification",
                  "hbs_entry_ids", "hbs_role_labels", "hbs_mapping"]
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(data["sources"])
    files = ["edition-data.json", "explorer.template.html", "index.html", "source-cards.csv",
             "coordination/europe-published-cells.json", "coordination/dsit-published-cells.json",
             "coordination/published-table-checks.json", "../evidence/source-register.csv",
             "../evidence/hbs-corpus.csv", "../evidence/literature.csv",
             "../evidence/v1-audit-2026-10-01/checks/cetic-published-cells.json"]
    manifest = {f: hashlib.sha256((ROOT / f).read_bytes()).hexdigest() for f in files}
    (ROOT / "build-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"PASS: {count} catalogue cards; all 76 HBS entries linked; 112 European pairs and four national panels match reviewed inputs; offline HTML built.")


if __name__ == "__main__":
    main()
