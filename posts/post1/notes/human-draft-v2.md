# Is AI delegated more on low-wage work or on high-wage work?

*September 2026 · Evidence from Claude*

## Half of Claude.ai use is delegation, and nobody has asked what that work pays

A one-line request to translate a contract clause is one kind of conversation with Claude. A two-hour back-and-forth on a grant proposal is another. In the first, the person **hands the task over**: they say what they want, Claude does it, and the exchange ends, or continues only so the person can steer the output. In the second, they **collaborate**: they ask to understand something, work on a draft turn by turn, or bring finished work to be checked.

About half of the conversations people have with Claude.ai are the first kind. Anthropic has published this split in every Economic Index report since the first, in early 2025, and has watched it move: delegation rose sharply through the summer of 2025, then eased back as more of what people brought to Claude became learning and iteration.

Economists have a name for why the split matters. A technology that **substitutes** for a person's work and one that **complements** it have opposite consequences for who gets paid, and how much. Whether people delegate or collaborate is the closest thing the Index has to a signal of which of the two is happening, task by task; it is a measure of how people use the tool, not a verdict on what becomes of their jobs, and Anthropic's reading of its own data is that most jobs evolve rather than disappear. The reports leave the interpretation open on purpose. If the rise in delegation means models can simply do more tasks, the workers doing those tasks are the ones at risk. If it means people are learning to trust the tool with work they still supervise, the same number describes the opposite.

The Index has learned a good deal about **who delegates more**. Businesses using Claude through the API delegate far more than people on Claude.ai. Countries with less Claude use per person delegate more than countries with more. People new to Claude delegate more than long-standing users. And the level of education a task demands makes no difference at all.

What the Index has never asked is **what the delegated work pays**. It knows the answer for each task: since March 2026 the reports have priced the tasks brought to Claude by the hourly wage of the American workers who do them, and used that price to show which tasks get the most capable model and the most tokens. But the price of the work and the way the work was done have never been put in the same table. So a plain question has no published answer. When people hand work over to AI, is it more often the low-paid work or the high-paid work?

The answer matters for two different readers, and this post keeps returning to both.

**(i) For anyone thinking about jobs**, it is the difference between two stories. In one, the routine, low-paid tasks go to AI first and the well-paid ones are protected by their complexity. In the other, the well-paid work is the first to be handed over, because it is the work AI is best at. Anthropic's own reports have raised the second possibility: if AI substitutes for the less expert work and complements the more expert work, that is one more form of skill-biased technological change; if the reverse, the people at the top of the pay scale are the ones whose work is being automated.

**(ii) For anyone using the Index's numbers**, it is a question of measurement. The delegation share Anthropic publishes counts conversations and gives every task the same weight. Anthropic's own labour-market exposure measure and its scenario models weight delegated work more heavily than collaborative work, and price tasks by what they pay. If delegation is concentrated at one end of the pay scale, reading the unweighted share as if it were weighted by wages carries an error whose direction nobody has established.

This post crosses the two for the first time, in three separate weeks of Claude.ai conversations between August 2025 and February 2026. Three things follow, stated here without numbers so they can be read before the tables.

1. The best-paid quarter of the work brought to Claude is delegated a little more often than the worst-paid quarter, in every one of the three weeks, though the size of the gap is not the same in any two of them.
2. That gap is entirely a matter of what kind of work sits at the top of the pay scale. It is software. Once software is set aside, the best-paid work is delegated *less* than the worst-paid.
3. Weighting the published delegation share by the wage of the work barely moves it.

So the answer is two-sided, and the title is a question for that reason.

Two limits need saying before the first table, because a reader will think of them first.

1. **This is Claude.ai, not the economy.** The tasks people bring to a chat assistant lean heavily toward writing, coding and analysis, and Anthropic has said itself that its data are "not broadly representative of the US economy".
2. **The unit is a task, not a person.** Nobody's occupation or salary is observed. The wage attached to a conversation is the median wage of the American occupations whose work most resembles what was asked. So "low-wage work" and "high-wage work" here mean the bottom and top quarter of the tasks brought to Claude, ranked by what that work pays in the United States, not the bottom and top of anyone's payroll.

## Four possible answers, and the pattern each would leave in the data

The measured quantity is one number per week: the delegation share of the best-paid quarter of tasks minus the delegation share of the worst-paid quarter, in percentage points, with each task counted by how many conversations it received. Call it **the gap**. A gap of one percentage point was fixed in advance as the smallest difference worth calling a gradient, and the possible answers were written down before the data were run, each with the pattern that only it would produce.

| If the truth were… | …then in all three weeks | What the three weeks showed |
|---|---|---|
| Delegation rises with the pay of the work | the gap is positive and clears one point, and survives when coding tasks are set aside | Positive in all three, clears one point in two, and reverses once coding is set aside |
| Delegation falls with the pay of the work | the gap is negative and clears one point | Not found |
| The pay of the work makes no difference | the gap sits inside one point either way | Not found |
| It is the kind of work, not the pay | a positive gap that loses its sign when coding tasks are set aside, or when the comparison is made within occupational groups | **This is what the data show**, on both tests, in every week |

A fifth outcome was also written down: a gap whose direction is steady but which does not clear one point in every week. That is a real difference whose size the design cannot pin down, and it is where the headline landed. The kind-of-work reading was then tested, as the rules required, and it held. The three findings that follow take those steps in order.

## Finding 1: the best-paid quarter of tasks is delegated a little more, in every week, but only the direction is steady

Two definitions first, because every number below depends on them.

**Delegated** means what Anthropic's classifier calls automation: the person either hands the whole task over, or hands it over and steers with feedback. Its counterpart, **collaborated**, covers asking to learn, iterating on a draft together, and asking for a check on one's own work. A task's **delegation share** is its delegated conversations divided by all five of those patterns together. Conversations that fit none of the patterns are outside the count and are reported separately in Figure 2. Two of Anthropic's own cautions travel with the measure: (i) delegation is not autonomy, since a one-line translation request is fully delegated and asks almost nothing of the model; and (ii) the shape of one conversation does not show what the person did with the result afterwards.

**The wage of the work** is the median hourly wage of the American occupations that do a task, averaged over those occupations by how many people they employ. Tasks are ranked by that wage and cut into four quarters of equal conversation volume, so "the best-paid quarter" holds a quarter of the week's conversations, not a quarter of its tasks.

The delegation share is not a smooth line in pay. In every week it falls from the worst-paid quarter to the second and rises again to the best-paid: 53.1, 47.0, 49.8 and 54.4% across the four quarters in August 2025; 46.6, 41.3, 46.0 and 54.0% in November; 48.8, 41.6, 43.5 and 49.5% in February 2026. The middle of the pay scale, where most of the writing and analysis lives, is where people collaborate most. The two ends are where they delegate.

**Figure 2. The delegation share is U-shaped in the wage of the work: it falls from the worst-paid quarter of tasks to the second and rises again to the best-paid, in every week.** Plotted: each wage quarter's delegation share, in percentage points of that quarter's classified conversations, one panel per Claude.ai week. Each quarter holds a quarter of the week's conversations, not a quarter of its tasks (the bottom quarter holds 600 / 699 / 649 tasks and the top 360 / 403 / 482). The grey figure under each point is that quarter's share of conversations fitting none of the five patterns, printed so the base is never implicit; the x labels carry each quarter's conversation-weighted mean hourly wage. Sample as Figure 1. Bars are two-sided 95% intervals from a conversation-level binomial with the task mix held fixed, a lower bound on the sampling variance.

The contrast between the two ends is the headline. **In each of the three Claude.ai weeks the delegation share of conversations on top-wage-quartile tasks exceeded that of conversations on bottom-quartile tasks: by 1.4 points in August 2025, 7.4 points in November 2025 and 0.7 points in February 2026.** The uncertainty bands on those numbers treat each conversation as an independent draw with the task mix held fixed (two-sided 95% intervals); because no release identifies a user or a session, they understate the true uncertainty and are a lower bound on it.

Two things about the three numbers matter more than their average, which is why no average is given.

1. **The size is not steady.** It runs from two thirds of a point to more than seven, a spread twenty-six times the within-week standard error, so the intervals describe sampling inside a week and say nothing about why the weeks differ.
2. **The gap exceeds one point in two of the three weeks and not in the third.** The rule set in advance therefore records a steady direction, and does not record a gradient above the one-point margin in every week.

**Figure 1. In all three Claude.ai weeks the delegation share is higher on top-quartile than on bottom-quartile tasks, and in none of them does the gap clear one point under every rule.** Plotted: the delegation share of the top wage quartile minus that of the bottom, in percentage points, one point per week (4–11 August 2025, 13–20 November 2025, 5–12 February 2026), each estimated on its own and never pooled. A task's delegation share is its directive plus feedback-loop conversations over its five classified collaboration patterns; tasks are ranked by the employment-weighted median hourly wage of the occupations that hold them and cut into quarters of conversation volume. Sample: the 1,802 / 2,075 / 2,188 tasks with a wage and at least one classified conversation, 97.2 / 96.2 / 96.5% of named-task usage, on 818,673 / 854,432 / 848,716 classified conversations. Bars are two-sided 95% intervals from a conversation-level binomial with the task mix held fixed, a lower bound on the sampling variance.

Three cautions belong beside the headline rather than in a list at the end, because each one changes how it should be read.

**(i) The August gap depends on where the quarters are cut.** The boundary between the third and fourth quarter falls, in every week, at $43.40 an hour. That is the wage the file assigns to one group of computer occupations, and the 99 / 106 / 111 tasks priced at exactly that wage carry 8 to 11 percentage points of a week's conversations. Which of them count as top-quartile is decided by sort order. Sharing that boundary wage between the two quarters instead gives gaps of 0.5, 7.2 and 0.3 points, and August no longer exceeds one point. Under a different rule for pricing tasks that several occupations share, February's gap is −0.2 points with an interval containing zero, and the rule would then record no steady direction at all. And the top quarter is small where it counts. Counting tasks by how evenly conversations are spread across them, it behaves like 10.6, 8.9 and 16.4 tasks in the three weeks, because a few software tasks dominate it.

**(ii) November's seven points carry a warning.** A task's global delegation rate blends every country's conversations and cannot be cleaned at this grain, and Anthropic's own country regression, reproduced here, has lower-usage countries delegating more. The one geography that can be bounded is Seychelles, which that week sent a large volume of coding conversations. Netting its conversations out of the task weights moves November's gap to +6.5 points, and counting every one of its conversations against the finding still leaves +4.5. So Seychelles does not account for November's excess over the other two weeks. What does move November is dropping the 23 tasks in which Seychelles exceeded a tenth of the global count, which takes the gap to −4.6 points. But those 23 tasks include the two largest software-modification tasks in the data, so that flip is a coding result, not a Seychelles result.

**(iii) The composition test decides how all of this is read.** The tasks that make up the best-paid quarter are 73, 71 and 65% Computer & Mathematical by conversation volume in the three weeks, against 43, 40 and 36% of all tasks. Set that family aside and the sign reverses in every week.

So far the numbers look like the story in which well-paid work goes to AI first. The next finding is why that story does not survive.

## Finding 2: the whole of the excess is coding; set it aside and the best-paid work is delegated less

The pre-registered test for "kind of work, not pay" had three legs, each re-estimating the same gap.

1. **Set aside coding.** Remove every Computer & Mathematical task and keep the quartile boundaries where they were.
2. **Compare within occupational groups.** Compare management tasks with management tasks, clerical with clerical, and so on across the 22 broad groups of the US occupational classification, then average the gaps.
3. **Keep only work.** Keep only tasks that are mostly brought to Claude as work rather than as personal or coursework requests, to check whether the gap is really a difference between working and non-working use.

**With Computer & Mathematical tasks excluded, the delegation share of the best-paid quarter was 13.0, 10.5 and 11.9 points *below* the worst-paid quarter's, in the three weeks.** **Within occupational groups, averaging over the ten (August, November) or nine (February) groups that hold tasks in both extreme quarters, the gap was −4.2, −1.9 and −6.2 points.** Those groups carry 80, 80 and 76% of the two quarters' conversations; the remaining groups have tasks at only one end and cannot be compared. Both legs lose the sign of the headline in every week. The composition rule set in advance therefore fires, and the relation between delegation on Claude.ai and the wage of the work reads as a mix that travels with wage, not as a property of the wage.

**Figure 3. The gap does not survive either composition test: setting aside Computer & Mathematical tasks, or comparing within occupational groups, turns it negative in all three weeks; keeping only work-dominant tasks does not.** Plotted: the top-minus-bottom gap in the delegation share re-estimated under each pre-registered composition leg, in percentage points, one panel per week. The coding exclusion removes 42.8 / 39.7 / 35.6% of analysis-set conversations and 73.1 / 71.3 / 65.5% of the top quartile's, with the quartile boundaries kept from the full set. The within-group leg averages the group-level gaps over the ten, ten and nine major groups with tasks in both extreme quartiles, weighted by their conversations there. The work-dominant leg keeps the 943 and 1,071 tasks whose published use-case cells are at least half work, in November and February; August publishes no use-case facet and is untested. Bars are two-sided 95% intervals on the same binomial model, a lower bound on the sampling variance.

Two readings of the first leg have to be kept apart.

**(i) What it does not say** is that outside coding, delegation falls with pay. Once the coding tasks are removed, what remains of the best-paid quarter is a small set of managerial, scientific, engineering and clinical tasks, six to eight percentage points of a week's conversations, and it is being compared with clerical, educational and sales tasks at the bottom. That is a comparison of task types. The within-group leg is the cleaner statement, because it holds the type fixed.

**(ii) What it does say** is that the headline gap is a coding gap wearing a wage label, and every other cut agrees. Removing any single occupational group other than Computer & Mathematical moves the headline by at most 3.2, 2.3 and 2.9 points; removing Computer & Mathematical moves it by 14.4, 17.9 and 12.6. Removing just the ten largest tasks by conversation volume, a fifth to a quarter of all conversations and mostly software, turns the gap to −11.6, −13.1 and −11.4 points. And inside the coding family alone there is no pay gradient to speak of: the gap within it is −0.1, +6.5 and +0.8 points, on a bottom quarter of only 24, 23 and 14 tasks.

The third leg is the one that did not fire, and it settles nothing. Restricting to work-dominant tasks leaves the gap at 3.7 points in November and 2.8 in February, keeping its sign and at least half its size, so on the rule as written the use-case mix does not carry the gradient. But in November the retained fraction sits exactly on the half-way boundary with an interval straddling it, August cannot be tested, and the work-dominant top quarter is the coding top quarter under another name, since most of its conversations are kept while only a fifth to three tenths of the bottom quarter's are. The use-case reading is neither confirmed nor ruled out.

Something about it is visible all the same. The worst-paid quarter of tasks is only about a third work, 33% in November and 29% in February, against 61% in the best-paid, and it is close to half personal requests. **Low-wage work on Claude.ai is not, for the most part, low-wage labour.** It is people asking for help with their own lives. For the jobs story, that matters as much as the coding result: the bottom of this pay scale is not a workforce.

## Finding 3: weighting the published delegation share by the wage of the work barely moves it

The measurement question can now be answered directly. **Weighting the published delegation share by the hourly wage of each task would move it by −0.02 points in August, an interval containing zero; by +0.84 points in November; and by −0.15 points in February.** In the three weeks the unweighted shares of the tasks in the analysis are 51.1, 47.0 and 45.9% and the wage-weighted shares 51.1, 47.8 and 45.7%.

Two things follow. (i) The change is below one point in every week, which is the line the design fixed in advance for a correction that would matter, and it runs in the same direction as the quartile gap in only one week of three. (ii) It is a correction to an **hourly rate, not to a wage bill**: the re-weighting uses the price of an hour of the work and no hours enter it, so it says nothing about how much labour payment sits behind delegated conversations.

**Figure 4. Weighting the published delegation share by the wage of the work moves it by less than a fifth of a point in two weeks and by eight tenths of a point in the third, and August's interval contains zero.** Plotted: the wage-weighted minus the unweighted delegation share of Claude.ai conversations, in percentage points, one marker per week, on the same tasks, weights and per-task shares as Figure 1. The null value is zero, the value it takes when the delegation share is uncorrelated with the wage across the task mix. Bars are two-sided 95% intervals on the conversation-level binomial model, a lower bound on the sampling variance. The one-point materiality line is the brief's and is separate from the one-point margin applied to the quartile gap.

The reason the correction is small is the reason the headline is two-sided. A continuous slope of the delegation share in the hourly wage has no steady sign: −0.05 points per $10 in August, not distinguishable from zero; +1.77 in November; −0.28 in February. Add each task's work share to that regression and the November slope moves from +1.78 to −0.06 points per $10, and the February slope from −0.28 to −1.63. Pay does not order delegation across the task mix as a whole. One family of tasks does, and it happens to be well paid.

Three further probes were run and labelled **exploratory** in advance, so they are context, not findings.

1. Splitting delegation into its two components, the fully directive conversations are *less* common on top-quartile tasks in every week, by 7.0, 9.5 and 9.9 points, while feedback-loop conversations are more common, by 8.4, 16.9 and 10.6. The excess is a feedback-loop excess: the best-paid work is handed over and steered, not handed over and forgotten.
2. On the API, where businesses run Claude and delegation dominates, the gap is negative in every week, −2.4, −2.5 and −5.2 points, though the February API sample includes Claude Code and this is not a replication.
3. Against Job Zone, O\*NET's ordering of tasks by how much preparation they need, delegation falls by about 6.7, 6.0 and 6.8 points per zone.

None of these was a pre-registered test, and none appears in a heading or a conclusion.

## What this means: it is the kind of work, not the pay

On Claude.ai, in these three weeks, the wage of the work is not what orders whether people delegate or collaborate. The kind of work is. Software happens to be both the best-paid work people bring to Claude and the work they most readily hand over. That is why a naive reading of the data says AI is delegated more on high-wage work, and why that reading is wrong. Compare like with like and the best-paid tasks are delegated a little less than the worst-paid. Neither statement is a statement about pay. The design prices a task by the occupation it resembles, and it cannot separate what the work pays from what the work is, so it withdraws the sentence "delegation depends on the wage of the work" in both directions.

**(i) For the jobs story**, this changes which story to tell. The evidence here does not support the picture in which well-paid work is being handed over to AI because AI is good at it, nor the picture in which low-paid routine work goes first. It supports a narrower and more useful claim: the work being delegated is a specific kind of work, and its pay is incidental. Wherever Anthropic's reports have found delegation concentrated, in businesses using the API, in countries with less usage, among newer users, the same question should be asked of each: is it the pay of the work, or is it that these users bring more software? The three weeks here point to the second wherever it has been tested.

**(ii) For the reader who uses the Index's numbers as inputs**, the answer is more direct. A published delegation share can be read as a wage-blind average without much error, because the wage-weighted version is close to it in every week and not consistently above or below. What such a reader should condition on instead is the share of software in the task mix, which is the one composition that moves the number, and which an unweighted share hides. A model that weights delegated tasks by what they pay is not wrong to do so. But the quantity it is really tracking, in this data, is coding.

The obvious objection is that three weeks of one product cannot carry a claim about work. That is right, and the size of the gap is the warning. It varied from two thirds of a point to more than seven across three weeks whose sampling error is a fraction of that, so something other than sampling moved it, and the design cannot say what. Anthropic's own reports name candidates: the influx of new users in early 2026, who bring lower-wage tasks, and the drift of coding toward agentic tools, which would thin the top quarter. Read as a claim about tasks in general rather than about these conversations, a design that resamples tasks resolves nothing below about fourteen to twenty percentage points. The honest generalisation is the direction and the mechanism, not the number.

What would change the reading is specific.

1. A later week in which the gap keeps its sign under every rule for drawing the quarters and pricing shared tasks, and after the largest tasks are dropped, would make the direction more than a sign.
2. A wage source that prices the computer occupations, which the only alternative available here does not, would make the check against a second wage source a real one.
3. A week with a published use-case cross could test whether personal requests, rather than software, explain the bottom of the pay scale.

Until then the answer to the title is its own two halves. On Claude.ai, high-wage work is delegated somewhat more often than low-wage work, and the whole of that excess is coding. Take the coding family out, and high-wage work is delegated less.

## Recommendations to Anthropic

**(i) The Economic Index should publish the collaboration split crossed with the wage quartile and with the occupational group, in the release itself.** Both halves already ship in the same file for the same week, and the cross is one join that no report has printed. It would not settle the question where it stays open: intersections are published at global grain only, so the cross would still blend countries inside a task.

**(ii) Whoever maintains the observed-exposure measure should report its automation weight twice, with and without Computer & Mathematical tasks.** The measure weights delegated use more heavily and is wage-blind by construction. The results here say that one occupational family carries the whole of the difference between delegation at the two ends of the pay scale, so a single weight hides the only composition that moves it. It would not help inside that family, where the exclusion leaves nothing to compare.

**(iii) Anyone quoting a published delegation share as a model input should say which average it is, and put the wage-weighted figure beside it.** In these weeks the two are within a point of each other, which is worth having in print rather than assuming. It would not close the gap for a model that weights by labour payments, because the correction measured here re-weights an hourly rate and no hours enter it.

## Limitations

The design observes how work was actually done, at task resolution, on more than eight hundred thousand classified conversations a week. Its costs follow from the same choice, in the order a referee would raise them.

1. **Composition, not price, and this withdraws a claim.** The best-paid quarter is two thirds to three quarters coding, and the gap reverses without it, within occupational groups, and when the ten largest tasks are dropped. A task's wage is the wage of the occupation it resembles, so the design cannot separate what the work pays from what the work is. The post does not write "delegation depends on the wage of the work" in either direction. The direction of this bias is unsigned: the confound could as easily be masking a pay relation as manufacturing one.

2. **The country mix inside a task.** A task's global delegation rate blends countries and cannot be rebuilt from the country files. Lower-usage countries delegate more in Anthropic's own regression; if the best-paid tasks draw relatively more from high-usage countries, which the data cannot confirm, the bias runs against the reported sign. Seychelles in November is the one bounded case, worth up to three points, not enough to account for that week's excess.

3. **The size is unstable between weeks.** Two thirds of a point in one week, more than seven in another, against within-week intervals of about three tenths of a point. The intervals are the wrong uncertainty for any statement that spans weeks, and the pre-registered power calculations assumed a constant true gap, which the three estimates refute. Every interval is also a lower bound, because no release carries a user or session identifier to cluster on.

4. **The top quarter is small, and the conclusion flips at known thresholds.** Its effective size is 10.6, 8.9 and 16.4 tasks; the two largest software-modification tasks are a quarter to two fifths of its conversations; and the third-quartile boundary sits on one computer occupation's wage, so sort order places 5 to 7 points of the top quarter's conversations. The fractional quartile rule takes August below one point, and the modal-holder wage rule takes February below zero.

5. **There is no independent second wage source.** The BLS Employment Projections table prices about a tenth of the coding family, so rebuilding the gap on it reproduces the coding exclusion rather than checking the wage. No independent source has confirmed the sign, and none is available while the shipped O\*NET file carries 2010 occupation codes.

6. **The use-case rival is under-tested.** It can be tested in two weeks, sits on the boundary in one, and cannot be tested in August. A leg that does not fire is nothing shown.

7. **The construct.** "Delegated" is directive plus feedback loop, and the two move in opposite directions across the pay scale, so the headline is a feedback-loop finding. Delegation is not autonomy and is not displaced labour, and the wage-weighting correction re-weights an hourly rate with no hours in it. The wage level built here does not reproduce Anthropic's published task-value series, which is why every result is a rank contrast and no dollar level in this post is Anthropic's.

8. **The generalisation bound.** As a statement about tasks rather than about these weeks' conversations, the design resolves nothing below about 14 to 20 percentage points, twice the largest gap reported and many times the smallest.

## How the analysis was done

**Data.** Three Economic Index releases, one week each: `release_2025_09_15` (4–11 August 2025, Claude AI Free and Pro), `release_2026_01_15` (13–20 November 2025) and `release_2026_03_24` (5–12 February 2026, Claude AI Free, Pro and Max). The cut is the task-by-collaboration intersection at global grain, with the same week's per-task conversation share as the weight. Tasks are priced through the shipped O\*NET task statements to the wage file in `release_2025_02_10`, joined on the full O\*NET-SOC code, with median salary divided by 2,080 for an hourly rate and averaged over holding occupations by employment. The BLS Employment Projections table is the second wage source, used for rank and sign only. Analysis set: the 1,802 / 2,075 / 2,188 named global tasks with a wage and at least one classified collaboration cell, 97.15 / 96.23 / 96.52% of named-task usage, 818,673 / 854,432 / 848,716 classified conversations, Kish effective 94 / 83 / 126 tasks; the 805 / 1,079 / 1,056 tasks with a wage and no classified cell and the 5 / 12 / 12 with a cell and no wage are dropped, never zeroed.

**Measures.** The outcome is Anthropic's own column, the percentage of classifiable collaboration that is automation-focused (directive and feedback-loop patterns), on the classifier's definition of directive as complete delegation with minimal interaction. It is not a count of tasks automated and not autonomy. The price of a task follows Anthropic's construct, the average hourly wage of US workers who perform it, averaged over holders by employment, and the quartiles are cut by conversation volume as Anthropic's own wage-quartile figures are. The design is rank-based because the wage level does not reproduce Anthropic's published series on matched weeks.

**Models.** The headline gap and the composition legs are estimated with the task mix held fixed on a conversation-level binomial; intervals are two-sided 95% and are lower bounds under within-task dependence. A design-based variance that resamples tasks is reported beside them as the generalisation bound. The wage-weighting correction is the covariance of wage and delegation share across tasks divided by the mean wage. The slope is a usage-weighted regression of the per-task share on the hourly wage, reported for sign and significance only.

**Stress tests, all pre-registered.** Two alternative rules for pricing tasks that several occupations hold, two alternative quartile allocations, a minimum-conversation floor of 100, two Seychelles cuts, a design-based variance model, a permutation placebo, the second wage source, a fourth task-level week on the unchanged taxonomy, a leave-one-group-out series over all twenty-two major groups, and a ten-largest-tasks leave-out. Every confirmatory quantity was produced twice by two independent code paths; the largest disagreement between them is 1.8 × 10⁻¹⁴ points, and the bootstrap standard errors are within 0.9% of the closed form and cover 95.2–95.3%.

**Reproduction of the published numbers first.** Each week's own five-pattern delegation share reproduces at 51.07 / 46.74 / 45.55% against the published 49 / 45 / 44% on the all-conversation base, and Anthropic's released country regression returns its published figure exactly (−3.112, partial R² 0.394, N 111).

## What was fixed before the data were run

The pre-registration is `posts/post1/prereg/prereg.md`, committed at `066b761` before any primary test was run. What had been seen at that point was the shape of the quartiles without their outcome: the boundaries, the coding family's share of the top quarter, the use-case mix by quarter, the effective counts and the Seychelles figures. Nobody had computed the gap, any quarter's delegation share, any composition leg or the placebo.

The confirmatory set was counted in advance: 17 confirmatory estimates, of which 8 are the composition legs, plus 3 exploratory tests labelled as such. Seventeen and three are what was run. The smallest effect of interest was one percentage point on the headline gap, chosen so the rule could fail, with a realised minimum detectable effect of 0.40 / 0.39 / 0.39 points a week at 80% power.

Three deviations were logged, each with the registered rule and the corrected rule both run and both reported: (i) the tie order at the $43.40 boundary wage, made reproducible and paired with an order-free fractional rule that declares the same outcome; (ii) a two-percent agreement tolerance on a ratio that no implementation could meet, replaced by the linear contrast the pre-registration already required; and (iii) the permutation placebo's size band, widened from one to two points, which did no work because the realised size fell inside the original band.

## Reproducing this post

The analysis is eight numbered scripts run in order, each ending in a check block that stops on a wrong number: `02_build.py` through `09_results_and_figures.py`, preceded by `01_power_rules.py`, which loads no data. The inputs are five public Economic Index release bundles and the BLS Employment Projections table. The page is rebuilt from the write-up and the outputs by

```
python3 site/tools/build_page.py post1
python3 site/tools/verify_page.py post1
```

The verifier extracts every number from the write-up and from the built page and matches each to an entry in `posts/post1/data/processed/results.json` through `posts/post1/notes/claims-map.json`; it fails on a mismatch or on a number bound to nothing. Every script, its check output and its tables are in the drawers under each section of this page, as the analyst wrote them; the pre-registration, the lab notebook and the red-team memo are under the methods section.

## How Claude was used, and how it was checked

Every part of this post was produced by Claude models working to a fixed division of labour and a file-ownership rule: one thread wrote the brief, one confirmed the data at column level, one wrote the pre-registration and the scripts, one refereed, and one wrote the page. No thread edited another's files.

Four things were done to catch the work being wrong. (i) Every confirmatory quantity was implemented twice by code paths that share no estimation step, with a synthetic-recovery test for every estimator. (ii) The referee re-derived the headline numbers from the raw release files with its own code and no import from the analysis scripts, and they reproduce to floating-point tolerance. (iii) A red-team memo put the strongest case against each finding before the write-up began, and a claims list written after verification fixed which sentences the evidence licenses; several sentences that would have read better are absent because that list forbade them. (iv) The page build fails if any number on the page is not in `results.json`. What none of that catches is a shared misreading of what a released column means, which is why the definitions above are Anthropic's own.
