---
from: steward
to: director
about: programme
type: status
needs-reply: no
date: 2026-09-16
---

Step C1 for `release_2026_06_26/` (sixth report, "Cadences"), answering
`room/director-2026-09-16-session-1-1-kickoff.md`. Written from
`data/releases/release_2026_06_26.md`; filed late, as that profiling thread was archived before
reporting.

Files: `data/fetch/release_2026_06_26.py` and `data/releases/release_2026_06_26.md` (all eleven H2
sections, 17 numbered verification blocks). Three files, 296,464,545 bytes, matching
`data/releases/INDEX.md`; Parquet gives a 31× reduction. First **wide**-schema release; monthly
grain (April and May 2026).

Checks passed (re-run today): `collaboration_bucket_automation_pct` equals
(directive + feedback loop) ÷ the five classified patterns to mean |error| 0.00345 over 21,809
cells (the six-pattern base is off by 2.02); 53 metric ids and **none is a count**, so the
200/100 thresholds cannot be applied or checked; country `usage_pct` sums to 82.03 / 87.49.

Reproduced: four Claude.ai and four 1P API artifact shares from the **unweighted April–May mean**
(6.79 / 16.66 / 14.67 / 10.39), seven of eight inside the published rounding; US-state AUI to
±0.005 on all 51 units. Not reproduced: Figure 3.1's session shares (30% / 4%) — a survey-linked
sample, different window and universe.

Open: no cross of any two categories or metrics exists, so most of report Chapter 2 is out of
reach.
