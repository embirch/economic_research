#!/usr/bin/env python3
"""Fetch release_2026_03_24 of Anthropic/EconomicIndex into data/cache/release_2026_03_24/.

Convention: data/fetch/README.md. File list and byte sizes: data/releases/INDEX.md
(revision 2ea58ff75e4247d26810c37f10c179edc2466cac).

Downloads every file of the folder keeping its internal path, verifies byte size against the
list below, verifies sha256 against the Git-LFS oid published by the HF tree API (the LFS oid
IS the sha256 of the content), writes CHECKSUMS.txt, and converts CSVs over 20 MB to Parquet
beside the raw file. Raw files are write-once: never modified, never deleted.

Run from the repository root:  python data/fetch/release_2026_03_24.py
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import pandas as pd
import requests

RELEASE = "release_2026_03_24"
BASE = "https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/main"
CACHE = Path("data/cache") / RELEASE
PARQUET_MIN_BYTES = 20 * 1024 * 1024

# (path inside the release folder, bytes, sha256 == Git-LFS oid or "" when not LFS-stored)
FILES = [
    (
        "data/aei_raw_1p_api_2026-02-05_to_2026-02-12.csv",
        43_957_174,
        "b3bcd68e7f6d820ffbb50a3c53d71ec2a122556fc2a38226cd86951a054bd4c8",
    ),
    (
        "data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv",
        103_287_181,
        "69ebf6f9afc1e3be45caab172a84ae09e78bf41b97e1c310100d81c8a35a7433",
    ),
    ("data_documentation.md", 17_739, ""),
]

# Schema of both raw CSVs, confirmed by profiling (data/releases/release_2026_03_24.md).
# Every column is read; all are strings except `value`. keep_default_na=False because the
# ISO-2 country code for Namibia is NA.
CSV_DTYPES = {
    "geo_id": "string",
    "geography": "string",
    "date_start": "string",
    "date_end": "string",
    "platform_and_product": "string",
    "facet": "string",
    "level": "Int64",
    "variable": "string",
    "cluster_name": "string",
    "value": "float64",
}


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def download(rel_path: str, dest: Path) -> None:
    url = f"{BASE}/{RELEASE}/{rel_path}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    with requests.get(url, stream=True, timeout=300) as resp:
        resp.raise_for_status()
        with tmp.open("wb") as fh:
            for chunk in resp.iter_content(chunk_size=1 << 20):
                fh.write(chunk)
    tmp.replace(dest)


def to_parquet(csv_path: Path) -> str:
    pq_path = csv_path.with_suffix(".parquet")
    if pq_path.exists() and pq_path.stat().st_mtime >= csv_path.stat().st_mtime:
        return "parquet up to date"
    header = pd.read_csv(csv_path, nrows=0, keep_default_na=False).columns.tolist()
    unknown = [c for c in header if c not in CSV_DTYPES]
    if unknown:
        raise SystemExit(f"FAIL {csv_path}: unexpected columns {unknown}; update CSV_DTYPES")
    df = pd.read_csv(
        csv_path,
        usecols=header,
        dtype={c: CSV_DTYPES[c] for c in header},
        keep_default_na=False,
        na_values=[],
    )
    df.to_parquet(pq_path, index=False)
    return f"parquet written ({len(df):,} rows, {pq_path.stat().st_size:,} B)"


def main() -> int:
    if not Path("data/fetch/README.md").exists():
        raise SystemExit("run from the repository root")
    CACHE.mkdir(parents=True, exist_ok=True)

    fetched, skipped, problems, checksums, notes = 0, 0, [], [], []
    total_bytes = 0

    for rel_path, want_bytes, want_sha in FILES:
        dest = CACHE / rel_path
        have = dest.exists() and (not want_sha or sha256_of(dest) == want_sha)
        if have and dest.stat().st_size == want_bytes:
            skipped += 1
        else:
            download(rel_path, dest)
            fetched += 1

        got_bytes = dest.stat().st_size
        got_sha = sha256_of(dest)
        if got_bytes != want_bytes:
            problems.append(f"{rel_path}: {got_bytes} bytes, INDEX.md says {want_bytes}")
        if want_sha and got_sha != want_sha:
            problems.append(f"{rel_path}: sha256 {got_sha} != published LFS oid {want_sha}")
        total_bytes += got_bytes
        checksums.append(f"{got_sha}  {rel_path}")

        if got_bytes > PARQUET_MIN_BYTES and dest.suffix.lower() in (".csv", ".tsv"):
            notes.append(f"{rel_path}: {to_parquet(dest)}")

    (CACHE / "CHECKSUMS.txt").write_text("\n".join(sorted(checksums, key=lambda s: s.split("  ", 1)[1])) + "\n")

    print(f"{RELEASE}: {fetched} fetched, {skipped} skipped, {total_bytes:,} bytes in {CACHE}")
    for n in notes:
        print(f"  {n}")
    print(f"  CHECKSUMS.txt: {len(checksums)} lines (sha256sum -c compatible)")
    if problems:
        print("MISMATCH:")
        for p in problems:
            print(f"  {p}")
        return 1
    print("  all sizes and sha256 match data/releases/INDEX.md and the published LFS oids")
    return 0


if __name__ == "__main__":
    sys.exit(main())
