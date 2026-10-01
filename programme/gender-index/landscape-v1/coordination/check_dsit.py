"""Read selected published DSIT cells from a pinned ODS; no derived gap estimates.

Usage: python3 check_dsit.py /path/to/dsit-ai-2025-2026.ods
The public aggregate workbook stays outside Git. Standard library only.
"""
import hashlib
import json
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
import zipfile

SHA256 = "a34ed705b6f8c2966d82586917befaae975fee8f61206ef3a2d679cc95c4610a"
SOURCE = "https://assets.publishing.service.gov.uk/media/6a58999031fb6daf314137c5/DSIT_Public_Engagement_Survey_2025_2026_artificial_intelligence_tables.ods"
NS = {"t": "urn:oasis:names:tc:opendocument:xmlns:table:1.0",
      "x": "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
      "o": "urn:oasis:names:tc:opendocument:xmlns:office:1.0"}


def read_cells(path, wanted):
    """Expand ODS repeated rows/columns only within the selected small ranges."""
    with zipfile.ZipFile(path) as archive:
        root = ET.fromstring(archive.read("content.xml"))
    found = {}
    for sheet in root.findall(".//t:table", NS):
        name = sheet.get(f"{{{NS['t']}}}name")
        if name not in wanted:
            continue
        cells = {}
        row_number = 1
        for row in sheet.findall("t:table-row", NS):
            repeat_rows = int(row.get(f"{{{NS['t']}}}number-rows-repeated", "1"))
            column_number = 1
            for cell in row:
                if cell.tag not in [f"{{{NS['t']}}}table-cell", f"{{{NS['t']}}}covered-table-cell"]:
                    continue
                repeat_cols = int(cell.get(f"{{{NS['t']}}}number-columns-repeated", "1"))
                for target_row, target_col in wanted[name]:
                    if (row_number <= target_row < row_number + repeat_rows
                            and column_number <= target_col < column_number + repeat_cols):
                        display = " ".join("".join(p.itertext()) for p in cell.findall("x:p", NS))
                        cells[(target_row, target_col)] = display
                column_number += repeat_cols
            row_number += repeat_rows
            if row_number > max(r for r, _ in wanted[name]):
                break
        missing = wanted[name] - cells.keys()
        if missing:
            raise ValueError(f"Missing cells: {name} {sorted(missing)}")
        found[name] = cells
    if set(found) != set(wanted):
        raise ValueError("Required sheet missing")
    return found


def extract(path):
    actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual_hash != SHA256:
        raise ValueError("Source hash changed; audit the new vintage before extracting")
    labels = {6: "TOTAL", 38: "Male", 39: "Female", 40: "Identify in another way", 41: "Prefer not to say"}
    wanted = {"Table_E5": {(r, c) for r in labels for c in (1, 2, 3, 5, 6)}}
    wanted["Table_E5"].update({(1, 1), (5, 3), (5, 5), (5, 6)})
    cells = read_cells(path, wanted)["Table_E5"]
    if "base: all adults" not in cells[(1, 1)]:
        raise ValueError("Unexpected table population")
    for col, title in [(3, "Generative AI user"), (5, "Unweighted base"), (6, "Weighted base")]:
        if cells[(5, col)] != title:
            raise ValueError(f"Unexpected header at column {col}")
    rows = []
    for row, label in labels.items():
        if cells[(row, 2)] != label or cells[(row, 1)] != ("TOTAL" if row == 6 else "Gender"):
            raise ValueError(f"Unexpected subgroup at row {row}")
        percentage = cells[(row, 3)]
        if not 0 <= float(percentage) <= 100:
            raise ValueError("Percentage outside range")
        rows.append({"source_label": label, "source_cells": f"Table_E5!B{row}:F{row}",
                     "published_percent": percentage,
                     "unweighted_base": int(cells[(row, 5)].replace(",", "")),
                     "displayed_weighted_base": cells[(row, 6)]})
    return {"source_id": "UK_DSIT_USE", "sample_family": "UK_DSIT_PES_2025_2026",
            "retrieved": "2026-10-01", "source_url": SOURCE, "source_sha256": actual_hash,
            "source_bytes": path.stat().st_size, "sheet": "Table_E5", "rows": rows,
            "status": "published cells reproduced; not a harmonised international indicator",
            "notes": "Provider display precision retained. No gaps, confidence intervals or significance tests calculated."}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    print(json.dumps(extract(Path(sys.argv[1])), indent=2, ensure_ascii=False))
