---
from: steward
to: director
about: programme
type: status
needs-reply: no
date: 2026-09-16
---

Step C1, release `release_2025_03_27` (2nd report, Claude 3.7 Sonnet) profiled.

**Files produced:** `data/fetch/release_2025_03_27.py`, `data/releases/release_2025_03_27.md`
(all eleven H2 sections in the kick-off order; dated log is a sub-section so the H2 set is
exact). Not touched: `data/ATLAS.md`.

**Checks passed:** 16/16 files fetched, 10,308,805 bytes = INDEX.md total; `sha256sum -c` clean;
rebuild idempotent and re-download verified. All 16 code cells of `v2_report_replication.ipynb`
(the dataset's only published replication notebook) ran verbatim; **every stored output matched.**

**Reproduced:** augmentation 56.9381% ("57%"), learning 23.2667→27.9879, Computer &
Mathematical +3.0143 pp, all 17×5 category shares and all 25 top-occupation bars, task curve at
x=0.2 (41.6%), and all 20 extended-thinking bars once the specification was found (blank
`thinking_fraction` = **0**, usage-weighted over all the occupation's tasks, ≥0.5% prevalence).

**Not reproduced:** "1 million conversations", "11 days" (no counts or dates in any file);
"17,000 O\*NET tasks" (file has 18,429).

**Open question:** the post says no category is automation-dominant; its own figure shows
Protective Service 55.4% and Production 54.9%. Recorded both. Worth a journal entry.
