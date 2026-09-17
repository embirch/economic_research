#!/usr/bin/env python3
"""Fetch the BLS Employment Projections occupation table (post1 cut C7).

Convention: data/fetch/README.md. Profile: data/ATLAS.md (`## Supplementary sources`,
and log (h) 8 for the merge audit against the O*NET task file).

One file: the 2024-34 Employment Projections "Occupational Projections and Worker
Characteristics" table served as a single HTML page at
`https://data.bls.gov/projections/occupationProj`. It supplies `Median Annual Wage 2025`
(post1's second wage source) and `Employment 2025` (the employment weights of the
multi-holder wage rule). OEWS, Anthropic's own wage source, is unobtainable from this
sandbox: `www.bls.gov` and `download.bls.gov` both return 403.

Unlike the Hugging Face folders this is a live page, not a pinned artefact: BLS may
re-render or re-publish it. The script therefore pins the sha256 observed on 2026-09-17
and **warns** rather than failing when the bytes differ, but it does **fail** if the
parsed table stops carrying the two columns and the 831 detailed-SOC rows the C7 audit
is built on. US Government work, public domain; attribute BLS.

Run from the repository root:  python data/fetch/supplementary_bls_ep.py
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import pandas as pd
import requests

CACHE = Path("data/cache/supplementary/bls_employment_projections")
URL = "https://data.bls.gov/projections/occupationProj"
NAME = "occupationProj.html"

# observed 2026-09-17; the page is live, so a change is reported, not fatal
SHA256 = "bbde16e0457b9b93662b17d5ccb3e9bec66929a175c1770c21f381d57765e795"
BYTES = 1397448

# what the C7 audit depends on (data/ATLAS.md log (h) 8)
DETAILED_SOC_ROWS = 831
REQUIRED_COLUMNS = ("Occupation Code", "Median Annual Wage 2025", "Employment 2025")


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    if not Path("data/fetch/README.md").exists():
        raise SystemExit("run from the repository root")

    dest = CACHE / NAME
    if dest.exists() and sha256_of(dest) == SHA256:
        fetched = "skipped (hash matched)"
    else:
        CACHE.mkdir(parents=True, exist_ok=True)
        resp = requests.get(URL, timeout=300)
        print(f"  HTTP {resp.status_code}")
        resp.raise_for_status()
        tmp = dest.with_suffix(".part")
        tmp.write_bytes(resp.content)
        tmp.replace(dest)
        fetched = "fetched"

    got, size = sha256_of(dest), dest.stat().st_size
    (CACHE / "CHECKSUMS.txt").write_text(f"{got}  {NAME}\n")

    table = max(pd.read_html(dest), key=len)
    table.columns = [c[0] if isinstance(c, tuple) else c for c in table.columns]
    table = table.loc[:, ~table.columns.duplicated()]
    missing = [c for c in REQUIRED_COLUMNS if c not in table.columns]
    code = table["Occupation Code"].astype(str).str.strip() if not missing else pd.Series(dtype=str)
    detailed = int(code.str.match(r"^\d\d-\d{4}$").sum())

    print(f"bls_employment_projections: {fetched}, {size:,} bytes in {CACHE}")
    print(f"  detailed-SOC rows {detailed} ; columns present: {not missing}")
    if got != SHA256 or size != BYTES:
        print("  NOTE: the page differs from the 2026-09-17 pin (it is live, not archived):")
        print(f"    sha256 {got} (pinned {SHA256}); {size:,} bytes (pinned {BYTES:,})")
    if missing:
        print(f"  FAIL: missing columns {missing}")
        return 1
    if detailed != DETAILED_SOC_ROWS:
        print(f"  FAIL: {detailed} detailed-SOC rows, expected {DETAILED_SOC_ROWS}")
        return 1
    print("  structure matches the C7 audit (data/ATLAS.md log (h) 8)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
