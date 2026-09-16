# What went wrong in single-session research, 15 September 2026, and what the team must guard against

Written from the post 1 and post 2 sessions before designing the managed-agent team. Each lesson names the failure, its cause, and the structural fix a team should build in.

## 1. The question drifted with the numbers
Post 1 began as "culture or cohort", became "income", then "education", then "human capital", each retitle driven by the latest striking coefficient. The original intent (explain what drives the country gap, add an original contribution) was recovered only when Emily forced a step back.
**Cause:** the same context that ran the analysis also judged it, and each new number reset the frame.
**Fix:** the brief, the contribution statement and the "why it matters" are written by one agent and frozen before analysis; the director checks every write-up against them; the analyst never retitles.

## 2. Hidden assumptions were raised by Emily, not by the researcher
Selection of Claude's users within countries; the impossibility of unbundling education from income and connectivity; occupation inferred from tasks rather than users. Each was known (Anthropic's own reports say the first two) and each was left out of the framing until she asked.
**Cause:** the assumptions sweep existed as a rule but had no owner and no gate.
**Fix:** a named QC step before the pre-registration and again before the write-up, with the four-item sweep (value judgement; construct mapping; composition or selection; Anthropic's own results that cut against) as a required artifact, not a habit.

## 3. Pre-registered rules were mis-specified twice
The state-test rule keyed to a full model whose MDE was 6.8; the place rule residualised on one predictor before testing a correlated one. Both had to be overridden and admitted.
**Cause:** the pre-registration was written by the analyst in a hurry, with no second reader.
**Fix:** QC reviews every decision rule for power and specification before it is committed; the rule must state its expected MDE.

## 4. Overclaiming in the opening
"Adoption adds nothing at all" when it keeps a fifth; "education" when the bundle cannot be separated.
**Cause:** the write-up was drafted from memory of results rather than from the verified numbers, and the editor was the analyst.
**Fix:** the editor writes only from the results file and the QC-approved claims list; every quantitative sentence maps to a number in an output file; a script checks the page against the JSON outputs before release (this worked when used).

## 5. Too many threads
Nineteen exploratory scripts and a 6,500-word post nobody could follow.
**Cause:** exploration and writing were the same activity; each result begged the next.
**Fix:** the director sets a fixed budget of confirmatory tests per post and a separate exploratory allowance; anything beyond goes to a drawer or the next post's idea list.

## 6. Data facts were assumed, then discovered
The June release has no request-by-occupation cross; Nov/Feb state rows exist under a different label; the August state occupation table is 74% unclassified; Census API now needs a key; BLS blocks curl; Anthropic's "1% increase in share" means one percentage point; the Gini is unweighted.
**Cause:** no single owner of the data, and the audit lived in scattered notes.
**Fix:** a data agent that owns a living data dictionary (what exists, at what grain, with what thresholds and conventions, and what each published number's exact specification is) and answers feasibility questions before a brief is approved.

## 7. Small samples produced confident stories
Utah's abuse-flagged row; Wyoming's swings; half of one month's state outliers gone the next.
**Cause:** no standing noise check.
**Fix:** persistence across independent windows and leave-one-out are required for any geographic claim; flagged units are excluded by rule.

## 8. Context loss between sessions
Work resumed from summaries; generators were lost and rebuilt; the same checks were re-derived.
**Cause:** everything lived in one conversation.
**Fix:** every artifact (brief, prereg, data dictionary, notebook, results JSON, page) is a file in a git repository; agents read from files, not from chat; the memory store holds only durable lessons and conventions.

## 9. The human was the quality control
Emily caught the framing errors, the assumptions, and the loss of intent.
**Cause:** no independent reviewer in the loop.
**Fix:** a QC agent with an adversarial brief and no stake in the result, plus explicit human checkpoints at brief approval, pre-registration, and final draft.

## What worked and must be kept
Exact replication with Anthropic's own code before anything new; check blocks that stop on a wrong number; two implementations of every key number; MDE with every null; the lab notebook with dated deviations; the red-team memo; programmatic verification of the page against outputs; pre-registration by git commit; the drawer structure for evidence; the nine rules.
