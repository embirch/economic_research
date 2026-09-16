#!/usr/bin/env python3
"""Fetch every file of Anthropic/EconomicIndex release_2025_09_15 into data/cache/.

Convention: data/fetch/README.md. File list and byte sizes: data/releases/INDEX.md
(HF tree API, revision 2ea58ff75e4247d26810c37f10c179edc2466cac).

Run from the repository root:  python data/fetch/release_2025_09_15.py
Downloads are write-once; raw files are never modified. Parquet siblings are derived
and gitignored.
"""

from __future__ import annotations

import hashlib
import sys
import urllib.parse
import urllib.request
from pathlib import Path

RELEASE = "release_2025_09_15"
BASE = "https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/main"
CACHE = Path("data/cache") / RELEASE
PARQUET_MIN_BYTES = 20 * 1024 * 1024

# (relative path within the release folder, byte size from data/releases/INDEX.md)
FILES: list[tuple[str, int]] = [
    ("README.md", 2640),
    ("code/aei_analysis_functions_1p_api.py", 76365),
    ("code/aei_analysis_functions_claude_ai.py", 92526),
    ("code/aei_report_v3_analysis_1p_api.ipynb", 8079),
    ("code/aei_report_v3_analysis_claude_ai.ipynb", 22150),
    ("code/aei_report_v3_change_over_time_claude_ai.py", 18565),
    ("code/aei_report_v3_preprocessing_claude_ai.ipynb", 85914),
    ("code/preprocess_gdp.py", 11748),
    ("code/preprocess_iso_codes.py", 3226),
    ("code/preprocess_onet.py", 5279),
    ("code/preprocess_population.py", 13542),
    ("data/input/BTOS_National.xlsx", 63052),
    ("data/input/Population by single age _20250903072924.csv", 2176),
    ("data/input/automation_vs_augmentation_v1.csv", 197),
    ("data/input/automation_vs_augmentation_v2.csv", 198),
    ("data/input/bea_us_state_gdp_2024.csv", 1663),
    ("data/input/census_state_codes.txt", 1485),
    ("data/input/geonames_countryInfo.txt", 31667),
    ("data/input/imf_gdp_raw_2024.json", 265358),
    ("data/input/onet_task_statements_raw.xlsx", 1204658),
    ("data/input/sc-est2024-agesex-civ.csv", 818707),
    ("data/input/soc_structure_raw.csv", 77176),
    ("data/input/task_pct_v1.csv", 461306),
    ("data/input/task_pct_v2.csv", 435372),
    ("data/input/working_age_pop_2024_country_raw.csv", 22974),
    ("data/intermediate/aei_raw_1p_api_2025-08-04_to_2025-08-11.csv", 7027019),
    ("data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv", 18894517),
    ("data/intermediate/gdp_2024_country.csv", 4115),
    ("data/intermediate/gdp_2024_us_state.csv", 2179),
    ("data/intermediate/iso_country_codes.csv", 4564),
    ("data/intermediate/onet_task_statements.csv", 3650862),
    ("data/intermediate/soc_structure.csv", 78834),
    ("data/intermediate/working_age_pop_2024_country.csv", 6321),
    ("data/intermediate/working_age_pop_2024_us_state.csv", 1079),
    ("data/output/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv", 26840881),
    ("data/output/request_hierarchy_tree_1p_api.json", 302699),
    ("data/output/request_hierarchy_tree_claude_ai.json", 438531),
    ("data_documentation.md", 20133),
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_checksums() -> dict[str, str]:
    f = CACHE / "CHECKSUMS.txt"
    if not f.exists():
        return {}
    out = {}
    for line in f.read_text().splitlines():
        if line.strip():
            digest, rel = line.split("  ", 1)
            out[rel] = digest
    return out


def download(rel: str, dest: Path) -> None:
    url = f"{BASE}/{RELEASE}/{urllib.parse.quote(rel)}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    with urllib.request.urlopen(url, timeout=300) as resp, tmp.open("wb") as fh:
        while chunk := resp.read(1 << 20):
            fh.write(chunk)
    tmp.replace(dest)


def to_parquet(csv_path: Path) -> bool:
    """Convert a raw CSV to a Parquet sibling. Returns True if written."""
    import pandas as pd

    pq = csv_path.with_suffix(".parquet")
    if pq.exists() and pq.stat().st_mtime >= csv_path.stat().st_mtime:
        return False
    # keep_default_na=False: 'NA' is Namibia, not a missing value.
    df = pd.read_csv(csv_path, keep_default_na=False, dtype=str)
    if "value" in df.columns:
        df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df.to_parquet(pq, index=False)
    return True


def main() -> int:
    if not Path("data/releases/INDEX.md").exists():
        print("run from the repository root", file=sys.stderr)
        return 2
    CACHE.mkdir(parents=True, exist_ok=True)
    known = read_checksums()

    fetched = skipped = 0
    bytes_total = 0
    size_mismatch: list[str] = []
    hash_mismatch: list[str] = []
    digests: dict[str, str] = {}

    for rel, expect_bytes in FILES:
        dest = CACHE / rel
        if dest.exists() and rel in known and sha256(dest) == known[rel]:
            skipped += 1
            digests[rel] = known[rel]
        else:
            if dest.exists() and rel in known:
                hash_mismatch.append(rel)
            download(rel, dest)
            fetched += 1
            digests[rel] = sha256(dest)
        got = dest.stat().st_size
        bytes_total += got
        if got != expect_bytes:
            size_mismatch.append(f"{rel}: INDEX.md {expect_bytes}, on disk {got}")

    (CACHE / "CHECKSUMS.txt").write_text(
        "".join(f"{digests[rel]}  {rel}\n" for rel, _ in sorted(FILES))
    )

    converted = []
    for rel, _ in FILES:
        p = CACHE / rel
        if p.suffix.lower() in (".csv", ".tsv") and p.stat().st_size > PARQUET_MIN_BYTES:
            if to_parquet(p):
                converted.append(p.with_suffix(".parquet").name)

    print(f"{RELEASE}: {len(FILES)} files, {bytes_total:,} bytes")
    print(f"  fetched {fetched}, skipped (hash matched) {skipped}")
    print(f"  checksums -> {CACHE / 'CHECKSUMS.txt'}")
    print(f"  parquet written: {converted if converted else 'none (all up to date)'}")
    if hash_mismatch:
        print(f"  RE-DOWNLOADED after checksum mismatch: {hash_mismatch}")
    if size_mismatch:
        print("  SIZE MISMATCH vs data/releases/INDEX.md:")
        for m in size_mismatch:
            print(f"    {m}")
        return 1
    print("  all byte sizes match data/releases/INDEX.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
