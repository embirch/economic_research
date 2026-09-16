# Anthropic Economics team — publication log

Compiled 2026-09-07 for Emily Birch's Fellows application research designs. Every number below is taken from the source text (PDF where available, otherwise the anthropic.com page). Quotations are verbatim. Items marked [NOT FETCHED] could not be retrieved. Where the PDF and blog differ, the PDF is treated as authoritative.

Fetch status:
- 1. Labor market impacts — PDF fetched and text-extracted (17 pp) + Appendix PDF fetched (11 pp).
- 2. 81,000 people / economics — PDF fetched and text-extracted (15 pp).
- 3. Economic Index Survey announcement — page fetched.
- 4. Agentic coding and persistent returns to expertise — blog page fetched + PDF fetched and text-extracted (18 pp) + Appendix PDF fetched (27 pp).
- 5. Coding agents in the social sciences — blog page fetched + Appendix PDF fetched and text-extracted (6 pp).
- 6. Evidence review of worker retraining — PDF fetched and text-extracted (123 pp).
- 7. Occupational Outlook — PDF fetched and text-extracted (31 pp).
- 8. How AI is transforming work at Anthropic — page fetched.
- 9. Economic Futures program + Research Fund — three pages fetched (program page, /economic-futures, Research Fund agenda).

---

## 1. Labor market impacts of AI: A new measure and early evidence

- **Date:** March 5, 2026
- **Authors:** Maxim Massenkoff and Peter McCrory (Anthropic)
- **URLs:** https://www.anthropic.com/research/labor-market-impacts ; PDF https://cdn.sanity.io/files/4zrzovbb/website/3f7fd9d552e66269bdb108e207c5d80531d04b8b.pdf
- **Data availability:** "Observed coverage at the task and job level is available at: https://huggingface.co/datasets/Anthropic/EconomicIndex."
- **Acknowledged reviewers:** Martha Gimbel, Anders Humlum, Evan Rose, Nathan Wilmers.
- **Bibtex key:** massenkoffmccrory2026labor

### Key findings (verbatim bullets)
- "We introduce a new measure of AI displacement risk, observed exposure, that combines theoretical LLM capability and real-world usage data, weighting automated (rather than augmentative) and work-related uses more heavily"
- "AI is far from reaching its theoretical capability: actual coverage remains a fraction of what's feasible"
- "Occupations with higher observed exposure are projected by the BLS to grow less through 2034"
- "Workers in the most exposed professions are more likely to be older, female, more educated, and higher-paid"
- "We find no systematic increase in unemployment for highly exposed workers since late 2022, though we find suggestive evidence that hiring of younger workers has slowed in exposed occupations"

### Quantitative findings (exact)
1. O*NET enumerates tasks for "around 800 unique occupations in the US".
2. Tasks rated β=1 (fully feasible for an LLM alone) account for **68%** of observed Claude usage; tasks rated β=0 account for **3%** (Figure 1; usage from the previous four Economic Index reports).
3. **97%** of tasks observed across the previous four Economic Index reports fall into categories rated theoretically feasible by Eloundou et al. (β=0.5 or β=1.0).
4. β shows scope for LLM penetration in **94%** of tasks in Computer & Math and **90%** in Office & Admin occupations (employment-weighted category averages).
5. Claude "currently covers just **33%** of all tasks in the Computer & Math category" (observed exposure).
6. Most exposed occupation: Computer Programmers, **75%** coverage; then Customer Service Representatives ("whose main tasks we increasingly see in first-party API traffic"); Data Entry Keyers **67%** covered. Discussion also names financial analysts among the most exposed.
7. **30%** of workers have **zero coverage** ("their tasks appeared too infrequently in our data to meet the minimum threshold") — e.g. Cooks, Motorcycle Mechanics, Lifeguards, Bartenders, Dishwashers, Dressing Room Attendants.
8. BLS projections 2024–2034 (published 2025): "For every **10 percentage point** increase in coverage, the BLS's growth projection drops by **0.6 percentage points**." Regression at occupation level weighted by current employment; binned scatter with **25** equally sized bins. "there is no such correlation using the Eloundou et al. measure alone."
9. CPS, Aug–Oct 2022 (three months before ChatGPT), top quartile of exposure vs the 30% with zero exposure: more exposed group is **16 pp** more likely female, **11 pp** more likely white, "almost twice as likely to be Asian", earn **47%** more on average; graduate degrees **4.5%** of unexposed vs **17.4%** of most exposed ("an almost fourfold difference"). Key finding also says more exposed workers are "older".
10. Unemployment DiD (top quartile vs zero-exposure, CPS since 2016): "The average change in the gap since the release of ChatGPT is small and insignificant, suggesting that the unemployment rate of the more exposed group has increased slightly but the effect is indistinguishable from zero."
11. Detectability: "differential increases in unemployment on the order of **1 percentage point** would be detectable" (from the CI of the pooled estimate; "merely a ballpark estimate").
12. Scenario: if all workers in the top **10%** of coverage were laid off, unemployment within the top-quartile group would rise from **3% to 43%**, and aggregate unemployment from **4% to 13%**.
13. Scenario "Great Recession for white-collar workers": 2007–2009 US unemployment doubled **5% → 10%**; such a doubling in the top quartile would move it **3% → 6%** — "This should be visible in our analysis as well."
14. Brynjolfsson et al. (2025) report a **6–16%** fall in employment in exposed occupations among workers aged 22–25 (6 pp vs flat-growth counterfactual; 16 pp from within-firm comparison of similar workers in different occupations — footnote 10).
15. Young workers (22–25) unemployment rate in exposed occupations: "flat (see Appendix)".
16. Job-start rate (monthly, CPS panel), age 22–25: less-exposed occupations stable at **2% per month**; entry into most exposed jobs decreases "by about **half a percentage point**"; series "visually diverge in 2024".
17. Averaged post-ChatGPT estimate: "a **14% drop** in the job finding rate compared to that in 2022 in the exposed occupations, although this is just barely statistically significant. (There is no such decrease for workers older than 25.)"
18. Robustness (footnote 9): varying the treatment percentile cutoff "from the median to the 95th percentile. In all cases, the impact is flat or negative (meaning that unemployment decreases for the exposed group)." Also DOL UI-claimant data: "In n[o] extension do we find clear impacts on exposed jobs."
19. Eloundou framework detail (footnote 4): "Directly exposed" = could be completed in half the time with an LLM "(with a 2,000-word input limit and no access to recent facts)"; "exposed with tools" = same speedup with software access; not exposed = duration not reducible by 50% or more.
20. Historical benchmark cited: offshorability measure identified "roughly a quarter of US jobs as vulnerable" but "a decade on, most of those jobs maintained healthy employment growth."
21. Footnote 6: "the Spearman (rank-rank) correlation of job exposure across many resolutions to these questions is exceedingly high" (Appendix).

### Data
- **O*NET** task database (~800 occupations).
- **Anthropic Economic Index** usage data: "We use the previous two Anthropic Economic Index datasets, covering usage from August and November 2025. For ONET tasks that are highly semantically similar, we split the counts across them." Figure 1 uses "the previous four Economic Index reports".
- **Eloundou et al. (2023)** task-level β ∈ {0, 0.5, 1}.
- **BLS Employment Projections** 2024–2034 (published 2025).
- **Current Population Survey (CPS)**: demographics Aug–Oct 2022; unemployment trends since 2016; panel dimension for monthly job starts (workers 22–25). "unemployed respondents report their previous job and industry."
- **Crosswalk:** "To match O*NET-SOC codes to occ1990 codes in the CPS, we use the crosswalk provided by Eckhart and Goldschlag (2025)" [EIG, Aug 2025].
- **Department of Labor unemployment insurance claimants** (appendix robustness).

### Methods
- Observed exposure construction: a task counts as *covered* if theoretically capable (β>0) AND "sufficient work-related usage in Claude traffic" (minimum threshold, unspecified in main text); "fully automated implementations receive full weight, while augmentative use receives half weight"; task coverage averaged to occupation "weighted by the fraction of time spent on each task" (time-fraction measure); category averages weighted by total employment. Exposure is higher if: tasks theoretically possible with AI; significant usage in Economic Index; performed in work-related contexts; "relatively higher share of automated use patterns or API implementation"; AI-impacted tasks make up a larger share of the role. Mathematical details in Appendix ("Appendix available here" — footnote 7).
- Validation: employment-weighted occupation-level OLS of BLS projected growth on coverage; binned scatter (25 bins).
- Treatment definition: "We compare workers in the top quartile of time-weighted task coverage to those in the bottom" (the 30% zero-exposure group); "we center our analysis on the idea that impacts should be felt most in the groups with the highest mean exposure"; cutoff varied median → 95th percentile in appendix. Notes that an absolute threshold might become more helpful if capabilities advance quickly.
- Outcome: **unemployment rate** as priority outcome ("most directly captures the potential for economic harm"); difference-in-differences framework, gap relative to 2022 baseline; pooled post-ChatGPT estimate with CI.
- Hiring: CPS panel monthly job-start rate ("when a worker reports a job that they did not have in the previous month"), split by exposure of destination occupation, DiD in bottom panel.
- Theoretical framing cited: Gans & Goldfarb (2025) O-ring automation; Hampole et al. (2025) mean vs concentrated exposure; Autor & Thompson (2025) expertise.
- Comparators: Gimbel et al. (2025) occupational mix; Brynjolfsson et al. (2025) ADP by age; Acemoglu et al. (2022) Burning Glass; Hampole et al. (2025) Revelio, instrumenting with university hiring networks; Johnston & Makridis (2025) industry-level admin data; Hui et al. (2024) Upwork.

### Stated limitations / caveats (verbatim)
- "This approach won't capture every channel through which AI could reshape the labor market"
- "The impacts of AI, however, might be less like COVID and more like the internet or trade with China. The effects may not be immediately clear from aggregate unemployment data; factors like trade policy and the business cycle could cloud interpretations of trendlines."
- "Some tasks that are theoretically possible may not show up in usage because of model limitations. Others may be slow to diffuse due to legal constraints, specific software requirements, human verification steps, or other hurdles." (Example: "Authorize drug refills and provide prescription information to pharmacies", β=1, never observed.)
- Footnote 6: "There are judgment calls involved at every step. Should the Eloundou et al. (2023) measure enter as {0, 0.5, 1} or something else? What determines 'significant' use? How do we handle tasks which seem very similar to those with high usage, but are too rare to have been picked up specifically in the sampling for the Economic Index? How much more should automation workflows count compared to augmentation?"
- "If AI capabilities advance quickly, task coverage might be high for lower percentiles of coverage, which might make an absolute threshold more helpful."
- "Note that our core estimate is based on differential changes in the unemployment rate in the exposed group compared to the less exposed group. If unemployment increased for all workers in parallel, we would not attribute this to AI advancements that still leave many tasks unaffected."
- "(this will change as new data comes in, so it is merely a ballpark estimate)"
- "slowed hiring may not necessarily manifest as increased unemployment, since many young workers are labor market entrants without a listed occupation in the CPS data and may exit the labor force rather than appear as unemployed."
- "But there are several alternative interpretations. The young workers who are not hired may be remaining at their existing jobs, taking different jobs, or returning to school. A further data-related caveat is that job transitions may be more vulnerable to mismeasurement in surveys." (cites Fujita, Moscarini & Postel-Vinay 2024)
- "Our work is a first step toward cataloging the impact of AI on the labor market."
- "The Eloundou et al. metric could also be updated, to the extent that it is linked to LLM capabilities as of early 2023."

### Future work (verbatim)
- "Our goal is to establish an approach for measuring how AI is affecting employment, and to revisit these analyses periodically."
- "Our usage data will be incorporated in future updates, forming an evolving picture of task and job coverage in the economy."
- "given the suggestive results around young workers and labor market entrants, a key next step might be to look at how recent graduates with educational credentials in exposed areas are navigating the labor market."
- Footnote 3: "Our task- and occupation-level exposure measures can readily incorporate other usage data, and be extended to different countries. We intend to apply this methodology to new settings over time."

### Open questions raised / left unexplained
- Which workers count as "treated"? "Should changes in employment be expected from just 10% task coverage?" (O-ring vs mean-exposure vs concentration; not resolved — they choose top quartile "with an eye toward simplicity").
- Why does observed exposure correlate with BLS projections but the Eloundou measure alone does not? (noted as "Interestingly", not explained).
- Where do un-hired young workers go (existing jobs, other jobs, school, out of labor force)?
- The minimum usage threshold for "covered" and the exact formula are relegated to the appendix; no sample sizes (N) for CPS regressions are given in the main text.
- Whether the slight rise in exposed-group unemployment is real (estimate positive but insignificant).
- The measure covers only Claude traffic; other providers' usage not incorporated.

### Terminology
- **Observed exposure** / **observed coverage** / **task coverage** / **job coverage** (used interchangeably); **theoretical capability** (β); **covered** task; **automated** vs **augmentative** use; **work-related** use; **first-party API traffic**; **time fraction measure**; **treated** group; **top quartile of exposure**; **zero-exposure group** (30% of workers); **job finding rate** / **job start rate**; **counterfactuals**; "Great Recession for white-collar workers"; "signal from noise".

### Appendix to "Labor market impacts of AI" (March 2026) — fetched: https://cdn.sanity.io/files/4zrzovbb/website/e5f77fc0e77c0185110b5e4b909602791ae76eae.pdf
- **Task gate:** a task is covered only if it "sees sufficient traffic in our Economic Index samples… with more weight given to API usage". Work usage = ClaudeWorkUsage_t (Claude.ai transcripts classified work-related via the use-case primitive of Appel et al. 2026) + APIUsage_t (all 1P API traffic, not filtered for work). "The strict gate we impose is that WorkUsage_t must be **100** or **0.0025%** of traffic." Tasks below the gate get exposure 0. "The exact cutoff has little impact on the job rankings." Footnote 3: 100 = 0.0025% of the previous two Economic Index reports (**2M** Claude.ai + **2M** 1P API), "similar to the median share of time spent on a particular O*NET task… **0.0014%**."
- Footnote 1: the use-case primitive was introduced in the September data; "in the August data we impute the percent of work-related Claude.ai traffic using a model trained on embeddings of the September tasks."
- **β treatment:** β_t "set to 1 if β is above zero" — i.e. β=0.5 tasks are upgraded to 1 ("many LLMs today will have such capabilities, and the extent to which they are not actually helpful will be captured in the usage and automation measures").
- **Automation factor α_t:** built from AutoShare_t (share of Claude.ai usage that is automative) and API presence; "A task that sees only augmentative uses and does not appear in the API transcripts would have α_t equal to **0.5**… A task with only automative uses would have α_t = **1**."
- **Task exposure** r̃_t = f(gate, β_t, α_t); **job exposure** = Σ_{t∈T_o} w_t · r̃_t, with w_t = fraction of time on task t (Tamkin & McCrory 2025). "Comparing two jobs that differ by 0.10 on the measure, the higher-coverage job could have a 10 percentage point higher share of their day covered by AI, or a 20 percentage point higher automation share."
- Worked example: Health Information Technologists' task "Identify, compile, abstract, and code patient data" = **13%** of their time; >**2,000** observations; β=0.5; automation factor **0.96** ("over 90 percent of the usage is in the 1P API data").
- Shared/near-identical tasks: counts allocated across jobs "equally… according to employment shares".
- "It does not measure the intensive margin of AI use."
- **Young workers (22–25) unemployment:** pre-2022 rate consistently lower for exposed group; gap "roughly constant"; pooled DiD "negative and indistinguishable from zero."
- **Cutoff sensitivity:** varying the treated-group threshold, "the impact on unemployment remains small and insignificant."
- **UI-claims check (ETA 203 "Characteristics of the insured unemployed"):** state-quarter × major SOC group; bottom quartile **1%** average coverage vs **31%** top quartile; four highly exposed groups: Computer & Mathematical, Office & Administrative Support, Business & Financial, Sales. Insured unemployment rate = UI claimants / CPS respondents in SOC × state. Pooled post-ChatGPT estimate **0.1 percentage point**, insignificant.
- **Task granularity:** O*NET has ~**18,000** task statements, **2,087** DWAs, **332** IWAs; aggregating to DWA/IWA rejected (groups dissimilar work, cleaves identical tasks). Alternative grouping (shared IWA + semantic similarity ≥ **0.7**) has Spearman **0.9** with the main grouping. "There is still ample room for improvement in the O*NET task framework. Calibrating the specificity of tasks appropriately, and representing their inter-dependency, could be a useful next step."
- **Measure comparison (Spearman):** raw Claude.ai usage vs baseline **0.81**, vs Eloundou **0.72**; Baseline × success "almost perfectly correlates" (footnote 4: r = **0.999**, "success rate is not strongly correlated with occupation"); Ridge-imputed usage "looks very similar to β"; DWA-level, IWA-level (as in Tomlinson et al. 2025), success ≥ 50% gate, and O*NET coreweight variants also reported.
- Footnote 2: non-work conversations excluded from Claude.ai counts, but personal API calls counted "because personal questions… routed through an API call seem more likely to represent incipient automation."

---

## 2. What 81,000 people told us about the economics of AI

- **Date:** April 22, 2026
- **Authors:** Maxim Massenkoff (led analysis, wrote post) and Saffron Huang (led the interview project). Methodological feedback: Zoe Hitzig, Eva Lyubich. Anthropic Interviewer implemented in Claude.ai by Grace Yun, AJ Alt, Thomas Millar. Clustering infrastructure: Theodore Sumers.
- **URLs:** https://www.anthropic.com/research/81k-economics ; PDF https://cdn.sanity.io/files/4zrzovbb/website/3a8d990bc90098038eabd77b0d12ff636ed58d50.pdf
- **Companion:** "What 81,000 people want from AI" (and its appendix) — same data; this study "adds additional variables using Claude-powered classifiers."
- **Bibtex key:** massenkoff2026interviewer

### Key findings (verbatim)
- "people who work in roles that are more exposed to AI have more concerns about AI-driven job displacement. These concerns are also higher among early-career respondents."
- "Those in the highest- and lowest-paid occupations report the largest productivity gains, most commonly from increases in scope (doing new tasks)."
- "Respondents experiencing the largest speedups from AI express higher concern about job displacement."

### Quantitative findings (exact)
1. Sample: "81,000 Claude users"; acknowledgements thank "the **80,508** Claude users who shared their stories."
2. "One fifth of the respondents in our survey voiced concern about economic displacement."
3. Occupation inferred for **39%** of respondents (missing for **61%**); **~11%** explicitly mentioned an occupation; **28%** inferred from other clues. Robustness: same qualitative results for Figures 1 and 3 using only the 11% explicit.
4. "For every **10-percentage-point** increase in exposure, perceived job threat increased by **1.3 percentage points**." (Figure 1, occupation-level, simple linear fit.)
5. "People in the top **25%** of exposure mentioned the worry **three times** as often as those in the bottom 25%."
6. Career stage inferred for "about half of respondents".
7. Productivity scale 1–7; mean productivity rating **5.1** ("substantially more productive"). **3%** reported negative or neutral impacts; **42%** "did not give a clear indication on productivity."
8. Recipient of gains named in "about a quarter of interviews"; of those, **10%** "said that employers or clients were asking for and getting more work"; smaller share cited AI companies; even smaller said net negative.
9. "only **60%** of early-career workers indicated that they personally benefited from AI, compared to **80%** of senior professionals."
10. Type of productivity gain: **scope** cited by **48%** of users who explicitly mentioned productivity effects; **speed** by **40%**; quality and cost smaller (not quantified).
11. Speedup coded 1 (much slower) / 4 (no change) / 7 (much faster); relationship between speedup and perceived job threat is **U-shaped** (Figure 6): those slowed down more likely to report significant threat; thereafter threat "increases consistently with the level of speedup".
12. Highest productivity gain by major group: management (mostly entrepreneurs; removing "solopreneurs" leaves management tied with computer & math); lowest: scientific and legal professions.
13. High-wage result "holds when we leave out computer and math occupations."
14. Earlier Economic Index finding echoed: in tasks requiring greater education, Claude reduced task time by a higher percentage.
15. Example testimonials scored: 7 = "It used to take months to make the website I [made] in 4-5 days"; 5 = "What might have taken four hours was accomplished in half the time"; 2 = "…it took multiple passes"; accountant: "finish a financing task in 15 minutes that used to take 2 hours."

### Data
- Open-ended interviews via **Anthropic Interviewer** in Claude.ai, personal accounts, December (per survey announcement); first question: "What's the last thing you used an AI chatbot for?"
- Linked to **observed exposure** (Massenkoff & McCrory 2026) at occupation level; occupational median wage quartiles from **BLS**.

### Methods
- Claude-powered classifiers for: occupation (left missing if unclear), career stage (labels: student_or_entry, junior, mid, senior_or_lead, executive, unclear), job threat ("said their role was already being replaced or substantially reduced, or that such changes were likely in the near term"), productivity rating 1–7 (1 less productive, 2 no change, 3 slightly, 4 moderately, 5 substantially, 6 much, 7 transformatively more productive — "The scale is not centered because most people say positive things about productivity, yielding almost entirely 6s and 7s on the original Likert scale"), productivity dimension (speed / quality / scope / cost / not_discussed — single label), speedup (1/4/7), beneficiary.
- Occupation-level linear fit of job-threat share on observed exposure; means by wage quartile and major SOC group with 95% CIs.
- Robustness: exclude computer & math; exclude solopreneurs; explicit-occupation-only subsample.
- Full classifier prompts given in Appendix.

### Stated limitations (verbatim)
- "Our respondents were, of course, active Claude users who were willing to take a survey. This could make them more likely to report productivity benefits than the average user."
- "There are key caveats to our analysis, owing to the nature of the data. First, our survey is limited to users of personal accounts on Claude.ai who chose to respond. Among other potential biases, these users could be more likely to perceive the benefits as flowing to themselves. Second, the users weren't asked directly about many of the derived variables here, so our inferences on occupation, career stage, and other variables from contextual clues could be wrong. Relatedly, because the survey is open-ended, our measures are based on what respondents happen to mention; these findings should be confirmed in structured surveys that ask about these topics directly."
- Footnote 5: "A major caveat, however, is that this survey went out to people with personal Claude accounts. A more representative picture would also include enterprise users, who may be more likely to say the value accrues to their employers."
- "Some of these inferences will be wrong."

### Open questions
- "A key question as AI diffuses through the economy is where the benefits will accrue—to workers, their managers, consumers, or corporations." (only 25% named a recipient.)
- Why the U-shape: creative workers slowed by AI yet fearful; mechanism proposed only informally ("if the time required to do one's tasks is shrinking quickly, there may be more uncertainty").
- "showing how qualitative data can surface quantitative hypotheses" — explicit invitation to test in structured surveys.
- Whether low-wage productivity gains reflect side projects rather than the main job (delivery driver e-commerce; landscaper music app).

### Terminology
- **Observed exposure**; **perceived job threat**; **economic displacement**; **career stage**; **scope / speed / quality / cost**; **speedup**; **surplus** ("Where does the surplus from AI productivity go?"); **solopreneurs**; **Anthropic Interviewer**; **Claude-powered classifiers**.

---

## 3. Announcing the Anthropic Economic Index Survey

- **Date:** April 22, 2026
- **Authors:** not bylined (Anthropic Economic Research)
- **URL:** https://www.anthropic.com/research/economic-index-survey-announcement

### Details
- Population: "a small, randomly selected group of Claude users"; "Anyone with a personal account at least **two weeks** old may be invited."
- Cadence: **monthly**, rotating samples, to reach "as broad a range of people as possible over time."
- Administration: via **Anthropic Interviewer**; invitation as a banner on claude.ai, by email for mobile-only users; also via the **Cowork** desktop app.
- Content: how work is changing, tasks delegated to AI, productivity gains, hiring/role shifts, expectations for one year ahead, and ten-year visions of an AI-shaped economy.
- Linkage: "Claude usage data in a privacy-preserving way" combined with qualitative responses; de-identified quotes may be published "from users who opt in."
- Companion: the **81,000** open-ended responses collected in December via Anthropic Interviewer (item 2).
- Privacy: processed under the "Supplemental Privacy Policy".
- No response rates, incentives, or question counts stated.

### Caveats / motivation (verbatim)
- "There is substantial uncertainty about how AI will affect jobs, productivity, and unemployment (and on what timeline)"
- Traditional labor-market indicators "track what has already happened, often with meaningful delay"

### Future work
- Findings to appear in "future Anthropic Economic Index reports and other research briefs"; no release schedule.

### Open questions
- Response rates and representativeness of the randomly invited sample vs the self-selected 81k sample.
- How the panel/rotation will be used for time-series inference (monthly rotating cross-sections, not a panel).

---

## 4. Agentic coding and persistent returns to expertise

- **Date:** June 16, 2026
- **Authors (PDF):** Zoe Hitzig, Maxim Massenkoff, Eva Lyubich, Ryan Heller, and Peter McCrory. (Blog page additionally lists Shaoyi Zhang.)
- **URLs:** https://www.anthropic.com/research/claude-code-expertise ; PDF https://cdn.sanity.io/files/4zrzovbb/website/433472e34b60db1a52ebf0b8c6600f057b6908c5.pdf ; Appendix "Available here" (separate document; classifier prompts, validation, regressions, task-value estimator).
- **Acknowledged:** Anton Korinek, Alex Tamkin, Boris Cherny, Cat Wu, Szymon Sacher, Santi Ruiz, Miles McCain, Jack Clark, others.
- **Bibtex key:** hitzig2026agentic

### Key findings (verbatim)
- "a privacy-preserving analysis of ~400,000 Claude Code sessions from between October 2025 and April 2026"
- "In a typical session, people make most of the planning decisions (what to do) and Claude makes most of the execution decisions (how to do it). The greater domain expertise a person brings to a session, the more work Claude does per instruction. On coding tasks, every major occupation succeeds… at nearly the same rate as software engineers, on average."
- "The more domain expertise a person has, the more often the session ends in success—though the gap between intermediate and expert users is modest. Over the seven months we observe, the share of sessions spent debugging fell by nearly half"
- "the value of the typical task, which we estimate through a comparison to freelance job postings, rose in almost every kind of work, and about 25% on average."

### Quantitative findings (exact)
1. ~**400,000** interactive sessions from ~**235,000** people, **October 2025 – April 2026** (seven months).
2. Claude Code users "spend an average of **20 hours per week** using the tool" (footnote 2: hours in which Claude Code was actively running, not hands-on typing time).
3. GitHub: coding-agent activity detected in **16–23%** of projects as of end-October 2025 (study of **128,000** public repositories); follow-up found adoption "more than twice as high among projects created after that period" (footnote 1; detection via co-authorship tags and config files "likely undercount").
4. Work modes: **56%** of sessions write (**25%**), fix (**26%**), or test/orchestrate (**5%**) code; operating software **17%**; planning/exploring **14%**; analysis or prose **13%**.
5. Codebase anchoring: **48%** primarily modify existing code; **17%** explore code; **14%** create new code from scratch; "Roughly a fifth of sessions touch no codebase at all."
6. Classifier–telemetry agreement: "more than **90%** of sessions our classifier labeled as creating or modifying code showed code changes in the telemetry."
7. Decision attribution: people make ~**70%** of planning decisions and ~**20%** of execution decisions (Claude ~80% of execution).
8. Typical session ≈ **4** turns; each prompt sets off ~**10** Claude actions on average ("sometimes over a hundred"); Claude writes ~**2,400 words** of output per turn.
9. Tail: ~**2%** of sessions average >100 actions per prompt; ~**1 in 270** >200; ~**1 in 2,300** >500.
10. When user keeps control of execution (>80% of execution decisions), Claude takes ~**8** actions per turn; when Claude controls planning (>80%), ~**16** actions.
11. Expertise gradient in autonomy: novice sessions ≈ **5** actions and ~**600 words** per prompt; expert sessions **12** actions and **3,200 words** ("more than twice as long… five times the output"). Regression-adjusted: **+9% actions** and **+13% output** per expertise level, p<0.001, controlling for work mode, task value, month, occupation, model family; SEs clustered by user; each adjacent-level step also significant.
12. Occupation inferred in ~**70%** of sessions (23 SOC major groups). Largest: Computer & Mathematical; then Business & Financial Operations; Arts, Design & Media; Management; Life, Physical & Social Sciences. Fastest-growing non-software groups: management, sales, legal.
13. Composition shift Oct 2025 → Apr 2026: fixing broken code **33% → 19%**; operating software **14% → 21%**; writing + data analysis "roughly doubled, from about **10% to 20%**".
14. Task value (freelance-posting comparison): average session value **+27%** Oct→Apr; building **+43%**, operating **+34%**, fixing **+32%** (key findings round to "about 25%").
15. Sessions with "no clear goal": ~**7.7%** of full sample (excluded from success analysis).
16. Success by expertise (adjusted): novice **verified success 15%**, at-least-partial **77%**; intermediate-or-above **verified 28–33%**, partial **91–92%**.
17. Among sessions that hit trouble (failure signal ≥3): verified success **4%** novice → **15%** expert; at-least-partial **60%** novice vs **80–81%** intermediate-through-expert.
18. Abandonment (judged failed and zero lines of code written) among troubled sessions: **19%** novice vs **5–7%** everyone else.
19. Footnote 9: "the average estimated value of a troubled session roughly **doubles** from the bottom of the expertise scale to the top."
20. Occupation vs success: computer & mathematical occupations verified success ~**30%** overall vs ~**26%** other professions; among code-producing sessions **34%** vs **29%** — "That five-point gap is small, and it has neither widened nor narrowed over seven months, even as the success rates in both groups increased."
21. "every one of the **ten largest** occupations in our dataset lands within **seven points** of software engineers"; Management occupations highest on verified success, "slightly above" software engineering.
22. "Sessions rated expert reach verified success more than **twice** as often as those rated novice".
23. Blog adds: partial success by occupation 89% (software) vs 88% (other) in code-producing sessions.

### Data
- Claude Code interactive sessions via CLI, claude.ai, or desktop app. **Excluded:** third-party IDE integrations, SDKs, headless `claude -p "<prompt>"` mode ("much of it is programmatic… we do not see a user's session end-to-end").
- Telemetry recorded automatically per session (lines added/deleted, etc.).
- Public reference dataset for examples: **SWE-chat**.
- Task-value calibration: "a public dataset of real postings" from a freelance marketplace.
- Privacy: privacy-preserving analysis tool (Clio-style); "No researcher reads individual transcripts, occupation labels are never linked to identifiable users, and we only observe aggregates over a minimum number of distinct users."
- All classifiers use **Claude Sonnet 4.6** unless noted.

### Methods
- Nine **work modes** (single label per session): building, fixing, testing, orchestrating, operating, understanding, planning, analyzing, communicating.
- **Decision attribution classifier**: lists meaningful decisions, splits into planning (what to do, which approach, what counts as done) vs execution (which files, what code, what language, which commands), attributes each to Claude or user → two shares per session.
- **Expertise classifier**: five-point novice→expert, task-specific; signals: precision of framing, what user asks Claude to verify, who corrects whom.
- **Occupation classifier**: 23 SOC major groups; uses project context, file names/structure, artifacts referenced, vocabulary; "explicitly instructed not to treat the act of coding as evidence of a coding profession."
- **Judged success** (succeeded / partially succeeded / failed / no clear goal) + **success signal** classifier (0 "no signal", 1 "weak signal" … 5 "multiple hard signals": git commits/PRs matching the work, passing tests, explicit user affirmation) + **failure signal** classifier (errors, failed tests, retries, pushback). **Verified success** = judged success AND ≥1 hard verifiable signal. **Hit trouble** = failure signal ≥3. **Abandoned** = judged failed and zero lines of code written.
- **Adjusted rates**: compare sessions sharing same work mode, task-value band, month, task subject, and user type (software-related occupation or not); regressions detailed in Appendix; CIs on sample means; Figure 6 CIs computed on distinct accounts.
- **Task value estimator**: fuzzy match of session to freelance job postings; used for relative comparisons, "not as dollar values to be read literally."
- Validation: classifiers vs telemetry; agreement with "a strong reference model on the majority of sessions" (Appendix).
- Figure 3: boxes IQR split at median, whiskers 5th–95th percentile, white dots geometric means.

### Stated limitations (verbatim)
- "These findings are preliminary. As in most of our research, we cannot measure real-world outcomes, like whether code written in a session is actually used or discarded thereafter, or whether it produces an economically valuable artifact."
- "In addition, the non-interactive usage this report excludes is a substantial share of activity. Developing a framework to measure it is a priority for future work."
- "And all of our classifications of sessions depend on a model's reading of the transcript… But classifiers remain challenging to validate at scale, and Claude Code sessions add further difficulty, as they may be too long and complex for human labels to serve as ground truth."
- "One might worry that expertise isn't the real driver—perhaps experts simply pick different tasks, or differ in other ways. Throughout this section, we partially address this worry…"
- Footnote 8: "The estimation approach we take here is intended to get at relative differences in the value of sessions, not absolute value. The dollar amount is based on comparisons to the freelancer market—not salaried work—and comes from an ultimately fuzzy match between the Claude Code session and the job posting. Since the relative estimates will remove any consistent bias from these issues, we place more emphasis there."
- Footnote 9: "Conditioning on trouble selects different sessions for different users. Experts hit trouble less often overall, so the troubled sessions they do have are likely to be on harder problems… Part of the gap in recovery rates may therefore reflect that novices get stuck on routine problems while experts get stuck on challenging hard problems."
- Footnote 10: "Even if the model misclassifies managers, the signals relied upon to determine that the user is a likely manager—perhaps in how tasks are delegated and specified—tend to be associated with greater success. In other words, perhaps acting like a manager confers greater success."
- "verification rests partially on explicit confirmation in the transcript, and managers may be more likely to communicate when they get what they ask for."
- Footnote 1: GitHub detection "likely undercount[s] actual usage."

### Future work / signals to watch (verbatim)
- "The picture in this report will be updated as the models, the users, and the division of labor between them change."
- "if the returns to expertise begin to decrease over time, that would suggest that models are starting to supply the essential judgment that users currently bring, and that the gains from these tools are broadening beyond domain experts."
- "If the share of coding sessions completed successfully by users outside software occupations continues to grow, it could indicate that software production is becoming a part of ordinary work in every field, rather than the product of a single occupation."
- "coding is a leading case—what happens in software is likely a preview of what may come as agentic tools take on other forms of knowledge work."

### Open questions raised
- "Can people without formal coding experience successfully direct an agent through complex technical work? And what will rapid adoption and improvement of these tools mean for knowledge work broadly? While we don't have full answers to these questions yet…"
- Is expertise causal or selection (task choice, unobserved user differences)? Only "partially" addressed by conditioning.
- Why management outperforms software engineers (transferable delegation skill vs measurement artefact).
- Whether "amplifies some forms of knowledge and skills, while substituting for others" holds "across the economy".
- No wage/earnings outcomes; no external validity beyond Claude Code interactive surfaces.

### Terminology
- **agentic coding**; **interactive session**; **turn**; **actions per prompt**; **work modes** (nine); **planning vs execution decisions**; **decision attribution**; **division of labor** ("People decide what to build, and the agent decides how to build it"); **expertise** (task-specific, five-point); **judged success**; **verified success**; **success signal / failure signal** (0–5); **hit trouble**; **abandoned**; **task value / price estimate**; **persistent returns to expertise**; **competence, not mastery**; **headless mode**; **telemetry**.

### Appendix to "Agentic Coding and Persistent Returns to Expertise" (June 2026) — fetched: https://cdn.sanity.io/files/4zrzovbb/website/7426c33b0e75ab4771c465d30d5bc1019bdd0c9c.pdf
- **Exact sample:** **398,198** sessions uniformly randomly sampled from Claude Code traffic, from **234,751** users; **73,066** users appear more than once, **6,382** more than 5 times, **1,413** more than 10 times. Internal Anthropic usage excluded. Sessions with zero human turns excluded (headless).
- **Classifier mechanics:** each turn middle-truncated at **5,000** characters, transcript truncated at **25,000** characters; single call to **Claude Sonnet 4.6 at temperature 0.2** answering with exactly one option; task-value estimator uses **Haiku 4.5** (summarizer) + **Opus 4.7** (pricer).
- **Telemetry used:** human prompts, model calls, successful tool calls, output tokens, lines of code added/removed, account age (days since Anthropic signup).
- Classifiers (full prompts published): Work Mode (9, no "Unclear", "Pick by DOMINANT activity"); User expertise (1–5 + Unclear; three co-equal signals: setup specificity, verification type, direction of correction); Occupation (user profile) — 23 SOC major groups + Unclear, "Do NOT classify on the task being performed"; Occupation (work performed) — no Unclear; Session outcome (Succeeded / Partially / Failed / No clear goal; "default to Succeeded if the trajectory is clean"); Success signal (NONE, 1–5; 4 = one hard signal, 5 = multiple); Failure signal (NONE, 1–5).
- **Derived definitions:** verified success = judged Succeeded AND success signal ∈ {4,5}; hits trouble = failure signal ≥ 3; abandoned = judged Failed AND zero lines added; wrote code = ≥1 line added; sessions with Unclear occupation excluded from occupation analyses (**~30%**).
- **Task value estimator:** session rewritten as an Upwork-style posting, priced against a tier-balanced calibration corpus of **200** real postings (50 per tier: $10–200, $200–1,000, $1,000–5,000, $5,000–50,000) from ~**23,000** filtered fixed-price postings (2024–2026, $10–$50,000, ≥50-char description; raw tier distribution ~62/27/9/2%). Holdout of **999** postings: log R² = **0.38**; "Within-tier discrimination is concentrated at the low end and is essentially zero above $5,000"; small jobs over-priced ~**2.4x**, largest under-priced ~**7x**; uniform calibration under-priced $5,000+ jobs ~**12x** (median $800); balanced raised median to $2,000. "we generally use these task value estimates ordinally."
- **Validation vs telemetry:** share judged Succeeded rises from **13%** at success-signal 1 to **90%** at 5; falls from **85%** at failure-signal 1 to **3%** at 5. Claude-led planning ↔ more model calls and tool calls per prompt; execution share "near-orthogonal".
- **Internal outcome validation:** same prompts on internal Anthropic Claude Code sessions joined to whether commits landed on main; expertise–success gradient replicates within-engineer: "judged success rises by roughly **3–5 percentage points** per expertise level with author fixed effects".
- **Strong-model agreement:** classifiers re-run on **198** SWE-chat sessions; reference model **Mythos Preview** labels; blind judge (Mythos Preview) adjudicates disagreements; one author re-adjudicates. Agreement **78–98%** (categorical); ordinal **78–99%** with adjacent points, **53–68%** exact; concerning disagreements **0–3%** per classifier (≤5 of 198); human concurred with judge in **11 of 15** flagged.
- Caveat (verbatim): "As long as the classifier's mistakes are similar across groups (which we did not extensively verify here), those mistakes cancel each other out when making comparisons." "We are actively developing methods of validation that take seriously that human labels may no longer be the gold standard for complex sessions."
- **Table A1:** OLS with FE, **375,687** sessions (excl. no clear goal); columns add controls cumulatively: (2) work mode, (3) month, (4) task subject, (5) occupation group [preferred], (6) model and session length; SEs clustered by user; coefficient = change in P(verified success) per expertise step. **Table A2:** indicator per expertise level under column-(5) FE, Novice omitted (basis of Figure 5/6 adjusted rates). Cells under the aggregation limit dropped.

---

## 5. Coding agents in the social sciences

- **Date:** May 27, 2026
- **Authors:** Thomas Lyttelton (MIT), Maxim Massenkoff (Anthropic), Nathan Wilmers (MIT)
- **URLs:** https://www.anthropic.com/research/coding-agents-social-sciences ; Appendix PDF https://cdn.sanity.io/files/4zrzovbb/website/403415e54964751190003985896630e56829e797.pdf
- **Study name (Appendix):** "WFL Baseline Survey" — the baseline wave of "a larger ongoing study of how coding agents affect research productivity, including a randomized experiment" providing Claude Max / Claude Code access.

### Quantitative findings (exact)
1. Analytic sample **1,260** respondents (US/Canada quantitative social scientists); fielded **February 20 – March 24, 2026**.
2. Recruitment: **44,700** academics directly emailed (scraped department sites at R1 and major Canadian universities; OpenAlex, restricted to those published in the last year; conference programs); plus DGS distribution and society lists (Academy of Management, ASA). **$10** gift card; eligibility for a randomized experiment providing Claude Max accounts.
3. Screener: quantitative empirical data users; doctoral students with ≥**2 years** of training who plan to enter academia.
4. **81%** have tried AI chatbots in research; only **20%** have adopted coding agents (regular = "more than once a week", CLI-integrated: Codex, Cursor, Claude Code; follow-up verification incl. Google Antigravity).
5. Gender (verbatim): "those with typically male names have adopted coding agents at more than twice the rate of respondents with typically female names." Adoption by field: economics **39%**; political science **25%**; public health **6%**; communication **6%**; education **4%**.
6. Gender: "Twice as many" researchers with typically male names use coding agents vs typically female names (gender_guesser on first names; androgynous/unknown excluded); gap persists within discipline × career stage and is "slightly larger" among those who have tried AI.
7. Top-25 institutions (Nature Index 2025): **28%** of respondents; researchers at top universities **40%** more likely to use coding agents.
8. Career stage: doctoral students/postdocs — "just over a quarter" use coding agents at least weekly; tenured professors' rate "more than half lower". Composition: ~**40%** full/associate professors, **25%** assistant professors, ~**30%** doctoral students.
9. Tool shares among coding-agent users: Claude Code **86%**; Codex **31%**.
10. Use cases: code generation **97%** of coding-agent users vs **77%** of other AI users; prose editing second most common; only **one-third** of AI users have drafted prose with it.
11. Output (six months pre-survey, adjusted for career stage, discipline, survey week; Figure 5 "Productivity differences in research output between regular AI coding agent users and other researchers"): verbatim — "Coding agent users are starting projects at a pace of around **a quarter of a paper** more and posting around **a half of a working paper** more than non agent users." and "In percentage terms, coding agent users look around **10%** (empirical projects started) to **75%** (working papers posted) more productive than others in their discipline and career stage." (Percent = β ÷ control-group mean, per appendix. The task brief's "~50% more working papers" is a rounding of the 0.5-paper absolute gap; cite the 75% figure for the percent version.)
12. No evidence coding-agent users submit more new papers to journals or resubmit faster. Unadjusted (Figure A1): agent users post more working papers and submit more grants "but actually submit fewer papers to journals" — the latter reflects discipline/career-stage composition.
13. Optimism: **88%** score above 5 on a 1–10 scale that AI raises productivity; **50%** score 8+; respondents ~**70%** more optimistic about own-paper productivity than about field-level impact.
14. Pilot vs main (Table A2; main restricted to sociology/poli sci/management, excluding full professors): "little difference in overall rates of AI use"; full sample "one point more optimistic about field impacts and a half point more optimistic about paper productivity effects" on the 1–10 slider.
15. Significance: reported differences at p<0.05; Figure A1 stars * p<0.05, ** p<0.01.
16. Discipline free-text: **318** unique values consolidated to eight buckets + "Other" via Claude classification and hand coding.

### Data
- Email survey; self-reported outputs over prior six months: projects started, working papers posted, journal submissions, journal resubmissions, grant submissions, conference submissions (working papers / submissions / resubmissions mutually exclusive).
- Timing context: launched ~two months after the December 2025 Claude Code/Opus 4.6 moment, ~one month after Claude Code (desktop) release, before the OpenAI Codex app.

### Methods (Appendix, verbatim spec)
- "Output_i = β × CodingAgentUser_i + γ × X_i + ε_i" where X_i = fixed effects for career stage (five: PhD student, postdoc, assistant, associate, full professor), discipline bucket (nine), and calendar week of survey completion. "Standard errors are heteroskedasticity-robust." OLS; β divided by control-group mean to get percent differences. "A Poisson model specification gives similar results." 95% CIs "using the robust standard errors scaled by the outcome mean."
- Selection check: pilot sample (early Feb, no AI-experiment advertising; excluded full professors; sociology, poli sci, management only) vs main sample.

### Stated limitations (verbatim)
- "The data presented here is based on an email survey of quantitative social scientists, recruited explicitly to participate in a study on workflows and AI use." Respondents likely "both heavier users and more optimistic about LLMs than non-responders".
- "This was not a representative sample—respondents were recruited for a study that offered access to Claude Max accounts"
- "The early-stage productivity differences we see should be interpreted descriptively."
- "The early adopters of coding agents may be more productive and otherwise different from non-adopters in many ways that we cannot measure directly in the survey."
- "Differences should not be interpreted as causal, but as a first cut comparison between researchers using coding agents and those who are not."
- "We only look here at the number of projects researchers report, and report nothing about their quality."
- Appendix: "The main sample we use here suffers from its function as recruitment for an experiment on Claude Code access and research productivity." "Overall, the full sample is composed of more pro-AI respondents, but the key gradients that we can measure are similar in the pilot sample"; pilot "is missing our detailed coding agent question."

### Future work (verbatim)
- "We will publish results from this experiment in the future"
- "In future updates on this study, we will show results comparing coding agent users to a clean comparison group, and assess whether the content, and not just quantity, of coding agent augmented work looks different."

### Open questions raised
- Why productivity differences show only in early-pipeline outputs (projects, working papers) and not journal submissions/resubmissions — lag or composition?
- Whether field-level costs feared by respondents (congestion, selective reporting, risk-averse research) materialise; the paper-vs-field optimism gap.
- What drives the steeper gender and institutional gradients for coding agents vs general AI use.
- Quality of output (unmeasured).

### Terminology
- **coding agents**; **agentic coding platforms**; **regular use** (>1/week); **WFL Baseline Survey**; **discipline buckets**; **typically male / typically female name**; **top 25 institutions**; **adjusted vs unadjusted differences**; **paper productivity vs field impact**.

## 6. An evidence review of worker retraining

- **Date:** August 12, 2026
- **Authors:** David Roodman (Independent) and Maxim Massenkoff (Anthropic)
- **URL:** https://www-cdn.anthropic.com/4ef47f859bc67be739a14f5d40b43927eecacdb6/WorkerRetraining.pdf (123 pp)
- **Code/data:** github.com/droodman/job-training-meta-analysis ; interactive results at droodman.github.io/job-training-meta-analysis
- Acknowledged: David Fein, Richard Hendra, Evan Rose (comments); Martha Gimbel, Anders Humlum, Benjamin Hyman, Molly Kinder, Laura Peck, Kelsey Schaberg, Nathan Wilmers, Peter McCrory, Jack Clark and others.
- Note: PDF header carries the (mis-)label "Anthropic Economic Index report: Cadences".

### Executive-summary numbers (verbatim where possible)
1. "146 impact estimates from 56 randomized trials conducted in the United States from 1973 to the present." Programs "run six months and cost roughly **$13,000** per person."
2. "programs on average increased employment by **1.7 percentage points**, compared to a baseline employment rate of **63%** in the control group. They increase earnings by **$800 per year** on average." (per person offered treatment)
3. "Some 'sector programs' boost earnings **10 times** as much… lifted pay by **$5–10,000 per year**".
4. Sector programs "filter out >**80%** of applicants."
5. Retraining is "the most popular policy for mitigating labor market disruption from AI" (Karger et al. 2026, Figure 16 — survey of economists, AI experts and superforecasters; beat enhanced UI, jobs guarantee, UBI).
6. In 2017 the US spent **$14 billion**/year on job search assistance, counseling and retraining, reaching ~**10.7 million** people (GAO 2019). CEA (2019) called programs "largely ineffective".
7. Evidence base: **7** randomized/discontinuity studies in Europe; **2** judge-randomization studies (US, Denmark); **56** US RCTs. **678,014** apprentices active in US in 2025 (ETA 2025) — apprenticeships out of scope for lack of evidence.

### Meta-analysis (§6.5) — exact numbers
8. Sample: **56** studies, **24** report multiple subgroups → **146** impact estimates. Overlap with prior reviews: **37** in Smedslund et al. (2006), **0** in Haelermans & Borghans (2012), **2** in Card, Kluve & Weber (2018), **26** in Peck et al. (2021). "No previous meta-analysis has included nearly so many US-based randomized studies."
9. Training-primary subset (Claude-assessed): **33** studies, **78** estimates. Classroom training a component **90%** of the time, OJT **29%**; ~**6 months** duration; cost **$13,046** per person offered (2025 $; Table 1). Dislocated-worker programs only **3–4%** of sample.
10. Table 2 (REML random effects, SEs clustered by study): training-primary employment impact **+2.8 pp** in year 2, **+1.7 pp** in years 3–5; earnings **+$1,139** (yr 2) and **+$791**/yr (yrs 3–5) in 2025 $. All programs: employment **+2.5–2.9 pp** (medium), **+1.7–1.8** (long); earnings **+7.8%** medium ($1,000–1,100 from bases of $12,500 full / $14,700 training-primary), **+4.9%** long ($700–800 from $14,400 / $16,100). "11 of the 12 mean impact estimates are 2–4 times their standard errors"; exception = short-term earnings for training-primary (in-training losses).
11. Compliance: offer accepted **75%**; control access **9%**; program take-up differential **66 pp** → "LATE-program" ≈ **1.5×** ITT; any-training differential **28 pp** → "LATE-training" ≈ **4×** ITT ("likely an upper bound"; executive summary says 2–4×).
12. Costs: among the **67%** of training-primary interventions with cost data, **$13,598** per treatment-group member; NPV of earnings impacts to retirement **$14,146**, **$19,525** incl. fringe; government recoups ~**76%** → long-term fiscal cost **~24%** of upfront (lower if Social Security contributions not treated as pure taxes).
13. Table G1 (training-primary, per treatment-group member, 2025 $): program cost −13,598; reduced other-training spend +2,778; pre-tax earnings +14,146; fringe +5,379; payroll taxes 2,420; income taxes 2,434; sales taxes 572; public-benefit reduction 2,096; work-related spending −1,180; unpaid time −2,511; totals participant **8,312**, government **−3,299**, society **5,013**. **B/C narrow 1.44; broad 1.80; MVPF 2.52; govt net/gross cost 0.24; societal IRR 5.97%.**
14. Table G2 (sector programs): cost −11,602; other-training +1,289; pre-tax earnings **+60,319**; fringe +22,938; payroll 10,317; income tax 10,379; sales 2,441; benefits 8,937; work spending −5,031; unpaid time −3,099; totals participant **43,052**, government **+21,762**, society **64,814**. **B/C narrow 7.18; broad 8.07; MVPF ∞ (raw −1.98); govt net/gross −1.88; societal IRR 34.03%.**
15. Benefit-cost assumptions (Appendix G): earnings impacts projected to age **65** with slow decay per Karahan & Ozkan (2013); discount rate = real 30-yr TIPS (FRED DFII30, 18 May 2026); pre-tax wages = **72.4%** of total compensation (ECEC 2025, office & admin support) → fringe = (1−0.724)/0.724 × earnings NPV; FICA **7.65%**; employer taxes **6.85%** of compensation; income tax **17.2%** (avg of 19.0/15/17.6/17.6 from WorkAdvance sites); sales tax **5.69%**; public-benefit reduction = **14.8%** of earnings gain; work-related spending **8.34%**; unpaid time valued at **50%** of earnings impact (adjusted for employment effect); deadweight loss of taxation excluded; crime/health benefits excluded; GE/displacement assumed away. Persistence check: among **28** training-primary estimates with medium-term gain ≥$200 and longer follow-up, long-term impacts total **110%** of medium-term (median ratio **0.90**). "Without that persistence, they would have a benefit-cost ratio under 1."
16. Meta-regression correlates (Table 3; block-based "survivor" selection copied from Peck et al. 2021; REML; with/without multiple imputation, **10** imputed datasets): employment impacts have "fallen by about **0.07 points per year** since the 1970s"; non-South regions **2–4 pp** higher employment impacts; classroom training no clear advantage; dislocated workers harder to help (driven solely by WIA nulls); intellectual-disability programs **+8 pp** long-term (2 programs); **employer hiring commitment: +$8,000–9,000/yr** in year 2 and beyond (driven by 3 programs: Wildcat, Year Up, WRTP); **regional unemployment +1 pt → +1.2 pp** employment impact (medium term) and **+$250/yr** earnings; long-term coefficient only **0.37** and insignificant; +1 pt unemployment → **+3.4 pp** program participation (SE 2.8) and **+4.7 pp** any-training participation (SE 1.8); persistence coefficients of medium-term on long-term impacts **0.48** and **0.52**.
17. Justice-involved effect driven entirely by NSWD.

### Sector programs (§7) — exact numbers
18. Sector programs (defined for meta-analysis by employer involvement in curricula; Peck et al. traits "curricula adapted for employers' needs" and "input on curriculum" correlate **0.58**): cost **$11,602** vs $13,598/$13,046; discounted earnings impact **$60,319** vs $14,146; **B/C 7.18** ("almost five times the 1.44"); random-effects ITT: employment bump ~**3.0 pp** (partially transient), earnings **+$3,000–4,000/yr**; program take-up differential **56 pp** → LATE-program = **1.79×** ITT; any-training differential ~**25%**. Control groups: long-term employment **80%** vs 60% for training programs; control earnings **50–75%** higher — "Sector programs draw from populations that are higher paid even without training."
19. Katz et al. (2022) covers **9** studies of **8** programs; the review adds **10** randomized evaluations (CET + replications; 3 Green Jobs and Health Care; ATIM; ACE Maryland/Texas; 3 more PACE incl. VIDA). "the earnings impacts are 3–5 times higher than for the average job training program."
20. Named results: CET San Jose (MFSP) employment **57% → 66%**, monthly pay **$405 → $506** (1986 $); JOBSTART CET **$250/month**; CET replication failed at all **14** sites (only **4** high fidelity, **6 of 14** high fidelity on employer involvement); P/PV Sectoral Employment Impact Study (QUEST, WRTP, JVS-Boston, Per Scholas) **+$2,000–5,000/yr**; **Year Up +$8,000/yr** with no diminishment after 7 years, cost ~**$30,000**/participant, 8 cities; other 8 PACE programs null; WorkAdvance: Per Scholas standout, St. Nicks reached **+$8,000/yr** at 7–10 years; Project QUEST pre/post **$5,367 → $24,907**/yr (non-randomized, Ashenfelter's dip). WorkAdvance programs accepted ~**20%** of applicants; Per Scholas 2025: **70,000** applicants for **5,000** spots; WRTP ran **2–8-week** trainings.
21. Selectivity, soft+vocational skills, coaching, and graduation into work listed as components; "It is unclear—and a question for further research—exactly how important each of these components is."

### Major US RCTs (§4) — exact numbers
22. **NSWD** (1975–78): $82.4M cost (~4× today); 6,616 randomized across 10 sites (of 10,043 participants; 14 orgs, 4 dropped); 4 target groups (AFDC women ≥30 of 36 months, ex-addicts, ex-offenders, dropouts; latter three 80–94% male; ~80% Black, 10% Hispanic; ~10 years schooling); 18-month interview rates 84% (AFDC) / ~70%; uptake 95% (AFDC) vs 11%/3%/4% control crossover; AFDC employment ITT **+7.1 pp** (p<0.1), earnings **+$75/month ≈ $900/yr**; ex-addict last-quarter gap **17.2 pp**; Couch (1992) SSA linkage: **$441/yr** (1978 $) 1982–86 ≈ half; ~1/3 of eligibles applied → impact among eligibles ≈ **2.5 pp**; footnote: randomizing among eligibles would need 20,000 vs 6,600 sample. Non-randomized benchmarks (Fraker & Maynard 1984): youth 1979 earnings true **$7** vs estimates **−$617 to −$1,982**; Imbens & Xu (2025): all modern non-randomized methods fail placebo checks on NSWD.
23. **JTPA** (random assignment Nov 1987–Sep 1989; **15,981** subjects; 2:1 split; 16 of 649 SDAs after approaching >200): enrollment 65% of treated; JTPA-participation differential ~65 pp, any-training ~25 pp; 18-month earnings +$539 (adult women), +$550 (men; 4.5% of $12,306 control), youth −$182 / −$854; 30-month: +$1,837 / +$1,599 adults; young male arrestees UI −$4 vs self-report −$4,209; GAO (1996) SSA data: **~3 pp** employment, **$500–600/yr** earnings, fading year 5; control employment ~75%; cost ~**$1,000**/enrollee vs $8,000 NSWD; LATE for any training ≈ 4× ITT ≈ 12 pp / $2,000–2,400. "creaming" and enrollment-timing gaming under performance standards (Goodhart's Law).
24. **Job Corps** (1994–96 intake; **5,977** control, **9,409** treatment, of ~81,000 applicants; 87% residential; avg stay 8 months; >75 trades): self-reported earnings ~2× SSA-reported; 1998 gap **$972** self-report vs **$218** SSA (**$393** on self-report subsample); 20-yr IRS follow-up (Schochet 2021): employment TOT **+4.2 pp** for 20–24s in 2015 (p<0.1); **−4.6 pp** for 18–19s in 2013–14; overall "essentially no impact"; baseline 20–24 vs 16–17: ever worked 90.4% vs 68.4%, $5.47 vs $4.71/hr, children 34.3% vs 8.6%.
25. **WIA Gold Standard** (randomization late 2010–early 2012; **28** sites stratified over 6 regions; Adult **2,974**, Dislocated **1,983**; three arms core / core+intensive / full-WIA): training take-up 34% / 41% / 50% in first three quarters (differential **≤16 pp**); training spend $3,223 of which $1,521 government; government cost **$2,409**/treatment subject; NDNH outcomes; nulls. New Jersey (Corson et al. 1989) and Texas (Bloom 1990) dislocated-worker pilots: JSA+training no better than JSA alone within 12 months.

### Judge-randomization studies (§5)
26. **Hyman (2018) TAA:** petitions 1974–2016 linked to LEHD (24 states + DC; snapshots 1985/2002–2011); leave-one-out investigator approval-rate instrument; +10 pp investigator leniency → +**6 pp** approval; balance F-test p = **0.18**; net **+20 months** of work and **+$50,000** over 10 years, fading by year 10; **20–40 pp** more likely to move commuting zone (similar for industry); training vs 3-year UI extension not separable.
27. **Humlum, Munch & Rasmussen (2025) Denmark:** birth-day-of-month caseworker assignment; **167,222** unemployment episodes, **127,713** people, **536** caseworkers, 2012–2017; simulated 58% rule-following; first stage +10 pp propensity → **+3.8 pp** classroom, **+2.1 pp** OJT; classroom training **+26 hours/month** in year 2 (≈**16%** of 160 h; "among the very largest in this review"), **+~20 pp** employment at quarter 7; OJT ≈ 0 (CIs ~2× wider; p for equality 0.03–0.22); classes average **52 days**; job-search courses 19 days; effects concentrate in new occupations; offshoring-exposed impacts >2× (p = 0.14); dropouts/never-starters show similar per-person impacts (puzzle); 65 balance checks: 5 and 12 significant at 0.1 vs ~6.5 expected.

### Prior meta-analyses (§6.1–6.4)
28. Smedslund et al. (2006): 46 studies (44 US, 2 Canada); employment **+9.7%** yr 1, **+9.2%** yr 2, **+3.7%** yr 5 (percent, not pp); earnings +4.3%, +4.4%, +1.1%; skills-training programs +5.6% employment, +4.5% earnings. Haelermans & Borghans (2012): 71 estimates / 38 studies, none randomized; OJT wage effect **3.9% → 2.6%** after publication-bias correction ("inflates the typical reported impact by 50%"). CKW (2018): 857 estimates / 207 papers; 502 Germanic/Nordic, 87 Anglo-Saxon; 418 training estimates, **54** randomized; training +1.4–2 pp yr 1, +4.0–4.6 pp more in yr 2+; +12 pts for long-term unemployed; +6 women; +3 under-25; +~3 pts per 1-pt rise in unemployment; equal study weights, SEs clustered by study; experimental ≈ 1 pt lower (ns). Peck et al. (2021): 46 career-pathways studies (27 RCT); targeted-occupation employment **26 → 45 pp** (+72%); total employment **+~6 pp** from ~60%; earnings **+$1,040/yr** over $16,320 base (3 yrs); >75 traits coded; block "survivor" selection (p<0.1 and standardized coef >0.1); rule of thumb 10 studies per correlate (→ ~4.6).

### Data & methods
- Search sources: Greenberg & Shroder (2004), Smedslund et al. (2006), Dutta-Gupta et al. (2016), CKW (2018), Peck et al. (2021), Katz et al. (2022), plus recent PACE/WorkAdvance follow-ups; "aggressive" search incl. Library of Congress, DOL library, retired authors, 2005 Digest of Social Experiments.
- Extraction: "We deploy Claude Opus—with engaged oversight—to extract the needed information… instruct Claude to: a) produce a 'reasoning table' documenting sources and logic for extracted values and b) perform an adversarial review of all extractions." Training-primary flag = "according to Claude's reading of reports".
- Timeframes adapted from CKW: short (yr 1, omitted as artifact-prone), medium (yr 2), long (yrs 3–5).
- Significance imputation where only stars reported: p = **0.005, 0.03, 0.075, 0.55** for <0.01, <0.05, <0.1, >0.1 (following Greenberg, Michalopoulos & Robins 2006); binary outcomes use the standard formula.
- REML random-effects; SEs clustered by study; ITT basis; block-based meta-regression with multiple imputation (10 datasets); benefit-cost model follows Schaberg & Greenberg (2020) WorkAdvance framework; five summary statistics (narrow B/C, broad B/C, MVPF, net/gross govt cost, societal IRR).
- Evidentiary standard: RCTs plus regression discontinuity and judge randomization; matching studies excluded (e.g. Rothstein et al. 2022) despite arguable credibility.

### Stated limitations / caveats (verbatim)
- "This project is not purely a systematic review, nor more specifically a meta-analysis. It was not structured from the start to mechanically filter and synthesize findings"
- "We do not claim to have perfectly applied our 'high evidentiary standard.' Notably, we do not cover any matching studies even though some are arguably as credible as research we include."
- "The humble warning in Card, Kluve, and Weber (2010)—'There are likely to be measurement errors and errors of interpretation in the extraction of information from the studies.'—applies as well to this AI-accelerated effort."
- "These uncertain imputations influence the meta-analytic, random-effects results."
- "The results are therefore geared to represent the impact of the typical study, not the average impact on participants across all studies."
- "no matter how rigorous the individual studies, meta-analytical comparisons among them are not as dispositive as to which factors cause training to be more effective as distinct from merely being correlated with them."
- "there may be a tendency to follow successful programs longer." / "The placement of randomized studies is indeed non-random."
- "In light of the great uncertainties in the projection of impacts, this result should be read as a little better than break-even."
- "A key limitation of this report, however, is that it only covers stand-alone job training programs… Beyond our scope are high school vocational programs, apprenticeships, community colleges, four-year colleges, professional schools, and online education."
- "We have no research evidence on how well job training helps people adjust when large language models start doing their jobs."
- "The body of evidence and experience is of course an imperfect match for an AI-disrupted future. If layoffs mainly affect white-collar workers, the new raft of long-term unemployed would be the most educated and highly paid in history."
- "We don't know if or when technological advances will cause a surge in unemployment; it's unclear which jobs would be most affected, and the unemployed population may look different from the subjects in these studies"
- "we assume away general equilibrium or displacement effects. If trainees displace other workers seeking the same jobs, the benefits we measure are inflated."
- "The ITT may be small just because the control group sought other similar programs."
- "many studies—including half of the sector program evaluations—are limited to surveys."

### Future work / recommendations (verbatim)
- "A 'fire drill' evaluation meant to rapidly scale and test leading job retraining programs could pay lasting dividends."
- "Scaling and randomizing the most promising programs would bring needed lessons."
- "future research should consider how traditional degree programs could be expanded and repurposed for this scenario."
- "funders should invest dramatically more in learning which components of the model are essential, and how best to replicate the model in more locations for more kinds of workers."
- "cutting-edge job matching approaches might be a crucial (and low-cost) tool for dealing with labor market disruption." (left out of scope)
- "Some of these investigations are evergreen: yielding helpful evidence regardless of AI's impact on unemployment."

### Open questions raised
- "if private charities… strike upon a promising system, can governments bring it to far more people without denaturing it?"
- Which sector-program components (selectivity, soft skills, coaching, employer hiring commitment) are causal.
- ITT vs LATE: which better models an AI-displacement world where "readiness to train" and training supply both shift.
- Why HMR's classroom effects are as large for dropouts/never-starters; why classroom beats OJT.
- Why the unemployment-rate association exists in the medium term but not long term (three theories offered).
- Whether short programs can serve displaced high-skill professionals ("compressed mid-career master's degree"); trigger-based (TAA-style) aid fails when displacement occurs via non-hiring rather than firing.
- Whether past performance "will underpredict future performance" if programs serve people with good work histories and demand for training surges.

### Terminology
- **training-primary / training-secondary**; **sector program / sectoral strategy**; **career pathways**; **ITT / LATE-program / LATE-training / TOT**; **Ashenfelter's dip**; **placebo check**; **judge randomization**; **creaming**; **Goodhart's Law**; **credibility revolution**; **narrow / broad B-C ratio**; **MVPF**; **societal IRR**; **survivors** (block-based meta-regression); **fire drill** evaluation; **train and pray**; **arbitrageurs or matchmakers**; **adaptive capacity** (Manning & Aguirre 2026: 356 professions; e.g. 1.7M secretaries/admin assistants at 59% exposure, 14% adaptive capacity).

---

## 7. How predictable is job destruction? Evidence from the Occupational Outlook

- **Date:** October 16, 2025 (WORKING PAPER)
- **Author:** Maxim Massenkoff, Naval Postgraduate School (maxim.massenkoff@nps.edu). RA: Jalaluddin Khan. Feedback: Alexander Barry, Tyler Borek, Ethan Heppner, Ezra Karger, Evan Rose, Nathan Wilmers.
- **URL:** http://maximmassenkoff.com/papers/OccupationalOutlooks.pdf
- Cited in the labor-market paper as the basis for "The government's own occupational growth forecasts, while directionally correct, have added little predictive value beyond linear extrapolation of past trends."

### Abstract claims (verbatim fragments)
- "across 4,000 unique predictions, occupations in the top third of projections grew significantly more in the subsequent three decades compared to ones in the bottom third."
- "The forecasts were especially accurate when they made reference to business practices… Technology-focused forecasts were less accurate because, on average, they underestimated the extent of job loss."
- "While the forecasts outperform naive extrapolations, the advantage is small, indicating that most of the explanatory power is captured in pre-existing trends."

### Quantitative findings (exact)
1. Core dataset: **23** issues/editions of the BLS Occupational Outlook, **1946–1996**, digitized; on average **238** occupations per publication; ~**4,000** unique predictions. Editions released every 2–3 years; 1949–1959 each sold ~**40,000** copies. The 1948 edition "Describes 250 occupations which cover approximately 107 million jobs."
2. Pooled terciles: top third grew "about **50 percentage points** faster than the bottom third over the three decades following their publication"; similar when weighting by occupation shares at time of report.
3. "Sixty years after the initial prediction, employment in the top tercile has **quadrupled** compared to a **doubling** in the bottom tercile."
4. Raw event-study (Fig 4a): 20 years after prediction, top tercile +**57%** vs bottom +**12%**; at year 40, "almost **100 percentage point** difference".
5. Naive benchmark (Fig 4b; terciles by growth over the most recent Census decade): at year 20 top +**50%** vs bottom +**11%**.
6. **Table 3** (log employment growth; Census-year FE; weighted by reference-year employment; two-way clustered SEs by job and Census): Outlook — Lowest tercile **−0.052*** (0.017)**, Highest **0.055** (0.020)**, Highest−Lowest **0.107 (0.024)**, R² **0.148**, N **12,613**. Naive — **−0.055* (0.027)**, **0.039* (0.021)**, lift **0.094 (0.026)**, R² **0.139**, N **12,534**. Combined — **−0.074*** (0.021)**, **0.045** (0.018)**, lift **0.120 (0.027)**, R² **0.154**, N 12,534. Text: lift ≈ **10** log points (Outlook), **9** (naive), **12** (combined).
7. **Table 4** (continuous ML predictions from XGBoost; Outlook and Census FE; N **9,526**): Outlook-embedding prediction coef **2.207*** (0.256)**, R² **0.299**; past-growth prediction **2.418*** (0.356)**, R² **0.156**; both: **1.913*** (0.255)** and **1.338*** (0.240)**, R² **0.332**. Text states R² **0.25** (Outlook) vs **0.16** (naive).
8. **Table A1** (normalized worker share outcome): Outlook lift **0.384 (0.071)**, Naive **0.340 (0.068)**, Combined **0.441 (0.073)**; R² 0.136 / 0.113 / 0.154.
9. **Table A2** (balanced panel of **132** occupations observed in all seven decades; N **9,254**): lifts **0.106 (0.024)**, **0.084 (0.026)**, **0.110 (0.025)**.
10. Decade-specific (Fig 5): both Outlook and naive ≈ **50 pp** growth difference at 20 years; at **40 years** the series diverge — Outlook "more informative" and naive less so.
11. **Table 5** topic regressions (Eq. 2; N **9,143**; Outlook × Census FE; Outlook variable = equal-weighted average of normalized growth score and XGBoost embedding prediction): Outlook × Technological **−0.110** (0.037)**; × Demographics **0.068* (0.034)**; × Business **0.094* (0.045)**; × Industry 0.145 (0.098); × Government 0.069 (0.043); × Geography −0.041 (0.062); × Consumers −0.033 (0.044). Share mentioning: Industry **95.1%**, Technological **56.1%**, Demographics 37.8%, Business 32.5%, Government 28.3%, Consumers 18.8%, Geography **18.2%**.
12. **Table 6** (N **11,212**; Census-year × Outlook-year FE): forecasts mentioning technology score **−0.562*** (0.110)** points lower on the 1–7 growth score (mean 4.861, SD 1.335); conditional on growth score, technology mention predicts **−0.306** (0.101)** lower actual growth (outcome mean 1.551, SD 1.243); growth score coefficient on actual growth **0.183*** (0.026)**. "predictions improve when an additional growth discount on the order of **30 percentage points** is added to forecasts mentioning technology."
13. Most recent Outlook (2023) mentions AI for "about **twenty** occupations".
14. Context cited: **37%** of US jobs could be done fully remotely (Dingel & Neiman 2020).

### Data
- Occupational Outlook editions 1946–1996 (23 issues), digitized; sections: nature of work, where employed, training, earnings, employment forecast. Pre-1970s forecasts are verbal, not quantitative.
- US Census via IPUMS (Ruggles et al. 2025), harmonized **occ1950** occupation codes; reference year = most recent Census before Outlook publication; event time = Census year − Outlook year, rounded to nearest decade.
- Unit of observation: (occupation)-(Outlook year)-(Census year); restricted to Census observations **5 to 34 years** after prediction "to approximate what would be useful to a prospective job seeker"; weighted by reference-year employment; Census years repeated across Outlooks.

### Methods
- **Growth score:** LLM converts each occupation's forecast text to 1–7 (1 = Rapid decline/obsolescence, 4 = Stable, 7 = Exceptional growth), with CONFIDENCE and REASONING fields (prompt in Appendix B).
- **Embedding-based prediction:** LLM strips occupation-specific context ("context-free" paragraphs, Appendix C), encode with **all-mpnet-base-v2** sentence embeddings, fit **XGBoost** ("basic hyperparameter tuning"); out-of-sample predictions used as continuous forecast; same procedure for naive predictor "to give both forecasts similar flexibility in functional form."
- **Naive benchmark:** rank occupations by growth over the most recent Census decade available at publication.
- **Eq. 1:** Y_iot = α_t + β1·BottomTercile_iot + β3·TopTercile_iot + e_iot; estimand β3 − β1 ("lift"); terciles by Outlook, naive, or unweighted average of the two.
- **Eq. 2:** Y_iot = α_ot + β1·Outlook_iot + β2·Topic_io + β3·Outlook_iot × Topic_io + e_iot; α_ot = Outlook-by-Census FE; β3 of interest; seven topics each in a separate regression.
- Decade-specific: forecasts interacted with time horizon; 95% CIs.
- Robustness: normalized worker share outcome; balanced 132-occupation panel; continuous ML predictions.

### Stated limitations / caveats (verbatim)
- "One limitation of the LLM-based approach is that, even if instructed not to, the model might incorporate occupation-specific contextual knowledge when generating numeric ratings rather than focusing solely on the growth language."
- "the forecasting task may not have been that hard in the first place."
- "This does not necessarily mean that infusing a forecast with business-related insights would cause it to be more accurate. It could be, for example, that forecasts mentioning these factors were written by people with deeper knowledge of the occupation. So varying levels of expertise is one reason to be cautious about a causal interpretation."
- "Note though that this does not mean that technological innovations tended to be bad for employment growth—it could be that the Outlook's authors only thought to mention technological shocks that would displace labor."
- "these predictions were not that much better than a naive forecast based only on growth over the previous decade. One implication is that, in general, jobs go away slowly: over decades rather than years."
- "But there are key reasons why this time could be different… If this is true, the coming economic changes could dwarf the slow—and predictable—displacement that once sidelined teamsters, elevator operators, and farmers."

### Open questions raised
- Why the Outlook becomes more informative than the naive forecast only at 40+ years ("may have been picking up on deeper shifts in the labor market").
- Whether warnings/forecasts can actually change worker behaviour (cites Wiswall & Zafar 2015; Cederlöf et al. 2025; Cattaneo et al. 2025) — motivation, not tested.
- Whether AI-era displacement will be fast enough to break the historical predictability pattern.
- Accuracy of the ~20 AI-referencing forecasts in the 2023 Handbook (untestable yet).

### Terminology
- **Occupational Outlook**; **growth score** (1–7); **optimism** terciles; **naive prediction / hands-off prediction**; **lift**; **event time**; **normalized growth**; **context-free version**; **topic** dummies (Industry, Technological, Demographics, Government, Geography, Business, Consumers); **predictive lift by years since prediction**.

---

## 8. How AI is transforming work at Anthropic

- **Date:** December 2, 2025
- **Authors:** Saffron Huang, Bryan Seethor, Esin Durmus, Kunal Handa, Miles McCain, Michael Stern, Deep Ganguli
- **URL:** https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
- **Bibtex key:** huang2025aiwork

### Quantitative findings (exact, from the page)
1. Survey: **132** Anthropic engineers and researchers; **53** in-depth qualitative interviews ("first 53 people who responded").
2. Sampling: **68** responses via Slack (convenience); direct outreach to **20** teams (5–10 people each), **207** contacted, **64** responses = **31%** response rate.
3. Timing: **August 2025**, when Claude Sonnet 4 and Opus 4 were the most capable models.
4. Use Claude in daily work: **59%** now vs **28%** twelve months earlier.
5. Self-reported productivity gain: **+50%** average now vs **+20%** a year earlier ("2–3x increase year-over-year in both usage and productivity").
6. **14%** report >**100%** productivity increases.
7. Daily use for: debugging **55%**; code understanding **42%**; implementing new features **37%**.
8. More than half can "fully delegate" only **0–20%** of their work.
9. **27%** of Claude-assisted work "wouldn't have been done otherwise"; on average **44%** of Claude-assisted work consists of tasks employees would not have enjoyed.
10. Claude Code transcript analysis (**~200,000** internal transcripts, Feb 2025–Aug 2025, Clio): task complexity **3.2 → 3.8** on a 1–5 scale; max consecutive tool calls **9.8 → 21.2** (+116%); human turns per transcript **6.2 → 4.1** (−33%); feature implementation **14.3% → 36.9%** of usage; code design/planning **1.0% → 9.9%**; papercut fixes **8.6%** of current tasks.
11. Merged PRs per engineer per day: **+67%** after Claude Code adoption.
12. Team splits: pre-training team **54.6%** of Claude Code usage for new features; security team **48.9%** code understanding; non-technical employees **51.5%** debugging, **12.7%** data science.
13. Complexity scale anchors: 1.0 basic edits; 3.2 "troubleshoot Python module import errors"; 3.8 "implement and optimize caching systems"; 5.0 expert-level weeks/months of work.

### Data & methods
- Mixed methods: Slack convenience sample + stratified team outreach; survey questions publicly shared; qualitative interviews; Clio privacy-preserving analysis of Claude Code transcripts with proportionate sampling across time periods; task classification on complexity scale; telemetry (tool calls, human turns).

### Stated limitations (verbatim)
- "There is likely some selection bias here, as people who are particularly engaged with Claude or have strong opinions (positive or negative) may have been more likely to respond, while those with more neutral experiences may have been underrepresented."
- "Responses may be affected by social desirability bias (since responses were not anonymous and all participants are Anthropic employees, respondents may have inflated positive assessments of Claude's impact)"
- "Recency bias (asking participants to recall their productivity and usage patterns from 12 months ago is subject to memory distortion)"
- "Productivity is in general very difficult to estimate, so these self-reports should be taken with a grain of salt."
- "There is recent work from METR, an AI research nonprofit, showing that experienced developers working with AI on highly familiar codebases overestimated their productivity boost from AI."
- "It is also not clear from our data where reported time savings are being reinvested—whether into additional engineering tasks, non-engineering tasks, interacting with Claude or reviewing its output, or activities outside of work."
- "Our Claude Code analysis uses proportionate sampling across time periods, which means we can only measure relative changes in task distribution, not absolute changes in work volume." "…when we report that feature implementation increased from 14% to 37% of Claude Code usage, this does not necessarily indicate that more total feature work is being done."
- "We recognize that studying AI's impact at a company building AI means representing a privileged position…"
- "our findings likely don't generalize to other organizations or contexts right now"
- "future research would benefit from anonymous data collection and more robustly validated measurement instruments." "Further research is needed to disentangle these effects."

### Open questions raised
- "paradox of supervision": can engineers supervise Claude if skills atrophy from disuse?
- How mentorship changes when juniors ask Claude instead of seniors; what skills remain valuable; whether SWE roles exist in current form in a few years; how CS curricula should adapt; where time savings are reinvested; generalisation across organisations.

### Terminology
- **full-stack**; **papercuts**; **paradox of supervision**; **cold start problem**; **vibe coding**; **trust progression**; **task complexity scale**; **tool calls**; **human turns**; **output volume**; **manager of AI agents**.

---

## 9. Economic Futures program and the $200M Research Fund (brief)

### Economic Futures program (launched June 2025; UK/Europe expansion Nov 5, 2025)
- **URLs:** https://www.anthropic.com/economic-futures ; https://www.anthropic.com/economic-futures/program
- Three pillars: (1) catalyzing independent research (grants, API credits, partnerships); (2) policy development (symposia); (3) economic measurement (scaling the Anthropic Economic Index as "one of the first longitudinal datasets on AI's economic usage, diffusion, and impact").
- **Rapid research awards:** **$10,000–$50,000** grants plus **$5,000** in Claude API credits per recipient; **6-month** completion window; currently not accepting applications.
- **Symposia:** Washington, D.C. (September 2025; application deadline July 25, 2025; partner McCourt School of Public Policy, Georgetown) and London (November 2025; deadline September 12, 2025; partner LSE Data Science Institute). Travel, accommodation, honorarium provided. DC symposium policy proposals published.
- Research themes (eight): labor market transitions, human-AI complementarity, productivity effects, value creation, fiscal policy adaptation, international impacts, plus geographic/enterprise adoption and "economic primitives".

### Economic Futures Research Fund (announced June 10, 2026; research agenda published July 22, 2026)
- **URL:** https://www.anthropic.com/news/economic-futures-research-fund-agenda
- **$200 million** total; grants "primarily in the **$5 million to $30 million** range, with flexibility upward"; **$1 million** floor. Alongside a separate **$150 million** national fellowship program for early-career professionals (per press coverage).
- Five priority areas: (1) shaping AI's impact on workers at the firm/workplace level (field experiments on organizational choices, worker voice; retention tax credits, employer co-investment); (2) equipping people to navigate AI-driven transitions (retraining, job placement, licensing reform, sectoral packages, early-career pipeline experiments, paid retraining leave); (3) modernizing income support (UI reforms, automatic extension triggers, wage insurance, longer-duration unconditional income pilots); (4) building worker stakes in AI-driven growth (pre-distributive capital accounts, equity-sharing, dividends, automation/capital-gains/corporate taxes); (5) new evidence on public investments (human-facing service roles, AI-enabled public services, guaranteed jobs, place-based interventions).
- Eligibility: accredited universities, research institutes, policy research orgs, nonprofits "with a track record of running field experiments at scale"; individuals as PIs only via institutional proposals. Application via RFP/Google Form; no deadline stated.
- Stated lesson from the earlier program: "it's hard for us to scale capacity to manage many small grants at once" — hence larger grants.
- Note the direct link to paper 6: the retraining review's call for a "fire drill" evaluation of sector programs maps onto priority area (2).

---

## Methods the team uses (checklist, with source paper)

**Measurement / construct-building**
- [ ] Task-level exposure built from O*NET tasks × theoretical capability (Eloundou β, upgraded 0.5→1) × observed usage gate (WorkUsage ≥ 100 / 0.0025%) × automation factor α (augmentative = 0.5, automative = 1), time-fraction weighted to occupation, employment-weighted to category — *Labor market impacts* (+ appendix).
- [ ] Splitting counts across near-identical O*NET tasks by employment share; rejecting DWA/IWA aggregation; Spearman heatmap across measure variants as robustness — *Labor market impacts appendix*.
- [ ] Work-related vs personal/educational filter via Economic Index "use case primitive"; 1P API traffic as a signal of production integration — *Labor market impacts*; *Economic primitives report* (cited).
- [ ] LLM-based classifiers with published prompts, single forced-choice call (Sonnet 4.6, temp 0.2), truncation limits, aggregation over minimum distinct users (Clio-style privacy) — *Returns to expertise*; *81k*; *How AI is transforming work*.
- [ ] Converting qualitative text into ordinal scores with an LLM (1–7 growth score; 1–7 productivity; 1–5 expertise; 0–5 success/failure signals) and hedging with an embeddings + XGBoost variant — *Occupational Outlook*; *81k*; *Returns to expertise*.
- [ ] "Verified" outcomes = judged outcome AND ≥1 hard telemetry/transcript signal; abandonment = failure AND zero lines of code — *Returns to expertise*.
- [ ] Freelance-posting-calibrated task value (Haiku summarizer → Opus pricer against 200 tier-balanced postings), used ordinally — *Returns to expertise appendix*.
- [ ] Occupation inference from context, explicitly not from the act of coding; separate "user profile" vs "work performed" occupation classifiers — *Returns to expertise*.
- [ ] Inferring occupation/career stage from open-ended survey text, leaving missing when unclear (61% missing), robustness on explicit-mention subsample — *81k*.

**Identification / estimation**
- [ ] Difference-in-differences on CPS: top-quartile exposure vs zero-exposure (30%), 2022 baseline, pooled post-ChatGPT estimate with CI → "detectable effect size" statement; cutoff varied median→95th pct — *Labor market impacts*.
- [ ] Priority outcome = unemployment rate (harm-focused); secondary = monthly job-start rate from CPS panel for ages 22–25 — *Labor market impacts*.
- [ ] Administrative cross-check (DOL ETA 203 UI claims by state × SOC) against survey (CPS) — *Labor market impacts appendix*.
- [ ] Employment-weighted occupation-level OLS and 25-bin binned scatter against BLS projections as external validation — *Labor market impacts*.
- [ ] Occupation-level linear fit of survey sentiment on exposure ("per 10 pp exposure, +1.3 pp job threat") — *81k*.
- [ ] Session-level OLS with cumulative fixed effects (work mode, task-value band, month, task subject, occupation group, model family, session length), SEs clustered by user; step-function version with novice omitted — *Returns to expertise appendix*.
- [ ] Survey OLS with career-stage, discipline and survey-week FE, robust SEs, β ÷ control mean → percent; Poisson check; pilot sample without AI-recruitment framing as selection check — *Coding agents in social sciences appendix*.
- [ ] Event-study terciles + OLS with Census-year FE, weighted by reference-year employment, two-way clustered SEs (job, Census); naive extrapolation benchmark; combined forecast; horizon-interacted coefficients; topic × forecast interactions — *Occupational Outlook*.
- [ ] REML random-effects meta-analysis with study-clustered SEs; ITT basis; LATE scaling by take-up differentials; block-based "survivor" meta-regression with multiple imputation (10 sets); significance imputation from stars; benefit-cost with five summary statistics (narrow/broad B-C, MVPF, net/gross cost, IRR) — *Worker retraining*.
- [ ] AI-assisted extraction from long reports with "reasoning table" + adversarial self-review — *Worker retraining*.

**Validation / robustness habits**
- [ ] Classifier vs telemetry agreement (>90%); strong-reference-model agreement with blind adjudication (Mythos Preview); internal replication with author fixed effects on observable outcomes (commits landing) — *Returns to expertise appendix*.
- [ ] Reporting effects both unadjusted and adjusted; emphasising relative over absolute estimates when the measure is biased — *Returns to expertise*; *Coding agents*.
- [ ] Balanced-panel and alternative-outcome robustness (worker share; 132 always-observed occupations) — *Occupational Outlook*.
- [ ] Explicit scenario benchmarks for what the design could detect (top-10% layoff → 3%→43%; Great Recession doubling → 3%→6%) — *Labor market impacts*.
- [ ] Time-series comparison of the same measure across windows (Oct 2025→Apr 2026; 6-month Claude Code windows; 12-month recall) — *Returns to expertise*; *How AI is transforming work*.
- [ ] Repeated cross-sections planned as monitoring instruments (monthly rotating Economic Index Survey; periodic re-runs of exposure/unemployment analysis) — *Survey announcement*; *Labor market impacts*.

**Framing habits**
- [ ] Historical humility priors (offshorability, robots, China shock, Outlook forecasts) before any AI claim — *Labor market impacts*; *Occupational Outlook*.
- [ ] Early-career / ages 22–25 as the canary subgroup — *Labor market impacts*; *81k*; *Coding agents* (doctoral students).
- [ ] Naming "what would change our conclusion" (returns to expertise falling; non-software success share rising) — *Returns to expertise*.
- [ ] Linking usage data to survey sentiment and to external labour data (BLS wages, CPS, UI) — *81k*; *Labor market impacts*.

## Questions the authors explicitly leave open

- Which workers count as "treated" under partial task coverage (O-ring vs mean vs concentrated exposure); whether an absolute coverage threshold should replace the top-quartile rule as capabilities advance — *Labor market impacts*.
- Why observed exposure correlates with BLS projections but the Eloundou measure does not — *Labor market impacts*.
- Where un-hired 22–25-year-olds go (staying put, other jobs, school, non-participation); whether job transitions are mismeasured in CPS — *Labor market impacts*.
- How recent graduates with credentials in exposed fields are navigating the labour market (named "key next step") — *Labor market impacts*.
- Extending observed exposure to other providers' usage data and other countries — *Labor market impacts* (footnote 3).
- Calibrating O*NET task specificity and representing task interdependency — *Labor market impacts appendix*.
- Where AI's surplus accrues (workers, managers, consumers, corporations) — only ~25% of respondents named a recipient; enterprise users unobserved — *81k*.
- Confirming inferred occupation/career-stage/productivity variables in structured surveys — *81k*; addressed in part by the monthly *Economic Index Survey*.
- Mechanism behind the U-shaped speedup–threat relationship — *81k*.
- Whether the returns to expertise will fall as models supply judgment; whether non-software occupations' success share keeps rising — *Returns to expertise*.
- Whether expertise effects are causal or selection (task choice, unobservables) — only "partially" addressed — *Returns to expertise*.
- Why management occupations out-succeed software engineers (skill vs measurement artefact) — *Returns to expertise*.
- Measuring non-interactive/headless Claude Code usage ("a priority for future work") — *Returns to expertise*.
- Real-world outcomes of sessions (is the code used? economically valuable?) — *Returns to expertise*.
- Validating LLM classifiers when sessions exceed human labelling capacity — *Returns to expertise appendix*.
- Causal effect of coding-agent access on research output and content (RCT pending); why gains appear in projects/working papers but not journal submissions; quality vs quantity; congestion/selective-reporting fears; steeper gender and institutional gradients — *Coding agents in the social sciences*.
- Whether forecasts/warnings change worker behaviour; why Outlook forecasts only beat naive extrapolation at 40+ years; whether AI displacement will be too fast to be predictable — *Occupational Outlook*.
- Where engineers' time savings are reinvested; the "paradox of supervision"; mentorship and curriculum implications; generalisation beyond Anthropic — *How AI is transforming work at Anthropic*.
- Can governments scale private sector programs "without denaturing" them; which program components are essential; ITT vs LATE as the right forecast object for an AI shock; why classroom > OJT in Denmark and why dropouts benefit; short programs vs multi-year reskilling for high-skill workers; trigger-based aid when displacement is via non-hiring — *Worker retraining*.
- Job-matching approaches, apprenticeships, and degree-program repurposing as untested channels — *Worker retraining*.
