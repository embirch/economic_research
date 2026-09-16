#!/usr/bin/env python3
"""Fetch the public Anthropic sources that sit beside Anthropic/EconomicIndex.

Convention: data/fetch/README.md. Profiles and cautions: data/ATLAS.md
(`## Supplementary sources`) and data/releases/INDEX.md (`## Second distribution channel`,
`## Sibling Anthropic datasets on Hugging Face`).

Three groups, all keyless:
  1. Anthropic/AnthropicInterviewer  — 1,250 interview transcripts (NOT the 80,508 of the
     March 2026 feature, which is unreleased).
  2. Anthropic/enabling-independent-research — partner cluster tables over ~250k Claude.ai and
     Claude Code conversations, April-May 2026; the only public Anthropic file with Claude Code.
  3. economic-research.anthropic.com zips — the second distribution channel for the two most
     recent Economic Index waves; byte-identical to Hugging Face, so fetched only to re-verify
     that claim, never as an input.

Downloads into data/cache/supplementary/<group>/, skips files whose sha256 already matches,
writes CHECKSUMS.txt per group, and prints a summary. Raw files are write-once.

Run from the repository root:  python data/fetch/supplementary_anthropic.py
"""

from __future__ import annotations

import hashlib
import sys
import zipfile
from pathlib import Path

import requests

CACHE = Path("data/cache/supplementary")
HF = "https://huggingface.co/datasets"
GCS = "https://economic-research.anthropic.com/releases/econ-index"

# (group, relative path, url, sha256 as verified 2026-09-16)
FILES = [
    ("anthropic_interviewer", "README.md", f"{HF}/Anthropic/AnthropicInterviewer/resolve/main/README.md",
     "2ef76a7484626211b2b3b37ec865c3a28bc90d49d49ec8414fb4504cd55db185"),
    ("anthropic_interviewer", "workforce_transcripts.csv",
     f"{HF}/Anthropic/AnthropicInterviewer/resolve/main/interview_transcripts/workforce_transcripts.csv",
     "09ff307d42ebc8ed0b0ba25f41ffe2e50e9baa0b3c1ab4133ee528118817aab4"),
    ("anthropic_interviewer", "creatives_transcripts.csv",
     f"{HF}/Anthropic/AnthropicInterviewer/resolve/main/interview_transcripts/creatives_transcripts.csv",
     "d4e865b9959671990ceb51089c7494dbeed7560f9a623da873e6eb0f1b6506b4"),
    ("anthropic_interviewer", "scientists_transcripts.csv",
     f"{HF}/Anthropic/AnthropicInterviewer/resolve/main/interview_transcripts/scientists_transcripts.csv",
     "338677e4a4ec17824cb5bfbc9242c8a37e7041157d34fb65e7e6fb58ea3f407a"),
    ("enabling_independent_research", "README.md",
     f"{HF}/Anthropic/enabling-independent-research/resolve/main/README.md",
     "4af508201e6571138a217fa91b53db0d053e215f16547221a1b900c5ce5d6926"),
    ("enabling_independent_research", "stanford_clusters.csv",
     f"{HF}/Anthropic/enabling-independent-research/resolve/main/stanford_clusters.csv",
     "b18fa38b6dfb43b63d981ce9d233cae71ebdca28e9c488adc4fc8b2172579a91"),
    ("enabling_independent_research", "oxford_clusters.csv",
     f"{HF}/Anthropic/enabling-independent-research/resolve/main/oxford_clusters.csv",
     "280d11af144c3a7b961423bb064cc795f1b17000b3386175790d918d9a74e31f"),
    ("enabling_independent_research", "metr_clusters.csv",
     f"{HF}/Anthropic/enabling-independent-research/resolve/main/metr_clusters.csv",
     "69b0d3e4ae956dbdf8fe14a603c70d5871884adcb589d0e78c62700e891e01bb"),
    ("enabling_independent_research", "metr_addendum_clusters.csv",
     f"{HF}/Anthropic/enabling-independent-research/resolve/main/metr_addendum_clusters.csv",
     "226fb00be668b6ad1471b6f26cb9d7914f8870c83da9e878a24c67254433c000"),
    ("econ_research_zips", "release-2026-06-26.zip", f"{GCS}/release-2026-06-26.zip",
     "9be20dd451b91e4d59bd605528a8d5e55f6a182c1d280172f303f871553236da"),
    ("econ_research_zips", "release-2026-03-24.zip", f"{GCS}/release-2026-03-24.zip",
     "a4efbee617e32b1df74b68a32663dff9c7b9fb4eab8b24be9205429da9ef2d49"),
]

# sha256 of each zip member, as published on Hugging Face (verified 2026-09-16).
ZIP_MEMBERS = {
    "release-2026-06-26.zip": {
        "README.md": "1a01eeb7d34250b192aa9c906098bea1db971644e6bdb04497d87b7a4ed141a5",
        "aei_1p_api_2026-06-26.csv": "62197f003e001945ad130c2f26f5e07f3fda45ff41644df91444b04fd524a19f",
        "aei_claude_ai_2026-06-26.csv": "f974b358bce0e5a8417510c61da4342234cd0de9d9d0b62acf4c6dbcf8ec7b68",
    },
    "release-2026-03-24.zip": {
        "aei_claude_ai_2026-03-24.csv": "69ebf6f9afc1e3be45caab172a84ae09e78bf41b97e1c310100d81c8a35a7433",
    },
}


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


def zip_member_hashes(zip_path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    with zipfile.ZipFile(zip_path) as zf:
        for name in zf.namelist():
            h = hashlib.sha256()
            with zf.open(name) as fh:
                for chunk in iter(lambda: fh.read(1 << 20), b""):
                    h.update(chunk)
            out[name] = h.hexdigest()
    return out


def main() -> int:
    if not Path("data/fetch/README.md").exists():
        raise SystemExit("run from the repository root")

    fetched = skipped = 0
    problems: list[str] = []
    by_group: dict[str, list[str]] = {}

    for group, rel, url, want in FILES:
        dest = CACHE / group / rel
        if dest.exists() and sha256_of(dest) == want:
            skipped += 1
        else:
            download(url, dest)
            fetched += 1
        got = sha256_of(dest)
        if got != want:
            problems.append(f"{group}/{rel}: sha256 {got} != expected {want}")
        by_group.setdefault(group, []).append(f"{got}  {rel}")

    for group, lines in by_group.items():
        (CACHE / group / "CHECKSUMS.txt").write_text(
            "\n".join(sorted(lines, key=lambda s: s.split("  ", 1)[1])) + "\n"
        )

    # The mirror's only job is to prove it is a mirror: hash every member in place.
    for zip_name, members in ZIP_MEMBERS.items():
        got = zip_member_hashes(CACHE / "econ_research_zips" / zip_name)
        if got != members:
            problems.append(f"{zip_name}: member hashes differ from the Hugging Face folder: {got}")
        else:
            print(f"  {zip_name}: {len(members)} members, all sha256 identical to Hugging Face")

    total = sum((CACHE / g / f.split('  ', 1)[1]).stat().st_size for g, ls in by_group.items() for f in ls)
    print(f"supplementary_anthropic: {fetched} fetched, {skipped} skipped, {total:,} bytes in {CACHE}")
    if problems:
        print("MISMATCH:")
        for p in problems:
            print(f"  {p}")
        return 1
    print("  all sha256 match the values recorded in data/ATLAS.md (2026-09-16)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
