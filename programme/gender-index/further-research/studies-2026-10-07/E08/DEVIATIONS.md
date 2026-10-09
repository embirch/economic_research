# E08 execution deviations

Protocol copied from the reviewed 7 October 2026 selected-studies plan. Prior outcome inspection is disclosed there. Record new changes below with reason, affected target, and whether the result was seen.

| Date | Type | Change or finding | Why and effect |
|---|---|---|---|
| 2026-10-07 | Implementation repair before estimates | Schema validator initially expected numeric age/education codes; pinned SAS source contains character codes | Corrected exact expected storage types before a completed run. No response recode, exclusion, sample change or estimand change. |
| 2026-10-07 | Release-rule application after results | Suppressed Men+ user very-difficult time-off category (F); companion difficult category also suppressed | Prevents reconstruction from the combined binary outcome. Conservative event-count quality safeguard and complementary suppression implement frozen release rules. Binary outcome and all internal computations unchanged. |
| 2026-10-07 | Warning application after results | Both Men+ daily-work frequency shares and Women+ user very-difficult time-off share carry E warnings | Source counts support use with caution. Values retained with pointwise uncertainty; not selected according to estimated signs. |
| 2026-10-07 | Presentation change | Full unpaid-work frequency distribution supplied as 20 ordered dot-and-interval rows rather than four stacked bars | Coordinator's native figure specification accepts dots and makes all pointwise intervals visible. Same five categories and four populations; no analytic change. |
| 2026-10-07 | Literature update | Newly located October 2025 Jiang conference draft read in relevant sections; latest February 2026 full text still inaccessible. Accessible Dillon primary paper provides contrasting randomized evidence | Narrows novelty and interpretation, without altering estimates or study selection. Reading depths and version discrepancy retained in literature-review.md. |
| 2026-10-07 | Formatting repair | Decimal half-up rounding and normalized displayed negative zero | Aligns public outputs with guide §9.1. Estimates and uncertainty remain unrounded internally. |
| 2026-10-07 | Integration clarification | Exact unweighted respondent counts retained; axis states the Women+-minus-Men+ comparison explicitly | Coordinator withdrew a proposed sample-count rounding after source-rule clarification. Guide §9.1's estimated-count rounding is not misapplied to sample metadata. |

No new outcome, subgroup search, covariate, threshold, link function, geography or wave analysis was added. Both original main-support targets and the failed age-saturated diagnostic were executed. Native numerical review remains a separate check; author review precedes any new manuscript review. External spend is $0.
