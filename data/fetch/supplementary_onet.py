#!/usr/bin/env python3
"""Fetch the O*NET Center files the Economic Index releases do not ship.

Convention: data/fetch/README.md. Profiles: data/ATLAS.md (`## Supplementary sources`,
`## Taxonomies and identifiers`).

Two groups, both keyless, both O*NET Center (CC BY 4.0, attribute O*NET):

  1. onet_soc_2019_crosswalk — the official O*NET-SOC **2010 -> 2019** crosswalk
     (1,164 rows, 1,110 2010 codes, 1,012 2019 codes). This is the file that makes the
     March-2026 report's occupational figures reproducible: the shipped
     `onet_task_statements.csv` is O*NET DB 20.1 on the **2010** O*NET-SOC taxonomy, and
     report 5 footnote 2 (p.11) says its occupation numbers use the **2019** vintage. With
     the recode, Figure A.1 and the published "+14% API / -18% Claude.ai" reproduce; without
     it, the API leg comes out at +3.2%. See data/ATLAS.md
     `## Conventions` -> "SOC major groups from onet_task, and the 2019 recode".

  2. onet_db_27_3 — the O*NET 27.3 database text zip, the vintage
     `labor_market_impacts/task_penetration.csv` was built on (the shipped 20.1 file is the
     wrong vintage for it) and the source of `Tasks to DWAs.txt`.

Downloads into data/cache/supplementary/<group>/, skips files whose sha256 already matches,
writes CHECKSUMS.txt per group, and prints a summary. Raw files are write-once; the zip is
left packed (extract into a scratch directory, never into the cache).

Run from the repository root:  python data/fetch/supplementary_onet.py
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import requests

CACHE = Path("data/cache/supplementary")

# (group, relative path, url, sha256 and byte size as verified 2026-09-16)
FILES = [
    (
        "onet_soc_2019_crosswalk",
        "2010_to_2019_onet_soc_crosswalk.csv",
        "https://www.onetcenter.org/taxonomy/2019/walk/2010_to_2019.csv?fmt=csv",
        "8f026a33134bfde5770308d1c6117cf70d9dd41c2b3467e6dd271d65bdeecc5a",
        108052,
    ),
    (
        "onet_db_27_3",
        "db_27_3_text.zip",
        "https://www.onetcenter.org/dl_files/database/db_27_3_text.zip",
        "98450a43c573c475fdbfecfc11cb4feeb20cb0d9c6d54e1a7973b35ece092b41",
        11504351,
    ),
]


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    with requests.get(url, stream=True, timeout=300) as resp:
        resp.raise_for_status()
        with tmp.open("wb") as fh:
            for chunk in resp.iter_content(chunk_size=1 << 20):
                fh.write(chunk)
    tmp.replace(dest)


def main() -> int:
    if not Path("data/fetch/README.md").exists():
        raise SystemExit("run from the repository root")

    fetched = skipped = 0
    problems: list[str] = []
    by_group: dict[str, list[str]] = {}

    for group, rel, url, want, want_bytes in FILES:
        dest = CACHE / group / rel
        if dest.exists() and sha256_of(dest) == want:
            skipped += 1
        else:
            download(url, dest)
            fetched += 1
        got = sha256_of(dest)
        size = dest.stat().st_size
        if got != want:
            problems.append(f"{group}/{rel}: sha256 {got} != expected {want}")
        if size != want_bytes:
            problems.append(f"{group}/{rel}: {size} bytes != expected {want_bytes}")
        by_group.setdefault(group, []).append(f"{got}  {rel}")

    total = 0
    for group, lines in by_group.items():
        (CACHE / group / "CHECKSUMS.txt").write_text(
            "\n".join(sorted(lines, key=lambda s: s.split("  ", 1)[1])) + "\n"
        )
        total += sum((CACHE / group / ln.split("  ", 1)[1]).stat().st_size for ln in lines)

    print(f"supplementary_onet: {fetched} fetched, {skipped} skipped, {total:,} bytes in {CACHE}")
    if problems:
        print("MISMATCH:")
        for p in problems:
            print(f"  {p}")
        return 1
    print("  all sha256 match the values recorded in data/ATLAS.md (2026-09-16)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
