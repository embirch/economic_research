# Pre-registration · Post 2 (outliers) · Where AI use is distinctive across US states, and why

**Written 15 September 2026, late evening, before steps 09–12 were run.** What had been seen: the persistence prototype (April vs May 2026, request level 1, 53 clusters with ≥ 0.5% of national use, 51 states): 49 and 55 cells at ≥ 1.6× the national share, 22 in both months, month-to-month correlation of log distinctiveness 0.62; the list of the 22 (West Virginia fiction/companionship/gaming/media; Maine, Nebraska, Wisconsin outdoor and garden; Hawaii destination research; DC editing, self-presentation writing, research and evidence; Mississippi, Arkansas, Alabama, New Mexico fiction writing; Alaska, Kansas gaming; Iowa science; Mississippi formatted writing and instructional design; Oklahoma, Kentucky media discovery). No regression has been run on any of it.

## Definitions, fixed
Distinctiveness D(s, c) = state share of level-1 request cluster c ÷ US share of c, in April and in May 2026 separately; clusters with ≥ 0.5% of US use in the month. Outlier: D ≥ 1.6. Persistent: outlier in both months. Utah excluded from every model. Leisure clusters, fixed now: Fiction writing; Gaming; Companionship and conversation; Media discovery. All models: 50 states, HC3, MDE = 2.8 × SE, at most two predictors.

## H1 noise (step 09)
Recurrence rate = persistent ÷ (April outliers). Regress an indicator of recurrence on the state's log May usage share across April outlier cells (logit or linear). **Rule:** H1 holds if recurrence < 60% overall and rises with usage share (coefficient positive, interval excluding zero). Report also the state-level count of persistent outliers against usage.

## H2 the hobbyist signature (step 10)
For each of the four leisure clusters: log D on log Usage Index (model a) and on log Usage Index + personal-use share (model b), each month. **Rule:** a cluster "passes" if the index coefficient is negative with interval excluding zero and |coef| ≥ MDE in model (a) in both months. The signature "holds" if ≥ 3 of 4 clusters pass. Report whether personal share absorbs the index in (b).

## H3 the place in the request (step 11)
Persistent non-leisure outlier clusters and their pre-stated covariate (one each, all from ACS 2023 summary tables unless noted):
- Outdoor and garden → share of employed in agriculture, forestry, fishing and hunting (C24030), with a fallback note that a rural-share table may be unavailable.
- Destination research → share of employed in arts, entertainment, recreation, accommodation and food services (C24030).
- Editing and rewriting; Self-presentation writing; Research and evidence → share of employed in public administration (C24030).
- Instructional design; Science; Formatted writing → share of the population enrolled in college or graduate school (B14001).
Model: log D on the covariate (standardised), then with log Usage Index added; each month. **Rule:** an outlier is "explained" if the covariate's coefficient is positive with interval excluding zero and ≥ MDE in the one-predictor model in both months. Otherwise "unexplained by the stated mechanism," and no other story is substituted.

## H4 real after jobs (step 12)
For each persistent cluster: log D on the state's user occupation shares for the three groups most related to it (fixed: Fiction writing → Arts/Design/Media; Gaming → Computer & Mathematical, Arts; Science → Life/Physical/Social Science; Editing/Self-presentation/Research → Management, Business, Office; Outdoor → Farming; Destination → Sales, Personal care; Instructional design → Education). **Rule:** the outlier is "composition" if the occupation shares explain R² ≥ 0.5 of its distinctiveness across states in both months; otherwise "not composition."

## Robustness
Outlier threshold 1.5 and 2.0; level-0 clusters where published; without DC; recurrence by state size tercile.

## Deviations
Logged in notes/lab-notebook.md with date and reason.
