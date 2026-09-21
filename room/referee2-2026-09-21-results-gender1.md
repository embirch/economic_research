---
from: referee
to: director
about: gender1
type: verdict
needs-reply: no
date: 2026-09-21
---

Second read of the analyst's revision a13ac3e against my results verdict
`posts/gender1/notes/referee-results.md` (46666e5) and the notebook entry of the same date. Full item-by-item
ruling: `posts/gender1/notes/referee-results-2.md`.

**PASS WITH CHANGES — no sign off yet.** All three blocking items are applied as worded (Figure 3's labels,
D3 with both counts, the p-values renamed and D4 logged), and eleven of the other twelve. I refetched the
Eurostat TSV (`7f668f7b…`) and the Signals bundle (`83b49feb…`) and re-ran 02, 03, 05, 06, 07, 04, 08: all
seven check blocks pass and `results.json` reproduces on 4,296 of 4,296 leaves bar the timestamp and one
float ULP in an uncitable p-value. No verdict, count, class or mark moved; only the medians, keys and
strings the verdict asked for.

Three fixes owed by the analyst, all in `scripts/08_results_and_figures.py` and its captions: Figure 1's
legend now covers Ireland's bar instead of Malta's; Figure 2 still prints "−0" for Belgium at 25–34 (exactly
−0.50); Figure 5's caption says the sex difference in internet use is "within a point" when the new key says
1.1. Two stale bindings in my own `notes/claims.md` and `notes/red-team.md` (extension median 4.6 → 4.4;
"within one point") are mine to correct — my first verdict's wording caused the third one.
