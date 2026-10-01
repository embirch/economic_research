# Pilot report: Eurostat foundation and geographic feasibility

Data steward, 1 October 2026. Branch `work/index-steward-pilot-2026-10-01`.
Assignment: `team/assignments/2026-10-01-steward-pilot.md` (user authorisation: Emily,
1 October 2026). Deliverables in this directory: [`eurostat-profile.md`](eurostat-profile.md),
[`geographic-coverage.csv`](geographic-coverage.csv), [`checks.py`](checks.py), this report.

**What this is.** A bounded source-verification and geographic-feasibility pilot. It is not new
effect estimation. No composite, no global ranking, no causal claim, no model, no empirical
gender-gap result is produced or approved here. Any gap arithmetic performed while checking the
data is exploratory verification output, explicitly not an index output.

**The headline.** The European core is verified, reproducible and clear for re-use. The current
register cannot support a global release, but that is a fact about *the register*, not about the
world: the register was never a global search. One genuinely global, population-representative,
gender-disaggregated source was found during this pilot — and it measures **attitudes, not use**.
The honest recommendation is option **(B)**: a European core now, with source-specific
non-European modules, and a short, bounded discovery assignment before any geography is promised.

---

## 1. Supported conclusions

### 1.1 The European foundation is reproducible

My independent download of `isoc_ai_iaiu.tsv` from Eurostat's dissemination API on
2026-10-01T08:30:35Z is **byte-identical** to the manuscript's frozen snapshot of
2026-09-21T15:13:28Z (SHA-256 `7f668f7b…96ab`). No silent revision occurred between those dates.
The index can reuse the article's vintage without re-freezing anything, and the manuscript's
inputs are currently regenerable from the live primary source.

Both Eurostat tables carry DOIs (`10.2908/ISOC_AI_IAIU`, `10.2908/ISOC_AI_IAIUXR`), open bulk
download with no registration, and a re-use policy that authorises commercial and non-commercial
re-use with source acknowledgement and no written licence. This is the strongest access position
of any candidate in the register.

Denominator semantics were confirmed arithmetically rather than assumed: 9,486 purpose-ratio
comparisons agree to within 0.96 pp, and 12,920 internet-user-base comparisons to within 0.019 pp.

### 1.2 Three definition corrections the register needed

These were *not* visible from the register text and would have produced wrong indicators:

1. **EU_NONUSE measures the single MAIN reason**, not multiple reasons. Model-questionnaire item
   B7 is "tick one". The five reasons are mutually exclusive and sum to ~99% of the base. Treating
   them as independent multiple-response items would have been a reporting error.
2. **There is no `sex` dimension.** Sex is a prefix inside `ind_type` (`M_Y16_74`, `F_Y16_74`), and
   it is crossed only with age and education — **never with occupation, employment status or
   country of birth.** Any sex × occupation analysis is simply unavailable from these aggregates.
3. **The generative-AI question is asked only of recent internet users** (routed from filter B1).
   `PC_IND` therefore folds internet non-use into AI non-use. Which denominator is used must be a
   stated choice, not an accident of which cell was downloaded.

### 1.3 Uncertainty cannot be quantified from these tables, and that is now documented

Eurostat's reference metadata (ESMS §13.2) states that national institutes supply estimated
standard errors only for the e-commerce indicator. There is therefore **no published standard
error for any generative-AI rate and none at all for a male−female difference**, whose sampling
variance also depends on an unpublished covariance. Resident-population counts are not sample
sizes. The only quality signal in the files is the `u` (low reliability) flag — the sole flag
present — covering ~9% of cells, with a further ~8% unavailable. The headline male/female cells
are complete and unflagged in all 37 geographies; precision degrades sharply for finer crossings.

A first release must therefore present descriptive gaps with the `u` flag surfaced and an
explicit statement that sampling uncertainty is not quantifiable from published cells.

### 1.4 Period and coverage limits

**Both tables contain 2025 only.** There is no Eurostat time series, so no trend, convergence or
"gap is closing" statement is available from this source. Coverage is EU27 + euro area + 35
countries (36 for non-use, which adds Montenegro). Iceland is absent from both.

### 1.5 What I could not verify, stated separately

- I could not read the article repository's frozen `data/raw/` files or
  `outputs/validation/report.json`: it is not mounted and the session token cannot reach it. I did
  not attempt to work around that boundary. **I cannot independently reproduce the article's
  four-hash source-validation report.** The coordinator states a local re-run on 1 October 2026
  matched all four hashes; that is coordinator-supplied provenance, recorded as such.
- The EIGE mirror reports 53,280 values for `isoc_ai_iaiuxr`; the Eurostat primary has 54,825.
  Unexplained. Use the Eurostat primary.
- Check C2: the published non-user base cannot be reliably reconstructed from the use table
  (up to 6.5 pp divergence, confined to BE, SE, NO, LU). Reported as a discrepancy, not resolved
  and not tuned away.

---

## 2. Geographic assessment — explicitly provisional triage

**This section is triage, not an audit.** Core verification consumed most of the pilot. Of the 14
register candidates, three (the Eurostat family) were file-verified; four were given fresh
documentation checks; seven are carried forward on their September evidence without re-checking.
`geographic-coverage.csv` marks each row's verification mode, and the dated status of every claim.

**The register is Europe-heavy because of how it was built, not because of what exists.** It was
seeded from a European manuscript and two European-leaning audits. *Absence from the register is
not evidence of absence in the world.* Within one afternoon's bounded checking, this pilot and the
coordinator together surfaced four substantial non-European sources that the register does not
contain. That is the single most important finding for Emily's scope question.

### 2.1 By region

Regions are assessed for **population-representative, sex-disaggregated measurement of
generative-AI adoption or use** unless otherwise stated. Country count, world-population share,
geographic diversity, measurement comparability and representativeness are kept distinct.

| Region | Verified in the register | Verified elsewhere in this pilot | Honest status |
|---|---|---|---|
| **Europe** | EU27 + 35–36 countries, file-verified, open, one year (2025) | — | **Strong.** A harmonised, instrument-identical, sex-disaggregated adoption measure. The only region where cross-country comparison is currently defensible. |
| **North America** | US only: Pew (documentation-verified, Feb 2026, n=5,119, US-only); RPS (blocked on reuse terms) | Canada: coordinator-supplied Statistics Canada CSWC lead, workplace use, 15–69, past 12 months, not audited by me | **Source-specific, not comparable.** Pew measures *ever-use of chatbots*; Eurostat measures *last-three-months generative-AI use*. These are different estimands and must never be pooled or ranked together. |
| **Latin America / Caribbean** | **Nothing.** | Coordinator-supplied Cetic.br TIC Domicílios 2025 (Brazil, sex rows, purposes and non-use modules), not audited by me; Pew Global covers AR BR CL CO MX PE for attitudes | **Register gap, not a data gap.** Brazil appears to run a national ICT household survey with the right structure. This is the clearest case where the register misled. |
| **Asia** | **Nothing.** | Pew Global covers BD IN ID JP MY PK PH SG KR LK TH for attitudes; ISSP membership includes IN JP PH KR TW TH but module participation unknown | **Unknown, leaning under-explored.** No adoption measure verified. No basis to claim data do or do not exist. |
| **Africa** | **Nothing.** | Pew Global covers GH KE NG ZA for attitudes; ISSP membership includes South Africa only | **Unknown and least explored.** One attitudes source across four countries is not adoption coverage. Do not infer African use rates from anything currently held. |
| **Oceania** | **Nothing.** | Pew Global covers Australia for attitudes; ISSP membership includes AU and NZ; coordinator's Melbourne/KPMG lead is unverified for reusable cells | **Unknown.** |
| **Middle East / North Africa** | Not named as a region in the assignment | Pew Global covers Israel and the West Bank and East Jerusalem | Noted for completeness; outside the six regions assessed. |

**Unknown stays unknown.** For Asia, Africa and Oceania this pilot establishes only that *the
register contains nothing* and that *a bounded search immediately found attitudes data*. Neither
supports a statement that comparable adoption data do not exist.

### 2.2 What would be averaged if we forced a global number today

Nothing legitimate. Eurostat measures last-three-months generative-AI use among individuals aged
16–74 with a single harmonised instrument. Pew's US item measures ever-use of chatbots among
adults. The coordinator's Canadian lead measures workplace use over twelve months among workers
aged 15–69. Signals counts **messages** with **name-inferred** categories and is not a population
sample at all. These have different reference windows, age ranges, tool definitions, units and
sampling frames. Averaging them would manufacture a number with no population.

Global ambition is served by *more verified sources shown separately*, not by pooling.

---

## 3. The three options compared

### (A) European core only

- **Can be delivered from verified evidence today.** One harmonised instrument, 35–36
  geographies, open terms, reproducible provenance, documented denominators and routing.
- **Costs:** covers roughly 6% of world population; cannot speak to any region Emily may care
  about most; a single year, so no trend; and it largely re-presents the first paper's source.
- **Verdict:** the safe floor, but it concedes the global ambition before testing it, and this
  pilot has already shown the register understates what is reachable.

### (B) International evidence resource with source-specific modules — **recommended**

- A verified European core module, plus separately presented national/regional modules (US Pew;
  Canada and Brazil subject to steward verification; a platform module if Signals' current release
  passes audit), each with its own estimand, denominator and evidence card. No pooling, no ranking
  across modules, visible coverage gaps.
- **Supported by what is verified now.** The European module is ready; the non-European modules
  are leads with named primary sources and concrete next checks, not speculation.
- **Honest about what it is not:** a coverage map, not a world estimate. The explorer must make a
  cross-module comparison impossible by construction where the instruments differ.
- **Verdict:** the only option that is both deliverable and faithful to "ideally global, but led
  by data". It lets geography grow as verification succeeds, without promising it in advance.

### (C) Comparable global survey indicators

- **Not supported by any evidence currently held.** No harmonised multi-country generative-AI
  *adoption* instrument with sex disaggregation has been verified outside Europe.
- The nearest thing found is Pew's 37-country study — genuinely global, population-representative,
  gender-disaggregated and harmonised — but it measures **attitudes and expectations about AI**,
  not generative-AI use. A global *attitudes* comparison may be feasible; a global *adoption*
  comparison is not established.
- **Verdict:** keep as a research question. Revisit only after the discovery leads below are
  checked. Do not design the release around it.

---

## 4. Discovery leads — at most three, as instructed

The coverage gaps are material, so three leads are named. Each is a **primary source** with a
named next check. This is a bounded list, not a licence for open-ended discovery.

**Lead 1 — Pew Research Center global AI survey (37 countries).**
Verified from the publisher's own page on 2026-10-01: 42,151 respondents, fieldwork
8 February – 13 May 2026, 36 countries plus the US, designed to represent each country's adult
population, with gender results reported (a gender difference in 11 mostly high-income countries).
Coverage spans Africa, Asia, Latin America, North America, Oceania, Europe and the Middle East.
*Next check:* whether the topline and detailed-tables appendix publish country-by-gender cells for
every item or only selected ones; and whether a respondent-level release exists. *Caveat:* this is
attitudes, not adoption — it can anchor a genuinely global attitudes module and must never be
presented as a use measure.

**Lead 2 — national statistical offices running ICT-household surveys outside Europe.**
The coordinator's Cetic.br lead (Brazil TIC Domicílios 2025, with sex rows and purpose and
non-use modules) shows the Eurostat *pattern* — an official household ICT survey with the right
structure — exists beyond Europe. *Next check:* a time-boxed enumeration of national statistical
offices publishing a sex-disaggregated generative-AI or AI-tool use item (Brazil, Canada,
Australia, South Korea, and the ITU/UNCTAD indicator catalogues as finding aids), recording for
each whether the item, the sex breakdown and open aggregate access all exist. This is the highest
-value lead for genuine adoption coverage and the one most likely to change Emily's scope decision.

**Lead 3 — re-identify the current OpenAI Signals release.**
The hub page confirms a 2026Q1 Signals update exists, so the prior audit's v2.0 bundle may be
superseded; the data-download page refused two automated requests. *Next check:* obtain the
current release identifier, its licence, its country/month completeness and its name-classification
documentation. Signals remains a **message-level, name-inferred platform** source and can never
substitute for a population survey, but it is the only candidate offering monthly multi-country
granularity.

---

## 5. Unresolved blockers

| Blocker | Attempts made | Reasonable alternative taken | Status |
|---|---|---|---|
| Article repository frozen files and validation report | None attempted — access boundary respected by instruction | Coordinator-supplied provenance recorded as such; current live download hashed independently and found identical | **Not a failure; a declared limitation.** |
| GESIS / ISSP release ZA10020 country list | Three automated requests (two user agents, plus an independent fetcher) — all HTTP 403 | `issp.org` member-states page used instead; establishes 41 member countries across six regions | **Blocked.** Module participation remains unknown; membership is not participation. |
| OpenAI Signals data-download page | Two automated requests — HTTP 403 | OpenAI Signals hub page retrieved; confirms the download page and a 2026Q1 update | **Blocked.** Current release not identified. |
| Cedefop reusable microdata; ECB workplace AI fields; RPS novel-reuse permission | Not re-attempted in this pilot | — | **Carried forward** from the September audit, unchanged. |
| EIGE vs Eurostat cell-count difference | Both pages read | — | **Open.** Use the Eurostat primary. |
| Check C2 residual (BE, SE, NO, LU) | Quantified and localised | — | **Open.** Needs the country-specific notes annex. |

---

## 6. Proposed next checks, in priority order

1. **Resolve Lead 2** with a time-boxed national-statistics enumeration. This is the decision-
   relevant question for release geography and should come before any build work.
2. **Verify the three coordinator-supplied leads** (Cetic.br, Statistics Canada, Melbourne/KPMG)
   to steward standard: population, reference window, AI definition, sex measurement, denominator,
   access and reuse terms. They are currently recorded as coordinator-supplied, not verified.
3. **Resolve Lead 1's gender-by-country cell availability** from the Pew topline and appendix.
4. **Finish the remaining register candidates** (Signals, EWCS, Eurobarometer, ISSP, ILO, Spain)
   that this pilot could not reach. This remains the later full-inventory assignment.
5. **Close the two Eurostat open items**: the C2 residual and the country-specific comparability
   notes, both needed before any country comparison is published.

---

## 7. Boundaries observed

No source-owner was contacted; no registration, terms acceptance or purchase was made; no
restricted or individual-level data were downloaded, and none exist in the Eurostat aggregates
used. Downloads went to ignored local scratch and are not committed — only hashes, code and this
written evidence are. The manuscript was not read, edited or substituted, and `posts/gender1/` was
not used. No agent was spawned. No composite, ranking, causal claim, model or effect estimate was
produced. No register row outside EU_USE / EU_PURPOSE / EU_NONUSE was altered, and
`new_check_this_setup=false` was preserved on all three, retaining its historical meaning that the
30 September migration performed no verification.

The memory stores mounted for this session are read-only, so the durable findings from this pilot
live in these files rather than in the research journal. A coordinator with write access may wish
to record the three definition corrections in §1.2, which are the kind of thing a future session
would otherwise rediscover the hard way.
