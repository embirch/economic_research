> **Status, 30 September 2026:** Historical landscape scan; read README.md in this directory and the follow-up audit before using it. The unqualified novelty claim below is not established: adjacent gender/AI indices were identified in the newer concept memo. Source leads and licence claims still require verification.

# A Gender Index for AI · landscape scan · 30 September 2026

Synthesis of three parallel scans (`strand1-gender-indices.md`, `strand2-ai-trackers.md`, `strand3-literature-datasets.md`), each with URLs for every claim. Entries the strands mark `[S]`, `†` or "secondary" came from search snippets or press because the primary site blocked automated fetching; they are leads to verify, not confirmed facts. Where this synthesis relies on one, it says so.

## 1. Verdict

**Nothing equivalent exists.** No product named a gender AI index, AI gender gap index or tracker, women in AI index, scorecard, barometer or monitor was found. No existing index combines sex-disaggregated AI access, use, exposure of work, workplace conditions, outcomes and attitudes; none is recurring and reproducible from public data.

- The established gender indices carry **no AI indicator**: EIGE's Gender Equality Index 2025, the UNDP/UN Women twin indices, the OECD's SIGI, the SDG Gender Index. Where AI appears it is a LinkedIn sidebar on talent (WEF Global Gender Gap Report, OECD.AI) or recycled headline statistics (UN Women's Gender Snapshot 2026, UNESCO).
- The AI trackers mostly carry **no gender**: Microsoft's AI Diffusion reports none; Stanford's AI Index dropped its diversity chapter in 2026; Anthropic's gender result is one paragraph of the June 2026 report with no released data.
- UNESCO's Women4Ethical AI study names the gap directly: the lack of gender-disaggregated data.

## 2. The closest existing things, and how the proposal differs

| Comparator | What it is | What it lacks |
|---|---|---|
| Cranney, Delecourt and Koning (2026), "Global Evidence on Gender Gaps and Generative AI Over Time" | The de facto global measure of the adoption gap: 76 sources, over 100 countries, about 319,000 respondents; 47.8% of men against 39.3% of women; relative gap stalled near 16% since early 2025 (figures from press coverage, to verify against the paper) | Adoption only; a working paper, not a scheduled release; no compiled dataset found; pools surveys with different questions |
| OpenAI Signals | The only open, recurring, gender-disaggregated instrument: share of messages by name-inferred gender, by country, topic and month, CC BY 4.0 | One product; messages not people; gender inferred from names above 95% prevalence |
| Eurostat `isoc_ai_iaiu`, mirrored by EIGE | Official, open, annual, sex by age and by education, four purposes, 35 geographies | Use only; Europe only; one wave so far; no academic paper using it was found |
| WEF Global Gender Gap Report AI sections | Annual, global | Talent and skills only; proprietary LinkedIn data; outside the index itself |
| ILO refined exposure index (2025) and the 2026 brief on occupational segregation | Exposure by sex across 84 countries; ISCO-08 scores openly downloadable | Analytical reports, not a maintained open series by sex |

An institutional competitor is plausible: EIGE already mirrors the Eurostat table.

## 3. Coverage by pillar

| Pillar | Best public series | Open? | Recurring? | Geography | State |
|---|---|---|---|---|---|
| Participation (adoption) | Eurostat `isoc_ai_iaiu`; Pew ATP (2024, 2026); US SHED; UK DSIT tracker tables | Eurostat and SHED open; Pew with a lag | Annual | Europe, US, UK | **Thick** |
| Patterns of use | Eurostat purposes; OpenAI Signals gender by topic | Yes | Annual; monthly | Europe; global | Thin but usable |
| Exposure of work | ILO ISCO-08 scores and Anthropic observed exposure, each joined to labour-force employment by sex and occupation | Yes | Recomputable yearly | Global; US; Europe | **Thick**, not yet a series |
| Workplace conditions and training | EWCS 2024; Eurobarometer 101.4 (ZA8844); SHED 2025; Coursera enrolment shares; Women in the Workplace | EWCS and Eurobarometer on registration; rest closed | Irregular | Europe; US | Thin |
| Attitudes and trust | Pew; DSIT tracker; Reuters Institute | Partly | Repeated items | US, UK | Moderate |
| Builders | OECD.AI and WEF from LinkedIn; PatentsView; doctoral statistics | Mostly proprietary | Annual | Global | Moderate, not reproducible |
| Outcomes and returns | One study of researcher productivity with open data; experiments without gender splits | Almost none | No | — | **Empty** |

The emptiness of the outcomes pillar is a finding in its own right. No recurring public source reports pay, productivity or promotion in relation to AI use by gender.

## 4. Comparability traps (all three strands agree)

1. **Recall window.** Pew "ever use" (50% and 47%), Eurostat "last three months" (34.9% and 30.5%), the New York Fed "previous 12 months" (50% and 37%) and Oliver Wyman "at least once a week" are different quantities and must never be pooled.
2. **Unit.** People (surveys), messages (OpenAI), visits (Similarweb), firms (JPMorgan), workers (EWCS), occupations (ILO).
3. **Gender measure.** Self-reported binary sex in official surveys; name-inferred in platform logs and LinkedIn, which drops ambiguous and non-Western names unevenly.
4. **Population.** Households aged 16–74, workers, household heads, one product's users.
5. **Relative against absolute gaps.** "22%" is relative; the same data are an 8.5-point gap.
6. **Revisions.** Eurostat's table has already changed since February 2026 press coverage (four countries with women ahead then, six geographies now).

## 5. Design lessons from existing indices

- **A dashboard of parity ratios, not a weighted composite.** ITU's female-to-male ratio with a parity band of 0.98 to 1.02 is transparent. EIGE needed expert-elicited weights and removed a correcting coefficient because it distorted results.
- **Report relative and absolute gaps together**, and disaggregate by purpose: the European gap sits in private and work use and vanishes for formal education.
- **Version the method and back-cast** when it changes, as EIGE did in 2025.
- **Publish coverage and leave gaps blank.** Do not rescale weights silently when a pillar is missing.
- **Never rest a pillar on platform data alone.**
- **Do not treat men's rate as the norm.** A gap is a difference, not a deficit, the point Stephany and Duszynski press.

## 6. What the index could be (version 0)

An open, versioned release with six pillars, each a small set of indicators with a stated population, unit, recall window and gender measure, a parity ratio and an absolute gap, a sampling bound where sample sizes are published, and an explicit "not measured" entry where nothing public exists. Europe first, because it has the one harmonised official series; the United States second; a global layer from OpenAI Signals and the ILO labelled as a different construct. No single score.

The contribution is the instrument: harmonised definitions, the comparability grading, the bounds, the reproducible pipeline, and the map of what is not measured, which doubles as a recommendation to Anthropic, Eurostat and the labs.

## 7. Candidate spin-off papers

1. **Where and for whom does the gap reverse?** Eurostat 2025. Drafted and refereed as `posts/gender1`. No academic paper using this table was found.
2. **The exposure–use mismatch.** Women hold the most exposed jobs on both the ILO's and Anthropic's measures, yet use AI less, most of all in exposed occupations (Henseke). An exposure-adjusted gap by country from Anthropic's occupation-level release, the ILO scores, labour-force employment by sex and EWCS. It connects directly to Massenkoff and McCrory's paper.
3. **Do encouragement, training and permission close the gap outside Denmark?** Humlum and Vestergaard find the gap falls from 11.9 to 5 points where firms encourage use and to 3.6 with training, on register data nobody else can use. EWCS 2024 or Eurobarometer 101.4 could test it across Europe, if the variables exist; the questionnaires must be checked first.
4. Reserve: **convergence across topics** on OpenAI Signals, from the earlier audit.

## 8. Corrections and open checks

- Strand 3 could not find the OSF deposit for the Spanish study. The earlier data audit (`posts/gender1/notes/data-audit.md`) downloaded and profiled it: the audit stands.
- To verify at source before any of it is quoted: the Cranney, Delecourt and Koning headline figures; the WEF 2026 figures; the OECD "Algorithm and Eve" sentence; Pew's tool-by-gender figures; whether the Bick, Blandin and Deming microdata include the generative-AI waves; the EWCS 2024 study number and its AI items; the Eurobarometer 101.4 access terms; the SHED 2025 AI variables.
- Licences not yet checked: Eurostat reuse terms, the ILO score repository.

## 9. Next step

An indicator inventory: for each pillar, every candidate series with its table or file, population, unit, recall window, gender measure, frequency, first and latest period, licence and a comparability grade; then a one-page prototype for a single country with good coverage to see whether the pillars cohere.
