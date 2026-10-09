# Generative AI use and unpaid job work: a gender comparison in Canada

## Introduction

**Making tasks faster does not necessarily mean that workers are working less.** Time saved on one task can allow a shorter working day, more output or different responsibilities. Which follows depends on demand for output and how jobs are organised.

For workers, one relevant outcome is **unpaid job work**: work done during personal time to meet job demands. It can compete with rest, family commitments and other activities. AI could help employees complete their work within paid time; additional output or responsibilities could also leave unpaid demands unchanged or increase them. Understanding workers' circumstances requires evidence about those demands alongside evidence of AI use.

**Working-time arrangements also matter for gender inequality.** [Claudia Goldin's research](https://www.aeaweb.org/articles?id=10.1257/aer.104.4.1091) connects gender pay gaps to how jobs reward long hours and work at particular times. This gives a reason to examine whether the working conditions accompanying AI use differ between women and men. A larger user–nonuser difference in one group might persist at a common broad job mix, or change when job distributions are made comparable. The distinction matters before describing the pattern as a general difference between women and men.

Canada's [2024–2025 Survey on Working Conditions](https://www150.statcan.gc.ca/n1/pub/14-25-0001/142500012026001-eng.htm) records job-related generative AI use and unpaid-work frequency for the same respondents. [Hahmann and Lovei](https://www150.statcan.gc.ca/n1/pub/75-006-x/2026001/article/00007-eng.htm) already describe Canadian adoption and occupational patterns. This study adds a comparison of unpaid-work demands among users and nonusers, and examines how the gender comparison changes when their job distributions are made comparable.

The analysis covers **20,538 employees aged 15–69 in Canada's ten provinces who answered about a main job in the public or private sector**. This is their “reference job”, the main job the survey asked about. Here unpaid work concerns the job, not domestic or caring work, and frequency does not tell us how many hours it takes.

AI use means any reported use for the reference job during the relevant 12 months, not how often someone uses it. Men+ and Women+ are the survey's published gender categories, which include some nonbinary respondents to protect confidentiality. The survey compares users with nonusers rather than following what happens when someone starts using AI. It can describe the unpaid-work demands accompanying use, but cannot determine whether AI increased or reduced them.

### Research questions

For these Canadian employees, the study asks:

1. Within each gender group, are those reporting generative AI use for their job more likely than nonusers to report unpaid job work **daily or several times a week**?
2. Is the **percentage-point difference between users and nonusers** larger for Women+ or Men+?
3. How does that gender comparison change when all four groups are given the **same broad occupation-and-sector mix**?

**AI users report frequent unpaid job work more often in both gender groups.** The absolute difference between users and nonusers is larger for Women+ in the observed workforce, but that ordering does not persist in the point estimates at a common broad job mix. The uncertainty at that common mix permits either gender ordering. The main finding is therefore a clear association with unpaid work, alongside a gender comparison that depends on which job distribution is described.

## AI users more often report frequent unpaid job work in both gender groups

Among Women+, [16.3% of users and 6.2% of nonusers](figures/frequent-work.csv) report it daily or several times a week. Among Men+, the corresponding rates are 10.6% and 3.9%.

<!-- FIGURE: frequent-work -->

The difference is about **10 more people per 100 among Women+, compared with 7 among Men+**: [10.1 and 6.7 percentage points](public-tables.csv), respectively. The difference between those associations is **3.4 points**, with a 95% sampling interval of 0.5–6.3 points. These are differences in observed prevalence, not additional people doing unpaid work because of AI.

**The larger absolute gap for Women+ is not a larger proportional association.** Relative to each group's nonuser rate, the user rate is roughly [2.6 times as high for Women+ and 2.7 times as high for Men+](scale-comparison.csv). These ratios simply describe the same four rates; the primary comparison remains the percentage-point difference, which expresses how common frequent unpaid work is in each group.

These rates describe the job distributions reported by the employees. The four gender/use groups represent different mixes of occupations and public/private sectors. The next comparison asks whether the larger absolute gap for Women+ persists when those groups receive a common broad job mix.

## The larger absolute gap for women is sensitive to how jobs are compared

**A common job mix gives each group the same shares of broad occupation-and-sector combinations.** For example, a public-sector occupation contributes the same share to each group's rate, even if it accounts for more of one group's actual employment. The shared distribution is the pooled employee distribution. All 20,538 employees remain included; only the weight given to each job category changes.

At this common mix, [10.6% of Women+ users and 6.1% of nonusers](public-tables.csv) report frequent unpaid work. Among Men+, the rates are 11.0% and 4.8%. Users still have the higher rate in both gender groups. The Women+-minus-Men+ difference between the two user–nonuser gaps is now **−1.7 percentage points**, with a 95% sampling interval of −5.2 to 1.7 points. This interval permits either group to have the larger association; it establishes neither a reversed gender pattern nor equal associations.

<!-- FIGURE: composition -->

Applying the common mix changes the gender contrast by **[−5.1 percentage points](public-tables.csv)**, with an interval of −7.7 to −2.6 points. The shift results from reweighting the same employees, not excluding some of them or observing a change in anyone's work.

The observed workforce comparison remains relevant because it describes employees in their reported jobs. The common-mix result shows why its larger Women+ gap should not become a general claim independent of job context. Broad categories still contain different tasks, responsibilities and working arrangements, and some component groups contain few respondents.

A [check removing each job category in turn](influence-summary.json) reinforces this caution. Applying a common mix still lowers the gender contrast in every restricted comparison, but the resulting point estimate ranges from −2.6 to +0.1 points and every interval permits either gender ordering. The shift is unevenly distributed across job categories, so it should not be presented as a stable reversed gender pattern.

**A separate adjustment model gives a different estimate.** Accounting for age, education, occupation, industry and sector gives a gender contrast of [2.7 points, with an interval of −0.2 to 5.6 points](public-tables.csv). That model applies shared adjustments across the four groups. The common-mix calculation uses only occupation and sector, but allows each group its own rate within every job combination. Both the variables included and the modelling assumptions differ; this comparison cannot attribute the discrepancy to either feature alone.

Together, the observed, model-adjusted and common-mix estimates support **sensitivity to the comparison being made**. They do not show that accounting for jobs generally removes the gender difference, or establish that occupations cause it.

## Discussion

**High AI participation can coexist with frequent unpaid job work.** Users report more of that work than nonusers in both gender groups, while the comparative gender result depends on the job distribution and adjustment used. Monitoring uptake alone therefore leaves an important part of workers' experience unmeasured.

More frequent unpaid work among users can coexist with genuine time savings from AI. Employees facing greater demands may be more likely to use the technology and could still do less unpaid work than they would without it. In a [randomised field experiment by Dillon and colleagues](https://arxiv.org/html/2504.11436v4), access to an integrated GenAI tool reduced recorded work in digital applications outside regular hours. That measure does not capture all work or establish whether it was unpaid. The experiment measures a change under assigned access; the Canadian survey compares existing users and nonusers. Their findings need not conflict.

For an employer evaluating AI adoption, tracking unpaid-work frequency and hours alongside participation would show whether demands on employees' personal time are changing. Observations before and after access changes, with a credible comparison group, could establish what the rollout causes. Output and pay would help distinguish time savings returned to workers from gains used to produce more. Gender comparisons should report employees' actual circumstances as well as clearly defined adjusted comparisons. This survey provides a benchmark for that evaluation, without establishing that AI raises total hours or gives women fewer benefits.

## Methodology

### Population, measures and uncertainty

The analysis uses 20,538 public- and private-sector reference-job employees surveyed between September 2024 and July 2025. Rates use the producer's survey weights; sampling intervals use its 1,000 public bootstrap weight sets. The [methods appendix](methods.html), [published estimates](public-tables.csv) and [analysis code](analysis.py) document the comparisons, support checks and quality rules. The intervals describe sampling uncertainty. Common-mix intervals include uncertainty in both the group rates and the estimated job distribution; the interval for the change in the gender contrast also accounts for the dependence between the two estimates.

The ten-province survey excludes specified groups, including institutionalised people, full-time Armed Forces members and people on reserves and other Indigenous settlements. Some respondents had already left the reference job. The guide's 4.9% figure describes the whole survey sample, not this employee subset; the public file cannot identify and remove these respondents. Their 12-month questions concern the last year in that job.

### Supporting comparisons

The common occupation-and-sector mix covers 16 combinations and retains the full employee sample. Adding education gives a Women+-minus-Men+ contrast of [−1.0 percentage points](public-tables.csv), with an interval of −4.5 to 2.5 points; 20,413 respondents and 99.4% of employee survey weight remain. The smallest component gender/use cells contain three respondents for occupation/sector and one after adding education. Their individual rates are not published, and the pooled estimates retain this sparse-component limitation.

The separate statistical model uses categorical age, education, occupation, industry and sector adjustments, alongside gender, use and their interaction. It is an additive projection with shared adjustments across the four gender/use groups. It does not compare otherwise identical jobs or estimate a causal effect.

The bounded influence check omits each of the 16 occupation/sector combinations once from all four groups, then recomputes both their rates and the common mix. Each result describes a different restricted employee population; none replaces the original estimate. The [methods appendix](methods.html) documents contributions, sample support, sampling intervals and the [reproducible diagnostic](influence_check.py). Fine-cell results remain private under the source's release rules.

The full unpaid-work frequency distribution below shows the five response categories behind the chosen daily-or-several-times-a-week threshold. Categories measure frequency, not duration. Both Men+ daily-frequency estimates carry the source's use-with-caution warning.

<!-- FIGURE: frequency-profile -->

### Interpretation and prior research

Neither temporal order nor changes for an individual are observed. Recall, donor imputation, unmeasured job demands and selection into use introduce limits beyond the sampling intervals. No estimate measures total working hours, productivity, wages or employees' preferences. Suppressed small estimates and raw respondent records are not released.

[Hahmann and Lovei](https://www150.statcan.gc.ca/n1/pub/75-006-x/2026001/article/00007-eng.htm) already describe Canadian adoption and occupational patterns. [Jiang, Park, Xiao and Zhang](https://faculty.marshall.usc.edu/Gerard-Hoberg/CETAFE/papers/paper7.pdf) examine occupational AI exposure and diary-based work and leisure time, including gender and household differences. The present study adds a comparison of reported use with unpaid-job-work frequency and makes its alternative job distributions explicit. The [literature note](literature-review.md) records source versions and the unavailable latest Jiang full text. AI and working time are established research topics; this study does not claim the first link between them.

Adapted from Statistics Canada, Canadian Survey on Working Conditions, 2024–2025. This does not constitute an endorsement by Statistics Canada of this product.
