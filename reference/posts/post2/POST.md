# Where AI use is distinctive across US states, and why

*September 2026 · Evidence from Claude, with Microsoft and OpenAI beside it*

## The outliers

West Virginia asks Claude for fiction writing at 2.3 times the national rate, for companionship at 1.8 times, for gaming help at 1.7. Maine and Nebraska ask about outdoor and garden work at more than twice the rate. Hawaii researches destinations at twice the rate. Washington DC edits and rewrites at 1.7 times the rate and works on how it presents itself at 1.6. Mississippi, Arkansas, Alabama and New Mexico write fiction; Alaska and Kansas game; Iowa does science.

Anthropic's reports describe places like this. Its September 2025 report noted DC's "disproportionate focus on document editing, information provision and job applications," and its country spotlights do the same for Australian states and Canadian provinces. The press has turned three providers' state rankings into stories about the AI culture of each state. This post asks two questions the descriptions skip. Are the distinctive uses real, in the sense that they are there again a month later? And for the ones that are, what about the place explains them?

The answers, in order: half of them are not; the biggest single pattern among the real ones is not about the places at all but about who is using Claude there; two of the rest can be tied to something measurable about the state; and one is a puzzle the post leaves open rather than inventing a reason.

Distinctive is a description, not a ranking. Utah is excluded throughout: Anthropic flagged its August 2025 traffic as possibly "coordinated abuse."

## Are they real?

The June 2026 release publishes two full months, April and May, with the same taxonomy, which makes a persistence test possible for the first time. Distinctiveness here is a state's share of a request cluster divided by the national share, for the 53 level-1 clusters that account for at least half a percent of national use. An outlier is a cell at 1.6 times or more.

There are 49 such cells in April and 59 in May. Twenty-two appear in both months. Forty-five percent of April's distinctive uses are still distinctive in May; at a threshold of twice the national rate the count falls to four. The month-to-month correlation of distinctiveness across all 2,600 cells is 0.62. And the outliers are a small-state phenomenon: the seventeen states with the least Claude use produce 1.8 single-month outliers each, the middle seventeen 1.0, and the seventeen largest 0.1. The pre-registered test asked whether recurrence rises with state size; it does not detectably, because the large states produce almost no outliers to recur. *A distinctive use reported from one window of data is a coin flip; a distinctive use in a large state is rare.*

*Figure 5. Every state-by-cluster cell's distinctiveness in April against May 2026. Gold cells are outliers in one month only; green cells in both; the dashed lines mark 1.6 times the national share.*

DC's editing survives the test. So do the twenty-one others listed above, and they are what the rest of the post explains.

## What jobs explain, and what they do not

Before the outliers, the structure. Anthropic's January 2026 report explains most of *how much* a state uses Claude with the share of its workforce in computer and mathematical occupations. That reproduces: 0.37 log points of usage per capita per point of share on the August 2025 wave, 62% of the variance, against the report's 0.36 and "nearly two-thirds." After the workforce, education adds ten points of variance and nothing else does, which is what Doms found for personal computers and Skinner and Staiger for hybrid corn and beta blockers. And three providers see the same places above and below their labour-market line: after the workforce share is removed, Anthropic's state residuals correlate 0.70 with OpenAI's and 0.50 with Microsoft's.

But jobs do not explain *what* a state uses Claude for. The occupational content of conversations, which Anthropic infers from the tasks people bring, is nearly the same in every state: computer and mathematical work is 19% to 27% of conversations everywhere, against 1.5% to 7.9% of workforces, and where the workforce is most technical the conversations are slightly less so. That invariant content explains 21% of the variation between states in what conversations produce. The other four-fifths is where the outliers live, and none of the twenty-two is composition: regressed on the user occupation shares most related to it, no persistent cluster's distinctiveness has a variance explained above 0.42 in either month, and most are below 0.2.

## The hobbyist signature

Four of the persistent clusters are leisure: fiction writing, gaming, companionship and conversation, media discovery. Nine of the twenty-two persistent outliers are one of these four, and every one of the nine is in a low-adoption state. The pre-registered test asked whether that is a pattern or a coincidence: for each of the four, log distinctiveness on the log Usage Index across all fifty states, both months.

All four pass, in both months. Gaming distinctiveness falls 0.43 log points per log point of the index, explaining 67% of the variance in May; media discovery 0.48 and 68%; fiction writing 0.39 and 51%; companionship 0.21 and 28%. Pooled, the leisure index falls 0.41 per log point of adoption and the relationship explains 74% of the variance across states. A state with half the national adoption has leisure distinctiveness a third above the national rate; DC, at three times the national adoption, is at half. Adding the state's personal-use share changes almost nothing, so this is not the personal-versus-work split; it is the composition of what is asked within it.

*Figure 6. Leisure distinctiveness, the mean of the four clusters, against the Usage Index, May 2026, both on log scales.*

The reading is not that West Virginians like fiction more than Californians. It is that where professional use of Claude is thin, what remains is hobbyists, and hobbyists write fiction, play games, talk and look for things to watch. The distinctive uses of low-adoption states are the signature of a user base that professional work has not yet filled out. That is the same asymmetry post 1 found between countries, with the sign reversed: across countries the narrow user bases are professional and the broad ones casual; across US states the narrow ones are casual and the broad ones are work. It says something about how AI arrives in a place: in the United States it comes through play before it comes through jobs.

## The place in the request

The remaining persistent outliers each had one mechanism written down in advance and tested across all fifty states, not just the state that caught the eye.

**Outdoor and garden is rural America in planting season.** Maine, Nebraska and Wisconsin are the outliers; the mechanism was the agricultural share of employment. It passes in both months: 0.15 and 0.16 log points per standard deviation, intervals clear of zero, a fifth of the variance. The rural share of the population, added beside it, is stronger still at 0.22 to 0.24. April and May are the months this cluster should peak, and it does. *Where people have gardens, they ask about them, when it is time to plant.*

**DC's editing is the federal workforce, in one month of two.** The mechanism for DC's three clusters was the public-administration share of employment. For editing and rewriting it passes in May, 0.10 per standard deviation with an interval from 0.07 to 0.13 and 30% of the variance, and fails in April, where the interval crosses zero; research and evidence does the same. Self-presentation writing, which includes résumés and applications, does not pass in either month. By the pre-registered rule these are unexplained; the honest description is partly explained, in the direction the mechanism predicts, and DC is far enough off the line that its own value carries the May result.

**Hawaii's destination research is not tourism, or not measurably.** The mechanism was the share of employment in arts, entertainment, recreation, accommodation and food services. It does not pass in either month; the intervals are wide and span zero. Hawaii is distinctive on its own, Nevada and Florida are not, and the post leaves it there. One reading is that visitors' conversations are geolocated to the island; the data cannot say.

**Students explain nothing.** Mississippi's instructional design and formatted writing and Iowa's science were assigned the college-enrolment share of the population. None passes; the coefficients are near zero in both months.

*Figure 7. Two mechanisms across all fifty states, May 2026: outdoor-and-garden distinctiveness against the rural share of population, and editing-and-rewriting distinctiveness against the public-administration share of employment.*

## What this means

The most-reported kind of fact about AI geography, that a place uses AI in a distinctive way, is half noise when it comes from one window of data, and almost entirely a small-state phenomenon. Anthropic can fix that with a reporting rule: two windows, a sample floor, and the mix reported after occupation.

Of the distinctive uses that are real, the largest single pattern is not about places but about diffusion. Leisure use is distinctive exactly where adoption is low, with three-quarters of the variance explained, because where professional use is thin the remaining users are hobbyists. In the United States, AI reaches a state through play before it reaches it through work, which is the reverse of the pattern between countries and bears on who captures the value of the technology first.

Two of the remaining outliers are the place showing through: gardens where the country is rural, in the months when people plant; government documents where the government is. That is the beginning of what conversation data can be for local economics, a measure of what a place is doing that arrives in weeks rather than years. The post claims it for two clusters and declines to claim it for Hawaii.

## Recommendations to Anthropic

- **Report distinctive uses only when they persist across two windows**, with the sample floor and the state's usage stated. Single-window descriptions in the country and state spotlights should carry that caveat.
- **Report the mix after occupation.** A state's workforce sets how much it uses Claude; the occupational content of conversations is the same everywhere; the residual is where the geography is.
- **Publish request shares within occupation group by state**, so the decomposition can be exact for requests as it is for artifacts.
- **Treat leisure distinctiveness as a diffusion measure.** It tracks the Usage Index at 0.74 R² and says where the professional user base has not yet arrived.
- **Carry Utah's flag in the file.**

## Limitations

**Two months.** Persistence is tested across April and May 2026, the only two windows with a common taxonomy. Two months rule out one kind of noise, not seasonality, and the outdoor-and-garden result is partly seasonal by design.

**Fifty units, small-state noise.** Distinctiveness in small states is measured from small samples, and Anthropic's suppression removes the smallest cells; the counts of outliers by state size say as much. The persistent list is what survives, not what exists.

**Occupation is inferred from the task, not the user.** "Hobbyist" is a reading of the pattern, not an observation of people; the data show what is asked, not who asks.

**Mechanisms are correlations across fifty states**, one covariate each, chosen in advance. Two pass, one passes in one month, three fail. Nothing is causal, and Hawaii is unexplained.

**The pre-registered place rule in the decomposition was mis-specified** (residualising on one predictor before testing a correlated one); the education result rests on the joint model listed as robustness, and both are reported. **The cross-provider mix comparison could not be run** with the published taxonomies. **Census 2023 workforce shares** stand in for the BLS shares Anthropic used.

## Methodology

**Data.** Anthropic Economic Index public releases (2025_09_15 state rows; 2026_01_15 and 2026_03_24 `country-state` rows for US-XX; 2026_06_26 subregion rows for US-XX, April and May), CC-BY 4.0. Usage Index published for August 2025 and June 2026 and rebuilt for November and February from usage shares and Anthropic's state population file, to the convention verified in post 1. American Community Survey 2023 one-year table-based summary files: C24010 (occupation of the employed, 22 groups mapped to SOC major groups), B15003 (bachelor's or higher), B28002 (broadband), B19013 (median household income), B01002 (median age); state GDP per working-age adult from Anthropic's file. Microsoft AI Diffusion `State_Rankings_2026Q1.csv` (public GitHub). OpenAI Signals v2.0 public CSVs: `usa_share_of_messages_by_state_2025_rank.csv` and `usa_share_of_messages_by_topic_state_2025.csv` (CC BY 4.0). Population density was to be added from the Census gazetteer, which was unavailable, and is omitted.

**Replication.** log Usage Index on the computer-and-mathematical workforce share in percentage points (Anthropic's "1% increase in the share" is one point; the log-log elasticity of 1.2 to 1.5 does not match). Gini: unweighted over 51 states (the population-weighted Lorenz version gives 0.32, 0.28, 0.21 and does not match).

**Stage 1.** User occupation shares from `soc_occupation` (April and May 2026; the August 2025 state table is 74% unclassified with two-thirds of cells suppressed and is not used); suppressed small groups treated as zero; renormalised over classified groups. Dissimilarity index = half the sum of absolute differences between user and workforce shares.

**Stage 2.** Expected mix for a state = Σ over occupation groups of (user share of the group in the state × the group's within-group mix in the United States, from the country-level `soc_occupation` rows, which publish every metric for major groups). Observed = the state's `overall` shares. Pooled R² across state-by-category cells after removing category means; per-state dissimilarity; largest residuals profiled. The global within-group mix was tried first and under-predicts advice and email for every state alike, a US-versus-world difference; the US mix removes it and is the one reported.

**Place.** Residual of log index after workforce tech share on standardised covariates, HC3; and the joint model log index on standardised tech share and graduate share. MDE = 2.8 × SE.

**Catch-up.** Change in log index by period on the period's own starting level; Aug→May change on starting level plus covariates; rank persistence; Wyoming robustness; change size on August sample size.

**Outliers.** Distinctiveness = state share of a level-1 request cluster ÷ US share, April and May 2026 separately, clusters with ≥ 0.5% of US use (53); outlier ≥ 1.6×; persistent = both months. Recurrence tested against state usage share. Leisure clusters fixed in advance (fiction writing, gaming, companionship and conversation, media discovery): log distinctiveness on log Usage Index, then with personal-use share. Mechanisms, one covariate per persistent cluster fixed in advance: agriculture share of employment (C24030) for outdoor and garden, with rural share (2020 Census) beside it; arts, entertainment, recreation, accommodation and food services share for destination research; public administration share for DC's three clusters; college enrolment share (B14001) for instructional design, science and formatted writing. After jobs: log distinctiveness on the state's user occupation shares for the groups fixed in advance. All 50 states, HC3, MDE with every coefficient.

**Providers.** Spearman rank correlations of the three levels raw and between residuals after the workforce tech share. Mix: Anthropic level-2 request clusters mapped to OpenAI's five topics by a list fixed in the script before it ran.

**What was set in advance.** Two pre-registrations, both committed before the steps they govern: the decomposition (steps 04 to 07) and the outliers (steps 09 to 12, after the persistence prototype had been seen and is disclosed there). Steps 01 to 03 (loading, replication, stage 1) were run first; the pre-registration with hypotheses, models, decision rules and robustness for steps 04 to 07 was committed before any of them ran. Deviations: the global-to-US mix change in stage 2 (logged, reason above) and the place rule's mis-specification (logged, both models reported).

**Reproduction.** Thirteen numbered scripts and one shell script rebuild every table and figure from the raw files; every script ends with a check block. Scripts, check outputs, tables, figures, the pre-registration and this text are released together.

**Assistance.** The analysis was designed and directed by the author and executed with Claude Code, which wrote the scripts under instruction; every step was read, run and checked by the author, and every number in this post was verified programmatically against the script outputs before publication.
