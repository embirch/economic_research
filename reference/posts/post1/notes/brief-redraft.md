# Post 1 · Redrafted brief · written 15 September 2026, after the analysis

This is how the brief would read if written today. It is a draft for discussion, not the brief of record. The pre-registration (prereg/prereg.md) is unchanged; anything here that goes beyond it is marked as reframing or as a new registered prediction.

---

## Adoption curve, culture, or human capital? Why countries work with AI so differently

### The question

Anthropic's Economic Index reports that countries which use Claude more hand over less to it: after adjusting for what people ask about, each unit of the AI Usage Index goes with about three points less automation. The reports offered three readings and tested none: an adoption curve that closes as user bases mature, "cultural and economic factors", or early adopters who happen to be technical. Which is it?

### Why it matters

The three readings predict different futures and call for different responses.

- If it is an **adoption curve**, the gap closes on its own and nothing needs doing.
- If it is **culture**, the gap never closes, and a single global default for how much the model does unasked is a cultural intervention that nobody examined.
- If it is **human capital**, the gap closes as education and access spread, not as GDP grows or user bases age; and the same population brings the same habits to AI whether it lives in a poor country or a poor state. Product defaults, oversight rules and forecasts of who will delegate what all rest on which of these is true.

### Three hypotheses, each with a signature that the others do not share

| | Across countries, income held constant | Within one country, across US states | Which behaviour moves |
|---|---|---|---|
| **Adoption curve** | The Usage Index predicts delegation | The Usage Index predicts delegation | All patterns, uniformly |
| **Culture** | Authority norms (power distance) predict delegation | No gradient: culture is constant within a country | All patterns, uniformly |
| **Human capital** | Education and access predict delegation; the Usage Index does not | Education predicts delegation; the Usage Index does not | The directive pattern only, and most in judgment-heavy work |

The first column was pre-registered on 15 September 2026 as the culture-versus-development test. The second column was added as a dated addendum before any state model was run. The third column was explored after the primary result was known and is reported as exploratory.

### Data

Anthropic Economic Index public releases, five waves from August 2025 to May 2026, country and US-state level, with Anthropic's released code for the task-mix adjustment. Hofstede and GLOBE for authority norms. World Bank for income, internet access and tertiary enrolment. Census Bureau ACS 2023 for state education, broadband and income. Threshold of 200 conversations per country and 100 per state, as in Anthropic's code.

### Primary tests, in order

1. **Reproduce and repeat.** Anthropic's Figure 2.11 with its own function, then the same on four later waves. Establishes the gap is persistent.
2. **The horse race across countries.** Adjusted automation on power distance, log income, the Usage Index and controls, 61 countries, HC3 errors, decision rule and minimum detectable effect fixed in advance. Culture predicts power distance survives income; human capital predicts income survives and the Usage Index does not.
3. **The same test inside one country.** Adjusted automation across US states on graduate share and income, three waves. Culture predicts nothing; adoption curve predicts the Usage Index; human capital predicts education.
4. **Which behaviour moves.** The five collaboration patterns separately, and delegation within occupation groups and work activities. Human capital predicts the directive pattern falls, most where the work involves judgment.

### Decision rules

As pre-registered for test 2 (coefficient outside the minimum detectable effect with the interval excluding zero). For test 3, the rule as registered in addendum 3, with the disclosed flaw that its full-model MDE was uninformative; the verdict is read from the simple model and the two full-month waves. Test 4 is exploratory and carries no rule.

### What would count against human capital

Power distance surviving income across countries. No education gradient across US states. The Usage Index keeping its coefficient with education present. A uniform fall across all five patterns rather than a fall in the directive pattern.

### Robustness

Regional Hofstede scores, GLOBE, other dimensions, directive-only outcome, later waves, English-only, second classifier, placebo outcome, leave-one-out, Utah and DC exclusions, unadjusted outcome, synthetic-data recovery, two implementations of every key number.

### Confirmatory and exploratory, stated

Confirmatory: tests 1, 2 and the August 2025 half of test 3. Exploratory: the 2026 waves of test 3 for this purpose, all of test 4, the unbundling of income into access and education, education quality and orientation, the subregion results.

### Contribution

Anthropic's collaboration gradient is not an adoption curve and not a cultural difference. With education and income in the model the Usage Index has no effect, across 111 countries and within 51 US states; authority norms explain nothing detectable; and what differs between populations is specifically how much judgment-heavy work they hand over. The gap is a human-capital gradient of the kind the diffusion literature describes, in the intensity of use rather than in arrival.

### Registered prediction for the next Economic Index release (proposed addendum 4)

Written before the data exist. On the next wave that publishes US states:

1. The graduate-share coefficient on adjusted automation across states lies between −0.8 and −1.5 points per standard deviation with an interval excluding zero.
2. With graduate share in the model, the state Usage Index coefficient lies inside its own minimum detectable effect.
3. Across countries, with tertiary enrolment and internet access in the model, the income coefficient lies inside its minimum detectable effect.
4. The education effect is carried by the directive pattern, and the coefficient on developing objectives and strategies is negative while the coefficient on working with computers is non-negative.

Any one failing is reported as a failure of the human-capital account.

### Release

Scripts, check blocks, data, figures, notebook, red-team memo and this brief, with the pre-registration commits, in one public repository. The post is the write-up of the tests in the order above.

---

## The opening of the post, as it would read

**Adoption curve, culture, or human capital? Why countries work with AI so differently**

In September 2025, Anthropic's Economic Index reported that countries which use Claude more hand over less to it. Where many people use it, conversations tend to be collaborative: people refine drafts, ask for explanations, ask for checks. Where few use it, people hand over the whole task and take the result. The pattern survived an adjustment for what people ask about, and the report called it "somewhat counter-intuitive," offered "cultural and economic factors" or technical early adopters as guesses, and asked for more research. Two later reports leaned different ways without settling it.

Three readings of that finding predict different things, and this post tests them against each other with the public data, a measure of authority norms the reports never used, Anthropic's own released code, and one place the reports did not look: inside the United States. The reading built into the pre-registration, that culture explains the gap, is the one the data reject. The reading on which the finding was originally stated, that it is an adoption curve, does no better: with a country's income in the model, the Usage Index adds nothing, across countries and across US states alike. What survives is human capital. The gap follows education and access, it reappears across the states of one country where language, product and culture are all the same, and what it changes is specific: better-educated populations hand over routine work and keep strategy. It is a gap in how intensively a technology is used, of the kind the diffusion literature has described for a century of other technologies, not a gap in whether it has arrived and not a difference in what people believe about authority.
