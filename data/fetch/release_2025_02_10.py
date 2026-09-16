#!/usr/bin/env python3
"""Fetch every file of release_2025_02_10 from Anthropic/EconomicIndex.

Run from the repository root:  python data/fetch/release_2025_02_10.py

File list and byte sizes are hard-coded from data/releases/INDEX.md (revision
2ea58ff75e4247d26810c37f10c179edc2466cac).  Downloads go to data/cache/release_2025_02_10/
keeping the folder's internal path.  Files whose sha256 already matches CHECKSUMS.txt are
skipped.  Raw files are never modified.  No CSV in this release exceeds 20 MB, so no Parquet
conversion is performed (the rule in data/fetch/README.md applies to files > 20 MB).
"""

import hashlib
import sys
import urllib.request
from pathlib import Path

RELEASE = "release_2025_02_10"
BASE = "https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/main"
CACHE = Path("data/cache") / RELEASE

# path inside the release folder -> byte size from data/releases/INDEX.md
FILES = {
    "README.md": 2981,
    "SOC_Structure.csv": 77176,
    "automation_vs_augmentation.csv": 197,
    "bls_employment_may_2023.csv": 1132,
    "onet_task_mappings.csv": 461306,
    "onet_task_statements.csv": 3592256,
    "plots.ipynb": 25886,
    "plots/automation_vs_augmentation.png": 38030,
    "plots/occupational_category_distribution.png": 141804,
    "plots/occupational_category_distribution_bls.png": 230300,
    "plots/occupations_distribution.png": 104710,
    "plots/task_distribution.png": 221631,
    "plots/wage_distribution.png": 214070,
    "wage_data.csv": 128047,
}
PARQUET_THRESHOLD_BYTES = 20 * 1024 * 1024


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_checksums() -> dict:
    f = CACHE / "CHECKSUMS.txt"
    if not f.exists():
        return {}
    out = {}
    for line in f.read_text().splitlines():
        if line.strip():
            digest, rel = line.split("  ", 1)
            out[rel] = digest
    return out


def main() -> int:
    if not Path("data/fetch").is_dir():
        sys.exit("run from the repository root")
    CACHE.mkdir(parents=True, exist_ok=True)
    known = read_checksums()

    fetched, skipped, size_mismatch, hash_mismatch = 0, 0, [], []
    digests = {}

    for rel, want_bytes in sorted(FILES.items()):
        dest = CACHE / rel
        if dest.exists() and rel in known and sha256(dest) == known[rel]:
            digests[rel] = known[rel]
            skipped += 1
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            url = f"{BASE}/{RELEASE}/{rel}"
            with urllib.request.urlopen(url) as resp, dest.open("wb") as fh:
                while True:
                    chunk = resp.read(1 << 20)
                    if not chunk:
                        break
                    fh.write(chunk)
            digests[rel] = sha256(dest)
            fetched += 1
            if rel in known and known[rel] != digests[rel]:
                hash_mismatch.append(rel)
        got = dest.stat().st_size
        if got != want_bytes:
            size_mismatch.append((rel, want_bytes, got))
        if got > PARQUET_THRESHOLD_BYTES and rel.endswith((".csv", ".tsv")):
            print(f"NOTE: {rel} exceeds 20 MB; Parquet conversion not implemented here")

    (CACHE / "CHECKSUMS.txt").write_text(
        "".join(f"{digests[r]}  {r}\n" for r in sorted(digests))
    )

    total = sum((CACHE / r).stat().st_size for r in FILES)
    print(f"{RELEASE}: {fetched} fetched, {skipped} skipped, {len(FILES)} files, {total} bytes")
    print(f"checksums: {CACHE / 'CHECKSUMS.txt'}")
    if size_mismatch:
        for rel, want, got in size_mismatch:
            print(f"SIZE MISMATCH vs INDEX.md: {rel} expected {want} got {got}")
    else:
        print("size check: all 14 files match data/releases/INDEX.md")
    if hash_mismatch:
        for rel in hash_mismatch:
            print(f"HASH MISMATCH vs CHECKSUMS.txt: {rel}")
        sys.exit("checksum mismatch: upstream file changed; investigate before using the cache")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
