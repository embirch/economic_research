# Generative AI users more often report unpaid job work in their own time: a gender comparison of Canadian employees

## Introduction

**Generative AI makes individual work tasks faster to finish. What happens to the time it saves is a separate question, and a more consequential one for the people doing the work.**

Time saved on a task can end a worker's day earlier. It can be filled with more tasks of the same kind, so that output rises while the working day stays the same length. It can be spent on work the person could not previously take on at all. These are different outcomes for the worker, and more than one of them can happen to the same person.

There is evidence for each of them, which is why the destination of saved time cannot be assumed. Anthropic's analysis of 100,000 conversations on [Claude.ai](https://www.anthropic.com/research/estimating-productivity-gains) estimates, using the model's own judgements of how long tasks take, that AI assistance cuts the time a task requires by about 80%; randomised trials of narrower tasks have reported smaller savings, and in one case no saving at all. In a separate [survey of 81,000 Claude users](https://www.anthropic.com/research/81k-economics), among the respondents who said who was benefiting from their own productivity gains, most named themselves, through faster tasks, wider scope and freed-up time. One in ten said instead that employers or clients were asking for and getting more work. One software developer in that survey described project managers responding to AI by handing out "harder and harder tickets and bugs to solve". Both of those sources describe self-selected users of one AI product rather than a national workforce, which is a reason to look at a general-population survey.

**Unpaid job work during personal time is one part of this that can be observed directly.** It means work done to meet the demands of a job, outside paid hours and without pay: finishing a report in the evening, clearing messages at the weekend. It competes with rest, family commitments and everything else a person does when not working. If AI saves an employee time and that employee keeps it, unpaid job work is one of the things that should fall. If the saved time is absorbed by additional work, it need not fall at all.

**How jobs reward time is also one of the better-supported explanations of the gender earnings gap.** [Claudia Goldin's account](https://www.aeaweb.org/articles?id=10.1257/aer.104.4.1091) is that many occupations pay disproportionately for long hours and for availability at particular times, and that this, rather than different pay for identical work, drives much of what remains of the gap. A technology that changes how work fits into time therefore has no particular reason to be neutral between women and men. Whether the working conditions accompanying AI use actually differ by gender is a question to answer rather than assume.

The answer also bears on how adoption statistics are read. Gender gaps in generative AI use are now well documented, and the [foundational review by Cranney, Delecourt and Koning](https://www.hbs.edu/ris/Publication%20Files/25-023_be8fb517-3dd5-40aa-97f9-4e42e1c8e6ff.pdf) reads them as likely gaps in access to the technology's benefits. That step assumes participation delivers the benefit. Participation is straightforward to count. What happens to the people who participate is not, and a survey that measures both on the same respondents can show whether the two move together.

Canada's [2024–2025 Survey on Working Conditions](https://www150.statcan.gc.ca/n1/pub/14-25-0001/142500012026001-eng.htm) asks both questions of the same people. It records whether a respondent used generative AI tools for their main job, and how often that respondent does job work during free time without pay. [Hahmann and Lovei](https://www150.statcan.gc.ca/n1/pub/75-006-x/2026001/article/00007-eng.htm) have already described Canadian adoption and its occupational and gender patterns from this source. This study adds the unpaid-work comparison, and asks what the gender contrast looks like when users and nonusers are placed on the same broad job distribution.

The analysis covers **20,538 employees aged 15 to 69 in Canada's ten provinces who answered about a main job in the public or private sector**. That job is the survey's reference job, and for a minority of respondents it is one they have already left. Self-employed respondents are not included.

Three definitions govern everything that follows. **Unpaid work here means work for the job**, not domestic or caring work. **The outcome is a frequency rather than a quantity**: respondents report how often they do such work on a five-point scale running from daily to never, and never how many hours it takes. **AI use means any reported use** for the reference job during the relevant 12 months, so an employee who used it weekly and one who used it once are both counted as users. Men+ and Women+ are the survey's published gender categories, which absorb some nonbinary respondents to protect confidentiality.

The survey observes users and nonusers at one point in time, and nobody is seen before and after they start using AI. It can describe the unpaid-work demands that accompany AI use. It cannot establish that AI raised or lowered them.

### Research questions

For these Canadian employees, the study asks:

1. Within each gender group, are those reporting generative AI use for their job more likely than nonusers to report unpaid job work **daily or several times a week**?
2. Is the **percentage-point difference between users and nonusers** larger for Women+ or Men+?
3. How does that gender comparison change when all four groups are given the **same broad occupation-and-sector mix**?

The short answer is that **users report frequent unpaid job work far more often than nonusers, and that this holds for women and men alike.** In the observed Canadian workforce the gap is larger for Women+ measured in percentage points, but it is not larger in proportional terms, and the ordering does not survive placing the four groups on a common job mix. The association is the finding that holds up under every comparison tried. The gender ranking is not.

## Generative AI users report frequent unpaid job work more than two and a half times as often as nonusers, in both gender groups

Among Women+, [16.3% of users and 6.2% of nonusers](figures/frequent-work.csv) report doing unpaid job work in their free time daily or several times a week. Among Men+ the rates are 10.6% and 3.9%.

<!-- FIGURE: frequent-work -->

In percentage points, that is a gap of [10.1 points for Women+ and 6.7 points for Men+](public-tables.csv): about ten more Women+ users per hundred than Women+ nonusers, and about seven more among Men+. These are differences between two groups of people observed at the same time, not people whose unpaid work went up.

**In proportional terms the association is almost identical in the two groups.** Measured against each group's own nonuser rate, the user rate is about [2.6 times as high for Women+ and 2.7 times as high for Men+](scale-comparison.csv). The absolute gap is the larger one for Women+ because their nonuser rate is already higher, 6.2% against 3.9%, and a similar proportional association applied to a higher starting rate produces a bigger difference in percentage points. The difference between the two gaps is **3.4 percentage points**, with a 95% sampling interval of 0.5 to 6.3 points.

**The pattern is not an artefact of where the threshold was placed.** The whole frequency distribution shifts. Among Men+, the share reporting that they never do unpaid job work falls from 81.4% of nonusers to 56.2% of users; among Women+ it falls from 75.8% to 53.4%. The two intermediate categories, several times a month and once a month or less, are both more common among users in both gender groups.

<!-- FIGURE: frequency-profile -->

These rates describe employees as they are actually distributed across jobs. The four groups do not hold the same mix of occupations and sectors, and frequent unpaid job work is much more common in some of those categories than others. The next comparison asks what the gender contrast looks like once that difference in job mix is taken out.

## The gender comparison depends on which job distribution is being described

**A common job mix gives all four groups the same shares of broad occupation-and-sector combinations.** The survey's eight broad occupational groups and two sectors make 16 combinations. Each group's overall rate is then rebuilt using the pooled share of all employees in each combination in place of its own share. A given combination, health occupations in the public sector for instance, contributes the same amount to every group's rate, even where it accounts for a far larger part of one group's actual employment than another's. All 20,538 employees stay in the calculation. Only the weight attached to each job category changes.

At this common mix, [10.6% of Women+ users and 6.1% of Women+ nonusers](public-tables.csv) report frequent unpaid job work. Among Men+ the rates are 11.0% and 4.8%. Users still have the higher rate in both gender groups, which is the result that does not move. What moves is the comparison between the groups: the Women+ gap becomes the smaller of the two, and the Women+-minus-Men+ difference between them is now **−1.7 percentage points**, with a 95% sampling interval of −5.2 to 1.7 points.

**That interval allows either group to have the larger association.** It is not evidence that the two are equal, and the negative point estimate is not a demonstrated reversal.

<!-- FIGURE: composition -->

Setting the available comparisons side by side shows how much the answer depends on the description chosen. Only the observed-workforce estimate has an interval excluding zero. Moving from the observed workforce to the common job mix changes the gender contrast by [−5.1 percentage points](public-tables.csv), with an interval of −7.7 to −2.6 points. That shift comes from reweighting the same 20,538 employees. Nobody is dropped from the calculation, and nobody's reported work changes.

**One group's rate does most of the moving.** Applying the pooled job mix lowers the Women+ user rate from 16.3% to 10.6%, while the Men+ user rate goes from 10.6% to 11.0%. Women+ who report using AI are concentrated in broad job categories where frequent unpaid job work is more common. That is a statement about where people work, obtained by arithmetic on the same respondents. It does not establish that those occupations cause the unpaid work, and the 16 categories are wide enough to contain jobs with very different responsibilities, deadlines and working arrangements.

A [check that removes each of the 16 job categories in turn](influence-summary.json) indicates that this sensitivity belongs to the comparison rather than to one unusual category. Across all 16 restricted populations the common-mix contrast ranges from −2.6 to +0.1 points, and every one of the 16 intervals includes zero. The shift away from the observed-workforce figure stays negative in all 16, although its size varies. Each deletion describes a different and smaller population, so none of them is an alternative estimate for Canada.

**A separate model gives a third answer, for reasons that cannot be separated.** Adjusting additively for age, education, occupation, industry and sector gives a gender contrast of [2.7 points, with an interval of −0.2 to 5.6 points](public-tables.csv). That model uses more variables than the common-mix calculation, but it imposes the same adjustments on all four groups. The common-mix calculation uses fewer variables, but lets each group keep its own rate inside every job combination. The variables and the modelling assumptions both differ, so the distance between 2.7 and −1.7 cannot be attributed to either of them alone.

Taken together, the four estimates establish that **the gender ranking is a property of the comparison being made rather than a stable feature of Canadian employees**. They do not show that job composition accounts for the difference, and they do not show that women and men are equally placed.

## Discussion

**Counting who uses AI does not describe how those people are working.** In Canada in 2024 and 2025, the employees most likely to report using generative AI for their jobs were also the employees most likely to report working unpaid in their own time, by a wide margin and in both gender groups. Participation and working conditions are measured here on the same respondents, and they do not line up the way a benefits reading of adoption would predict.

This is the study's main addition to how gender gaps in AI use are interpreted. A participation gap is commonly treated as a gap in access to the technology's advantages. These data neither refute that interpretation nor measure a benefit. What they show is that the more participating group is not thereby the group with lighter demands on its personal time. Participation cannot stand in for workers' experience, and a claim about who benefits needs a measure of the benefit.

**The gender result is the more modest of the two and should be stated as such.** Women+ employees who use AI report the highest rate of frequent unpaid job work of the four groups, at 16.3%, and they also start from the highest nonuser rate. Proportionally, the association between use and unpaid work is close to identical for Women+ and Men+. Once broad job categories are held to a common distribution, the point estimates no longer favour either ordering. The defensible reading is that this is a pattern Canadian women and men who use AI share, and that the extra percentage points among women follow from their higher baseline rate and the job categories they occupy.

**Which way the relationship runs is genuinely open, and that governs what the result can be used for.** Employees facing heavy demands may be the likeliest to reach for a tool that saves time, in which case the association describes who adopts rather than what adoption does, and those same employees could be doing less unpaid work than they would without it. The randomised evidence points that way. In a [field experiment by Dillon and colleagues](https://arxiv.org/html/2504.11436v4), giving workers access to an integrated generative AI tool reduced recorded activity in digital applications outside normal hours. That measure captures application telemetry rather than all work, and cannot establish whether the work was paid. The two results do not conflict. One describes what granting access did; the other describes which existing users and nonusers carry which demands.

Settling the direction would take observations of the same workers before and after a change in access, alongside a comparison group that did not get it. Adding hours to the frequency measure would show whether frequent unpaid work is also long unpaid work, and pay and output would show whether saved time returns to the worker or is converted into more production. None of that is available here, and the present finding does not depend on it. High reported AI participation sitting alongside high unpaid-work frequency is itself the result, it is large, it is shared by both gender groups, and it survives every adjustment attempted.

For an employer or a statistical agency tracking AI at work, that suggests one concrete change. Adoption rates are already collected. Collecting the demands on employees' own time beside them, and reporting both the workforce as it stands and the comparison at a common job mix, would show whether a rising adoption rate comes with lighter or heavier calls on personal time. On the Canadian evidence, those two series would not have told the same story.

## Methodology

### Population, measures and uncertainty

The analysis uses the 20,538 public- and private-sector reference-job employees in the [Canadian Survey on Working Conditions 2024–2025 public-use file](https://www150.statcan.gc.ca/n1/pub/14-25-0001/142500012026001-eng.htm), collected between 23 September 2024 and 18 July 2025 and pooled. The four groups contain 7,993 Men+ nonusers, 2,224 Men+ users, 8,080 Women+ nonusers and 2,241 Women+ users. These are respondent counts, not population totals.

Rates use the producer's survey weights, and all sampling intervals use its 1,000 public bootstrap weight sets. The intervals describe sampling uncertainty only. They do not cover measurement error, imputation, recall or the choice of comparison. Common-mix intervals carry uncertainty in both the group rates and the estimated job distribution, and the interval for the change in the gender contrast also accounts for the dependence between the two estimates it compares. The [methods appendix](methods.html), [published estimates](public-tables.csv) and [analysis code](analysis.py) document every comparison, support check and release rule.

The ten-province frame excludes the territories, institutionalised people, full-time Armed Forces members, and people on reserves and other Indigenous settlements. Estimates do not describe all Canadian residents or all jobs. The survey guide reports that 4.9% of the whole survey sample answered about a job or business already left; that figure covers the whole sample rather than this employee subset, and the variable identifying those respondents is absent from the public file. For them, the 12-month questions concern their last year in the reference job.

The source's published whole-file generative AI benchmark of 22.1% includes self-employed respondents and is not the employee adoption rate used here. Both Men+ daily-frequency estimates in the full distribution carry the source's use-with-caution warning.

### Supporting comparisons

The common occupation-and-sector mix covers 16 combinations and retains the whole employee sample, so restricting the sample changes nothing by construction. Adding education gives a Women+-minus-Men+ contrast of [−1.0 percentage points](public-tables.csv), with an interval of −4.5 to 2.5 points, retaining 20,413 respondents and 99.4% of employee survey weight. The smallest component gender-and-use cells hold three respondents for occupation and sector, and one after education is added. Those component rates are not published, and the pooled estimates carry that sparse-component limitation.

The separate statistical model adjusts for categorical age, education, broad occupation, broad industry and sector alongside gender, use and their interaction. It is an additive linear projection with adjustments shared across the four groups. It does not compare otherwise identical jobs and does not estimate a causal effect.

The bounded influence check removes each of the 16 occupation-and-sector combinations once from all four groups, then recomputes both the group rates and the common mix. Contributions to the reweighting shift are concentrated: the largest single category accounts for 46.8% of the total absolute contribution and the largest three for 67.0%, with positive and negative contributions offsetting, so these are not shares of the net change explained. Ten of the 16 categories contain at least one gender-and-use group with fewer than 75 respondents, together covering 41.5% of the pooled target weight. The same deletions leave the observed-workforce contrast positive in all 16 point estimates, ranging from 0.0 to 4.9 points, with 14 of its 16 intervals excluding zero. Each result describes its own restricted population, the intervals are pointwise and dependent, and none replaces the national estimate. The [reproducible diagnostic](influence_check.py) and its [public summary](influence-summary.json) record support, concentration and sampling intervals; fine-cell results stay private under the source's release rules.

A further diagnostic that also held age constant failed, because required cells were empty in two bootstrap replicates. It is retained as a failure rather than published as an estimate.

### Interpretation and prior research

Neither the order of events nor any change within an individual is observed. Recall, donor imputation, unmeasured job demands and selection into use introduce limits beyond the sampling intervals. No estimate here measures total working hours, productivity, wages, personal time gained or employees' preferences. Suppressed small estimates and raw respondent records are not released.

[Hahmann and Lovei](https://www150.statcan.gc.ca/n1/pub/75-006-x/2026001/article/00007-eng.htm) already describe Canadian adoption and occupational patterns, and this study makes no claim to have found the adoption gap. [Jiang, Park, Xiao and Zhang](https://faculty.marshall.usc.edu/Gerard-Hoberg/CETAFE/papers/paper7.pdf) relate occupational AI exposure to diary-based work and leisure time, including gender and household differences, using measures different from those used here. The contribution of this study is the Canadian combination of reported use with unpaid-job-work frequency on the same respondents, and the explicit side-by-side reporting of the observed workforce and the common job mix. AI and working time are established research topics, and no first finding is claimed. The [literature note](literature-review.md) records the exact source versions, how deeply each was read, and the latest Jiang full text that could not be accessed.

Adapted from Statistics Canada, Canadian Survey on Working Conditions, 2024–2025. This does not constitute an endorsement by Statistics Canada of this product.
