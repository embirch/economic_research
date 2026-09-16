# economic-index-2025-09-report — The Anthropic Economic Index report: Uneven geographic and enterprise AI adoption

## Source

- **Title (PDF cover, p.1):** "The Anthropic Economic Index report: Uneven geographic and enterprise AI adoption". The web page's H1 reads "Anthropic Economic Index report: Uneven geographic and enterprise AI adoption" (no leading "The"); the browser title is "Economic Index: Uneven AI adoption".
- **Authors (p.1, and the "Authors and Acknowledgments" block on the web page):** Ruth Appel\*, Peter McCrory\*, Alex Tamkin\*, Miles McCain, Tyler Neylon, Michael Stern. "\*Lead authors. Contributed equally to this report." (p.1)
- **Published:** September 15, 2025 (p.1; web page date line "Sep 15, 2025").
- **Document type:** Economic Index report (the report calls itself "This third iteration of the Anthropic Economic Index Report", p.46). No separate appendix document exists; the methodology lives in per-chapter endnotes and in the release's own `data_documentation.md`.
- **URLs:**
  - Primary web page (summary of record for the general reader): https://www.anthropic.com/research/anthropic-economic-index-september-2025-report
  - PDF (document of record): https://assets.anthropic.com/m/218c82b858610fac/original/Economic-Index.pdf
  - arXiv version (posted later, 19 Nov 2025): https://arxiv.org/abs/2511.15080 (arXiv:2511.15080 [econ.GN], DOI 10.48550/arXiv.2511.15080)
- **Page count:** 48 PDF pages. p.1 is the unnumbered cover; printed page numbers 2–47 correspond exactly to PDF pages 2–47; PDF p.48 is blank. All page references below are to the printed number (= PDF page index).
- **Structure:** Introduction (pp.2–6, with endnotes 1–5 on p.6) · Chapter 1 "Claude.ai Usage Over Time" (pp.7–11, endnotes 1–5 on p.11) · Chapter 2 "Claude usage across the United States and the globe" (pp.12–29, endnotes 1–9 on pp.28–29) · Chapter 3 "API Enterprise Deployment of Claude" (pp.30–45, endnotes 1–14 on pp.44–45) · "Concluding remarks" (pp.46–47, endnote 1 on p.47). 11 numbered figures in Chapter 2 counting from Figure 2.1; 9 figures and 1 table in Chapter 3; 2 figures in Chapter 1; 2 tables in Chapter 2.
- **Release it rests on:** `release_2025_09_15` of the Hugging Face dataset `Anthropic/EconomicIndex`. Both samples are drawn from the window **4–11 August 2025**: the released files are `data/intermediate/aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv`, `data/output/aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv` and `data/intermediate/aei_raw_1p_api_2025-08-04_to_2025-08-11.csv`. The release also ships the only `code/` library in the dataset (6 `.py` + 4 `.ipynb`), a `data_documentation.md` (20,133 bytes) and a replication `README.md`.
- **Prior waves it compares against:** V1 = the first report's December 2024 / January 2025 sample; V2 = the second report's February / March 2025 sample; V3 = this report's August 2025 sample (p.7). V1 and V2 enter through four files carried into this release: `automation_vs_augmentation_v1.csv`, `automation_vs_augmentation_v2.csv`, `task_pct_v1.csv`, `task_pct_v2.csv`.
- **Companion:** a short blog post published the same day, "Anthropic Economic Index: Tracking AI's role in the US and global economy" (`economic-index-2025-09-blog`), is a separate wiki entry.

---

## Claims

Every substantive empirical claim, numbered, with page and figure/table reference, the number as published, and the comparison it rests on.

### Introduction and headline summary (pp.2–6)

1. **40% of US employees report using AI at work, up from 20% two years earlier** (p.2). Comparison: 2025 vs 2023, self-report. Not Anthropic data — attributed in endnote 1 (p.6) to "Gallup 2025, AI Use at Work Has Nearly Doubled in Two Years."
2. **Coding is 36% of the total Claude.ai sample; educational tasks rose from 9.3% to 12.4% and scientific tasks from 6.3% to 7.2%** (p.3, headline bullet). Comparison: V1 → V3 shares of sampled conversations. Note: the V3 figures in this bullet (12.4%, 7.2%) do not match the V3 values plotted in Figure 1.1 (12.7%, 7.4%) — see §What it did not test, item I1.
3. **"Directive" conversations jumped from 27% to 39%** (p.3). Comparison: V1 → V3 share of sampled Claude.ai conversations classified directive.
4. **Program creation in coding +4.5pp and debugging −2.9pp** (p.3). Comparison: V2 → V3 task shares. Note: Chapter 1 (p.9) gives the debugging change as −2.8pp; the −2.9pp figure appears only in the summary bullet.
5. **Geographic cuts released for 150+ countries and all U.S. states, for the first time** (p.3). Comparison: against prior Index releases, which had no geography.
6. **Singapore 4.6x and Canada 2.9x expected usage; Indonesia 0.36x, India 0.27x, Nigeria 0.2x** (p.3). Comparison: each country's share of global Claude.ai usage against its share of global working-age population. Note: Chapter 2's own figure for Singapore is 4.57 (Figure 2.2, p.14) and its overview text says "4.5 times" (p.12).
7. **DC leads US per-capita usage at 3.82x its population share; Utah is close behind at 3.78x** (p.3). Comparison: state share of US Claude.ai usage against state share of US working-age population.
8. **Coding is over half of all usage in India versus roughly a third of all usage globally** (p.4). Comparison: India vs global O*NET task mix.
9. **After controlling for task mix, low-AUI countries are more likely to delegate complete tasks (automation) while high-adoption areas tend toward learning and human-AI iteration (augmentation)** (p.4). Comparison: partial regression of automation share on AUI across countries, both residualised on task-mix-predicted automation.
10. **77% of business (1P API) uses involve automation usage patterns, compared to about 50% for Claude.ai users** (p.5). Comparison: 1P API transcripts vs Claude.ai conversations, same window.
11. **The most-used tasks in the API data tend to cost more than the less frequent ones; "we find evidence of weak price sensitivity"** (p.5). Comparison: across O*NET tasks, cost index vs usage share.
12. **API customers using Claude for complex tasks tend to provide lengthy inputs — "Context constrains sophisticated use"** (p.5). Comparison: across O*NET tasks, input token index vs output token index.
13. **"At present, geographic usage patterns are only available for Claude.ai traffic."** (p.5). A stated scope limit on the released data: no geography for the API sample.

### Chapter 1 — Claude.ai usage over time (pp.7–11)

14. **Computer and Mathematical tasks are 36% of usage** in the text (p.7); Figure 1.1 (p.8) plots **37.2% (Jan 2025 / V1) → 39.6% (Mar 2025 / V2) → 36.9% (Aug 2025 / V3)**. Comparison: SOC major group share of sampled conversations, three waves.
15. **Educational Instruction and Library rose from 9% in V1 to 12% in V3** (p.7); Figure 1.1: **9.3% → 11.0% → 12.7%**.
16. **Life, Physical, and Social Science increased from 6% to 7%** (p.7); Figure 1.1: **6.3% → 6.8% → 7.4%**.
17. **Business and Financial Operations fell from 6% to 3%** (p.7); Figure 1.1: **5.9% → 4.4% → 3.1%**.
18. **Management dropped from 5% to 3%** (p.7); Figure 1.1: **4.5% → 3.1% → 2.7%**.
19. **Figure 1.1 also reports three groups not discussed in the body text** (p.8): Arts, Design, Entertainment, Sports, and Media **10.2% → 9.4% → 8.5%**; Office and Administrative Support **7.8% → 7.0% → 8.4%** (the only non-monotone panel, falling then rising); Architecture and Engineering **4.7% → 3.8% → 2.5%**.
20. **"Search electronic sources, such as databases or repositories, or manual sources for information" grew from 0.03% to 0.49%** (p.8; endnote 1, p.11), attributed to the March web-search release. Comparison: V2 → V3 O*NET task share.
21. **"Conduct internet-based and library research" grew from 0.003% to 0.27%** (p.8; endnote 1, p.11), attributed to the April Research mode. Comparison: V2 → V3.
22. **Tasks relating to developing instructional materials increased by 1.3pp, from 0.2% to 1.5% — "a more than 6-fold increase"** (p.8). Endnote 2 (p.11): "Statistic computed from tasks containing the string 'develop instructional materials'."
23. **Creating multimedia documents rose 0.4pp, "nearly tripling" from 0.16% to 0.55%** (p.8), attributed to the Artifacts feature.
24. **Tasks involving creating new code more than doubled, +4.5pp from 4.1% to 8.6%; debugging and error correction fell 2.8pp from 16.1% to 13.3% — "a net 7.4pp shift toward creation over fixing code"** (p.9). Comparison: V2 → V3, aggregated over the task lists in endnote 3 (p.11).
25. **Endnote 3 (p.11) gives the underlying task-level moves** (V2 → V3), for tasks whose frequency changed by ≥0.2pp. Creation: "write new programs or modify existing programs" 1.5% → 4.9%; "design, build, or maintain web sites" 1.2% → 2.0%; "write, analyze, review, and rewrite programs" 1.2% → 0.5%; "develop new software applications" 0.06% → 0.6%; "develop transactional web applications" 0.1% → 0.3%; "develop application-specific software" 0.05% → 0.3%. Debugging/error correction: "modify existing software to correct errors" (two variants) 2.5% → 3.8% and 4.8% → 2.7%; "correct errors by making appropriate changes" 3.0% → 2.1%; "perform initial debugging procedures" 2.0% → 0.9%; "diagnose, troubleshoot, and resolve hardware/software problems" 1.6% → 2.5%; "review and analyze computer printouts to locate code problems" 1.3% → 0.9%; "determine sources of web page or server problems" 0.9% → 0.4%.
26. **The directive share jumped from 27% in V1 to 39% in V3, "primarily at the expense of task iteration and learning interactions"; "This is the first report where automation usage exceeds augmentation usage."** (p.9).
27. **Figure 1.2 (p.10), left panel: automation 41.1% (V1) → 41.7% (V2) → 49.1% (V3); augmentation 55.5% → 55.1% → 47.0%** *(figure label — all six values are printed data labels inside the figure, read from a page render; marking added 2026-09-16 per `room/director-2026-09-16-figure-values-ruling.md` and `room/referee-2026-09-16-corpus-audit.md` defect L6, which verified the six against the source)*. Comparison: share of sampled Claude.ai conversations by aggregated collaboration mode, three waves. The crossover happens between V2 and V3.
28. **Figure 1.2 (p.10), right panel plots all five modes across V1–V3** (directive, feedback loop, task iteration, validation, learning). Directive rises **from 27% to 39%** — those two endpoints are published body text, "The share of directive conversations sampled from Claude.ai conversations jumped from 27% in V1 in late 2024 to 39% in V3" (p.9, and claim 26), and are the only numbers in this claim that are published. The other four series: task iteration falls from ~30% to ~22%, learning from ~27% to ~20%, feedback loop from ~14% to ~10%, and validation rises from ~3% to ~4% *(wiki author's reading from axis position on a page render; the right panel prints no data labels; not published values)*. Reworded 2026-09-16 under `room/director-2026-09-16-figure-values-ruling.md` and `room/referee-2026-09-16-ledger-threads-verdict.md` §G, after re-rendering p.10 at 130 dpi: the **left** panel carries six printed data labels (claim 27), the **right** panel carries none. **The five-mode series does not have to be read off this plot.** It is reproducible exactly from the collaboration facet of `release_2025_02_10`, `release_2025_03_27` and `release_2025_09_15` (`data/ATLAS.md` §Conventions), so a post wanting these values asks the data steward for them and never cites this figure.
29. **Robustness on the classifier change (endnote 4, p.11): rerunning the V3 data with Claude Sonnet 3.7 still shows directive interactions rising significantly, "though to a lower absolute level of 45% automation versus 49% with Sonnet 4".** Comparison: same V3 sample, two classifier models. The endnote also states the shift "is not driven by changes in task mix — the shift toward directive interactions appears across a wide range of occupational categories".

### Chapter 2 — Geography (pp.12–29)

30. **The sample is "a privacy-preserving analysis of 1 million Claude.ai conversations"** (p.12), specified in endnote 2 (p.28) as 1 million Claude.ai Free and Pro conversations from 4–11 August 2025, randomly sampled from conversations not flagged as potential trust-and-safety violations.
31. **The United States accounts for 21.6% of total global Claude.ai usage; India 7.2%; Brazil 3.7%** (pp.12–13, Figure 2.1). Comparison: country share of the global sample, unadjusted for population.
32. **Figure 2.1 (p.13) — top 30 countries by share of global Claude.ai usage:** United States 21.6%, India 7.2%, Brazil 3.7%, Japan 3.7%, South Korea 3.7%, United Kingdom 3.2%, Germany 2.6%, France 2.2%, Canada 2.1%, Australia 1.9%, Indonesia 1.9%, Italy 1.5%, Thailand 1.3%, Israel 1.1%, Vietnam 1.1%, Spain 1.1%, Turkey 1.1%, Poland 1.0%, Taiwan 1.0%, Pakistan 1.0%, Mexico 1.0%, Philippines 0.9%, Colombia 0.8%, The Netherlands 0.8%, Nigeria 0.7%, Argentina 0.6%, Ukraine 0.6%, Egypt 0.6%, Singapore 0.6%, South Africa 0.5%. Caption: "The data includes Claude.ai Free and Pro conversations."
33. **Israel leads global per-capita usage with an AUI of 7 — "its working-age population uses Claude 7x more than expected based on its population"; Singapore 4.57, Australia 4.10, New Zealand 4.05, South Korea 3.73** (p.14, Figure 2.2).
34. **Figure 2.2 (p.14) — top 20 countries by AUI, with sample sizes:** Israel 7.00 (N = 10.9k), Singapore 4.57 (5.4k), Australia 4.10 (18.8k), New Zealand 4.05 (3.6k), South Korea 3.73 (35.3k), United States 3.62 (208.2k), Estonia 3.11 (701), Canada 2.91 (20.4k), Malta 2.83 (283), Switzerland 2.81 (4.3k), Luxembourg 2.74 (333), United Kingdom 2.67 (30.5k), The Netherlands 2.56 (7.8k), Cyprus 2.39 (587), Denmark 2.31 (2.3k), Taiwan 2.29 (9.7k), Norway 2.26 (2.1k), Ireland 2.26 (2.1k), Sweden 2.20 (3.8k), Georgia 2.19 (1.3k). Comparison: usage % / working-age population %, restricted to countries with ≥200 observations.
35. **Table 2.1 (p.15) — AUI tiers across countries:** Leading (top 25%) AUI 1.84–7.00, 37 countries (examples: Israel, Monaco, Singapore, Australia, New Zealand); Upper middle (50–75%) 0.89–1.71, 35 countries (Czechia, Austria, Slovenia, Poland, Armenia); Lower middle (25–50%) 0.37–0.85, 39 countries (Peru, Seychelles, Colombia, Albania, Argentina); Emerging (bottom 25%) 0.01–0.36, 53 countries (Indonesia, Ghana, Kuwait, Mongolia, Rwanda); Minimal 0.00–0.00, 25 countries (Aruba, Tonga, Nauru, Samoa, Palau). Total 189 countries assigned. Note the gaps between adjacent tier ranges (1.71→1.84, 0.85→0.89, 0.36→0.37): the quartile cut-points come from the ≥200-observation subset while the tier assignment is applied to all countries.
36. **Figure 2.3 (p.15)** is a world map of the same tiers plus "Claude not available" and "No data" categories; the caption's finding is that "countries in North America, Europe and Oceania" lead in Claude adoption per working-age capita.
37. **Israel and Singapore both "rank highly in the Global Innovation Index"** (p.16). Comparison: the report's own AUI ranking against an external innovation ranking (WIPO Global Innovation Index 2024, linked from the web page). Presented as interpretation, not as a computed correlation.
38. **United States AUI 3.62, Canada 2.91, United Kingdom 2.67, France 1.94, Japan 1.86, Germany 1.84** (p.16). Comparison: major developed economies against each other and against the small leaders.
39. **Bolivia 0.48, Indonesia 0.36, India 0.27, Nigeria 0.2** (p.16). Comparison: below-1 AUI economies against the proportional benchmark of 1.
40. **A 1% increase in GDP per capita is associated with a 0.7% increase in Claude usage per capita** (p.16). Figure 2.4 (p.17) reports **β = 0.690 (p < 0.001), R² = 0.709**, labelled "Power law: AUI ~ GDP^0.69". Comparison: OLS of ln(AUI) on ln(GDP per working-age capita in USD), countries with ≥200 observations, log-log.
41. **Within the US, California leads total usage with 25.3%; New York 9.3%, Texas 6.7%, Virginia 4.0%** (p.18). Comparison: state share of US usage, unadjusted for population.
42. **The District of Columbia leads the state AUI at 3.82, "indicating that Claude usage in DC is 3.82x greater than its share of the country's working-age population"; Utah 3.78, "notably ahead of California (2.13), New York (1.58) and Virginia (1.57)"** (p.18).
43. **Figure 2.5 (p.19) — top 20 US states by AUI, with sample sizes:** District of Columbia 3.82 (N = 1.8k), Utah 3.78 (8.3k), California 2.13 (52.6k), New York 1.58 (19.3k), Virginia 1.57 (8.4k), Washington 1.51 (7.5k), Massachusetts 1.42 (6.4k), Colorado 1.30 (4.9k), Vermont 1.10 (430), Nevada 1.08 (2.2k), Oregon 1.02 (2.7k), Missouri 0.99 (3.7k), Maryland 0.98 (3.8k), Illinois 0.88 (6.9k), Connecticut 0.87 (2.0k), New Hampshire 0.85 (736), New Jersey 0.85 (4.9k), Hawaii 0.84 (685), Georgia 0.80 (5.6k), Minnesota 0.77 (2.7k). Restriction: states with ≥100 observations.
44. **The state-level income–adoption correlation is "similar, but weaker" than the cross-country one; "Income differences explain less than half the variation in cross-state adoption rates"; but adoption rises faster with income — "Each 1% increase in state GDP per capita is associated with a 1.8% increase in the AI Usage Index"** (p.19). Comparison: cross-state log-log elasticity 1.8 against the cross-country 0.7, with a lower R² at state level. No state-level R², β standard error or figure is given.
45. **Table 2.2 (p.20) — AUI tiers across US states:** Leading (top 25%) 0.98–3.82, 13 states (DC, Utah, California, New York, Virginia); Upper middle (50–75%) 0.71–0.88, 12 states (Illinois, Connecticut, New Hampshire, New Jersey, Hawaii); Lower middle (25–50%) 0.43–0.70, 13 states (Arizona, Florida, Pennsylvania, Tennessee, New Mexico); Emerging (bottom 25%) 0.21–0.42, 13 states (South Carolina, Alabama, Wyoming, North Dakota, Iowa). Total 51 (50 states + DC).
46. **Figure 2.6 (p.20)** maps those state tiers; the caption's finding is "high per-capita usage in the West Coast, but also higher usage in Nevada, Utah, Colorado, Missouri, and Virginia".
47. **As per-capita adoption rises, usage shifts away from Computer and Mathematical tasks toward education, office and administrative uses, arts, and the life, physical and social sciences — "though the overall pattern is noisy"** (p.21 and Figure 2.7 caption, p.22).
48. **Figure 2.7 (p.22) — four cross-country regressions of SOC occupation group share on AUI**, each country weighted equally, ≥200 observations: Computer and Mathematical **β = −0.700 (p = 0.385), R² = 0.007**; Educational Instruction and Library **β = 0.082 (p = 0.858), R² = 0.000**; Arts, Design, Entertainment, Sports, and Media **β = 0.357 (p = 0.146), R² = 0.037**; Office and Administrative Support **β = 0.448 (p = 0.009), R² = 0.091**. Only the Office and Administrative Support slope reaches conventional significance; the Computer and Mathematical slope, which carries the narrative, does not.
49. **Figure 2.8 (p.23) — top overrepresented middle-level request clusters, by country** (ratio = country share ÷ global share; only requests with ≥1% frequency globally *and* in that country). **United States:** "Provide comprehensive cooking, nutrition, and meal planning assistance" 1.43x; "Help with job applications, resumes, and career documents" 1.41x; "Provide personal relationship advice and life guidance support" 1.34x; "Provide comprehensive travel planning and booking assistance" 1.30x; "Provide comprehensive medical and healthcare guidance across multiple specialties" 1.29x. **Brazil:** "Provide translation services and comprehensive language learning assistance across multiple languages" 6.4x; "Provide comprehensive legal assistance and document drafting across multiple practice areas" 5.0x; "Help create and optimize comprehensive digital marketing content and strategies" 1.15x; "Edit and improve existing written content and documents" 1.07x; "Assist with game development programming and general gaming support" 1.01x. **Vietnam:** "Help with cross-platform mobile app development, debugging, and feature implementation" 1.85x; "Debug and fix web application errors and technical issues" 1.73x; "Fix and improve web and mobile application UI layouts, styling, and components" 1.70x; "Create comprehensive K-12 educational materials and teaching resources" 1.59x; "Provide comprehensive multi-technology programming development assistance and technical guidance" 1.48x. **India:** "Fix and improve web and mobile application UI layouts, styling, and components" 2.4x; "Debug and fix web application errors and technical issues" 2.1x; "Help develop, debug, and modify web applications and frontend components" 2.1x; "Help with cross-platform mobile app development, debugging, and feature implementation" 2.1x; "Help build complete web applications and websites from scratch" 2.1x. Selection rule stated on p.23: these four are "the country with the highest total usage within a given Anthropic AI Usage Index tier".
50. **"This likely reflects local specialization: Brazil has been an early adopter of AI in the judicial system, and India has a large information technology sector."** (p.23). An interpretation, not a test.
51. **"Across all countries, software development emerges as the most common use of Claude."** (p.23). Comparison: request/task mix within every country in the sample.
52. **Cross-state AUI differences "account for less than half of the variation in income differences across US states"** (p.24) — note this restates claim 44 with the variables the other way round; see item I5 below.
53. **Figure 2.9 (p.25) — top overrepresented middle-level request clusters, by US state** (ratio = state share ÷ US share; ≥1% frequency in the US and in that state). **California:** "Help with basic numerical tasks and number-related requests" 3.7x; "Help solve math problems and perform calculations" 3.6x; "Provide translation services and comprehensive language learning assistance across multiple languages" 1.17x; "Help develop, debug, and implement machine learning and AI systems" 1.13x; "Help create and optimize comprehensive digital marketing content and strategies" 1.09x. **Texas:** "Help with job applications, resumes, and career documents" 1.32x; "Help optimize business workflows and project management systems" 1.30x; "Provide comprehensive legal assistance and document drafting across multiple practice areas" 1.25x; "Provide comprehensive job search and career advancement support" 1.24x; "Create comprehensive K-12 educational materials and teaching resources" 1.19x. **Florida:** "Provide sports training advice, fitness guidance, and sports-related tools and analysis" 1.35x; "Help create and optimize comprehensive digital marketing content and strategies" 1.33x; "Provide comprehensive business consulting and strategic development assistance" 1.31x; "Provide comprehensive legal assistance and document drafting across multiple practice areas" 1.25x; "Provide comprehensive medical and healthcare guidance across multiple specialties" 1.22x. **South Carolina:** "Provide comprehensive legal assistance and document drafting across multiple practice areas" 1.67x; "Provide sports training advice, fitness guidance, and sports-related tools and analysis" 1.55x; "Assist with game development programming and general gaming support" 1.51x; "Provide personal relationship advice and life guidance support" 1.50x; "Create comprehensive K-12 educational materials and teaching resources" 1.29x. Selection rule (p.24): the top state in each usage tier — California for leading, Texas for upper middle, Florida for lower middle, South Carolina for emerging.
54. **California's IT, digital marketing and translation overrepresentation "likely reflect[s] its tech sector and linguistically diverse population"; its overrepresented basic-numerical requests "may represent tests of model capabilities or abuse"; Florida's business-advice and fitness overrepresentation is "potentially tied to its role as a financial hub with relatively low tax rates and a warm climate amenable to outdoor activities"** (p.24). Interpretations offered without test.
55. **In DC, "help with job applications is 1.84x as common in DC as in the US overall"** (p.25).
56. **Figure 2.10 (p.26) — DC's top-5 overrepresented O*NET tasks:** "Edit or rewrite existing copy as necessary, and submit copy for approval by supervisor" 2.69x; "Instruct individuals in career development techniques such as job search and application strategies, resume writing, and interview skills" 2.07x; "Provide information and advice to the public regarding the selection, purchase, and care of products" 1.55x; "Provide private instruction to individual or small groups of students to improve academic performance, improve occupational skills, or prepare for academic or occupational tests" 1.36x; "Perform routine system administrative functions such as troubleshooting, back-ups, and upgrades" 1.22x. **DC's top-5 overrepresented request clusters:** "Provide comprehensive job search and career advancement support" 1.87x; "Help with job applications, resumes, and career documents" 1.84x; "Draft professional business communications and formal documents" 1.82x; "Provide personal relationship advice and life guidance support" 1.72x; "Provide comprehensive business consulting and strategic development assistance" 1.51x.
57. **Controlling for task mix, "As Claude usage per capita increases, countries shift from automation-focused to augmentation-focused usage"** (p.26). **Figure 2.11 (p.27) reports the partial regression: β = −3.112, R² = 0.394 (p < 0.001)**, of automation-% residuals on AUI residuals, countries with ≥200 observations. Comparison: the residual of each country's actual automation share after removing the automation share its own task mix predicts, against the residual of its AUI after the same removal. The most positive automation residuals are Mozambique, Brazil and Pakistan; the most negative sit at high AUI (Cyprus, Lithuania, Montenegro, Finland, Norway, Denmark); Israel, at the far right of the AUI axis, sits near zero.
58. **Utah caveat (endnote 7, p.29): "a notable fraction of its usage appeared to be possibly associated with coordinated abuse … also reflected in a much higher 'directive' automation score than average", but "we ran robustness checks and believe that this activity is not driving the results."** No robustness numbers are reported.

### Chapter 3 — First-party API enterprise deployment (pp.30–45)

59. **Census Business Trends and Outlook Survey: AI adoption among US firms "more than doubled in the past two years, rising from 3.7% in fall 2023 to 9.7% in early August 2025"** (p.31, Figure 3.1). External data, not Anthropic's. Adoption question quoted in the Figure 3.1 caption and endnote 4 (p.44).
60. **"in early August 2025, one in four businesses in the Information sector reported using AI, which is roughly ten times the rate for Accommodation and Food Services"** (p.31). Comparison: BTOS by sector.
61. **"the vast majority of firms in the US do not report using AI in their production processes"** (p.31); endnote 3 (p.44) restates this as "nine out of ten businesses in the US report not using AI" and flags it as a different measure of adoption from the 40% employee figure in the introduction.
62. **The API sample is "1 million transcripts from August 2025, sampled randomly from a pool of 1P API customers constituting roughly half of our 1P API usage"** (endnote 2, p.44). "Each record is a prompt-response pair from our sample period which in some instances is mid-session for multi-turn interactions."
63. **"Among the top 15 use clusters—representing about half of all API traffic—the majority relate to coding and development tasks"** (p.32).
64. **"Debugging web applications and resolving technical issues each account for roughly 6% of usage"** (p.32); Figure 3.2 (p.33) gives "Resolve software development technical issues and workflow problems" 6.1% and "Debug and develop web application frontend code and components" 6.0%.
65. **"around 5% of API traffic focuses specifically on developing and evaluating AI systems themselves"** (p.32); Figure 3.2 gives "Develop, configure and evaluate AI systems across domains" 5.2%.
66. **API customers "also deploy Claude to create marketing materials (4.7%) and to process business & recruitment data (1.9%)"** (p.33).
67. **Figure 3.2 (p.33) — top 15 broad bottom-up 1P API use clusters, by share of total request count:** Resolve software development technical issues and workflow problems 6.1%; Debug and develop web application frontend code and components 6.0%; Develop and manage professional business software and service systems 5.2%; Develop, configure and evaluate AI systems across domains 5.2%; Software development troubleshooting and optimization assistance 4.9%; Create professional marketing, business, and journalistic content 4.7%; Develop and troubleshoot data extraction and analytics systems 4.4%; Develop data extraction and conversion tools for multiple sources 2.9%; Develop and debug automated software testing infrastructure 2.5%; Web security assessment and digital communications protection 2.3%; Develop financial software and trading analysis tools 2.3%; Develop and troubleshoot software authentication and access control systems 1.9%; Process and evaluate professional business and recruitment data 1.9%; Design and develop web interface UI/UX elements 1.8%; Implement and troubleshoot software database and search functionality 1.8%. (These sum to 53.1%, consistent with "about half".)
68. **"Little less than half of all API traffic maps to computer and mathematical tasks—more than 8 percentage points higher than Claude.ai usage. Office and administrative tasks come second at roughly 10% of transcripts"** (p.33).
69. **"education and library tasks drop from 12.3% to 3.6%, while arts and entertainment fall from 8.2% to 5.2%"** (p.33). Comparison: Claude.ai share → 1P API share. Note the Claude.ai education figure here (12.3%) differs again from the 12.4% in the summary bullet and the 12.7% in Figure 1.1.
70. **Figure 3.3 (p.34) — usage shares across top occupational categories, Claude.ai vs 1P API** (rounded to whole percent on the chart): Computer and Mathematical 36% / 44%; Office and Administrative Support 8% / 10%; Educational Instruction and Library 12% / 4%; Life, Physical & Social Science 7% / 7%; Arts, Design, Entertainment, Sports & Media 8% / 5%; Business and Financial Operations 3% / 3%; Sales and Related 2% / 4%; Management 3% / 3%. Caption: "44% of API traffic in our sample was matched to a task characteristic of a Computer and Mathematical occupation."
71. **"In many cases however, occupational categories are reasonably close between Claude.ai and API data, suggesting that underlying model capabilities, rather than the specific product surface, drives adoption in many instances."** (p.34).
72. **"Among Claude.ai conversations, the bottom 80% of task categories account for only 12.7% of usage; for API customers it's somewhat more concentrated at 10.5%"** (p.34, Figure 3.4).
73. **The text reports "Gini coefficients of 0.84 and 0.86" (p.34); Figure 3.4's own legend (p.35) reports 1P API Gini = 0.842 and Claude.ai Gini = 0.822.** The two are inconsistent — see item I2.
74. **Figure 3.4 right panel (p.35) — task rank against usage share, tasks representing ≥0.1% of overall usage: 1P API y = −1.11x + 2.51; Claude.ai y = −1.13x + 2.53; Zipf's Law reference line y = −1.00x + 2.52.** Comparison: both empirical slopes against the Zipf benchmark of −1.
75. **"Both converge on comparable concentration levels, suggesting a common matching process between AI capabilities and associated economic tasks."** (p.35).
76. **"In our data, 77% of API transcripts show automation patterns (especially full task delegation) versus just 12% for augmentation … Based on a sample of conversations from Claude.ai, the split between automation and augmentation is nearly even."** (p.36). Note 77% + 12% = 89%; the residual 11% is not accounted for in the text (it corresponds to the `not_classified` and `none` categories of the collaboration facet — see Definitions).
77. **"97% of tasks show automation-dominant patterns in API usage, compared to only 47% on Claude.ai"** (p.36); Figure 3.5 (p.37) gives **1P API: automation dominant 97.9% of tasks, augmentation dominant 2.1%; Claude.ai: automation dominant 47.0%, augmentation dominant 53.0%.** Comparison: per-O*NET-task dominance, the two surfaces side by side.
78. **"tasks at the 90th percentile of output length are more than 4x longer than tasks at the 10th percentile"** (p.38).
79. **Table 3.1 (p.38) — example O*NET tasks by output token index percentile, with Claude's own summaries.** *10th percentile (value ≈ 0.40):* "Answer questions regarding store merchandise", "Maintain website links and functionality", "Respond to customer complaints about services", "Configure email and virus protection software" — Claude's summary: "Simple operational tasks requiring brief, straightforward responses. Focus on routine customer service, basic maintenance, and standard procedures with minimal complexity." *50th percentile (value ≈ 0.82):* "Analyze data to determine scientific signifcance and environmental correlations" [sic, as printed], "Examine objects for exhibit planning and display arrangements", "Observe and evaluate student work for progress assessment", "Manage projects and contribute to collaborative work" — "Moderate complexity tasks involving analysis, evaluation, and coordination. Balance between routine work and strategic thinking, requiring structured but detailed responses." *90th percentile (value ≈ 1.75):* "Develop new biological research methods", "Create experimental designs and analytical methods", "Revise business plans for online business", "Study technical blueprints and specifications" — "Complex analytical and development tasks requiring detailed, comprehensive responses. Focus on research, strategic planning, technical design, and creative problem-solving." The 1.75/0.40 ratio is the "more than 4x" of claim 78.
80. **Figure 3.6 (p.39) — average output token index by leading occupational category:** Educational Instruction and Library 1.25; Computer and Mathematical 1.20; Life, Physical & Social Science 1.09; Arts, Design, Entertainment, Sports & Media 1.03; All Other 0.93; Office and Administrative Support 0.83. Comparison: category means against the all-task average of 1.0.
81. **"Across economic tasks, each 1% increase in input length is associated with a less-than-proportional 0.38% increase in output length … This elasticity of 0.38 suggests that there are strong diminishing marginal returns in translating longer contextual inputs into longer outputs"** (p.40). Figure 3.7 (p.40) reports **Best fit R² = 0.294, β = 0.382**, on ln(output token index) against ln(input token index).
82. **Figure 3.7 (p.40) task counts by category:** Office and Administrative Support N = 225; All Other N = 1,083; Arts, Design, Entertainment, Sports & Media N = 113; Life, Physical & Social Science N = 188; Computer and Mathematical N = 298; Educational Instruction and Library N = 147. Total 2,054 O*NET tasks matched to 1P API traffic — the effective universe for every Chapter 3 task-level regression.
83. **"tasks typical of computer and mathematical occupations cost more than 50% more than sales-related tasks, yet dominate usage"** (p.41).
84. **"Overall, we find a positive correlation between cost and usage: higher-cost tasks tend to have higher usage rates"** (p.41). Figure 3.8 (p.42) reports **Best fit R² = 0.228, β = 2.962**, ln(usage share %) on ln(average API cost index across tasks), one point per occupational category (22 categories plotted). Caption: "The estimated elasticity of 3 implies that each 1% increase in the average cost of a task is associated with a 3% increase in prevalence in our sample."
85. **"The positive correlation between cost and usage suggests that cost plays an immaterial role in shaping patterns of enterprise AI deployment."** (p.41). An interpretive step, not a separate estimate — and in tension with claim 86 and with the "weak price sensitivity" of the summary bullet (claim 11). See item I3.
86. **"Controlling for task characteristics, we find that each 1% cost increase is associated with a 0.29% reduction in usage frequency in our sample of API transcripts … According to this estimate, a 10% cost reduction for a particular task would only increase usage by around 3%."** (p.42). Figure 3.9 (p.43) reports **Partial relationship R² = 0.025** and an elasticity of **−0.29**. Sample restricted to tasks appearing in both the 1P API and Claude.ai samples. Controls (Figure 3.9 caption and endnote 13, p.45): fixed effects for occupational category, collaboration mode share from Claude.ai, and indicators for whether a given collaboration mode was censored for privacy in the Claude.ai sample. No standard error or p-value is reported for the −0.29.
87. **"Our API data captures enterprise AI adoption in its early stages: highly concentrated, automation-focused, and surprisingly price-insensitive (at least among the tasks our API customers use Claude for)."** (p.43).

### Concluding remarks (pp.46–47)

88. **"early AI adoption is strikingly uneven. Usage currently clusters in a small set of tasks, with strong geographic variation that is highly correlated with income—particularly across countries."** (p.46). The "particularly across countries" qualifier is the report's own acknowledgement that the state-level relationship is weaker (claim 44).
89. **"Early business adoption of Claude is at once both similar to consumer use (coding is the most common use for both), and different in several consequential ways."** (p.46).
90. **"We are now open-sourcing comprehensive API usage data alongside our existing Claude.ai consumer data (now including geographic breakdowns at state and country levels), all intersected with detailed task-level classifications."** (pp.46–47).

---

## Definitions (verbatim)

Every definition of a construct or measure, quoted exactly. Sources are marked `[PDF p.N]` for the report of record, `[web]` for the primary web page where it differs, and `[data_documentation.md]` for the release's own data documentation at `release_2025_09_15/data_documentation.md` (fetched 2026-09-16), which is the only place several released constructs are defined.

### The collaboration facet and its five patterns

> "At a high level, we distinguish between automation and augmentation modes of using Claude:
>
> Automation encompasses interaction patterns focused on task completion:
> - Directive: Users give Claude a task and it completes it with minimal back-and-forth
> - Feedback Loops: Users automate tasks and provide feedback to Claude as needed
>
> Augmentation focuses on collaborative interaction patterns:
> - Learning: Users ask Claude for information or explanations about various topics
> - Task Iteration: Users iterate on tasks collaboratively with Claude
> - Validation: Users ask Claude for feedback on their work"
>
> — [PDF p.9]

> "Here, we use the same augmentation and automation collaboration patterns as defined in Chapter 1." — [PDF p.26]

> "Automation and augmentation modes are defined in Chapter 1." — [PDF p.37, Figure 3.5 caption]

> "'Directive' conversations, where users delegate complete tasks to Claude" — [PDF p.3]

> "**automation_pct**: Percentage of classifiable collaboration that is automation-focused (directive, feedback loop patterns)" — [data_documentation.md, Collaboration Pattern Metrics]

> "**augmentation_pct**: Percentage of classifiable collaboration that is augmentation-focused (validation, task iteration, learning patterns)" — [data_documentation.md, Collaboration Pattern Metrics]

> "**collaboration_pct**: Percentage of geographic total with this pattern" — [data_documentation.md]

> "**collaboration_pct_index**: Specialization index comparing pattern to baseline" — [data_documentation.md]

### Automation and augmentation *dominance* (a task-level construct, distinct from the shares)

> "Automation dominance is defined as a task having a greater observed share of automation usage. Likewise for augmentation dominance." — [PDF p.37, Figure 3.5 caption]

> "When for privacy-preserving reasons we do not observe usage shares for a particular collaboration mode we give that category a value of 0% in this figure." — [PDF p.37, Figure 3.5 caption]

### The Anthropic AI Usage Index (AUI)

> "To account for differences in population size, we analyze usage adjusted for the working-age population, introducing a new measure called the Anthropic AI Usage Index (AUI): For each geography, we calculate its share of Claude usage, and its share of the working-age population (ages 15-64). We then calculate the AUI by dividing these shares:" — [PDF p.14] (the formula itself is set as an image; the axis label of Figures 2.2, 2.5 and 2.7 renders it as "Anthropic AI Usage Index (usage % / working-age population %)")

> "This index reveals whether countries use Claude more or less than expected relative to their working-age population. A region with an AUI > 1 has higher usage than expected after adjusting for population, while a region with an AUI < 1 has lower usage." — [PDF p.14]

> "we introduce the Anthropic AI Usage Index (AUI) to measure whether Claude.ai use is over- or underrepresented in an economy relative to its working age population." — [PDF p.3]

> "**usage_per_capita_index**: Concentration index showing if a geography has more/less usage than expected based on population share (1.0 = proportional, >1.0 = over-representation, <1.0 = under-representation)" — [data_documentation.md]

> "**working_age_pop**: Population aged 15-64 (working age definition used by World Bank)" — [data_documentation.md]

> "**gdp_per_working_age_capita**: Total GDP divided by working age population (in USD)" — [data_documentation.md]

### Per-capita usage and usage shares

> "**usage_count**: Total number of conversations/interactions in a geography" — [data_documentation.md]

> "**usage_pct**: Percentage of total usage (relative to parent geography - gobal for countries, US for states)" — [data_documentation.md, as printed, including the typo "gobal"]

> "**usage_per_capita**: Usage count divided by working age population" — [data_documentation.md]

### AUI tiers

> "Next, we create per capita usage tiers based on the AUI. We look at countries with at least 200 conversations in our random sample of 1 million conversations, and set thresholds for different usage tiers-based quartiles, i.e. Leading (top 25%), Upper Middle (50-75%), Lower Middle (25%-75%) and Emerging (bottom 25%). We then assign countries, even if they have fewer than 200 observations, to a tier based on their AUI. We assign countries for which we have population data, but no usage in our sample, to a Minimal tier." — [PDF p.15] (as printed: "Lower Middle (25%-75%)" — Table 2.1 and Figure 2.3 label the same tier "Lower middle (25-50%)")

> "Tier thresholds (quartiles) are based on countries with at least 200 observations for the global level, and on US states with at least 100 observations for the US level. Countries with no observed usage are assigned to the Minimal tier since we do not know if they have exactly zero usage or little usage that our random sample did not capture." — [PDF p.28, Chapter 2 endnote 4]

> "The different tiers reflect a country's position within the global distribution of the Anthropic AI Usage Index as defined in this chapter." — [PDF p.15, Figure 2.3 caption]

> "The different tiers reflect a US state's position within the US distribution of the Anthropic AI Usage Index as defined in this chapter." — [PDF p.20, Figure 2.6 caption]

> "**usage_tier**: Usage adoption tier (0 = no/little adoption, 1-4 = quartiles of adoption among geographies with sufficient usage)" — [data_documentation.md]

### The O*NET task taxonomy and SOC groups

> "First, we classify conversations into tasks according to O*NET, a US taxonomy that maps specific tasks to occupations and occupation groups (e.g., a task involving software debugging would fall into the Computer and Mathematical occupation group)." — [PDF p.20]

> "SOC share is based on how many O*NET tasks in a given geography fall into a given SOC group." — [PDF p.22, Figure 2.7 caption]

> "**soc_pct**: Percentage of classified O*NET tasks associated with this SOC major occupation group (e.g., Management, Computer and Mathematical)" — [data_documentation.md]

> "**onet_task_pct**: Percentage of geographic total using this task" — [data_documentation.md]

> "**onet_task_pct_index**: Specialization index comparing task usage to baseline (global for countries, US for states)" — [data_documentation.md]

> "**onet_task_collaboration_pct**: Percentage of the base task's total that has this collaboration pattern (sums to 100% within each task)" — [data_documentation.md]

### Request clusters and the request hierarchy

> "Second, we use Claude to construct a bottom-up taxonomy of user requests on Claude.ai, which provides insight into usage patterns that do not fit neatly into existing taxonomies. For example, the request cluster 'help write and improve cover letters for job applications' (lowest level) feeds into the higher-level cluster 'help with job applications, resumes, and career documents' (middle level), which in turn feeds into the cluster 'help with job applications, resumes, and career advancement' (highest level). These two complementary approaches allow us to both report results aligned with standard labor statistics, and provide flexibility to capture tasks that standard taxonomies miss." — [PDF pp.20–21]

> "For this figure, we focus on request clusters at the middle level of granularity, i.e. more aggregated than the lowest level request clusters, but less aggregated than the highest level request clusters." — [PDF p.23, Figure 2.8 caption; repeated p.25, Figure 2.9 caption]

> "**request**: Request complexity levels (0=highest granularity, 1=middle granularity, 2=lowest granularity)" — [data_documentation.md, Claude.ai Facets]

> "**request**: Request categories (hierarchical levels 0-2 from bottom-up taxonomy)" — [data_documentation.md, 1P API Facets]

> "**request_pct_index**: Specialization index comparing request usage to baseline" — [data_documentation.md]

> "Contains the hierarchy of request clusters for Claude.ai usage with their names and descriptions." — [data_documentation.md, on `request_hierarchy_tree_claude_ai.json`]

Note on naming: Figure 2.9's chart title says "high-level requests" while its caption says "middle level of granularity". The caption governs.

### Overrepresentation (the "local specialisation" measure)

> "A request is overrepresented in a country when the share of conversations containing that request is higher for that country than globally." — [PDF p.23, Figure 2.8 caption]

> "A request is overrepresented in a state when the share of conversations containing that request is higher for that state than in the US as a whole." — [PDF p.25, Figure 2.9 caption]

> "A task or request is overrepresented in a state when the share of conversations containing that task or request is higher for that state than in the US as a whole." — [PDF p.26, Figure 2.10 caption]

> "Only includes requests with at least 1% frequency globally and for that country." — [PDF p.23, Figure 2.8 caption]

> "Requests were filtered to those that represent at least 1% of requests at the global level and 1% of the local level." — [PDF p.29, Chapter 2 endnote 8]

### The task-mix adjustment (Figure 2.11)

> "To isolate the relationship between automation preference and Claude usage accounting for task composition differences, we do the following: First, we calculate each country's expected automation percentage by taking a weighted average. For each O*NET task (e.g., coding, writing, or analysis), we multiply that task's share of the country's usage by the global automation rate for that task type (the percentage of that task that Claude completes via directive/feedback loop patterns globally). Summing these gives us the expected values for each country's automation percentage given the country's specific task mix. We then regress both the actual automation % and AUI on this expected automation %. The residuals from these regressions represent the variation in each variable that cannot be explained by task composition. By examining the relationship between these residuals (known as partial regression analysis), we can determine whether countries that have higher AI usage than their task mix would predict tend also to have higher-than-predicted automation." — [PDF p.29, Chapter 2 endnote 9]

> "We plot the relationship after accounting for a geography's task mix, thus we show the regression residuals." — [PDF p.27, Figure 2.11 caption]

### Privacy thresholds

> "For privacy reasons, our automated analysis system filters out any cells—e.g., countries, and (country, task) intersections—with fewer than 15 conversations and 5 unique user accounts. For bottom-up request clusters, we have an even higher privacy filter of at least 500 conversations and 250 unique accounts." — [PDF p.28, Chapter 2 endnote 1]

### The 200 and 100 observation thresholds

> "We only include countries with at least 200 observations in our sample for this figure because of the uncertainty of the measure for low-usage countries in our random sample." — [PDF p.14, Figure 2.2 caption; repeated verbatim in the captions of Figure 2.4 (p.17), Figure 2.7 (p.22) and Figure 2.11 (p.27)]

> "We only include states with at least 100 observations in our sample for this figure because of the uncertainty of the measure for low-usage states in our random sample." — [PDF p.19, Figure 2.5 caption]

> "**Minimum Observations**: 200 conversations per country, 100 per US state (applied in enrichment step, not raw preprocessing)" — [data_documentation.md, Data Processing Notes]

### not_classified and none

> "**not_classified**: Indicates data that was filtered for privacy protection or could not be classified" — [data_documentation.md, Special Values]

> "**none**: Indicates the absence of the attribute (e.g., no collaboration, no task selected)" — [data_documentation.md, Special Values]

> "**not_classified**:
>   - For regular facets: Captures filtered/unclassified conversations
>   - For intersection facets: Each base cluster has its own not_classified (e.g., 'task1::not_classified')" — [data_documentation.md, Data Processing Notes]

> "**Percentage Index Calculations**:
>   - Exclude `not_classified` and `none` categories from index calculations as they are not meaningful" — [data_documentation.md, Data Processing Notes]

> "**Intersection Percentages**: Calculated relative to base cluster totals, ensuring each base cluster's percentages sum to 100%" — [data_documentation.md, Data Processing Notes]

### The API token and cost measures

> "For each O*NET task in our sample, we calculate the average input and output length of associated API transcripts. We then divide these values by the average lengths across all tasks appearing in our sample. This produces an input token index and an output token index for each task. An index value of 1.5, for example, means that the API transcripts associated with that task are 50% longer than the average across tasks." — [PDF p.38]

> "API input length refers to the text in API messages, system prompts, and any additional content sent to the model, including files and datasets relevant to the task at hand. Output length refers to Claude's generated response to an API call." — [PDF p.45, Chapter 3 endnote 8]

> "For each O*NET task matched to 1P API traffic we calculate an output token index: Dividing the average output length across transcripts associated with that task by the average (unweighted) value across all tasks in our sample." — [PDF p.39, Figure 3.6 caption; also pp.38–39, Table 3.1 caption]

> "The input token index is constructed similarly." — [PDF p.40, Figure 3.7 caption]

> "For each O*NET task matched to 1P API traffic we calculate an API cost index: Dividing the average API cost across transcripts associated with that task by the average (unweighted) value across all tasks in our sample." — [PDF p.42, Figure 3.8 caption; repeated p.43, Figure 3.9 caption]

> "To see that this is the case, we first aggregate O*NET tasks that we identify in our API sample by broad occupational category to measure overall usage shares and the average cost per task in each category. As with the input and output tokens reported by O*NET task, we normalize average cost per task by the average value across tasks observed in our sample." — [PDF p.45, Chapter 3 endnote 12]

> "**prompt_tokens_index**: Re-indexed mean prompt tokens (1.0 = average across all tasks)" — [data_documentation.md]

> "**completion_tokens_index**: Re-indexed mean completion tokens (1.0 = average across all tasks)" — [data_documentation.md]

> "**cost_index**: Re-indexed mean cost (1.0 = average across all tasks)" — [data_documentation.md]

> "**onet_task::prompt_tokens**: Mean prompt tokens per task (normalized, average = 1.0)" / "**onet_task::completion_tokens**: Mean completion tokens per task (normalized, average = 1.0)" / "**onet_task::cost**: Mean cost per task (normalized, average = 1.0)" — [data_documentation.md, 1P API Facets]

### Enterprise / 1P API versus consumer / Claude.ai

> "Our API allows customers to integrate Claude directly into their own products and applications, and charges by the token used, rather than a flat subscription fee. This represents a fundamentally different product experience to Claude.ai, which we focused on in the previous two chapters." — [PDF p.30]

> "Importantly, API users access Claude programmatically, rather than through a web user interface (as with Claude.ai)." — [PDF p.4]

> "**platform_and_product** | string | 'Claude AI (Free and Pro)'" — [data_documentation.md, Claude.ai Data Schema]

> "**platform_and_product** | string | '1P API'" — [data_documentation.md, 1P API Data Schema]

> "Each record is a prompt-response pair from our sample period which in some instances is mid-session for multi-turn interactions." — [PDF p.44, Chapter 3 endnote 2]

> "The unit of observation is a conversation with Claude on Claude.ai, not a user, so it is possible that multiple conversations from the same user are included" — [PDF p.28, Chapter 2 endnote 2]

### The Gini coefficient

> "The Gini coefficient is a measure used to quantify inequality within a distribution, such as the distribution of task usage. It ranges from 0 to 1, where 0 represents perfect equality (every task has exactly the same usage share) and 1 represents perfect inequality (where one task accounts for all usage, and every other task has none)." — [PDF p.44, Chapter 3 endnote 5]

> "Zipf's law, in which the coefficient of the best-fit-line is equal to -1, occurs with some regularity in various economic settings." — [PDF p.35, Figure 3.4 caption]

### Firm-level AI adoption (the external benchmark)

> "AI adoption rates are calculated as the share of firms responding 'yes' to the question 'In the last two weeks, did this business use Artificial Intelligence (AI) in producing goods or services? (Examples of AI: machine learning, natural language processing, virtual agents, voice recognition, etc.)'." — [PDF p.32, Figure 3.1 caption]

> "The Business Trends and Outlook Survey (BTOS), published by the Census Bureau, is a reputable barometer of AI adoption by firms in the US." — [PDF p.44, Chapter 3 endnote 4]

### Geolocation

> "Aggregate geographic statistics at the country and US state level were assessed and tabulated from the IP address of each conversation. For geolocation, we use ISO-3166 codes since our provider for IP geolocation uses this standard. International locations use ISO-3166-1 country codes, US state level data use ISO-3166-2 region codes, which include all 50 US states and Washington DC." — [PDF p.28, Chapter 2 endnote 2]

> "International locations use ISO-3166-1 country codes, which includes countries and some territories." — [PDF p.28, Chapter 2 endnote 3]

> "**geo_id** | string | Geographic identifier (ISO-2 country code for countries, US state code, or 'GLOBAL', ISO-3 country codes in enriched data)" — [data_documentation.md]

> "**geography** | string | Geographic level: 'country', 'state_us', or 'global'" — [data_documentation.md]

---

## Data and methods

*(in the wiki author's words, with page references)*

**Two samples, one window.** Chapter 1 and Chapter 2 rest on 1 million Claude.ai Free and Pro conversations from 4–11 August 2025, drawn at random from all conversations in that period that were not flagged as potential trust-and-safety violations (p.28, Ch.2 endnote 2). Chapter 3 rests on 1 million 1P API transcripts described in the report only as "from August 2025", sampled at random from a pool of 1P API customers accounting for roughly half of Anthropic's 1P API usage (p.44, Ch.3 endnote 2). The released API file is named `aei_raw_1p_api_2025-08-04_to_2025-08-11.csv`, so the API window appears to be the same 4–11 August week as the Claude.ai sample, which is what makes the "concurrently sampled Claude.ai conversations" used as controls in Figure 3.9 (p.45, Ch.3 endnote 13) coherent; the report itself never states the API window to the day.

**Units.** For Claude.ai the unit is a conversation, not a user; multiple conversations from one user can enter the sample, which the report defends by reference to earlier work finding random vs user-stratified sampling substantively similar (p.28, endnote 2, citing the Clio paper). For the API the unit is a prompt-response pair, which "in some instances is mid-session for multi-turn interactions" (p.44, endnote 2). The two units are therefore not commensurate, and the Claude.ai–API comparisons in Chapter 3 compare conversations with prompt-response pairs.

**Geolocation.** Country and US-state assignment comes from the IP address of each conversation, via a third-party geolocation provider using ISO-3166-1 (countries, "and some territories") and ISO-3166-2 (50 states + DC). Conversations originating from VPN, anycast or hosting services are excluded, as determined by the provider (p.28, endnote 2). Geography exists for Claude.ai only; the API data carries `geo_id = "GLOBAL"` throughout (p.5; `data_documentation.md`).

**Classifiers and taxonomies.** Two parallel classifications, as in the earlier reports: (i) top-down mapping of each conversation to an O*NET task statement, aggregated to SOC major groups; (ii) a bottom-up, Claude-constructed three-level hierarchy of user requests (pp.20–21). The release documents O*NET Database 20.1 and the 2019 SOC structure as the external taxonomies, downloaded 2 September 2025. The V3 collaboration classifier is Claude Sonnet 4; V2 used Sonnet 3.7 (p.11, Ch.1 endnote 4). Chapter 3 states that "we apply the same privacy-preserving classification methods from previous chapters" to anonymised API transcripts (p.32). Table 3.1's summaries were themselves generated by Claude Sonnet 4 from a deliberately minimal prompt (pp.38–39; p.45, endnote 9).

**Privacy filtering.** Cells with fewer than 15 conversations *and* 5 unique accounts are dropped; bottom-up request clusters require at least 500 conversations and 250 unique accounts (p.28, endnote 1). Where a collaboration mode is censored for a task, Figure 3.5 assigns it 0% (p.37) — a convention that mechanically pushes censored tasks toward whichever mode survives. Figure 3.9's controls include indicators for exactly this censoring (p.43; p.45, endnote 13). In the released data these cells surface as `not_classified`, which is excluded from all index calculations (`data_documentation.md`).

**Reporting thresholds.** Country figures are restricted to ≥200 observations, state figures to ≥100 (Figure captions 2.2, 2.4, 2.5, 2.7, 2.11; `data_documentation.md` confirms these are applied at the enrichment step, not in raw preprocessing). Tier cut-points are the quartiles of that restricted set, but tier *assignment* extends to all countries, including those below the threshold and those with zero observed usage (p.15; p.28, endnote 4).

**Population and income data.** Working-age population is ages 15–64: World Bank / UN series SP.POP.1564.TO for countries (2024, downloaded 2 September 2025), with Taiwan added from the Taiwanese National Development Council because the World Bank series excludes it; US Census SC-EST2024-AGESEX-CIV civilian population by single year of age for states. GDP is IMF World Economic Outlook NGDPD (current prices, USD, 2024) for countries and BEA SASUMMARY state GDP (2024) for states. All from `data_documentation.md`.

**Regressions run.** Six in total, all cross-sectional and all reported as a coefficient with an R² and sometimes a p-value, never with a standard error or a sample size in the text:
1. ln(AUI) on ln(GDP per working-age capita), countries ≥200 obs: β = 0.690, p < 0.001, R² = 0.709 (Figure 2.4, p.17).
2. The same at US-state level: elasticity 1.8, "less than half the variation" explained; no figure, no R², no p-value (p.19).
3. SOC group share on AUI, four separate panels, countries weighted equally (Figure 2.7, p.22): β = −0.700 (p = 0.385), 0.082 (p = 0.858), 0.357 (p = 0.146), 0.448 (p = 0.009).
4. Partial regression of automation-% residuals on AUI residuals, both residualised on task-mix-expected automation % (Figure 2.11, p.27): β = −3.112, R² = 0.394, p < 0.001. Method in endnote 9, p.29.
5. ln(output token index) on ln(input token index) across O*NET tasks (Figure 3.7, p.40): β = 0.382, R² = 0.294; 2,054 tasks across the six category buckets.
6. ln(usage share) on ln(average API cost index): across 22 occupational categories, β = 2.962, R² = 0.228 (Figure 3.8, p.42); and, restricted to tasks present in both samples and with occupational fixed effects, Claude.ai collaboration-mode shares and censoring indicators, elasticity −0.29, partial R² = 0.025 (Figure 3.9, p.43; endnote 13, p.45).

**Robustness checks actually reported.** Two. (i) The V3 collaboration classification rerun with Sonnet 3.7, giving 45% automation against 49% with Sonnet 4, and a check that the directive shift appears across occupational categories rather than arising from task-mix change (p.11, endnote 4). (ii) An unspecified set of checks on Utah's possibly-coordinated-abuse traffic, whose conclusion but not whose numbers are reported (p.29, endnote 7).

**Released data and code.** `release_2025_09_15` on Hugging Face (`Anthropic/EconomicIndex`), 38 files. The Claude.ai data ships in a long, one-row-per-metric format keyed on `geo_id` × `geography` × `facet` × `level` × `variable` × `cluster_name`, with facets `country`, `state_us`, `onet_task`, `collaboration`, `request`, `onet_task::collaboration` and `request::collaboration`; the API data uses the same shape at `geo_id = "GLOBAL"` and adds the three mean-value intersection facets `onet_task::prompt_tokens`, `onet_task::completion_tokens` and `onet_task::cost`. Raw counts and percentages sit in `data/intermediate/`; derived measures (indices, tiers, per-capita, automation/augmentation percentages) are produced by the enrichment notebook and sit in `data/output/`. The release is the only one in the dataset to ship a code library: four preprocessing scripts (`preprocess_iso_codes.py`, `preprocess_population.py`, `preprocess_gdp.py`, `preprocess_onet.py`), a change-over-time script (`aei_report_v3_change_over_time_claude_ai.py`), two analysis function modules (`aei_analysis_functions_claude_ai.py`, `aei_analysis_functions_1p_api.py`) and four notebooks. Two request-hierarchy JSON trees (one per surface) give cluster names and descriptions. V1 and V2 comparison data arrive as four CSVs carried forward from `release_2025_03_27`. Two documentation/tree mismatches are worth knowing before attempting replication: the replication `README.md` names a preprocessing notebook `aei_report_v3_preprocessing_1p_api.ipynb` that does not exist in the tree (the tree has `aei_report_v3_preprocessing_claude_ai.ipynb`), and `data_documentation.md` names the Taiwan population file `Population by single age _20250802235608.csv` while the tree carries `Population by single age _20250903072924.csv`. Definitive file-level facts belong to `data/releases/release_2025_09_15.md` (data steward).

**What the report says it hopes the data will be used for.** Four questions, stated on pp.5–6 and quoted in full in the next section.

---

## Limitations (verbatim)

The report has no "Limitations" section. Every limitation it states is quoted below, in document order.

**On the sample and its unit**

> "The unit of observation is a conversation with Claude on Claude.ai, not a user, so it is possible that multiple conversations from the same user are included, though our past work suggests that sampling conversations at random versus stratified by user does not yield substantively different results." — [p.28, Ch.2 endnote 2]

> "We exclude conversations originating from VPN, anycast, or hosting services, as determined by our IP geolocation provider." — [p.28, Ch.2 endnote 2]

> "Data in this section covers 1 million transcripts from August 2025, sampled randomly from a pool of 1P API customers constituting roughly half of our 1P API usage." — [p.44, Ch.3 endnote 2]

> "Each record is a prompt-response pair from our sample period which in some instances is mid-session for multi-turn interactions." — [p.44, Ch.3 endnote 2]

> "At present, geographic usage patterns are only available for Claude.ai traffic." — [p.5]

**On the classifier and the over-time comparison**

> "We note that V3 uses Claude Sonnet 4 for classification, while V2 used Sonnet 3.7, which complicates direct comparison. To address this, we reran V3 data with Sonnet 3.7 and still found directive interactions rising significantly (though to a lower absolute level of 45% automation versus 49% with Sonnet 4)." — [p.11, Ch.1 endnote 4]

> "This could also be due to changes in the underlying user base." — [p.11]

> "Most strikingly, the data point toward increased delegation of tasks to AI systems–perhaps due to some combination of user trust in the technology as well as improvement of underlying model capabilities." — [p.11]

**On small cells, noise and the geographic measures**

> "We only include countries with at least 200 observations in our sample for this figure because of the uncertainty of the measure for low-usage countries in our random sample." — [p.14, Figure 2.2 caption; identical text in Figures 2.4, 2.7, 2.11]

> "We only include states with at least 100 observations in our sample for this figure because of the uncertainty of the measure for low-usage states in our random sample." — [p.19, Figure 2.5 caption]

> "While the overall pattern is noisy–especially for countries with fewer observations–Figure 2.7 suggests that as we progress from lower to higher per capita Claude adoption, usage shifts away from tasks in the Computer and Mathematical occupation group (e.g., programming) to more diverse tasks in areas such as education, office and administrative uses, and arts." — [p.21]

> "As we move from lower to higher adoption countries, Claude usage appears to shift away from programming-dominant tasks to a more diverse mix of tasks, though the overall pattern is noisy" — [p.22, Figure 2.7 caption]

> "The regression weights every country equally." — [p.22, Figure 2.7 caption]

> "Countries with no observed usage are assigned to the Minimal tier since we do not know if they have exactly zero usage or little usage that our random sample did not capture." — [p.28, Ch.2 endnote 4]

> "However, this concentration is affected by the population size of each country – larger countries may have larger usage shares purely because of their population size." — [p.13]

> "Though not adjusted for population, we suspect that these strong adoption figures partly reflect rapid adoption in technology hubs—in keeping with how economically consequential technologies have historically tended to diffuse." — [p.18]

> "We document a similar, but weaker correlation than at the global level between Claude adoption and income per capita across US states. Income differences explain less than half the variation in cross-state adoption rates." — [p.19]

> "The world map is based on Natural Earth's world map with the ISO standard point of view for disputed territories, which means that the map may not contain some disputed territories. We note that in addition to the countries shown in gray ('Claude not available'), we do not operate in the Ukrainian regions Crimea, Donetsk, Kherson, Luhansk, and Zaporizhzhia. In accordance with international sanctions and our commitment to supporting Ukraine's territorial integrity, our services are not available in areas under Russian occupation." — [p.28, Ch.2 endnote 5]

> "'No data' applies to countries with partially missing data. Some territories (e.g., Western Sahara, French Guiana) have their own ISO-3611 code. Some of these have some usage, others have none. Since the Anthropic AI Usage Index is calculated per working-age capita based on working age population data from the World Bank, and population data is not readily available for all of these territories, we cannot calculate the AUI for these territories." — [pp.28–29, Ch.2 endnote 6]

> "When further investigating Utah's activity, we discovered a notable fraction of its usage appeared to be possibly associated with coordinated abuse. This is also reflected in a much higher 'directive' automation score than average. However, we ran robustness checks and believe that this activity is not driving the results." — [p.29, Ch.2 endnote 7]

> "California also has disproportionately frequent requests for help with basic numerical tasks, which may represent tests of model capabilities or abuse." — [p.24]

**On the privacy censoring**

> "For privacy reasons, our automated analysis system filters out any cells—e.g., countries, and (country, task) intersections—with fewer than 15 conversations and 5 unique user accounts. For bottom-up request clusters, we have an even higher privacy filter of at least 500 conversations and 250 unique accounts." — [p.28, Ch.2 endnote 1]

> "When for privacy-preserving reasons we do not observe usage shares for a particular collaboration mode we give that category a value of 0% in this figure." — [p.37, Figure 3.5 caption]

> "Because some tasks have censored collaboration mode shares, we also include indicators for whether that a particular mode has missing data." — [p.45, Ch.3 endnote 13]

**On the construct validity of the API measures**

> "Of course, output length does not capture all dimensions of task complexity, but it appears to be a sensible, easily measured proxy." — [p.39]

> "Claude associated output length with task complexity." — [p.39, Table 3.1 caption; i.e. the complexity reading of the index is Claude's, from a minimal prompt]

> "Claude was prompted to identify tasks at the 10th, 50th, and 90th percentile of the ONET task distribution with the minimal organization of 'The columns should be 'Example tasks', 'Index Value', 'Summary' where you provide a summary'." — [p.45, Ch.3 endnote 9]

> "Another contributing factor could be the degradation in performance some models experience at longer context lengths." — [p.45, Ch.3 endnote 10]

> "In turn, any systematic relationship between input length and output produced by Claude partly captures the underlying contextual constraints in deploying Claude for sophisticated tasks." — [p.40; "partly" is the report's own hedge]

**On the cost analysis**

> "With the important caveat that this should be viewed as a preliminary exploration, this is what we find." — [p.42]

> "The question we ask in this section is whether, all else equal, cost differences across tasks shapes relative usage patterns. This is different from studying whether overall Claude usage is sensitive to external competitive pricing pressures." — [p.45, Ch.3 endnote 11]

> "We restrict attention to the set of tasks identified in both our API sample and our Claude.ai samples." — [p.45, Ch.3 endnote 13]

> "Our API data captures enterprise AI adoption in its early stages: highly concentrated, automation-focused, and surprisingly price-insensitive (at least among the tasks our API customers use Claude for)." — [p.43]

**On what the findings can and cannot say about labour markets**

> "But the implications for the labor market are not entirely clear." — [p.44]

> "Note that this is a different measure of adoption than in the introduction to this report. Reported adoption by consumers and employees of AI reached 40% in 2024 whereas when measured at the firm-level, nine out of ten businesses in the US report not using AI." — [p.44, Ch.3 endnote 3]

> "Setting aside questions of causality, the straightforward interpretation is that this is due to AI substituting for work previously done by early-career workers." — [p.47, concluding endnote 1]

---

## Open questions, conjectures and promised follow-ups (verbatim)

**The four questions the report asks the public data to answer** (pp.5–6):

> "Key questions we hope this data will help others to investigate include:
> - What are the local labor market consequences for workers and firms of AI usage & adoption?
> - What determines AI adoption across countries and within the US? What can be done to ensure that the benefits of AI do not only accrue to already-rich economies?
> - What role, if any, does cost-per-task play in shaping enterprise deployment patterns?
> - Why are firms able to automate some tasks and not others? What implications does this have for which types of workers will experience better or worse employment prospects?"

**On diffusion and convergence**

> "In other words, a hallmark of early technological adoption is that it is concentrated—in both a small number of geographic regions and a small number of tasks in firms. As we document in this report, AI adoption appears to be following a similar pattern in the 21st century, albeit on shorter timelines and with greater intensity than the diffusion of technologies in the 20th century." — [p.2]

> "The uneven geography of early AI adoption raises important questions about economic convergence." — [p.4]

> "If the productivity gains are larger for high-adoption economies, current usage patterns suggest that the benefits of AI may concentrate in already-rich regions—possibly increasing global economic inequality and reversing growth convergence seen in recent decades." — [p.4]

> "These geographic patterns provide real-world evidence about AI's economic diffusion, helping track whether different regions are converging or diverging in their AI adoption, and revealing how local economic characteristics shape technology deployment." — [p.12]

> "Our data provides a window into these patterns across geographies, and going forward, will enable us to track whether these adoption gaps narrow, widen, or change in structure over time." — [pp.12–13]

> "Drawing parallels to the diffusion patterns of prior technologies may help us better understand the diffusion and impact of AI." — [pp.27–28]

> "Similar to the local specialization in task use, the local specialization in AI collaboration patterns suggests that impact of AI could be very different in different regions." — [p.28]

> "The geographic patterns of AI adoption—where it is used, for which tasks, and how—suggest that in order to realize the potential of AI to benefit people across the globe, policymakers need to pay attention to local concentration of AI use and adoption, and address the risk of deepening digital divides." — [p.28]

> "These patterns risk creating divergence. If AI's productivity gains concentrate in already-prosperous regions and automation-ready sectors, existing inequalities could widen rather than narrow." — [p.46]

> "History shows that the patterns of technological adoption aren't fixed: they shift as the technologies mature, as complementary innovations emerge, and as societies make deliberate choices about their deployment. The patterns of highly concentrated use that we observe today may yet evolve towards a broader distribution—one that captures more of AI's productivity-enhancing potential, accelerates innovation in lagging sectors, and enables new forms of economic value creation." — [p.47]

**Conjectures about why usage differs across geographies** (p.17–18; five bullets offered without test):

> "The disparities in Claude usage likely reflect a confluence of factors, some of which are correlated with income:
> - Digital infrastructure: High-usage countries typically have robust internet connectivity and cloud computing access needed to access AI assistants.
> - Economic structure: As documented in this and previous reports, Claude capabilities are well-suited to various tasks typical of knowledge workers. Advanced economies tend to have a greater share of the workforce in such roles as compared to lower-income economies with a larger employment share in manufacturing.
> - Regulatory environment: Governments differ in how actively they encourage the use of AI across different industries and in how heavily they regulate the technology.
> - Awareness and access: Countries with stronger connections to Silicon Valley and AI research communities may have greater awareness of and access to Claude.
> - Trust and comfort: Public opinion on trust in AI varies substantially across countries."

> "This concentration in advanced economies with limited population sizes reflects their established patterns as technology pioneers. … suggesting that general investments in information technology position economies well for rapid adoption of frontier AI." — [p.16]

> "This suggests that other regional differences—including the compatibility of Claude capabilities with the occupational composition of the local workforce—play a larger role in determining why usage is more concentrated in some states than others." — [p.24]

**On the geographic collaboration finding — the report's own "more research is needed"**

> "In this section, we investigate whether automated use is systematically different among low and high per capita adoption economies—even when controlling for differences in task mix." — [p.26]

> "This is somewhat counter-intuitive, since we are controlling for the more diverse task composition across different countries. We speculate that cultural and economic factors might affect the automation share, or perhaps that early adopters in each country tend to use AI in a more automotive way—but more research is needed here." — [pp.26–27] (the report's only explicit "more research is needed"; "automotive" appears to be a typo for "automated"/"automative")

**On the rise in directive use — an explicitly unresolved fork**

> "One interpretation is that this is a result of increasing model capabilities. As models improve at anticipating user needs and producing high-quality outputs on first attempts, users may need fewer follow-up refinements. The jump in directive usage could also signal growing confidence in delegating complete tasks to AI, a form of learning-by-doing." — [p.10]

> "Whether the growth in directive usage is attributable to improving model capabilities or learning-by-doing could signal very different labor market implications. If more advanced models simply expand the set of automated tasks, then the risk increases that workers performing such tasks will be displaced. However, if instead the rise in directive use reflects learning-by-doing, then workers most able to adapt to new AI-powered workflows are likely to see greater demand and higher wages. In other words, AI may benefit some workers more than others: it may lead to higher wages for those with the greatest ability to adapt to technological change, even as those with lower ability to adapt face job disruption. This will be an important area of inquiry for future research." — [p.10]

> "We thank Anton Korinek for the observation that AI itself might accelerate the diffusion and economic impact of AI to the extent that it plays the role that skilled workers played in the past in figuring out how to effectively wield new technologies in novel settings." — [p.11, Ch.1 endnote 5]

> "This divergence suggests AI usage may be diffusing especially quickly among tasks involving knowledge synthesis and explanation, compared to traditional business operations—possibly because these tasks benefit more from Claude's reasoning capabilities." — [p.7]

> "This may suggest that models have become increasingly reliable, such that users spend less time fixing problems and more time creating things in a single interaction." — [p.9]

> "We view the evidence presented below as suggesting that new product features have enabled new forms of work rather than simply accelerating adoption for existing tasks." — [p.7]

**Promised next steps on measurement**

> "The next chapter of this report for the first time breaks down usage across geography, allowing us to disentangle temporal vs. geographic changes more clearly going forward. We will continue to track these trends closely in future reports." — [p.11]

> "Future work, for example using stratified sampling, will allow us to explore these patterns with higher accuracy given limited observations for smaller countries and states." — [p.28, Ch.2 endnote 4]

> "We'll continue tracking these patterns as AI capabilities advance, and provide empirical grounding for navigating one of the most significant economic transitions of our time." — [p.47]

**On why some tasks lead and others do not**

> "Across all countries, software development emerges as the most common use of Claude. Why do developer tasks consistently lead in overall Claude usage patterns? Several factors likely contribute to this effect:
> - Model-task fit: Claude is a very strong coding model and readily deployed across code generation, debugging, and technical problem-solving tasks.
> - Developer receptivity: Developer communities embrace new tools rapidly, and this usage diffuses through their social and professional networks.
> - Low organizational barriers: Individual developers can typically adopt Claude without complex approval processes—in contrast to, say, medical use cases." — [pp.23–24]

> "The long tail of rarely used tasks could reflect several factors. For example, some tasks are simply less common—debugging software happens far more often than negotiating circus contracts. The extreme concentration also suggests the potential role of O-Ring forces: if a task needs a level of reasoning Claude can't handle, internal data the firm can't access, or regulatory approval that doesn't exist, any single barrier could prevent adoption." — [p.35]

> "The similarity across platforms is particularly striking given their different user bases and use cases. Both converge on comparable concentration levels, suggesting a common matching process between AI capabilities and associated economic tasks." — [p.35]

> "Why do our API customers use Claude for some tasks more than others? Beyond fundamental model capabilities, a potentially important explanation is that it is easier to provide Claude with the information needed for successful deployment for some tasks than others." — [p.37]

**On enterprise adoption, context and pricing**

> "Institutional inertia, alongside fixed costs of adoption, suggests that early examples of enterprise use of AI is likely to be concentrated among specialized tasks where deployment is easy, capabilities are robust, and the economic benefits from adoption are high." — [p.30]

> "This could represent a barrier to broader enterprise deployment for some important tasks that rely on dispersed context that is not already centralized or digitized. Correcting for this bottleneck may require firms to restructure their organization, invest in new data infrastructure, and centralize information for effective model deployment." — [p.31]

> "The upshot is that deploying AI for complex tasks might be constrained more by access to information than on underlying model capabilities. Companies that can't effectively gather and organize contextual data may struggle with sophisticated AI deployment, creating a potential bottleneck for broader enterprise adoption—particularly for occupations and in industries where tacit, diffuse knowledge is crucial to business operations." — [p.41]

> "While this positive correlation holds overall, we next ask whether demand for Claude capabilities is lower among otherwise similar but costlier tasks." — [p.42]

> "Other factors, beyond the cost of using Claude for particular tasks, appear to matter more for patterns of use." — [p.43]

> "This implies that for some firms costly data modernization and organizational investments to elicit contextual information may be a bottleneck for AI adoption." — [p.5]

> "In the presence of fixed costs of adjustment, the question businesses face is not necessarily if they will adopt AI, but when." — [p.44, Ch.3 endnote 1]

**On the labour-market implications of API automation**

> "While both augmented and automated approaches enhance human capabilities, system-level automation is likely to yield both larger productivity gains across the economy as well as more significant changes in the labor market: Fully automating some tasks, changing which tasks are important for various jobs, and even producing new forms of work altogether." — [p.36]

> "Given clear automation patterns in business deployment, this may also bring disruption in labor markets, potentially displacing those workers whose roles are most likely to face automation." — [p.44]

> "But the implications for the labor market are not entirely clear. As we document above, complex tasks require disproportionately more context. Such information may be scattered across organizations. In such conditions, workers with tacit knowledge about business operations may stand to benefit as complements to sophisticated AI-powered automation. Understanding the uneven labor market implications of AI adoption is an important area for future research." — [p.44]

> "Businesses looking to adopt AI effectively may need to restructure how they organize and maintain the information that frontier systems rely on. Whether today's narrow, automation-heavy adoption evolves toward broader deployment will likely determine AI's future economic impacts." — [p.44]

> "If AI automation improves the productivity of workers with tacit organizational knowledge—as some of our evidence suggests—then more experienced workers could see rising demand and higher wages even as entry-level workers face worse labor market prospects." — [p.46]

> "An alternative interpretation is presented by Gans 2025, If AI and workers were strong complements, what would we see?: That relatively faster employment growth for experienced workers reflects AI making such workers more productive and thus in high demand. Whether AI compliments or substitutes work is perhaps the most important question that we hope our data will help answer." — [p.47, concluding endnote 1]

**On the purpose of the release**

> "By making this data public, we hope to enable others to investigate questions we haven't considered, test hypotheses about AI's economic impacts, and develop policy responses grounded in empirical evidence." — [p.47]

> "Ultimately, the economic effects of transformative AI will be shaped as much by technical capabilities as by the policy choices societies make." — [p.47]

---

## What it did not test

*Everything in this section is the wiki author's inference, not the report's. It records adjacent questions the report had the data to answer but did not, constructs it used without validating, and internal inconsistencies to avoid propagating.*

### Internal inconsistencies to be careful of

- **I1. Three different V3 education shares.** The headline bullet says educational tasks rose "from 9.3% to 12.4%" (p.3); Chapter 1 says "from 9% in V1 to 12% in V3" (p.7); Figure 1.1 plots 12.7% for Aug 2025 (p.8); Chapter 3 uses 12.3% as the Claude.ai education share when comparing to the API (p.33). Similarly for science: 7.2% (p.3) vs 7.4% (Figure 1.1). A post that reproduces "the published number" must say which one, and the release's `soc_pct` for the `GLOBAL` geography is the only arbiter.
- **I2. The Gini coefficients.** The text reports "Gini coefficients of 0.84 and 0.86" for Claude.ai and the API respectively (p.34); Figure 3.4's legend reports 1P API = 0.842 and Claude.ai = 0.822 (p.35). 0.86 appears nowhere in the figure. The figure is the more likely correct pair, and it reverses the text's implied ordering of magnitude gap.
- **I3. "Immaterial" versus −0.29.** Page 41 concludes that "cost plays an immaterial role in shaping patterns of enterprise AI deployment"; page 42 then estimates a conditional elasticity of −0.29 and calls the result "consistent with standard economic theory that higher prices lead to lower demand"; the summary bullet calls it "weak price sensitivity" (p.5). These are three different claims about the same object. An own-price elasticity of −0.29 is small but is not zero, and no confidence interval is given for it.
- **I4. Debugging: −2.8pp or −2.9pp.** p.9 gives 16.1% → 13.3% (−2.8pp); p.3 gives −2.9pp. The stated "net 7.4pp shift" is consistent only with the −2.9pp version.
- **I5. The state income sentence, reversed.** p.19: "Income differences explain less than half the variation in cross-state adoption rates." p.24: "cross-state differences in the Anthropic AI Usage Index account for less than half of the variation in income differences across US states." These are not the same statement; only the first matches the regression described.
- **I6. Tier label.** The tier definition text calls the third tier "Lower Middle (25%-75%)" (p.15); Table 2.1, Table 2.2 and both maps call it "Lower middle (25-50%)".
- **I7. Figure cross-references differ between the PDF and the web page.** In Chapter 3 the PDF's in-text references are internally consistent (Figures 3.5, 3.6, 3.8, 3.9); the web page's body text points to Figures 3.6, 3.7, 3.9 and 3.10 while its captions still read 3.5–3.9. Cite the PDF.
- **I8. Singapore's AUI is given three ways.** 4.6x (p.3), "4.5 times" (p.12), 4.57 (Figure 2.2, p.14).

### Adjacent questions the report had the data to test but did not

- **The state-level income regression is never plotted or tabulated.** The cross-country relationship gets a figure, a β, a p-value and an R²; the cross-state elasticity of 1.8 gets a sentence. Both GDP series and both AUI series are in the release, so the state regression — with its R², its standard error, and the leverage of DC and Utah — is directly recomputable, as is the question of whether the 1.8-versus-0.7 difference is statistically distinguishable at all. The report does not ask whether the state elasticity is being driven by DC, a single non-state observation with N = 1.8k.
- **Whether the Figure 2.7 "diversification" story survives its own statistics.** The panel that carries the claim (Computer and Mathematical) has p = 0.385 and R² = 0.007. The report's own hedge is "noisy", but it does not report the obvious alternatives: weighting countries by usage rather than equally (the caption states it weights equally), restricting to the ≥1,000-observation countries, or testing a diversity index (Herfindahl or entropy across SOC groups) rather than four separate group shares. A diversity index is the construct the narrative actually claims and is constructible from `soc_pct`.
- **Whether the automation–AUI relationship survives income.** Figure 2.11 residualises on task mix only. GDP per working-age capita is in the same release and is the variable the report says AUI is 0.69-elastic to. Whether the automation gradient is an adoption gradient or an income gradient is untested, and the two are not separable by the report's own design.
- **Whether the automation–AUI relationship survives the `not_classified` share.** The automation and augmentation percentages are shares "of classifiable collaboration". If the censored share varies systematically with country sample size — and it must, because the privacy filters are absolute counts — then the denominator varies with AUI. The report never reports the `not_classified` share by country, nor tests whether it correlates with AUI.
- **Whether 77% + 12% = 89% matters.** The 11% of API transcripts that are neither automation nor augmentation is never named or explained in the text. Whether it is `not_classified`, `none`, or a mixture changes whether "77% automation" is a share of all traffic or of classifiable traffic, and therefore whether it is comparable with the Claude.ai "nearly even" split.
- **The Utah robustness check is asserted, not shown.** The report states that a notable fraction of Utah's usage may be coordinated abuse with an abnormally high directive score, that checks were run, and that the checks were reassuring. No excluded-Utah AUI, no re-estimated state elasticity, no re-estimated directive share is given. Utah is the second-ranked state and one of the two observations that makes the DC/Utah-over-California headline.
- **The V1→V3 trend is never decomposed into geography.** The report itself names this as the reason geography was introduced (p.11) but does not do the decomposition, even for the one wave where it has geography: it cannot, because V1 and V2 have no geographic cut. So "changes in the underlying user base" remains an unaddressed rival explanation for the entire Chapter 1 result, including the automation crossover.
- **No sampling uncertainty anywhere.** Every AUI is a ratio of two estimated shares from a 1-million random sample, and Figure 2.2 and Figure 2.5 print the Ns (down to N = 283 for Malta and N = 430 for Vermont), but no interval is attached to any index value, tier boundary or rank. Whether Israel's 7.00 is distinguishable from Singapore's 4.57, or DC's 3.82 from Utah's 3.78, is not addressed. The tier cut-points are point estimates of quartiles of a noisy distribution.
- **Cost is measured but price is not.** The API cost index is realised spend per transcript — tokens × the price of whatever model the customer chose. A task that is expensive because customers route it to a larger model is not the same object as a task that is expensive because it needs more tokens at a fixed price. The release carries `prompt_tokens_index`, `completion_tokens_index` and `cost_index` separately, so the model-choice channel is partly separable, but the report does not separate it, does not report which models are in the sample, and does not use any published price schedule. The −0.29 "elasticity" is therefore a correlation between realised spend and usage across tasks, not a demand elasticity with respect to a price the customer faces.
- **The input–output elasticity is not identified as a context constraint.** The report's own argument requires that customers minimise input tokens subject to completing the task (p.40). Under that assumption, β = 0.38 is read as diminishing returns to context. But the same β is consistent with output length caps, with `max_tokens` settings, with customers who truncate outputs for downstream systems, and with the long-context degradation the report itself flags in endnote 10 (p.45). None of these is tested, and none is testable from the released aggregates.
- **Cross-surface comparisons rest on non-commensurate units.** Every Claude.ai-versus-API number in Chapter 3 (Figure 3.3, Figure 3.4, Figure 3.5, the 77%/50% comparison) compares conversations with prompt-response pairs, some of them mid-session. The report never estimates how many prompt-response pairs a session contains, nor what the comparison would look like at the session level, though it could have reported the multi-turn share.
- **"Enterprise" is an inference from the surface, not an observation of the buyer.** Chapter 3's title, the "businesses use Claude" framing and the "firms" language all rest on the API surface as a proxy for a firm. The sample is "a pool of 1P API customers" of unstated composition — solo developers, startups, and companies of any size all appear as API traffic, and the report's own Figure 3.2 includes clusters ("Develop, configure and evaluate AI systems across domains", 5.2%) that are as consistent with AI-lab and hobbyist use as with enterprise production. No firm size, industry, geography or customer count is reported, and the report cannot say what fraction of traffic comes from how many customers. It also cannot see third-party API traffic (Bedrock, Vertex), so "half of our 1P API usage" is an unknown fraction of all Claude enterprise usage.
- **BTOS is invoked as context and then not used.** `BTOS_National.xlsx` is shipped in the release inputs, the report plots the national adoption series and quotes the Information-versus-Accommodation sector contrast, but it never maps its own O*NET/SOC task mix onto BTOS industries — which is the one comparison that would test the claim on p.31 that API use is "primarily deployed for tasks typical of Information sector occupations". The claim is asserted, not measured.

### Constructs used without validation

- **The AUI's denominator.** Working-age population is a proxy for the population that could use Claude. No internet-using population, no knowledge-worker share, no English-proficiency adjustment, no smartphone/broadband penetration adjustment is offered, although the report's own "digital infrastructure" and "economic structure" conjectures (p.17) say that the denominator is the wrong one. The AUI therefore cannot distinguish "few people here use Claude" from "few people here could".
- **IP geolocation as the location of the user.** VPN, anycast and hosting traffic is excluded on the provider's determination, which is an unvalidated classifier; the residual accuracy of the provider is not reported. DC's 3.82 in particular mixes residents, commuters and federal-network traffic, and no test distinguishes them.
- **The collaboration classifier as a measure of delegation.** The five patterns are LLM judgements over conversation transcripts. The report reports one classifier-swap robustness check on the aggregate automation share (p.11) and nothing on per-pattern agreement, no human-coded validation set, no confusion matrix, and no check that the classifier behaves the same way across languages — which matters directly, because the headline geographic finding is a cross-country difference in classified collaboration mode, and non-English conversations are concentrated in exactly the low-AUI countries where the automation residual is highest. Language is neither reported nor controlled for anywhere in the report.
- **"Automation" as delegation, and its relation to autonomy.** The report glosses directive as "users delegate complete tasks to Claude" (p.3). That is a statement about interaction shape, not about how much decision-making the user handed over; a one-shot translation request is directive but low-autonomy. The report does not separate the two and, unlike later Index waves, has no autonomy measure.
- **The output token index as a complexity proxy.** The complexity reading comes from Claude summarising task lists under a deliberately minimal prompt (p.45, endnote 9), and the report says as much. There is no external complexity benchmark (O*NET Job Zone, required education, task-statement length) against which the index is checked, although O*NET ships several and the release ships O*NET 20.1.
- **O*NET as a task taxonomy for non-US economies.** O*NET is described in the report as "a US taxonomy" (p.20). Every cross-country task-mix comparison, including the India-coding claim and the whole of Figure 2.7, is therefore measured through the occupational structure of the United States. The report notes the taxonomy limitation in general terms ("provide flexibility to capture tasks that standard taxonomies miss", p.21) but never asks whether O*NET coverage itself varies by country.
- **The occupation attached to a task is not the occupation of the user.** Nothing in the data observes who is typing. Chapter 2's local-specialisation readings ("financial services in Florida", "career assistance in DC") treat task mix as evidence about the local workforce; that inference is not tested against any local employment statistic, though BEA and Census data are already in the release.
- **Tier membership as a variable.** Countries below the 200-observation threshold are assigned tiers from cut-points estimated only on countries above it, and zero-usage countries are placed in a "Minimal" tier that the report says it cannot distinguish from "little usage our sample did not capture" (p.28). Tier is then used as the selection rule for the flagship request-cluster figures (2.8, 2.9), so the choice of Brazil, Vietnam, India, Texas, Florida and South Carolina as exemplars is downstream of a construct the report calls uncertain.

---

## Verification

- **Date of verification:** 2026-09-16.
- **URLs fetched and read in full on that date:**
  - `https://assets.anthropic.com/m/218c82b858610fac/original/Economic-Index.pdf` — downloaded (13,850,183 bytes), text extracted with `pdftotext -layout`, all 48 pages read. This is the source for every `[PDF p.N]` quotation and every claim page reference.
  - `https://www.anthropic.com/research/anthropic-economic-index-september-2025-report` — fetched and read in full, including all endnotes, the citation block and the author list. Used to confirm the title, date, author list and the PDF link, and to establish the PDF/web figure-cross-reference divergence recorded as item I7.
  - `https://arxiv.org/abs/2511.15080` — fetched; abstract, author list, subject classes, DOI and submission date (19 Nov 2025) read. The arXiv listing page confirms the report's four headline findings in Anthropic's own abstract wording; the arXiv PDF itself was not downloaded, so nothing in this file is sourced to it.
  - `https://huggingface.co/api/datasets/Anthropic/EconomicIndex/tree/main/release_2025_09_15?recursive=true` — fetched; full 38-entry file listing with sizes read. Source for the release file names and the 4–11 August 2025 window on the API file.
  - `https://huggingface.co/datasets/Anthropic/EconomicIndex/raw/main/release_2025_09_15/data_documentation.md` — fetched (20,133 bytes) and read in full. Source for every `[data_documentation.md]` quotation, for the external-data provenance in §Data and methods, and for the `not_classified` / `none` / index-exclusion definitions, none of which appear in the PDF.
  - `https://huggingface.co/datasets/Anthropic/EconomicIndex/raw/main/release_2025_09_15/README.md` — fetched (2,640 bytes) and read in full. Source for the replication pipeline order and for the missing-notebook mismatch noted in §Data and methods.
- **Figures whose values do not survive PDF text extraction** were read off page renders at 130–150 dpi (`pdftoppm -png`): p.8 (Figure 1.1, all eight panels and all 24 data labels), p.10 (Figure 1.2, both panels), p.13 (Figure 2.1, all 30 country labels), p.17 (Figure 2.4, β and R²), p.22 (Figure 2.7, all four panels' β, p and R²), p.27 (Figure 2.11, β, R² and p), p.35 (Figure 3.4, Gini legend and both fit equations), p.38 (Table 3.1, which is an image in the PDF and has no text layer at all), p.42 (Figure 3.8, R² and β). The sign of every regression coefficient was confirmed visually, because the minus sign is dropped by the text layer: this is how the negative signs on Figure 2.7's Computer and Mathematical panel (β = −0.700) and on Figure 2.11 (β = −3.112) were established.
- **Could not be fetched or does not exist:**
  - **There is no appendix.** The September 2025 report has no separate appendix document and no appendix section: pp.2–47 are Introduction, three chapters and Concluding remarks, and PDF p.48 is blank. What the director's brief calls "appendix results" are carried in the per-chapter endnotes (Introduction 1–5 on p.6; Chapter 1 endnotes 1–5 on p.11; Chapter 2 endnotes 1–9 on pp.28–29; Chapter 3 endnotes 1–14 on pp.44–45; Concluding remarks endnote 1 on p.47) and in the release's `data_documentation.md`. Every one of those endnotes is quoted or cited above; the methodological ones are in §Definitions, §Limitations and §Open questions, and the endnote-only empirical results (task-level moves, the Sonnet 3.7 rerun, the Utah check, the BTOS question wording, the Figure 3.9 control set) appear as claims 20–21, 25, 29, 58, 59, 61 and 86.
  - The `www-cdn.anthropic.com/7b76335c444876a93fa22a63aabb4aeb820aff25.pdf` mirror named in `wiki/INDEX.md` was not separately downloaded; the `assets.anthropic.com` copy was used. Their identity was not re-verified in this thread.
  - The arXiv PDF was not downloaded, so no claim here is attributed to it; whether the arXiv version's pagination or figure numbering matches the Anthropic PDF is unverified.
  - The interactive dashboard referenced on p.25 (`anthropic.com/economic-index#us-usage`) was not exercised; nothing here rests on it.
- **Quotation check.** Every passage in §Definitions (verbatim), §Limitations (verbatim) and §Open questions, conjectures and promised follow-ups (verbatim) was copied from the text extracted from the fetched PDF, or from the fetched `data_documentation.md`, and its page or section reference was read from the same extraction. Where the source contains a typographical error — "gobal", "signifcance", "Lower Middle (25%-75%)", "automotive", "ISO-3611", "whether that a particular mode" — it is reproduced as printed and marked. No quotation in those three sections has been paraphrased, trimmed mid-sentence without ellipsis, or reconstructed from memory.
