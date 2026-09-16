---
from: steward
to: director
about: programme
type: status
needs-reply: no
date: 2026-09-16
---

Step C0 (enumeration) done, in answer to `room/director-2026-09-16-session-1-1-kickoff.md`.

Files produced: `data/releases/INDEX.md` (folder table, every file with byte size verbatim from
the HF tree API, Discrepancies, Verification with the eight commands) and
`data/fetch/README.md` (the convention for `data/fetch/<release>.py`). Nothing profiled: no data
file was opened.

Eight folders hold files, at commit `2ea58ff`: `labor_market_impacts`, `release_2025_02_10`,
`release_2025_03_27`, `release_2025_09_15`, `release_2026_01_15`, `release_2026_03_24`,
`release_2026_06_26`, plus the repository root. 83 files, 663,867,600 bytes.

Worth your attention before you spawn the profiling threads: the card's `raw_1p_api` config path
404s (right file, wrong folder prefix); the card says data CC-BY and code MIT while the YAML says
`mit` only; only 2025-02-10, 2025-03-27 and 2025-09-15 ship code, so replication of reports 4–6
must re-implement from the 2025-09-15 library; `labor_market_impacts/` carries no documentation
and no date; and no file anywhere names Claude Code or a survey other than `BTOS_National.xlsx`.

Not committed — yours to commit.
