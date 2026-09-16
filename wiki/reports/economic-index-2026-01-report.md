# economic-index-2026-01-report

## Source

- **Title:** *The Anthropic Economic Index report: Economic Primitives* (cover page title, p.1). The landing page heads it "Anthropic Economic Index report: Economic primitives"; the running footer on every page reads "The Anthropic Economic Index Report".
- **Authors (p.1):** Ruth Appel,\* Maxim Massenkoff,\* Peter McCrory\* (lead authors, "Contributed equally to this report"); Miles McCain, Ryan Heller, Tyler Neylon, Alex Tamkin.
- **Acknowledgements (p.1):** Xabi Azagirre, Tim Belonax, Keir Bradwell, Andy Braden, Dexter Callender III, Sylvie Carr, Miriam Chaum, Ronan Davy, Evan Frondorf, Deep Ganguli, Kunal Handa, Andrew Ho, Rebecca Jacobs, Owen Kaye-Kauderer, Bianca Lindner, Kelly Loftus, James Ma, Jennifer Martinez, Jared Mueller, Kelsey Nanan, Kim O'Rourke, Dianne Penn, Sarah Pollack, Ankur Rathi, Zoe Richards, Alexandra Sanderford, David Saunders, Michael Sellitto, Thariq Shihipar, Michael Stern, Kim Withee, Mengyi Xu, Tony Zeng, Xiuruo Zhang, Shuyi Zheng, Emily Pastewka, Angeli Jain, Sarah Heck, Jared Kaplan, Jack Clark, Dario Amodei.
- **Published:** January 15, 2026 (p.1; landing page "Jan 15, 2026").
- **Document type:** Economic Index report — the fourth in the series. The report calls itself "This fourth Anthropic Economic Index report" (p.54) and refers to its own wave as "V4" in figure legends (Figs 1.4, 1.6, 1.8).
- **Primary URL:** https://www.anthropic.com/research/anthropic-economic-index-january-2026-report
- **PDF:** https://www-cdn.anthropic.com/096d94c1a91c6480806d8f24b2344c7e2a4bc666.pdf — **55 pages.**
- **Online appendix (separate document):** https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/main/release_2026_01_15/aei_v4_appendix.pdf — *Online Appendix: Economic Primitives and Classification Prompts*, 19 pages, produced by LaTeX with hyperref, PDF creation date 2026-01-15 19:35:15 UTC, 6,036,245 bytes.
- **Release the report rests on:** `release_2026_01_15` on the `Anthropic/EconomicIndex` Hugging Face dataset. Sample window **November 13–20, 2025** for both platforms (fn1, p.17; fn2, p.36). The report states the data "predates the release of Opus 4.5" (p.42) and describes the window as "just prior to the release of Opus 4.5" (p.2).
- **Companion blog post:** the short general-reader post at https://www.anthropic.com/research/economic-index-primitives is a separate wiki entry (`economic-index-2026-01-blog`) and is not covered here.

**Correction to the index row (wiki author's note, 2026-09-16).** `wiki/INDEX.md` line 19 records the appendix as "appendix inline from p.40, no separate document". That is not what the fetched PDF contains. The 55-page report PDF runs Introduction (pp.2–4), Chapter 1 (pp.5–18), Chapter 2 (pp.19–27), Chapter 3 (pp.28–37), Chapter 4 (pp.38–53), Concluding Remarks (pp.54–55), with no appendix section. Page 40 carries a *reference* to "Appendix Figure A.1", and fn2 on p.52 states "Our online appendix is available at https://huggingface.co/datasets/Anthropic/EconomicIndex". The appendix is the separate 19-page `aei_v4_appendix.pdf` on Hugging Face, fetched and covered in this file. The index row needs amending; a room note has gone to the director.

---

## Claims

Every claim below is quoted or paraphrased from the fetched text with its page and, where one exists, its figure or table number. Where the report gives a regression statistic only inside a figure's inset box, that is marked "(figure inset)". Page numbers are the report's own printed page numbers, which match the PDF page numbers throughout.

### Chapter 1 — what changed since the September 2025 report

1. **Task concentration on Claude.ai rose marginally.** "The ten most common tasks represent 24% of usage on Claude.ai, up from 23% in our last report" (p.5). Elaborated on p.6: "The share of conversations assigned to the ten most prevalent O\*NET tasks was 24% in November 2025, 1pp higher than in August and up from 21% in January 2025." Comparison: Nov 2025 vs Aug 2025 (V3) vs Jan 2025 (V1). Figure 1.1 plots the series and labels four points: Jan 2025 21%, Mar 2025 24%, Aug 2025 23%, Nov 2025 24% (p.7, Fig 1.1).
2. **The single most common Claude.ai task.** "The most prevalent task in November 2025—modifying software to correct errors—alone represented 6% of usage" (p.6). Comparison: share of one O\*NET task within the Claude.ai sample.
3. **Task concentration on the 1P API rose more sharply.** "For first-party (1P) API enterprise customers, concentration among tasks increased more notably: the top ten tasks now represent 32% of traffic, up from 28% in the last report" (p.5); "The ten most common tasks grew from 28% of API records in August to 32% in November" (p.6). Figure 1.1 labels Aug 2025 28% and Nov 2025 32% for the 1P API line, which begins only in Aug 2025 (p.7, Fig 1.1).
4. **The most common API task matches the most common Claude.ai task.** "As with Claude.ai the most common task among API customers was modifying software to correct errors, which accounted for one in ten records" (p.7).
5. **Breadth of the task distribution.** "While we see over 3,000 unique work tasks in Claude.ai, the top 10 most common tasks account for 24% of our sampled conversations" (p.2).
6. **Coding tasks still dominate both platforms but have declined on Claude.ai.** "computer and mathematical tasks—like modifying software to correct errors—continue to dominate Claude usage overall, representing a third of conversations on Claude.ai and nearly half of 1P API traffic. Such dominance has subsided on Claude.ai: the share of conversations on Claude.ai assigned to such (mostly) coding-related tasks is down from a peak of 40% in March 2025 to 34% in November 2025. At the same time, the share of transcripts assigned to computer and mathematical tasks among 1P API traffic edged higher from 44% in August to 46% in November 2025" (p.7, with Fig 1.2). Comparison: Claude.ai Mar 2025 peak vs Nov 2025; API Aug vs Nov 2025.
7. **Educational Instruction and Library is the second largest Claude.ai category and has risen throughout the series.** "The second largest share of Claude.ai usage in November 2025 was in the Educational Instruction and Library category… Such usage has risen steadily since our first report, up from 9% of conversations on Claude.ai in January 2025 to 15% in November" (p.8, Fig 1.2). Comparison: Jan 2025 vs Nov 2025.
8. **Arts, Design, Entertainment, Sports and Media rose on Claude.ai, reversing a decline.** "The share of usage on Claude.ai for Arts, Design, Entertainment, Sports, and Media tasks increased between August and November 2025 as Claude was used in a growing share of conversations for writing tasks, primarily copyediting and the writing and refinement of fictional pieces. This jump in the prevalence of design- and writing-related tasks reversed a steady decline across earlier reports" (p.8, Fig 1.2).
9. **Life, Physical and Social Science fell on both platforms.** "For both Claude.ai and API customers, there was a drop in the share of conversations/transcripts where Claude was used for Life, Physical, and Social Science-related tasks" (p.8, Fig 1.2).
10. **Back-office work grew fastest on the API.** "Perhaps the most notable development for API customers was the increase in the share of transcripts associated with Office and Administrative Support related tasks, which rose 3pp in August to 13% in November 2025" (p.8, Fig 1.2). The inference drawn: "Because API use is automation-dominant, this suggests that businesses are increasingly using Claude to automate routine back-office workflows such as email management, document processing, customer relationship management, and scheduling" (pp.8–9).
11. **Named back-office request clusters on the API, with shares.** "Generate personalized B2B cold sales emails" (0.47%), "Analyze emails and draft replies for business correspondence" (0.28%), "Build and maintain invoice processing systems" (0.24%), "Classify and categorize emails into predefined labels" (0.23%), "Manage calendar scheduling, meeting coordination, and appointment booking" (0.16%) (fn4, p.18). These are bottom-up request clusters, not O\*NET tasks.
12. **Augmentation overtook automation again on Claude.ai.** "The share of conversations classified as augmented jumped 5pp to 52% and the share deemed automated fell 4pp to 45%" (p.5; Fig 1.3, p.10, labels Claude.ai Nov 2025 at 52% augmentation / 45% automation). Comparison: Nov 2025 vs Aug 2025 (49% automation / 47% augmentation per the Fig 1.3 labels).
13. **The unclassified residual shrank.** "The share of conversations on Claude.ai that were classified into neither automation nor augmentation categories fell from 3.9% to 3.0%" (fn2, p.17).
14. **The one-year baseline.** "In January 2025, augmented use of Claude was dominant: 56% of conversations were classified as augmentation compared to 41% automated" (p.9). Figure 1.3 labels Jan 2025 at 55%/41% and Mar 2025 at 55%/42% for Claude.ai (p.10, Fig 1.3) — the figure label (55%) and the body text (56%) differ by a point.
15. **The directive share reversed.** "From January 2025 to August 2025 the share of such directive conversations rose from 27% to 39%" (p.9); "Three months later, the share of directive conversations had fallen 7pp to 32% in November 2025" (p.9). Comparison: Jan → Aug → Nov 2025.
16. **The automation trend is read as still upward despite the reversal.** "the automation share was still elevated as compared to nearly one year ago when we first began tracking this measure, suggesting that the underlying trend is still toward greater automation even as the August spike overstated how quickly it was materializing" (p.9).
17. **The reversal was driven by task iteration, not learning.** "The rise in augmented use was driven mainly by users iterating with Claude to complete tasks ('task iteration') rather than asking Claude to explain concepts ('learning')" (pp.9–10, with Fig 1.4).
18. **The API remained automation-dominant and barely moved.** Figure 1.3 (p.10) labels the 1P API panel: automation 77% in Aug 2025 and 75% in Nov 2025; augmentation 12% in Aug and 14% in Nov. The figure note states "Automation = Directive + Feedback loop. Augmentation = Validation + Task iteration + Learning."
19. **Collaboration shares by SOC major group, with sample sizes.** Figure 1.4 (p.11) reports V4 shares of Directive / Task Iteration / Learning by SOC major group with n per group, including Production (n=6k), Arts/Design/Entertainment/Sports and Media (n=92k), Personal Care and Service (n=6k), Business and Financial Operations (n=23k), Sales and Related (n=25k), Management (n=24k), Architecture and Engineering (n=12k), Office and Administrative Support (n=70k), Educational Instruction and Library (n=145k), Life/Physical/Social Science (n=46k), Healthcare Practitioners and Technical (n=17k), Computer and Mathematical (n=329k), Community and Social Service (n=25k); V3 is plotted alongside. Restriction: "O\*NET tasks that have at least 100 observations in our sample. We weight observations by number of records to construct a representative sample."
20. **Vocabulary signatures of the three main collaboration modes.** "Directive interactions emphasize production ('create,' 'develop,' 'draft'); Task Iteration centers on refinement and iteration ('edit,' 'rewrite,' 'revise'); Learning focuses on explanation and knowledge transfer ('help,' 'explain,' 'provide'). Patterns are consistent across both classification methods" (Fig 1.5 caption, p.11). Restriction: top quartile of O\*NET tasks and bottom-up request groups with at least 1,000 observations.

### Chapter 1 — geography, the AUI, and the state convergence model

21. **The five leading countries by overall use.** "The US, India, Japan, the UK, and South Korea lead in overall Claude.ai use" (p.2). The supporting ranking is Online Appendix Figure 2 ("Leading countries in terms of global Claude.ai usage share").
22. **A worked AUI value.** "Denmark has an AUI of 2.1, meaning its residents use Claude at roughly twice the rate its share of the global working-age population would suggest" (p.12).
23. **US usage is concentrated in a handful of states.** "the top five US states account for nearly half (50%) of all usage despite representing only 38% of the working-age population" (pp.5–6). Comparison: usage share vs working-age population share.
24. **Cross-country AUI concentration did not change.** "the left panel of Figure 1.6 shows that the AUI concentration across countries was essentially unchanged between our last report and this report" (p.12). The figure legend gives the numbers: countries Gini = 0.478 in V3 (Aug 2025) and 0.468 in V4 (Nov 2025) (Fig 1.6, p.13, figure inset).
25. **US state AUI concentration fell.** "the Gini coefficient, a standard measure of equality, fell from 0.37 to 0.32" (p.12). The figure legend gives 0.367 (V3 Aug 2025) and 0.318 (V4 Nov 2025) (Fig 1.6, p.13, figure inset) — the body text rounds these to two decimals.
26. **A back-of-envelope extrapolation from the Gini.** "If the Gini coefficient for the US again falls by 0.05 every three months, then parity of usage would be reached in roughly two years" (p.12).
27. **Lorenz-curve reading.** "the top 20 percent of US states accounted for 40 percent of population-adjusted usage in the US" (Fig 1.6 caption, p.13).
28. **Global convergence: no evidence either way.** "Globally, Claude usage per capita—as captured by the Anthropic AI Usage Index (AUI)—remains highly uneven and strongly correlated with GDP. These gaps are stable: we see no evidence that low-use countries are catching up or that high-use countries are pulling away" (p.6).
29. **The tech-workforce elasticity — the headline geography number.** "each 1% increase in the share of such tech workers in a state is associated with 0.36% higher usage per capita (Figure 1.7). This alone accounts for nearly two-thirds of the cross-state variation in AUI" (p.13). The fitted line in the figure inset reads `ln(AUI) = 0.36 × Comp & Math Share − 1.40, R² = 0.61` (Fig 1.7, p.14, figure inset). Note that the regressor in the inset is the share in percentage points, not its log, so the coefficient is a semi-elasticity per percentage point of employment share; the body text renders it as a percentage-change-per-percentage-change relationship. Named high-AUI states: "Washington D.C., Virginia, and Washington" (p.13).
30. **The result generalises beyond tech workers, via KL divergence.** "Usage per capita is higher in states with more workers in occupations where Claude usage is overrepresented as compared to the US workforce (e.g., Arts, Design, Entertainment, Sports and Media) or with relatively fewer workers in occupations where Claude usage is low as compared to the national economy (e.g., Transportation and Material Moving)… States with a lower KL divergence—and thus with a workforce that looks more similar to Claude usage patterns—tend to have higher usage per capita" (p.14).
31. **Within the US income is not the predictor it is globally.** "Within the US, income is less clearly a predictor of usage. Instead, what appears to matter most is the composition of each state's workforce and how well-matched the workforce is to Claude capabilities as reflected in task-level usage" (p.13).
32. **The convergence benchmark.** "with quarterly data a value of β = 0.99 implies a half-life of about 17 years. To illustrate, starting from an initial AUI of 2, this means AUI would decline to around 1.4 after 17 years and to around 1.1 after 50 years. We take β = 0.99 as a sensible benchmark because it implies a pace of diffusion similar to economically consequential technologies in the 20th century" (p.15).
33. **The OLS and WLS convergence estimates.** "Naively estimating this equation by ordinary least squares (OLS) yields an estimate of β̂ ≈ 0.77. Weighted least squares (WLS) where we weight by each state's workforce yields an estimate of β̂ ≈ 0.76 (Figure 1.8). Both are statistically distinguishable from 1 at conventional levels" (p.15). The figure inset gives `OLS: ln(AUI_v4) = 0.77 × ln(AUI_v3) − 0.03, R² = 0.83` and `WLS: ln(AUI_v4) = 0.76 × ln(AUI_v3) + 0.00, R² = 0.79` (Fig 1.8, p.16, figure inset).
34. **The constant is estimated as zero, as the model requires.** "We include a constant term in the regression since it should be equal to zero under the null hypothesis. Across all our specifications, the constant term is estimated to be close to and statistically indistinguishable from zero" (fn8, p.18).
35. **The attenuation-bias concern and the 2SLS fix.** "our AUI estimates are subject to sampling noise and other variation unrelated to diffusion. This can produce classical attenuation bias: even if AUI is not actually changing, our estimate of [β] could end up meaningfully below one" (p.16). The instrument: "instrumenting the log of AUI in August 2025 with the composition of each state's workforce, measured by its proximity to overall Claude usage patterns" (p.16); the identifying argument is "workforce composition is a strong predictor of Claude usage (relevance) but being measured independently, is expected to be uncorrelated with sampling noise in our AUI estimates (validity)" (pp.16–17).
36. **The 2SLS estimates.** "The 2SLS estimates imply modestly slower convergence: β̂ ≈ 0.89 unweighted and β̂ ≈ 0.86 when weighting by each state's working-age population. However, these estimates are less precise, and only the former is statistically distinguishable from 1 at the 10% level. Despite implying a slower convergence than OLS, the 2SLS estimates still imply rapid diffusion: just four to five years for the log deviation of each state's AUI to shrink by 90%" (p.17).
37. **The headline diffusion claim and its historical comparison.** "usage per capita would be equalized across the country in 2-5 years, a pace of diffusion roughly 10x faster than the spread of previous economically consequential technologies in the 20th century" (p.6). The 20th-century benchmark is Kalanyi et al. (2025), quoted at fn3, p.17: "Second, as the technologies mature and the number of related jobs grows, hiring spreads geographically. This process is very slow, taking around 50 years to disperse fully." Also p.15: "Economically consequential technologies have historically taken around half a century to achieve full diffusion across the US (Kalanyi et al., 2025)."
38. **Seychelles and Wyoming are dropped for abusive traffic.** "We exclude the Seychelles from all geographic analyses because a large fraction of usage we saw during the sampling dates was abusive traffic" (fn5, p.37). "We exclude Wyoming from all US state analyses because a large fraction of usage we saw during the sampling dates was abusive traffic" (fn6, p.37).

### Chapter 2 — the five economic primitives

39. **What is new, and how many classifiers implement it.** "This report introduces five new economic primitives beyond the one we already measure, collaboration patterns… These primitives capture five dimensions of a human-AI conversation: 1) task complexity, 2) human and AI skills, 3) work, coursework or personal use case, 4) the AI's level of autonomy, and 5) task success" (p.19). "We selected a final set of nine new classifiers for the five primitives, all of which are directionally accurate even if they may deviate somewhat from human ratings" (p.22). The nine classifiers named in Table 2.1 (p.20): human time estimate, human with AI time estimate, multitasking, human ability to complete task alone, human education years, AI education years, work vs. coursework vs. personal, AI autonomy, task success.
40. **AI autonomy is explicitly distinguished from automation.** "AI autonomy captures something different from our existing automation/augmentation distinction. For example, 'Translate this paragraph into French' is high automation (directive, minimal back-and-forth) but low AI autonomy (the task requires little decision-making from Claude)" (p.19).
41. **Global Claude.ai averages for all nine primitives.** Figure 2.2 (p.25), Global average, N = 999,875: Human time **3.1 h**; Human and AI time **15.4 min**; Multitasking **9%**; Human could do alone **88%**; Human education **12.2 years**; AI education **12.2 years**; Work use **46%**; AI autonomy **3.4**; Task success **67%**.
42. **Software-development request cluster.** Figure 2.2 (p.25), "Develop, debug and optimize software", N = 147,984: Human time 3.3 h; Human and AI time 15.8 min; Multitasking 8%; Human could do alone 82%; Human education 13.8 years; AI education 13.8 years; Work use 64%; AI autonomy 3.5; Task success 61%. The cluster's full label is "Help debug, develop, and optimize software across multiple programming domains" (p.25).
43. **Personal-life-management request cluster.** Figure 2.2 (p.25), N = 26,460: Human time 1.8 h; Human and AI time 14.7 min; Multitasking 10%; Human could do alone 96%; Human education 9.1 years; AI education 9.4 years; Work use 17%; AI autonomy 3.5; Task success 78%. Full label: "Assist with personal life management and everyday tasks" (p.25).
44. **Reading of the contrast.** "Claude estimates that users would be able to complete personal life management requests by themselves 96% of the time, versus 82% for software development requests—indicating that Claude provides more essential support for technical work" (p.25). And: "Claude assesses personal tasks as successfully completed 78% of the time, versus 61% for software development. Harder tasks—those requiring more specialized knowledge and where users could not easily complete them alone—show lower estimated success rates" (p.26).
45. **Autonomy barely distinguishes the two clusters.** "Both clusters show similar estimated autonomy levels (~3.5 on a 1 to 5 scale), near the global average. This means that both software development and personal life management tasks, on average, afford Claude a similar autonomy to make decisions on how to complete the task" (p.26).
46. **The headline use-case split on Claude.ai.** "Overall, Claude.ai use is 46% work, 19% coursework, and 35% personal" (p.26).
47. **Claude.ai vs 1P API across primitives — the platform comparison.** "API usage is overwhelmingly work-related (74% vs. 46%) and directive (64% vs. 32%), with three-quarters of interactions classified as automation compared to less than half on Claude.ai" (p.26). "tasks tend to be more lengthy—both in terms of human time with AI (15 minutes vs. 5 minutes) and the estimated time a human would need to complete the task alone (3.1 hours vs. 1.7 hours). Claude.ai also shows higher task success rates (67% vs. 49%), which may reflect the benefits of multi-turn conversation… Claude.ai users also give the AI more autonomy on average, and are more likely to bring tasks they couldn't complete alone" (pp.26–27).
48. **Claude.ai vs 1P API across occupations.** "API usage is heavily concentrated in Computer & Mathematical tasks (52% vs. 36%)… Office & Administrative tasks are also more prevalent in the API (15% vs. 8%)… Claude.ai, by contrast, sees substantially more Educational Instruction tasks (16% vs. 4%)—coursework help, tutoring, and instructional material development—as well as more Arts, Design, and Entertainment tasks (11% vs. 6%). Claude.ai also has a longer tail of human-facing categories like Community & Social Service and Healthcare Practitioners" (p.27).
49. **The structural reason API records look different.** "Claude.ai transcripts can include multi-turn conversations, while the API data we analyze is limited to single input-output pairs. This is because API requests arrive independently, with no metadata linking them to prior exchanges. This means we can only analyze them as isolated user-assistant pairs rather than full conversation trajectories" (p.26).
50. **The external validation of the human-education primitive.** Figure 2.1 (p.24) plots Claude's average years-of-schooling estimate for an occupation's tasks against the BLS share of workers in that occupation with a bachelor's degree or higher; the figure inset gives **N = 576, R² = 0.282, Slope = 8.09** (figure inset). Education data are from "Educational attainment for workers 25 years and older by detailed occupation" (BLS), "based on microdata from the 2022 and 2023 American Community Survey" (Fig 2.1 caption, p.24).
51. **The time-estimate primitives were validated elsewhere, not here.** "In our productivity work, Claude's time estimates correlate with actual time spent on software engineering tasks" (p.23); "For classifying task duration with and without AI, we used minimally modified versions of our prior productivity work" (p.22). No correlation statistic for the time estimates is reported in this report.
52. **Chain-of-thought prompting was kept for exactly three facets.** "We then compared performance of classifier versions with vs. without chain of thought prompting, and decided to keep chain of thought prompting only for three facets (human time estimate, human with AI time estimate, and AI autonomy) where we found that it substantially improved performance" (p.22). The appendix confirms this: the Claude.ai and 1P API prompts for AI Autonomy, Human-Only Time and Human-with-AI Time all carry `<thinking>` blocks, whereas the six shared prompts (multitasking, human ability, use case, task success, human education, AI education) do not (Online Appendix §2.1–2.3, pp.12–18).
53. **A simple classifier beat a complex one for task success.** "we find that in some instances (e.g., to measure task success), a simple classifier performed better than a nuanced, complex classifier when compared to human ratings" (p.22).

### Chapter 3 — geographic variation in how Claude is used

54. **The GDP elasticity of adoption.** "A 1% increase in GDP per capita is associated with a 0.7% increase in Claude usage per capita at the country level" (pp.28, 31). The country panel in Figure 3.3 gives **r = 0.869, R² = 0.755, p < 0.001, β = 0.70** (p.31, figure inset). The US state panel in Figure 3.4 gives **r = 0.750, R² = 0.563, p < 0.001, β = 1.77** (p.32, figure inset) — a markedly steeper slope within the US than across countries.
55. **AUI against the five core primitives, country level** (Fig 3.3, p.31, figure insets; dependent variable is ln AUI, sample restricted to countries with ≥200 observations):
    - Human only time (hours): r = −0.561, R² = 0.315, p < 0.001, β = −0.97
    - Human education (years): r = 0.359, R² = 0.129, p < 0.001, β = 0.75
    - AI autonomy (1–5): r = −0.801, R² = 0.642, p < 0.001, β = −8.10
    - Work use case (%): r = 0.164, R² = 0.027, p = 0.079, β = 0.03
    - Task success (%): r = 0.140, R² = 0.020, p = 0.134, β = 0.05
56. **AUI against the five core primitives, US state level** (Fig 3.4, p.32, figure insets; ≥100 observations per state):
    - Human only time (hours): r = −0.115, R² = 0.013, p = 0.428, β = −0.23
    - Human education (years): r = 0.680, R² = 0.463, p < 0.001, β = 1.25
    - AI autonomy (1–5): r = −0.247, R² = 0.061, p = 0.084, β = −2.65
    - Work use case (%): r = 0.481, R² = 0.231, p < 0.001, β = 0.07
    - Task success (%): r = 0.243, R² = 0.059, p = 0.088, β = 0.06
57. **The level-dependence, stated plainly.** "at the country level, the AUI correlates negatively with the time it would take a human to complete a task without AI, and with how much decision-making autonomy AI is given. At the US state level, these relationships are not statistically significant–likely also due to the smaller sample size for US states. Additionally, we observe a positive correlation between the AUI and Claude.ai use for work at the US state, but not at the country level" (p.32).
58. **Use case against income across countries** (Fig 3.2, p.30, figure insets; x-axis is GDP per working-age capita, log scale):
    - Work (%): r = 0.142, R² = 0.020, p = 0.131, β = 0.74
    - Coursework (%): r = −0.542, R² = 0.293, p < 0.001, β = −4.24
    - Personal (%): r = 0.681, R² = 0.463, p < 0.001, β = 3.49
    Reading: "work use cases and personal use cases of Claude are more common in higher income countries, while coursework use cases are more common in lower income countries" (p.29). Note that the work-use relationship is not statistically significant at conventional levels, while the headline in the introduction (p.3) is stated without that qualification.
59. **Named geographic extremes on use case.** "At the global level, the Balkans and Brazil have the highest relative share of work use (see Figure 3.1), and Indonesia stands out with the highest share of coursework. At the US state level, New York stands out as the state using Claude relatively the most for work" (p.29).
60. **Convergence with an outside source.** "these findings converge with recent work by Microsoft showing that AI use for school is associated with lower per capita income, whereas AI use for leisure is associated with higher per capita income" (p.29).
61. **Task success vs human education, the sign flip** (Fig 3.5, p.34, figure insets):
    - Countries, bivariate: r = −0.295, R² = 0.087, p = 0.001, β = −1.63
    - Countries, partial (controlling for GDP per capita, AI autonomy, automation percent, work and coursework shares, human-without-AI time, human-with-AI time, multitasking and human ability): partial r = −0.341, partial R² = 0.116, p < 0.001, partial β = −2.334
    - US states, bivariate: r = 0.317, R² = 0.100, p = 0.025, β = 2.30
    - US states, partial: partial r = 0.064, partial R² = 0.004, p = 0.656, partial β = 0.768
    Reading: "task success is negatively associated with human education at the country level, but positively related at the US state level. However, the positive relationship at the state level becomes insignificant when controlling for other primitives… This means the relationship pattern at one level of observation (country) contradicts the relationship pattern at another level (US state)" (p.33).
62. **The near-perfect human/AI education correlation.** "We find a very high correlation between human and AI education, i.e. the number of years of education required to understand a human prompt or the AI's response (countries: r = 0.925, p < 0.001, N = 117; US states: r = 0.928, p < 0.001, N = 50)" (p.34). Note the state N of 50: 50 states plus DC minus Wyoming.
63. **The state-level education association is not robust.** "at the US state level, human education years show a strong association with the Anthropic AI Usage Index in isolation, but this relationship disappears once we control for GDP and other primitives—suggesting education may be capturing variation that's better explained by economic development and other factors" (pp.32–33).
64. **Income, usage and augmentation.** "Higher per capita usage countries, which tend to be higher per capita income countries, show lower automation, and less decision-making autonomy delegated to Claude. That is, higher income countries use AI more as an assistant and collaborator rather than letting it work independently. This relationship is not significant at the US state level, perhaps because income variation and use case diversity are more limited within the United States than globally. This mirrors a finding from our 3rd Economic Index report" (p.35).

### Chapter 4 — tasks and productivity

65. **The speedup–complexity gradient.** "in Claude.ai conversations, for example, prompts requiring 12 years of schooling (a high school education) enjoy a speedup of 9x, while those requiring 16 years of schooling (a college degree) attain a 12x speedup. This implies that productivity gains are more pronounced for use cases requiring higher human capital" (pp.38–39, Fig 4.1 panel a). Comparison: binned scatter at the O\*NET task level, split by platform.
66. **The API speedup is uniformly higher.** "Throughout the range of task complexity, the speedup is higher for API users. This could reflect the nature of the API data, which is restricted to single-turn interactions, and that API tasks have been specifically selected for automation" (p.39, Fig 4.1).
67. **The countervailing success gradient.** "On Claude.ai, for example, tasks requiring less than a high school education (e.g., answering basic questions about products) attain a 70% success rate, but this drops to 66% for college-level conversations like developing analysis plans" (p.39, Fig 4.1 panel b).
68. **The gradient survives the adjustment.** "accounting for the difference in success rates—by either excluding low-success tasks or discounting speedups by success probability—does not eliminate the education gradient: complex tasks still show greater net productivity gains" (p.39).
69. **Automation share does not vary with the education of the prompt — a null.** "the automation share is essentially unrelated to the human levels of education required to write the prompt (Appendix Figure A.1). On both Claude.ai and 1P API, tasks across education levels show automation patterns in roughly equal shares" (p.40). The referenced figure is Online Appendix Figure 1 (appendix p.2); no regression statistic is reported for it in either document.
70. **Autonomy rises slightly with complexity on Claude.ai but not on the API.** "Claude.ai users give the AI slightly more autonomy when working on more complex tasks. In contrast, API usage shows uniformly lower autonomy at all levels of complexity" (p.40). The figure inset gives Claude.ai r² = 0.026 and 1P API r² = 0.000 (Fig 4.2, p.40, figure inset) — that is, the Claude.ai gradient explains under 3% of the between-bin variance and the API gradient explains none.
71. **The task-horizon result for the API.** "In the API data, success rates drop from around 60% for sub-hour tasks to roughly 45% for tasks estimated to take humans 5+ hours. The fitted line crosses the horizontal 50% success line at 3.5 hours, suggesting that API calls attain a 50% success rate for tasks that are 3.5 hours" (pp.41–42, Fig 4.3; the figure legend gives n = 727 for 1P API).
72. **The task-horizon result for Claude.ai.** "Claude.ai data tells a different story. Success rates decline far slower as a function of task length. Extrapolating using the linear fit, Claude.ai would hit a 50% success rate at about 19 hours. This may reflect how multi-turn conversation effectively breaks complex tasks into smaller steps, with each turn providing a feedback loop that allows users to correct course" (p.42, Fig 4.3; n = 951 for Claude.ai). The 19-hour figure is an extrapolation beyond the plotted range, whose x-axis tops out at 8 hours.
73. **The METR comparison.** "The analogous time estimate in METR's software engineering benchmark is 2 hours for Sonnet 4.5 and about 5 hours for Opus 4.5. (The data in this report predates the release of Opus 4.5.)" (p.42). METR's operationalisation is quoted at p.41: "METR operationalizes task horizon primarily as the maximum duration at which a model achieves at least 50% success."
74. **Task coverage has risen across the series.** "Our earlier work found that 36% of jobs had AI usage for at least a quarter of their tasks, with about 4% reaching 75% task coverage… First, we find that task coverage is increasing. Combining across reports, 49% of jobs have seen AI usage for at least a quarter of their tasks" (p.43). Comparison: first-report coverage vs coverage pooled across all four reports. Note the denominators differ — 49% pools across reports, 36% did not.
75. **High task coverage overstates job impact.** "On the right side of the plot, occupations with high coverage—where almost all tasks appear with some frequency in Claude data—generally fall below the 45-degree line. This suggests that even 90% task coverage does not necessarily indicate large job impacts, since Claude may fail on key covered tasks or miss the most time-intensive ones" (p.43, Fig 4.4).
76. **Occupations that gain from the effective-coverage adjustment.** "data entry workers have one of the highest effective AI coverage. This is because although only two of their nine tasks are covered, their largest task—reading and entering data from source documents—has high success rates with Claude" (p.44). "Medical transcriptionists and radiologists also move up because their covered tasks happen to be their most time-intensive and highest-frequency work. For radiologists, their top two tasks—interpreting diagnostic images and preparing interpretive reports—have high success rates. These occupations have low task coverage because AI can't do the hands-on or administrative work in their job profiles, but it succeeds on the core knowledge work that dominates their workday" (pp.44–45). Figure 4.4 highlights and labels: Data Entry Keyers, Medical Transcriptionists, Radiologists, Clergy, Microbiologists, Psychology Teachers Postsecondary, Database Architects, Software Developers Applications (p.44).
77. **The occupation that loses from the adjustment.** "Microbiologists fall below the 45-degree line, suggesting lower effective AI coverage than would be predicted by task coverage alone. Claude covers half of their tasks, but not their most time-intensive: hands-on research using specialized lab equipment" (p.45).
78. **The task-education model and a worked example.** "O\*NET doesn't provide task-level education requirements, so we train a model that predicts years of schooling from task embeddings, using the BLS's occupation-level education as the target… For example, Legal Secretaries is a 12-year education occupation, but the task 'Review legal publications and perform database searches to identify laws and court decisions relevant to pending cases' is predicted to require 17.7 years because it resembles tasks typically performed by lawyers and paralegals" (pp.45–46).
79. **Claude covers higher-education tasks than the economy average.** "The mean predicted education for tasks in the economy is 13.2 years. For tasks that we see in our data, the mean prediction is about a year higher, 14.4 years (corresponding to an Associate's degree)" (p.46). The figure legend gives the sample sizes: all tasks n = 18,429, Claude-covered tasks n = 3,169 (Fig 4.5, p.46, figure inset); both distributions are employment-weighted.
80. **The net effect of task removal is deskilling.** "Overall, the net first-order impact is to deskill jobs, since AI removes tasks that require relatively higher levels of education" (p.46). Worked examples: technical writers lose "Analyze developments in specific field to determine need for revisions" (18.7 years) and "Review published materials and recommend revisions or changes in scope, format" (16.4 years), keeping "Draw sketches to illustrate specified materials" (13.6 years) and "Observe production, developmental, and experimental activities" (13.5 years) (pp.46–47). Travel agents lose "Plan, describe, arrange, and sell itinerary tour packages" (13.5 years) and "Compute cost of travel and accommodations" (13.4 years), keeping "Print or request transportation carrier tickets" (12.0 years) and "Collect payment for transportation and accommodations" (11.5 years) (p.47).
81. **The upskilling counter-example.** "Real estate managers experience upskilling because AI covers routine administrative tasks—maintaining sales records (12.8 years), reviewing rents against market rates (12.6 years)—while tasks requiring higher-level professional judgment and in-person interaction remain, like securing loans, negotiating with architecture firms, and meeting with boards" (p.47). The introduction (p.4) calls the same occupation "Property managers"; chapter 4 calls it "Real estate managers".
82. **Teaching professions are deskilled.** "Several teaching professions experience deskilling because AI addresses tasks like grading, advising students, writing grants, and conducting research without being able to do the hands-on work of delivering lectures in person and managing a classroom" (p.47).
83. **The 1.8pp productivity estimate is replicated on the new, larger sample.** "Based on the speedups associated with tasks with at least 200 observations in our sample of 1M Claude.ai conversations, we replicate our previous finding that current-generation AI models and current usage patterns imply a productivity effect of 1.8 percentage points per year over the next decade" (p.48). Comparison: 1M Nov-2025 sample vs the 100k Fall-2025 sample of the earlier productivity paper.
84. **The API sample implies the same number, for offsetting reasons.** "Two countervailing forces are at play: API usage is more concentrated in a narrower set of tasks and occupations (particularly coding-related work), which would tend to reduce implied effects; but task-level speedups are higher on average among API tasks… These forces largely offset: the API sample likewise implies a 1.8 percentage point increase in labor productivity over the next decade" (p.48).
85. **The reliability adjustment — the chapter's headline revision.** "implied productivity growth falls from 1.8 to 1.2 percentage points per year for the next decade based on Claude.ai usage, and to 1.0 percentage points for API traffic. Yet, even after accounting for reliability, the implied impact remains economically significant—a sustained increase of 1.0 percentage point per year for the next ten years would return US productivity growth to rates that prevailed in the late 1990s and early 2000s" (p.48). **Internal tension (wiki author's flag):** the chapter's own opening summary says "Adjusting productivity estimates for task reliability roughly halves the implied gains, from 1.8 to about 1.0 percentage points of annual labor productivity growth over the next decade" (p.38). The body gives 1.2pp for Claude.ai and 1.0pp for API; "about 1.0" and "roughly halves" describe the API figure, not the Claude.ai one. Anyone quoting a single success-adjusted number must say which platform it is.
86. **The CES complementarity exercise.** At σ = 1 the model reproduces the baseline: "An increase in labor productivity growth of ~1.8 percentage points per year over the next decade implied by both Claude.ai and API samples" (p.49). "at σ = 0.5 the implied overall labor productivity effect is 0.7–0.9 percentage points per year—around half the size as implied by our baseline estimates. Additionally adjusting for task success further reduces the implied productivity effects to 0.8pp for Claude.ai and 0.6pp for API" (p.50). "at σ = 1.5 the implied labor productivity effect rises to 2.2–2.6 percentage points per year, consistent with greater specialization in tasks where AI provides the largest speedups" (pp.50–51).
87. **The API is more sensitive to the substitution parameter.** "In both cases the implied productivity impact based on API traffic is more responsive to the degree of task substitutability. This is consistent with the fact that there is a larger share of API traffic concentrated in fewer tasks and associated occupations as compared to Claude.ai: When tasks are complements, this concentration amplifies the bottleneck problem; when they are substitutes, it amplifies productivity gains from task specialization" (p.51).
88. **The threshold choice drives the headline number, and the report says so.** "We choose a threshold of 0.02% because it replicates our previous results for our sample of Claude.ai conversations… If we do not impose a restriction on our 1M sample and assume that efficiency gains for any task in our sample, even those with just 15 observations out of one million, the implied aggregate labor productivity growth over the next decade would be roughly 5% percentage points per year—a mechanical increase based on a the much larger set of tasks included" (fn6, pp.52–53). That is, the reported 1.8pp is a threshold-dependent number and the unrestricted alternative is roughly 2.8x larger. (The phrase "roughly 5% percentage points" appears exactly so in the source; the "%" appears to be a typographical error for "percentage points per year".)
89. **The aggregation theorem.** "this result is based on applying Hulten's Theorem to task-level productivity shocks and assuming that the corresponding one-time increase in total factor productivity materializes over the course of a decade alongside capital deepening effects" (fn7, p.53).
90. **Attribution of the complementarity exercise.** "We thank Pascual Restrepo for suggesting this particular exercise" (fn9, p.53).

### Sampling, privacy and measurement claims that carry numbers

91. **Sample sizes and window.** "Throughout the report we analyze a random sample of 1M conversations from Claude.ai Free, Pro and Max conversations… and 1M transcripts from our first-party (1P) API traffic… Both samples come from November 13, 2025 to November 20, 2025" (fn1, p.17). Figure 2.2 reports the realised Claude.ai N as 999,875 (p.25), i.e. slightly under 1M after exclusions.
92. **Privacy thresholds.** "our automated analysis system filters out any cells—e.g., countries, and (country, task) intersections—with fewer than 15 conversations and 5 unique user accounts. For bottom-up request clusters, we have an even higher privacy filter of at least 500 conversations and 250 unique accounts" (fn1, p.36).
93. **Figure-level inclusion thresholds.** Countries need ≥200 observations and US states ≥100 observations in the geographic figures (Figs 3.1–3.5 captions, pp.29–34). "When we study the correlation between primitives with the O\*NET, we restrict to tasks appearing in at least 100 conversations to reduce measurement error. In the coverage analysis, we use all tasks above the privacy threshold of 15" (fn1, p.52). The productivity aggregation uses tasks with "at least 200 observations" (p.48).
94. **The classifier model changed between waves.** "In this report we use Sonnet 4.5 for classification whereas in our previous Economic Index report we used Sonnet 4. We previously found that different models can generate different classification outcomes, though these effects tend to be modest" (fn7, p.18). This is a confound on every Aug-2025 → Nov-2025 comparison in Chapter 1.
95. **Binned scatterplots throughout.** "Throughout this report, we use binned scatterplots to show bivariate relationships. We divide observations into 20 equally-sized bins based on the x variable, then plot the average x and y values for each bin. The leftmost dot, for example, represents the averages for observations in the lowest 5% of the x distribution" (fn2, p.27). Every correlation and R² quoted from Figures 3.2–3.5 and 4.1–4.3 is therefore a **between-bin** statistic, not a conversation-level one.
96. **Geolocation method and exclusions.** "Aggregate geographic statistics at the country and US state level were assessed and tabulated from the IP address of each conversation… We exclude conversations originating from VPN, anycast, or hosting services, as determined by our IP geolocation provider" (fn2, p.36). "US state level data use ISO-3166-2 region codes, which include all 50 US states and Washington DC" (fn2, p.36).
97. **Trust-and-safety exclusion.** "We then excluded content that was flagged as potential trust and safety violations" (fn2, p.36).
98. **Unit of observation.** "The unit of observation is a conversation with Claude on Claude.ai, not a user, so it is possible that multiple conversations from the same user are included, though our past work suggests that sampling conversations at random versus stratified by user does not yield substantively different results" (fn2, p.36).
99. **AUI denominator source and its gaps.** "the Anthropic AI Usage Index is calculated per working-age capita based on working age population data from the World Bank, and population data is not readily available for all of these territories, we cannot calculate the AUI for these territories" (fn4, p.37).
100. **Map conventions.** "The world map is based on Natural Earth's world map with the ISO standard point of view for disputed territories… we do not operate in the Ukrainian regions Crimea, Donetsk, Kherson, Luhansk, and Zaporizhzhia" (fn3, p.37).

### The online appendix

101. **Contents.** The online appendix contains two sections: "1 Supplementary Figures" (10 figures, pp.2–11) and "2 Prompts for Claude.ai and 1P API facets" (pp.12–18), the latter split into "2.1 Claude.ai and 1P API shared prompts" (6 prompts), "2.2 Claude.ai prompts" (4 prompts) and "2.3 1P API prompts" (4 prompts) — 14 prompt texts in all, covering the nine new primitive classifiers plus the collaboration-pattern classifier, in platform-specific variants where they differ.
102. **Appendix Figure 1 is the "Appendix Figure A.1" referenced on p.40.** "Automation share vs. Human education years, split by platform. This figure shows a binned scatterplot of the bivariate relationship between the share of automation and years of formal education needed to understand the User prompts, all measured at the O\*NET task level and split by platform" (appendix p.2). No fit statistic is printed in the caption.
103. **Appendix Figures 2–7 are the geographic league tables.** Figure 2 "Leading countries in terms of global Claude.ai usage share"; Figure 3 "Leading countries in terms of Claude.ai adoption per capita… the top 30 countries based on the Anthropic AI Usage Index"; Figure 4 "Countries by Claude.ai adoption per capita… Anthropic AI Usage Index for all countries"; Figure 5 "Leading US states in terms of Claude.ai usage share"; Figure 6 "Leading US states by Claude.ai adoption per capita… the top 30 US states"; Figure 7 "US states by Claude.ai adoption per capita… for all US states" (appendix pp.3–8). Figures 3, 4, 6 and 7 carry the same ≥200-country / ≥100-state observation thresholds as the main text.
104. **Appendix Figures 8 and 9 are the partial regressions behind the Chapter 3 controls.** "Partial regression of the Anthropic AI Usage Index on five core economic primitives and GDP per capita at the country level" (appendix p.9) and "…at the US state level" (appendix p.10), "controlling for other core primitives". These are the figures behind the claim at p.32–33 that the state-level human-education association disappears under controls.
105. **Appendix Figure 10 relates automation and autonomy to income directly.** "Relationship between automation share or AI autonomy and GDP per working-age capita. Each plot shows the relationship between automation share (left panels) or AI autonomy (right panels) and log GDP per working-age capita" (appendix p.11). This is the figure behind the Chapter 3 claim that higher-income countries show lower automation and lower autonomy.
106. **The collaboration-pattern classifier instructs liberal use of 'None'.** "If you are unsure or there is not enough context to determine the most representative pattern, return 'None' as your answer. Use 'None' liberally---for only some conversations will this task be possible" (appendix pp.15–16 and 18). This is the mechanism behind the 3.0% residual reported at fn2, p.17.
107. **The 1P API prompts carry an explicit reframing instruction the Claude.ai prompts do not.** "IMPORTANT: These interactions are happening via an LLM API, not an actual human-AI assistant conversation. Consider what is implied by the context in which the API is being used. We're interested in how an end user is interacting with the AI-driven feature or service, NOT how the developer is prompting the API… For the purposes of this task, when we say 'human', we mean 'end user'" (appendix p.19, §2.3.4). Shorter versions of the same warning appear in the API autonomy, human-only time and human-with-AI time prompts (appendix pp.17–18). Every cross-platform comparison in the report therefore compares outputs of prompts that are not identical.

---

## Definitions (verbatim)

All quotations in this section are verbatim from the fetched documents. No paraphrase, no interpretation.

### The primitives programme

> "we expand the breadth of data available to external researchers by providing insights on five economic 'primitives', by which we mean simple, foundational measures of the ways that Claude is used, which we generate by asking Claude to answer specific questions about the anonymized transcripts in our sample. Some of our primitives encompass several such questions, and others use a single indicator." — p.19

> "These 'primitives'—simple, foundational measures of how Claude is used, which we generate by asking Claude specific questions about anonymized Claude.ai and first-party (1P) API transcripts—cover five dimensions relevant to AI's economic impact: user and AI skills, how complex tasks are, the degree of autonomy afforded to Claude, how successful Claude is, and whether Claude is used for personal, educational, or work purposes." — p.2

> "A classifier is a model that assigns a given input (e.g., a user conversation) a specific output (e.g., the use case 'work'). In this report, we use Claude as a classifier, meaning that we prompt Claude to select a specific output and then use Claude's response as the output (see Table 2.1 for the prompts)." — fn1, p.27

### Task complexity (the primitive category)

> "**Task complexity** captures that tasks can vary in their complexity, including how long they take to complete and how difficult they are. A 'debugging' task in O\*NET could refer to Claude fixing a small error in a function or comprehensively refactoring a codebase—with very different implications for labor demand. We measure complexity through estimated human time to complete tasks without AI, time spent completing tasks with AI, and whether users handle multiple tasks within a single conversation." — p.21

#### Human time estimate (human-only time)

Table 2.1 operationalisation, p.20:

> "Estimate how many hours a competent professional would need to complete the tasks done by the Assistant.
> Assume they have:
> • The necessary domain knowledge and skills
> • All relevant context and background information
> • Access to required tools and resources
> • No access to AI tools to assist with the work"

Full Claude.ai prompt, Online Appendix §2.2.2, appendix p.14:

> "Human: Consider the following conversation:
>
> \<conversation\>
> {TRANSCRIPT}
> \</conversation\>
>
> Estimate how many hours a competent professional would need to complete the tasks done by the Assistant.
>
> Assume they have:
> - The necessary domain knowledge and skills
> - All relevant context and background information
> - Access to required tools and resources
> - No access to AI tools to assist with the work
>
> Before providing your final answer, use \<thinking\> tags to break down your reasoning process:
> \<thinking\>
> 2-5 sentences of reasoning estimating how many hours would be needed to complete the tasks.
> \</thinking\>
>
> Provide your output in the following format:
> \<answer\>A number representing hours (can use decimals like 0.5 for shorter tasks)\</answer\>
>
> Assistant: \<thinking\>"

The 1P API variant (Online Appendix §2.3.2, appendix p.17) is identical except that "Consider the following conversation:" becomes "Consider the following API call." with `<api_call>` tags, and the following sentence is inserted before the thinking block:

> "IMPORTANT: These interactions are happening via an LLM API, not an actual User-Assistant conversation."

#### Human with AI time estimate

Table 2.1 operationalisation, p.20:

> "Estimate how many minutes the User spent completing the tasks in the prompt with the Assistant.
> Consider:
> • Number and complexity of User messages
> • Time reading Assistant's responses
> • Time thinking and formulating questions
> • Time reviewing outputs and iterating
> • Realistic typing/reading speeds
> • Time implementing suggestions or running code outside of the conversation (only if directly relevant to the tasks)"

Full Claude.ai prompt, Online Appendix §2.2.3, appendix p.15:

> "Human: Consider the following conversation:
>
> \<conversation\>
> {TRANSCRIPT}
> \</conversation\>
>
> Estimate how many minutes the User spent completing the tasks in the prompt with the Assistant.
>
> Consider:
> - Number and complexity of User messages
> - Time reading Assistant's responses
> - Time thinking and formulating questions
> - Time reviewing outputs and iterating
> - Realistic typing/reading speeds
> - Time implementing suggestions or running code outside of the conversation (only if directly relevant to the tasks)
>
> Before providing your final answer, use \<thinking\> tags to break down your reasoning process:
> \<thinking\>
> 2-5 sentences of reasoning about how many minutes the User spent.
> \</thinking\>
>
> Provide your output in the following format:
> \<answer\>A number representing minutes\</answer\>
>
> Assistant: \<thinking\>"

The 1P API variant (Online Appendix §2.3.3, appendix p.18) adds the same IMPORTANT sentence and uses `<api_call>` tags.

#### Multitasking

Table 2.1 operationalisation, p.20:

> "Did the User multitask in this conversation? Choose from these options:
> • Yes: the User was working on multiple tasks over the course of the conversation
> • No: the User was working on a single task over the course of the conversation"

Full prompt, shared across platforms, Online Appendix §2.1.1, appendix p.12:

> "Did the User multitask in this conversation? Choose from these options:
>
> - Yes: the User was working on multiple tasks over the course of the conversation
> - No: the User was working on a single task over the course of the conversation
>
> Your classification should be exactly one of the answer options, nothing else, provided in \<answer\> tags. For example, your answer could be \<answer\>Yes\</answer\> or \<answer\>No\</answer\>."

### Human and AI skills (the primitive category)

> "**Human and AI skills** address how automation interacts with skill levels. If AI disproportionately substitutes for tasks requiring less expertise while complementing higher-skilled work, it could be another form of skill-biased technical change—increasing demand for highly skilled workers while displacing lower skilled workers. We measure whether users could have completed tasks without Claude, and the years of education needed to understand both user prompts and Claude's responses." — p.21

#### Human ability to complete task alone (human-only ability)

Table 2.1 operationalisation, p.20:

> "Could the User have completed this task by themselves? Choose from these options:
> • Yes: the User would have been able to complete the task without the Assistant, even if it would have taken more time
> • No: the User would not have been able to complete the task without the Assistant, even with more time"

Full prompt, shared, Online Appendix §2.1.2, appendix p.12:

> "Could the User have completed this task by themselves? Choose from these options:
>
> - Yes: the User would have been able to complete the task without the Assistant, even if it would have taken more time
> - No: the User would not have been able to complete the task without the Assistant, even with more time
>
> Your classification should be exactly one of the answer options, nothing else, provided in \<answer\> tags. For example, your answer could be \<answer\>Yes\</answer\> or \<answer\>No\</answer\>."

#### Human education years

Table 2.1 operationalisation, p.20:

> "Estimate how many years of formal education someone would need to understand the User prompts in this conversation. Your answer should be a single number out of the discrete numbers ranging from 0-20."

Full prompt, shared, Online Appendix §2.1.5, appendix p.13:

> "Estimate how many years of formal education someone would need to understand the User prompts in this conversation. Your answer should be a single number out of the discrete numbers ranging from 0-20.
>
> Your classification should be exactly one of the answer options, nothing else, provided in \<answer\> tags. For example, your answer could be \<answer\>0\</answer\> or \<answer\>20\</answer\>."

The report also glosses it in running text:

> "Human education—Claude's estimate of years of formal education needed to understand the human prompt" — p.28

> "Human education (how many years of education it takes to understand the human written prompts in a conversation)" — p.31

> "our core measure of task complexity, the human years of schooling required to understand the inputs" — p.38

#### AI education years

Table 2.1 operationalisation, p.20:

> "Estimate how many years of formal education someone would need to understand the Assistant responses in this conversation. Your answer should be a single number out of the discrete numbers ranging from 0-20."

Full prompt, shared, Online Appendix §2.1.6, appendix p.13:

> "Estimate how many years of formal education someone would need to understand the Assistant responses in this conversation. Your answer should be a single number out of the discrete numbers ranging from 0-20.
>
> Your classification should be exactly one of the answer options, nothing else, provided in \<answer\> tags. For example, your answer could be \<answer\>0\</answer\> or \<answer\>20\</answer\>."

### Use case (work vs coursework vs personal)

> "**Use case** distinguishes professional, educational, and personal use. Labor market effects most directly follow from workplace use, while educational use may signal where the future workforce is building AI-complementary skills." — p.21

Table 2.1 operationalisation, p.20:

> "Analyze whether the conversation between the User and the Assistant primarily focuses on work, coursework or personal use. Analyze the use case according to these categories:
> • Work: professional use to accomplish tasks that are part of the User's job
> • Coursework: use to help the User complete coursework in educational contexts
> • Personal: use for any domain that is not work or coursework"

Full prompt, shared, Online Appendix §2.1.3, appendix p.12:

> "Analyze whether the conversation between the User and the Assistant primarily focuses on work, coursework or personal use. Analyze the use case according to these categories:
>
> - Work: professional use to accomplish tasks that are part of the User's job
> - Coursework: use to help the User complete coursework in educational contexts
> - Personal: use for any domain that is not work or coursework
>
> Your classification should be exactly one of the answer options, nothing else. For example, your answer could be \<answer\>Work\</answer\> or \<answer\>Coursework\</answer\> or \<answer\>Personal\</answer\>."

### AI autonomy

> "**AI autonomy** measures the degree to which users delegate decision-making to Claude. Our latest report documented rising 'directive' use where users delegate tasks entirely. Tracking autonomy levels—from active collaboration to full delegation—helps forecast the pace of automation." — p.21

> "AI autonomy captures something different from our existing automation/augmentation distinction. For example, 'Translate this paragraph into French' is high automation (directive, minimal back-and-forth) but low AI autonomy (the task requires little decision-making from Claude)." — p.19

Table 2.1 operationalisation, p.20:

> "Estimate how much autonomy the Assistant had to make decisions in this conversation (a discrete number ranging from 1-5, where 1 is none and 5 is extreme)."

Full Claude.ai prompt, Online Appendix §2.2.1, appendix pp.13–14:

> "Human: Consider the following conversation:
>
> \<conversation\>
> {TRANSCRIPT}
> \</conversation\>
>
> Estimate how much autonomy the Assistant had to make decisions in this conversation (a discrete number ranging from 1-5, where 1 is none and 5 is extreme).
>
> Before providing your final answer, use \<thinking\> tags to break down your reasoning process:
> \<thinking\>
> 2-5 sentences of reasoning estimating how much autonomy the Assistant had to make decisions in this conversation.
> \</thinking\>
>
> Provide your output in the following format:
> \<answer\>A discrete number representing the level of autonomy the Assistant had to make decisions (ranging from 1-5, where 1 is none and 5 is extreme)\</answer\>
>
> Assistant: \<thinking\>"

The 1P API variant (Online Appendix §2.3.1, appendix pp.16–17) uses `<api_call>` tags and inserts:

> "IMPORTANT: These interactions are happening via an LLM API, not an actual User-Assistant conversation. We are interested in the dynamics between the human User and the Assistant."

### Task success

> "**Task success** measures Claude's assessment of whether Claude completes tasks successfully. Task success helps assess whether tasks can be automated effectively (can a task be automated at all?) and efficiently (how many attempts would it take to automate a task?). That is, task success matters for both the feasibility and the cost of automation labor tasks." — p.21

Table 2.1 operationalisation, p.20:

> "Did the Assistant complete the task provided by the User successfully? Choose from these options:
> • Yes: the Assistant completed the task provided by the User successfully
> • No: the Assistant did not complete the task provided by the User successfully"

Full prompt, shared, Online Appendix §2.1.4, appendix p.13:

> "Did the Assistant complete the task provided by the User successfully? Choose from these options:
>
> - Yes: the Assistant completed the task provided by the User successfully
> - No: the Assistant did not complete the task provided by the User successfully
>
> Your classification should be exactly one of the answer options, nothing else, provided in \<answer\> tags. For example, your answer could be \<answer\>Yes\</answer\> or \<answer\>No\</answer\>."

### Automation and augmentation (the prior, sixth primitive)

> "At a high level, we distinguish between automation and augmentation modes of using Claude. Automation encompasses interaction patterns focused on task completion: Directive: Users give Claude a task and it completes it with minimal back-and-forth; Feedback Loops: Users automate tasks and provide feedback to Claude as needed; Augmentation focuses on collaborative interaction patterns: Learning: Users ask Claude for information or explanations about various topics; Task Iteration: Users iterate on tasks collaboratively with Claude; Validation: Users ask Claude for feedback on their work." — fn5, p.18

> "These interaction modes are not mutually exhaustive. In some instances, Claude determines that a sampled conversation does not match any of the five interaction modes." — fn6, p.18

> "Automation = Directive + Feedback loop. Augmentation = Validation + Task iteration + Learning." — Fig 1.3 note, p.10

> "Directive conversations are those in which users give Claude a task and it completes it with minimal back-and-forth." — p.9

The collaboration-pattern classifier's own category definitions, Online Appendix §2.2.4, appendix pp.15–16:

> "- Directive - Human delegates complete task execution to AI with minimal interaction
> - Feedback Loop - Human and AI engage in iterative dialogue to complete task with human mainly providing feedback from the environment
> - Task Iteration - Human and AI engage in iterative dialogue to complete a task with the human refining the AI outputs
> - Learning - Human seeks understanding and explanation rather than direct task completion
> - Validation - Human uses AI to check or validate their own work"

> "Based on your analysis, identify which of the above is most representative of the user's response. If multiple patterns are present, select the one that is most appears most frequently. If you are unsure or there is not enough context to determine the most representative pattern, return 'None' as your answer. Use 'None' liberally---for only some conversations will this task be possible." — Online Appendix §2.2.4, appendix p.16

### Anthropic AI Usage Index (AUI)

> "In our previous report, we introduced the Anthropic AI Usage Index (AUI), a measure of whether Claude is over- or underrepresented in a given geography relative to the size of its working-age population. The AUI is defined as
>
> Anthropic AI Usage Index_c ≡ (Country c's share of Claude Usage) / (Country c's share of working-age population)
>
> An AUI above 1 indicates that a country uses Claude more intensively than its population alone would predict, while an AUI below 1 indicates lower-than-expected usage." — p.12

> "Globally, Claude usage per capita—as captured by the Anthropic AI Usage Index (AUI)" — p.6

### The state convergence model

> "We model diffusion as proportional convergence toward a common steady state of equalized usage per capita in which each state s has an AUI equal to 1:
>
> AUI_{s,t} = AUI^β_{s,t−1}, β ∈ (0,1)
>
> Under this model, the log deviation of AUI from steady state (AUI = 1) shrinks by a factor of [β] every three months, implying a half-life of ln(.5)/ln([β]) quarters." — p.15

> "This model of convergence motivates the following regression specification:
>
> ln AUI_{s,t} = α + β × ln AUI_{s,t−1} + ε_{s,t}" — p.15

### Speedup

> "Our estimates suggest that, in general, the more complex tasks in our data yield a greater time savings (or 'speedup') from AI. We derive this by having Claude estimate both how long a task would take a human working alone and the duration when human and AI work together, which we validated in previous work. Speedup is then the human-alone time divided by the human-with-AI time. So reducing a 1 hour task to 10 minutes would give a 6x speedup." — p.38

### Effective AI coverage

> "We define effective AI coverage as the percent of a worker's day that can be performed successfully by Claude. It's calculated as the weighted sum of task success rates, where each task's weight is its share of the worker's time adjusted by how frequently the task occurs. The success rate comes from our primitives, the hours estimate from our previous work on productivity effects, and the frequency estimate from O\*NET data, where surveyed workers indicate how often they perform the task." — p.43

> "Effective AI coverage tracks the share of a worker's time-weighted duties that AI could successfully perform, based on Claude.ai data. Task coverage is the share of tasks that appear in Claude.ai usage." — Fig 4.4 caption, p.44

### Task horizon

> "METR operationalizes task horizon primarily as the maximum duration at which a model achieves at least 50% success, and growth in this metric has become a key indicator of AI progress." — p.41

> "Controlled benchmarks like METR's measure the frontier of autonomous capability. Our real-world data can measure the *effective* task horizon, reflecting a mix of model capabilities and user behavior, and expanding beyond coding tasks." — p.42

### The task-level education model

> "O\*NET doesn't provide task-level education requirements, so we train a model that predicts years of schooling from task embeddings, using the BLS's occupation-level education as the target. This way, a low-education occupation may still have a high-skill task if it looks like those that tend to exist in high-education occupations." — p.45

> "We generate embeddings for each task statement using a pretrained sentence transformer (all-mpnet-base-v2) and predict education with Ridge regression." — fn4, p.52

### The CES aggregation

> "We use a CES (constant elasticity of substitution) production function to aggregate task-level time savings to economy-wide productivity impacts. The elasticity parameter σ governs how easily workers can substitute between tasks. When σ=1, we apply Hulten's theorem directly: the aggregate productivity gain equals the wage-share-weighted sum of log speedups across tasks. For σ≠1, we use a two-level aggregation: first, within each occupation, we compute an occupation-level speedup as a CES aggregate of task speedups weighted by time fractions, using ρ=(σ-1)/σ. Then we apply Hulten's theorem to these occupation-level speedups. When σ<1 (complements), productivity gains are bottlenecked by tasks with the smallest speedups. When σ>1 (substitutes), workers can specialize in tasks where AI provides the largest speedups, amplifying aggregate gains. For tasks without observed AI speedup data, we assume no productivity change." — fn9, p.53

> "The key parameter is the elasticity of substitution across tasks, σ. When the elasticity of substitution is less than one, tasks are complements and those tasks that are not sped up by AI become bottlenecks for broader productivity gains. Alternatively, when the elasticity of substitution is greater than one, then workers can allocate toward the more productive tasks—thereby amplifying the overall time savings at the occupational level. An elasticity of substitution equal to one is a special case that replicates the main analysis above." — p.49

### The binned scatterplot

> "Throughout this report, we use binned scatterplots to show bivariate relationships. We divide observations into 20 equally-sized bins based on the x variable, then plot the average x and y values for each bin. The leftmost dot, for example, represents the averages for observations in the lowest 5% of the x distribution." — fn2, p.27

### Consumer and enterprise data

> "we analyze a random sample of 1M conversations from Claude.ai Free, Pro and Max conversations (we also refer to this as 'consumer data' since it mostly represents consumer use) and 1M transcripts from our first-party (1P) API traffic (we also refer to this as 'enterprise data' since it mostly represents enterprise use)… For 1P API data, each record is a prompt-response pair from our sample period which in some instances is mid-session for multi-turn interactions." — fn1, p.17

---

## Data and methods

In the wiki author's words, with page references.

**Samples and window.** Two samples, both drawn from **13–20 November 2025** (fn1, p.17; fn2, p.36). One is a random sample of 1 million Claude.ai conversations drawn from the Free, Pro and Max tiers; the other is 1 million first-party API transcripts. The report labels the first "consumer data" and the second "enterprise data" while noting these are approximations of who is actually on each platform (fn1, p.17). After exclusions the realised Claude.ai N is 999,875 (Fig 2.2, p.25). The window sits deliberately before the release of Opus 4.5 (pp.2, 42), which matters for every capability claim in Chapter 4.

**Units of observation differ by platform.** On Claude.ai the unit is a conversation, which may be multi-turn; multiple conversations from the same user can appear (fn2, p.36). On the API the unit is a single prompt–response pair, which may be mid-session in a multi-turn interaction, because "API requests arrive independently, with no metadata linking them to prior exchanges" (p.26; fn1, p.17). The report is explicit that this structural asymmetry, not only user behaviour, drives part of the platform gap it reports.

**Exclusions.** Content flagged as a potential trust-and-safety violation is dropped (fn2, p.36). Conversations from VPN, anycast or hosting services are dropped, as determined by the IP geolocation provider (fn2, p.36). Seychelles is excluded from all geographic analyses and Wyoming from all US state analyses, in both cases because a large fraction of observed usage in the window was abusive traffic (fns 5–6, p.37). This last exclusion is why the state-level correlations report N = 50 (50 states plus DC, minus Wyoming) rather than 51.

**Geography.** Country and US state assignment is from the conversation's IP address, mapped to ISO-3166-1 and ISO-3166-2 codes respectively (fn2, p.36). The AUI denominator is World Bank working-age population; territories without World Bank working-age population data cannot be assigned an AUI and appear as "No data" (fn4, p.37). The world map uses Natural Earth boundaries with the ISO standard point of view for disputed territories, and the report records that Anthropic does not operate in five Russian-occupied Ukrainian regions (fn3, p.37).

**Classification.** Claude itself is the classifier (fn1, p.27). The classification model for this wave is **Sonnet 4.5**; the previous wave used Sonnet 4, and the report notes that "different models can generate different classification outcomes, though these effects tend to be modest" (fn7, p.18). Classifiers run through the privacy-preserving tooling described in Anthropic's Clio work (p.22). Nine new classifiers implement the five new primitives, plus the pre-existing collaboration-pattern classifier (p.22; Online Appendix §2, appendix pp.12–19).

**Prompts.** The full prompt texts are in the online appendix, not the report; Table 2.1 (p.20) carries abbreviated versions. Six prompts are shared verbatim across the two platforms (multitasking, human ability, use case, task success, human education, AI education); four — AI autonomy, human-only time, human-with-AI time and collaboration pattern — exist in separate Claude.ai and 1P API variants (appendix pp.12–19). The API variants substitute `<api_call>` for `<conversation>` and add explicit instructions about reading the API context, most extensively in the collaboration-pattern prompt (appendix p.19). All prompts constrain the output to `<answer>` tags with an enumerated or numeric range.

**Chain of thought.** Kept only where it substantially improved measured performance: human time estimate, human-with-AI time estimate and AI autonomy (p.22). This is verifiable in the appendix — those three prompts, and the collaboration-pattern prompt, carry `<thinking>` blocks; the six shared prompts do not.

**Classifier validation.** The report gives a process, not a metric table (p.22). Multiple candidate measures were designed for each concept; for Claude.ai they were compared against a human researcher's ratings "on a small set of transcripts in which users gave feedback to Claude.ai and for which we thus have permission to look at underlying transcripts"; for the 1P API they were checked against "a mix of internal and synthetic data". Classifiers that performed poorly were discarded or revised; a simple task-success classifier beat a more nuanced one. The report states only that the surviving nine are "directionally accurate", and reports **no** accuracy, agreement or kappa statistic anywhere in the report or the appendix. The only quantified validation is the external one in Figure 2.1 (N = 576, R² = 0.282, slope = 8.09, p.24), which validates the human-education primitive against BLS occupational educational attainment; the time-estimate primitives lean on validation done in the earlier productivity paper (pp.22, 23, 38), not repeated here.

**Thresholds.** Several distinct thresholds operate at once, and confusing them will produce wrong replications:
- *Privacy floor:* cells with fewer than 15 conversations and 5 unique accounts are suppressed; bottom-up request clusters need at least 500 conversations and 250 unique accounts (fn1, p.36).
- *Geographic figures:* countries need ≥200 observations; US states need ≥100 (Figs 3.1–3.5 captions, pp.29–34; appendix Figs 3, 4, 6, 7).
- *Primitive–O\*NET correlations:* tasks appearing in ≥100 conversations (fn1, p.52; Fig 1.4 caption, p.11).
- *Coverage analysis:* all tasks above the privacy floor of 15 (fn1, p.52).
- *Word clouds:* tasks/requests with ≥1,000 observations, top quartile only (Fig 1.5 caption, p.11).
- *Productivity aggregation:* tasks with ≥200 observations, an implied 0.02% of the 1M sample, chosen because it replicates the earlier 100k-sample result (p.48; fn6, pp.52–53).

**Plot construction.** Almost every bivariate relationship in Chapters 3 and 4 is a 20-bin binned scatterplot (fn2, p.27), so the r and R² values quoted in figure insets are computed between bin means, not between conversations or tasks, and are mechanically larger than conversation-level equivalents. Figures 3.3, 3.4 and 3.5 are the exception in that their units are countries and states rather than bins.

**Regressions.**
- *Convergence:* `ln AUI_{s,t} = α + β ln AUI_{s,t−1} + ε_{s,t}`, estimated on US states with two observations each (Aug and Nov 2025), by OLS (β̂ ≈ 0.77), WLS weighted by state workforce (β̂ ≈ 0.76), and 2SLS instrumenting `ln AUI_{s,Aug}` with the state's workforce proximity to overall Claude usage patterns (β̂ ≈ 0.89 unweighted, β̂ ≈ 0.86 weighted by working-age population) (pp.15–17). A constant is included because the null implies it is zero, and it is estimated near zero throughout (fn8, p.18).
- *Cross-state AUI on tech-worker share:* `ln(AUI) = 0.36 × Comp & Math Share − 1.40`, R² = 0.61 (Fig 1.7, p.14).
- *Partial regressions:* the Chapter 3 controls set is GDP per capita, AI autonomy, automation percent, work and coursework use-case shares, human-without-AI time, human-with-AI time, multitasking and human ability (Fig 3.5 caption, p.34). The corresponding AUI partial regressions are in the online appendix (Figs 8 and 9, appendix pp.9–10).
- *Task education model:* sentence-transformer embeddings (`all-mpnet-base-v2`) of O\*NET task statements, Ridge regression onto BLS occupation-level education (fn4, p.52).
- *Productivity aggregation:* Hulten's Theorem applied to task-level productivity shocks, assuming the one-time TFP increase materialises over a decade alongside capital deepening (fn7, p.53); CES generalisation with ρ = (σ−1)/σ within occupation, then Hulten across occupations (fn9, p.53). The success adjustment multiplies task-level time savings by task-specific success rates before aggregating (p.48), with efficiency gains defined as the log difference between human-only and human-with-AI time (fn8, p.53).

**Outside data layered in.** BLS "Educational attainment for workers 25 years and older by detailed occupation", built on 2022 and 2023 American Community Survey microdata (Fig 2.1 caption, p.24, and the Ridge target at fn4, p.52); O\*NET task statements, task frequency ratings and employment weights (pp.43, 45–46); World Bank working-age population (fn4, p.37); GDP per working-age capita at country and state level (Figs 3.2–3.4); state workforce composition by SOC major group, used both as a regressor and as an instrument (pp.13–17); Natural Earth boundaries (fn3, p.37).

**Released data.** The report points readers to https://huggingface.co/datasets/Anthropic/EconomicIndex for the online appendix (fn2, p.52) and Table 2.1's full prompt texts (Table 2.1 caption, p.20). The release folder is `release_2026_01_15`. The report describes the release as "the most comprehensive to date, covering five new dimensions of AI use, consumer and firm use, and country and region breakdowns for Claude.ai" (p.2) and says it includes "task-level classifications along new dimensions and regional breakdowns globally for the first time" (p.54).

**No code was released for this wave.** Neither the report nor the appendix names a replication notebook, repository or script. The `release_2026_01_15` folder on Hugging Face contains `data/`, `data_documentation.md` and `aei_v4_appendix.pdf` and no `code/` directory (verified against the Hugging Face tree API, 2026-09-16). Reports 1–3 shipped notebooks or a code library; this one does not. Any replication of the numbers in this report must be re-implemented from the data documentation and the 2025-09-15 code library. Confirm the exact file list with the data steward before writing a fetch script.

---

## Limitations (verbatim)

Every limitation the report states about itself, quoted.

**On the primitives as measures**

> "We propose that multiple simple primitives, even if somewhat noisy and not perfectly accurate by themselves, can together provide important signals on how AI is being used. We therefore mainly tested for directional accuracy." — p.22

> "We selected a final set of nine new classifiers for the five primitives, all of which are directionally accurate even if they may deviate somewhat from human ratings." — p.22

> "While we are very confident in the directional accuracy of the new measures (e.g., tasks with higher average years of education needed to understand the human prompt are likely more complex), none of the measures should be taken as exact or definitive (e.g., Claude.ai may somewhat underestimate the human education years needed for many tasks)." — p.23

> "these measures are directionally accurate and, taken together, provide important signals even if individual classifications are imperfect." — p.54

**On the validation data**

> "For Claude.ai, we evaluated the classifier performance compared to a human researcher on a small set of transcripts in which users gave feedback to Claude.ai and for which we thus have permission to look at underlying transcripts. For first-party API (1P API) data, we validate the classifiers using a mix of internal and synthetic data. Neither data sources are fully representative of Claude.ai or 1P API traffic, but they allow us to check that the classifiers are working on data that resembles real usage data, while ensuring privacy." — p.22

**On the classifier model changing between waves**

> "In this report we use Sonnet 4.5 for classification whereas in our previous Economic Index report we used Sonnet 4. We previously found that different models can generate different classification outcomes, though these effects tend to be modest." — fn7, p.18

**On the diffusion estimate**

> "While this is consistent with rapid AI adoption and diffusion, this estimate comes with uncertainty given that it is based on a change observed over a three month period. Diffusion may ultimately proceed more slowly in the months and years to come." — p.6

> "This estimate comes with a high degree of uncertainty as the precision of our estimates cannot rule out much slower rates of diffusion." — p.15

> "A concern with estimating convergence this way is that our AUI estimates are subject to sampling noise and other variation unrelated to diffusion. This can produce classical attenuation bias: even if AUI is not actually changing, our estimate of [β] could end up meaningfully below one." — p.16

> "However, these estimates are less precise, and only the former is statistically distinguishable from 1 at the 10% level." — p.17

> "That said, our estimates are based on just three months of data. And while the 2SLS specification may help address sampling noise, considerable uncertainty remains." — p.17

**On the Gini comparison**

> "While it is important to exercise caution in interpreting short-run changes, this is a relatively large change toward perfect equality in which the AUI is equal to 1 for all states with a Gini coefficient of 0." — p.12

**On causality in the geography chapter**

> "Importantly, the primitives themselves are not necessarily causal factors—we don't know if income or education are truly driving adoption, or if they're proxies for other underlying conditions. Many of these factors are highly correlated with one another. For example, at the US state level, human education years show a strong association with the Anthropic AI Usage Index in isolation, but this relationship disappears once we control for GDP and other primitives—suggesting education may be capturing variation that's better explained by economic development and other factors." — pp.32–33

**On the state-level null results**

> "At the US state level, these relationships are not statistically significant–likely also due to the smaller sample size for US states." — p.32

> "This relationship is not significant at the US state level, perhaps because income variation and use case diversity are more limited within the United States than globally." — p.35

**On the level-dependence of the task-success/education relationship**

> "This means the relationship pattern at one level of observation (country) contradicts the relationship pattern at another level (US state)." — p.33

**On the platform comparison**

> "Part of this reflects the nature of the interaction: Claude.ai transcripts can include multi-turn conversations, while the API data we analyze is limited to single input-output pairs. This is because API requests arrive independently, with no metadata linking them to prior exchanges. This means we can only analyze them as isolated user-assistant pairs rather than full conversation trajectories." — p.26

> "This could reflect the nature of the API data, which is restricted to single-turn interactions, and that API tasks have been specifically selected for automation." — p.39

**On selection into observed tasks — the task-horizon caveat**

> "It's worth noting that a fundamental difference from the METR setting is selection. METR constructs a benchmark where a fixed set of tasks is assigned to models. In our data, users choose which tasks to bring to Claude. This means observed success rates reflect not just model capability but also user judgment about what will work, the cost of setting up the problem for Claude, and the expected time savings if the task succeeds." — p.42

> "If users avoid tasks they expect to fail, for example, observed success rates will overstate true capability on the full distribution of potential tasks. This selection likely operates on both platforms, but in different ways: API customers select for tasks amenable to automation, while Claude.ai users select for tasks that could benefit from iteration. Also due to this selection effect, there's no guarantee that more performant models would show improvement in this plot, because users may respond to new models by providing more challenging presentations of otherwise similar O\*NET tasks." — p.42

**On effective AI coverage**

> "This measure arguably gives a more realistic picture of job-level AI penetration. However, its implications depend on how often these Claude conversations actually displace or augment work that would otherwise be done by humans. For data entry clerks, AI likely does substitute for tasks previously performed manually. But when a Claude conversation maps to a teacher performing a lecture, it is less clear how this translates to reduced lecture time on the job." — p.45

> "This suggests that even 90% task coverage does not necessarily indicate large job impacts, since Claude may fail on key covered tasks or miss the most time-intensive ones." — p.43

**On the deskilling/upskilling exercise**

> "However, our education-based measure differs from Autor and Thompson's expertise concept: their framework would label some tasks as high expertise where ours specifies low education—for example, the Electrician task 'Connect wires to circuit breakers, transformers, or other components.' And these predictions are based on current Claude usage patterns, which will shift as models are trained on new capabilities and users discover new applications—potentially changing which tasks are covered and whether the net effect is deskilling or upskilling." — p.47

> "While highly suggestive, this may miss an important detail: the most complex tasks where Claude is used tend also to be those where it struggles most." — p.51

> "If we assume that AI-assisted tasks diminish as a share of worker responsibilities, removing them would leave behind less-skilled work." — p.4

**On the productivity estimates**

> "However, these estimates reflect current model capabilities, and all signs suggest that reliability over increasingly long-running tasks will improve." — p.38

> "A salient critique of this analysis is that it fails to account for model reliability. If workers must validate AI output, the productivity benefits will be smaller than raw speedups suggest." — p.48

> "A second critique concerns task complementarity. If some tasks are essential and cannot easily be substituted, then overall productivity effects will be constrained regardless of speedups on other tasks. Teachers may prepare lesson plans more efficiently with AI while having no impact on time spent with students in the classroom." — pp.48–49

> "There are certainly other ways to adjust based on task reliability. If tasks in our sample are composed of sub-tasks with heterogeneous AI applicability, and workers optimally deploy AI only on sub-tasks where it is effective, then scaling the efficiency gain by the success rate captures the extensive margin of AI adoption within a task." — fn8, p.53

> "Expanding the sample to 1M observations means that we need to take a stand on how to handle very infrequently occurring tasks—which are very common given that usage follows a power law, as we documented in our past report. We choose a threshold of 0.02% because it replicates our previous results for our sample of Claude.ai conversations… If we do not impose a restriction on our 1M sample and assume that efficiency gains for any task in our sample, even those with just 15 observations out of one million, the implied aggregate labor productivity growth over the next decade would be roughly 5% percentage points per year—a mechanical increase based on a the much larger set of tasks included." — fn6, pp.52–53

> "For tasks without observed AI speedup data, we assume no productivity change." — fn9, p.53

**On the sampling frame**

> "The unit of observation is a conversation with Claude on Claude.ai, not a user, so it is possible that multiple conversations from the same user are included, though our past work suggests that sampling conversations at random versus stratified by user does not yield substantively different results." — fn2, p.36

**On coverage of the world**

> "Since the Anthropic AI Usage Index is calculated per working-age capita based on working age population data from the World Bank, and population data is not readily available for all of these territories, we cannot calculate the AUI for these territories." — fn4, p.37

> "We only include countries with at least 200 observations in our sample for this figure because of the uncertainty of the measure for low-usage countries in our random sample." — Fig 3.1 caption, p.29 (and repeatedly through Figs 3.2–3.5)

**On abusive traffic**

> "We exclude the Seychelles from all geographic analyses because a large fraction of usage we saw during the sampling dates was abusive traffic." — fn5, p.37

> "We exclude Wyoming from all US state analyses because a large fraction of usage we saw during the sampling dates was abusive traffic." — fn6, p.37

---

## Open questions, conjectures and promised follow-ups (verbatim)

### Explicit promises of future work

> "We will revisit this question of the pace of diffusion in future reports." — p.17

> "In future work, we could leverage our 1P API data to understand which of these tasks are being integrated into production workflows." — p.45

> "We will track these dynamics over time, providing a longitudinal view of AI's role in the economy." — p.54

> "Ultimately, the strongest validation will come from the primitives' ability to capture meaningful variation in labor market outcomes. The data we release enable external researchers to analyze economic shifts in new ways." — p.24

> "This data release aims to enable researchers and the public to better understand the economic implications of AI and investigate the ways in which this transformative technology is already having an effect." — p.4

> "We publish this data to enable researchers, journalists, and the public to investigate novel questions about AI's economic impacts that can form the empirical foundation for policy responses." — p.54

### Where the report revises or pushes back on its own earlier report

> "In our previous report we noted that automated use had risen to exceed augmented use on Claude.ai, perhaps capturing both improving capabilities and greater familiarity among users with LLMs. Data from November 2025 points to a broad-based shift back toward augmented use on Claude.ai" — p.5

> "Nevertheless, the automation share was still elevated as compared to nearly one year ago when we first began tracking this measure, suggesting that the underlying trend is still toward greater automation even as the August spike overstated how quickly it was materializing." — p.9

> "Product changes during this period—including file creation capabilities, persistent memory, and Skills for workflow customization—may have shifted usage patterns toward more collaborative, human-in-the-loop interactions." — p.5

> "Our earlier work found that 36% of jobs had AI usage for at least a quarter of their tasks, with about 4% reaching 75% task coverage. This measure was based only on the appearance of a task in our data, however. The primitives introduced in this report can help better characterize how AI is changing the work content of occupations." — p.43

> "In earlier work, we estimated that widespread adoption of AI could increase US labor productivity growth by 1.8 percentage points annually over the next decade. Here we revisit that analysis, incorporating the task success primitive introduced in this report and a richer treatment of task complementarity." — p.48

> "Adjusting productivity estimates for task reliability roughly halves the implied gains, from 1.8 to about 1.0 percentage points of annual labor productivity growth over the next decade." — p.38

> "This mirrors a finding from our 3rd Economic Index report where countries with higher Anthropic AI Usage Index tend to use Claude in a more collaborative manner (augmentation), rather than letting it operate independently (automation)." — p.35

> "This echoes findings from our prior report and aligns with recent work by Microsoft." — p.28

> "we replicate the finding from our prior report that GDP is strongly correlated with the AUI" — pp.30–31

### Conjectures offered as explanation, not established

> "Multiple factors could contribute to these patterns:
> • Personal use cases may be more common as AI adoption increases and more diverse users use AI, or existing users explore wider applications of AI. In contrast, countries with lower per capita adoption (which is correlated with lower per capita income) may be focused on specific use cases such as coding or as coursework.
> • Countries differ in their ability to pay for Claude, and coursework use cases may be better suited to free Claude usage than complex use cases in work areas such as software engineering.
> • Users in higher-income countries may have more other resources, such as free time and continuous Internet access, that enable non-essential personal use cases." — p.30

> "This aligns with a simple adoption curve story: early adopters in less developed countries tend to be technical users with specific, high-value applications or use Claude for education, whereas mature markets see usage diversify toward casual and personal purposes." — p.3

> "Cross-country, educated populations may attempt harder tasks and therefore see lower success rates. Within homogeneous contexts, education may not improve task success." — p.33

> "Claude.ai also shows higher task success rates (67% vs. 49%), which may reflect the benefits of multi-turn conversation, where users can clarify, correct course, and iterate toward a solution." — p.26

> "This may reflect how multi-turn conversation effectively breaks complex tasks into smaller steps, with each turn providing a feedback loop that allows users to correct course." — p.42

> "Rising concentration among a small set of tasks suggests the highest-value applications continue to generate outsized economic value even as models have become more capable at a wider range of tasks." — p.7

> "Because API use is automation-dominant, this suggests that businesses are increasingly using Claude to automate routine back-office workflows such as email management, document processing, customer relationship management, and scheduling." — pp.8–9

> "Rather than displacing highly skilled professionals, this could instead reinforce the value of their complementary expertise in understanding AI's work and assessing its quality." — p.51

> "Indeed, the close relationship between education levels in inputs and outputs signals that countries with higher educational attainment may be better positioned to benefit from AI, independent of adoption rates alone." — p.4

> "Combined with the finding that higher-usage countries engage Claude more collaboratively, this suggests that the skills required to use AI well may themselves be unevenly distributed." — p.36

> "This highlights the importance of skills and suggests that how humans prompt the AI determines how effective it can be. This also highlights the importance of model design and training. While Claude is able to respond in a highly sophisticated manner, it tends to do so only when users input sophisticated prompts." — pp.34–35

> "How models are trained, fine-tuned and instructed affects how they respond to users. For example, one AI model could have a system prompt that instructs it to always use simple language that a middle school student could understand, whereas another AI model may only respond in complex language that would require a PhD education to understand. For Claude, we observe a more dynamic pattern where how the user prompts Claude relates to how Claude responds." — p.35

### Open questions stated as questions or unresolved

> "One way to examine the implications of the education gradient is to look at the share of automation across the education levels required to understand the inputs. If high-education tasks show relatively more automation, it could signal more exposure for white collar workers. Here, though, the message is unclear: the automation share is essentially unrelated to the human levels of education required to write the prompt" — pp.39–40

> "In what contexts do users defer more to Claude?" — p.40

> "Beyond how much of a worker's day AI can successfully perform, a separate question is which tasks get covered, and whether those tend to be the high-skill or low-skill components of the job." — p.45

> "Combined with income-driven differences in how AI is used, this raises questions about whether AI will narrow or widen international economic gaps." — p.54

> "But these impacts depend crucially on complementarity across tasks, and whether increased productivity at a certain task may increase the demand for it." — p.54

> "What this analysis shows is that the productivity effects of automation may ultimately be constrained by bottleneck tasks that elude AI automation for the time being. And the labor market implications of increasingly capable AI could be similarly affected by such forces. For example, Gans and Goldfarb (2026) argue that the presence of bottleneck tasks within jobs means that partial AI automation can lead to an increase in labor income as such tasks increase in economic value (at least until a job is entirely automated)." — p.51

> "On the other hand, some historical evidence suggests that when technologies automating job tasks appear in patent data, employment and wages subsequently fall for exposed occupations (Webb 2020)." — fn5, p.52

> "If the education level can be interpreted like expertise in Autor and Thompson's analysis, their framework might predict that wages will fall and employment will increase for technical writers and travel agents; conversely, real estate managers will specialize in complex negotiations and stakeholder management, shrinking employment while increasing wages." — p.47

> "These patterns illustrate how jobs may evolve over the coming years as their task content adjusts in response to AI." — p.47

> "Equally important to the patterns documented here are potential changes across this and subsequent reports. As AI capabilities advance, Claude's success rate may increase, usage patterns may show greater autonomy, users may tackle new and more complex tasks, and tasks that prove automatable may graduate from interactive chat to API deployment." — p.54

> "On the other hand, the continuing growth in model capabilities suggests that both task coverage and task success may increase, which, in turn, could increase productivity impacts." — p.52

> "These relationships may help predict labor market outcomes and inform a smooth transition to an AI-enabled economy that will require different skillsets." — p.36

> "How willing users are to experiment with AI, and whether policymakers create a regulatory context that advances both safety and innovation, will shape how AI transforms economies. For AI to benefit users globally, expanding access alone will not suffice—developing the human capital that enables effective use, particularly in lower-income economies, is essential." — p.55

### Invitations to combine the primitives

> "These validations suggest individual primitives are directionally correct—and combining them may provide additional analytical value, such as enriching productivity estimates with task success rates or constructing new measures of occupational exposure." — p.23

> "Even so, the primitives enrich our understanding of how people use AI. Systematic relationships emerge across primitives, regions, and tasks—patterns we explore in depth in Chapters 3 and 4. That these relationships are intuitive and consistent suggests the primitives capture relevant aspects of how people and businesses use Claude." — p.23

> "Because AI capabilities are advancing so rapidly and the economic effects will be unevenly experienced, we need a breadth of signals to uncover not just how Claude is used but also to inform what impact this technology will have." — p.19

> "See also Tomlinson et al (2025) for a related AI applicability score." — fn3, p.52

---

## What it did not test

*This section is the wiki author's inference, not the report's own text. It lists adjacent questions the report had in hand the data to address but did not, and constructs it used without validating.*

### Constructs used without validation

1. **Task success has no reported validation statistic.** The report says a "simple classifier performed better than a nuanced, complex classifier when compared to human ratings" (p.22) but gives no accuracy, agreement rate, confusion matrix or kappa. Task success then carries the entire success-adjusted productivity revision (1.8 → 1.2/1.0pp, p.48), the effective-coverage measure (p.43) and the task-horizon result (pp.41–42). It is the most load-bearing and least validated primitive in the report.
2. **AI autonomy has no reported validation statistic and no external benchmark.** Figure 2.1 validates human education against BLS; the productivity paper validated the time estimates. Autonomy, multitasking and human-only ability have neither. Autonomy nevertheless produces the strongest single country-level correlation in Chapter 3 (r = −0.801, β = −8.10, Fig 3.3) — the largest effect in the chapter rests on the least externally anchored measure.
3. **Claude grades its own work.** Task success is Claude's assessment of whether Claude succeeded (p.21). The report does not test whether this self-assessment is calibrated, whether it is biased by task type, or whether it varies with the classifier model. Since the classifier is Sonnet 4.5 and the underlying conversations came from a mix of production models, the report also does not decompose success by the model that produced the response — which the transcripts would support.
4. **"Human could do alone" (88% globally) is never used in an analysis.** It appears in Figure 2.2 and in the partial-regression control set (Fig 3.5 caption) and nowhere else. It is the primitive most directly about substitution versus complementarity, and it is the one least explored.
5. **Multitasking (9% globally) is likewise measured and then set aside.** It appears only in Figure 2.2 and in the Chapter 3 control set. Its bearing on the human-with-AI time estimate — a multi-task conversation's minutes are not one task's minutes — is not examined.
6. **The 2SLS exclusion restriction is argued but not tested.** The instrument is workforce composition; validity rests on the claim that it "is expected to be uncorrelated with sampling noise in our AUI estimates" (pp.16–17). No first-stage F statistic, overidentification test or weak-instrument diagnostic is reported. Nor are standard errors reported anywhere for the convergence estimates; only the outcome of significance tests is stated in words.
7. **The task-education Ridge model is not validated out of sample.** No hold-out R², no cross-validation score, no comparison against an alternative target such as O\*NET Job Zones. The entire deskilling result depends on its predictions, and the report itself names a case where it disagrees with the Autor–Thompson expertise concept (p.47) without quantifying how often that happens.

### Adjacent questions the data would support but the report did not ask

8. **Coverage of the primitives by state and by country jointly.** Chapter 3 correlates each primitive with the AUI one at a time and then shows partial regressions in the appendix. It never asks which primitive best predicts the AUI once all are entered together, nor reports the full multivariate coefficient table behind Figures 8 and 9.
9. **Whether the state convergence result survives dropping DC.** DC is the extreme AUI outlier in both Figures 1.7 and 1.8 and has a workforce unlike any state. Its influence on β̂ ≈ 0.77 and on `R² = 0.61` is not reported, and with N = 50 a single leverage point can move both materially. The report drops Wyoming for abusive traffic but does not test DC's leverage.
10. **Whether the Gini fall is a composition effect.** The AUI numerator is a share of a 1M random sample. If the sample's geographic composition shifted — for instance because the Aug and Nov samples differ in tier mix, or because Claude Code and other surfaces entered the Claude.ai traffic differently — the Gini could fall without diffusion. The report notes sampling noise as an attenuation problem for β but does not test whether the Gini change survives a bootstrap over the sample.
11. **Whether the augmentation reversal is a classifier-model artefact.** The report names the Sonnet 4 → Sonnet 4.5 change (fn7, p.18) and separately reports a 5pp jump in augmentation and a 7pp fall in directive use. It does not re-run the Aug 2025 sample through Sonnet 4.5, or the Nov 2025 sample through Sonnet 4, to bound how much of the reversal is measurement. This is the single most available and most consequential robustness check in Chapter 1 and it is not done.
12. **Whether the product changes named as a possible cause coincide with the reversal in time.** File creation, memory and Skills are named (p.5) but the data are a single week in November; no event study, no before/after within the window, no comparison between users with and without access.
13. **Task horizons by SOC group.** The task-horizon plot pools all O\*NET tasks (Fig 4.3). The report emphasises that its advantage over METR is "expanding beyond coding tasks" (p.42) but never splits the horizon estimate by occupational family — the obvious test of whether the 19-hour Claude.ai figure is a coding number or an everything number.
14. **The 19-hour extrapolation is never bounded.** It extrapolates a linear fit from a plot whose x-axis ends at 8 hours to a crossing at 19 hours. No confidence band, no alternative functional form (METR's own work uses a logistic in log duration), no sensitivity to the binning choice.
15. **Effective AI coverage is computed but never linked to anything observable.** No correlation with employment change, wage change, vacancy postings or any labour-market outcome, though the report says elsewhere that outcome-linkage is "the strongest validation" (p.24). The 49%-of-jobs coverage figure and the effective-coverage scatter sit unconnected to the labour market.
16. **The deskilling exercise is not weighted to a population of workers.** Figure 4.5 is employment-weighted, but the occupation-level deskilling/upskilling results are reported as named anecdotes (technical writers, travel agents, real estate managers) rather than as a distribution. How many workers are in deskilled versus upskilled occupations is not reported, though every input to that calculation is in hand.
17. **Task success is never crossed with collaboration mode.** The report has both facets on the same conversations. Whether directive conversations succeed more or less often than task-iteration ones — which speaks directly to whether delegation is efficient — is not reported, on either platform.
18. **Speedup is never reported by use case.** Speedup is shown against education (Fig 4.1) but not split by work versus coursework versus personal, though the productivity claim is about work and 54% of Claude.ai conversations are not work.
19. **The productivity aggregation uses Claude.ai and API speedups separately but never a weighted blend.** The two samples imply the same 1.8pp headline for different reasons (p.48); the report does not ask what a realistically weighted economy-wide mix of the two deployment modes would imply.
20. **Country-level results are never checked against the AUI threshold.** Countries need ≥200 observations to enter Figures 3.1–3.5, and the country sample is N = 117 (p.34). The report does not report how much of world usage or world working-age population that leaves out, nor whether the excluded low-usage countries would move the income gradients if included with wider error bars.
21. **Coursework use is measured but its 19% share is never analysed at the task level.** The report says educational use "may signal where the future workforce is building AI-complementary skills" (p.21) and that coursework is concentrated in low-income countries (p.29), but never asks which O\*NET tasks or request clusters the coursework conversations map to.
22. **The AI education primitive is measured, correlated with human education, and then dropped.** After the r = 0.925/0.928 result (p.34), the report does not use AI education anywhere else — not in the productivity analysis, not in effective coverage, not as a residual measure of where Claude over- or under-shoots the user's level. The residual (AI education minus human education) is a construct the data supports and the report does not build.

### Internal tensions a replicator should know about

23. **Two different success-adjusted productivity numbers.** Chapter 4's opening summary says "from 1.8 to about 1.0 percentage points" (p.38); the body says 1.2pp for Claude.ai and 1.0pp for API (p.48). Anyone citing "success-adjusted productivity" must state the platform.
24. **"Property managers" (p.4) and "real estate managers" (p.47) are the same upskilling example under two names.** The O\*NET occupation is presumably Property, Real Estate, and Community Association Managers; the report does not give the SOC code.
25. **Figure 1.3's Jan-2025 augmentation label reads 55% while the body text on p.9 reads 56%.**
26. **The Gini values differ between text (0.37 → 0.32) and figure legend (0.367 → 0.318).** Rounding, but a replication that reproduces 0.318 and compares it to a quoted 0.32 should know why.
27. **The tech-worker coefficient's units.** The body reads it as "each 1% increase in the share… is associated with 0.36% higher usage per capita" (p.13) while the figure inset fits `ln(AUI)` on the share in percentage points (Fig 1.7). Under the inset's specification 0.36 is a log-point change per percentage point of employment share, not an elasticity. A post that quotes this number should state which reading it uses.
28. **The web version of the report contains a paragraph the PDF does not.** After Figure 4.2 the landing page carries: "Note though that these distributions do not span the same set of tasks. API usage covers a more narrow swath of tasks in the economy, as seen in the concentration plot in Chapter 1. The high education tasks that experience heavy usage in the API data include security analysis, testing and quality assurance, and code review, whereas Claude.ai users are more likely to have iterative, instructive sessions." This paragraph is absent from PDF pp.40–41. Other small divergences: the PDF introduction says augmentation patterns "grew, rising to just over half" where the page says "edged to just over half" (p.2); the PDF says "24% of usage on Claude.ai" where the page says "24% of observed usage" (p.5); the PDF says users in higher-income countries "may have more other resources" where the page says "may have other resources" (p.30). Quote the PDF and say so.

---

## Verification

- **Date of fetch and check:** 2026-09-16.
- **URLs fetched and read in full on that date:**
  1. https://www-cdn.anthropic.com/096d94c1a91c6480806d8f24b2344c7e2a4bc666.pdf — the report, all 55 pages, fetched as a PDF and read page by page including all figure captions, figure insets and footnotes.
  2. https://www.anthropic.com/research/anthropic-economic-index-january-2026-report — the landing page, read in full apart from a trailing block of the Authors & Acknowledgements list (159 lines) that the fetch tool truncated. That truncated block contains the author and acknowledgement names, which are independently recorded from PDF p.1, and no substantive research content: the page's Concluding Remarks section was retrieved complete immediately before it.
  3. https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/main/release_2026_01_15/aei_v4_appendix.pdf — the online appendix, all 19 pages. `web_fetch` returned `url_not_accessible` for this URL; the file was retrieved with `curl` and converted with `pdftotext -layout`, and the resulting text read in full. File metadata confirmed with `pdfinfo`: 19 pages, 6,036,245 bytes, created 2026-01-15 19:35:15 UTC by pdfTeX-1.40.27.
  4. https://huggingface.co/api/datasets/Anthropic/EconomicIndex/tree/main/release_2026_01_15 — the release folder listing, used solely to establish that the appendix is a separate file and that the folder contains no `code/` directory. Returned `data/` (directory), `aei_v4_appendix.pdf` (6,036,245 bytes) and `data_documentation.md` (18,721 bytes), at repo commit `2ea58ff75e4247d26810c37f10c179edc2466cac`.
- **What could not be fetched:** nothing material. `web_fetch` refused the Hugging Face appendix URL and the fallback `curl` route succeeded. The landing page's trailing acknowledgements block was truncated by the fetch tool, as noted above.
- **Figures.** The report's figures were read as rendered images within the fetched PDF. Values quoted from figure insets (regression coefficients, r, R², p, N, Gini) are read off those rendered plots and are marked "(figure inset)" in the Claims section. Values that the running text also states are cross-checked against the text; where text and inset differ, both are recorded (see Claims 14, 25, and What it did not test §§25–26).
- **Quotation check.** Every passage inside quotation marks in the `Definitions (verbatim)`, `Limitations (verbatim)` and `Open questions, conjectures and promised follow-ups (verbatim)` sections, and every quoted fragment in `Claims`, was checked against the fetched text of the report PDF or the fetched text of the online appendix at the cited page before being written here. Where the source contains an apparent typographical error it is reproduced as printed and flagged rather than corrected — see fn6, p.52 ("roughly 5% percentage points"), fn9's use of both ρ and ϱ, and the collaboration-pattern prompt's "the one that is most appears most frequently" (appendix p.16).
- **Not consulted as a source.** `reference/sources/` was not used; nothing in this file derives from the earlier programme.
