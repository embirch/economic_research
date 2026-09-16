# Scenarios for our Economic Future (Econ Scenario Explorer v1.0)

## Source

- **Slug:** `econ-scenarios-explorer-2026-09`
- **Title:** "Scenarios for our Economic Future" (the `<title>` and Open Graph title). The page's own H1 is different: **"What will our economic future look like?"** The tool inside it is named in the disclaimer as "the Econ Scenario Explorer".
- **Type:** Institute post — an interactive, scroll-driven essay wrapped around a parameterised economic model. It is not styled as a report or a paper, has no page numbers, no footnotes, no bibtex block and no abstract, so **every reference below is to a named section or element of the page**, using the page's own headings ("Finding 1: GDP growth", "Disclaimer and thanks to reviewers") or, where a block has no heading, a descriptive name defined at first use.
- **Primary URL:** https://www.anthropic.com/institute/econ-scenarios
- **Published:** the page carries **no dateline**. The only date on it is in the disclaimer block: "v1.0 of the Econ Scenario Explorer, September 2026". `wiki/INDEX.md` records 2026-09-09; third-party coverage fetched during verification also gives 9 September 2026. Recorded as: the day-level date is **not** attested on the page itself.
- **Versioning:** the page states its own version in prose — "The economic scenario explorer is currently Version 1.0." There is no changelog, no corrections block and no prior-version archive.
- **Companion technical report — a separate slug, not summarised here.** The page links "Economic Scenarios for Transformative AI (Korinek et al., 2026)" twice, at https://www-cdn.anthropic.com/files/4zrzovbb/website/cf58f84d46a4a76bf5a5b039ac695fba6b80041c.pdf. See `wiki/reports/econ-scenarios-paper-2026-09.md` (The Anthropic Institute Working Paper No. 2026-02). **The PDF was not fetched in this thread.** Everywhere below that a parameter's provenance points into the report ("NOTE Table 1, sec3 L…"), the pointer is recorded and the content is deliberately left to that file.
- **Other Anthropic pages linked from the body:** https://www.anthropic.com/economic-index (the Index, set against this tool — see `Claims` 2); https://www.anthropic.com/institute/recursive-self-improvement; https://www.anthropic.com/economic-futures ("the research Anthropic funds"); and a policy PDF linked twice, from "we can take steps" and from "the policy ideas we propose", at https://www-cdn.anthropic.com/files/4zrzovbb/website/9ea607a5dd67c168093829b701f3a0a6d21156d5.pdf. The last three belong to `wiki/reports/programme-and-product-pages.md`; none was fetched here.
- **"Read blog" is not a link.** The hero shows three affordances: "Read technical report" (a link to the PDF), "Jump to explorer" (an in-page scroll button) and "Read blog" (a `scrollHint` button with no `href`). **There is no companion blog post**; the string is a scroll cue, and a reader hunting for a separate blog will not find one.
- **Credits (verbatim, closing paragraph of the disclaimer):**
  > "Anton Korinek, Chad Jones, Szymon Sacher, Tess Cotter, and Peter McCrory developed the economic model and co-authored the companion technical report. Santi Ruiz wrote this piece with them, with editorial support from Sarah Pollack and Adam Farina. Kelsey Nanan designed and built the interactive experience, with visual design and art direction by Nikki Makagiansar and Monika Tuchowska; Kyle Turman and Szymon Sacher built the scenario explorer and led the translation of the model into interactive form; Fayaz Ashraf and Ryan Heller contributed engineering, and Kim Withee and Maria Gonzalez supported production. Szymon Sacher and Tess Cotter designed and fielded the accompanying surveys with Morning Consult, with support from Ben Fowler. Peter McCrory, Anton Korinek, and Charles Yang coordinated the project, and Jack Clark provided direction throughout. Miriam Chaum, Jack Clark, Saffron Huang, Maxim Massenkoff, and Peter McCrory helped originate this effort. Jim Baker, Shan Carter, Johannes Hermle, Zoë Hitzig, and Eva Lyubich provided feedback."

  **The mentor is named here** — "Maxim Massenkoff … helped originate this effort" — and nowhere else on the page. He is not an author of the model or the report.
- **Terms it introduces or fixes into the Anthropic economics vocabulary:** *modest / substantial / extreme scenario*; *knowledge workers* against *all other workers*; *displaced* / *crossed over* / *still there* / *still need to move*; *tasks unchanged / augmented / automated / new tasks created by AI*; *job reallocation*; *labor share* against *capital share*; *Econ Scenario Explorer*. Note that "knowledge worker" here is a **two-way partition of all US employment**, not an exposure score; see `Definitions`.

### Three kinds of material on this page, and how each is marked

This entry draws on three layers, which the page does not distinguish and a post building on it must:

| Layer | What it is | Marking used below |
|---|---|---|
| Page prose and headings | Server-rendered text, identical in the rendered fetch and the raw HTML | unmarked |
| Figure data labels | Values printed as `<text>` inside the server-rendered SVG of the job-reallocation figure | **`(figure label)`** |
| Survey chart payload | The JSON object the page ships to draw the five survey distributions (React Flight payload, not a separate file) | **`(chart data asset)`** |
| Explorer model bundle | The model's calibration, scenario presets and quiz wording, shipped in the page's JavaScript chunk | **`(explorer bundle)`** — a new marking; a ruling is requested in `room/lead-2026-09-16-wiki-econ-scenarios-explorer-2026-09.md` |

`(figure label)` follows `room/director-2026-09-16-figure-values-ruling.md`. `(chart data asset)` follows `room/director-2026-09-16-chart-asset-ruling.md`; the only difference from the precedent case is that this page's chart data is embedded in the page payload rather than served as a separate `.json` file, which if anything makes it *more* clearly part of the published page. `(explorer bundle)` goes beyond both rulings and is flagged, not assumed — see `Verification`. **No number in this file was read off a chart image**, and three of the page's four findings are illustrated by charts that render client-side with no values in the source at all (see `Verification`).

## Claims

Numbers are reproduced as published. Every claim names the comparison it rests on. The unit of argument on this page is almost never a level: it is **one scenario against another**, or **a scenario against the same economy without AI**, and the page is explicit that this is a counterfactual gap, not a forecast.

### Framing and standing

1. **What the tool is for.** "Anthropic's Economics team built a model of how AI might affect jobs, growth, and unemployment in the US in coming years. Read about possible economic futures and make your own predictions about AI capabilities to see the economy they imply." (hero). *Comparison:* a user's own parameter settings against the three published presets.

2. **Where it sits relative to the Economic Index — the load-bearing sentence for our programme.** "While our [Economic Index](https://www.anthropic.com/economic-index) measures how AI is being used across the economy right now, this scenario explorer is about looking ahead." (opening section). *Comparison:* measured present usage against modelled future outcomes. This is the page's own statement of the division of labour between the Index and this model, and it is the only place the Index is mentioned. The page does **not** say that the Index feeds the model; the model bundle says it does, at one parameter (see `Data and methods`).

3. **The headline range, stated before any number.** "In scenarios ranging from business as usual to an economy where AI increases growth to about twice the normal rate, unemployment stays within the historical range and wages remain flat or rise depending on the industry. But in scenarios where growth is faster than anything in economic history, there are adverse impacts on wages and job prospects for knowledge workers. In those scenarios, society is far wealthier, so the challenge is making sure that the gains are broadly shared." (opening section). *Comparison:* the modest-to-substantial band against the extreme scenario, on two outcomes at once (unemployment, wages). Note what is being conceded: the page's own summary says the disruption story only appears in the scenario it describes as unprecedented.

4. **The size of the object being modelled.** "Today, if you add up every single instance of tasks performed in the US, by people and by the machines and software they work with, you get the US economy: over $30 trillion of value created over the past year." (§"From tasks to the economy"). *Comparison:* none; a scale anchor for the GDP levels that follow.

5. **The task taxonomy's source.** "Each of the tasks listed are based on the US Department of Labor's O\*NET taxonomy, listing the tasks for each occupation." (§"The economy is made out of tasks", nurse walk-through). *Comparison:* none; a provenance statement. **This is the page's only named external taxonomy**, and it is attached to the *illustration*, not to the model's calibration — the model's occupational data are CPS/OEWS/IPUMS (see `Data and methods`).

### The three scenarios, as characterised in prose

6. **Modest.** "In the modest scenario, it's hard to see the effect of AI in macroeconomic data: its economic impact is something like the internet's." and "It drives real economic gains, but they're within the historical norm for new technologies, and they arrive gradually." (§"There are many possible futures…"). *Comparison:* AI against the internet, and against "the historical norm for new technologies".

7. **Substantial.** "In the substantial scenario, AI is capable of doing half of all knowledge work by 2030, the majority of it autonomously, but it's not adopted for all of that work: most knowledge work tasks are still done without AI. The economy grows at twice its normal rate. Wages for knowledge workers don't rise, but other workers see gains." *Comparison:* capability against adoption (the page's central distinction), and knowledge workers against other workers. Also "AI makes a bigger impact than the internet, or the railroad."

8. **Extreme.** "In the extreme scenario, AI is more productive than humans at the vast majority of knowledge-work tasks. It does nearly all of them autonomously, and it creates essentially no new knowledge tasks for people. This scenario would likely require recursively self-improving AI, adopted quickly for knowledge work." *Comparison:* against the other two scenarios on three dials at once (capability, autonomy, new-task creation).

9. **The extreme scenario's growth rate.** "As AI diffuses, annual GDP growth rates reach **15**% a year, leading the economy to double in size every **4.5** years. As a society, we're far richer than we've ever been, but many fewer workers have jobs in knowledge work, and unemployment has risen beyond typical recessionary levels." *Comparison:* against "typical recessionary levels" of unemployment, and against any historical growth rate. The two numbers are rendered as separate inline spans, computed by the model at page build; the doubling time is the arithmetic consequence of the growth rate.

### Finding 1 — GDP

10. **GDP levels and gaps by scenario** (§"Finding 1: GDP growth", the waterfall figure; chart title "US GDP in 2030, by scenario (measured in trillions of dollars)\*"):

| Scenario | GDP gap in 2030 | GDP level in 2030 |
|---|---|---|
| Modest | **+1.6%** | *$34.1T GDP* |
| Substantial | **+8.3%** | *$36.3T GDP* |
| Extreme | **+32.4%** | *$44.4T GDP* |

*Comparison:* each scenario against **the same economy in 2030 without AI** — this is a counterfactual gap, not a growth rate over 2026. The figure decomposes each bar into four components named in its key: "Tasks augmented", "Tasks automated", "New tasks created by AI", "Productivity". The footnote reads "\*GDP is calculated at 2025 price levels". The component magnitudes are drawn client-side and are **not** in the page source.

11. **The finding sentence.** Heading: "AI grows the economy in every scenario, but some more than others"; body: "AI drives GDP growth in all scenarios, although the scale varies enormously depending on the scenario." *Comparison:* the dispersion across scenarios treated as the finding, rather than any one level.

12. **The pivot away from GDP, stated immediately.** "But growth isn't the only economic dynamic we care about. What would these potential futures mean for how much of this growth workers receive in their paychecks, or how many people have to find new jobs?" and "This model isn't a complete map of reality, but it shows us some interesting findings. The country's GDP will grow, but a larger share of that prosperity might go to the resources and technology used to create more wealth (capital) compared to workers, even if society as a whole is much wealthier." *Comparison:* aggregate growth against its distribution. This is the page's editorial thesis and it is placed before the distributional evidence, not after.

13. **The one-exception framing for unemployment.** "And in most scenarios, job reallocation and unemployment both stay within ranges history has seen before, with one exception. In the extreme scenario, if we see recursive self-improvement and rapid adoption, unemployment could spike to historic levels." *Comparison:* modelled unemployment against the historical range of US unemployment. No historical range is quantified anywhere on the page.

### Finding 2 — job reallocation

14. **The reallocation figure, substantial scenario** (§"Finding 2: Job reallocation"; chart title "Where workers are in 2030 (percent of all workers)"; figure `aria-label` "the share of all workers in each place in 2026, in transit, and in 2030"). The figure has a three-way toggle, **Modest / Substantial / Extreme, and ships with Substantial pre-selected** (`aria-pressed="true"`); the values below are therefore the substantial scenario's, and the modest and extreme versions are computed client-side and are not in the source.

| Node | Value | Column |
|---|---|---|
| Knowledge workers | **62.2%** *(figure label)* | 2026 |
| All other workers | **37.8%** *(figure label)* | 2026 |
| Displaced | **2.5%** *(figure label)* | in transit |
| Crossed over | **1.8%** *(figure label)* | in transit |
| Still there | **59.7%** *(figure label)* | 2030 |
| All other workers | **39.6%** *(figure label)* | 2030 |
| Still need to move | **0.7%** *(figure label)* | 2030 |

*Comparison:* the 2026 stock against the 2030 stock, with the flow between them shown as a middle column; all as percentages of **all** workers. The key names three states: "Knowledge workers", "All other workers", "Displaced". Note that 62.2% is also the published base-period share of the cognitive group in the model's calibration (see `Data and methods`), so this figure's left column is a calibration input, not a model output.

15. **The finding sentence.** "In more transformative scenarios, more workers have to change occupations. That may mean higher unemployment." *Comparison:* across the three scenarios, on the amount of occupational switching required. Note the hedge in "may".

16. **Churn is normal; the claim is about its scale.** "There is always some churn in the job market—people losing jobs and finding new ones. In normal times, this process can be painful, but works relatively well from a macroeconomic perspective. Most job seekers find new jobs fairly quickly." *Comparison:* the modelled reallocation against normal-times churn. This sentence is doing the work of setting the null.

17. **Who moves where, at the individual level.** "In our substantial and extreme scenarios, knowledge workers may see a lot of automation and displacement. At the individual level, it means coders and call service center agents may have to switch to jobs like electrician and nurse, which are less exposed to AI." *Comparison:* named exposed occupations against named unexposed ones. **This is the page's only occupation-level statement**, and it is illustrative: the model has two groups, not occupations (see `Definitions`). Note the tension with the nurse walk-through that opens the page, where the nurse's own job is substantially reshaped by AI.

18. **The mechanism that turns switching into unemployment.** "But changing occupations entirely is hard, and it takes many people a long time to land a new job. The more of this switching a scenario requires, the more people will be between jobs." and "Switching to a new occupation is difficult for a few reasons: workers may not want to change occupations. They may need to learn new skills. And even when they do, it's not easy to get a new job. In the extreme scenario, as large swathes of knowledge work are automated more quickly, affected workers may be unemployed for a prolonged period." *Comparison:* switching volume against duration between jobs. Three distinct frictions are named in prose (preference, skills, matching); the model represents them through search parameters, not separately (see `Data and methods`).

19. **The direction of the employment shift.** "As we progress from 2026 to 2030, the number of jobs available in occupations AI affects (knowledge work) decreases, while the jobs available in occupations AI doesn't affect increase." *Comparison:* the two groups' employment, moving in opposite directions. Recorded because it is the page's clearest statement that the model's labour-demand effect is a **reallocation between two groups**, not a net level effect.

20. **The unemployment chart, with no values.** Chart title: "Unemployment in knowledge work rises; in other occupations, it falls"; three panels, "modest scenario", "substantial scenario", "extreme scenario"; key: "Knowledge workers", "All other workers", "Total". *Comparison:* the two groups' unemployment paths against each other and against the total, in each scenario. **No axis labels, no data labels and no values of any kind appear in the page source** — the panels are empty frames server-side. Nothing is recorded from this figure beyond its title and key. This is the page's central labour-market result and it is published only as a picture.

### Finding 3 — wages

21. **The finding sentence.** "Across the three scenarios, average wages rise, but this increase is concentrated in occupations outside of knowledge work." *Comparison:* the average against its composition — an explicit warning that the aggregate hides the split.

22. **The mechanism, in the page's own words.** "That's because it takes time for workers to switch to occupations where demand is rising. If there's less demand for human knowledge work, that puts downward pressure on wages. Meanwhile, as AI increases productivity within knowledge work, the demand for manual work that benefits from that productivity will increase. For example, more quickly producing designs and permitting for physical infrastructure could increase the number of construction projects, resulting in rising demand for construction workers, which pushes those wages higher." *Comparison:* falling demand for cognitive labour against rising derived demand for complementary manual labour. The construction example is the page's only worked channel.

23. **The two quantified wage statements.** "In the substantial scenario, wages for knowledge workers are essentially flat. In the extreme scenario, they fall by more than 10% by 2030." *Comparison:* knowledge-worker wages against the same economy without AI ("percent above the same economy without AI", per the chart title). "More than 10%" is the **only** wage magnitude published on this page; the precise figure and the other-worker figure are in the technical report, not here.

24. **The wage chart, with no values.** Chart title: "Pay by occupation group, percent above the same economy without AI"; three panels, "modest scenario", "substantial scenario", "extreme scenario"; key: "Knowledge workers", "All other workers", "Average". *Comparison:* three series against a no-AI counterfactual, in each scenario. **As with the unemployment chart, no values are in the page source.**

### Finding 4 — labour and capital shares

25. **Today's split, as the page states it.** "Today, of each dollar the economy produces, about **60**¢ goes to workers and **40**¢ go to capital." *Comparison:* the base period against the scenarios. The 60/40 split is a model parameter (base-period labour share s_L = 0.6), not an estimate produced here.

26. **The mechanism.** "If the economy grows, but AI automates more tasks, more of each dollar might go to capital. This can happen even when wages for all workers rise substantially. If capital becomes more useful for more things, it will be in higher demand, which raises its price. In that world, more of the gains from a growing economy flow to owners of capital." *Comparison:* the level of wages against labour's share — the page is careful that these move independently.

27. **The factor-share figure** (chart title "How GDP is shared between workers and capital"; same four-part key as the GDP waterfall):

| Scenario | GDP | To labour | To capital |
|---|---|---|---|
| Modest | *$34.1T GDP* | **59.4**% *to labor* | **40.6**% *to capital* *(up 0.6 points)* |
| Substantial | *$36.3T GDP* | **56.1**% *to labor* | **43.9**% *to capital* *(up 3.9 points)* |
| Extreme | *$44.4T GDP* | **45.2**% *to labor* | **54.8**% *to capital* *(up 14.8 points)* |

*Comparison:* each scenario's factor shares against the base-period 60/40, with the capital-share change stated in points. In the extreme scenario the shares cross: capital takes the majority.

28. **The summary of the finding.** "We find that the labor share falls noticeably in the substantial and extreme scenarios, and the capital share rises. Average wages rise—non-knowledge workers are paid much more—but wages for knowledge workers stagnate or decline alongside worsening unemployment." *Comparison:* factor shares against wage levels against unemployment, all at once — the page's fullest statement of its own result.

29. **The distributional close, and the sharpest sentence on the page.** "In the extreme scenario, the gains from a rapidly expanding economy are unevenly distributed. Most knowledge workers face either lower wages or unemployment, and workers overall get a smaller fraction of the larger pie. **Total labor income is barely changed by 2030.**" *Comparison:* total labour income under the extreme scenario against the no-AI path — i.e. a 32.4% larger economy delivering approximately nothing in aggregate to labour. No number is attached.

30. **The policy framing that follows from it.** "In this scenario, the main challenge is not achieving economic growth, but making sure the benefits are broadly shared and the costs aren't unequally dispersed." *Comparison:* a growth problem against a distribution problem. Repeated from the opening section, and it is the page's thesis.

31. **The restatement under the figure.** "With each scenario, the total economy grows (measured in GDP). But more of the growth goes to capital, compared to the amount people receive in their wages. Some professions see their wages increase significantly, but overall, wages make up a smaller share of the country's economic growth." *Comparison:* growth against its factor split; recorded because it is the caption-position gloss and a post quoting the shares should quote this alongside them.

### The survey

32. **The survey's scale and subject.** "In August, we surveyed more than 10,000 Americans about their views on present and future AI capabilities, adoption, and the ease of finding new work if they have to change occupations." (§"People's expectations about future AI capabilities vary."). *Comparison:* public expectations against the model's scenarios. The year is **not stated** in this sentence; the survey payload gives "Survey of U.S. adults, August 2026" **(chart data asset)** and the credits name Morning Consult as the field house.

33. **The survey's headline result — what the public's beliefs imply when run through the model.** "The typical respondent's answers imply outcomes close to the 'substantial change' scenario: GDP is 10% higher by 2030 than it would be without AI, and the overall unemployment rate has risen to around 5%. Around 10% of respondents have views in line with the extreme scenario." *Comparison:* the typical respondent's implied outcome against the three presets, and the extreme-leaning tail against the whole. Note that **"substantial change"** appears in quotation marks here and nowhere else; the scenario is called "substantial" everywhere else on the page. Note also that this is not a survey result about GDP: respondents were asked about capability, adoption, autonomy, productivity and job-finding time, and the GDP and unemployment numbers are the **model's** output from their answers.

34. **The two cohorts and their sizes** (the card under the survey chart):
    - "General public — n = **10,980**" *(chart data asset: `n: 10980`, label "General public", framing "fielded", source "Survey of U.S. adults, August 2026")*
    - "Site visitors — n = **27,148**" *(chart data asset: `n: 27148`, framing "self-selected", source "Readers of this page who took the quiz")*

    *Comparison:* a fielded probability-style sample of US adults against self-selected readers of this page, on identical questions. **The site-visitor count is live and rises as people use the page:** the rendered fetch taken minutes before the raw fetch gave 27,143, the raw fetch 27,148. Any post quoting it must give the timestamp.

35. **The five survey questions, as labelled on the page.** The chart title is "How people answered the five questions (share of respondents at each answers)" (the grammatical slip "at each answers" is in the source). The five, with the page's short labels:

| Category | Short question (page) | Answer scale (page) |
|---|---|---|
| Capabilities | "What tasks can AI do?" | continuous, poles "0%" and "100%" |
| Adoption | "How much do people use AI?" | continuous, poles "0%" and "100%" |
| Autonomy | "How much does AI do by itself?" | "Almost none / Some of them / About half / Most of them / Almost all of them" |
| Productivity | "How much more productive does AI make people?" | "Same / 1.5× / 2× / 4× / 10×+" |
| Adjustment | "How long does it take people to find a new job?" | "1–2 months / ~3 months / ~6 months / ~9 months / A year / 2 years / 3+ years or never" |

*Comparison:* the two cohorts' answer distributions against each other, question by question. The full question wording is not on the page; it is in the explorer bundle (see `Definitions`).

36. **The published answer distributions for the three ordinal questions (chart data asset).** Shares of each cohort at each option, as shipped:

| Question | Option | General public | Site visitors |
|---|---|---|---|
| Autonomy | Almost none | 0.1666 | 0.0057 |
| | Some of them | 0.2191 | 0.0601 |
| | About half | 0.3637 | 0.1842 |
| | Most of them | 0.1444 | 0.5515 |
| | Almost all of them | 0.1061 | 0.1984 |
| Productivity | Same | 0.2951 | 0.0175 |
| | 1.5× | 0.2160 | 0.1824 |
| | 2× | 0.2472 | 0.2495 |
| | 4× | 0.1516 | 0.3460 |
| | 10×+ | 0.0901 | 0.2047 |
| Adjustment | 1–2 months | 0.1481 | 0.0184 |
| | ~3 months | 0.1272 | 0.0550 |
| | ~6 months | 0.2249 | 0.2585 |
| | ~9 months | 0.0959 | 0.1479 |
| | A year | 0.1108 | 0.2448 |
| | 2 years | 0.1971 | 0.1280 |
| | 3+ years or never | 0.0960 | 0.1473 |

*Comparison:* fielded public against self-selected readers. The gap is large and systematic in one direction — site visitors are far more bullish on autonomy and productivity — which is the page's own evidence for how unrepresentative its readership is, and which the page never remarks on. The capability and adoption questions ship as 101-bin densities over 0 to 1 **(chart data asset)** rather than discrete options; those are not tabulated here.

37. **Per-question respondent counts differ from the headline n, and from each other (chart data asset).** The payload carries a `counts` field per question:

| Question | General public | Site visitors |
|---|---|---|
| Capability | 8,904 | 27,148 |
| Adoption | 4,664 | 27,148 |
| Autonomy | 4,216 | 27,148 |
| Productivity | 8,474 | 27,148 |
| Adjustment | 4,480 | 27,148 |

*Comparison:* none is drawn by the page. **Every one of the five is below the headline n = 10,980, and they differ by a factor of more than two between questions**, which is the signature of a split-sample or routed instrument rather than item non-response. The page never mentions this: it prints one n on the card and five different denominators underneath it. Flagged, not resolved — the instrument's design is not published, and this belongs to the technical report or an unpublished appendix.

### The close

38. **Indeterminacy stated as the conclusion.** "The future is not predetermined." and "Ultimately, what the economy looks like in 2030 depends on many factors, like what AI can do, and how companies and workers choose to adopt it. It also depends on how the financial benefit of this technology is shared." *Comparison:* technology against choices — capability, adoption and distribution given equal billing.

## Definitions (verbatim)

All quotations are the page's own words unless marked. References are to section headings.

### What the model is

**The task representation (§"The economy is made out of tasks"):**
> "This model represents all the jobs people do in the economy as bundles of tasks. AI can help people do a given task better or faster. It can automate the task. It might not affect the task at all. And it can lead to new tasks."

**The four task types** — four separate key labels above the nurse illustration, each quoted individually: "Tasks unchanged by AI"; "Tasks augmented"; "Tasks automated"; "New tasks created by AI".

The GDP and factor-share figures carry a different five-label key: "Task types"; "Tasks augmented"; "Tasks automated"; "New tasks created by AI"; "Productivity" — i.e. the decomposition on those figures adds "Productivity" and drops "Tasks unchanged by AI".

**Augmentation, defined by example (§"Some tasks will get augmented"):**
> "AI helps a human do them better, or faster. AI helps the nurse draft discharge instructions, monitor patients remotely, and plan the shift's care schedule."

**Automation, defined by example (§"Some tasks may get fully automated"):**
> "For instance, AI may chart a patient's vitals, or order the ward's supplies."

**New tasks, defined by example (§"And new tasks will appear"):**
> "Historically, new technologies have also created new tasks for workers. For a nurse, that might be checking how well an AI triages patients, or reviewing an AI-proposed care plan."

**Tasks only humans do (§"Only humans can do some tasks"):**
> "For instance, AI can't bathe a patient."

**Task bundles are not static (§"Jobs change over time"):**
> "Tasks leave the bundle (hardly anyone hand-writes paper charts anymore) and new tasks arrive (30 years ago, no one monitored patients remotely). The bundle of tasks isn't static, and the job changes as tasks change."

**From task to aggregate (§"Every task happens millions of times every day, across the country" and §"From tasks to the economy"):**
> "Nurses are doing their work on every ward and on every shift. As more nurses use AI, AI supports a higher percentage of these millions of instances of each task."

> "Today, if you add up every single instance of tasks performed in the US, by people and by the machines and software they work with, you get the US economy: over $30 trillion of value created over the past year."

**The four questions the model turns into outcomes (§"From tasks to the economy"):**
> "The answer depends on how AI affects all the tasks that make up the economy, the new tasks it creates, and how fast AI takes on this work. Will AI lead to more task augmentation or automation? How much more productive will it make us? How quickly will it be adopted by workers and companies? The answers to these questions have direct effects on GDP, the labor market, and the share of the pie taken home by workers."

**The task taxonomy behind the illustration (§"The economy is made out of tasks"):**
> "Each of the tasks listed are based on the US Department of Labor's O\*NET taxonomy, listing the tasks for each occupation."

### The three scenarios

**What a scenario is (§"There are many possible futures, but we're highlighting three scenarios"):**
> "The future will depend on how AI's capabilities advance, and how industries and workers adopt those capabilities. The three scenarios we share capture distinct kinds of impact."

**Modest:**
> "In the modest scenario, it's hard to see the effect of AI in macroeconomic data: its economic impact is something like the internet's."

> "In the modest scenario, AI has roughly the same kind of impact as the internet did. It drives real economic gains, but they're within the historical norm for new technologies, and they arrive gradually."

(The lead-in phrase above this paragraph is "Small economic gains".)

**Substantial:**
> "In the substantial scenario, AI makes a bigger impact than the internet, or the railroad."

> "In the substantial scenario, AI is capable of doing half of all knowledge work by 2030, the majority of it autonomously, but it's not adopted for all of that work: most knowledge work tasks are still done without AI. The economy grows at twice its normal rate. Wages for knowledge workers don't rise, but other workers see gains."

(Lead-in: "A revolution in knowledge work". Called "substantial change" once, in §"People's expectations…".)

**Extreme:**
> "And in the extreme scenario, AI drives a completely transformed, unprecedented economy, likely driven by recursively self-improving AI systems and a faster rate of AI adoption."

> "In the extreme scenario, AI is more productive than humans at the vast majority of knowledge-work tasks. It does nearly all of them autonomously, and it creates essentially no new knowledge tasks for people. This scenario would likely require recursively self-improving AI, adopted quickly for knowledge work."

(Lead-in: "A profound economic transformation".)

### The groups and the outcome measures

**"Knowledge workers" is never defined in prose.** The term carries the whole of Findings 2 and 3 and the page gives it no definition, no occupation list and no source. The nearest thing to a gloss is the parenthesis in §"Finding 2":
> "the number of jobs available in occupations AI affects (knowledge work) decreases, while the jobs available in occupations AI doesn't affect increase"

i.e. **knowledge work = the occupations AI affects, by construction**, and "all other workers" is its complement. The two-way partition is defined in the model bundle, where the group is called *Cognitive* and is a list of SOC major groups:
> "Cognitive occupations (SOC 11–29, 41, 43: management, professional, sales, office)" **(explorer bundle)**

with member major groups "Management", "Business and financial operations", "Computer and mathematical", "Architecture and engineering", "Life, physical, and social science", "Community and social service", "Legal", "Education, training, and library", "Arts, design, entertainment, sports, and media", "Healthcare practitioners and technical", "Sales and related", "Office and administrative support" **(explorer bundle)**. The complement group is named *Other*:
> "All other occupations (SOC 31–39, 45–53: service, farming, construction, maintenance, production, transportation)" **(explorer bundle)**

with member major groups "Healthcare support", "Protective service", "Food preparation and serving related", "Building and grounds cleaning and maintenance", "Personal care and service", "Farming, fishing, and forestry", "Construction and extraction", "Installation, maintenance, and repair", "Production", "Transportation and material moving" **(explorer bundle)**. **This matters for reading claim 17:** nurses ("Healthcare practitioners and technical", SOC 29) are inside the knowledge-work group, so the page's own example of a safe destination occupation — "switch to jobs like electrician and nurse" — puts one of the two named destinations in the *exposed* group.

**The four states in the reallocation figure** are labelled only in the figure: "Knowledge workers", "All other workers", "Displaced" (key); "Displaced", "Crossed over", "Still there", "Still need to move" (flow labels). None is defined in prose. The figure's `aria-label` is the fullest gloss:
> "the share of all workers in each place in 2026, in transit, and in 2030"

**The wage measure (chart title, §"Finding 3"):**
> "Pay by occupation group, percent above the same economy without AI"

**The GDP measure (chart title and footnote, §"Finding 1"):**
> "US GDP in 2030, by scenario (measured in trillions of dollars)\*"

> "\*GDP is calculated at 2025 price levels"

**Labour and capital shares (§"Finding 4"):**
> "Today, of each dollar the economy produces, about 60¢ goes to workers and 40¢ go to capital."

> "How GDP is shared between workers and capital"

**Capital, defined parenthetically (§"Finding 1"):**
> "a larger share of that prosperity might go to the resources and technology used to create more wealth (capital) compared to workers"

### The parameters exposed to the user

The page names the five dials only by their short prompts (claim 35). The full question text, the answer scales, the "today" markers and the "beyond the paper" notes live in the explorer bundle. **The bundle contains two wordings of each of the five questions**, one terser than the other; which renders in the live UI was not determined, and both are recorded.

**Capabilities (explorer bundle):**
> "What fraction of all knowledge work—work you do mainly with your head, not your hands—will AI be capable of doing by 2030?"

> (alternate) "What fraction of all knowledge work will AI be capable of doing by 2030?"

with emphasis on "capable of doing", the context note "Think about everything the best models could do, whether or not they're widely used." (alternate: "What the latest frontier models could do, whether or not they're widely used."), poles "None of them" / "All 100", and the readout "knowledge-work tasks AI could do".

**Adoption (explorer bundle):**
> "Even when AI can do a task, people don't always use it for that task. Out of every 100 instances of a task AI can do in 2030, how many will AI actually be doing?"

> (alternate) "Of every 100 tasks AI is capable of doing in 2030, how many will it actually be doing?"

with emphasis on "actually be doing", context "Think about reasons people and organizations might not use AI for certain tasks—it costs money, it isn't allowed, nobody set it up, or they'd simply rather do it themselves.", poles "None of them" / "All of them", readout "instances done with AI". **Capability and adoption multiply**: the displayed stat is the product of the two.

**Autonomy (explorer bundle):**
> "For those AI tasks in 2030, how many will be fully automated?"

with emphasis on "fully automated", context "What does AI do on its own? What tasks still need a human in the loop?", and the five labels "Almost none" / "Some of them" / "About half" / "Most of them" / "Almost all of them".

**Productivity (explorer bundle):**
> "In tasks where AI is involved, how much more gets done in an hour in 2030, compared with doing the tasks without AI?"

> (alternate) "On the tasks where AI is involved, how much more gets done in an hour in 2030 than doing them without AI?"

with the worked context "Think about how much someone gets done in an hour on just these tasks. For instance, say a nurse currently writes discharge instructions without AI. But in 2030, that task is either supported by AI or automated entirely. In 2030, how many patients' discharge instructions can the nurse get through in an hour, compared to an hour of writing them on her own?", poles "Same as without AI" / "Ten times as much or more", and the five stops "About the same" (1), "Half again as much (1.5×)", "Twice as much (2×)", "Four times as much (4×)", "Ten times as much or more" (10).

**Adjustment (explorer bundle):**
> "When AI displaces someone from their occupation in 2030, how long until they find work in a new occupation?"

> (alternate) "When AI displaces someone from their occupation in 2030, how long until they find work in a new one?"

with the context "Today it takes people about three months to find a job after losing one, on average.", poles "Quicker than today" / "Most never make it back", and the seven stops "Quicker than today (1–2 months)" (1.5), "Like today (~3 months)" (3), "Twice as long (~6 months)" (6), "Around 9 months" (9), "About a year" (12), "Around two years" (24), "More than three years, or never" (600) — the last coded as 600 months, i.e. never.

**The "today" markers on two dials (explorer bundle).** The capability slider's note is a template, not a fixed string: it reads "Below today: AI already shows up in about", then a computed integer, then "of every 100 knowledge-work tasks." The integer is the model's mid-2026 exposure anchor divided by the cognitive employment share (0.14 ÷ 0.6235), which evaluates to **about 22** (the wiki author's evaluation of the published expression, not a published number). The adoption slider's note is a literal string:
> "Below today: about 10% of the capable tasks already run with AI."

Two of the three "beyond the paper" notes marking the top of the published range are literal strings:
> "Beyond the paper: its scenarios top out near 95%." *(adoption)*

> "Beyond the paper: its extreme scenario reads a bit over twice as much by 2030." *(productivity)*

The capability one is again a template — "Beyond the paper: its extreme scenario reaches about", a computed integer, "of 100 by 2030, on the way to nearly all of it." — whose integer is the capability detent for the extreme scenario, 0.857, i.e. **about 86** (the wiki author's evaluation, not a published number).

## Data and methods

In the wiki author's words, with references. The technical report is the document of record for the model; this section records only **what the page and its shipped assets establish**, and points to `wiki/reports/econ-scenarios-paper-2026-09.md` for the rest.

### What the explorer computes

**A two-sector task-based macro model of the US economy, simulated monthly from a 2024 base to 2030 (selectable to 2040), reporting each scenario as a gap against the same economy without AI.** The user sets five numbers; the tool maps them onto the model's parameter paths, solves, and redraws the GDP, unemployment, wage and factor-share figures. The three named scenarios are presets of the same parameter set, so **the presets and any user prediction are the same object**; the page's "Around 10% of respondents have views in line with the extreme scenario" is a statement about where survey answers land in that parameter space.

The model's structure, as recoverable from the page and the bundle:

- **Two groups, fixed at the start.** *Cognitive* (SOC 11–29, 41, 43) and the rest. Employment shares in the base period 0.6235 / 0.3765, from CPS 2025 annual averages **(explorer bundle)** — the 62.2% / 37.8% left column of the reallocation figure.
- **Three task paths per group**, each a logistic (or linear, for the gain) path anchored at mid-2026 and read at 2030.0: **m**, the share of cognitive work AI affects, with ceiling m̄ = the cognitive share ("all cognitive work"); **d**, the share of affected instances actually done with AI, ceiling 1 ("every instance"); **a**, the log productivity gain on those instances.
- **Two disruptiveness parameters:** **ψ**, the share of affected tasks that is automated rather than augmented; **ρ**, the rate at which new cognitive tasks are created.
- **A search-and-matching labour block** with a den Haan–Ramey–Watson matching function, group-specific separation and finding rates, a cross-group mobility discount **μ**, a posting-speed parameter **θ**, and a sticky cognitive wage that closes a fraction (1 − ξ) of its gap to the market-clearing wage each year.
- **A capital block** with an elastic capital supply (ε), so that automation raises the rental rate and hence capital's share — the channel behind Finding 4, and, per the disclaimer, a channel **added after external review**.
- **An endogenous-ideas block** (semi-endogenous growth, λ and 1 − φ, research funded by a fixed share of GDP) through which AI raises the growth rate, not only the level. This is why the extreme scenario produces a growth *rate* of 15% a year rather than a one-off level gain.

**The scenario presets (explorer bundle).** The three scenarios differ on eight numbers:

| Parameter | Modest | Substantial | Extreme |
|---|---|---|---|
| m, mid-2026 anchor | 0.14 | 0.14 | 0.14 |
| m at 2030.0 | 0.20 | 0.30 | 0.50 |
| d, mid-2026 anchor | 0.10 | 0.10 | 0.10 |
| d at 2030.0 | 0.20 | 0.40 | 0.60 |
| a, mid-2026 anchor | 0.30 | 0.35 | 0.45 |
| a, slope per year | 0 | 0.028 | 0.10 |
| ψ (automation share, constant) | 0.50 | 0.75 | 0.90 |
| ρ (new tasks) | 0.50 | 0.25 | 0 |
| μ (cross-group mobility) | 0.17 | 0.08 | 0.04 |
| θ (posting speed, per month) | 0.10 | 0.25 | 0.50 |

Held common across scenarios **(explorer bundle)**: σ = 0.5 (elasticity of substitution across tasks); ε = 3 (elasticity of capital supply); s_L = 0.6 (base-period labour share — the "60¢" of claim 25); g_A = 1% a year (no-AI TFP growth); n = 0.33% (labour-force growth, "so that GDP grows at 2 percent without AI"); λ = 1 and 1 − φ = 3.1 in TFP units (2.86 in the model's units); ι_R = 3.5% of GDP to research in 2024; ι = 1.27 (matching-function curvature); q̄ = 0.11 a year (normal quit rate, of which 0.06 occupational moves and 0.05 labour-force exits); normal-times μ̄ = 0.17; ξ = 0.50 a year (cognitive wage rigidity); t₀ = 2024, anchors at t = 2026.5, scenario values read at t = 2030.0 (January), horizon 2030.

**The single most important line for our programme.** The bundle's provenance note for the m anchor reads, in part:

> "m anchored at 0.14 at mid-2026 in every scenario, 'observed exposure, averaged over occupations' (the exposure observed in Claude traffic at CPS employment weights)" **(explorer bundle)**

That is: **the model's one empirical anchor on AI's current reach is measured from Claude usage, weighted to CPS employment.** The page never says this — it says only that the Index "measures how AI is being used across the economy right now" while the explorer "is about looking ahead". Whether 0.14 is reproducible from a published Economic Index release, and at what grain, is a question for the data steward and for `wiki/reports/econ-scenarios-paper-2026-09.md`; it is not settled here. The same note records that the anchor was 0.12 before mid-August 2026.

**The calibration data (explorer bundle).** Five named sources, with the defaults marked:

| Input | Source as stated | Default |
|---|---|---|
| Employment shares | "BLS Current Population Survey 2025 annual averages, table 11 (employed persons by occupation) and table 25b (unemployed persons by occupation of last job)" | yes |
| Alternative shares | "BLS Occupational Employment and Wage Statistics, May 2021, summed to SOC major groups" | no |
| E→U and U→E hazards, u₀ | "IPUMS-CPS matched monthly panel … raw, not seasonally adjusted; aggregated with linked person-month weights", windows 2010–2019 / 2015–19 and 2022–24 / 1994–2024 | 2010–2019 |
| Occupational destination matrix | "CPS unemployed job-finders' destination matrix by SOC major group, occupational-coding-error corrected (Carrillo-Tudela & Visschers)", 2010–2019 corrected or 1976–2021 corrected | 2010–2019 |
| Task exposure | "Eloundou, Manning, Mishkin & Rock (2023) dv_rating_beta = E1 + 0.5 E2 by Census occupation, OEWS-2021-weighted within majors, CPS-2025-weighted across them" | **diagnostic only** |

Two published base-period facts follow: unemployment rates of **3.00%** (cognitive) and **5.19%** (other), aggregate **3.84%**; and a pooled occupational switching share among job-finders of **14.3%**, which the μ parameter is calibrated to match **(explorer bundle)**. The GPT-exposure measure of Eloundou et al. is present but explicitly **not** used to drive anything — worth noting, because it is the measure most external work would expect a model like this to use.

**What the presets are calibrated *to* is the report, not this page.** Almost every parameter in the bundle carries a pointer of the form "NOTE Table 1, sec3 L…", i.e. to a table and line of the technical report. Those pointers are recorded as pointers; their content belongs to `wiki/reports/econ-scenarios-paper-2026-09.md`.

**Robustness switches that exist in the code but are not reachable from the published page (explorer bundle):** exact versus first-order solution of the level effect (the explorer reports exact); measured TFP as a base-price index over tasks versus the factor-share dual; separation rates by group versus common; three hazard windows; two destination matrices. A "Model tab", a "How the data enter" panel and an "advanced parameters" panel are referred to in the bundle; **none of them is reachable from the published page**, which exposes five dials and three preset buttons and nothing else.

### The survey

- **Fielded in August 2026 to US adults by Morning Consult** ("Szymon Sacher and Tess Cotter designed and fielded the accompanying surveys with Morning Consult"; payload source string "Survey of U.S. adults, August 2026"). The page says "more than 10,000 Americans"; the card and payload say n = 10,980.
- **Note the plural: "the accompanying survey*s*".** The credits say surveys; the page presents one. The site-visitor quiz is the obvious second instrument, but it is described in the payload as "Readers of this page who took the quiz", which is not a fielded survey. Unresolved.
- **Five questions**, the same five as the explorer's dials, so that each respondent's answers are a point in the model's parameter space and can be run through the model. This is the design's one genuinely novel move: **the survey instrument and the model's parameter vector are the same object**, which is what licenses "the typical respondent's answers imply outcomes close to the 'substantial change' scenario".
- **No sampling frame, weighting scheme, quota design, field dates, mode, incentive or margin of error is published on the page.** Neither is the routing that produces five different per-question denominators (claim 37).
- **Two answer formats.** Capability and adoption ship as 101-bin densities over 0–1; autonomy, productivity and adjustment as 5, 5 and 7 discrete options **(chart data asset)**. In the capability density, the public cohort's first six bins carry an identical value (0.0297 each) and the top five bins are exactly zero, while the site-visitor density heaps sharply on round numbers (0.48, 0.50, 0.60, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, and 12.0% of visitors at exactly 1.00) **(chart data asset)**. The two cohorts' distributions are therefore not produced by the same elicitation, whatever the question wording says; the page does not mention this.
- **The payload's own status flag reads `illustrative: false` (chart data asset)** — i.e. the distributions are real data, not mock. Recorded because the same payload also ships a `finding` and an `unresolved` string for each question whose text is unfinished placeholder copy (e.g. "[Placeholder finding.]", "[Placeholder.] A caveat about this question goes here."). None of this text renders on the page. **The consequence for the wiki is an absence, not a number: the page publishes five survey distributions and no per-question finding or caveat, and the slot for each was cut, not filled.**

### Versioning, data and code availability

- **Version:** "v1.0 of the Econ Scenario Explorer, September 2026"; "The economic scenario explorer is currently Version 1.0." No changelog, no version history, no DOI, no suggested citation and no bibtex block.
- **Data availability: none stated.** There is no download link, no CSV, no Hugging Face dataset and no repository link anywhere on the page. The survey microdata, the scenario time series behind all four findings, and the calibration inputs are all unavailable as files.
- **Code availability: none stated — but the model is in the page.** The full simulation kernel, the calibration constants and the scenario presets ship in the page's JavaScript, so the model is *de facto* public and reproducible in the browser while being *de jure* unpublished: there is no licence, no citation, no versioned artefact and no statement that it may be used. The bundle also carries internal build annotations — a source repository path, commit hashes, an internal decision-log identifier scheme and a set of input-file checksums — which are not reproduced here and which suggest the annotations were not written for publication. **Nothing in this entry should be cited as an Anthropic publication on the strength of the bundle alone**; see `Verification` and the accompanying room note.
- **Relation to the Economic Index releases:** none at the level of published files. The page draws the contrast itself (claim 2). The one substantive link is the m anchor described above, and it is stated only in the bundle.

## Limitations (verbatim)

**The version statement and the omissions list (§"Disclaimer and thanks to reviewers"):**
> "The economic scenario explorer is currently Version 1.0. Like every model, it is a stark simplification of a complex reality: it isolates a few key forces and omits many others that may become relevant and important in the coming years. For example, it leaves out policy responses, business cycles, potential aggregate demand or financial market disruptions, and possible catastrophic risks. The scenario explorer is a work in progress, and we expect it to evolve both as we invest more time and as economic research itself develops."

**Robots, excluded by name (§"The future is not predetermined."):**
> "Like any economic model, this one has limits. For example, we did not include scenarios where humanity develops hyper-capable robots. The model draws on our research and external review, and we'll keep adding to it as the evidence develops."

**What external review changed, and the disclaimer of endorsement (§"Disclaimer and thanks to reviewers"):**
> "We are grateful to the economists who read an early draft of the technical report that lays out the framework behind the explorer, Economic Scenarios for Transformative AI, and gave us detailed comments: Daron Acemoglu, Lukas Althoff, David Autor, Tom Cunningham, Lukas Freund, Joe Hazell, Ben Jones, Pete Klenow, Danial Lashkari, Kurt Mitman, Ben Moll, Emi Nakamura, Pascual Restrepo, David Romer, Jón Steinsson, Chris Tonetti, Ludo Visschers, and David Wiczer. Their feedback was generous and candid, and it has already improved our model. Two examples: several reviewers noted that advances in AI may raise the returns to capital, so that more of the gains flow to the owners of capital; and several noted that the wages of workers in the occupations AI affects most may diverge from those in occupations it barely affects. Both channels are now part of the scenarios. External reviewers were not asked to endorse our conclusions, and any remaining errors are ours."

**The open criticisms, listed by Anthropic against itself (§"Disclaimer and thanks to reviewers"):**
> "Other criticisms are still open, and we plan to address many of them in future versions. Reviewers pointed out that the model does not follow individual workers, so it can only paint a very coarse picture of the costs of job displacement. Some questioned whether occupations exposed to AI will shrink at all rather than grow. Some felt the most extreme scenario is better read as a thought experiment than a scenario, while others felt the most modest one understates what is already visible in the data. Several asked us to be clearer that the model does not include the aggregate demand effects driven by the data center buildout. And more than one reviewer argued that we may be underestimating how much AI could accelerate technological progress itself. We agree that many of these are limitations of the current model."

**What the tool is and is not for, stated as the last sentence of the disclaimer:**
> "The scenario explorer should be viewed as a tool for thinking about what different technological developments would imply for the economy—actual outcomes may differ materially."

**The model is not a map (§"Finding 1"):**
> "This model isn't a complete map of reality, but it shows us some interesting findings."

**Outcomes are choices, not projections (§"The future is not predetermined."):**
> "Ultimately, what the economy looks like in 2030 depends on many factors, like what AI can do, and how companies and workers choose to adopt it. It also depends on how the financial benefit of this technology is shared."

**Hedges attached to the findings themselves.** The page hedges each distributional claim in its own sentence, and these are limitations in the place a reader meets them:
> "The country's GDP will grow, but a larger share of that prosperity might go to the resources and technology used to create more wealth (capital) compared to workers"

> "In more transformative scenarios, more workers have to change occupations. That may mean higher unemployment."

> "And in most scenarios, job reallocation and unemployment both stay within ranges history has seen before, with one exception."

> "The pie will grow, but a larger share might go to capital"

**The self-selection of the site-visitor cohort, stated only in the shipped payload (chart data asset):**
> framing: "self-selected" · source: "Readers of this page who took the quiz"

(The fielded cohort's framing is "fielded". These two words are the page's entire treatment of the difference between its two survey cohorts, and neither appears in rendered text.)

## Open questions, conjectures and promised follow-ups (verbatim)

**A promised next version, stated twice (§"Disclaimer and thanks to reviewers"):**
> "The scenario explorer is a work in progress, and we expect it to evolve both as we invest more time and as economic research itself develops."

> "Other criticisms are still open, and we plan to address many of them in future versions."

**A promise to keep adding to the model (§"The future is not predetermined."):**
> "The model draws on our research and external review, and we'll keep adding to it as the evidence develops."

**What the Institute says this model is *for* — the clearest statement on the page of what it wants next:**
> "This model, alongside our full research portfolio, will inform the research Anthropic funds to identify effective interventions for labor market disruptions. It'll also inform the policy ideas we propose, with the goal of ensuring that the economic benefits of AI are broadly shared across society, both in the US and around the world."

(The first link goes to https://www.anthropic.com/economic-futures, the second to the policy PDF.)

**The open question the page ends its distributional argument on (§"Finding 4"):**
> "In this scenario, the main challenge is not achieving economic growth, but making sure the benefits are broadly shared and the costs aren't unequally dispersed."

**The same, stated in the opening as the challenge the whole exercise is about:**
> "In those scenarios, society is far wealthier, so the challenge is making sure that the gains are broadly shared."

**Reviewer criticisms Anthropic records as unresolved and adopts as open questions.** Each of the five below is an open question with a named source (an external reviewer) and an explicit concession ("We agree that many of these are limitations of the current model"):
> "Reviewers pointed out that the model does not follow individual workers, so it can only paint a very coarse picture of the costs of job displacement."

> "Some questioned whether occupations exposed to AI will shrink at all rather than grow."

> "Some felt the most extreme scenario is better read as a thought experiment than a scenario, while others felt the most modest one understates what is already visible in the data."

> "Several asked us to be clearer that the model does not include the aggregate demand effects driven by the data center buildout."

> "And more than one reviewer argued that we may be underestimating how much AI could accelerate technological progress itself."

**The untested conjecture behind Finding 3 — the derived-demand channel (§"Finding 3"):**
> "Meanwhile, as AI increases productivity within knowledge work, the demand for manual work that benefits from that productivity will increase. For example, more quickly producing designs and permitting for physical infrastructure could increase the number of construction projects, resulting in rising demand for construction workers, which pushes those wages higher."

**The untested conjecture behind claim 17 — where displaced knowledge workers go (§"Finding 2"):**
> "At the individual level, it means coders and call service center agents may have to switch to jobs like electrician and nurse, which are less exposed to AI."

**The untested conjecture behind the new-task channel (§"And new tasks will appear"):**
> "Historically, new technologies have also created new tasks for workers."

**The question the whole page is built to ask the reader (§"How might powerful AI change the economy?"):**
> "How do you think AI development will go over the next few years? And what would that path mean for the economy? We invite you to consider these questions, and explore potential answers with our scenario explorer."

**The framing question, unanswered by design (hero):**
> "We don't know yet how AI will reshape the economy. Will it lead to unprecedented growth? Widespread unemployment? Neither, or something else? How can we tell?"

(The page never returns to "How can we tell?" — no indicator, no test and no diagnostic for distinguishing the scenarios in real time is offered anywhere on it. Recorded as the page's own unanswered question.)

## What it did not test

The wiki author's inference, **not** the page's claims. Each item is something the page's text leaves open, or a cut its own apparatus would permit and it does not take. Items whose answer may sit in the technical report are marked *(check paper)*; that file, not this one, is where to look.

1. **Nothing here is tested at all.** This is the first and most important entry. The explorer is a calibrated simulation with no estimation, no confidence interval, no probability on any scenario, no out-of-sample check and no historical backtest anywhere on the page. Every number in `Claims` is an output of assumptions. A post building on this page builds on a *framework and a set of parameter choices*, not on evidence, and must say so in its first paragraph.

2. **The scenarios are never given probabilities, and the survey is not treated as one.** The page reports that the typical respondent implies the substantial scenario and about 10% imply the extreme, then declines to turn that into a probability distribution over scenarios — which is the obvious next step and would be the most useful thing the survey could produce. Whether the public's implied distribution over 2030 GDP is even well defined under this mapping is untested.

3. **"How can we tell?" — no leading indicator.** The hero asks which future we are in and how we would know. The model runs on five quantities, at least two of which (m, the affected share; d, the adopted share) are measurable now and are in fact measured by the Economic Index. **No diagnostic, no tracking series and no "which scenario are we on" test is published.** This is the single largest gap between what the page asks and what it delivers, and it is squarely in our programme's reach.

4. **The Claude-traffic anchor is never validated or shown.** m = 0.14 at mid-2026 is the model's only empirical tether, it is measured from Claude usage at CPS employment weights **(explorer bundle)**, and the page does not mention it, does not reproduce it, does not say which release it comes from and does not bound the gap between *Claude's* traffic and *AI's* reach. The note records that it moved from 0.12 to 0.14 within a month of publication, so the whole scenario family is anchored on a quantity that is both unpublished here and moving *(check paper)*.

5. **Sensitivity of any finding to any parameter.** Ten parameters differ across the three presets and change together. Nothing decomposes which of them drives the GDP gap, the unemployment spike or the labour-share fall. A reader cannot tell whether the extreme scenario's 54.8% capital share comes from ψ = 0.9, from ρ = 0, from μ = 0.04 or from ε = 3. The dials permit exactly this exercise and the page does not run it.

6. **The robustness switches that exist and are not exposed.** Two hazard windows besides the default, two destination matrices, two employment-share sources, exact versus first-order solution, two TFP definitions, group-specific versus common separation rates — all implemented, none reachable from the published page, none reported **(explorer bundle)**. The default choices (2010–2019 hazards, 2010–2019 matrix, CPS 2025 shares) are not defended anywhere in public, and the 2010–2019 window excludes both the pandemic and the tight labour market that followed it.

7. **The two-group partition, tested against any alternative.** "Knowledge worker" is 62.2% of US employment and includes cashiers, administrative assistants, teachers and nurses. Every result in Findings 2 and 3 is a statement about that group against its complement. No alternative partition — by task exposure score, by wage, by education, by the Economic Index's own occupational usage — is tried, and the exposure measure the bundle *does* carry (Eloundou et al. 2023) is marked "diagnostic only". Whether the results survive a continuous exposure measure is untested *(check paper)*.

8. **Whether the page's own example survives its own taxonomy.** Displaced coders are said to move to "electrician and nurse". Nurses are in the cognitive group. The page's illustration of a safe destination is, in the model, half inside the exposed group, and nothing reconciles them.

9. **Occupational detail, which the calibration has and the output does not.** The model is calibrated on a 22 × 22 SOC-major-group transition matrix and per-major-group employment, hazards and unemployment rates **(explorer bundle)**, then reports everything at two groups. No major-group result, no destination pattern, no statement of which of the twelve cognitive majors absorbs the displacement. The data to do it are in the page.

10. **Heterogeneity within a group.** No age, education, tenure, region, firm size or wage-level dimension exists in the model or the output. The reviewer criticism that "the model does not follow individual workers" is conceded and not addressed, so the distribution of the adjustment cost across people — which is the thing the policy conclusion depends on — is not modelled at all.

11. **Any geography below the US.** One country, one aggregate. No state, metro or industry cut, despite the closing claim that the work bears on outcomes "both in the US and around the world".

12. **Anything after 2030, or before 2026.** The horizon is 2030 by design (the bundle makes 2035 and 2040 selectable but the page does not). More consequentially, nothing is shown for 2024–2026, so the reader cannot see whether the modest scenario is already ruled in or out by data that exist — which is precisely the disagreement the page records among its reviewers ("others felt the most modest one understates what is already visible in the data") and does not settle.

13. **The survey's representativeness and its five denominators.** No weighting, no frame, no field dates, no margin of error, no comparison of respondents to the US population on any observable. The five per-question counts (8,904 / 4,664 / 4,216 / 8,474 / 4,480 against a headline 10,980) **(chart data asset)** are never reconciled, so no published share on this page can be converted to a count, and the reader cannot tell whether the "typical respondent" is a single person answering five questions or a composite of five subsamples.

14. **Whether the survey answers are internally coherent.** Each respondent supplies five numbers that jointly imply a 2030 economy. Nobody checks whether individuals' answers are mutually consistent, whether the five are correlated within a person, or whether the "typical respondent" (presumably a median-by-question composite) corresponds to any actual respondent. The extreme-leaning 10% is reported as a share of people; the implied-GDP distribution behind it is not.

15. **The two cohorts, compared as a finding.** Site visitors are dramatically more bullish than the public on autonomy and productivity **(chart data asset)** — the two cohorts are on the page, side by side, on identical scales, and the page never remarks on the gap. A comparison of who believes what about AI, and by how much, is sitting unused in the page's own data.

16. **Whether people's beliefs move.** One cross-section, August 2026. No panel, no repeat, no pre/post exposure to the explorer — even though the site-visitor cohort is, by construction, people who have just read the argument, and their answers are being recorded.

17. **Any external benchmark for the survey.** Public beliefs about AI capability and job loss are measured regularly elsewhere. Nothing here is set against any other instrument, so "the typical respondent implies the substantial scenario" cannot be checked for instrument effects, and the framing effect of asking these five questions inside this page is unbounded.

18. **The aggregate-demand and data-centre channels, conceded and omitted.** The reviewer point is recorded verbatim and not acted on. Given that the data-centre buildout is a large share of recent measured US growth, a model whose modest scenario is "+1.6%" omits a channel of comparable size to its own headline.

19. **Robots, policy, business cycles, financial disruption and catastrophic risk**, all named in the disclaimer as omitted. Each is named, none is bounded: the page never says which direction any omission pushes its results, or by how much.

20. **The unemployment and wage results are published only as pictures.** The two figures carrying Findings 2 and 3 render client-side and contain no values, labels or axis ticks in the page source. The page's most consequential labour-market numbers — the unemployment paths and the wage gaps by group — are therefore not quotable from this page at all, only from the technical report *(check paper)*. Any post that wants them must take them from there and say so.

21. **Reproducibility, in the ordinary sense.** No data, no code repository, no licence, no citation, no version archive. The model is fully present in the page's JavaScript, which makes it inspectable by accident rather than by publication, and gives a reader no sanctioned way to cite or rerun it.

22. **Whether the explorer and the Index agree.** The page sets them side by side rhetorically (claim 2) and never joins them. The Index publishes automation-versus-augmentation shares; the model sets ψ, the automation share, at 0.5 / 0.75 / 0.9 by assumption. **The Index measures the quantity the model assumes**, and no one has put the two numbers next to each other. That comparison — what the Index's observed automation share implies about which scenario's ψ is plausible — is the most direct contribution available to our programme, and it is not made here or, on the evidence of this page, anywhere.

## Verification

- **Fetched 2026-09-16.**
  - https://www.anthropic.com/institute/econ-scenarios — HTTP 200, fetched twice. (i) `web_fetch`, which returned the rendered markdown: all body prose, all headings, all chart titles, the survey card, the GDP and factor-share figures' values, the disclaimer and the credits, read in full. (ii) `curl` to the raw HTML, 383,504 bytes, from which 383 lines of visible text were extracted and read in full. **The two agree on every quoted sentence.** The raw fetch adds three things the rendered fetch does not: the reallocation figure's SVG `<text>` data labels with their `aria-pressed` scenario state; the survey payload; and the JavaScript chunk manifest.
  - **Survey chart payload:** reconstructed from the 21 `self.__next_f.push` chunks in the page HTML (84,082 characters of React Flight payload) and parsed as JSON. It contains one object, `survey`, with `illustrative`, two `cohorts` and five `questions`, each carrying `stops`, `indices`, `ordinal`, `density` (per cohort), `counts` (per cohort), `finding` and `unresolved`. It is served **inside the page**, not as a separate file, so there is no asset URL to cite; the citation is the page URL plus the payload path `survey.questions[*]`.
  - **Explorer model bundle:** 18 JavaScript chunks are referenced by the page; all 18 were fetched, all HTTP 200. The model, the calibration and the quiz wording are in `/_next/static/chunks/2jxuplajve9n_.js` (334,487 bytes); one further chunk contains the word "modest" in unrelated copy. Chunk filenames are content-hashed and will change on the next deploy, so the bundle is cited by page URL and symbol, not by chunk name.
- **Fetch failures:** none. Every URL attempted returned HTTP 200.
- **Not fetched, deliberately:** the technical report PDF (`cf58f84d…pdf`) — a separate slug, `econ-scenarios-paper-2026-09`; the policy PDF (`9ea607a5…pdf`) and the three Anthropic pages linked from the body — all belong to `wiki/reports/programme-and-product-pages.md` or their own slugs.
- **Alt text:** the raw HTML contains **no `alt` attributes at all** except the two social-card metadata strings, both of which read "Anthropic logo". The director's alt-text ruling therefore has nothing to bite on in this entry; no number in this file is marked `(alt text)`.
- **Images and client-rendered figures.** Two static images exist on the page and both are social-card assets, not figures. Every figure is drawn in the browser. Three of them contain **no values in the page source**: the GDP waterfall's four-part decomposition, the unemployment trend panels (§"Finding 2") and the wage trend panels (§"Finding 3") are empty `<div class="…frame">` elements server-side. Their titles and keys are recorded; **no value is recorded from any of them, and nothing was read off a rendered image.**
- **Figure labels, per `room/director-2026-09-16-figure-values-ruling.md`.** Seven values in `Claims` 14 are marked `(figure label)`: they are printed as `<text>` elements inside the server-rendered SVG of the reallocation figure, i.e. data labels inside a figure, which that ruling permits in `wiki/reports/`. The scenario they belong to was established from the toggle's `aria-pressed="true"`, which sits on "Substantial". The modest and extreme versions of the same figure are computed in the browser and are not recorded. The GDP and factor-share values in `Claims` 10 and 27 are **not** marked: they are emphasised text in the page's own markup, present identically in the rendered fetch, and are quoted as published prose.
- **Chart data asset, per `room/director-2026-09-16-chart-asset-ruling.md`.** Fifteen places in this file carry a value or label from the survey payload, each marked `(chart data asset)`. The ruling's condition — values in a published chart data asset, JSON served by the page to draw its charts — is met; the only difference from the precedent case is that this payload is embedded in the page rather than served as a separate file, which strengthens rather than weakens the case. Nothing here was read off an image. **The dependency matters:** claims 34, 36 and 37 and `What it did not test` 13 and 15 rest on it, and item 37 — the five different per-question denominators — is the entry's single most consequential finding about the survey and exists nowhere else.
- **Explorer bundle — a new marking, flagged not assumed.** Twenty-six places carry a value, label or quoted string from the page's JavaScript model bundle, each marked `(explorer bundle)`. This goes beyond both existing rulings: the chart-asset ruling covers data served to draw charts, and this is *code and its constants*. The argument for recording it: the bundle is the explorer's source of record for what the explorer computes, the `Data and methods` section could not otherwise say what the tool does, and the material is served unauthenticated from anthropic.com as part of the published page. The argument against: it carries internal build and provenance annotations (a source repository path, commit hashes, an internal decision-log identifier scheme, input-file checksums and unfinished placeholder copy) that were plainly not written for readers, which is evidence that the *annotations*, at least, are not a publication. **A ruling is requested in `room/lead-2026-09-16-wiki-econ-scenarios-explorer-2026-09.md`.** If the director rules the bundle out of scope, the marked passages come out; `Definitions` loses the full question wording and the group definitions, `Data and methods` loses the preset table, the calibration table and the Claude-traffic anchor, and `What it did not test` 4, 6, 7 and 9 lose their support. Internal identifiers, hashes and repository paths are recorded nowhere in this file by intent; only their existence is noted, because it bears on whether the bundle may be cited at all.
- **No arithmetic on any released data file, and no data file opened.** Two derived quantities appear and both are marked as the wiki author's evaluation of a published expression rather than as published numbers: the capability slider's "today" marker (0.14 ÷ 0.6235 ≈ 0.2245, rendering as "about 22 of every 100"), and the observation that the site-visitor count changed between the two fetches. `team/agents/programme-lead.md` and `room/director-2026-09-16-alt-text-ruling.md` are observed: nothing under `data/` was read, and the questions this entry raises that data would settle — whether m = 0.14 is reproducible from a published Economic Index release, and how the Index's observed automation share compares with the model's ψ of 0.5 / 0.75 / 0.9 — are put to the steward in the accompanying room note, not answered here.
- **Quotation check.** Every passage in quotation marks in `Definitions`, `Limitations`, `Open questions` and `Claims` was checked string-for-string against both fetched renderings after normalising whitespace, curly quotes and dashes. 71 distinct quoted passages: 58 matched against the page text in both fetches; 13 matched against the explorer bundle, where they are the only place they appear, and each of those is marked `(explorer bundle)` at the point of use. Source oddities reproduced deliberately: "share of respondents at each answers" (survey chart title) and the page's own inconsistency between "substantial scenario" and "substantial change" scenario.
- **Internal discrepancies recorded, not resolved:** (i) the `<title>`/OG title "Scenarios for our Economic Future" against the H1 "What will our economic future look like?"; (ii) no dateline on the page — only "September 2026" — against `wiki/INDEX.md`'s 2026-09-09; (iii) headline survey n = 10,980 against five per-question counts of 8,904 / 4,664 / 4,216 / 8,474 / 4,480; (iv) site-visitor n = 27,143 in the rendered fetch against 27,148 in the raw fetch minutes later; (v) "more than 10,000 Americans" against 10,980; (vi) "the accompanying survey**s**" in the credits against one survey presented; (vii) "substantial" against "substantial change"; (viii) the nurse as the page's worked example of an AI-transformed job and as its example of a destination occupation "less exposed to AI", with nurses inside the model's cognitive group; (ix) the O\*NET taxonomy named for the illustration while the calibration runs on CPS/OEWS/IPUMS; (x) "Read blog" rendered as an affordance with no blog behind it; (xi) two different wordings of each of the five survey questions in the bundle.
- **Cross-file consistency.** Slug, title, date, type and primary URL match the row for `econ-scenarios-explorer-2026-09` in `wiki/INDEX.md`, whose methodology-appendix column is `—` (correct: there is no appendix) and whose wiki/style column is `—` per `room/director-2026-09-16-resume-decisions.md` §2. `wiki/INDEX.md` was **not** edited in this thread. The technical report is cross-referenced and not summarised, per the task.
