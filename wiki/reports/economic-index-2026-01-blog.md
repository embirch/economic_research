# Anthropic Economic Index: New building blocks for understanding AI use

## Source

- **Slug:** `economic-index-2026-01-blog`
- **Title on page (H1):** "Anthropic Economic Index: New building blocks for understanding AI use"
- **Title in page metadata (`og:title`, `<title>`):** "Economic Index: New building blocks for AI use" — shorter than the H1; the metadata title drops "understanding".
- **Category label on page:** Economics
- **Date on page:** Jan 15, 2026
- **URL (canonical, as declared in page metadata):** https://www.anthropic.com/research/economic-index-primitives
- **PDF:** none. The page offers "Read the full report", not "Download PDF".
- **Authors:** none named on the page. The blog carries no author block. (The report it summarises names a first author block of Ruth Appel, Maxim Massenkoff, Peter McCrory, and a second block of Miles McCain, Ryan Heller, Tyler Neylon, Alex Tamkin.)
- **Type:** blog companion to the fourth Anthropic Economic Index report. The page states its own function: "You can read the fourth Economic Index report here. Below, we summarize its results."
- **Companion report (separate wiki entry, `economic-index-2026-01-report`):** https://www.anthropic.com/research/anthropic-economic-index-january-2026-report
- **Scope of this file:** what *this page* says. Where the page's wording, numbers or emphasis differ from the full report, a line marked **Report cross-check** records the difference. The report's own content is catalogued in `wiki/reports/economic-index-2026-01-report.md`, not here.
- **Page structure (used as the reference system below; the page has no page numbers and its figures are unnumbered):** untitled introduction → "What we've learned from our economic primitives" → "Tasks" (with three question sub-headings) → "Occupations" ("Coverage", "Task content") → "Aggregate impact" → "Updates on our previous measures" → "Conclusion" → "Footnotes" (three).

### Outbound links the page makes (as evidence of the thread it places itself in)

Within Anthropic: Clio ("analysis method"), the first Economic Index report ("occupation and wage level"), the software-development report ("looked more closely at software development"), the geography report ("by country and by US state"), the productivity-gains paper ("estimated"), the January 2026 report, and the Rwandan government / ALX partnership announcement. Outside Anthropic: METR (organisation and the task-horizons blog post), NBER w32966, Microsoft's *New Future of Work Report 2025*, and Michael Webb's AI-and-patents paper.

---

## Claims

Each claim is given as the page states it, with the page section or figure caption it sits under, and the comparison the number rests on.

1. **More complex tasks are sped up more (Claude.ai).** Section "Tasks" → "Which tasks does AI speed up, and by how much?". Tasks with prompts requiring a high school education (12 years) were "sped up by a factor of 9"; those requiring a college degree (16 years) "by a factor of 12". *Comparison:* 12 years of schooling vs 16 years of schooling, within Claude.ai, at the O\*NET task level. The claim rests on a cross-sectional gradient across task complexity bins, not on any change over time. Figure: "Speedup and success rate vs. human years of schooling" (left panel).
   - **Report cross-check:** the report's Figure 4.1 caption calls this a *binned* scatterplot and the fit "the fit from a linear regression"; the blog's caption for the same image calls it "a scatterplot" and "the line of best fit". The blog drops "binned", which is the fact that each plotted point is a bin average of ~5% of the distribution rather than a task.

2. **The speedup is larger on the API.** Same section, parenthetically: "(On the API, the speedup was greater still.)" *Comparison:* API vs Claude.ai, across the range of task complexity. No number is given on this page.
   - **Report cross-check:** the report gives the reason the blog omits — "This could reflect the nature of the API data, which is restricted to single-turn interactions, and that API tasks have been specifically selected for automation."

3. **Success rate falls as task complexity rises.** Same section. Claude "successfully completes tasks that require a college degree 66% of the time, compared to 70% for those tasks that require less than a high school education". *Comparison:* college-degree tasks vs sub-high-school tasks. Figure: "Speedup and success rate vs. human years of schooling" (right panel).
   - **Report cross-check:** the report attaches "On Claude.ai, for example" to these two numbers. The blog sentence names no platform, so a reader can take 66%/70% as a whole-sample figure. It is Claude.ai only.

4. **The complexity gradient in speedup survives the success adjustment.** Same section: the trend "holds—albeit in weaker form—when we adjust for tasks' success rates", and "Claude's impact on task speedup scales more sharply with complexity than complexity correlates with a decrease in success rate". *Comparison:* the speedup gradient against the success-rate gradient, both taken over human years of schooling. This is a comparison of two slopes, not a level.

5. **Anthropic's inference from claims 1–4.** Same section: "These results imply that AI's productivity gains are currently accruing in tasks that require relatively high human capital, which is consistent with the evidence that white collar professionals are more likely to use AI at work." *Comparison:* the internal complexity gradient against external survey evidence on who adopts AI (linked to NBER w32966). Marked on the page as an implication, not a measurement.

6. **Claude's effective 50%-success task horizon is much longer than METR's benchmark horizon.** Section "Tasks" → "What are the time horizons over which Claude can support tasks?". "METR's benchmark suggests that Claude Sonnet 4.5 (the model in our own analysis) achieves 50% success rates on tasks of 2 hours. By contrast, our own API data finds that Claude is 50% successful at tasks that take nearly twice as long (around 3.5 hours), and on Claude.ai, the duration is vastly longer still—around 19 hours." *Comparison:* three horizons — METR benchmark 2 h, Anthropic 1P API 3.5 h, Anthropic Claude.ai 19 h — for the same model generation. Figure: "Task success vs. human-only time."
   - **Report cross-check, two differences.** (a) The report states the 19-hour figure as an extrapolation: "Extrapolating using the linear fit, Claude.ai would hit a 50% success rate at about 19 hours." The blog states 19 hours without the word "extrapolating", so the page does not disclose that the number lies outside the fitted range. (b) The report gives a second METR comparator the blog omits: "The analogous time estimate in METR's software engineering benchmark is 2 hours for Sonnet 4.5 and about 5 hours for Opus 4.5." The blog cites only the 2-hour Sonnet 4.5 figure, while separately noting Opus 4.5's release in the aggregate-impact section.

7. **Use case shifts with national income.** Section "Tasks" → "How does the nature of Claude's work vary across countries?". "In countries with higher GDP per capita, Claude is used much more frequently for work or for personal use—whereas countries at the other end of the spectrum are more likely to use it for educational coursework." *Comparison:* share of work / coursework / personal use against log GDP per capita, across countries, Claude.ai only. Figure: "Per capita income predicts how Claude is used across countries." No correlation, elasticity or sample size is reported on this page.
   - **Report cross-check:** the report's Figure 3.2 caption states the inclusion rule the blog's caption drops — "We only include countries with at least 200 observations in our sample for this figure because of the uncertainty of the measure for low-usage countries in our random sample."

8. **External convergence for claim 7.** Same section: "These results align with recent work by Microsoft that associates AI use in education with lower per-capita income, and AI use for leisure with higher incomes." *Comparison:* Anthropic's country-level use-case shares against Microsoft's *New Future of Work Report 2025*.

9. **A programme is justified by claim 7.** Same section: the Rwandan government and ALX partnership "is designed with this in mind: participants begin by developing AI literacy, and we're piloting a program for granting some graduates year-long access to Claude Pro, supporting the transition from educational use to a broader range of applications." *Comparison:* none — this is a statement of programme design, offered as the operational response to the income–use-case gradient.
   - **Report cross-check:** this passage is blog-only. The report contains no equivalent link from the income–use-case finding to a named Anthropic access programme. It is the clearest instance on the page of the blog doing work the report does not.

10. **Task coverage has risen from 36% to 49% of jobs.** Section "Occupations" → "Coverage". "In our first report, with data from January 2025, we found that 36% of jobs in our sample saw Claude being used for at least a quarter of their tasks. Pooling data across reports, this has risen to 49%." *Comparison:* the January 2025 first-report figure against a figure pooled across all reports. The two sides of the comparison are constructed differently — one sample vs a pool of samples — and the page does not say so.
    - **Report cross-check:** the report words the 49% the same way ("Combining across reports, 49% of jobs have seen AI usage for at least a quarter of their tasks") and adds a first-report figure the blog omits: "with about 4% reaching 75% task coverage".

11. **Effective coverage reorders which occupations are most affected.** Same section. "some occupations (like data entry keyers and radiologists) are much more heavily affected by AI than task coverage alone would suggest, while others (like teachers and software developers) are relatively less affected." *Comparison:* effective AI coverage (y) against task coverage (x) at occupation level, read against the 45-degree line. Figure: "Effective AI coverage vs. task coverage."
    - **Report cross-check:** the occupations named differ. The report's Chapter 4 names data entry workers, medical transcriptionists and radiologists as moving up, and microbiologists as falling below the line; the report's introduction names "data entry keyers and database architects". Neither passage names teachers or software developers as the below-the-line cases. "Teachers and software developers" appears to be blog-only wording for the report's general observation that high-task-coverage occupations "generally fall below the 45-degree line".

12. **Claude covers tasks requiring more education than the economy's average.** Section "Occupations" → "Task content". Claude is "relatively more likely to cover the tasks that require *higher* education levels—specifically, tasks that require an average of 14.4 years of education (equivalent to a US associate's degree), relative to the economy's average of 13.2". *Comparison:* mean predicted task-level education for Claude.ai-observed tasks (14.4 years) vs all O\*NET tasks weighted by employment (13.2 years). Figure: "Education level of all tasks vs. Claude-covered tasks."

13. **Removing Claude-covered tasks would deskill jobs on average.** Same section. "As a first-order effect, this would *deskill* jobs on average, since it would remove those higher-education tasks. Professions like technical writers, travel agents, and teachers would be affected …, though a rarer few (like real estate managers) would see effects going the other way." *Comparison:* the mean education level of a job's tasks before vs after deleting the tasks observed in Claude.ai data. Explicitly framed as a counterfactual removal exercise, not an observed change.
    - **Report cross-check, two differences.** (a) The report attributes the exercise — "a simple task removal exercise inspired by Autor and Thompson (2025)" — and the blog does not name the antecedent at all. (b) The report's own summary uses "Property managers" for the upskilling case while its Chapter 4 uses "Real estate managers"; the blog uses "real estate managers".

14. **The deskilling result is offered as a signal, not a prediction.** Same section. "We're not necessarily *predicting* that this deskilling will occur … That said, we think this offers a useful signal as to the most immediate effects that AI might have on occupations in the near future." *Comparison:* none; this is a statement about the status of claim 13.

15. **The 1.8pp productivity estimate replicates, including with API data.** Section "Aggregate impact". "Based on our estimates of task speedups alone, we replicated our earlier finding of a 1.8 percentage point increase (even when we added in our API data)." *Comparison:* the new November 2025 sample against the earlier productivity paper's estimate of "1.8 percentage points per year over the next ten years—around double the trend rate".

16. **Adjusting for reliability cuts the estimate to 1.2pp (Claude.ai) and 1.0pp (API).** Same section. "when we adjust our estimate of task-level time savings by the probability that the task is *successful*, our estimate falls by about one-third for tasks completed on Claude.ai (to 1.2 percentage points per year), and by slightly more (to 1.0 percentage points) for the typically more challenging tasks completed on our API." *Comparison:* success-adjusted vs unadjusted aggregation of the same task-level time savings, by platform.
    - **Report cross-check:** same numbers, different characterisation of their size. The blog says the estimate "falls by about one-third"; the report's Chapter 4 introduction says reliability adjustment "roughly halves the implied gains, from 1.8 to about 1.0 percentage points". Both describe 1.8 → 1.2 and 1.8 → 1.0; the blog quantifies the fall against the Claude.ai figure and the report against the API figure.

17. **Even 1.0pp would be historically notable.** Same section. "Even a 1 percentage point increase in annual labor productivity growth would still be notable: it would return US productivity growth to the rates of the late 1990s and early 2000s." *Comparison:* the success-adjusted estimate against the realised US productivity growth rate of the late 1990s / early 2000s.

18. **The estimate is a floor with respect to capability and sophistication.** Same section. The "top-line estimate does not account for the possibilities that AI models become much more powerful, or that the use of AI at work becomes much more sophisticated—which could push the number much higher. Indeed, since our survey, Claude has become substantially more powerful, with the release of Claude Opus 4.5." *Comparison:* the sample period (November 2025, predominantly Sonnet 4.5) against the model available at publication (Opus 4.5).

19. **Task usage remains concentrated and is becoming more so.** Section "Updates on our previous measures". "even though our sample includes 3,000 unique work tasks on Claude.ai, the top ten account for 24% of the set, which has steadily increased from 21% in January 2025." *Comparison:* November 2025 top-ten share (24%) against January 2025 (21%), Claude.ai.
    - **Report cross-check, three differences.** (a) The report says "over 3,000 unique work tasks"; the blog drops "over". (b) "24% of the set" is loose: the report's measure is "the share of conversations assigned to the ten most prevalent O\*NET tasks", i.e. 24% of sampled conversations, not 24% of the 3,000 tasks. (c) The blog's "steadily increased from 21%" compresses the report's series (21% January → 23% August → 24% November) and omits the 1P API series entirely (28% August → 32% November), which the report calls a more notable increase.

20. **Computer and mathematical tasks continue to dominate.** Same section. "computer and mathematical tasks continue to dominate Claude use: they're about a third of all conversations on Claude.ai, and nearly half of our API traffic." *Comparison:* Claude.ai vs 1P API composition, by SOC major group.
    - **Report cross-check — direction of emphasis.** The report gives the same two levels (34% Claude.ai, 46% API) but states that the Claude.ai share is falling: "Such dominance has subsided on Claude.ai: the share … is down from a peak of 40% in March 2025 to 34% in November 2025", while the API share "edged higher from 44% in August to 46% in November 2025". The blog's "continue to dominate" reports the level and drops the divergent trends.

21. **Augmentation has overtaken automation again on Claude.ai.** Same section. "augmentation (52% of conversations) has overtaken automation (45%) as the most popular pattern of interaction with Claude on Claude.ai. This is a reversal of what we saw in our August sample (when automation led by 49% to 47%), but, when we assess this question over a longer time-frame, we still see a slow rise in *automation*'s share of tasks: augmentation led by 55% to 41% in January of last year, and by 55% to 42% in March." *Comparison:* four points in the same series — January 2025, March 2025, August 2025, November 2025 — on Claude.ai. The reversal is the short-run finding; the rise in automation is the long-run one.
    - **Report cross-check — a numerical discrepancy.** The blog gives January 2025 as "55% to 41%". The report gives "In January 2025, augmented use of Claude was dominant: 56% of conversations were classified as augmentation compared to 41% automated." 55% vs 56% for the same quantity. The blog's March figures (55% to 42%) appear only in the report's Figure 1.3, not in its text. Any post using this series should take it from the released data, not from either page.

22. **Geographic concentration persists globally; US states are converging.** Same section. "The US, India, Japan, the UK, and South Korea still lead in overall Claude.ai use, and adoption remains well-explained by GDP per capita. That said, in the US, we've observed greater changes: Claude use has become noticeably more evenly distributed across US states. In fact, if this trend was sustained, our model predicts that Claude use would be equalized across the country within two to five years." *Comparison:* August 2025 against November 2025, globally (unchanged concentration) and within the US (falling concentration), the latter projected forward under a convergence model.
    - **Report cross-check — what the blog leaves out.** The page never names the Anthropic AI Usage Index, the measure the convergence claim is built on; never gives the Gini coefficient fall (0.37 → 0.32) that motivates it; never reports the estimated convergence parameters (OLS β̂ ≈ 0.77, WLS ≈ 0.76, 2SLS ≈ 0.89 / 0.86, of which only some are distinguishable from 1, and the 2SLS pair only at the 10% level); and never carries the report's warning that the estimate "is based on just three months of data" and that "Diffusion may ultimately proceed more slowly in the months and years to come." The blog's "our model predicts" is the strongest form of this claim in either document. It also omits the report's comparison that this pace is "roughly 10x faster than the spread of previous economically consequential technologies in the 20th century" and the report's separate finding that state workforce composition accounts for nearly two-thirds of cross-state AUI variation.

23. **The headline conclusion is unevenness.** Section "Conclusion". "the impact of AI on the global workforce remains a highly uneven one: AI use remains concentrated in specific countries and occupations, and it affects some occupations in a very different way to others, as the evidence on task coverage suggests." *Comparison:* across countries and across occupations, within the November 2025 sample.

24. **This report is a baseline for future comparison.** Section "Conclusion". "this report has given us a new baseline against which to compare our future surveys. As Claude improves, we expect it'll be asked to take on harder tasks, and that it'll likely find greater success." *Comparison:* prospective — this sample against future samples.

---

## Definitions (verbatim)

Quoted exactly as fetched from https://www.anthropic.com/research/economic-index-primitives on 2026-09-16. Emphasis markup in the source (bold and italic) is not reproduced; wording, punctuation and numerals are exact.

**Economic primitives** — body text, section "What we've learned from our economic primitives" (introduced in the untitled introduction):

> "we're introducing what we've called economic primitives: a set of five simple, foundational measurements to track the economic impacts of Claude over time. Our initial set includes task complexity, skill level, purpose (work, education, or personal use), AI autonomy, and success."

**How the primitives are generated** — untitled introduction:

> "We derive these primitives from asking Claude to answer a common set of questions about every conversation in our sample for this report."

**What the primitives are for** — untitled introduction:

> "These primitives provide a leading indicator of AI's potential economic impacts—and allow us to answer far more complex questions about how AI is already changing jobs."

**Task complexity** — Footnote 2(i):

> "Task complexity captures that tasks can vary in their complexity, including how long they take to complete and how difficult they are. A "debugging" task in O*NET could refer to Claude fixing a small error in a function or comprehensively refactoring a codebase—with very different implications for labor demand. We measure complexity through estimated human time to complete tasks without AI, time spent completing tasks with AI, and whether users handle multiple tasks within a single conversation."

**Human and AI skills** — Footnote 2(ii):

> "Human and AI skills address how automation interacts with skill levels. If AI disproportionately substitutes for tasks requiring less expertise while complementing higher-skilled work, it could be another form of skill-biased technical change—increasing demand for highly skilled workers while displacing lower skilled workers. We measure whether users could have completed tasks without Claude, and the years of education needed to understand both user prompts and Claude's responses."

**Use case** — Footnote 2(iii):

> "Use case distinguishes professional, educational, and personal use. Labor market effects most directly follow from workplace use, while educational use may signal where the future workforce is building AI-complementary skills."

**AI autonomy** — Footnote 2(iv):

> "AI autonomy measures the degree to which users delegate decision-making to Claude. Our latest report documented rising "directive" use where users delegate tasks entirely. Tracking autonomy levels—from active collaboration to full delegation—helps forecast the pace of automation."

**Task success** — Footnote 2(v):

> "Task success measures Claude's assessment of whether Claude completes tasks successfully. Task success helps assess whether tasks can be automated effectively (can a task be automated at all?) and efficiently (how many attempts would it take to automate a task?). That is, task success matters for both the feasibility and the cost of automating labor tasks."

**The sample** — Footnote 1:

> "As with previous reports, all our analysis is based on privacy-preserving analysis. Throughout the report we analyze a random sample of 1M conversations from Claude.ai Free, Pro and Max conversations (we also refer to this as "consumer data" since it mostly represents consumer use) and 1M transcripts from our first-party (1P) API traffic (we also refer to this as "enterprise data" since it mostly represents enterprise use)."

**The two platforms** — untitled introduction:

> "Our privacy-preserving analysis method allows us to learn more about conversations on Claude.ai (capturing uses by consumers) and our first-party API (mostly capturing uses by businesses)."

**The measure of task complexity used in the speedup result** — section "Tasks" → "Which tasks does AI speed up, and by how much?":

> "We measure this by what Claude estimates as the number of years of schooling required to understand the conversation's inputs"

**Success-weighting of coverage** — section "Occupations" → "Coverage":

> "once we account for Claude's success rate (which we weight according to how often workers do that task and how long the task takes), we get a different picture of which jobs are most affected by the use of AI."

**Effective AI coverage and task coverage** — figure caption, "Effective AI coverage vs. task coverage":

> "Effective AI coverage tracks the share of a worker's time-weighted duties that AI could successfully perform, based on Claude.ai data. Task coverage is the share of tasks that appear in Claude.ai usage. The dashed line shows where effective AI coverage share equals task coverage."

**Task-level skill measure** — section "Occupations" → "Task content":

> "Using an estimate that we create of the skill level required for each task"

**METR's task horizons** — section "Tasks" → "What are the time horizons over which Claude can support tasks?":

> "METR's measure of AI's task horizons shows that longer tasks are harder for AI models to complete. But the length of time over which AI models can work is steadily increasing as models get better: this measure has now become a key indicator of AI progress."

**Effective time horizon** — same section:

> "Our analysis shows how Claude's effective time horizons might look different to those found in a study with a consistent set of tasks."

**Figure caption, speedup and success** — "Speedup and success rate vs. human years of schooling":

> "The chart on the left shows a scatterplot of the relationship between speedup and human years of schooling, measured at the O*NET task level. The dashed lines show the line of best fit. The chart on the right shows the relationship with the success rate."

**Figure caption, task horizons** — "Task success vs. human-only time":

> "This chart shows the relationship between task success (%) and the time the task would require a human to complete alone, all measured at the O*NET task level and split by platform. The dashed lines show the fit from a linear regression."

**Figure caption, income and use case** — "Per capita income predicts how Claude is used across countries":

> "Each plot shows the relationship between the share of a specific kind of use (work, coursework, or personal) for Claude.ai conversations, and log GDP per capita."

**Figure caption, task education levels** — "Education level of all tasks vs. Claude-covered tasks":

> "The blue bars give the distribution of the predicted task-level education required for all tasks in the O*NET database, weighted by employment. The orange bars show the same, restricting to tasks that appear in Claude.ai data."

### Definitions the page uses but does not give

Recorded here because their absence is a property of the page, not an inference about its content. The page uses **automation** and **augmentation** as headline quantities (claim 21) without defining either, and without listing the five collaboration modes; it uses **speedup** ("sped up by a factor of 9") without stating that speedup is human-alone time divided by human-with-AI time; it uses **task coverage** in the body (claim 10) with the definition appearing only in a figure caption; and it never names the **Anthropic AI Usage Index**, though claim 22 rests on it. A reader who arrives at the released data from this page alone has no construct definitions for automation, augmentation, speedup or the AUI.

---

## Data and methods

In the wiki author's words, with references to the page.

**Sample.** Footnote 1 gives two samples: a random sample of 1M Claude.ai conversations drawn from Free, Pro and Max tiers, called "consumer data"; and 1M transcripts of first-party (1P) API traffic, called "enterprise data". The untitled introduction dates the sample to November 2025 and names the model: "our latest report, which samples conversations from November 2025 (predominantly using Claude Sonnet 4.5)". The page gives no sampling window narrower than the month, no privacy thresholds, no exclusions and no counts beyond the two 1M figures. (The report supplies the window, 13–20 November 2025, the minimum-cell thresholds, and the country and state exclusions; none of this is on the blog.)

**Measurement.** Every primitive is produced by prompting Claude about a transcript — "asking Claude to answer a common set of questions about every conversation in our sample" — inside Anthropic's privacy-preserving pipeline, which the page attributes by link to Clio. The page does not describe the classifiers, their number, their prompts, or the validation procedure; it points elsewhere for all of it: "Our full methodology—including details on how we tested the accuracy of our primitives—is described in chapter two of the full report."

**Unit of analysis.** Most task-level results are stated at the O\*NET task level (figure captions for speedup, success and task horizons all say "measured at the O*NET task level"); coverage and task-content results are stated at the occupation level; the use-case results are at country level. Claim 12's comparison is between two employment-weighted distributions over O\*NET tasks.

**External data brought in.** O\*NET task statements and the employment weighting behind claim 12; national GDP per capita in logs for claim 7; METR's software-engineering task-horizon benchmark as the comparator in claim 6; US historical productivity growth rates as the yardstick in claim 17. The page names none of these sources' vintages.

**Derived measures the page introduces.** Effective AI coverage, defined in a figure caption as the share of a worker's time-weighted duties Claude could successfully perform, built by weighting task success by task frequency and task duration (claim 10's parenthesis and the figure caption). The success-adjusted productivity estimate, built by multiplying task-level time savings by task success probability before aggregating (claim 16). The task-removal exercise, which deletes Claude-covered tasks from each occupation and recomputes the mean task education level (claim 13).

**Figures.** Five figures, all unnumbered and un-cross-referenced in the body — they must be cited by caption. Two are shared with the report as identical image assets (the speedup/success panel pair, and the income-and-use-case triptych) but the speedup panel carries a materially looser caption on the blog, as recorded at claim 1. The task-horizons figure is a different image asset from the report's Figure 4.3, with substantively the same caption.

**Reproducibility from this page.** Nothing on the page is reproducible from the page. It names no dataset, gives no Hugging Face link, and states no column names. Its only data-access statement is in the conclusion: "researchers, journalists, and the public can use our data to inform their own research and thinking". Any replication must go through the report and the release.

---

## Limitations (verbatim)

Quoted exactly as fetched. These are the page's own statements of limitation; no interpretation is added in this section.

On the task-horizon comparison with METR — section "Tasks" → "What are the time horizons over which Claude can support tasks?":

> "But this might not be as discordant as it seems: our methodology is different to METR's in some important ways. In our sample, users can break down complex tasks into smaller steps, creating a feedback loop that allows Claude to correct course. And rather than a fixed set of tasks, our sample contains a form of selection bias: users bring tasks to Claude that they're more confident will work."

On what effective coverage can and cannot show — section "Occupations" → "Coverage":

> "That said, even our revised assessment is still limited: we only assess tasks that are performed on Claude.ai, and it's not always clear how these conversations might map onto changes in the real world."

On the deskilling exercise — section "Occupations" → "Task content":

> "We're not necessarily predicting that this deskilling will occur: it's possible that even if AI fully automated the tasks it currently supports, the labor market would dynamically adjust in ways that this analysis doesn't account for. (Of course, as models improve, the composition of tasks that AI covers will change, too.)"

On the productivity estimate — section "Aggregate impact":

> "as we mentioned in our earlier research, this top-line estimate does not account for the possibilities that AI models become much more powerful, or that the use of AI at work becomes much more sophisticated—which could push the number much higher."

On the model vintage relative to publication — section "Aggregate impact":

> "Indeed, since our survey, Claude has become substantially more powerful, with the release of Claude Opus 4.5."

On the size of the updates to previous measures — section "Updates on our previous measures":

> "Here, we mostly find only small evolutions from the results of previous analyses, which pointed to an uneven distribution of Claude use."

On the conditional status of the convergence projection — section "Updates on our previous measures":

> "In fact, if this trend was sustained, our model predicts that Claude use would be equalized across the country within two to five years."

---

## Open questions, conjectures and promised follow-ups (verbatim)

Quoted exactly as fetched. Grouped by kind; no interpretation is added in this section.

### Promised follow-ups

Section "Tasks" → "What are the time horizons over which Claude can support tasks?":

> "We'll track this indicator in further reports."

Section "Occupations" → "Coverage":

> "This is an area we plan to dig into further in future."

Section "Conclusion":

> "Through our primitives, we'll be able to measure how changes like these are beginning to impact real-world outcomes, including the nature of people's work, and which people (and where) are likely to be most affected during this period of rapid technological transition."

Section "Conclusion":

> "More generally, this report has given us a new baseline against which to compare our future surveys."

### Conjectures and stated expectations

Section "Tasks" → "How does the nature of Claude's work vary across countries?":

> "This fits a straightforward "adoption curve" story, in which lower-income countries show a large share of AI use on education and on a smaller number of work tasks, while AI use diversifies towards personal purposes as countries become richer."

Section "Occupations" → "Task content":

> "That said, we think this offers a useful signal as to the most immediate effects that AI might have on occupations in the near future."

Section "Conclusion":

> "As Claude improves, we expect it'll be asked to take on harder tasks, and that it'll likely find greater success. We also expect that tasks might move from Claude.ai to the API (that is, from predominantly consumers to predominantly businesses) as they become more reliable—and if this happens, it'll give us another possible indication of coming economic impacts, given the importance of business adoption for AI's effect on productivity."

Footnote 3, attached to the deskilling discussion:

> "Indeed, some historical evidence suggests that when technologies automating job tasks appear in patent data, employment and wages subsequently fall for exposed occupations."

### Questions the page poses

Untitled introduction:

> "Is artificial intelligence really making people faster at work? What sort of tasks does AI support best? And how might it change the nature of people's occupations?"

Untitled introduction, on what the fourth report is for:

> "uses our primitives to explore a wide range of questions that we wouldn't otherwise be able to answer—including how Claude's task-level success rates change for more complex tasks, and whether the use of Claude to date might portend a net-deskilling effect on many jobs."

Section headings posed as questions: "Which tasks does AI speed up, and by how much?"; "What are the time horizons over which Claude can support tasks?"; "How does the nature of Claude's work vary across countries?"

### Standing invitation to external researchers

Section "Conclusion":

> "In the meantime, researchers, journalists, and the public can use our data to inform their own research and thinking, and to provide an empirical foundation for the potential policy responses we might need."

---

## What it did not test

The wiki author's inference. Nothing in this section is a quotation or a claim by Anthropic; it is a list of gaps, and where a gap is filled by the full report rather than open in general, that is said.

**Gaps the page shares with the report (genuinely open).**

1. **No outcome data anywhere.** Every result is a property of conversations with Claude, classified by Claude. Nothing on the page is validated against an employment, wage, vacancy, output or hours series. Claims 11, 12 and 13 are exposure constructions; claim 13 is an arithmetic counterfactual on O\*NET task lists. The page's own limitation at "Coverage" concedes the mapping problem ("it's not always clear how these conversations might map onto changes in the real world") but no test of the mapping is attempted.
2. **No test of whether the deskilling result survives an expertise measure other than predicted years of schooling.** Claim 13 is entirely a function of the task-level education predictor. Whether a different skill construct reverses the sign for any occupation is untested here. (The report raises exactly this, noting its measure "differs from Autor and Thompson's expertise concept" and giving an electrician task as a case where the two disagree; the blog omits the caveat, so a blog-only reader would not know the result is construct-dependent.)
3. **No user-level or firm-level analysis.** The unit is a conversation, aggregated to task, occupation or geography. Nothing distinguishes heavy from light users, nor one API customer from another, so none of the concentration claims (19, 20, 22) can be decomposed into adoption breadth versus intensity.
4. **No test of the selection story the page invokes.** The page attributes the 19-hour Claude.ai horizon partly to users bringing tasks "they're more confident will work" (claim 6's limitation), but offers no bound on how much of the Claude.ai-versus-API-versus-METR gap is selection rather than the multi-turn feedback loop. The two explanations it names are not separated.
5. **No causal identification of the income–use-case gradient.** Claim 7 is a bivariate relationship against log GDP per capita, with no controls, no alternative explanation tested (price and payment capacity, connectivity, language, tier mix, VPN use), and no statistics reported.
6. **No test of whether the 36%-to-49% coverage comparison is like-for-like.** Claim 10 compares a single-report figure with a pooled-across-reports figure. Pooling mechanically raises coverage by accumulating rare tasks across samples. The page does not decompose the 13-point rise into genuine growth versus accumulated sample.
7. **No classifier-error propagation into any headline number.** Every number depends on Claude's classification, but no confidence interval, no human-agreement rate and no sensitivity to classifier version appears on the page. The success-adjusted productivity figures of claim 16 multiply two Claude-generated estimates (time saving and success probability) without treating either as measured with error.
8. **No test of the convergence model against a longer series or an alternative functional form** on this page. Claim 22's "two to five years" rests on one three-month change under a proportional-convergence model.
9. **No decomposition of the augmentation reversal.** Claim 21's reversal between August and November 2025 is not attributed to anything on this page — not to product changes, model changes, classifier changes, or user-mix changes.
10. **No treatment of Claude Code, the linked survey, or third-party API traffic.** The page's two platforms are Claude.ai and the first-party API. Claude Code is not mentioned; nor is any survey instrument, despite the page twice calling the sample a "survey".

**Gaps that are artefacts of the blog format, filled by the report.** Recorded because a post that cites this page must not treat these as open: the AUI and the Gini fall behind claim 22; the convergence regression estimates and their precision; the workforce-composition explanation of US state variation; the classifier count, validation procedure and the statement that the primitives are only directionally accurate; the sample window and privacy thresholds; the 1P API task-concentration series; the falling Claude.ai share of computer-and-mathematical work; the CES task-complementarity analysis, which on the report's numbers takes the productivity estimate as low as 0.6–0.8pp under complementarity (σ = 0.5) and as high as 2.2–2.6pp under substitutability (σ = 1.5). That last omission matters most: the blog's lowest productivity figure is 1.0pp, the report's is 0.6pp, and the blog gives no indication that the range is that wide.

**Terminology traps this page sets** (relevant to `/mnt/memory/standards/terminology.md`).

- The page renames two primitives in its body text relative to its own footnote and to the report: "skill level" for *human and AI skills*, and "purpose (work, education, or personal use)" for *use case*. It also shortens *task success* to "success". Quote the footnote or the report, not the body list.
- The page calls the sample a "survey" twice ("since our survey"; "our future surveys"). The Economic Index sample is a random sample of transcripts, not a survey; the Index's survey component is a separate publication. Do not carry this usage.
- The page reports augmentation and automation shares without defining them and without noting that the five collaboration modes are not exhaustive, so 52% + 45% does not sum to 100. A reader could infer a 3% residual category that the page never mentions.
- The page's "our model predicts that Claude use would be equalized across the country within two to five years" is the most assertive statement of the convergence result in either document, and it is the one most likely to be quoted back at us.

---

## Verification

- **Fetched on:** 2026-09-16.
- **URLs fetched:**
  1. https://www.anthropic.com/research/economic-index-primitives — fetched successfully, read in full, including all three footnotes, all five figure captions and the page metadata block. This is the source for every quotation in the `Definitions (verbatim)`, `Limitations (verbatim)` and `Open questions, conjectures and promised follow-ups (verbatim)` sections, and for every claim in `Claims`.
  2. https://www.anthropic.com/research/anthropic-economic-index-january-2026-report — fetched successfully and read, solely to support the `Report cross-check` lines required by this file's remit. Its content is catalogued in `wiki/reports/economic-index-2026-01-report.md` by another thread, not here. The fetched HTML version was truncated after the "Authors & Acknowledgements" heading (159 lines reported truncated), so the acknowledgements list and anything after it were not read; no cross-check in this file depends on that material. The report's linked PDF (https://www-cdn.anthropic.com/096d94c1a91c6480806d8f24b2344c7e2a4bc666.pdf) was **not** fetched.
- **Fetch failures:** none. Both URLs returned content on the first attempt.
- **Quotation check:** every passage inside quotation marks in this file was checked character by character against the fetched text of the URL cited beside it. Source emphasis markup (bold, italics) is not reproduced, and that is stated at the head of each verbatim section; wording, punctuation, hyphenation, em dashes and numerals are as fetched. Where the source itself contains nested quotation marks (footnote 2(iv) on "directive"; the "adoption curve" story), they are reproduced as they appear. No paraphrase appears in any section headed "verbatim".
- **Page defects noted during verification:** the page contains a malformed internal link, `https://www.anthropic.com/research/anthropic.com/research/anthropic-economic-index-january-2026-report` (the domain is duplicated inside the path), used three times — in the "What we've learned from our economic primitives" methodology parenthesis, in the "Task content" cross-reference, and in the "Updates on our previous measures" convergence-model cross-reference. The correct URL is used in the page's other four references to the report. Recorded because anyone re-fetching this page's links will hit three 404s.
- **Reference system:** the page has no page numbers and no numbered figures. References in this file are therefore the page's own H2/H3/H4 section headings and, for figures, the bolded first sentence of the figure caption. This is noted in `Source` and in `Data and methods`.
- **Not verified:** the numbers themselves. Nothing in this file has been reproduced from the released data; every figure is recorded as published. Claims 1, 3, 6, 12, 16, 19, 21 and 22 in particular should be reproduced from the release before any post builds on them, and claim 21's January 2025 augmentation share (55% on the blog, 56% in the report) must be taken from the data rather than from either page.
