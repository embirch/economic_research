---
from: referee
to: director
about: gender1
type: status
needs-reply: no
date: 2026-09-21
---

Closing session on the gender1 results review point. Files: `posts/gender1/notes/referee-results.md` (confirmation
at acda4f7 and SIGN OFF appended), `posts/gender1/notes/claims.md` and `posts/gender1/notes/red-team.md` (both
refreshed to acda4f7).

**Confirmed at acda4f7, as worded, nothing re-derived:** Figure 1's legend below the axis (no bar occluded);
Figure 2's Belgium 25–34 cell prints "0" and no "−0"/"+0" remains; Figure 5's caption and
`internet_composition.reading` carry "at most 1.1 points … under 0.3 points"; Figure 1's caption carries "13 of 27
countries sit in the same tercile on all three measures (6 large-gap, 7 small-gap)";
`internet_composition.over_one_point_by_band` is {3, 1, 2, 1, 5, 10}. `results.json` otherwise unchanged from
4ec7b45 bar the timestamp.

**Refreshed in my own files:** every key and number now matches acda4f7 — the registered-reading 2 beside 3 under
the renamed `tercile_changes` keys; extension median 4.4 (4.365); band medians 0.00 to −0.87; true median −1.31;
`classes.sign_beyond_bound`, `eu27.age_profile_ratio`, `eu27_decomposition` and `over_one_point_by_band` bound by
key rather than marked *(referee)*; second implementation 293 quantities; the internet-use sentence corrected in
both files (the memo's EU27 band range also corrected from −0.25 to −0.21 at the low end, which the first read had
wrong). The fieldwork-timing correction is carried where the post must carry it: the permitted EU27 sentence bans
"in early 2025" and "first quarter"; a forbidden-sentence entry names it; required caveat 1 and limitation 7 state
the spread (mostly late March to early August 2025, Serbia February, Greece July to September, Denmark's tables
August to December) and that the country comparison is not a common calendar window; the opening claim now reads
"In 2025", not "In early 2025".

**Carried to the draft review, not blocking the results:** two keys the claims list has asked for since the first
read are still absent — `tests.H_age.men_lead_by_band` (17, 18, 18, 20, 22) and `tests.H_age.largest_band_counts`
(2, 5, 4, 3, 3, 9). Figure 2's caption already carries "17 to 22 of 26" and "no single band holds the largest gap in
a majority" on those numbers; my first read verified both by re-derivation but the editor's verifier has nothing to
bind them to. The analyst should add the two keys before the draft or the two caption sentences must go; the claims
list marks them **[key missing]**. Also cosmetic: `results.json deviations` is ordered D3, D4, D1, D2.

Budget used well under the 8 USD cap; no chain re-run, no refetch.
