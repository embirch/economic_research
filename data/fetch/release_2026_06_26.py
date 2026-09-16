#!/usr/bin/env python3
"""Fetch release_2026_06_26 of Anthropic/EconomicIndex into data/cache/release_2026_06_26/.

Convention: data/fetch/README.md. File list and byte sizes: data/releases/INDEX.md
(revision 2ea58ff75e4247d26810c37f10c179edc2466cac).

Run from the repository root:  python data/fetch/release_2026_06_26.py

Downloads are write-once; raw files are never modified. Parquet siblings are derived
and gitignored. CSVs over 20 MB are converted with keep_default_na=False ("NA" is
Namibia) and explicit dtypes for the wide schema.
"""

from __future__ import annotations

import hashlib
import os
import sys
import urllib.request
from pathlib import Path

RELEASE = "release_2026_06_26"
BASE = "https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/main"
REVISION = "2ea58ff75e4247d26810c37f10c179edc2466cac"

# (path inside the release folder, expected bytes from data/releases/INDEX.md)
FILES: list[tuple[str, int]] = [
    ("data_documentation.md", 7_397),
    ("data/aei_1p_api_2026-06-26.csv", 77_282_477),
    ("data/aei_claude_ai_2026-06-26.csv", 219_174_671),
]

PARQUET_MIN_BYTES = 20 * 1024 * 1024

# Wide schema of both CSVs of this release (verified: see data/releases/release_2026_06_26.md).
WIDE_DTYPES = {
    "date_start": "string",
    "date_end": "string",
    "geo_id": "string",
    "geo_level": "string",
    "category_name": "string",
    "hierarchy_level": "string",
    "metric_id": "string",
    "value": "float64",
    "node_name": "string",
    "node_external_id": "string",
}

CACHE = Path("data/cache") / RELEASE
CHECKSUMS = CACHE / "CHECKSUMS.txt"


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_checksums() -> dict[str, str]:
    known: dict[str, str] = {}
    if CHECKSUMS.exists():
        for line in CHECKSUMS.read_text().splitlines():
            if not line.strip():
                continue
            digest, rel = line.split(maxsplit=1)
            known[rel.strip()] = digest
    return known


def download(rel: str, dest: Path) -> None:
    url = f"{BASE}/{RELEASE}/{rel}"
    tmp = dest.with_suffix(dest.suffix + ".part")
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "economic_research/data-steward"})
    with urllib.request.urlopen(req) as resp, tmp.open("wb") as out:
        commit = resp.headers.get("x-repo-commit")
        if commit and commit != REVISION:
            print(f"  ! {rel}: served revision {commit}, expected {REVISION}")
        while True:
            chunk = resp.read(1 << 22)
            if not chunk:
                break
            out.write(chunk)
    os.replace(tmp, dest)


def to_parquet(csv_path: Path) -> str:
    import pandas as pd

    pq_path = csv_path.with_suffix(".parquet")
    if pq_path.exists() and pq_path.stat().st_mtime >= csv_path.stat().st_mtime:
        return "parquet up to date"
    header = pd.read_csv(csv_path, nrows=0, keep_default_na=False).columns.tolist()
    dtypes = {c: WIDE_DTYPES[c] for c in header if c in WIDE_DTYPES}
    unknown = [c for c in header if c not in WIDE_DTYPES]
    if unknown:
        print(f"  ! {csv_path.name}: columns not in the known wide schema: {unknown}")
    df = pd.read_csv(csv_path, keep_default_na=False, dtype=dtypes, usecols=header)
    df.to_parquet(pq_path, index=False, compression="zstd")
    return f"parquet written ({pq_path.stat().st_size:,} bytes, {len(df):,} rows)"


def main() -> int:
    if not Path("data/fetch/README.md").exists():
        print("run from the repository root", file=sys.stderr)
        return 2

    CACHE.mkdir(parents=True, exist_ok=True)
    known = read_checksums()
    digests: dict[str, str] = {}
    fetched = skipped = mismatches = 0
    total_bytes = 0

    for rel, want_bytes in FILES:
        dest = CACHE / rel
        if dest.exists() and rel in known and sha256_of(dest) == known[rel]:
            digests[rel] = known[rel]
            skipped += 1
            action = "skipped (hash matches CHECKSUMS.txt)"
        else:
            download(rel, dest)
            digests[rel] = sha256_of(dest)
            fetched += 1
            action = "fetched"
            if rel in known and known[rel] != digests[rel]:
                mismatches += 1
                print(f"  ! {rel}: sha256 CHANGED from {known[rel]} to {digests[rel]}")

        got_bytes = dest.stat().st_size
        total_bytes += got_bytes
        if got_bytes != want_bytes:
            mismatches += 1
            print(f"  ! {rel}: {got_bytes:,} bytes, INDEX.md says {want_bytes:,}")
        note = ""
        if dest.suffix.lower() in (".csv", ".tsv") and got_bytes > PARQUET_MIN_BYTES:
            note = "; " + to_parquet(dest)
        print(f"  {action:38s} {got_bytes:>12,} B  {rel}{note}")

    CHECKSUMS.write_text("".join(f"{digests[r]}  {r}\n" for r in sorted(digests)))

    print(
        f"{RELEASE}: {fetched} fetched, {skipped} skipped, {total_bytes:,} bytes, "
        f"{mismatches} mismatch(es); checksums in {CHECKSUMS}"
    )
    if mismatches:
        print("FAIL: size or checksum mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
