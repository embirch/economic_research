---
from: steward
to: director
about: programme
type: status
needs-reply: no
date: 2026-09-16
---

Step C1 for `release_2025_09_15` done, in answer to `room/director-2026-09-16-session-1-1-kickoff.md`.

Files produced: `data/fetch/release_2025_09_15.py` and `data/releases/release_2025_09_15.md`
(all eleven required H2 sections, every fact with its command).

Checks passed: 38/38 files fetched, byte sizes match `data/releases/INDEX.md`, 38 sha256 lines
written and re-verified, re-run is a no-op, one Parquet sibling. Grain unique on the nine-column
key in all three AEI files (0 duplicates).

Reproduced with Anthropic's own code: Figure 2.11 (−3.111834, R² 0.393687, N 111); the AUI to
0.00000000 (denominator = thresholded countries **plus** `not_classified` over thresholded
population only); every AUI, usage-share, GDP-elasticity (0.6895 / 1.7684), Chapter 1 and
Chapter 3 number in the report. Not reproduced: Figure 3.4's Gini pair — the released function
gives 0.8225/0.8421, the report 0.84/0.86; keeping `none` and `not_classified` gives 0.8356/0.8597,
which is the published pair. Both recorded.

Two things for the skill-correcting thread: the report's 49%/77%/12% automation figures use a
**different denominator** from the file's `automation_pct`; and Utah carries no flag in the data —
only a +25.1 automation residual. Four errors in Anthropic's own README/data_documentation logged.

Not committed — yours to commit.
