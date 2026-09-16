# Exploratory detail: what income stands for

These sections were written as the exploratory analysis unfolded, after the pre-registered tests, and are kept in full here. The main text carries the summary.

## What income is doing

Income is not a mechanism. It is a bundle: education, English proficiency, digital infrastructure, the occupations of the people who use Claude, the maturity of the user base. Two results narrow the bundle.

**Personal use lowers delegation.** In the full model, each additional point of a country's conversations that are personal rather than work or coursework goes with 0.23 points less automation (interval −0.39 to −0.07). Richer countries use Claude more for personal purposes, as Anthropic's January 2026 report and Microsoft's Copilot data both find, and personal use is where people work things through rather than hand them over.

**Education lowers delegation in professional, judgment-heavy work, and not elsewhere.** June 2026 publishes automation share within each occupation group by country, which allows the same test inside each of 19 groups with enough countries. A first pass on four hand-picked groups suggested the effect sat in "learning-heavy" work. The full set says something more specific and less tidy. Education lowers handover most in the professional groups where the baseline automation share is already low: life, physical and social science (−2.0 points per standard deviation of tertiary enrolment, interval clear of zero), management (−1.3), healthcare practitioners (−1.3), business and financial operations (−1.1), and arts, design and media (−0.9, clear of zero). It does nothing in computer and mathematical work (−0.3), office and administrative support (−0.2), production, installation and repair, or protective service, the groups where automation runs at 56 to 74% everywhere. Across groups, the education coefficient does not track how much *learning* a group attracts (correlation −0.06); it tracks how low the group's automation share already is (correlation 0.38). And it is noisy: the April and May coefficients correlate at only 0.31 across groups, so any single group's number should be read loosely. *Richer, better-educated countries delegate less where the work involves judgment and there is room to choose; where the work is routine for the model, everyone delegates.*

*Figure 4. The education coefficient on automation share within each occupation group, May 2026, with the group's global automation share in brackets. Green marks are intervals clear of zero. The effect concentrates in professional groups with low baseline automation; routine and technical groups sit at zero.*


## Unbundling income: access and education

Income can be taken apart with public data. By country, the candidates for what it proxies are: the education level of prompts (Anthropic's human-education primitive), task complexity (human-only time), the work and coursework shares of conversations, the English share of conversations, internet users per hundred people (World Bank), and tertiary enrolment (World Bank). Each was added to the income model in turn, then all together, on the 100 countries with complete data. The rule, written down before the models were run, was that a candidate "carries" the income effect if it cuts the income coefficient by at least half while its own interval excludes zero.

| Model (all-country sample, N = 100) | Income coefficient per SD | Candidate coefficient per SD |
|---|---|---|
| Income only | −2.6 (−4.2, −1.0) | |
| + task complexity | −2.8 | +1.4 (−0.9, +3.7) |
| + work share | −2.6 | −0.2 (−1.1, +0.7) |
| + coursework share | −2.6 | +0.3 (−1.2, +1.8) |
| + English share | −2.5 | +0.4 (−0.9, +1.7) |
| + prompt education level | −2.1 | −0.8 (−1.8, +0.2) |
| + **internet users per 100** | **−1.1 (−2.7, +0.5)** | **−1.6 (−3.0, −0.3)** |
| + **tertiary enrolment** | **−1.2 (−2.9, +0.4)** | **−1.9 (−3.1, −0.7)** |
| + all seven | −0.3 (−2.3, +1.8) | |

Two candidates pass the rule and none of the others comes close. **Internet penetration** cuts the income coefficient by more than half and is clear of zero on its own; **tertiary enrolment** does the same. Entered together with income, they absorb it entirely: income falls to −0.2 with an interval spanning zero, tertiary enrolment keeps −1.6 (interval −2.8 to −0.5), and internet keeps −1.2 with an interval that just crosses zero (−2.6 to +0.3), Mozambique being the one country that moves it. Task complexity, the work-versus-study balance and the English share do nothing.

*Figure 5. The income coefficient as each candidate enters. It moves only for internet access and tertiary enrolment.*

The three are highly correlated (income with internet 0.81, with tertiary 0.77), so the data cannot fully rank access against education, and this analysis was specified after the primary result was known. But the direction is not ambiguous: *the collaboration gap tracks who can get online and how educated the population is, not the size of the economy.* That is the same story the Super Bowl wave and the personal-use result tell from the other side. Where access is broad, the user base is broad and casual, and casual users work things through rather than hand over; where access is narrow, the users are a professional and technical few, and they delegate.


## Why: what education changes

Access and education are still proxies. The last step the public data allows is to ask *which behaviour* changes with them. Automation is two patterns and augmentation is three, and each carries a different mechanism: more **learning** means people use the model to be taught; more **validation** means they check it; more **task iteration** means they work with it. Each of the five pattern shares was regressed on tertiary enrolment, internet access and income, with task mix and the usual controls held constant, on the 86 countries with complete data.

| Pattern (share of classified conversations) | Mean share | Tertiary enrolment, per SD | Internet access, per SD | Log income, per SD |
|---|---|---|---|---|
| Directive (hand over) | 39.6 | **−1.1 (−2.0, −0.2)** | −0.6 (−1.8, +0.6) | −0.7 (−2.2, +0.8) |
| Feedback loop (relay results back) | 12.2 | +0.1 | +0.2 | 0.0 |
| Task iteration (refine together) | 22.6 | +0.2 | +0.2 | −0.1 |
| Learning (ask to be taught) | 20.9 | +0.6 (−0.2, +1.5) | +0.1 | +0.8 |
| Validation (ask for a check) | 4.6 | +0.3 (−0.0, +0.6) | +0.2 | 0.0 |

The whole effect sits in one pattern. *Educated populations hand over less*: a standard deviation more tertiary enrolment goes with 1.1 points less directive use, and the interval is clear of zero. The share does not go to feedback loop, the coding relay, or to task iteration. It goes, as far as 86 countries can tell, to learning and to validation, a 6% relative rise in checking from a small base. Internet access, with education in the model, moves nothing on its own.

That narrows the "why" to two mechanisms the data cannot fully separate but both support. The first is **who uses the tool**. Where access is broad, the user base is broad, casual and personal, and such users learn from and check the model rather than commission it; where access is narrow, the users are a professional and technical few who delegate. The personal-use result, the Super Bowl wave and Anthropic's own observation that early adopters in less developed countries "tend to be technical users" all point here. The second is **what education does to how people use it**. Tertiary enrolment predicts less handover even with personal use, coding share and adoption held constant, and the behaviour it predicts is verification and learning, which are the habits education trains. The first mechanism can be tested part of the way. June 2026 publishes, within each occupation group by country, the split of that group's conversations between work, coursework and personal use. If richer countries' "managers" are managers at work and poorer countries' "managers" are students, the coursework share inside the group should absorb the education effect. It does not. In science the education coefficient moves from −1.9 to −1.6 with the group's own coursework and personal shares controlled; in management it does not move at all; in business, healthcare and the arts it is unchanged within noise. Poorer countries do have more student use inside professional groups (the correlation between a country's coursework share within a group and its tertiary enrolment runs from −0.2 to −0.6), but that is not what carries the effect. *Who is in the group explains little; what educated populations do with the model explains more.*

What they do is selective. The same test at the level of **work activity**, the 35 generalised work activities O*NET uses across occupations, shows that education does not lower delegation uniformly. It lowers it most for developing objectives and strategies (−4.0 points per standard deviation), thinking creatively (−1.4), getting information (−1.3) and documenting information (−1.2), all with intervals clear of zero, and it *raises* it for working with computers (+0.9, clear of zero). Across activities, the education coefficient is most negative where the model is globally granted the most autonomy (correlation −0.45): where the model is trusted with the most decision-making, educated populations pull back most. April and May agree on individual activities only loosely (0.26), so the pattern is the finding, not any single activity. *Better-educated populations delegate routine computer work more and strategy, creative and information work less; less-educated populations delegate more uniformly.*

*Figure 6. The education coefficient on automation share within each work activity, May 2026, with the activity's global automation share in brackets. Green marks are intervals clear of zero on either side.*

One more candidate was tested and failed: **accountability institutions**. If professionals in richer countries check the model more because they are more answerable for their output, measures of institutional quality should carry the effect. The World Bank's rule-of-law, regulatory-quality and government-effectiveness indicators add nothing to the overall model or within any professional group, and the education coefficient is unchanged by them (−1.7 overall with or without). Whatever education does, it is not through the courts or the regulator.

Both remaining mechanisms are consistent with everything above. Neither is a causal claim: they are country-level associations, and the individual-level question, whether *a more educated user* in the same country delegates less, can only be answered with data Anthropic holds.


## Education systems: quality and orientation, not just years

Tertiary enrolment measures how much schooling a country provides. It says nothing about what the schooling is like, or about what a society thinks learning is for. Three kinds of measure were tried, each added to the model with tertiary enrolment, internet access and income already in it: education *quality* (the World Bank's harmonised test scores and learning-adjusted years of school, which combine years with what is learned in them); cultural *orientation* (Hofstede's long-term orientation, built from World Values Survey items on perseverance and thrift, and indulgence, its counterpart; GLOBE's future and performance orientation); and, most directly, the World Values Survey's own wave 7 items on *how children should learn*, which ask respondents which qualities children should be encouraged to learn at home. The share choosing independence and imagination, and the share choosing obedience, are as close as a public survey comes to a country's stated learning culture.

| Added to the unbundled model (Aug 2025 outcome) | N | Coefficient per SD | Tertiary enrolment after |
|---|---|---|---|
| Harmonised test scores | 101 | **−1.2 (−2.4, −0.0)** | −1.4 |
| Learning-adjusted years of school | 101 | **−2.1 (−3.6, −0.7)** | −1.2 |
| Expected years of school | 101 | −1.5 (−2.9, −0.1) | −1.4 |
| Secondary enrolment | 101 | −0.6 (−1.8, +0.6) | −1.5 |
| Education spending, % of GDP | 98 | +0.1 (−0.7, +0.9) | −1.7 |
| GLOBE future orientation | 48 | −0.3 (−1.2, +0.7) | −1.1 |
| GLOBE performance orientation | 48 | +0.2 (−0.6, +1.0) | −0.9 |
| Hofstede long-term orientation | 72 | **−1.2 (−2.0, −0.4)** | −1.0 |
| Hofstede indulgence | 71 | **+1.4 (+0.4, +2.4)** | −1.0 |
| WVS: children should learn independence | 45 | −0.8 (−2.4, +0.9) | −1.1 |
| WVS: children should learn imagination | 45 | −0.4 (−2.2, +1.4) | −1.1 |
| WVS: children should learn obedience | 45 | +0.8 (−0.7, +2.4) | −1.1 |
| WVS: independence + imagination − obedience | 45 | −1.2 (−3.5, +1.1) | −1.2 |
| WVS: greater respect for authority is good | 45 | +0.7 (−1.9, +3.2) | −0.8 |

Two things pass. **Quality of schooling** predicts less delegation beyond the quantity of it: a standard deviation more in harmonised test scores, or in learning-adjusted years, goes with 1.2 to 2.1 points less automation, and tertiary enrolment keeps most of its own effect beside it. Spending and enrolment at lower levels add nothing. And **orientation** predicts it too: societies that Hofstede's survey-derived scores rate as long-term oriented, which is to say pragmatic and persevering, delegate less, and societies rated as indulgent delegate more, each by about 1.2 to 1.4 points per standard deviation. GLOBE's orientations, on 48 countries, do not.

The **direct measure of learning culture does not pass**, and the reason matters. The World Values Survey covers only 45 of the countries in the sample, and at that size effects smaller than about 2 to 3 points per standard deviation cannot be detected. Every stated value points the way the quality and orientation results point: countries where more parents want children to learn independence and imagination delegate less, countries where more want obedience delegate more, and the combined index is −1.2. None is clear of zero. Tertiary enrolment keeps its full effect beside every one of them, and none of the child-rearing items correlates with it above 0.4, so what education does here is not the same thing as what parents say they value. The stated values of a society are not, on this evidence, what carries the education effect; the schooling itself is.

The selective pattern sharpens with these measures. On developing objectives and strategies, a standard deviation of test scores goes with 6.1 points less delegation and learning-adjusted years with 6.5; GLOBE future orientation, null overall, is −3.0 here and clear of zero. On working with computers the sign flips: test scores +1.1, learning-adjusted years +1.2, both clear of zero. *Countries whose schools teach more, and whose cultures favour the long view, keep strategy and hand over code.* Thinking creatively is the one activity where long-term orientation rather than school quality does the work (−1.1, clear of zero). The World Values Survey items do nothing on any of the three activities: the largest, independence on strategy, is −2.0 on 34 countries with an interval from −5.2 to +1.3.

These are the last steps the public data allows and the most exploratory: sixteen candidates were tried, the quality measures correlate with tertiary enrolment at 0.7 or above, and the orientation scores rest on a 2010 revision of survey items. What they establish is direction. The gap is not only about how many people are schooled but about what the schooling teaches and how far a society takes the long view. What it is not, on the one direct test available, is a matter of the values parents say they want children to learn.

