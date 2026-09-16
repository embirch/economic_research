#!/usr/bin/env python3
"""Fetch every file of release_2026_01_15/ from the Hugging Face dataset
Anthropic/EconomicIndex into data/cache/release_2026_01_15/.

Convention: data/fetch/README.md. File list and byte sizes: data/releases/INDEX.md
(revision 2ea58ff75e4247d26810c37f10c179edc2466cac).

Run from the repository root:  python data/fetch/release_2026_01_15.py
Raw files are write-once; the .parquet siblings are derived and gitignored.
"""

from __future__ import annotations

import hashlib
import sys
import urllib.request
from pathlib import Path

RELEASE = "release_2026_01_15"
BASE = "https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/main"
CACHE = Path("data/cache") / RELEASE

# (path inside the release folder, bytes from data/releases/INDEX.md)
FILES = [
    ("aei_v4_appendix.pdf", 6_036_245),
    ("data/intermediate/aei_raw_1p_api_2025-11-13_to_2025-11-20.csv", 41_518_256),
    ("data/intermediate/aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv", 94_086_309),
    ("data_documentation.md", 18_721),
]

PARQUET_MIN_BYTES = 20 * 1024 * 1024

# Schema of both raw CSVs, verified in data/releases/release_2026_01_15.md.
# Every column is read; `value` is the only numeric one.
CSV_COLUMNS = [
    "geo_id",
    "geography",
    "date_start",
    "date_end",
    "platform_and_product",
    "facet",
    "level",
    "variable",
    "cluster_name",
    "value",
]
CSV_DTYPES = {c: "string" for c in CSV_COLUMNS if c != "value"}
CSV_DTYPES["value"] = "float64"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def download(rel_path: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    url = f"{BASE}/{RELEASE}/{rel_path}"
    with urllib.request.urlopen(url) as resp, tmp.open("wb") as out:
        while True:
            chunk = resp.read(1 << 20)
            if not chunk:
                break
            out.write(chunk)
    tmp.replace(dest)


def read_checksums() -> dict[str, str]:
    f = CACHE / "CHECKSUMS.txt"
    if not f.exists():
        return {}
    out = {}
    for line in f.read_text().splitlines():
        if line.strip():
            digest, path = line.split("  ", 1)
            out[path] = digest
    return out


def main() -> int:
    if not Path("data/fetch/README.md").exists():
        print("run from the repository root", file=sys.stderr)
        return 2

    CACHE.mkdir(parents=True, exist_ok=True)
    known = read_checksums()
    digests: dict[str, str] = {}
    fetched = skipped = 0
    total_bytes = 0
    problems: list[str] = []

    for rel_path, expected_bytes in FILES:
        dest = CACHE / rel_path
        if dest.exists() and rel_path in known and sha256(dest) == known[rel_path]:
            digests[rel_path] = known[rel_path]
            skipped += 1
        else:
            if dest.exists() and rel_path in known:
                problems.append(f"CHECKSUM MISMATCH on cached {rel_path}: re-downloading")
            download(rel_path, dest)
            digests[rel_path] = sha256(dest)
            fetched += 1
        size = dest.stat().st_size
        total_bytes += size
        if size != expected_bytes:
            problems.append(f"SIZE MISMATCH {rel_path}: {size} on disk, {expected_bytes} in INDEX.md")

    lines = [f"{digests[p]}  {p}" for p, _ in sorted(FILES)]
    (CACHE / "CHECKSUMS.txt").write_text("\n".join(lines) + "\n")

    converted = 0
    for rel_path, _ in FILES:
        if not rel_path.endswith((".csv", ".tsv")):
            continue
        src = CACHE / rel_path
        if src.stat().st_size <= PARQUET_MIN_BYTES:
            continue
        dst = src.with_suffix(".parquet")
        if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime:
            continue
        import pandas as pd

        header = pd.read_csv(src, nrows=0, sep="\t" if rel_path.endswith(".tsv") else ",").columns.tolist()
        if header != CSV_COLUMNS:
            problems.append(f"UNEXPECTED SCHEMA {rel_path}: {header}")
            usecols, dtypes = header, None
        else:
            usecols, dtypes = CSV_COLUMNS, CSV_DTYPES
        df = pd.read_csv(
            src,
            usecols=usecols,
            dtype=dtypes,
            keep_default_na=False,  # NA is Namibia
            # empty cluster_name is meaningful (facet-level aggregate row), so it stays "";
            # only `value` may be missing, and in this release never is.
            na_values={"value": [""]},
            sep="\t" if rel_path.endswith(".tsv") else ",",
        )
        df.to_parquet(dst, index=False)
        converted += 1

    print(f"{RELEASE}: fetched {fetched}, skipped {skipped}, {total_bytes:,} bytes in {CACHE}")
    print(f"  CHECKSUMS.txt: {len(digests)} entries; parquet written: {converted}")
    if problems:
        for p in problems:
            print("  " + p, file=sys.stderr)
        return 1
    print("  all sizes match data/releases/INDEX.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
