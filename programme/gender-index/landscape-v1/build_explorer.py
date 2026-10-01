"""Validate reviewed edition inputs and build a standalone, offline explorer."""
import csv
from decimal import Decimal
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent


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
                "population", "gender", "definition", "uncertainty", "access", "limit", "url"]
    for source in sources:
        if any(not isinstance(source.get(k), str) or not source[k].strip() for k in required):
            raise ValueError(f"Incomplete source card: {source['id']}")
        if not source["regions"] or not source["topics"]:
            raise ValueError("Missing filter tags")
        url = urlparse(source["url"])
        if url.scheme not in {"https", "http"} or not url.netloc:
            raise ValueError("Invalid source URL")
    for module in data["modules"]:
        if module["source_id"] not in ids or any(len(r) != len(module["columns"]) for r in module["rows"]):
            raise ValueError("Invalid module provenance or row width")
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
    return len(sources)


def main():
    data = json.loads((ROOT / "edition-data.json").read_text())
    count = validate(data)
    template = (ROOT / "explorer.template.html").read_text()
    if template.count("__EDITION_DATA__") != 1:
        raise ValueError("Expected one data placeholder")
    embedded = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c").replace("&", "\\u0026")
    result = template.replace("__EDITION_DATA__", embedded)
    (ROOT / "index.html").write_text(result)
    files = ["edition-data.json", "explorer.template.html", "index.html",
             "coordination/europe-published-cells.json", "coordination/dsit-published-cells.json"]
    manifest = {f: hashlib.sha256((ROOT / f).read_bytes()).hexdigest() for f in files}
    (ROOT / "build-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"PASS: {count} complete source cards; 112 European pairs and UK display match checked inputs; offline HTML built.")


if __name__ == "__main__":
    main()
