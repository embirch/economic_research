# Post 2 · Research brief · Where AI use is distinctive across US states, and why

Drafted 15 September 2026, before the outlier analysis is run. Supersedes the "Job or place?" framing; the replication, decomposition and provider comparison already built become one section of this post. A companion post will do the same for countries.

## The question

Which US states use AI in genuinely distinctive ways, and why? Not "which states rank highest," but: where does a place's use of Claude depart from the national pattern in a way that persists, and what about the place explains it?

## Why this matters, and to whom

**Because the descriptions are already out there and nobody has checked them.** Anthropic's reports and the press that follows them describe "distinctive" state uses from single windows of data: DC's document editing and job applications, California's IT, Florida's finance. Three providers now publish state rankings that disagree. A first look at two months of the June 2026 release shows half the state-level outliers in one month are gone the next. If a share of these descriptions is sampling noise, then the "AI culture of state X" stories being written from them are wrong, and the fix is a reporting standard: persistence across windows and a sample floor. That is a contribution Anthropic can act on directly.

**Because the real outliers tell us how AI arrives in a place.** The uses that persist cluster in a pattern: fiction writing, gaming, companionship and media discovery in West Virginia, Mississippi, Arkansas and Alaska, the lowest-adoption states. If that holds across all fifty, it means AI reaches low-adoption places through leisure and personal use before it reaches work, the opposite of the country pattern in post 1, where narrow user bases are professional. Whether a technology spreads through work or through play decides who captures its value first and which policies (skills, broadband, procurement) are the relevant ones. This is the diffusion question at the scale of a country's regions.

**Because AI use is becoming a mirror of local economic life.** Maine's and Nebraska's outdoor-and-garden requests in planting season, Hawaii's destination research, DC's editing and self-presentation writing in the year of federal workforce cuts: if each can be tied to a measurable feature of the place across all states, then conversation data is a new instrument for seeing what a local economy is doing, in near real time, with a lag of weeks rather than the years of official statistics. That is the Massenkoff interest in people and places, measured from what people ask rather than where they go.

**Because it is the kind of finding people remember.** The Freakonomics standard: a surprising pattern, an invisible force behind it, and the data to show the force operates everywhere, not just in the anecdote. Every mechanism proposed here is tested across all 51 states, and the post keeps only those that pass.

## The finding it extends, in Anthropic's words

"Washington DC shows a disproportionate focus on document editing, information provision and job applications" (September 2025). The public file's `request_pct_index` is the distinctiveness measure: a state's share of a request cluster divided by the national share. The January 2026 report explains two-thirds of the *level* of state use by workforce composition and does not decompose the *mix*. No report tests whether distinctive uses persist across windows.

## What is new

1. A persistence filter for distinctive use: which state-cluster outliers appear in both independent months of the June 2026 release, and how many single-month outliers vanish.
2. The structure behind the outliers: jobs explain how much a state uses Claude, not what for (the decomposition already built), so the outliers live in the residual.
3. Mechanisms, each pre-stated and tested across all states: the hobbyist signature of low adoption; season and rurality; tourism; the federal workforce; students.
4. A reporting standard Anthropic can adopt for distinctive-use claims.

## Hypotheses, each with what would count against it

- **H1 noise.** A large share of single-month state outliers (≥ 1.6 × the national share) do not recur the next month; persistence is lower for small states. *Against:* recurrence above 80% regardless of state size.
- **H2 the hobbyist signature.** Distinctiveness in the leisure clusters (fiction writing, gaming, companionship and conversation, media discovery) falls with the state's Usage Index and rises with its personal-use share, across all 51 states, in both months. *Against:* no relationship with the index once personal share is held constant; or the relationship reverses.
- **H3 the place in the request.** For each persistent non-leisure outlier, one pre-stated covariate predicts that cluster's distinctiveness across all states: outdoor and garden with rural share (and the spring months); destination research with tourism-industry employment share; editing and self-presentation writing with public-administration employment share; homework and instructional design with the student share of the population. *Against:* the covariate's coefficient inside its minimum detectable effect, in which case the outlier is reported as unexplained rather than explained by a story.
- **H4 real after jobs.** Persistent outliers survive the occupation decomposition: the cluster's distinctiveness is not predicted by the state's user occupation mix. *Against:* the expected-from-jobs mix reproduces the outlier.

## Assumptions sweep, done now

- **Selection.** A state's Claude users are not its population. H2 makes that the object of study rather than a caveat: distinctiveness in low-adoption states is about who is left using it.
- **Noise.** Small states have small samples; suppression removes the smallest cells. Persistence across two independent months is the filter, and the analysis reports how outlier counts scale with state usage.
- **Geolocation.** Tourism states (Hawaii, Nevada, Florida) may show visitors' conversations, not residents'. The destination-research test says so and treats "visitors" as one reading of the mechanism.
- **Taxonomy.** Request clusters change between releases, so only April and May 2026 (same taxonomy) are used for persistence; August 2025 is used only to check whether the DC pattern already existed.
- **Value judgement.** Distinctive is not better or worse. The post explains, and does not rank.
- **Anthropic's own results that bound this.** DC's pattern (September 2025); composition explains the level (January 2026); the Utah abuse flag (excluded); the "distinctive uses" in the country reports for Australia and Canada are single-window and unfiltered.

## Data, confirmed

June 2026 release, subregion rows for the 51 states: request level 1 (175 clusters, 53 with at least 0.5% of national use), level 0 where published; `overall` metrics (Usage Index, use-case split, artifacts); `soc_occupation` shares. August 2025 `request_pct_index` for the DC check. Census ACS 2023 summary tables already downloaded (occupation, education, age, broadband, income) plus C24030 (industry of the employed: accommodation and food services, public administration, agriculture) and B14001 (school enrolment); rural share from the 2020 Census urban-rural table if reachable, else the ACS proxy. Utah excluded throughout.

## Method

1. Distinctiveness = state share of cluster ÷ national share, both months, clusters with ≥ 0.5% of national use. Outliers at ≥ 1.6 ×; persistent if in both months. Report counts, recurrence rate, and recurrence against state usage.
2. H2: for each leisure cluster, log distinctiveness on the log Usage Index and the personal-use share, 50 states, HC3, both months.
3. H3: for each persistent non-leisure outlier cluster, log distinctiveness on its pre-stated covariate (one predictor, then with the Usage Index), 50 states, both months. MDE with every coefficient.
4. H4: the decomposition already built, applied to the outlier clusters' parent categories.
5. Profiles of the five most distinctive states, written from the tests, not from the anecdote.

## Decision rules

Fixed in prereg/prereg-outliers.md before steps 2 to 4 run: an outlier is "explained" only if its covariate passes in both months; "the hobbyist signature" holds only if at least three of the four leisure clusters pass H2 in both months; anything else is reported as such.

## What we would tell Anthropic

Publish distinctive-use figures only for uses that persist across two windows, with the sample floor stated. Report the mix as a residual after occupation, so that "distinctive" means the place and not the jobs. Where a state's distinctive use tracks a local industry, say so; it is the most useful thing the geography data can do.

## Execution

One day: persistence table (already prototyped), three Census downloads, six to eight regressions, four figures, write-up. Everything released with scripts, check blocks and the pre-registration.
