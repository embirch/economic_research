---
from: steward
to: director
about: programme
type: status
needs-reply: no
date: 2026-09-16
---

Step C1 for `release_2026_01_15/` (fourth report, primitives, Sonnet 4.5), answering
`room/director-2026-09-16-session-1-1-kickoff.md`. Written from
`data/releases/release_2026_01_15.md`; this note was filed late (the profiling thread was
archived before it could report).

Files: `data/fetch/release_2026_01_15.py` and `data/releases/release_2026_01_15.md` (all eleven
H2 sections, 27 numbered verification commands). Four raw files, 141,659,531 bytes, sizes match
`data/releases/INDEX.md`; `CHECKSUMS.txt` written; Parquet siblings built.

Checks passed (V19 re-run today): 174 country ids of which 55 sit below the 200-conversation
threshold (minimum 15), 1,091 sub-national ids of which 540 sit below 100 (minimum 1) — the
thresholds are **not** applied. Grain unique on the nine-column key; `NA` present, `NAM` absent.

Reproduced: 20 published numbers, including the AUI (Denmark 2.1007), the 0.32 state Gini, the
GDP elasticity 0.6998, both Figure 2.2 clusters field by field, and the task horizons 3.48 h /
18.93 h. Not reproduced: the 0.36 tech-worker slope (0.3124 with an ACS substitute; BLS OEWS
403s) and the 9×/12× speedup (needs conversation-level ratios).

Open: six skill corrections recorded, now in `data/ATLAS.md`.
