# E08 Canada: argument brief

Developmental brief for the proposed redraft. Internal working document, not reader-facing prose. Prepared by the managed Claude Editor on the safe pilot branch before drafting, as required by `../../editorial-method-2026-10-09/PROPOSED-METHOD.md` §1.

## 1. The economic question, and why gender belongs in it

Generative AI reliably shortens the time a worker needs to finish a particular task. That is the best-evidenced economic fact about the technology so far, and it is measured at the level of the task: Anthropic's analysis of 100,000 Claude.ai conversations puts the median estimated saving at about 80%, and randomised trials in narrower settings report savings between negative and 56%.

A saving on a task is not the same thing as a change in a worker's day. The saved time has to go somewhere, and the economically interesting question is where. It can be returned to the worker as time not worked. It can be absorbed by additional tasks of the same kind. It can be converted into work the person could not previously do at all. These are different outcomes for the worker, and the evidence shows they all occur. In Anthropic's survey of 81,000 Claude users, among those who named a beneficiary of their own productivity gains, most named themselves, while 10% said their employer or clients were asking for and receiving more work.

So the open question is not whether AI saves task time. It is which workers end up with more of their own time and which end up with more work. That is a distributional question, and it is the question this article engages.

Gender enters for a specific reason, not as a default category. Claudia Goldin's account of the remaining gender earnings gap turns on the fact that many jobs pay disproportionately for long hours and for work at particular times. If that is right, then a technology that changes how work fits into time is not gender-neutral in its consequences, whatever its average effect. Whether the working conditions that accompany AI use differ between women and men is therefore a question worth asking directly rather than assuming.

This also sharpens an interpretation now common in the gender-and-AI literature. The foundational review by Cranney, Delecourt and Koning reads a gender gap in AI participation as a likely gap in access to AI's benefits. That reading requires an assumption: that participating in the technology delivers the benefit. Participation is observable. Benefit is not, at least not from participation data alone. A dataset that measures both on the same people can test whether the assumption looks safe.

## 2. What this dataset actually observes

Statistics Canada's Canadian Survey on Working Conditions, 2024–2025 public-use file, asked the same respondents two things that are rarely asked together:

- whether they used generative AI tools for their main job, at any point in the relevant 12 months;
- how often they do work for that job during their own free time, without pay.

**Population.** 20,538 respondents aged 15 to 69, in the ten provinces, who answered about a reference job as an employee in the public or private sector. Self-employed respondents are excluded. The territories, institutionalised people, full-time Armed Forces members and people on reserves are outside the survey frame. For a minority of respondents the reference job is one they have already left; for them the 12-month questions concern their last year in that job.

**Period.** Collection ran from 23 September 2024 to 18 July 2025, pooled. There is no usable wave variable permitting a trend, and no panel: nobody is observed before and after starting to use AI.

**The AI measure.** Any reported use, not intensity, not frequency, not employer provision, not adoption date.

**The outcome measure.** An ordered frequency: daily, several times a week, several times a month, once a month or less, never. The study's threshold is the top two categories. It is a count of occasions, not hours, and it concerns job demands, not domestic or caring work. Nobody reports how long the unpaid work took.

**Gender.** Men+ and Women+, the source's confidentiality-protected categories, which absorb some nonbinary respondents.

**The comparison.** Four groups: Men+ nonusers (7,993), Men+ users (2,224), Women+ nonusers (8,080), Women+ users (2,241). The primary statistic is the difference between the two user-minus-nonuser gaps.

**What the design cannot do.** It compares people who use AI with people who do not, at one point in time. It cannot say what happened to anyone after they started using AI.

## 3. What the results jointly establish

The useful reading is that one result is robust and a second is not, and that the contrast between them is the finding.

**Robust.** Users report frequent unpaid job work far more often than nonusers, in both gender groups, by a wide margin. Women+: 16.3% against 6.2%. Men+: 10.6% against 3.9%. The association survives every comparison attempted. It holds at a common broad job mix (Women+ 10.6% against 6.1%; Men+ 11.0% against 4.8%) and in the additive model. It is not an artefact of the daily-or-weekly threshold: the whole frequency distribution moves, and the share reporting they never do unpaid job work falls by about 25 points among Men+ and about 22 points among Women+.

**Not robust.** Which group has the larger gap. The Women+-minus-Men+ difference between gaps is +3.4 points [0.5, 6.3] in the observed workforce, +2.7 [−0.2, 5.6] in the additive model, −1.7 [−5.2, 1.7] at a common occupation-and-sector mix, and −1.0 [−4.5, 2.5] once education is added. Across all 16 single-stratum deletions the common-mix estimate runs from −2.6 to +0.1 and every interval includes zero.

**Why the gender comparison moves, in plain terms.** Two published facts explain most of it, and the article should say so rather than leave the reader with four numbers.

1. *Proportionally the association is almost the same in both groups.* The user rate is about 2.7 times the nonuser rate for Men+ and about 2.6 times for Women+. Women+ nonusers already report frequent unpaid job work more often than Men+ nonusers, 6.2% against 3.9%. A similar proportional association applied to a higher starting rate produces a larger gap measured in percentage points. The +3.4-point result is substantially a statement about the different baselines, not about a different relationship.
2. *The Women+ user rate is the one that responds most to reweighting.* Giving all four groups the same broad occupation-and-sector mix moves the Women+ user rate from 16.3% to 10.6%, while the Men+ user rate moves from 10.6% to 11.0%. Women who report using AI are concentrated in broad job categories where frequent unpaid job work is more common. That is composition arithmetic. It identifies nothing about what occupations cause.

**The joint conclusion.** In Canada in 2024 and 2025, reported generative AI use and frequent unpaid job work go together strongly, and they go together for women and men alike. The data do not support a claim that AI use is distinctively associated with unpaid work for women. What looks like a gender-specific pattern in the observed workforce is largely a higher female baseline plus the job categories in which women who use AI are employed.

This is useful beyond a list of rates because it separates a conclusion that survives every reasonable way of describing the population from one that does not, and explains the difference.

## 4. Closest prior work and the actual increment

- **Hahmann and Lovei (Statistics Canada, June 2026)** already describe Canadian generative AI adoption, its occupational pattern and its gender pattern. This article does not rediscover the adoption gap and should not imply that it does.
- **Jiang, Park, Xiao and Zhang** relate occupational AI *exposure* to diary-measured work and leisure time, with gender and household breakdowns. Their design precedes this one and uses different measures. Their February 2026 full text could not be accessed; the readings on record are the August and October 2025 drafts. No stronger novelty claim is available.
- **Dillon, Jaffe, Immorlica and Stanton** randomised access to an integrated generative AI tool and found *less* recorded activity in digital applications outside regular hours. That is an experiment; this is a cross-section. Their telemetry does not capture all work and cannot say whether it was paid.
- **Cranney, Delecourt and Koning (May 2026)** supply the interpretation this article qualifies: a participation gap read as a benefits gap.

**The increment.** Reported generative AI use and unpaid personal-time job-work frequency measured on the same Canadian employees, with the observed-workforce and common-job-mix descriptions reported side by side rather than one presented as the correct answer. No first-ever claim. No causal effect.

## 5. Alternative interpretations that genuinely change the conclusion

1. **Selection into use.** Employees under heavier job demands may be likelier to adopt AI. On this reading the association reports who adopts, not what adoption does, and the same workers might be doing *less* unpaid work than they would without the tool. This interpretation is fully consistent with the data, and it reconciles the positive Canadian cross-section with Dillon and colleagues' negative experimental result. It does not weaken the article's actual claim, which is about co-occurrence in a measured population, and it is the reason the article must not drift into causal language.
2. **Unmeasured job content within broad categories.** Sixteen occupation-and-sector cells contain very different jobs. Managerial responsibility, deadlines, client exposure and seniority vary inside them and are not observed. This limits how much the common-mix comparison can be said to hold "the job" fixed.
3. **Reporting behaviour.** People who use AI for work may simply be more conscious of, or more willing to report, work done in their own time. Nothing in the data rules this out.
4. **Reference jobs already left.** A minority of respondents answer about a former job, and the variable identifying them is absent from the public file.

Interpretations 1 and 3 would change what the association means. Neither changes the measured pattern, and the article's conclusion is written to survive both.

## 6. Figures: what each one is for

**Figure 1, `frequent-work`: the four rates.** Carries the central result and, just as importantly, shows the reader the two nonuser baselines (6.2% and 3.9%) that explain why the absolute gap is larger for Women+. Without this figure the later discussion of baselines has nothing to point at. Placed immediately after the first results heading.

**Figure 2, `frequency-profile`: the full five-category distribution.** Answers the first objection an economist will raise, namely that the result is a threshold artefact. It shows the whole distribution shifting, with the never category falling sharply in both groups. It renders as an optional disclosure, which is the right weight: supporting evidence a sceptical reader can open. Moved from the Methodology section into the first results section, immediately after the claim it defends.

**Figure 3, `composition`: the four gender contrasts.** Shows the reader in one view that the sign of the gender comparison depends on which population is described, and that the uncertainty bands overlap zero for three of the four. Its argumentative job is to make the fragility visible rather than asserted. Placed after the common-mix rates are introduced, so the reader already knows what the third row means.

The time-off figure stays out of the article. Its copy entry is retained unchanged in `presentation-copy.json` because the builder requires an entry for every figure specification.

## 7. Paragraph plan

**Title.** Names the subject, the precise outcome and the population.

**Introduction.**
1. AI saves time per task; where that time goes is the open question. Three destinations, named, with evidence that all occur.
2. Unpaid job work during personal time is one directly observable part of the answer, and what it means for a worker.
3. Why the gender comparison is worth making: Goldin's argument about how jobs reward time, flagged as motivation.
4. The survey, what it measures on the same people, and the honest statement of what a cross-section can and cannot show.
5. Population, measure definitions, gender categories.
6. The three research questions, stated once.
7. The answer in advance.

**Results section 1: the association.** Four rates; figure 1; the two gaps and their difference; the proportional comparison and the baseline explanation; figure 2 defending the threshold; transition to job composition.

**Results section 2: the gender comparison depends on the job distribution.** What a common mix is, concretely; the four common-mix rates; the contrast and its interval; figure 3; the size of the shift and which rate moves; the influence check; the additive model and why it differs; what the set of estimates supports.

**Discussion.** The supported insight about participation versus experience; the selection interpretation and the experimental contrast; what would actually settle it; the bounded practical reading.

**Methodology.** Population, measures, uncertainty; supporting comparisons and their limits; interpretation, prior research and attribution.

## 8. Lines the draft must not cross

- No statement that AI increases hours, unpaid work, output or pay.
- No statement that women receive fewer benefits from AI.
- No statement that occupation "explains away" the gender difference.
- No presentation of the negative common-mix estimate as a reversal.
- No presentation of an interval containing zero as evidence of equality.
- No conclusion whose content is only that better data are needed.
