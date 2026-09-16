# Labor market impacts of AI: A new measure and early evidence

## Source

- **Slug:** `labor-market-impacts-2026-03`
- **Title:** "Labor market impacts of AI: A new measure and early evidence"
- **Type:** paper (Economics team; the paper calls itself both a "paper" (PDF p.3) and "This report" (PDF p.13), and the PDF's acknowledgements call it "this note" (PDF p.1) where the page's say "this report")
- **Authors:** Maxim Massenkoff and Peter McCrory (PDF p.1)
- **Published:** 5 March 2026 (PDF p.1: "Published March 5, 2026"; page dateline "Mar 5, 2026")
- **Corrected:** the page carries a Corrections block absent from the PDF — "Updated Mar 8, 2026: Corrected Figure 7, which incorrectly reversed the labels between top quartile and zero exposure group inflow rates."
- **Primary URL:** https://www.anthropic.com/research/labor-market-impacts
- **PDF:** https://cdn.sanity.io/files/4zrzovbb/website/2b5bbaf2c1eb81dbf6e6fb813c1a24e35a64d376.pdf (17 pp; pp.1 cover, 2 key findings, 3–14 body, 15–16 footnotes, 16–17 references). An earlier PDF URL for the same document, https://cdn.sanity.io/files/4zrzovbb/website/a42bc3fc08283562f08fd8bdee8f6f9a3d506e87.pdf, also still resolves.
- **Separate appendix:** yes — PDF footnote 7 reads "Appendix available here", and the page's Appendix section reads "Available here". It is a separate 11-page document and is **not** summarised here; see `wiki/reports/labor-market-impacts-2026-03-appendix.md` (slug `labor-market-impacts-2026-03-appendix`). Wherever this file says a definition, threshold or robustness check "is in the Appendix", the content is deliberately left to that file.
- **Data availability (verbatim, PDF p.14):** "Observed coverage at the task and job level is available at: https://huggingface.co/datasets/Anthropic/EconomicIndex."
- **Acknowledged for feedback:** "Martha Gimbel, Anders Humlum, Evan Rose, and Nathan Wilmers" (PDF p.1).
- **Bibtex key:** `massenkoffmccrory2026labor` (PDF p.14).
- **Prior work it stands on:** the Anthropic Economic Index releases of August and November 2025 (footnote 5); Eloundou et al. (2023); O*NET; BLS Employment Projections 2024–2034; the Current Population Survey.
- **Terms it introduces into the Anthropic vocabulary:** observed exposure, observed coverage, task coverage, job coverage, covered task, the zero-exposure group, time fraction measure, job start rate / job finding rate, "Great Recession for white-collar workers", "separate signal from noise".

### Differences between the page and the PDF (recorded because quotations must be reproducible)

| Location | PDF | Page |
|---|---|---|
| p.5, first use | "Our new measure, **Observed Exposure**, is meant to quantify" | "Our new measure, **observed exposure**, is meant to quantify" |
| p.12 scenario | "If all workers within the top 10% **of coverage** were laid off" | "If all workers within the top 10% were laid off" |
| p.12, Figure 7 lead-in | "Figure 7 shows the monthly **job start rate**" | "Figure 7 shows the monthly **job finding rate**" |
| Figure 4 caption | "The small **squares** mark individual example occupations" | "The small **diamonds** mark individual example occupations" |
| Footnote on robustness | "In **ni** extension do we find clear impacts on exposed jobs." (typo) | "In **no** extension do we find clear impacts on exposed jobs." |
| Footnote numbering | 11 footnotes; fn 7 = "Appendix available here" | 10 footnotes; the appendix footnote is dropped and later numbers shift down by one |
| Acknowledgements | omits Kim Withee; "feedback on earlier versions of this **note**" | includes Kim Withee; "feedback on earlier versions of this **report**" |
| Corrections | none | Figure 7 correction dated Mar 8, 2026 |

Footnote numbers cited below are **the PDF's**.

## Claims

Numbers are reproduced as published. Every claim names the comparison it rests on, because in this paper almost nothing is a level: it is a gap between two groups, two measures, or two dates.

1. **Observed exposure is a composite, not a capability score.** "We introduce a new measure of AI displacement risk, observed exposure, that combines theoretical LLM capability and real-world usage data, weighting automated (rather than augmentative) and work-related uses more heavily" (key findings, PDF p.2). *Comparison:* theoretical capability (Eloundou β) against realised, work-related, automated Claude usage.

2. **Usage is concentrated on theoretically feasible tasks.** "Tasks rated β=1 (fully feasible for an LLM alone) account for 68% of observed Claude usage, while tasks rated β=0 (not feasible) account for just 3%" (Figure 1 caption, PDF p.4). *Comparison:* share of Claude usage across the three β bins.

3. **97% of observed tasks are theoretically feasible.** "97% of the tasks observed across the previous four Economic Index reports fall into categories rated as theoretically feasible by Eloundou et al. (β=0.5 or β=1.0)" (PDF p.5, referring to Figure 1). *Comparison:* observed task set against the β=0.5/1.0 categories. Note the denominator: Figure 1 and this claim use **four** Economic Index reports, while the exposure measure itself uses **two** datasets (footnote 5) — see "What it did not test".

4. **Theoretical capability is high in the two most clerical/technical categories.** "the β measure shows scope for LLM penetration in the majority of tasks in Computer & Math (94%) and Office & Admin (90%) occupations" (PDF p.7, Figure 2). *Comparison:* employment-weighted category averages of β.

5. **Realised coverage is a fraction of capability — the paper's headline gap.** "Claude currently covers just 33% of all tasks in the Computer & Math category" (PDF p.7, Figure 2), against the 94% theoretical figure in claim 4. *Comparison:* red area (observed) against blue area (theoretical) in Figure 2, by occupational category. The key-finding form is "AI is far from reaching its theoretical capability: actual coverage remains a fraction of what's feasible" (PDF p.2).

6. **Most exposed occupation: Computer Programmers at 75%.** "Computer Programmers are at the top, with 75% coverage, followed by Customer Service Representatives, whose main tasks we increasingly see in first-party API traffic" (PDF pp.7–8, Figure 3). *Comparison:* ranking of occupations on the time-weighted coverage measure.

7. **Data Entry Keyers at 67%.** "Data Entry Keyers, whose primary task of reading source documents and entering data sees significant automation, are 67% covered" (PDF p.8, Figure 3). *Comparison:* same ranking. Only three of the ten occupations in Figure 3 are named in the text; the remaining seven are legible only in the figure image.

8. **Financial analysts are among the most exposed.** "We find that computer programmers, customer service representatives, and financial analysts are among the most exposed" (Discussion, PDF p.14). *Comparison:* same ranking. Financial analysts appear only here, not in the Figure 3 paragraph.

9. **Thirty per cent of workers have no measured exposure at all.** "At the bottom end, 30% of workers have zero coverage, as their tasks appeared too infrequently in our data to meet the minimum threshold. This group includes, for example, Cooks, Motorcycle Mechanics, Lifeguards, Bartenders, Dishwashers, and Dressing Room Attendants" (PDF p.8). *Comparison:* employment share below the usage gate versus above it. This group becomes the control group for every later result.

10. **Exposure predicts weaker official growth forecasts, slightly.** "For every 10 percentage point increase in coverage, the BLS's growth projection drops by 0.6 percentage points" (PDF p.9, Figure 4). *Comparison:* occupation-level regression of BLS 2024–2034 projected employment change on observed exposure, weighted by current employment; binned scatter with 25 equally sized bins (Figure 4 caption, PDF p.8). The paper's own gloss: "This provides some validation in that our measures track the independently derived estimates from labor market analysts, although the relationship is slight."

11. **The composite beats its own capability input on this test.** "Interestingly, there is no such correlation using the Eloundou et al. measure alone" (PDF p.9). *Comparison:* observed exposure versus β alone, both against BLS projections. The paper marks this "Interestingly" and does not explain it.

12. **Exposed workers were already advantaged before ChatGPT.** "The more exposed group is 16 percentage points more likely to be female, 11 percentage points more likely to be white, and almost twice as likely to be Asian. They earn 47% more, on average, and have higher levels of education. For example, people with graduate degrees are 4.5% of the unexposed group, but 17.4% of the most exposed group, an almost fourfold difference" (PDF p.9, Figure 5). *Comparison:* CPS respondents in the top quartile of exposure versus the 30% with zero exposure, August–October 2022, i.e. "the three months before ChatGPT was released". The key finding also says exposed workers are "older" (PDF p.2); no age number appears in the text, so that rests on Figure 5, which is an image.

13. **No detectable differential rise in unemployment.** "The average change in the gap since the release of ChatGPT is small and insignificant, suggesting that the unemployment rate of the more exposed group has increased slightly but the effect is indistinguishable from zero" (PDF p.11, Figure 6). *Comparison:* difference-in-differences on the unemployment-rate gap between the top exposure quartile and the zero-exposure group, CPS monthly series since 2016, ChatGPT release as the break. Stated as a key finding: "We find no systematic increase in unemployment for highly exposed workers since late 2022" (PDF p.2).

14. **COVID moved the two groups in the opposite direction to the AI hypothesis.** "During COVID, the less AI-exposed workers—who are more likely to have in-person jobs—saw a much larger increase in unemployment. Since then, the trends have been largely similar between the two groups" (PDF p.11, Figure 6 upper panel). *Comparison:* the same two groups, pre- and post-2020.

15. **Stated power of the design: about one percentage point.** "Based on the confidence interval of the pooled estimate, differential increases in unemployment on the order of 1 percentage point would be detectable (this will change as new data comes in, so it is merely a ballpark estimate)" (PDF p.12). *Comparison:* the confidence interval of the pooled post-ChatGPT DiD estimate against hypothesised effect sizes. This is the paper's own MDE statement.

16. **Benchmark scenario, mass layoff.** "If all workers within the top 10% of coverage were laid off, it would increase unemployment within the top quartile group from 3% to 43%, and it would increase aggregate unemployment from 4% to 13%" (PDF p.12). *Comparison:* counterfactual arithmetic against the observed 3% (top quartile) and 4% (aggregate) baselines.

17. **Benchmark scenario, white-collar recession.** "During the 2007-2009 Great Recession, unemployment rates doubled from 5% to 10% in the US. Such a doubling in the top quartile of exposure would increase its unemployment rate from 3% to 6%. This should be visible in our analysis as well" (PDF p.12). *Comparison:* the Great Recession's doubling applied to the exposed group's 3% base, against the ~1pp detectability threshold of claim 15.

18. **Youth unemployment in exposed occupations is flat, but hiring is not.** "We find that the unemployment rate for young workers in the exposed occupations is flat (see Appendix)" (PDF p.12). *Comparison:* young workers (22–25) in exposed versus unexposed occupations; the supporting figure is in the appendix, not here.

19. **Hiring of 22–25s into exposed occupations has slowed.** "Job finding rates at the less exposed occupations remain stable at 2% per month, while entry into the most exposed jobs decreases by about half a percentage point. The averaged estimate in the post-ChatGPT era is a 14% drop in the job finding rate compared to that in 2022 in the exposed occupations, although this is just barely statistically significant. (There is no such decrease for workers older than 25.)" (PDF pp.12–13, Figure 7). *Comparison:* monthly job-start rate for 22–25-year-olds entering high- versus zero-exposure occupations, DiD against 2022; and 22–25s against over-25s. "Apart from some large swings in 2020-2021, these series visually diverge in 2024" (PDF p.12). The page's Corrections note says Figure 7's group labels were reversed until 8 March 2026.

20. **The external comparator.** "Brynjolfsson et al. report a 6–16% fall in employment in exposed occupations among workers aged 22 to 25. They attribute this decrease primarily to a slowdown in hiring rather than an increase in separations" (PDF p.12). Footnote 10 explains the range: "The 6 percentage point drop compares to a counterfactual of flat employment growth. The 16 percentage point estimate comes from a design comparing similar workers in the same firm with different occupations." *Comparison:* this paper's CPS result against Brynjolfsson et al.'s ADP payroll result — the paper reports its own finding as echoing theirs.

21. **Robustness, as reported in the main text.** Footnote 9: "First, we ask whether the percentile cutoff that we use to define treatment matters, varying it from the median to the 95th percentile. In all cases, the impact is flat or negative (meaning that unemployment decreases for the exposed group). Next, we focus on young workers in particular, those aged 22 to 25 as in Brynjolfsson et al. (2025). Finally, we use data on unemployment insurance claimants from the Department of Labor to measure the unemployment, rather than CPS survey responses. In ni [no] extension do we find clear impacts on exposed jobs." *Comparison:* alternative treatment cutoffs, an alternative age window, and an administrative outcome against the CPS survey outcome. Footnote 6: "the Spearman (rank-rank) correlation of job exposure across many resolutions to these questions is exceedingly high." The numbers behind all of these are in the appendix.

22. **Historical humility, asserted as motivation not result.** "a prominent attempt to measure job offshorability identified roughly a quarter of US jobs as vulnerable, but a decade on, most of those jobs maintained healthy employment growth. The government's own occupational growth forecasts, while directionally correct, have added little predictive value beyond linear extrapolation of past trends" (PDF p.3). *Comparison:* past exposure measures against realised employment growth. Footnote 1 sources the forecast claim to Massenkoff (2025), the mentor's Occupational Outlook working paper.

23. **Scope claim about the framework itself.** "It is possible that the impacts of AI will be unmistakable. This framework is most useful when the effects are ambiguous—and could help identify the most vulnerable jobs before displacement is visible" (PDF p.3). *Comparison:* implicitly, COVID-style detectability against internet- or China-shock-style ambiguity (PDF pp.3–4).

## Definitions (verbatim)

All quotations below are the paper's own words. Where the main text defines something only qualitatively and defers the formula to the appendix, that is stated; the appendix's content belongs to `labor-market-impacts-2026-03-appendix.md`.

**Observed exposure — key-findings form (PDF p.2):**
> "We introduce a new measure of AI displacement risk, observed exposure, that combines theoretical LLM capability and real-world usage data, weighting automated (rather than augmentative) and work-related uses more heavily"

**Observed exposure — purpose (PDF p.5):**
> "Our new measure, Observed Exposure, is meant to quantify: of those tasks that LLMs could theoretically speed up, which are actually seeing automated usage in professional settings? Theoretical capability encompasses a much broader range of tasks. By tracking how that gap narrows, observed exposure provides insight into economic changes as they emerge."

(The page renders the same sentence with "observed exposure" in lower case.)

**What raises a job's exposure — the five qualitative conditions (PDF p.5):**
> "Our measure qualitatively captures several aspects of AI usage that we think are predictive of job impacts. A job's exposure is higher if:
> • Its tasks are theoretically possible with AI
> • Its tasks see significant usage in the Anthropic Economic Index⁵
> • Its tasks are performed in work-related contexts
> • It has a relatively higher share of automated use patterns or API implementation
> • Its AI-impacted tasks make up a larger share of the overall role⁶"

**The covered-task rule, i.e. the usage gate as stated in the main text (PDF p.6):**
> "We count tasks that are theoretically capable with an LLM as covered if they have seen sufficient work-related usage in Claude traffic."

The main text gives **no numeric threshold** for "sufficient". The only numeric consequence stated here is its effect: "their tasks appeared too infrequently in our data to meet the minimum threshold" (PDF p.8). The paper defers the formula — "We give mathematical details in the Appendix.⁷" (PDF p.6) — and footnote 6 lists the gate as an open judgement call: "What determines 'significant' use?" The numeric gate is in the appendix file.

**The automation weighting (the α weighting), as stated in the main text (PDF p.6):**
> "We then adjust for how the task is being carried out: fully automated implementations receive full weight, while augmentative use receives half weight."

The main text does not use the symbol α and gives no formula; the symbol and its construction are in the appendix.

**Aggregation from task to occupation (PDF p.6):**
> "Finally, the task-level coverage measures are averaged to the occupation level weighted by the fraction of time spent on each task."

**Aggregation from occupation to category (PDF p.7):**
> "We calculate this by first averaging to the occupation level weighting by our time fraction measure, then averaging to the occupation category weighting by total employment."

**Theoretical capability, β — the scale (PDF p.5):**
> "Eloundou et al.'s metric, β, scores tasks on a simple scale: 1 if a task can be doubled in speed by an LLM alone, 0.5 if it requires additional tools or software built on top of the LLM, and 0 otherwise.⁴"

**Theoretical capability, β — what the source measures (PDF p.4):**
> "Task-level exposure estimates from Eloundou et al. (2023), which measure whether it is theoretically possible for an LLM to make a task at least twice as fast."

**Theoretical capability, β — the three Eloundou categories (footnote 4, PDF p.15):**
> "In their framework, 'Directly exposed'' tasks were those that could be completed in half the time with an LLM (with a 2,000-word input limit and no access to recent facts). Tasks that were 'exposed with tools' were those subject to the same speedup with an LLM that had access to software for, e.g., information retrieval and image processing. Tasks that were not exposed could not have their duration reduced by 50% or more using an LLM."

**The task universe (PDF p.4):**
> "The O*NET database, which enumerates tasks associated with around 800 unique occupations in the US."

**The usage input and the near-duplicate-task rule (footnote 5, PDF p.15):**
> "We use the previous two Anthropic Economic Index datasets, covering usage from August and November 2025. For ONET tasks that are highly semantically similar, we split the counts across them."

**The zero-exposure group (PDF p.8):**
> "At the bottom end, 30% of workers have zero coverage, as their tasks appeared too infrequently in our data to meet the minimum threshold."

**Treatment definition (PDF p.11):**
> "With an eye toward simplicity, and noting that we are most concerned with large impacts, we center our analysis on the idea that impacts should be felt most in the groups with the highest mean exposure. We compare workers in the top quartile of time-weighted task coverage to those in the bottom."

**Priority outcome (PDF p.10):**
> "We focus on unemployment as our priority outcome because it most directly captures the potential for economic harm—a worker who is unemployed wants a job and has not yet found one. In this case, job postings and employment do not necessarily signal the need for policy responses; a decline in job postings for a highly exposed role may be counteracted by increased openings in a related one. Most harmful labor market developments of AI should arguably include a period of increased unemployment, as displaced workers search for alternatives. The Current Population Survey is well suited to tracking this, as unemployed respondents report their previous job and industry."

**Job start rate / job finding rate (PDF p.12):**
> "Figure 7 shows the monthly job start rate (i.e., when a worker reports a job that they did not have in the previous month) for young workers, split by whether they are entering a high- vs. low-exposure occupation."

(The page renders the same sentence as "the monthly job finding rate". The paper uses "job start rate" and "job finding rate" interchangeably; claim 19 quotes both.)

**Young workers (PDF p.12):** "young (22-25 year old) workers".

**Detectability / the paper's own MDE (PDF p.12):**
> "Based on the confidence interval of the pooled estimate, differential increases in unemployment on the order of 1 percentage point would be detectable (this will change as new data comes in, so it is merely a ballpark estimate)."

**What the core estimate is (PDF p.12):**
> "Note that our core estimate is based on differential changes in the unemployment rate in the exposed group compared to the less exposed group. If unemployment increased for all workers in parallel, we would not attribute this to AI advancements that still leave many tasks unaffected."

**Crosswalk (footnote 8, PDF p.16):**
> "To match O*NET-SOC codes to occ1990 codes in the CPS, we use the crosswalk provided by Eckhart and Goldschlag (2025)."

**The measure restated in the Discussion (PDF pp.13–14):**
> "Jobs are more exposed to AI to the extent that their tasks are theoretically feasible with LLMs and observed on our platforms in automated, work-related use cases."

**Figure captions, verbatim (these are the paper's construct definitions in miniature):**

- Figure 1 (PDF p.4): "Share of Claude usage by Eloundou et al. task exposure rating. This figure shows Claude usage distributed across O*NET tasks grouped by their theoretical AI exposure. Tasks rated β=1 (fully feasible for an LLM alone) account for 68% of observed Claude usage, while tasks rated β=0 (not feasible) account for just 3%. Data on Claude usage comes from the previous four Economic Index reports."
- Figure 2 (PDF p.6): "Theoretical capability and observed exposure by occupational category. This figure shows the share of job tasks that LLMs could theoretically perform (blue area) and our own job coverage measure derived from usage data (red area)."
- Figure 3 (PDF p.7): "Most exposed occupations. This figure shows the top ten most exposed occupations using our task coverage measure."
- Figure 4 (PDF p.8): "BLS projected employment growth from 2024–2034 vs. observed exposure. This is a binned scatterplot with 25 equally-sized bins. Each solid dot shows the average observed exposure and projected employment change for one of the bins. The dashed line shows a simple linear regression fit, weighted by current employment levels. The small squares mark individual example occupations for illustration." (Page: "small diamonds".)
- Figure 5 (PDF p.9): "Differences between high and low exposure workers, Current Population Survey. This table shows exposure, demographics, education, and labor market outcomes."
- Figure 6 (PDF p.11): "Trends in the unemployment rate for workers in the top quartile of observed exposure and no AI exposure, Current Population Survey. The top panel shows the unemployment rate for workers in the top quartile of exposure (red line) and the 30% of workers with zero exposure. The bottom panel measures the gap between these two series in a difference-in-differences framework."
- Figure 7 (PDF p.13): "New job starts among workers age 22-25 in occupations with high observed exposure and no AI exposure, Current Population Survey. The top panel shows the percent of young workers starting new jobs in high vs. no exposure occupations. The bottom panel measures the gap between these two series in a difference-in-differences framework."

## Data and methods

In the wiki author's words, with page references.

**Three inputs (PDF p.4).** O*NET supplies the task universe for around 800 US occupations and the time-fraction weights. The Anthropic Economic Index supplies realised usage. Eloundou et al. (2023) supplies theoretical capability β ∈ {0, 0.5, 1}. The Index input is specifically the **August and November 2025** datasets (footnote 5) — that is, the samples behind the September 2025 and January 2026 Economic Index reports. Figure 1, by contrast, is built from "the previous four Economic Index reports" (Figure 1 caption, PDF p.4), so the descriptive figure and the measure do not share a denominator.

**Building the measure (PDF pp.5–7).** A task enters as *covered* only if it clears two hurdles: β > 0 (theoretically feasible) and sufficient work-related Claude usage. Covered tasks are then weighted by how the work was done — full weight for fully automated implementations, half weight for augmentative use (PDF p.6) — which is the paper's way of saying that delegation is treated as more displacement-relevant than collaboration. Task-level coverage is averaged to the occupation using the fraction of time spent on each task, and occupation-level coverage is averaged to the SOC category weighting by total employment (PDF pp.6–7). Near-identical O*NET tasks have their usage counts split across them (footnote 5). The formula, the numeric usage gate and the automation factor's construction are all deferred to the appendix (PDF p.6 and footnote 7) and are documented in `labor-market-impacts-2026-03-appendix.md`.

**Validation against an outside forecast (PDF pp.8–9).** The occupation-level measure is regressed on BLS 2024–2034 projected employment change, weighted by current employment, and displayed as a binned scatter with 25 equally sized bins. The paper treats a −0.6pp projected-growth slope per +10pp coverage as partial external validation, and notes the same regression run on β alone yields no correlation.

**Linking to workers (PDF p.9, footnote 8).** O*NET-SOC codes are matched to CPS occ1990 codes using the Eckhart and Goldschlag (2025) crosswalk. Worker characteristics are measured in the CPS for August–October 2022, chosen as the three months before ChatGPT's release, so the comparison groups are described before any treatment could have acted.

**The estimator (PDF pp.10–12).** Unemployment is the priority outcome, justified on welfare grounds rather than statistical ones (PDF p.10). Treatment is the top quartile of time-weighted coverage; control is the bottom — in practice the 30% with zero coverage. The design is a difference-in-differences on the group gap in monthly CPS unemployment rates since 2016, with the ChatGPT release as the break; the pooled post-break estimate and its confidence interval are what generate the ~1pp detectability statement (PDF p.12). The paper explicitly declines to attribute parallel movements in both groups to AI (PDF p.12).

**The hiring margin (PDF p.12).** Because entrants often have no listed occupation in the CPS, the authors switch to the panel dimension and compute the monthly rate at which 22–25-year-olds start a job they did not hold the previous month, split by the exposure of the destination occupation, and run the same DiD on the gap. Over-25s serve as a placebo group.

**Robustness reported here, computed there (footnotes 6 and 9).** Varying the treatment percentile from the median to the 95th; restricting to 22–25-year-olds; substituting Department of Labor unemployment-insurance claimant data for CPS survey responses; and a Spearman rank correlation of job exposure across alternative construction choices. All are asserted in the main text and evidenced in the appendix.

**Released files.** The paper itself names **no filenames**: it says only that "Observed coverage at the task and job level is available at: https://huggingface.co/datasets/Anthropic/EconomicIndex" (PDF p.14). The two files that correspond to that sentence sit in the `labor_market_impacts/` folder of that dataset — `labor_market_impacts/job_exposure.csv` (the job-level measure) and `labor_market_impacts/task_penetration.csv` (the task-level measure) — and the dataset card describes the folder as "Job exposure and task penetration data". The paper says nothing further about either file: no column list, no units, no note on which of the two carries the time-fraction weights, the β value, the automation weight or the gate indicator, and no statement of whether the released coverage is the gated-and-weighted measure or an intermediate. Column-level facts are the data steward's to establish; see `data/releases/` and the steward's atlas. Any brief that builds on this paper must have the steward confirm which file carries which construct before a single number is quoted.

## Limitations (verbatim)

**On the framework's reach (PDF p.3):**
> "This approach won't capture every channel through which AI could reshape the labor market"

**On detectability (PDF pp.3–4):**
> "The impacts of AI, however, might be less like COVID and more like the internet or trade with China. The effects may not be immediately clear from aggregate unemployment data; factors like trade policy and the business cycle could cloud interpretations of trendlines."

**On why usage understates capability (PDF p.5):**
> "Some tasks that are theoretically possible may not show up in usage because of model limitations. Others may be slow to diffuse due to legal constraints, specific software requirements, human verification steps, or other hurdles."

**On a task that is feasible but unobserved (PDF p.5):**
> "For example, Eloundou et al. mark 'Authorize drug refills and provide prescription information to pharmacies' as fully exposed (β=1). We have not observed Claude performing this task, although the assessment seems correct in that it could theoretically be sped up by an LLM."

**On what the measure cannot see at the bottom (PDF p.8):**
> "At the bottom end, 30% of workers have zero coverage, as their tasks appeared too infrequently in our data to meet the minimum threshold."

**On the strength of the external validation (PDF p.9):**
> "This provides some validation in that our measures track the independently derived estimates from labor market analysts, although the relationship is slight."

**On the discretion in the construction (footnote 6, PDF pp.15–16):**
> "There are judgment calls involved at every step. Should the Eloundou et al. (2023) measure enter as {0, 0.5, 1} or something else? What determines 'significant' use? How do we handle tasks which seem very similar to those with high usage, but are too rare to have been picked up specifically in the sampling for the Economic Index? How much more should automation workflows count compared to augmentation?"

**On the treatment definition (PDF pp.10–11):**
> "A key question in interpreting our coverage measure is which workers should be considered treated? Should changes in employment be expected from just 10% task coverage?"

> "If AI capabilities advance quickly, task coverage might be high for lower percentiles of coverage, which might make an absolute threshold more helpful. But we make the assumption that impacts should affect the most exposed workers first, and present results varying the cutoff we use to define treatment."

**On the unemployment result (PDF p.11):**
> "The average change in the gap since the release of ChatGPT is small and insignificant, suggesting that the unemployment rate of the more exposed group has increased slightly but the effect is indistinguishable from zero."

**On the power statement (PDF p.12):**
> "(this will change as new data comes in, so it is merely a ballpark estimate)"

**On what the design would miss (PDF p.12):**
> "Note that our core estimate is based on differential changes in the unemployment rate in the exposed group compared to the less exposed group. If unemployment increased for all workers in parallel, we would not attribute this to AI advancements that still leave many tasks unaffected."

**On unemployment as a proxy for the youth effect (PDF p.12):**
> "But slowed hiring may not necessarily manifest as increased unemployment, since many young workers are labor market entrants without a listed occupation in the CPS data and may exit the labor force rather than appear as unemployed."

**On the youth hiring estimate (PDF p.13):**
> "although this is just barely statistically significant"

> "But there are several alternative interpretations. The young workers who are not hired may be remaining at their existing jobs, taking different jobs, or returning to school. A further data-related caveat is that job transitions may be more vulnerable to mismeasurement in surveys."

**On the paper's own standing (PDF p.14):**
> "Our work is a first step toward cataloging the impact of AI on the labor market."

**On the vintage of the capability input (PDF p.14):**
> "The Eloundou et al. metric could also be updated, to the extent that it is linked to LLM capabilities as of early 2023."

**On a figure that was wrong on publication (page, Corrections; not in the PDF):**
> "Updated Mar 8, 2026: Corrected Figure 7, which incorrectly reversed the labels between top quartile and zero exposure group inflow rates."

## Open questions, conjectures and promised follow-ups (verbatim)

**Promised repetition (PDF p.3):**
> "Our goal is to establish an approach for measuring how AI is affecting employment, and to revisit these analyses periodically."

**Stated purpose of building early (PDF p.3):**
> "by laying this groundwork now, before meaningful effects have emerged, we hope future findings will more reliably identify economic disruption than post-hoc analyses"

**Conjecture about when the framework earns its keep (PDF p.3):**
> "It is possible that the impacts of AI will be unmistakable. This framework is most useful when the effects are ambiguous—and could help identify the most vulnerable jobs before displacement is visible."

**Conjecture about the closing gap — untested (PDF p.7):**
> "As capabilities advance, adoption spreads, and deployment deepens, the red area will grow to cover the blue."

**Unexplained result, flagged and left (PDF p.9):**
> "Interestingly, there is no such correlation using the Eloundou et al. measure alone."

**Open theoretical question about treatment, with three competing answers named (PDF p.10):**
> "A key question in interpreting our coverage measure is which workers should be considered treated? Should changes in employment be expected from just 10% task coverage? Gans and Goldfarb (2025) show that if an O-ring model best describes jobs, employment effects might be seen only when all tasks have some degree of AI penetration. Hampole et al. (2025) argue that mean exposure decreases labor demand, but concentration of exposure in only certain tasks can counteract this. And Autor and Thompson (2025) highlight the level of expertise required for the remaining tasks."

**The design question the paper poses to itself (PDF p.12):**
> "What kind of scenarios can this framework identify?"

**Hedged reading of the youth result (PDF p.13):**
> "This may provide some signal of the early effects of AI on employment, and echoes the findings from Brynjolfsson et al."

**Promised updating of the measure (PDF p.14):**
> "There are several improvements to be made to the present work. Our usage data will be incorporated in future updates, forming an evolving picture of task and job coverage in the economy."

**Named next step (PDF p.14):**
> "And, given the suggestive results around young workers and labor market entrants, a key next step might be to look at how recent graduates with educational credentials in exposed areas are navigating the labor market."

**Promised extension to other data and countries (footnote 3, PDF p.15):**
> "Our task- and occupation-level exposure measures can readily incorporate other usage data, and be extended to different countries. We intend to apply this methodology to new settings over time."

**Robustness claim whose evidence sits in the appendix (footnote 6, PDF p.16):**
> "A reassuring finding which we expand on in the Appendix is that the Spearman (rank-rank) correlation of job exposure across many resolutions to these questions is exceedingly high."

**Stated hope for the method (PDF p.14):**
> "We hope that the analytical steps taken in this report, especially around coverage and counterfactuals, will be easy to update as new data on employment and AI usage emerge. An established approach may help future observers separate signal from noise."

## What it did not test

The wiki author's inference, not the paper's claims. Each item is something the paper's own text leaves open or explicitly out of frame.

1. **Whether the closing-gap conjecture holds.** "the red area will grow to cover the blue" (PDF p.7) is stated in the future tense with a single vintage of usage data behind it. The paper does not repeat the measure across the two Index datasets it uses to show whether coverage rose between August and November 2025, so the conjecture has no trend estimate attached.
2. **Why observed exposure correlates with BLS projections when β alone does not.** Flagged "Interestingly" (PDF p.9) and left there. No decomposition of which ingredient — the usage gate, the work-related filter, the automation weight, or the time-fraction weighting — carries the correlation.
3. **Which ingredient of the composite does the work anywhere.** The measure combines four adjustments; no result in the main text is reported with one of them switched off. Footnote 6's Spearman correlation reports that job *rankings* are stable, which is not the same as showing the ingredients are individually informative.
4. **Whether the choice of usage window matters.** The measure uses August and November 2025 (footnote 5); Figure 1 uses four reports. Neither the sensitivity to the window nor the effect of the mismatch is examined.
5. **Whether the half-weight for augmentative use is right.** Footnote 6 asks "How much more should automation workflows count compared to augmentation?" and the main text answers it by fiat at 0.5. No alternative weight is reported in the main text.
6. **Whether the zero-exposure group is a valid control.** By construction it is 30% of workers whose tasks fall below the usage gate, and Figure 5 shows the two groups differ sharply on sex, race, education and pay before treatment. The paper reports those differences but does not test parallel trends, reweight, or match; the COVID divergence in Figure 6 is itself evidence the groups respond differently to shocks.
7. **Employment, wages, hours, participation or job quality.** Unemployment is chosen as the priority outcome and job-starts as the secondary one (PDF p.10). Wages, hours, underemployment, labour-force exit and occupational switching are not estimated, even though the paper names labour-force exit as a reason its youth result may be understated (PDF p.12).
8. **Where the un-hired young workers went.** Named as an alternative interpretation — "remaining at their existing jobs, taking different jobs, or returning to school" (PDF p.13) — and not distinguished.
9. **The recent-graduate question it proposes.** "how recent graduates with educational credentials in exposed areas are navigating the labor market" (PDF p.14) is identified as the key next step, not attempted.
10. **Any causal identification.** The design is a two-group difference-in-differences with a single common break at the ChatGPT release. There is no instrument, no staggered adoption, no firm- or region-level variation, and no use of the paper's own variation in when Claude usage on a task actually appeared.
11. **Non-Claude AI usage.** The usage half of the measure is Claude traffic only. Footnote 3 says the measure "can readily incorporate other usage data" — an intention, not a test. Nothing establishes how much of AI use in exposed occupations the Claude sample represents, so the measure's level, unlike its ranking, is not interpretable.
12. **Non-US labour markets.** Also named in footnote 3 as a future extension. Everything here is O*NET, BLS and CPS.
13. **The API/consumer split inside the measure.** "a relatively higher share of automated use patterns or API implementation" raises exposure (PDF p.5), and Customer Service Representatives are said to rank second because their main tasks are ones "we increasingly see in first-party API traffic" (PDF p.8). No result separates the two surfaces, so the claim that API presence signals displacement risk is asserted rather than shown.
14. **Intensity of use.** The gate is binary and the weighting is about mode, not volume; two tasks above the gate count alike however different their traffic. (The appendix is where this is addressed; see the appendix file.)
15. **The seven unnamed occupations in Figure 3, and the age result.** Figure 3's full top-ten list and Figure 5's age and labour-market rows exist only in images. The key finding that exposed workers are "older" (PDF p.2) has no supporting number anywhere in the text.
16. **Whether the framework would have caught past shocks.** The paper opens by noting that offshorability and the official forecasts failed (PDF p.3), but does not back-test observed exposure — or its own design — against an episode where the answer is known.

## Verification

- **Fetched 2026-09-16.**
  - https://www.anthropic.com/research/labor-market-impacts — HTTP 200; full rendered text extracted (230 lines after stripping navigation) and read in full, including the Corrections block, all 10 page footnotes and the reference list.
  - https://cdn.sanity.io/files/4zrzovbb/website/2b5bbaf2c1eb81dbf6e6fb813c1a24e35a64d376.pdf — HTTP 200, 2,419,969 bytes, 17 pages; text extracted with `pypdf` and read in full, including all 11 footnotes and the reference list.
  - https://huggingface.co/api/datasets/Anthropic/EconomicIndex/tree/main/labor_market_impacts — HTTP 200; returns exactly two files, `labor_market_impacts/job_exposure.csv` (37,176 bytes) and `labor_market_impacts/task_penetration.csv` (1,889,822 bytes). There is no README in that folder (`.../raw/main/labor_market_impacts/README.md` returns "Entry not found").
- **Fetch failures:** none.
- **Not fetched, by instruction:** the separate appendix. Its URL is reached through the "Appendix available here" link (PDF footnote 7) and the page's Appendix section; it is covered by `labor-market-impacts-2026-03-appendix.md`. Every deferral above is marked as such rather than filled in from that document.
- **Quotation check.** Every passage in quotation marks in the `Definitions`, `Limitations` and `Open questions` sections, and every quoted number in `Claims`, was checked against the fetched text — 154 quoted passages in all, each matched string-for-string against the page text or the PDF text after normalising whitespace and curly quotes. The one exception, flagged where it appears, is "Job exposure and task penetration data", which is the Hugging Face dataset card's wording, not the paper's. Convention used: quotations are taken from the **page** rendering where the PDF's text layer breaks words or spacing (the extraction produces artefacts such as "T asks", "T amkin", "trendlines"/"trend lines"), because the page carries the same wording cleanly; page references are always to the PDF. Where the two sources genuinely differ in wording, both are recorded — in the table in `Source` and, for the three that affect meaning (capitalisation of the measure, "top 10%" versus "top 10% of coverage", "job start rate" versus "job finding rate"), inline at the point of use. One quotation retains a source typo: PDF footnote 9's "In ni extension", against the page's "In no extension".
- **Figures that could not be read.** Figures 1–7 are images in both renderings. Only the numbers stated in the body text or captions are recorded here; the full Figure 3 top-ten list, the full Figure 5 table, and all series values in Figures 4, 6 and 7 are not available from the fetched text and are marked as such in `Claims` and `What it did not test`.
- **Cross-file consistency.** Title, date, type, primary URL and PDF URL match the row for `labor-market-impacts-2026-03` in `wiki/INDEX.md`. `wiki/INDEX.md` was not edited in this thread.
