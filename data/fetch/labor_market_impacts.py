#!/usr/bin/env python3
"""Fetch the `labor_market_impacts/` folder of Anthropic/EconomicIndex.

Run from the repository root:  python data/fetch/labor_market_impacts.py

Downloads every file of the folder into data/cache/labor_market_impacts/ (gitignored),
checks byte sizes against data/releases/INDEX.md, writes sha256 to CHECKSUMS.txt and
skips files whose hash already matches. Raw files are write-once and never modified.
Both files are far below the 20 MB Parquet threshold of data/fetch/README.md, so no
Parquet sibling is written.
"""

import hashlib
import sys
import urllib.request
from pathlib import Path

RELEASE = "labor_market_impacts"
BASE = "https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/main/"

# Path -> expected byte size, from data/releases/INDEX.md (revision 2ea58ff).
FILES = {
    "labor_market_impacts/job_exposure.csv": 37176,
    "labor_market_impacts/task_penetration.csv": 1889822,
}

CACHE = Path("data/cache") / RELEASE


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read_checksums(path: Path) -> dict:
    if not path.exists():
        return {}
    out = {}
    for line in path.read_text().splitlines():
        if line.strip():
            digest, rel = line.split("  ", 1)
            out[rel] = digest
    return out


def main() -> int:
    if not Path("data/releases/INDEX.md").exists():
        sys.exit("run from the repository root: python data/fetch/labor_market_impacts.py")

    CACHE.mkdir(parents=True, exist_ok=True)
    checksums_path = CACHE / "CHECKSUMS.txt"
    known = read_checksums(checksums_path)

    fetched, skipped, total_bytes, problems = 0, 0, 0, []
    digests = {}

    for remote, expected_size in FILES.items():
        rel = remote[len(RELEASE) + 1:]          # keep the folder-internal path
        local = CACHE / rel
        local.parent.mkdir(parents=True, exist_ok=True)

        if local.exists() and rel in known and sha256(local) == known[rel]:
            digests[rel] = known[rel]
            skipped += 1
            total_bytes += local.stat().st_size
            if local.stat().st_size != expected_size:
                problems.append(f"{rel}: {local.stat().st_size} bytes on disk, "
                                f"INDEX.md says {expected_size}")
            continue

        if local.exists() and rel in known:
            problems.append(f"{rel}: sha256 mismatch against CHECKSUMS.txt — not overwritten")
            continue

        tmp = local.with_suffix(local.suffix + ".part")
        with urllib.request.urlopen(BASE + remote) as resp, tmp.open("wb") as fh:
            while True:
                chunk = resp.read(1 << 20)
                if not chunk:
                    break
                fh.write(chunk)
        size = tmp.stat().st_size
        if size != expected_size:
            tmp.unlink()
            problems.append(f"{rel}: downloaded {size} bytes, INDEX.md says {expected_size}")
            continue
        tmp.rename(local)
        digests[rel] = sha256(local)
        fetched += 1
        total_bytes += size

    checksums_path.write_text(
        "".join(f"{digests[rel]}  {rel}\n" for rel in sorted(digests))
    )

    print(f"{RELEASE}: {fetched} fetched, {skipped} skipped (hash match), "
          f"{total_bytes} bytes in {CACHE}")
    print(f"CHECKSUMS.txt: {len(digests)} of {len(FILES)} files")
    for p in problems:
        print("MISMATCH:", p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
