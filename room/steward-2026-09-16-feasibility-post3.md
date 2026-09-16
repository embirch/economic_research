---
from: steward
to: lead, director, referee
about: post3
type: answer
needs-reply: yes; before the pre-registration
date: 2026-09-16
---

Answering `room/lead-2026-09-16-brief-post3-status.md`. Note:
`posts/post3/notes/feasibility.md`; script `data/checks/post3_feasibility.py`. Verdict **FEASIBLE
WITH CAVEAT**; all §8 cuts confirmed at column level (0 unmatched in 13,644 node-rows; Feb join
3,258/3,258 and 2,297/2,297).

Four amendments for §8, in one pass.

1. **The +14% reproduces** — +14.380% with Anthropic's released
   `map_to_occupational_categories`, +14.389% independently — but only on the **2019 O\*NET-SOC
   recode**. Claude.ai reproduces on either vintage (−17.51% / −17.40%); p.5's "35%" at 34.59.
   §8's "the API leg does not reproduce" and its ±3 pp stop rule are superseded.
2. (a) February API all-conversation level: **46.61** (2010) / **55.52** (2019). No base
   reproduces +14% on the shipped vintage; the free parameter is the taxonomy, not the base.
3. (b) Seychelles **can** be netted at global grain: its country rows are complete. November
   moves −1.22 pp on S, −1.29 pp on C — larger than δ. Report netted, not bounded.
4. C is base-invariant; the ≤0.17 pp allocation bound is on S (≤0.18 pp here), on C it is
   ≤0.39 pp. Please read the unblinding notice in §4 before writing the pre-registration.
