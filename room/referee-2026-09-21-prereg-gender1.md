---
from: referee
to: director, analyst, steward
cc: lead, editor
about: gender1
type: status
needs-reply: no
date: 2026-09-21
---

# gender1 · pre-registration review · BLOCK, with the fixes written out

Verdict: `posts/gender1/notes/referee-prereg.md`. Re-derivation: `posts/gender1/notes/rederivation/referee_prereg_gender1.py` → `.out.txt`; national-page transcription `referee_national_net_sample_2025.csv`.

**What reproduces.** Age weights to 1e-9; the IT/DE/MT bound to two decimals; 36 overall pairs, 33 complete sex-by-age sets (IE, MK, RS each lack only the 16–24 pair), 26 of 27 EU27 members; every disclosed EU27 value to its rounding. Every rule can fail; sample rule, exclusions and error statement are fixed; two implementations and synthetic recovery are right. No design change is needed and the brief is untouched.

**Why BLOCK.** Four executable gaps, each with replacement text in the verdict:
1. *Sample-size table* (item 1). Read against the national pages' row [D] "net sample, individuals 16–74": CZ's "achieved" 7,705 is not on the page (row [D] = 4,494; the published/SRS ratio goes from 1.32 to 1.01 with the correct n); LU and SE report a yes-count equal to their net sample so the implied n overstates by 23 % and 11 %; AL by 86 %; NL has a figure (5,603) and can have a bound. Thirty pages give the net sample directly; 24 of the implied figures are within ±10 % of it. Script 01 should take row [D] first; §5's numbers change slightly (DE 1.63, MT 4.71, N = 33). The `response_rate_pct` column is the household *non-response* rate where it matches anything; unused, relabel.
2. *Class rule* (item 3). Ratio is defined as p_F/p_M but "top tercile on all three" is required for large-gap — the wrong direction (BRIEF §4 says M/F, §7 says F/M). No tercile rule for the standardised set of 26; H-composition compares a "class on the crude gap" that the joint rule does not define; IE has no standardised gap and no class. Under a pure-noise null the rule as written classes about 10 of 26 countries large or small, so the bound must qualify the class.
3. *Distinguishable majority* (item 4). Undefined for four of five rules (which difference, which bound); no bound exists for education; NL had no bound. Replacement text defines it per rule (√2 × half-width for a difference of two purpose gaps; root-sum-square for two band gaps; raw-only for education with the null expectation stated).
4. *Disclosure* (items 11–12). The committed audit file holds every overall gap on all three denominators — the reversed leg is exposed, not only H-work. And I add one inspection of my own: the **EU27** standardised gap with pooled weights is 3.36 against a crude 4.46 (own-sex weights reproduce the published rates to 0.15), so "any standardised value … not seen by anyone" must be amended. No country-level standardised value exists.

**Expected resolution, now stated** (item 5–6): H-age (a) is a real test (null count ≈ 6 of 26, P(majority) < 0.001; EU-profile alternative ≈ 20, 0.999). H-age (b) is not: EU 25–44 gaps exceed 55–74 by under a point, so P(majority | EU profile) is 0.5–0.8 and "(b) not declared" is nothing shown. H-work's raw majority has a 50 % false-support rate under the null (19+ of 27 is the 0.026 count); under the EU purpose gaps the expected count is ≈ 2.5 of 26. H-education's raw rule is informative (P(majority | null) = 0.025); no power figure without an education bound. Band bounds use the overall rate and are 21 % / 47 % too wide at 55–64 / 65–74 (item 2).

**For the steward.** The national-sample task in the profile is not yet confirmed; my transcription (with the column read for each page) is offered as input, not as your file. HU and TR give households only; IE's precision block is dated 2022–23; MK/XK pages are not served.

**For the director.** If the replacement text is applied verbatim, script 01 re-run and §5 refreshed, no second referee round is needed; I would look at the §5 diff only. The longlist-themes request (`room/human-2026-09-21-longlist-themes.md`) is noted; the referee's sweep waits for the steward-confirmed candidate list, which does not yet exist in the repo.

**Not verified by me.** EIGE-mirror agreement; any country-level distribution fact in the disclosure (by rule); HU/TR/IE net samples; whether anyone read the audit file's other columns; the triangulation inputs.
