# Red-team pass · Post 1 · 15 September 2026

The strongest case against each finding, written as a referee would, with the answer the post gives or the concession it makes.

**1. "You have shown that income is collinear with culture, not that culture does nothing."**
True in part. Power distance and log income correlate at −0.58; when two predictors overlap, the data cannot always split credit. The answer: (a) the pre-registered rule asked whether power distance survives income, and it does not, in any of nine specifications; (b) VIFs are moderate (1.7 and 3.9), so the overlap is not extreme; (c) GLOBE's practices measure, built differently, gives the same null; (d) the honest limit is stated: an effect below 1.3 points per SD is undetectable in 61 countries. Concession: the post cannot rule out a modest culture effect hidden inside income.

**2. "Income is a bundle. You have relabelled the mystery, not solved it."**
Conceded at first, then addressed. The unbundling shows income is standing in for internet access and tertiary enrolment; education lowers the directive pattern specifically, in professional and judgement-heavy work and activities (strategy, creative thinking), not in routine ones, and the quality of schooling and long-term orientation carry it beyond years of schooling. The direct World Values Survey measure of learning culture is null on 45 countries. The mechanism is narrowed, not proven: the post says so.

**3. "The Hofstede scores are fifty years old and cover 61 countries. A null on a bad measure is not evidence."**
Partly conceded. Answer: GLOBE (2004, different survey, different sample) gives the same null; the regional extension to 72 countries gives the same null; the raw PDI relationship (+1.9, p < 0.001) shows the measure has enough signal to produce a strong apparent effect, which is exactly what income then absorbs. A measure too weak to matter would not have produced the raw pattern.

**4. "The panel is worthless; within-country adoption barely moves."**
Conceded in the post. The cohort verdict rests on the ceiling arithmetic and the Super Bowl comparison, and the post says so. The panel is reported for completeness with its MDE.

**5. "The Super Bowl test has one treated unit and five controls. That is an anecdote."**
Fair. Answer: it was pre-registered with the comparator set and decision rule fixed in advance, which is what separates a designed one-unit comparison from an anecdote; the result went against the hypothesis its designer expected; and it is presented as one number, not a finding that stands alone. Concession: a single wave cannot exclude that something else moved the US in February 2026.

**6. "The Seychelles exclusion and the language-group collapse are post hoc."**
Both are logged with their reasons and dates in the notebook; the Seychelles rule was added before any culture test was run; the language collapse was made because HC3 errors were undefined with singleton groups, and it moved the power-distance coefficient from −0.53 to −0.63, both nulls. Neither changes any verdict.

**7. "The task-mix adjustment uses global automation rates per task. If the same task is classified differently across languages, you have adjusted with a biased rate."**
Partly conceded. Answer: language group is a control in every model; the English-only run gives the same null; the Stanford second classifier gives the same null. Concession: a language-specific classifier bias that correlates with income cannot be excluded with public data.

**8. "You found what Anthropic already said: development."**
Anthropic said "perhaps" development, or perhaps early adopters, or perhaps culture, and tested none. This post tests all three with their own code and data, finds that adoption itself does no work once income is in (which the reports did not say), bounds cohort, and locates the income effect in learning-heavy work. The replication across four later waves is also new.

**9. "Why should anyone believe the analysis of someone who has never used Python before this week?"**
Because none of it asks for belief: two independent implementations agree to six decimals, the code recovers known effects on synthetic data, the published numbers reproduce exactly, and every step is released with a check block that fails loudly.

**10. "The state test contradicts your own pre-registered verdict. You registered a rule, it said 'does not reappear', and you overrode it."**
True, and stated in the post. The rule keyed the verdict to the full model, whose minimum detectable effect turned out to be 6.8 points because education, income and the Usage Index correlate at 0.7 to 0.84 among 43 states; a rule that cannot detect anything cannot reject anything, and the post says the rule was badly designed. What is reported: the letter of the rule (does not reappear), the simple model with and without the pre-named Utah exclusion (−0.7 spanning zero; −0.9 clear of zero), and the two full-month waves that followed (−1.1 and −1.2, clear of zero, a third to half the variance). The 2026 waves were not pre-registered for this purpose and the post says so. Concession: a reader who accepts only pre-registered verdicts has one inconclusive August result and two clear unregistered ones.

**11. "Within the US, education and income are the same variable. You have not shown education."**
Conceded. They correlate at 0.84 across states and the post claims a human-capital gradient, not an education effect. Across countries, tertiary enrolment and internet access can be partly separated from income (each halves it; together they absorb it), and that is where the "access and education" reading comes from.

**12. "Utah is 25 points off. Why is it in the data at all, and how much else is like it?"**
It is in Anthropic's public file with no flag; the report's text flags it. Utah reverses the sign of Anthropic's own state relationship. The post recommends that flagged geographies carry their flag in the file. Nothing else in the state data is more than 8 points from the line.
