# How Canada uses Claude: Findings from the Anthropic Economic Index

## Source

- **Title:** "How Canada uses Claude: Findings from the Anthropic Economic Index"
- **Date on page:** Jul 14, 2026 (the BibTeX block at the foot of the page gives `date = {2026-06}`, a discrepancy — see `## Verification`)
- **URL:** https://www.anthropic.com/research/how-canada-uses-claude
- **Type:** country spotlight, published in the "Economics" category of anthropic.com/research
- **Author:** Peter McCrory (sole author named in the citation block: `@online{mccrory2026canadacountrybrief, author = {Peter McCrory}, ...}`)
- **Length and form:** web page only; no PDF, appendix or dataset is linked anywhere on the page (checked: the only outbound research link in the body is to the January 2026 report). The page runs "Key findings" plus four H3 sections ("Canada is at the forefront of Claude adoption"; "Within Canada, adoption is concentrated and tracks workforce composition"; "Understanding the distinctive uses of Claude within Canada"; "Conclusion") and seven figures, roughly 1,400 words of English body text, followed by a complete French translation of the same text and figures ("*Le français suit.*"; French heading "Utilisation de Claude au Canada : constatations présentées dans l'Anthropic Economic Index").
- **Which Economic Index release/window it rests on:** every figure is sourced to "Anthropic Economic Index, February 2026"; the Figure 1 caption specifies "1M conversations sampled from Claude.ai in February 2026", and the body says "Based on a sample of Claude.ai conversations in February 2026". The first key finding says only "Based on the latest release of the Anthropic Economic Index" — the page never names a dated release folder, a data-window range or a release URL. Claude.ai consumer traffic only; no first-party API, Claude Code or survey data appears. External sources named in captions: World Bank (Figure 1), IMF and World Bank (Figure 2), Statistics Canada (Figures 3, 4, 6).

## Claims

Numbered; each gives the reference on the page, the number as published, and the comparison the number rests on.

1. **Canada is 2.6% of global Claude.ai traffic and 8th by volume.** (§"Key findings"; §"Canada is at the forefront of Claude adoption"; Figure 1 left panel, and repeated in §"Conclusion".) Comparison: Canada's share of global Claude.ai consumer conversations against all other countries in the February 2026 sample of 1M conversations; the rank is against the same global distribution.

2. **Canada's AUI is 4.4.** (§"Canada is at the forefront of Claude adoption"; Figure 1 right panel.) Comparison: Canada's share of Claude usage against Canada's share of working-age population — "usage per capita is more than four times higher than would be expected based on its working-age population". Published to one decimal place, with no interval.

3. **Canada has the second-highest AUI among the top ten countries by volume, behind the United States.** (§"Key findings"; §"Canada is at the forefront of Claude adoption"; Figure 1.) Comparison: AUI ranking restricted to the ten countries that "collectively represent more than half of all usage", not to all countries. So the claim is "second among a volume-selected peer set", not "second in the world".

4. **Among IMF advanced economies, usage per capita rises with GDP per working-age capita, and Canada sits above the line.** (§"Canada is at the forefront of Claude adoption"; Figure 2.) Comparison: bivariate AUI-against-GDP-per-working-age-person scatter with a line of best fit, over "IMF advanced economies with at least 200 conversations in our sample"; Canada's residual is positive. No slope, standard error or R² is published, and no counts of countries in the sample are given.

5. **Ontario accounts for 43.9% of Canadian conversations; Quebec 20.8%, British Columbia 18.9%, Alberta 10.2%; the four together are "roughly 94%" of national usage.** (§"Key findings"; §"Within Canada, adoption is concentrated and tracks workforce composition"; Figure 3 left panel.) Comparison: each province's share of *Canadian* Claude.ai conversations (parent geography Canada, not global). The four published shares sum to 93.8%, consistent with the "roughly 94%" in the key findings; the body phrases the non-Ontario three as "[a]nother 50% of usage".

6. **Provincial AUI: British Columbia 1.4, Ontario 1.1, every other province below 1.0, Newfoundland and Labrador 0.2.** (§"Key findings"; §"Within Canada..."; Figure 3 right panel.) Comparison: each province's share of Canadian conversations against its share of Canada's working-age population, "where 1.0 indicates usage proportional to the province's working-age population" (Figure 3 caption). Note the reordering relative to claim 5: BC is third by volume but first per capita. Territories are excluded as below the reporting threshold.

7. **Within Canada, provincial income does not explain adoption; the employment share of professional, scientific and technical services does.** (§"Key findings"; §"Within Canada..."; Figure 4, two panels: AUI against GDP per working-age person, and AUI against the employment share of professional, scientific and technical services.) Comparison: cross-provincial correlation of AUI with each characteristic, explicitly set against the cross-country relationship of claim 4 — "In contrast to the global relationship between income and usage, we find that provincial usage per capita is mostly uncorrelated with income." The positive relationship is described as "systematically higher usage per capita" in provinces with larger such sectors. No coefficient, standard error, sample size or fit statistic is published for either panel.

8. **This replicates, within Canada, the within-US adoption pattern of the January 2026 report.** (§"Within Canada...": "This evidence is consistent with our [earlier findings](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report) concerning adoption diffusion within the United States.") Comparison: qualitative, against the US-state results of `economic-index-2026-01-report`; no joint estimation, pooled regression or numerical comparison of the two countries is shown.

9. **The use-case mix is near-flat across provinces: personal 44–51%, work 34–40%, coursework 13–18%.** (§"Key findings" gives all three ranges; §"Understanding the distinctive uses of Claude within Canada" gives personal and work and leaves coursework as the residual — "What remains is using Claude to assist with coursework-related tasks"; Figure 5.) Comparison: the three shares within each province, with provinces ordered by provincial AUI (Figure 5 caption), so the flatness claim is a comparison of mix against adoption *level* — "Usage patterns in Canada are largely uncorrelated with adoption rates" (§"Key findings").

10. **Translation and editing use is higher where public administration employment is higher; New Brunswick, Nova Scotia and Quebec top both.** (§"Key findings"; §"Understanding the distinctive uses..."; Figure 6, left panel public administration employment as a share of provincial employment, right panel translation and editing requests as a share of provincial conversations.) Comparison: cross-provincial, over "the seven provinces above the reporting threshold" (Figure 6 caption) — i.e. three of the ten provinces are dropped and not named. No correlation coefficient or shares are published; the three named provinces are identified by rank only ("the highest rates ... and the largest share").

11. **Document translation is Canada's single most distinctive use case relative to Australia, the UK and the US.** (§"Understanding the distinctive uses..."; Figure 7; repeated in §"Conclusion".) Comparison: "the net difference in the percent of conversations in Canada versus the average across Australia, the UK, and the US" (Figure 7 caption), restricted to "conversation groupings representing at least 1% of Canadian conversations", showing the six most distinctively Canadian and six most distinctive across peers. The peer average appears to be unweighted across the three countries; no per-country peer values or magnitudes are published in the text.

12. **Canadian usage tilts to education and labour-market entry.** (§"Key findings"; §"Understanding the distinctive uses..."; Figure 7.) Overrepresented relative to the three-country peer average: "academic coursework (mathematics and STEM), coding assistance, and resume drafting". Underrepresented: "workplace email, marketing content, legal assistance" and "everyday personal tasks to assist with cooking, home maintenance, and health questions". Comparison: same net-difference construction as claim 11; the categories are named but no percentage-point differences appear in the prose.

13. **Sample size and window.** (Figure 1 caption.) "1M conversations sampled from Claude.ai in February 2026" is the only sample-size number on the page; no Canadian, provincial or peer-country conversation counts are published.

## Definitions (verbatim)

Every construct definition that appears on the page, quoted exactly; references are the section heading or figure caption in which each appears. The page defines only three constructs explicitly (AUI twice, and work/personal by example); everything else is used undefined.

- **Anthropic AI Usage Index (AUI)** — Figure 1 caption: "The Anthropic AI Usage Index (AUI) measures whether Claude usage is over- or under-represented in a country relative to its working age population."
- **AUI, provincial reading of the 1.0 benchmark** — Figure 3 caption: "AUI by province, where 1.0 indicates usage proportional to the province's working-age population."
- **AUI, glossed in the body** — §"Canada is at the forefront of Claude adoption": "its Anthropic AI Usage Index (AUI) is 4.4, which implies that usage per capita is more than four times higher than would be expected based on its working-age population."
- **Personal use** — §"Understanding the distinctive uses of Claude within Canada": "personal use—looking up health information, researching products, getting help with recipes or home repairs—accounts for 44% to 51% of conversations."
- **Work-related use** — §"Understanding the distinctive uses of Claude within Canada": "Work-related use, where Claude is used to troubleshoot software, draft work emails, and build business applications, accounts for around 34% to 40%."
- **Coursework, as the residual** — §"Understanding the distinctive uses of Claude within Canada": "What remains is using Claude to assist with coursework-related tasks (Figure 5)."
- **The three-way split, as labelled in the figure** — Figure 5 caption: "Share of each province's conversations classified as work, coursework, or personal, ordered by the provincial AUI (in parentheses)."
- **Advanced-economy sample for the income relationship** — Figure 2 caption: "This plot shows the bivariate relationship between each country's AUI and GDP per working-age person among IMF advanced economies with at least 200 conversations in our sample. The dashed line shows the line of best fit."
- **Provincial economic characteristics used** — Figure 4 caption: "Panels plot provincial AUI against provincial characteristics: GDP per working-age person (left) and the employment share of professional, scientific and technical services (right)."
- **Translation measure** — Figure 6 caption: "Left panel: public administration employment as a share of total provincial employment. Right panel: translation and editing requests as a share of provincial conversations, for the seven provinces above the reporting threshold."
- **Distinctiveness measure** — Figure 7 caption: "This figure shows the net difference in the percent of conversations in Canada versus the average across Australia, the UK, and the US for various conversation groupings representing at least 1% of Canadian conversations (6 most distinctively Canadian and 6 most distinctive across peer countries)."
- **Sample** — Figure 1 caption: "based on 1M conversations sampled from Claude.ai in February 2026."

## Data and methods

In the wiki author's words, with references.

**Underlying data.** One cross-section of Claude.ai consumer conversations sampled in February 2026 — "1M conversations sampled from Claude.ai in February 2026" (Figure 1 caption) — attributed throughout to "Anthropic Economic Index, February 2026". The page gives no release identifier, no data-window dates, no classifier description, no geolocation method and no privacy or aggregation thresholds beyond the bare phrase "reporting threshold" (Figures 3 and 6). There is no methodology appendix and no link to one.

**Geography.** Two grains are used: country (for Figures 1, 2 and 7) and Canadian province (Figures 3–6). Country shares are shares of global usage (§"Canada is at the forefront..."); provincial shares are shares of Canadian usage (Figure 3 caption), i.e. normalised to the parent country. AUI at both grains is the usage share divided by the working-age-population share, with 1.0 as parity (Figures 1 and 3 captions); the working-age denominators come from the World Bank for countries (Figure 1) and Statistics Canada for provinces (Figure 3).

**External data layered on.** World Bank population (Figure 1); IMF advanced-economy classification and GDP per working-age person (Figure 2); Statistics Canada for provincial working-age population, provincial GDP per working-age person, employment share of professional, scientific and technical services, and public administration employment share (Figures 3, 4, 6). No vintage, table number or release date is given for any of these.

**Estimation.** Everything published is descriptive: shares, ratios, bivariate scatters and one "line of best fit" (Figure 2 caption). No regression output, no standard errors, no confidence intervals, no conversation counts by province, and no hypothesis test appear anywhere on the page. The Figure 7 statistic is a simple net difference in percentages of conversations against an average of three peer countries.

**Cell suppression.** Two thresholds are stated but not quantified: "Territories are below the reporting threshold" (Figure 3 caption) and translation shares are shown "for the seven provinces above the reporting threshold" (Figure 6 caption). A third selection rule is quantified: countries in Figure 2 need "at least 200 conversations in our sample"; and Figure 7 groupings need to represent "at least 1% of Canadian conversations".

**Is the underlying provincial cut in the public release?** The page itself publishes no data and links no file, so nothing here is directly reproducible from it. Separately, the public Economic Index release documentation supports a subnational grain that would include Canadian provinces: the `data_documentation.md` for `release_2026_03_24` (fetched from Hugging Face today, see `## Verification`) describes a `geography` field with levels "country", "country-state", or "global", where `geo_id` is an "ISO 3166-2 region code for country-state", and states that "country-state" means "Subnational region aggregations (ISO 3166-2 regions globally)" — with the caveat, in the same file, that "Some countries were excluded from region-level analysis due to mapping issues between source data codes and ISO 3166-2 standards." That release's Claude.ai file covers 2026-02-05 to 2026-02-12, the only public release window inside February 2026 (`data/releases/INDEX.md`). Whether Canadian `CA-*` rows are actually present, at which metrics and facets, and whether the released aggregates reproduce 43.9% for Ontario, is a data-steward question and is **not** confirmed here; the wiki author has not opened the release files. Note also that the page's own figure source line says "Anthropic Economic Index, February 2026" while its first key finding says "the latest release", which as of 14 July 2026 would be `release_2026_06_26` — the two are not obviously the same thing, and the page does not resolve it.

## Limitations (verbatim)

The page carries no section headed "Limitations", and no sentence on the page states a limitation in its own voice. The following are the only passages that bound the findings — thresholds, sample restrictions and hedged causal language — quoted verbatim with their references.

- Figure 3 caption: "Territories are below the reporting threshold."
- Figure 6 caption: "translation and editing requests as a share of provincial conversations, for the seven provinces above the reporting threshold."
- Figure 2 caption: "among IMF advanced economies with at least 200 conversations in our sample."
- Figure 7 caption: "for various conversation groupings representing at least 1% of Canadian conversations (6 most distinctively Canadian and 6 most distinctive across peer countries)."
- §"Canada is at the forefront of Claude adoption": "Based on a sample of Claude.ai conversations in February 2026, 2.6% of global traffic is in Canada."
- §"Within Canada, adoption is concentrated and tracks workforce composition": "we find that provincial usage per capita is mostly uncorrelated with income."
- §"Understanding the distinctive uses of Claude within Canada": "we find that use of Claude for translation and editing requests is systematically higher in parts of the country with a larger share of public administration employment—perhaps reflecting Canada's commitment to official bilingualism in the public sector …".
- §"Key findings": "In contrast to global, cross-country patterns, provincial income per capita does not appear to explain the gap. Instead, industrial composition appears more important …".
- §"Key findings": "We find evidence that specific use cases coincide with local economic characteristics."

## Open questions, conjectures and promised follow-ups (verbatim)

The page names no open question in so many words and promises no follow-up work. It poses one rhetorical question, which it then answers, and offers several explicitly hedged conjectures. All quoted verbatim with references.

**Question posed**

- §"Within Canada, adoption is concentrated and tracks workforce composition": "What explains the pattern of regional adoption? We explore this question in Figure 4."

**Conjectures and hedged mechanisms**

- §"Canada is at the forefront of Claude adoption": "In this sense, Canada appears further along on its AI adoption curve as compared to peer countries, perhaps reflecting its highly educated workforce and proximity to the US technology frontier."
- §"Key findings": "This aligns with other evidence that model capabilities matched to workforce composition determine overall adoption levels within high-income countries."
- §"Within Canada, adoption is concentrated and tracks workforce composition": "Evidently, workforce composition—rather than income per se—is a key determinant of within-Canada patterns of adoption. This evidence is consistent with our earlier findings concerning adoption diffusion within the United States. It appears that AI adoption in high-income countries is primarily shaped by how well matched model capabilities are to the structure of the local economy."
- §"Key findings": "Translation requests track public administration employment shares across provinces, likely reflecting Canada's policy of official bilingualism in federal services and communications …".
- §"Understanding the distinctive uses of Claude within Canada": "perhaps reflecting Canada's commitment to official bilingualism in the public sector, which generates demand for English–French translation wherever government employment is concentrated."
- §"Conclusion": "Such intensity of adoption allows us to better understand how Claude usage reflects the structure of the Canadian economy and broader economic conditions."
- §"Conclusion": "This is consistent with the view that model capabilities well-matched to the composition of the local economy primarily drive overall adoption rates. This stands in contrast to patterns of adoption globally, which appear more tightly linked to income per capita."
- §"Conclusion": "Translation is more common in provinces with more public administration employment, consistent with the official-languages requirements that apply across much of Canada's public sector …".

**Promised follow-ups:** none. The page contains no "future work", no "we plan to", and no "more research is needed" phrase of any kind.

## What it did not test

The wiki author's inference, from the fetched page; not the page's own statements.

1. **No language measurement anywhere.** The bilingualism mechanism (claim 10) is inferred from public-administration employment shares and from translation-request shares. The page never measures the language of the conversations themselves, never uses francophone population share or official-language-minority share as a covariate, and never separates English→French from French→English work. Nova Scotia, one of the three provinces named, is not a majority-francophone or officially bilingual province, and the alternative explanation — that public-sector work generates editing demand irrespective of language — is not tested against the bilingualism story.
2. **No multivariate specification.** Income and the professional/scientific/technical employment share are each plotted against AUI separately (Figure 4). Whether the services share survives conditioning on income, education, urbanisation or age structure — and whether the two provincial characteristics are collinear across ten provinces — is not examined.
3. **No inference at all.** With at most ten provinces and seven above the translation threshold, nothing on the page reports a standard error, a confidence interval or a sample count. Whether Newfoundland and Labrador's AUI of 0.2 or the NB/NS/QC translation ranking is distinguishable from sampling noise is untested.
4. **No sub-provincial geography.** Provincial results could be generated entirely by Toronto, Montreal and Vancouver; the page tests no metro/non-metro or urban-density split, so "provinces with large professional, scientific and technical services sectors" is not distinguished from "provinces containing a large tech metro".
5. **No time dimension.** One February 2026 cross-section. No growth rate for Canada across releases, no comparison with earlier Economic Index geography reporting, and so no test of the "further along on its AI adoption curve" conjecture, which is a statement about a trajectory made from a single point.
6. **Consumer surface only.** No first-party API, Claude Code or enterprise data appears, so business and developer adoption in Canada is unmeasured; the adoption ranking is a consumer ranking presented as national adoption.
7. **No Economic Index facets beyond the use-case mix.** The page reports no collaboration-pattern split (automation vs augmentation), no AI-autonomy measure, no O*NET task or occupation composition, and no task-success or multitasking cut for Canada or its provinces — all of which exist elsewhere in the Index. So "how Canada uses Claude" is answered with use-case categories only, and nothing is said about *how* Canadians work with the model.
8. **The education tilt is not benchmarked against education.** "Academic coursework ... overrepresented" (claim 12) is never compared with Canada's student population share, university enrolment rate, or age structure relative to Australia, the UK and the US, so a demographic composition explanation is neither ruled in nor out.
9. **Peer set is asserted, not chosen.** Three Anglosphere countries, apparently unweighted; the page tests no sensitivity to adding or dropping a peer, to weighting by conversation volume, or to comparing against the global average instead.
10. **Excluded cells are unexamined.** Territories are dropped, and the three provinces below the translation reporting threshold are never named, so the page does not say whether its translation finding would survive their inclusion, nor what the threshold is.
11. **Geolocation is not validated.** IP-based location, VPN use, travellers and non-resident users are not discussed; "usage in Canada" is not tested against any independent Canadian benchmark (for example Statistics Canada's own surveys of AI use by firms or individuals).
12. **Levels versus shares.** Only shares are published. The page does not test whether a province's use-case mix flatness (claim 9) survives at the level of conversations per capita, where provinces differ by a factor of seven in AUI.
13. **The US comparison is asserted, not estimated.** Claim 8 says the Canadian pattern is consistent with the US findings of the January 2026 report, but no pooled specification, no common definition check on the services-employment variable across StatCan and US sources, and no test of equality of the two relationships is shown.

## Verification

- **Fetched today, 2026-09-16:** https://www.anthropic.com/research/how-canada-uses-claude — fetched in full and read in full, including the French translation and the two BibTeX citation blocks. Every quotation in `## Definitions (verbatim)`, `## Limitations (verbatim)` and `## Open questions, conjectures and promised follow-ups (verbatim)`, and every number in `## Claims`, was checked character-by-character against that fetched text. No quotation is drawn from memory, from `reference/`, or from any other page.
- **PDF check:** the page links no PDF, appendix, dataset or code. The only research link in the body is https://www.anthropic.com/research/anthropic-economic-index-january-2026-report (not fetched in this thread; it is another slug's file). The `wiki/INDEX.md` row's "— (web only)" is confirmed.
- **Also fetched today, for the provincial-cut question only:** https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/main/release_2026_03_24/data_documentation.md (via `curl`, 309 lines). Used solely for the two quoted field descriptions in `## Data and methods`. `data/releases/INDEX.md` (the data steward's file, read not edited) was used for the `release_2026_03_24` Claude.ai window of 2026-02-05 to 2026-02-12.
- **Fetch failures:** none.
- **Discrepancies noted on the page itself:**
  1. Page date "Jul 14, 2026" versus the citation block's `date = {2026-06}` in both the English and French citations.
  2. English key findings say "every other province has below-parity rates of adoption"; the body says "The remaining provinces have below-parity rates of adoption"; the French body instead says "Les autres provinces affichent des taux d'adoption inférieurs à la moyenne nationale" ("below the national average"), which is a different statement. The English text is treated as authoritative throughout this file.
  3. The published provincial shares sum to 93.8% (43.9 + 20.8 + 18.9 + 10.2) against the text's "roughly 94%" and "[a]nother 50%"; arithmetic checked by the wiki author, not a claim of the page.
- **Transcription conventions in the verbatim sections:** the fetched page mixes curly and straight apostrophes; all apostrophes here are normalised to straight. Markdown link markup around "earlier findings" in §"Within Canada..." is stripped in the quotation (the link target is recorded in claim 8). A trailing " …" marks a quotation truncated before the end of its sentence; no word inside any quotation is altered, and no ellipsis appears inside a quotation.
- **Not verified here, flagged for the data steward:** whether Canadian province rows (`CA-*`, `geography: country-state`) are present in the public release, and whether Ontario's 43.9% share and the provincial AUI values reproduce from it. The wiki author opened no release data file.
