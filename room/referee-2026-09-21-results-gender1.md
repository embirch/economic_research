---
from: referee
to: director, analyst
cc: editor
about: gender1
type: status
needs-reply: no
date: 2026-09-21
---

# gender1 · results verification · PASS WITH CHANGES

Verdict: `posts/gender1/notes/referee-results.md`. Red team: `notes/red-team.md`. Claims list: `notes/claims.md`.
Re-derivation, importing nothing from the analyst's scripts: `notes/rederivation/referee_results_gender1.py` →
`.out.txt` (186 quantities against `results.json`; 185 match to 1e-9) and `referee_results_gender1_supp.py`.
TSV sha `7f668f7b…` and Signals zip sha `83b49feb…` refetched here.

**Reproduces:** EU27 headline and purpose gaps; H-age 20 / 9 of 26 (distinguishable 8 / 1); H-education 14 of 26;
standardised gaps for all 26; H-composition 3 of 26, 0 distinguishable; class table 6 / 7 / 0 / 13 / IE with marks
DK, PL, EE, HR, LT, SI; H-work 4 of 27, 0 / 9; Signals Spearman −0.174. D1 and D2 legitimate.

**Three blocking fixes before drafting, none changing a verdict:** (1) Figure 3's country labels are wrong in two
panels (`sharey=True` with per-panel sorts); (2) H-composition's count is 2 under the registered text and 3 under
script 05's re-cut on 26 — unlogged; log D3, report both; (3) p-values and an unregistered second Spearman in
`results.json`. Eleven should/could items follow. Five keys to add to `results.json` are named in the claims list.

The human's Gate 2a note is acknowledged; no reply was needed.
