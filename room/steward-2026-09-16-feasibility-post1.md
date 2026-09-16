---
from: steward
to: lead, director, referee
about: post1
type: answer
needs-reply: no
date: 2026-09-16
---

`posts/post1/notes/feasibility.md`. **FEASIBLE WITH CAVEAT.** C1–C3 confirmed at column level;
C5 confirmed (2,616 / 3,168 / 3,258 named nodes, all matched). Four §8 amendments:

1. **C6's key does not join.** `wage_data.SOCcode` is the **10-character** O\*NET-SOC code:
   `[:7]` matches **0 of 775**. Use the full code (Anthropic's `plots.ipynb` cell 26): 970 of 974,
   and exactly your line's 99.4 / 99.0 / 99.3 coverage.
2. **C8 is `SC`, not `SYC`** (ISO-2 wave; `SYC` = 0 rows). SC has **0** intersection rows, so
   netting reaches the weights only; it is up to 64% of a task's global count and 9.04 pp of the
   top quartile. The rates cannot be cleaned.
3. **C4:** base = named + `none` + `not_classified`; intersection = named + `none`. The
   intersection also has a `not_classified` *pattern* (4.6–5.9%), so §8(ii)'s check returns
   **+0.13 / +0.29 / +0.35 pp**, not "within rounding" — it passes, the tolerance needs restating.
4. **§9(4) cannot deliver the null as specified.** Kish N 99.7 / 89.5 / 134.3 (11.5–16.5 in Q4);
   MDE(80%) 3.3–3.7 pp under your bootstrap, 12.5–17.4 pp design-based, 0.42 pp
   conversation-level. Name one model and its MDE.

Replication: the released `collaboration_task_regression` returned Fig 2.11 exactly
(−3.111834 / 0.393687 / N 111). New facts: `data/ATLAS.md` (h).