# Estimating AI productivity gains from Claude conversations

## Source

- **Title:** "Estimating AI productivity gains from Claude conversations"
- **Authors:** Alex Tamkin and Peter McCrory (PDF cover, p. 1; BibTeX key `tamkinmccrory2025productivity`, p. 21). Acknowledgements name fifteen further people (p. 1).
- **Dates:** the web page header reads "Nov 25, 2025"; the PDF cover reads "Published: November 5, 2025" (p. 1) and both BibTeX blocks give `date = {2025-11-05}` (web §"Bibtex"; PDF p. 21). The `wiki/INDEX.md` row carries 2025-11-25, which is the web page's date. Flagged in `## Verification`.
- **URLs:** web https://www.anthropic.com/research/estimating-productivity-gains ; PDF https://www-cdn.anthropic.com/e5645986a7ce8fbcc48fa6d2fc67753c87642c30.pdf (linked from the page as "Read as a PDF").
- **Type:** research note / paper. The text calls itself "this research note" (p. 3) and "This report" (p. 5).
- **Length and form:** PDF 25 pages: Overview (pp. 2–4), Introduction (pp. 4–5), Estimating task length and time savings (pp. 5–6), Validation (pp. 6–8), Results — Task-level savings (pp. 9–13), From task-level efficiency gains to economy-wide productivity effects (pp. 13–17), How might AI change how workers spend their time? (pp. 17–18), Limitations (pp. 19–20), Conclusion (pp. 20–21), Bibtex and five footnotes (pp. 21–22), Appendix — comparison figure and four prompts (pp. 22–25). Ten numbered figures plus one unnumbered "Table:" on p. 11. The web version carries the same text and the same figures (the p. 11 table is likewise unnumbered there) and differs from the PDF in three sentences, listed in `## Verification`.
- **Which Economic Index release/window it rests on:** none. The note uses its own sample — "100,000 conversation transcripts from Claude.ai (Free, Pro, and Max tiers)" (p. 5) — and no sampling dates, release folder or data window are given anywhere in either version. It is positioned as part of the Index programme ("As part of the Anthropic Economic Index", p. 4) and follows "our Economic Index methodology" for aggregation (p. 5), but it publishes no release identifier and no dataset. Model named: Claude Sonnet 4.5 in the JIRA validation (p. 8); the model used to produce the 100,000 transcript estimates is never named.
- **External data:** O*NET task statements and occupation task lists (pp. 5, 14); BLS Occupational Employment and Wage Statistics (OEWS) May 2024 for wages and the total wage bill (pp. 9, 10, 14); the JIRA-ticket software-task dataset at Zenodo record 7022735 (p. 6, linked on the web as "software development tasks"); Filippucci, Gal and Schief (2024) for the comparison figure (p. 22); BLS/FRED for the labour-productivity history chart (Figure 8, p. 16); FRBSF for TFP history (footnote 5, p. 22).

## Claims

Numbered; each carries its page and figure/table reference, the number as published, and the comparison it rests on. Where two places in the document give different numbers for the same quantity, both are recorded.

**Headline and sample**

1. **100,000 Claude.ai conversation transcripts (Free, Pro and Max tiers) were analysed** (p. 5; web §"Estimating task length and time savings"). Comparison: none — this is the sample. The Overview describes it as "one hundred thousand real conversations from Claude.ai" (p. 2). No window, no geography, no user counts.

2. **Tasks would take on average about 90 minutes without AI assistance** (Overview, p. 2), given elsewhere as **"on average, take people 1.4 hours to complete"** (p. 3). Comparison: Claude's estimate of the human-alone completion time for the task in each conversation, averaged over the sample. 90 minutes = 1.5 h and 1.4 h are the same quantity stated to different precision in the Overview and the summary bullets.

3. **Claude speeds up individual tasks by about 80%** (Overview, p. 2; summary bullet, p. 3: "Claude estimates that AI reduces task completion time by 80%"). Comparison: `1 - time_with_ai / time_without_ai`, both terms Claude-estimated. Two other central-tendency figures appear: **"The median conversation experienced an estimated 84% time savings"** (p. 12) and **"The overall median savings is 81%"** across O*NET tasks (Figure 6 caption, p. 13). The three numbers are different statistics (headline, median conversation, median task) and the document does not reconcile them.

4. **The average task would cost about $55 in human labour** (p. 3, "By matching tasks to O*NET occupations and BLS wage data, we estimate these tasks would otherwise cost $55 in human labor"), stated later as **"a median of $54 in professional labor to hire an expert to perform the work in each conversation"** (pp. 10–11). Comparison: Claude's estimated task time multiplied by the OEWS May 2024 average hourly wage of the O*NET-matched occupation.

**Validation**

5. **Prompt self-consistency: log-scale correlations of r=0.89–0.93 across prompt variants, on 1,800 conversations per variant** (p. 6). Comparison: Claude's human-time estimates under one prompt phrasing against another ("employee with appropriate skills" vs "skilled professional"; Figure 2 uses Prompt 1 "employee with appropriate skills" vs Prompt 2 "human worker … competent in the relevant field"). Figure 2's panel title gives r=0.892 and a log regression slope of 0.91 (Figure 2, p. 7). Sample restriction: conversations "where users consented to share these conversations with us" (p. 6).

6. **External benchmark on 1,000 JIRA software tasks: developers ρ=0.50 and r_log=0.67; Claude Sonnet 4.5 ρ=0.44 and r_log=0.46; Sonnet 4.5 with ten examples ρ=0.39 and r_log=0.48** (pp. 7–8). Comparison: each estimator's predictions against time-tracked actual completion times, on the same 1,000-task subset; the human developers are the benchmark, and they "have full context on the codebase" while Claude "receives only the title and description of the JIRA tickets" (p. 7). The Figure 3 panel headers give the same statistics to three decimals — ρ=0.500, r_log=0.673, mean |dlog|=0.311 (developers); ρ=0.437, r_log=0.459, mean |dlog|=0.456 (Sonnet 4.5 zero-shot); ρ=0.393, r_log=0.484, mean |dlog|=0.450 (10-shot) — with log-fit slopes of 0.67, 0.30 and 0.31 (Figure 3, p. 8).

7. **Claude's estimates are compressed relative to reality and skew to overestimates** (p. 8). Comparison: the fitted log slopes above (0.30–0.31 for Claude against 0.67 for developers, both below the 45° line). The stated consequence: "the actual differences in task lengths across tasks may be larger than we report, and that actual task lengths may be slightly shorter" (p. 8).

**Task-level results**

8. **Nine example tasks (Figure 4, p. 9), with Claude-estimated task time, OEWS hourly wage, implied task cost and time savings:** vocational education teachers, develop curricula — 4.5 h, $33/h, $149, 96%; library science teachers, compile bibliographies — 2.5 h, $41/h, $101, 93%; office clerks, troubleshoot office equipment — 0.3 h, $22/h, $7, 56%; social science research assistants, prepare tables/graphs/reports — 2.8 h, $31/h, $84, 91%; executive secretaries, prepare invoices/reports/memos — 1.2 h, $37/h, $46, 87%; agricultural science teachers, advise students — 1.6 h, $47/h, $76, 83%; financial analysts, interpret price/yield data — 0.8 h, $58/h, $43, 80%; educational and vocational counselors — 0.4 h, $34/h, $14, 75%; secretaries and administrative assistants, compose meeting notes — 0.3 h, $23/h, $7, 61%. Comparison: within each row, the with-AI time against the without-AI time, both Claude-estimated; across rows, tasks against each other.

9. **Curriculum development tasks Claude thinks would take 4.5 hours are completed "in just 11 minutes", with "an implied labor cost of $115 based on the average hourly wage of teachers"** (p. 10). Comparison: the estimated human-alone time against the estimated with-AI time for one task. The $115 does not match Figure 4's $149 for the same 4.5-hour curriculum task at $33/h (see `## Verification`).

10. **"People also use AI to save 87% of the time it would take to write invoices, memos, and other documents … AI saves 80% of time on financial analyst tasks like interpreting financial data for tasks that would ordinarily cost $31 in wages"** (p. 10). Comparison: per-task savings ratios. The 87% and 80% match Figure 4's executive-secretary and financial-analyst rows; the $31 does not match Figure 4's $43 for the financial-analyst task (see `## Verification`).

11. **Task length by occupation: management 2.0 h, legal 1.8 h, education 1.7 h, arts/media 1.6 h; food preparation, installation/maintenance and transportation 0.3–0.5 h** (p. 10; full 22-row table, p. 11). Comparison: average Claude-estimated human-alone task time across the subset of tasks Claude is used for in each SOC major group — "we show averages for each occupation category among the subset of tasks that Claude is used for" (p. 10), with outliers handled per footnote 1.

12. **Task cost by occupation: management $133, legal $119, computer and mathematical $82, business and financial $69, food preparation and serving $8** (p. 10; table p. 11). Comparison: median task time × occupation average OEWS wage, averaged with weights by each task's prevalence in the sample (table caption, p. 11).

13. **Full occupation table (p. 11), time without AI / average wage / average task cost / time savings:** management 2.0 h, $68/h, $133, 85.1%; business and financial operations 1.5 h, $45/h, $69, 83.5%; computer and mathematical 1.5 h, $56/h, $82, 80.2%; architecture and engineering 1.3 h, $50/h, $64, 77.7%; life, physical and social science 1.5 h, $43/h, $63, 82.8%; community and social service 1.1 h, $30/h, $33, 80.8%; legal 1.8 h, $66/h, $119, 80.7%; education, training and library 1.7 h, $32/h, $52, 84.5%; arts, design, entertainment, sports and media 1.6 h, $37/h, $58, 78.6%; healthcare practitioners and technical 0.9 h, $51/h, $43, 74.8%; healthcare support 0.6 h, $19/h, $10, 75.9%; protective service 0.3 h, $29/h, $9, 77.7%; food preparation and serving 0.5 h, $17/h, $8, 75.4%; building and grounds cleaning and maintenance 0.6 h, $19/h, $11, 75.8%; personal care and service 0.5 h, $19/h, $10, 61.0%; sales and related 0.6 h, $26/h, $15, 66.2%; office and administrative support 0.7 h, $24/h, $16, 67.8%; farming, fishing and forestry 0.5 h, $20/h, $10, 83.3%; construction and extraction 1.1 h, $31/h, $35, 86.7%; installation, maintenance and repair 0.5 h, $30/h, $13, 65.7%; production 0.9 h, $24/h, $22, 79.7%; transportation and material moving 0.3 h, $23/h, $7, 79.4%. Comparison: SOC major groups against one another, within the sample of tasks Claude is used for.

14. **Higher-wage occupation categories are used for longer tasks: r=0.8** (p. 11 text and Figure 5 caption, p. 12), with the chart giving r=0.799, R²=0.638, n=22 (Figure 5, p. 12). Comparison: cross-sectional correlation across 22 SOC major groups between the category's average OEWS hourly wage and the average Claude-estimated task duration in the sample.

15. **Savings spread: "the task of checking diagnostic images only shows 20% time savings"; "compiling information from reports sees approximately 95% time savings"; the distribution is "concentrated within the 50-95% range, peaking between 80-90%"** (p. 12; Figure 6, p. 13). Comparison: O*NET tasks against one another, on the same savings ratio. The summary bullet on p. 3 gives the same idea by category: "healthcare assistance tasks can be completed 90% more quickly, whereas hardware issues see time savings of 56%" (p. 3; 56% matches the office-clerk hardware task in Figure 4, and 90% is a task, not the healthcare-support category's 75.9% in the table).

16. **Published RCT comparison: past trials found time savings of "56%, 40%, 26%, 14% and even negative"** (p. 13, each a hyperlink on the web to Peng et al., Noy and Zhang, a SSRN paper, NBER w31161 and the METR study). Comparison: this note's ~80% estimated savings against experimental estimates; the note attributes the gap to unmeasured post-conversation work or older model generations.

**Aggregation to the economy**

17. **Claude's estimates imply a 1.8% annualised increase in US labour productivity, and an implied 1.08% annualised increase in TFP** (Figure 7 caption, p. 15; the table's "Overall economy" row gives employment 154.1M, wage bill $10.46T, wage bill share 100.00%, ln(time est. ratio) 0.196, annual labour productivity contribution 1.80%). In the text: "Assuming 10 years for AI to reach universal adoption across the US economy—and using current models—we calculate that Claude's estimates imply an annual increase in US labor productivity of 1.8%… Assuming that labor's share of total factor productivity is 0.6, this implies an overall total factor productivity increase of 1.1% per year" (p. 15). Comparison: against the historical US rate — "which has averaged 2.1% per year since 1947 and 1.8% since 2019" (p. 15) — and against TFP growth that "has tended to be less than 1% since the early 2000s" (pp. 15–16), with footnote 5 giving 0.7% average TFP growth 2015–2024 and 1.6% for 1995–2004 (p. 22).

18. **Top-ten occupation contributions (Figure 7 table, p. 15):** software developers, 1.65M employed, $239.18B wage bill, 2.3% wage-bill share, ln(time est. ratio) 1.507, 0.34% annual labour-productivity contribution; general and operations managers 3.58M, $477.16B, 4.6%, 0.224, 0.10%; market research analysts and marketing specialists 0.86M, $74.47B, 0.7%, 1.271, 0.09%; secondary school teachers 1.07M, $79.05B, 0.8%, 0.820, 0.06%; lawyers 0.75M, $136.66B, 1.3%, 0.451, 0.06%; customer service representatives 2.73M, $123.70B, 1.2%, 0.431, 0.05%; retail salespersons 3.80M, $141.18B, 1.3%, 0.360, 0.05%; computer and information systems managers 0.65M, $121.44B, 1.2%, 0.379, 0.04%; marketing managers 0.38M, $66.03B, 0.6%, 0.697, 0.04%; elementary school teachers 1.39M, $97.24B, 0.9%, 0.384, 0.04%. Comparison: each occupation's wage-bill-weighted, time-weighted productivity gain against the 1.80% economy total.

19. **Share of the total gain: "Software developers contribute most (19%)… General and Operations Managers (about 6%), Market Research Analysts and Marketing Specialists (5%), Customer Service Representatives (4%) and Secondary School Teachers (3%) round out the top five"** (p. 17). Comparison: each occupation's contribution divided by the 1.8% total. The ordering of the last two differs from the Figure 7 table (see `## Verification`).

20. **Low-contribution sectors: "restaurants, healthcare delivery, construction, and retail contribute much less to the overall productivity effect. This is mostly because few of their tasks appear in our data"** (p. 17). Comparison: contribution to the aggregate against the sample's task coverage, not against those sectors' potential.

21. **The estimate sits at the upper end of the published range** (p. 16; Figure 10, p. 22). Comparison: the 1.8% dotted line against the eight estimates collected in Filippucci, Gal and Schief (2024) — Baily, Brynjolfsson and Korinek (2023, USA) ≈2.6; McKinsey (2023, Global) range ≈0.6–3.4; Goldman Sachs (2023, USA) ≈1.5; IMF (2024, UK) ≈0.9–1.5; AI Commission of France (2024, FRA) ≈1.35; Aghion and Bunel (2024, USA) ≈1.05; Bereaud (2024, EA) ≈0.45; Acemoglu (2024, USA) ≈0.3 (values read off the reproduced chart, Figure 10, p. 22).

**Bottlenecks**

22. **Within-occupation bottlenecks (Figure 9, p. 18).** Software developers: "Develop and direct software system testing and validation procedures, programming, and documentation" — 86% potential time savings, currently ~11% of weekly time; "Modify existing software to correct errors…" — 76%, ~22%; bottlenecks "Coordinate software system installation and monitor equipment functioning…" (~4% of weekly time) and "Supervise the work of programmers…" (~2%), both "No AI usage data". Retail salespersons: 80%/~12% and 80%/~6% accelerated; ~10% and ~5% bottlenecks. Customer service representatives: 73%/~38% and 47%/~9% accelerated; ~5% and ~5% bottlenecks. Secondary school teachers: 93%/~1% and 82%/~5% accelerated; ~3% and ~2% bottlenecks. Comparison: within an occupation, tasks with large Claude-estimated savings against tasks with no AI usage observed in the sample, each weighted by Claude's estimate of weekly time share.

23. **Task-composition example: "Claude estimates that programmers spend 23% of their time writing and maintaining code, 15% analyzing and rewriting programs, and smaller fractions on testing, documentation, and meetings"** (p. 14). Comparison: within-occupation time allocation across the O*NET task list, all of it Claude-estimated.

## Definitions (verbatim)

Every construct, measure, threshold and formula the document defines, quoted exactly, with page references. PDF page numbers; the identical text appears on the web page under the section headings named.

**The two core estimates (p. 5, §"Estimating task length and time savings")**

- "**Time estimate without AI**: The hours a human professional would need to complete the task without AI assistance"
- "**Time estimate with AI:** The amount of time it took to complete the task with AI assistance"

**Sample and aggregation to tasks (pp. 5–6)**

- "Using our privacy-preserving analysis system, we analyzed 100,000 conversation transcripts from Claude.ai (Free, Pro, and Max tiers) to measure the length and time savings of tasks Claude handles."
- "We used Claude to generate these estimates for each conversation. Following our Economic Index methodology, we then aggregated these individual chat conversations to tasks in the O*NET taxonomy by taking the median of time estimates for each task."
- Footnote 1 (p. 21), the outlier and weighting rule: "Claude is prone to produce outlier estimates of both time horizon and cost; for example, it classifies some programming tasks as taking humans years to complete or being valued at millions of dollars. While this is possible, to produce more conservative estimates we take an average of the median value for each task, weighted by the number of conversations in each task."

**Task-level measures (Figure 4 caption, p. 9)**

- "**Task time** is estimated by having Claude predict how long a professional would take to perform the task without AI assistance. **Hourly wage** is derived from the Occupational Employment and Wage Statistics (OEWS) May 2024 data. **Task cost** is computed by multiplying the task time by the hourly wage. **Time savings** is computed by estimating the time the human took to complete the task and computing 1 - time_with_ai / time_without_ai."

**Occupation-level measures (unnumbered table caption, p. 11)**

- "Average hourly wage for the occupational category is retrieved from OEWS 2024 data. Average task cost is computed by multiplying each occupation's hourly wage by its median task time and computing an average weighted by each task's prevalence in our sample. Time savings are computed via 1 - time_with_ai / time_without_ai."

**Distribution measure (Figure 6 caption, p. 13)**

- "Density plot of time savings across O*NET tasks in our sample. We see that Claude's estimated time savings are uneven across tasks in our sample, with most falling between 50 and 95%. The overall median savings is 81%. Time savings are computed by 1 - time_with_ai / time_without_ai. Our estimates do not take into account the time spent refining Claude's output outside of the chat window."

**Validation constructs (pp. 6–7)**

- "**Self-consistency testing:** First, we assess whether Claude produces stable estimates of task lengths across different conversation samples, or across variations in our prompts."
- "We create multiple prompt variations—for example, asking about an 'employee with appropriate skills' versus a 'skilled professional'—to assess how sensitive estimates are to the way the prompt is phrased. We analyze 1,800 conversations with each variant, where users consented to share these conversations with us, and computed correlations across prompt variants."
- Figure 2 caption (p. 7): "Prompt 1 asks Claude to estimate the time it would take an 'employee with appropriate skills' to complete and Prompt 2 asks about a 'human worker' who is 'competent in the relevant field.' The two prompts show a log-scale correlation of 0.89, indicating high agreement. Analysis performed on Claude.ai transcripts where users have consented to share them with us for research purposes."
- "**External benchmarking:** Self-agreement doesn't matter much if a model's predictions don't correspond well to reality. To check this, we tested Claude's time estimation capabilities against a dataset of thousands of real-world software development tasks gathered from JIRA tickets for open-source repositories, with both developer estimates and actual tracked completion times." (pp. 6–7)
- Figure 3 caption (p. 8), on the benchmark's information asymmetry: "Left: correlation with developers' initial time estimates with the final time-tracked outcomes. Developers are familiar with the full codebase and understand the full context behind the request and how long similar tasks have taken. Middle: correlation with Claude Sonnet 4.5's estimates, given just the task title and description of the JIRA ticket. Right: Correlation with Claude Sonnet 4.5's estimates, given 10 examples in the prompt to calibrate on. … Axes are log (base 10) scaled. Error bars are 95% CIs per bin."

**Hulten's theorem and the aggregation (p. 14 and footnotes 2–4, pp. 21–22)**

- "To estimate economy-wide productivity effects, we use Hulten's theorem, a standard method that allows us to aggregate efficiency gains at the task-level to the broader US economy. As in Acemoglu (2024)'s 'baseline' approach, we model the implied increase in labor productivity as a weighted average over task-level productivity gains—a modeling choice that implicitly assumes that capital investment will increase as a result of an increase in total factor productivity (TFP) associated with AI adoption. In this framework, the implied increase TFP is the gain in labor productivity multiplied by the labor share of income." (p. 14)
- Footnote 2 (p. 21), the theorem in full: "Hulten's theorem states that in a competitive equilibrium without distortions, the contribution to total factor productivity of micro-level productivity gains are proportional to that production factor's Domar weight to a first order approximation. A factor's Domar weight is the ratio of its value of gross output to GDP. In the task-based model presented by Acemoglu (2024) a task's Domar weight for labor-intensive tasks is equal to that task's share of the wage bill multiplied by the labor share of income. See Baqaee and Farhi (2019) for a recent treatment and extension of Hulten's Theorem. Formulaically, Hulten's Theorem states the log change in TFP is equal to the Domar-weighted sum over the log change in micro-productivities. In our case, the log change is taken as ln(Completion time without AI) minus ln(Completion time with AI)."
- Footnote 3 (p. 22): "The increase in TFP is more primitive than the increase in labor productivity. Labor productivity is the ratio of output per worker and can increase due to an increase in other factors of production aside from labor even when TFP is unchanged."
- Footnote 4 (p. 22), the labour-share parameter: "Acemoglu 2024 calculates the labor share in AI-exposed industries as 0.57; we use the economy-wide share of 0.6 for simplicity given how close it is."

**The three aggregation inputs (p. 14)**

- "**Task composition:** For each occupation, we obtain a list of work tasks from O*NET. We then use Claude to estimate what fraction of workers' time is spent on each of those tasks."
- "**Task-level productivity improvements:** In the previous section, we provided estimates we can use to compute how much more quickly each task is completed with AI assistance. We take the log difference between time without AI and the time with AI to generate a productivity improvement value, and conservatively assign tasks not observed in our sample a null improvement."
- "**Economy-wide estimate:** We weight each task's implied productivity gains by its economic importance using two factors: (i) the fraction of time that Claude estimates the occupation spends on that task (as above), and (ii) the occupation's share of the total US wage bill (the number of people employed in that occupational category multiplied by the average wage, then divided by total wage bill across all occupations). For the total wage bill, we use May 2024 OEWS data. This approach implicitly assumes the time estimates that Claude produces represent reliable averages across all instances of each task, and that Claude or similar AI systems will be adopted across the entire US economy."
- Figure 7 caption (p. 15), the aggregate measure: "The average ln(time estimate ratio) represents the time-weighted productivity gain across all tasks in each occupation, where time estimate ratio = time with AI / time without AI. Labor statistics derived from OEWS 2024 data."
- The adoption assumption, stated as part of the headline (Figure 7 caption, p. 15): "Claude's estimates imply a 1.8% annualized increase (dotted line) in US labor productivity assuming current AI systems were adopted universally for all tasks we observe"; and in the text (p. 15): "Assuming 10 years for AI to reach universal adoption across the US economy—and using current models".

**Bottleneck construct (Figure 9 caption, p. 18)**

- "Four different occupations along with 'accelerated' tasks that show large potential time savings, and potential 'bottleneck' tasks that do not appear in our sample. For example, software engineers see large estimated time savings in developing and debugging software, but not in supervising programmers. Weekly time fractions are estimated by Claude (see previous section)."

**The prompts — the operational definition of Claude-as-estimator (Appendix, pp. 23–25)**

Quoted from the web rendering, which preserves the closing XML tags that the PDF text layer drops (see `## Verification`).

Human time estimation prompt (p. 23):

```
Human: Consider the following conversation:

<conversation>
{{TRANSCRIPT}}
</conversation>

Estimate how many hours a competent professional would need to complete the tasks done by the Assistant.
Assume they have:
- The necessary domain knowledge and skills
- All relevant context and background information
- Access to required tools and resources

Before providing your final answer, use <thinking> tags to break down your reasoning process:
<thinking>
2-5 sentences of reasoning estimating how many hours would be needed to complete the tasks.
</thinking>

Provide your output in the following format:
<answer>A number representing hours (can use decimals like 0.5 for shorter tasks)</answer>

Assistant: <thinking>
```

Interaction time estimation prompt (p. 24):

```
Human: Consider the following conversation:

<conversation>
{{TRANSCRIPT}}
</conversation>

Estimate how many minutes the user spent completing the tasks in the prompt with the model.
Consider:
- Number and complexity of human messages
- Time reading Claude's responses
- Time thinking and formulating questions
- Time reviewing outputs and iterating
- Realistic typing/reading speeds
- Time implementing suggestions or running code outside of the converesation (only if directly relevant to the tasks)

Before providing your final answer, use <thinking> tags to break down your reasoning process:
<thinking>
2-5 sentences of reasoning about how many minutes the user spent.
</thinking>

Provide your output in the following format:
<answer>A number representing minutes</answer>

Assistant: <thinking>
```

Software development time estimation prompt (p. 25):

```
Human: You are estimating software development tasks for open-source projects. Provide ONLY a number in hours (e.g., 0.3, 1.6, 15). Do not explain.
Task: {task}
Description: {description}:
Estimate (hours):
Assistant:
```

Task time estimation prompt (p. 25):

```
You are estimating how much time workers in the occupation "{occupation_title}" spend on each of their job tasks.

Below is the complete list of tasks for this occupation. For each task, estimate how many hours per week a typical worker spends on it.

Important: Don't worry about making the hours sum to exactly 40 or any specific total - we'll normalize the results afterward. Just give your best estimate for each task independently based on what seems realistic.

Tasks:
{tasks}

Return ONLY a JSON object mapping each task_id to your estimated hours per week, with no additional text, explanations, or commentary. Format:
{{
  "task_id_1": hours,
  "task_id_2": hours,
  ...
}}"""
```

## Data and methods

In the wiki author's words, with references.

**Sample.** 100,000 Claude.ai conversation transcripts drawn from the Free, Pro and Max consumer tiers (p. 5), processed through the privacy-preserving system described in the Clio work (linked as "privacy-preserving analysis system", p. 5). No sampling dates, no country restriction, no user counts, no deduplication rule and no description of how the 100,000 were drawn appear in either version. The separate self-consistency exercise uses 1,800 conversations per prompt variant drawn from users "who consented to share these conversations with us for research purposes" (pp. 6–7) — a different, consent-based sample from the main 100,000.

**Estimator.** Claude is the measuring instrument twice over. For each conversation it produces (i) the hours a competent professional would have needed without AI and (ii) the minutes the user spent with the model; time savings is `1 - time_with_ai / time_without_ai` (Figure 4 caption, p. 9). Both prompts are reproduced above. Claude is used a third time, outside the conversation data, to estimate each occupation's weekly time allocation across its O*NET task list (p. 14). The model behind the 100,000-conversation estimates is not named; Claude Sonnet 4.5 (and, for one comparison, Claude Sonnet 4) is named only in the JIRA benchmark (p. 8).

**Aggregation to tasks.** Conversations are mapped to O*NET tasks "[f]ollowing our Economic Index methodology" (p. 5) — i.e. the task, not the user, determines the occupation — and the per-task statistic is the median of the conversation-level estimates. Footnote 1 (p. 21) adds that the reported occupation-level figures are an average of those per-task medians weighted by the number of conversations per task, adopted because Claude produces outliers of years and millions of dollars.

**Wages and costs.** Task cost is Claude's time estimate multiplied by the OEWS May 2024 average hourly wage of the matched occupation (pp. 9, 10). No wage percentiles, no regional wages, no benefits or overhead loading.

**Aggregation to the economy.** A first-order Hulten decomposition in the Acemoglu (2024) "baseline" form: the log time ratio for each task is the micro productivity gain, and the weight is the product of Claude's estimated within-occupation time share for that task and the occupation's share of the total US wage bill from OEWS May 2024 (p. 14, footnote 2 p. 21). Tasks not observed in the sample get a null improvement, which the note calls conservative (p. 14). The gain is then annualised by assuming universal adoption over ten years (p. 15). TFP is obtained by multiplying the labour-productivity gain by a labour share of 0.6 (p. 15, footnote 4 p. 22). No standard errors, bootstraps or confidence intervals are attached to any aggregate; the only error bars in the document are the per-bin 95% CIs in the validation figure (Figure 3, p. 8).

**Validation.** Two exercises, both bearing only on the *without-AI* human-time estimate. (i) Self-consistency across prompt phrasings: r=0.89–0.93 on log scale, 1,800 conversations per variant (p. 6). (ii) External benchmarking against 1,000 JIRA tickets with tracked completion times, comparing Claude against the developers' own estimates (pp. 7–8). The *with-AI* interaction-time estimate is not validated against anything, and the note says plainly "we lack real-world data to validate the estimates that Claude provides" (p. 19).

**Released data.** None with this note. The only commitment is prospective: "Our Economic Index will track how these estimates evolve over time, and share aggregate datasets that researchers can use to make their own forecasts and conclusions" (p. 6). No dataset link, no code repository, no Hugging Face release and no replication package appears in either version. The four prompts in the Appendix (pp. 23–25) are the only released artefacts.

## Limitations (verbatim)

The document has a section headed "Limitations" (pp. 19–20); its six bullets are quoted in full below, followed by every other passage in which the note bounds its own findings.

**The Limitations section (pp. 19–20)**

- Preamble: "Our approach has several limitations that we think warrant further research on this topic:"
- "**Claude's predictions are imperfect and we lack real-world validation of Claude's time estimates**: AI systems are imperfect predictors, and can't see activity that happens after the user finishes their interaction with the model. While we expect these estimates will improve with models capabilities, using model estimates introduces a significant source of noise. While our estimates show that models are approaching human performance at estimating task times, and humans are far from perfect themselves, we lack real-world data to validate the estimates that Claude provides."
- "**Task taxonomy limitations**: Real jobs are more complex than an O*NET task list, and the time allocations we estimate for each task are only approximate. Many important aspects of work—tacit knowledge, relationships, judgment under uncertainty—don't appear in these formal task descriptions, and the connections *between* tasks may matter just as much or more to productivity as the time savings for those tasks in isolation. While we show large predicted time savings for individual tasks, a recent randomized controlled trial studying end-to-end software features did not see time savings due to AI."
- "**Structural assumptions:** In our calculations above, we compare the time it would take a professional to complete a given task without AI to the time it took with AI. But this could either *understate* the productivity gains – since it takes additional resources we're not accounting for to hire an employee and communicate context, and possibly overstate it, if the quality of the AI's work is worse than a human's."
- "**Restructuring of organizations:** Historically, the largest productivity gains for individual firms have followed from restructuring business operations to adopt new technologies. Our model can help predict the *effects* of such a restructuring, but it cannot predict how companies might decide to restructure, or how quickly this process might happen."
- "**The role of innovation:** Technological innovation is the engine of economic growth. Our model does not capture how AI systems could accelerate or even automate the scientific process, nor the effects that would have on productivity, growth, and the structure of work."
- "**Limited data**: Our dataset is derived from Claude.ai conversations only. This sample is not representative of the full spectrum of AI uses, and there's likely some selection effect where the instances of tasks people use Claude for are the ones they think Claude will be most useful. Additionally, due to our finite sample size, we likely miss some less common AI tasks."

**Caveats stated elsewhere in the document**

- Overview (p. 3): "Our analysis has limits. Most notably, we can't account for additional time humans spend on tasks outside of their conversations with Claude, including validating the quality or accuracy of Claude's work."
- Overview (p. 2): "But this isn't a prediction of the future, since we don't take into account the rate of adoption or what might happen once AI models improve further." (Web wording differs — see `## Verification`.)
- Summary bullet (p. 3): "This doesn't account for the time that humans might spend on these tasks *beyond* their conversation on Claude.ai, however, so we think these estimates might overstate current productivity effects to at least some degree."
- Summary bullet (p. 3): "However, this estimate does not account for future improvements in AI models (or more sophisticated uses of current technology), which could significantly magnify AI's economic impact."
- Validation (p. 8): "However, we observe that Claude's estimates are much more compressed than humans—predicting comparatively long times for shorter tasks, and vice versa—and are overall more prone to overestimates. This suggests that the actual differences in task lengths across tasks may be larger than we report, and that actual task lengths may be slightly shorter."
- Validation (p. 8): "Overall, these findings demonstrate that model predictions have meaningful correlation with real-world outcomes, at least in this domain, making them useful for comparing one task to another or tracking changes over time."
- Task lengths (p. 10): "Given that Claude's time estimates tend to underestimate long tasks and overestimate short tasks, it is possible that these differences might be even greater in practice."
- Costs (p. 11): "Of course, the actual performance of current models will likely be worse than a human expert for many tasks, though recent research suggests the gap is closing across a wide range of different applications."
- Task-level savings (p. 13): "However, our approach doesn't take into account the additional work people need to do to refine Claude's outputs to a finished state, or whether they continue iterating on the work product across multiple sessions—both of which would result in smaller time savings. Past randomized controlled trials have typically found smaller time savings, including 56%, 40%, 26%, 14% and even negative time savings across different applications—perhaps due to these effects or because these studies examined earlier generations of models."
- Figure 6 caption (p. 13): "Our estimates do not take into account the time spent refining Claude's output outside of the chat window."
- Method (p. 14): "This approach implicitly assumes the time estimates that Claude produces represent reliable averages across all instances of each task, and that Claude or similar AI systems will be adopted across the entire US economy."
- Findings (p. 16): "Importantly, this exercise assumes that AI capabilities (and humans' effectiveness in using AI) remain the same over the next 10 years as when we took our sample. This, though, seems unlikely to hold: we think that AI will continue to improve rapidly over the coming years."
- Findings (pp. 16–17): "Therefore, this estimate should be taken as an exercise exploring what might happen based on *current usage patterns,* not a prediction of the impact on productivity that is actually most likely to happen."
- Findings (p. 17): "As models progress, this could represent an approximate lower bound on the productivity effects of AI, although our estimate does not account for unevenness in adoption, which might reduce real-world productivity gains in the short term."
- Findings (p. 17): "In contrast, restaurants, healthcare delivery, construction, and retail contribute much less to the overall productivity effect. This is mostly because few of their tasks appear in our data—largely because these occupations have few associated tasks in our sample."
- Conclusion (p. 21): "Our framework could be used to help estimate the effects of such restructuring, but it cannot predict which changes will occur, or how quickly."

## Open questions, conjectures and promised follow-ups (verbatim)

**Promised follow-ups**

- Overview bullet (p. 4): "This gives us a new lens for understanding how AI's economic impacts over time, which we will track going forward as part of our Economic Index: Computing these estimates based on real-world Claude conversations gives us a new lens to understand AI productivity. This complements other approaches, like lab studies in narrow domains, or government statistics which provide more coarse-grained insights. We will track how these estimates change over time to get an evolving picture of these issues as capabilities and adoption continue to progress."
- Method (p. 6): "Our Economic Index will track how these estimates evolve over time, and share aggregate datasets that researchers can use to make their own forecasts and conclusions."
- Limitations preamble (p. 19): "Our approach has several limitations that we think warrant further research on this topic:"
- Close of Limitations (p. 20): "The measurement infrastructure we develop here enables continuous tracking of the effect of AI on time savings at large scale. As models improve and better methods address these limitations, we can re-estimate these time savings and identify how these capability improvements translate into broader economic impacts. We expect to track these changes in the months and years ahead."
- Conclusion (p. 20): "We'll be tracking these changes over time as part of our Economic Index as model capabilities, products, and adoption continue to progress."
- Conclusion (p. 21): "An important direction for future work is understanding this question—to get a better understanding of when and how firms are reorganizing themselves around emerging AI capabilities. The answer will determine when AI makes the jump from providing significant but bounded productivity boosts, to representing the kind of structural transformation that has historically defined technological revolutions."

**Open questions posed**

- Introduction (p. 4): "How substantial are the tasks for which people use Claude, and how much time does Claude save them?"
- Introduction (p. 4): "Not only that, but as model capabilities improve, we want to understand whether they do higher-value work."
- Conclusion (p. 20): "But what is the aggregate effect of this work?"
- Section heading (p. 17): "How might AI change how workers spend their time?"

**Conjectures and hedged interpretations**

- Overview (p. 3): "But as AI models get better at time estimation, we think our methods in this research note could become increasingly useful for understanding how AI is shaping real work."
- Overview bullet (pp. 3–4): "As AI accelerates some tasks, others may become bottlenecks: We see large speedups for some tasks and much smaller ones in others, even within the same occupational groups. Where AI makes less of a difference, these tasks might become bottlenecks, potentially acting as a constraint on growth."
- Validation (p. 8): "We also observe higher correlation from Claude Sonnet 4.5 compared to Claude Sonnet 4, suggesting that these estimates may continue to improve with model capabilities."
- Validation (p. 6): "AI models have an even more difficult job, since they lack crucial context about the broader context of tasks (though we expect this context to increase over time as features like memory and external integrations become more comprehensive)."
- Task-level savings (p. 12): "For example, the task of checking diagnostic images only shows 20% time savings, likely because this is already a task that can be done quickly by experts without AI assistance. By contrast, the task of compiling information from reports sees approximately 95% time savings, likely because AI systems can read, extract, and cite information much more quickly than people."
- Task lengths (p. 10): "food preparation tasks (e.g. planning or pricing menu items), installation/maintenance, and transportation tasks all take 0.3-0.5hrs on average, suggesting more circumscribed tasks, or tasks with less waiting time."
- Costs (p. 11): "the Management and Legal occupational categories rank at the top of the classification in terms of average hourly wage—aligning with Claude's strengths in complex knowledge work."
- Findings (p. 17): "As we have written about in other work, we remain extremely alert to the possibility that AI causes significant labor market disruptions, which would likely be associated with larger increases in productivity due to AI."
- Bottlenecks (p. 17): "If workers are able to accelerate a subset of their occupational tasks with AI, the tasks where AI provides less speedup may come to represent a larger and thus more important share of those occupations' work. For example, AI might help a home inspector prepare reports, but if the inspector still has to spend the same amount of time physically traveling to the property to perform the inspection in person, this could make inspections a greater fraction of the job overall."
- Bottlenecks (p. 18), quoting Aghion, Jones and Jones: "From a growth perspective, these observations align well with a recent observation from Aghion, Jones, and Jones: 'growth may be constrained not by what we are good at but rather by what is essential and yet hard to improve.'"
- Conclusion (pp. 20–21): "These productivity gains come from making existing tasks faster to complete. Historically, though, transformative productivity improvements—from electrification, computing, or the internet—came not from speeding up old tasks, but from fundamentally reorganizing production. In futures like these, AI not only makes implementing features faster, but companies restructure meetings and code review to validate and ship those features faster, whether using AI or through other means."

## What it did not test

The wiki author's inference from the two fetched documents; not the note's own statements.

1. **The with-AI time estimate is never validated.** Both validation exercises (self-consistency, pp. 6–7; JIRA benchmark, pp. 7–8) test only the *human-alone* time estimate. The denominator of every savings ratio is untested, even though Anthropic holds actual session timestamps for the conversations it sampled and could in principle have compared Claude's minute estimate with observed wall-clock duration. That comparison is not reported.
2. **The external benchmark is one domain and one task type.** JIRA tickets for open-source repositories stand in for all of management, legal, education, healthcare and the rest. No benchmark exists in the note for any non-software occupation, and no test is reported of whether the compression bias measured on software (log slope 0.30) holds elsewhere.
3. **No uncertainty is propagated to the 1.8%.** No confidence interval, no bootstrap over conversations, no sensitivity of the aggregate to: the labour share (0.6 vs Acemoglu's 0.57), median vs mean aggregation, the null-improvement rule for unobserved tasks, the outlier-trimming rule of footnote 1, or the documented compression bias. The headline is a point estimate with no stated precision.
4. **The ten-year universal-adoption horizon is asserted, not varied.** It mechanically sets the annualisation (the same total gain over twenty years halves the annual number). No alternative horizon, no diffusion curve, and no adoption cost is modelled, though the note says adoption unevenness "might reduce real-world productivity gains in the short term" (p. 17).
5. **No output-quality measurement.** The counterfactual assumes the AI-assisted output is the same good as the professional's. Quality is raised as a direction of bias (p. 19) but never measured, scored or benchmarked — not even on the nine example tasks.
6. **The sample's geography is never stated, yet the weights are US-only.** Claude.ai conversations are global; the aggregation uses OEWS employment and the US wage bill (p. 14). The note does not say whether the 100,000 conversations were restricted to the US, nor test whether a non-US task mix biases the US extrapolation.
7. **Consumer surface only, and the note does not test what that omits.** No first-party API, no Claude Code, no enterprise deployments — the surfaces where sustained, agentic, long-horizon work happens. The "Limited data" bullet concedes non-representativeness but no bounding exercise is attempted (for example, re-weighting the task mix to O*NET or to the Index's own task shares).
8. **No general-equilibrium or reallocation analysis.** Hulten's first-order result is applied and its scope conditions ("competitive equilibrium without distortions", footnote 2, p. 21) are neither tested nor discussed. Labour reallocation, price and demand responses, Baumol-type drag from the bottleneck tasks the note itself identifies, and employment effects are all outside the exercise.
9. **The bottleneck claim is illustrated, not quantified.** Figure 9 (p. 18) shows four occupations by hand. The note never computes what share of the wage bill sits in tasks with no observed AI use, nor re-estimates the 1.8% under a specification where bottleneck tasks constrain the whole occupation rather than simply contributing zero.
10. **Tasks unobserved in the sample are assigned zero gain, and the consequences are not bounded.** This is called "conservative" (p. 14), but it also means the estimate is a function of Claude.ai's current task coverage; no alternative (for example, imputing the within-occupation mean savings) is reported to show how much of the 1.8% that choice moves.
11. **No linkage across conversations or sessions.** One conversation is treated as one task instance. Multi-session projects, repeated attempts and abandoned conversations are not identified; the note raises iteration "across multiple sessions" as a bias (p. 13) but does not measure how often it happens in its own data.
12. **Occupation is inferred from the task, not the user, and this is never probed.** The wage-bill weighting presumes that the O*NET-matched occupation is the one whose worker would otherwise have done the task. No test of that mapping — for example against the user's self-reported role, or against the share of consumer conversations that are not work at all — is reported, despite the sample being consumer tiers where much use is personal.
13. **No time series and no model-generation comparison in the conversation data.** Sonnet 4.5 is compared with Sonnet 4 only on the JIRA benchmark (p. 8). Whether estimated savings on real conversations have risen across model releases — the very thing the note promises to track — is not measured here, so there is no baseline trend.
14. **Prompt sensitivity is tested for one of three estimators.** The r=0.89–0.93 self-consistency check covers the human-time prompt only. The interaction-time prompt and the occupation time-allocation prompt (which supplies every weight in the aggregation) have no reported robustness check.
15. **No comparison with the Economic Index's own facets.** Whether estimated time savings differ by collaboration pattern (automation vs augmentation), by request category, or by the Index's task-share ranking is not examined, so the note does not say whether the fastest-saving conversations are the delegating ones.
16. **No replication material.** No data, code or intermediate aggregates are released with the note, so none of its numbers can be recomputed by a reader; the four prompts are the only artefacts.
17. **The comparison with RCTs is rhetorical, not adjudicated.** Five experimental estimates of 56% down to negative are listed (p. 13), and two candidate explanations are offered, but no reconciliation is attempted — for example, re-estimating savings on the subset of conversations most like the RCT tasks.

## Verification

- **Fetched today, 2026-09-16, both in full and read in full:**
  1. https://www.anthropic.com/research/estimating-productivity-gains (web version, including the Appendix prompts, the BibTeX block and all five footnotes).
  2. https://www-cdn.anthropic.com/e5645986a7ce8fbcc48fa6d2fc67753c87642c30.pdf (25 pages, all pages rendered, including the figure images from which the Figure 3, 5, 7, 9 and 10 values and the p. 11 table were read).
- **Fetch failures:** none.
- **Quotation check:** every quotation in `## Definitions (verbatim)`, `## Limitations (verbatim)` and `## Open questions, conjectures and promised follow-ups (verbatim)`, and every number in `## Claims`, was checked against the fetched text of both versions. Page numbers are the PDF's. Nothing is quoted from memory or from `reference/`.
- **Transcription conventions:** apostrophes normalised to straight; markdown hyperlink markup stripped from quotations (the link targets are named in `## Source` and `## Claims`); bold and italic markers inside quotations are preserved where the source emphasises a defined term. No ellipsis appears inside any quotation; no quotation is truncated mid-sentence.
- **PDF text-layer artefact:** in the Appendix prompts the PDF's extracted text drops the leading slash-bracket of closing tags (`</conversation>` appears as `/conversation>`, likewise `/thinking>` and `/answer>`), and renders the JSON ellipsis as `.`; the rendered page images show the tags intact. The prompts in this file are therefore transcribed from the web version, which preserves them, and were checked line-by-line against the PDF page images. The web version also silently repairs the PDF's line-break hyphenations ("open-source", "conversation"); the typo "converesation" is present in both and is preserved.
- **Date discrepancy:** web page header "Nov 25, 2025"; PDF cover "Published: November 5, 2025"; both BibTeX blocks `date = {2025-11-05}`. `wiki/INDEX.md` carries 2025-11-25.
- **Web/PDF wording differences (three, all in narrative text, none affecting a number):**
  1. Overview: PDF "we don't take into account the rate of adoption or what might happen once AI models improve further" (p. 2); web "we don't take into account the rate of adoption or the larger productivity effects that would come from much more capable AI systems".
  2. Conclusion: PDF "we find that current AI use of current models implies a potential increase in US labor productivity of 1.8% per year" (p. 20); web "we find that use of *current* models implies a potential increase in US labor productivity of 1.8% per year".
  3. Bottlenecks: PDF "Figure 9 illustrates this for a few occupations" (p. 17); web "The figure below illustrates this for a few occupations".
- **Web rendering artefact that looks like a numeric discrepancy:** the web text reads "Assuming that labor's share of total factor productivity is 0.64, this implies an overall total factor productivity increase of 1.1% per year." The PDF (p. 15) reads "0.6,4" — the trailing 4 is the superscript marker for footnote 4. The parameter is **0.6**, not 0.64, and 1.8 × 0.6 = 1.08, matching the "implied 1.08% annualized increase in TFP" of the Figure 7 caption (p. 15). The web rendering likewise leaves footnote 4 unanchored in the body text. This file uses 0.6.
- **Internal inconsistencies in the source (arithmetic checks by the wiki author, not claims of the note):**
  1. **Curriculum task cost.** Text: 4.5 hours with "an implied labor cost of $115 based on the average hourly wage of teachers" (p. 10). Figure 4 (p. 9) gives the same 4.5-hour curriculum task at $33/h and $149. 4.5 × 33 = 148.5. The $115 is unexplained.
  2. **Financial analyst task cost.** Text: tasks "that would ordinarily cost $31 in wages" (p. 10). Figure 4 gives 0.8 h at $58/h and a $43 task cost. The $31 is unexplained.
  3. **Three different headline savings.** 80% (Overview p. 2 and summary bullet p. 3), 84% ("median conversation", p. 12), 81% ("overall median savings" across O*NET tasks, Figure 6 caption p. 13).
  4. **Average cost.** $55 (p. 3) against "a median of $54" (pp. 10–11) — described as an average in one place and a median in the other.
  5. **Top-five contributions.** Text (p. 17) ranks "Customer Service Representatives (4%)" above "Secondary School Teachers (3%)"; the Figure 7 table (p. 15) gives secondary school teachers 0.06% and customer service representatives 0.05% of a 1.80% total, i.e. 3.3% and 2.8% respectively, the reverse order. Software developers' 19% checks out (0.34/1.80 = 18.9%).
  6. **Doubling.** "This would nearly double the current long-term growth rate, which has averaged 2.1% per year since 1947 and 1.8% since 2019" (p. 15); the web summary bullet says "This would double the annual growth the US has seen since 2019" (p. 3). An added 1.8 doubles the post-2019 rate but not the since-1947 rate.
  7. **Figure 8.** The caption says "five year moving averages" (p. 16); the chart's own subtitle reads "%oya in Labor Productivity in Nonfarm Business Sector, 15-year moving average".
  8. **Healthcare.** The summary bullet's "healthcare assistance tasks can be completed 90% more quickly" (p. 3) is a task-level figure; the healthcare-support category in the p. 11 table shows 75.9%.
- **Not verified here:** no data file was opened and no number was recomputed from any Economic Index release; the note releases no data with which to do so.
