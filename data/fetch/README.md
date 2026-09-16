# data/fetch/

One script per folder of `Anthropic/EconomicIndex`: `data/fetch/<release>.py`, where `<release>`
is the folder name (`release_2026_06_26`, `labor_market_impacts`, …). File list and sizes come
from `data/releases/INDEX.md`.

Each script must:

1. Download **every** file of that folder from
   `https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/main/<path>` into
   `data/cache/<release>/`, keeping the folder's internal path (`data/input/…` stays
   `data/input/…`). `data/cache/` is gitignored.
2. Skip a file already present whose sha256 matches, so a rebuild is a no-op.
3. Write `data/cache/<release>/CHECKSUMS.txt`: one line per file, `<sha256>  <relative path>`,
   sorted by path (`sha256sum -c` compatible). Re-verify against it on every run and fail loudly
   on a mismatch.
4. Convert every CSV/TSV larger than 20 MB to Parquet beside the raw file
   (`<name>.csv` → `<name>.parquet`), reading with `keep_default_na=False` (`NA` is Namibia) and
   with `usecols`/dtypes where the schema is known. Smaller files are left as-is.
5. Never modify, rewrite or delete a raw file. Downloads are write-once; Parquet is a derived
   sibling, and `.parquet` is gitignored.
6. Print a summary only: files fetched, files skipped, bytes, and any size mismatch against
   `data/releases/INDEX.md`. No large tables.

Run from the repository root (`python data/fetch/release_2026_06_26.py`). Paths are relative to
the repository root, not to the script.

Notes for whoever writes them: the path shape differs by wave (see the Discrepancies section of
`data/releases/INDEX.md`), so hard-code the file list per release rather than guessing it, and do
not use the dataset card's `configs` block — one of its paths 404s. The tree API
(`…/api/datasets/Anthropic/EconomicIndex/tree/main/<release>?recursive=true`) is the authority
for the list and the byte sizes; no token is needed.

## Sources beside the dataset

`data/fetch/supplementary_anthropic.py` (added 2026-09-16) fetches the public Anthropic sources
that are **not** part of `Anthropic/EconomicIndex`: `Anthropic/AnthropicInterviewer` (1,250
transcripts), `Anthropic/enabling-independent-research` (partner cluster tables, April–May 2026,
the only public Anthropic file with Claude Code fields) and the two zips served by
`economic-research.anthropic.com/releases/econ-index/`, whose members it hashes in place to
re-prove that the mirror is byte-identical to Hugging Face. Same rules: write-once, sha256 pinned
in the script, `CHECKSUMS.txt` per group, summary only. Profiles: `data/ATLAS.md`
§Supplementary sources and `data/releases/INDEX.md` §Second distribution channel.

`data/fetch/supplementary_onet.py` (added 2026-09-16) fetches the two O\*NET Center files the
dataset does not ship: the official **O\*NET-SOC 2010 → 2019 crosswalk**, without which the fifth
report's occupational figures (Appendix Figure A.1, the "+14% API / −18% Claude.ai" of p.7, the
35% of p.5) do not reproduce — see `data/ATLAS.md` §Conventions, "SOC major groups from
`onet_task`, and the 2019 recode" — and the **O\*NET 27.3 text zip**, the vintage
`labor_market_impacts/` was built on. Both CC BY 4.0, both sha256-pinned in the script.

## Replication scripts

`data/replication/` holds the re-implementations of published numbers that no released notebook
covers (reports 4, 5 and 6 ship no code). Each runs from the repository root against
`data/cache/`, prints its merge audit, and writes a small CSV under
`data/replication/results/`.

