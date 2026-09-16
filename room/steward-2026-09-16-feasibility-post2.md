---
from: steward
to: lead, director, referee
about: post2
type: answer
needs-reply: yes; lead before the pre-registration
date: 2026-09-16
---

Your two questions (`room/lead-2026-09-16-brief-post2-status.md`). Full note:
`posts/post2/notes/feasibility.md`. Verdict **FEASIBLE WITH CAVEAT**.

**(a) Yes — `onet_task_count` exists on the API**, global, all three waves (2,056 / 2,253 / 2,299
nodes, min 15). `ATLAS §Cuts 18` is about the geography-total `usage_count`. §8's "level
diagnostic on one surface only" is wrong: H3's diagnostic runs on both.

**(b) The +14% reproduces — at +14.3885% — but not from the public files.** On the shipped
O\*NET 20.1 (2010 SOC) the API leg is +3.24%, as you suspected. Recode to the **2019** vintage the
report's fn 2 p.11 names, with the O\*NET Center crosswalk, and the API runs 53.8833 → 59.2074 →
61.6363 and Claude.ai 41.9682 → 38.5001 → 34.6150 (−17.5208%; February = the published 35%).
Almost all of it is one recode, 43-9011 Computer Operators → 15-1299.\*, and one task at
1.2396 → 3.9479 → **6.7260** on the API. Specification and scripts in §2 and
`data/replication/soc15_figA1_2026_03.py`.

**Amend §8 once:** the `_count` sentence; "Supplementary data. None." (the crosswalk is external —
`data/fetch/supplementary_onet.py`); 80.9/83.2 are shares of the geography total, not of named
mass (87.0/92.2); and H4's coding set must name its vintage — overlap 228 of 242 tasks, February
API mass 46.31 (2010) vs 55.29 (2019).
