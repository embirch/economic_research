# Review of PIECE_1_RESEARCH_BRIEF v1.0 · 21 September 2026

Reviewed with the team's four lenses (referee, steward, lead, editor) against the programme's gates and standards (`economic_research/.claude/skills/qc-rubric`, `empirical-standards`, `wiki/style/STYLE-GUIDE.md`) and against the data itself (`gender_ai_audit/raw/isoc_ai_iaiu_Data.csv`, 37,885 rows). Numbers marked ⟨inspected⟩ were read from the extract during this review and are declared as such; the revised brief carries the same declaration.

## Verdict

**PASS WITH CHANGES: four items to fix before pre-registration, nine should-items, five could-items.** The brief is unusually careful about measurement, denominators, flags and what cannot be claimed. It is weak where the programme's first gate is strictest: it does not say why the answer matters, it pre-states no expectations, and it has no rule for what "largest" means once noise is taken seriously. Those are the same three faults the team's first post had at its brief stage, and the fixes are the same.

## Blocking items

**1. The why-it-matters is one sentence and is disconnected from the central agenda.** §1 says "unequal participation in an increasingly relevant technology." The agenda this post opens is "how gender differences in AI exposure, adoption and workplace conditions translate into differences in economic opportunity." The brief must state the link explicitly: participation is the first step of that chain; the returns to AI skills are already priced (the work in this area reports a wage premium for demonstrable AI skills), and Anthropic's own exposure and productivity measures are wage-blind and sex-blind. Then it must say what each pattern would change:

- a gap concentrated in **work use among 25–54-year-olds** is a labour-market gap, and the opportunity story follows;
- a gap **absent at 16–24 and present from 25** is a life-cycle or workplace pattern, not a cohort that will age out;
- a gap in **private use only** is a consumption gap, with different implications;
- a **reversed gap in education use** is a schooling channel running the other way.

Two readers, as in every post: a person asking whether AI is arriving unequally in women's lives and work, and an analyst deciding which number to put into an exposure or opportunity model.

**2. No hypotheses, no signatures, no decision rules.** A descriptive post still pre-states what it expects and what would count against it, because otherwise the write-up is chosen after the results. Three are available from the literature and from the audit's own inspection: (H-work) the gap is larger in work use than in private use; (H-age) the gap is smallest or reversed at 16–24 and largest at 25–44; (H-education) the gap widens with education. Each with the pattern that would refute it. The revised brief adds them, and labels the EU-level values already seen as inspected.

**3. "Largest" has no rule that survives noise.** The programme's second post found half of single-window rankings were noise. With no standard errors, a country-by-age heatmap of gaps of a few points is mostly sampling error (see item 5). The brief needs a persistence rule: a country is classed as large-gap only if it sits in the top tercile on the signed pp gap, on the ratio, and after age standardisation, on unflagged cells; small-gap likewise; everything else is "not distinguishable". The post then reports how many countries change class between measures, which is RQ2's answer in one number.

**4. Contribution per outcome and the close are missing.** The brief says what it will do, not what a reader learns under each result. The revised brief adds the three-branch contribution (holds, fails, null) and a close written for each outcome, as the team's §12 does.

## Should items

**5. Approximate uncertainty is obtainable and should be used, labelled as a bound.** The brief rightly refuses to invent confidence intervals. But Eurostat's metadata states the survey covered about 330,000 individuals in the EU in 2025 and that national sample characteristics are in the national metadata files. With a national n and a simple-random-sampling assumption, a binomial standard error is a lower bound on the true one (design effects only widen it). Order of magnitude, for the reader to judge: a country with 2,000 respondents per sex at a 33% rate has a standard error of about 1.1 points on each rate and 1.5 on the gap, so gaps below about 3 points are inside noise; an age band with 350 respondents per sex has a gap standard error near 4 points, so most country-by-age gaps are. The steward's task is to fetch the national sample sizes; the rule is: publish the bound with the assumption named, never as a survey interval.

**6. Age weights are secured.** Eurostat's API served `demo_pjan` for EU27_2020, 2025, by single age and sex today (status flag `ep`, estimated and provisional). Use population on 1 January 2025, sex-pooled, six bands, and disclose that the survey's household population differs from the resident population.

**7. Literature: the closest comparators are now identified and the novelty holds, narrowly.** Eurostat's own article gives gender only at EU level (35% vs 30%). Henseke (2026, EWCS 2024, 35 countries) reports a 4.1-point work-adoption gap among workers, concentrated in the most exposed occupations. Di Pietro (2026, Flash Eurobarometer 2024, 27 countries) finds young men more likely to use AI applications, with young women higher for schoolwork and research, by decomposition. Otis and co-authors (Harvard, meta-analysis of 143,000 people) put the gap at about 25% of the male rate. Pew (June 2026, US) reports convergence in ever-use to 50% vs 47% with persisting gaps in daily use and work use. Stephany and Duszynski (UK) attribute women's lower uptake to societal-risk perception. None publishes the 2025 Eurostat gender gap by country, by age band or by purpose, and none tests its sensitivity to composition and measurement. That is the contribution, and the brief should say it in those words and cite these six.

**8. Two cheap triangulation legs are available and the standards prefer one claim at two levels.** OpenAI Signals publishes the feminine share of messages by country and month; 26 of the EU27 have June 2025. It is a different construct (message share by name-inferred gender, consumer ChatGPT), which is exactly why agreement or disagreement of the country ordering is informative. Henseke's work-adoption gaps are the second leg for the work-use dimension. Both as sensitivity, neither as headline.

**9. Declare what was inspected.** The audit and this review have seen: the EU purpose gaps (4.5 / 5.5 / 3.0 / 0.05 points); the EU age profile of the gap (−1.7 at 16–24, then 4.7, 4.8, 2.8, 4.2, 4.1) ⟨inspected⟩; the EU education profile (3.8, 4.6, 7.0) ⟨inspected⟩; the country distribution of the overall gap (median 4.0, range −3.8 to +9.3, six of 36 geographies reversed: North Macedonia, Malta, Estonia, Slovenia, Lithuania, Croatia) ⟨inspected⟩; and that 33 of 36 geographies have all twelve unflagged sex-by-age cells (Ireland, North Macedonia and Serbia do not) ⟨inspected⟩. The brief must list these, and the hypotheses must be judged against the country-level and purpose-by-age results that have not been seen.

**10. Sex by employment and by occupation do not exist in the extract.** The group list carries employment and ISCO groups without a sex prefix. The brief says the employed denominator is unverified; it is absent, and the brief should say so and drop the caveat about it.

**11. The internet-user denominator is a composition test, not just a check.** Among 65–74-year-olds the sex gap in recent internet use is itself a gap; comparing the all-individual and internet-user gaps by age says how much of the AI gap is an internet gap. Promote it from "secondary check" to a named sensitivity with an interpretation.

**12. Education is not standardisable, and the brief should say why.** No sex-by-age-by-education cells exist, so age standardisation within education is impossible; the education profile is reported crude with that limit named.

**13. Name the assumptions sweep.** Value judgement (a gap is not a deficit; purposes differ); construct (recent use in three months, generative AI as the questionnaire defines it, not intensity); composition (age, internet use, education); what the literature already shows that cuts against (Pew's convergence; Di Pietro's reversed schooling gap). Four lines in the brief, as the rubric requires.

## Could items

14. The title should carry the contribution: "Where is the gender gap in generative AI use widest, and how much of that is measurement?"
15. Report the EU aggregate as a population-weighted mean and say that Germany, France, Italy and Spain drive it.
16. Present ties and near-ties as a band, not a rank; the figure sorts but the text does not rank.
17. Keep the non-use reasons table (`isoc_ai_iaiuxr`) out of this post, as the brief does, but say in the close that it is the next post.
18. State the fieldwork window (first quarter of 2025 by convention, so "recent use" is roughly December 2024 to March 2025 for most countries) rather than "the three months preceding the 2025 survey".

## Steward's data facts, confirmed today

- Extract: 37,885 published cells, 2025 only, 35 geographies plus EU27_2020, 104 group codes, flags `u` on 6,699 cells, no other flag; no 2024 wave exists (questions first asked in 2025).
- Indicators and units as the brief lists them; purposes are multi-select.
- Sex crosses exist only with age and with education; not with employment, occupation, income or urbanisation.
- Age weights: `demo_pjan` served by the Eurostat API for EU27_2020, 2025, by single age and sex (provisional).
- Uncertainty: no cell-level standard errors; national sample sizes to be fetched from national reference metadata; the EU total is about 330,000 individuals.
- Triangulation: OpenAI Signals gender by country by month covers all EU27, 26 with June 2025.

## Process recommendation

This post is not built on the Anthropic Economic Index, so the team's data skill does not apply, but everything else does: the gates, the pre-registration template, the referee's review procedure, the claims-list boundary, the page builder and the style corpus. The cheapest sound route is: fix the brief here (done below as v1.1), pre-register from it, then run the referee agent once on the pre-registration in a direct session (the referee's brief and pre-registration reviews caught the decisive faults in post 1 and cost under $20 each), and use the steward for the national sample sizes and the age-weight file. The analysis itself is small enough to run locally.
