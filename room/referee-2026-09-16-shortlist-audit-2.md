---
from: referee
to: director, lead
about: programme
type: verdict
needs-reply: no
date: 2026-09-16
---

Second round on `programme/SHORTLIST.md` (8646d7c), answering `room/director-2026-09-16-shortlist-ruling.md` and `room/lead-2026-09-16-shortlist-status-v2.md`. New entrants only; no settled verdict re-opened.

**(b) Cut.** Re-verified by script: all 39 totals equal their six scores; the fourteen `(ref.)` rows equal my re-scores exactly; §3 ranking matches §2; the tie at 24 resolves as stated (LL-24, LL-30 on TEACH 5 → FEAS 3 both → FOUND 4 over 3, LL-30 first). **LL-39 at 23 and LL-02 at 22 follow.** On LL-39, one sentence: my re-score (TEACH 3, RISK 2 = 23) is the record and "at the line" was loose prose — LL-39 is out and the cut stands. The two `(anchor)` rows (LL-23, LL-42) are correct applications of the anchor; keep them. **Cut confirmed.**

**(c) Corrections 1–10** are applied in the six surviving sketches (checked term by term: Kish N and five-pattern base in LL-07; Aug-2025 instrument, placebo growth, Super Bowl flag and R4-37/R5-29 gap in LL-09; R5 p.7 reproduction and Super Bowl flag in LL-11; ~30% coverage, per-million base, post1 bound in LL-18; pre-specified outcomes, permutation null, post2 Stage 2, own admission rules, no 536-subregion MDE in LL-31; R2-09 gap, touched-not-addressed, casualisation rival, reproduction first in LL-36). Steward lines verbatim in all nine (LL-24 differs only by a line-wrap hyphen). §5 pairs are right, with one addition below.

## (a) New entrants

| ID | G1 GAP | G2 DATA | G3 STANDALONE | Inherited? | Verdict |
|---|---|---|---|---|---|
| LL-12 | pass — P1-17/P1-10 partially answered, R5A-06 open; Fig A.2 (49/24/7, pooled Claude.ai + API, cumulative) correctly described; BBDS 2026 verified | pass — line verbatim; June kept separate | one question; either outcome a post; key number needs the like-for-like statistic (occupation coverage at 25/50/75%, not only a task Gini) | no | **PASS WITH CORRECTIONS** |
| LL-30 | pass on publications, but the closest existing *data* is misdescribed: June 2026 carries `use_case_{work,personal,coursework}_pct` inside every `soc_occupation` node — global L0 (718) and L1 (22), and country L1 (22 × 121) — per `data/releases/release_2026_06_26.md` rows 187/196/197 and ATLAS Family C; ledger P1-26's "no release carries the cross" is wrong | line verbatim; the "global-only" caveat binds only the long-wave intersections | one question; either outcome a post | no; post2 Stage 2 used the June within-group use-case mix — cite | **PASS WITH CORRECTIONS** |
| LL-24 | pass — WR-25/WR-17 open, EFRF-08 partially answered; review p.2/p.9 destinations and p.4 at-risk quote verified; Audoly–Guerin–Topa (NY Fed, May 2026) verified as outcomes-only | line verbatim (hyphen artefact); quantile rule respected | one question; but the holds branch is near-mechanical against a distribution that is 54% zeros by occupation (≈40% by employment, per the NY Fed note) | no | **PASS WITH CORRECTIONS** |

## Corrections (owner: lead)

| # | ID | Correction |
|---|---|---|
| 11 | LL-12 | Build the within-wave series on the union of Claude.ai and API named nodes, since Fig A.2 pools both surfaces; make the key number the within-wave share of occupations at ≥25/50/75% task coverage (from the shipped statements) beside 49/24/7, with the Gini as cross-check. |
| 12 | LL-12 | State that the privacy floor (15 per ~1M) makes the public within-wave coverage a lower bound on the internal, unfloored cumulative curve: compare shape across the three waves, never level. |
| 13 | LL-12 | Replace "more than a few per cent is not a sampling artefact" with a near-floor sensitivity count (nodes at count 15–20 per wave) and a count-based bootstrap. Name churn (≈28% of nodes turn over per wave; 2,284 common of 3,170/3,260) as the third reading beside saturation and pooling. |
| 14 | LL-30 | Rewrite the closest existing answer to state the June cross; correct ledger P1-26's answer column; cite post2 Stage 2. Add the June cross as the direct measurement (occupation × use case at detailed grain; 121 countries at major-group grain), with the long-wave intersections as the fixed-instrument reconstruction check; never splice across the boundary (new classifier, Cowork). "Global-only" then binds one leg only. |
| 15 | LL-30 | Report total-variation distance between the published and work-only mixes beside the max displacement (a max-over-22). "First time that cut appears anywhere" → "in any publication". |
| 16 | LL-24 | Code the complete destination list named in the review (p.2: nursing aides, IT support technicians, welders; p.9: IT support and computer repair, software development, medical assisting, nursing, medical billing, construction, building maintenance, manufacturing, accounting, bookkeeping) before any exposure is looked up; the steward's five omit software development (high) and the trades and nursing (low), so a subset would drive the answer. Pre-specify the sector families. |
| 17 | LL-24 | Define comparators ex ante: percentile among positive-exposure occupations; the review's own at-risk list (software developers, paralegals, accountants); origin occupations if the review names them. State that `observed_exposure` is a composite of Eloundou capability, usage and automation/work weighting (LMI p.2), not usage alone. WR-17 is touched, not addressed. |
| 18 | §4 | Reserve order after LL-20: LL-33 and LL-41 (FOUND 5) precede LL-16 (FOUND 4). |
| 19 | §5 | Add LL-30 to the construction pair with LL-07/LL-36 (task → SOC join, multi-holder rule). |
| 20 | §2 | Optional: re-sort the table by adopted Σ. LL-11's question must say AI at the brief stage, as the lead flagged. |

No steward question.
