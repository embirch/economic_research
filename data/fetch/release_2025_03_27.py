#!/usr/bin/env python3
"""Fetch every file of release_2025_03_27/ from Anthropic/EconomicIndex on Hugging Face.

Convention: data/fetch/README.md. File list and byte sizes: data/releases/INDEX.md
(revision 2ea58ff75e4247d26810c37f10c179edc2466cac).

Run from the repository root:  python data/fetch/release_2025_03_27.py

Downloads into data/cache/release_2025_03_27/ keeping the folder's internal path,
verifies byte sizes against INDEX.md, writes sha256 lines to CHECKSUMS.txt, and skips
files whose sha256 already matches. Raw files are write-once and never modified.
No file in this release exceeds 20 MB, so no Parquet conversion is done (the largest
is onet_task_statements.csv at 3.6 MB); the rule in data/fetch/README.md §4 is a no-op
here.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import requests

RELEASE = "release_2025_03_27"
BASE = "https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/main"
REVISION = "2ea58ff75e4247d26810c37f10c179edc2466cac"
CACHE = Path("data/cache") / RELEASE
PARQUET_THRESHOLD = 20 * 1024 * 1024

# (path inside the release folder, bytes per data/releases/INDEX.md)
FILES: list[tuple[str, int]] = [
    ("README.md", 3205),
    ("SOC_Structure.csv", 77176),
    ("automation_augmentation_by_occupation.png", 672136),
    ("automation_augmentation_comparison.png", 149993),
    ("automation_vs_augmentation_by_task.csv", 561368),
    ("automation_vs_augmentation_v1.csv", 197),
    ("automation_vs_augmentation_v2.csv", 198),
    ("cluster_level_data/README.md", 2917),
    ("cluster_level_data/cluster_level_dataset.tsv", 947989),
    ("cluster_level_data/cluster_level_example_analysis.ipynb", 280733),
    ("normalized_automation_by_category.png", 854296),
    ("onet_task_statements.csv", 3592256),
    ("task_pct_v1.csv", 461306),
    ("task_pct_v2.csv", 435372),
    ("task_thinking_fractions.csv", 372332),
    ("v2_report_replication.ipynb", 1897331),
]
EXPECTED_TOTAL = 10308805


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_checksums(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    out = {}
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        digest, rel = line.split("  ", 1)
        out[rel] = digest
    return out


def download(rel: str, dest: Path) -> None:
    url = f"{BASE}/{RELEASE}/{rel}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    with requests.get(url, stream=True, timeout=120) as r:
        r.raise_for_status()
        with tmp.open("wb") as fh:
            for chunk in r.iter_content(1 << 20):
                fh.write(chunk)
    tmp.replace(dest)


def main() -> int:
    CACHE.mkdir(parents=True, exist_ok=True)
    checks_path = CACHE / "CHECKSUMS.txt"
    known = read_checksums(checks_path)

    fetched, skipped, size_mismatch, hash_mismatch = [], [], [], []
    digests: dict[str, str] = {}
    total_bytes = 0

    for rel, expected_size in FILES:
        dest = CACHE / rel
        if not dest.exists():
            download(rel, dest)
            fetched.append(rel)
        else:
            skipped.append(rel)
            # A raw file is never modified here, so a recorded hash that no longer
            # matches means the file on disk (or upstream) changed: report, do not
            # overwrite.
            if rel in known and sha256_of(dest) != known[rel]:
                hash_mismatch.append(rel)

        actual = dest.stat().st_size
        total_bytes += actual
        if actual != expected_size:
            size_mismatch.append((rel, expected_size, actual))
        digests[rel] = sha256_of(dest)

    lines = [f"{digests[rel]}  {rel}" for rel in sorted(digests)]
    checks_path.write_text("\n".join(lines) + "\n")

    print(f"{RELEASE}  (revision {REVISION})")
    print(f"  fetched {len(fetched)}, already present {len(skipped)}, "
          f"files {len(FILES)}, bytes {total_bytes:,}")
    print(f"  INDEX.md total {EXPECTED_TOTAL:,}  -> "
          f"{'MATCH' if total_bytes == EXPECTED_TOTAL else 'MISMATCH'}")
    print(f"  checksums: {checks_path}")
    print(f"  files over {PARQUET_THRESHOLD//1024//1024} MB needing Parquet: 0")
    if hash_mismatch:
        print("  CHECKSUM MISMATCH (raw file changed on disk or upstream): "
              + ", ".join(hash_mismatch))
    for rel, exp, act in size_mismatch:
        print(f"  SIZE MISMATCH {rel}: INDEX.md {exp}, on disk {act}")
    if size_mismatch or hash_mismatch or total_bytes != EXPECTED_TOTAL:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
