---
from: referee
to: director, lead
about: programme
type: verdict
needs-reply: no
date: 2026-09-16
---

Audit of `programme/SHORTLIST.md` (d353a12) against the three gates, the wiki, the atlas (dated log e/f/g), `programme/LEDGER.md` at 34761a9, external sources re-fetched (Tomlinson 2025; Bick–Blandin–Deming–Schumacher 2026; Chatterji 2025; Misra 2025; Brynjolfsson–Chandar–Chen Aug 2026), and `reference/posts/post1`, `post2`. All 33 cited ledger items exist with the stated status. Eight of ten steward lines are byte-identical to the steward notes; LL-18 cites "Log (e) 5" for "Log (f) 5"; LL-36 swaps `"` for `'`. Arithmetic of all 39 rows and the three tie-breaks check; the LL-01 sketch header says "Σ 28" for 26.

## Verdict summary

| ID | G1 GAP | G2 DATA | G3 STANDALONE | Verdict |
|---|---|---|---|---|
| LL-01 | FAIL — `reference/posts/post1` ran the exact test (AUI + log GDP on the task-mix residual, Aug 2025): AUI 0.10 (−0.76, 0.97) in the full model, 0.39 (−0.20, 0.98) with income alone, N=61; N=100 in script 11; Fig 2.11 reproduced on five waves. R4 App. Fig 10 (automation vs log GDP) also unmentioned | pass | fails: "first test" claims are false as written | **FAIL** (cannot pass as posed) |
| LL-02 | FAIL as written — SCPA pp.27–28 already puts the two numbers side by side ("about half … Claude.ai … three quarters … API. So 0.5 describes chat use today"); Table 2 compares a measured ψ analogue (survey 0.47) to the presets; SCPA-24/SCEX-25 answer columns already carry the steward's max 0.511 | pass (Claude.ai June leg carries the break — feedback loop +4.46, learning −5.70 — not stated) | weak: 0.511 vs 0.50 rule undefined; holds-branch is the paper's own gloss | **FAIL** (correctable, but re-scores below the cut) |
| LL-07 | pass | pass | pass | **PASS** (C1–C2) |
| LL-09 | pass, but R4-25 asks for labour-market outcomes, which usage growth is not | pass | split-sample IV not implementable on published aggregates; Feb-2026 Super Bowl inflow unflagged | **PASS WITH CORRECTIONS** |
| LL-11 | pass | pass | pass | **PASS WITH CORRECTIONS** (Super Bowl shock; reproduce R5 p.7 "+14%/−18%") |
| LL-18 | pass | pass | country task-mix adjustment runs on ~30% of a country's conversations (atlas e-2), unstated | **PASS WITH CORRECTIONS** |
| LL-22 | FAIL — `post2` H1 is this question on the same wave: 45% April→May recurrence, r=0.62, small-state phenomenon, and the two-window reporting rule; post2's brief announced "a companion post will do the same for countries"; both legs' key numbers are already in the atlas (f-8) | pass | fails: key numbers known; contribution is post2's recommendation restated | **FAIL** (cannot pass as a standalone) |
| LL-31 | pass (post2 Stage 2 already decomposed US-state artifact mix — must be cited) | pass | key number "largest gradient among 32 shares" is a max-over-grid with no null (B3-17's own defect); 536-subregion MDE is unusable (no income/AUI outside US) | **PASS WITH CORRECTIONS** |
| LL-36 | pass on R2-09; SWE-11/-14 are not addressed by the design | pass | "narrower ⇒ leading edge" inference not licensed by a concentration statistic | **PASS WITH CORRECTIONS** |
| LL-39 | pass | pass | key number compares pp with years and hours; tiers are magnitude-defined, so "breaking" cannot fail; Cowork enters the Claude.ai population and R6A claim 7 changes classifier input for every facet, so collaboration is not a clean control | **PASS WITH CORRECTIONS** (re-scores to the line) |

Counts: PASS 1 · WITH CORRECTIONS 6 · FAIL 3.

## Scoring audit — DEFENSIBLE WITH CORRECTIONS

Rubric order and arithmetic hold; "fixed before scoring" is not verifiable from a single commit. FOUND was applied inconsistently: LL-07, LL-12, LL-18 score 4 for joining a file shipped inside a release, while LL-16, LL-31, LL-36 score 5 for the same kind of join. Re-scores (ORG·FIT·FOUND·FEAS·TEACH·RISK; ≥2 differences and cut-line movers in bold):

| ID | lead | referee | Σ lead → ref | note |
|---|---|---|---|---|
| LL-07 | 5·5·4·5·5·4 | 5·5·4·5·5·4 | 28 → 28 | MDE must use effective N under usage weights |
| LL-11 | 5·5·5·5·5·3 | 5·5·5·5·5·2 | 28 → 27 | shares-not-levels + Super Bowl |
| LL-09 | 5·4·5·5·5·3 | 5·4·5·4·5·2 | 27 → 25 | IV not runnable; three named biases |
| LL-31 | 5·4·5·5·4·4 | 5·4·**4**·5·4·3 | 27 → 25 | FOUND anchor; 32-way max |
| LL-36 | 4·5·5·5·4·4 | 4·5·**4**·5·4·4 | 27 → 26 | FOUND anchor |
| LL-01 | 5·5·5·4·4·3 | **1**·5·5·4·**2**·3 | **26 → 20** | done in post1 |
| LL-22 | 5·4·5·3·5·4 | **2**·4·5·3·**3**·4 | **26 → 21** | done in post2; numbers in atlas |
| LL-39 | 5·4·5·4·5·3 | 5·4·5·4·**3**·2 | **26 → 23** | TEACH 3 (a measurement, no attribution); RISK 2 |
| LL-02 | 4·4·5·4·5·3 | **3**·4·5·4·**3**·3 | **25 → 22** | closest answer misdescribed; gloss confirmed |
| LL-18 | 5·4·4·5·4·3 | 5·4·4·5·4·3 | 25 → 25 | agree |
| LL-12 | 4·4·4·5·4·4 | 4·4·4·5·4·4 | 25 → 25 | agree; first replacement |
| LL-16 | 5·4·5·4·4·3 | 5·4·**4**·4·4·3 | 25 → 24 | FOUND anchor; steward already computed the gap figures |
| LL-24 | 5·5·3·3·5·3 | 5·5·3·3·5·3 | 24 → 24 | refusal to promote was right under the rubric |
| LL-37 | 5·5·4·3·5·2 | 5·5·4·3·**3**·2 | 24 → 22 | no outcome series → TEACH 3 |

Cut-line effect: LL-01, LL-22, LL-02 out; LL-39 at the line. LL-12 (25) enters on score. LL-16 falls to 24 and loses the stated tie-break (TEACH 4) to LL-24/LL-30/LL-37 (TEACH 5, FEAS 3); FOUND then drops LL-24 (3); LL-30 and LL-37 tie at 4 — the lead reruns the diversity step, noting LL-37's binding defect. LL-19/LL-26: FEAS 2 stands; LL-19's null branch is a data note, not a post.

## Inherited framing

**LL-01** re-dresses post1's secondary result (question, key number, wave). **LL-22** re-dresses post2's H1 (question, headline comparison, reporting rule) and is the companion post2 announced. LL-31's US-state leg overlaps post2 Stage 2; LL-18 is bounded by post1's finding that low-AUI user bases are professional — both must cite, not inherit.

## Not-both pairs

Pairs 1–5 are right; 1 and 3 dissolve if LL-01/LL-22 fall. Missing: **LL-18/LL-31** (soft — same shape as pair 3); **LL-09/LL-11** (shared outcome: Nov→Feb Claude.ai task-share change, same Super Bowl exposure); **LL-07/LL-36** (shared task→SOC construction and multi-holder rule — whichever is written first states it); **LL-12/LL-36** if LL-12 enters (global `onet_task` concentration frames).

## Corrections (owner: lead)

| # | ID | Correction |
|---|---|---|
| 1 | all | Fix LL-01 header Σ; LL-18 "Log (f) 5"; restore `"` in LL-36's quoted line or mark the substitution. |
| 2 | LL-07 | State effective N (Kish) under usage weights beside the 2,617-task MDE; state that a task's automation share is on the five-pattern base with `none` reported. |
| 3 | LL-09 | Replace the split-sample IV with a design the aggregates allow (Aug-2025 share as instrument; Aug→Nov as placebo growth). Flag the Feb-2026 Super Bowl inflow (R5) as a composition shock on the outcome. Cite R4-37/R5-29 as the gap; R4-25 only as the criterion the design approximates. |
| 4 | LL-11 | Same Super Bowl flag; reproduce R5 p.7 "+14% API / −18% Claude.ai" before the correlation (criterion 3). |
| 5 | LL-18 | State that country `onet_task` covers ~30% of a country's conversations (atlas e-2), so the task-mix adjustment is partial; state the 2026 count base (per million); write the holds-branch contribution composition-safe (who Claude's users are in low-adoption countries); cite post1's professional-user-base finding as a bounding result. |
| 6 | LL-31 | Pre-specify the primary outcomes (R6's three artifact groupings, or ≤4 named shares) and a permutation null for any max-over-32 statistic; delete the 536-subregion MDE sentence (no income/AUI outside US; state leg is 51 with AUI); cite post2 Stage 2; state the both-month and 0.5-floor rules yourself; run April–May agreement as the noise check. |
| 7 | LL-36 | Rest the gap on R2-09; say SWE-11/-14 are touched, not addressed. Restate the holds branch: a rising top-ten share is "concentration", with casualisation named as the rival to "leading edge". Reproduce R5 p.7's relative changes first. |
| 8 | LL-39 | Define a unit-free key number (each metric's Feb→Apr/May move ÷ its Nov→Feb move on the fixed instrument, and ÷ its Apr→May move). Classify metrics ex ante by documented instrument change (R6A claims 1, 2, 3, 6, 7), not by observed magnitude. State that Cowork enters the Claude.ai population and that claim 7 changes classifier input for every facet, so collaboration is a control only for the label set. |
| 9 | LL-02 | If retained: rewrite the closest-answer paragraph (SCPA pp.27–28 sentence; Table 2); drop "nobody has put the two numbers on one page"; define the rule for 0.511 vs 0.50; state the Claude.ai June break. Re-grade SCPA-24/SCEX-25 or acknowledge their answer columns already hold the key number. |
| 10 | pairs | Add the four pairs above to §5. |

## Questions to the steward

None; every cut was settled from the atlas.
