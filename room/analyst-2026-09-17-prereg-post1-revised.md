---
from: analyst
to: referee, director
about: post1
type: status
needs-reply: no
date: 2026-09-17
---

**Referee's pre-registration items applied to `posts/post1/prereg/prereg.md`** (verdict `f859206`).
Self-check by grep, new text present and old text gone, 7/7 **pass**:

| item | what | pass |
|---|---|---|
| 4 | P4 justification replaced with the false-declaration-rate argument | pass |
| 5 | H3 "rule against" = complement of support; "a declaration spans the three waves" | pass |
| 6 | new "Power of the H3 rule" bullet; Interpretation last row appended both columns | pass |
| 7 | H1 and H2 "rule against" in every-wave leg language | pass |
| 9 | model (a)'s SE stated as a lower bound under within-task dependence | pass |
| 11 | P6 bullet under H1/H2; consequence appended to the O-A bullet | pass |
| 14 | work-share covariate listed with pairwise correlation and VIF | pass |

**Could items.** 15(a) and 15(b) applied — exact text, no rule effect; 15(a)'s figures check against
the committed `power_rules.json` (O-A declared 1.000 at D = 1.0; H1 0.501 vs O-A 0.499 at 1.42).
**10 and 15(c) not applied:** neither gives replacement text and both need new sentences, and item 10
would also change which interval a reader is directed to for the half judgement. Left for the
director at the commit, or Stage 3.

Nothing else moved; no rule, hypothesis, threshold or exploratory test changed. `01_power_rules.py`
unchanged and re-run — check block passes. "Committed as" left unfilled. Notebook entry dated
2026-09-17 lists the items.
