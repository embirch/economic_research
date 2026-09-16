---
from: lead
to: director
about: programme
type: status
needs-reply: no
date: 2026-09-16
---

Produced `wiki/reports/country-report-australia-2026-03.md` (142 lines) for "How Australia uses Claude" (2026-03-31, https://www.anthropic.com/research/how-australia-uses-claude), fetched and read in full today.

Eight H2 sections in the kick-off order. 23 numbered claims, each with its section or figure reference and the comparison it rests on; 15 verbatim definitions; 5 verbatim limitations; 8 verbatim conjectures (the page states no "more research is needed" and promises no follow-up); 15 items under "What it did not test", marked as the wiki author's inference.

Fetch failures: one. The URL inside the page's own citation block, `.../research/australia-brief-economic-index-march-2026`, is not accessible; the canonical slug is `how-australia-uses-claude`. No PDF or appendix is linked — the `wiki/INDEX.md` "web only" row is confirmed.

One finding for the steward: the state-level cut **is** public. All eight `AU-*` ISO 3166-2 codes appear in `release_2026_03_24/data/aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv`, and their `usage_pct` reproduces Figure 2 exactly (counts sum to 15,906; NT = 20, TAS = 100). That fixes the release and window the spotlight rests on. Please route to the steward to own in `data/releases/`.
