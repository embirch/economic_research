# Assignment: Eurostat foundation and geographic feasibility pilot

- User authorisation: Emily, 1 October 2026: "Let's do it - we also need to scope whether this stays European or broader - ideally it is global but we need to be led by data", accepting the proposed first $20 steward pilot.
- Question: Can the existing European measures provide a reproducible foundation, and what does the current candidate inventory actually support beyond Europe?
- Type: bounded source verification and geographic feasibility, not new effect estimation.
- Role: existing data steward, recorded deployed version 3; launcher verifies current deployment. Keep model unchanged. Do not spawn or delegate to other paid agents.
- Inputs: current PROJECT.md, programme/DECISIONS.md, team/SETUP.md, programme/gender-index/EXECUTION-PROPOSAL.md, FIRST-ASSIGNMENT.md, concept-and-feasibility.md, additional-sources-audit-2026-09-30.md, evidence/indicators.csv and literature.csv. Base proposal commit 068b1f4; exact launch commit is recorded by the coordinator in team/RUNS.csv.
- Writable paths: only programme/gender-index/evidence/pilot-2026-10-01/ and, if necessary, the EU_USE/EU_PURPOSE/EU_NONUSE rows of evidence/indicators.csv. Do not alter unrelated register rows. New dated audit links are relative to programme/gender-index/. Keep historical new_check_this_setup=false.
- Branch: work/index-steward-pilot-2026-10-01. Commit and push only your assigned files to this branch. Never push main, merge a PR, alter repository settings or edit coordinator-owned files.
- Budget: user envelope $20; service cap $18 to provide headroom. Stop before exhausting the cap, preserve partial findings, and reserve time to commit/push a short report. No cap increase, additional session, or automatic continuation.
- Review/integration owner: Codex; Emily decides release geography and later assignments.

## Deliverables, in priority order

1. `eurostat-profile.md`: audit EU_USE, EU_PURPOSE and EU_NONUSE with exact table/measure identifiers, populations, source sex categories, denominators/routing, countries and periods, available flags/uncertainty and source reuse terms. Verify primary provider documentation and permitted aggregate files. Do not rely on posts/gender1 or rewrite the first paper.
2. `geographic-coverage.csv`: one row per candidate/source family, with candidate IDs, claimed geography from previous audit, geography newly verified in this pilot, measured construct, unit, sex/gender field, data/access level, comparison limits, primary evidence URL, verification date and status. Review existing non-European/global leads (Signals, Pew, RPS, ISSP, ILO and the synthesis) without promising a full new audit of all 14 candidates. Distinguish documentation-only from file checks. Unknown region/country coverage must remain unknown.
3. `PILOT-REPORT.md`: supported conclusions, unresolved blockers and proposed next checks; compare (A) European core, (B) international evidence resource with source-specific modules, (C) comparable global survey indicators. Assess data for Africa, Asia, Latin America/Caribbean, North America, Oceania and Europe separately. The existing register is Europe-heavy and is not a global search: missing entries are not evidence of no data. Identify at most three high-value primary-source discovery leads if coverage gaps are material; no unlimited discovery.

## Article provenance supplied by the local coordinator

The separate article repository is not mounted in your session and the current GitHub token cannot access it. Do not attempt to work around this access boundary or use the alternative Claude paper instead. Local coordinator inspected its README, data/sources.csv and outputs/validation/report.json read-only on 1 October 2026. Treat the following as supplied provenance, not your own independently verified frozen files:

- Authoritative article commit: 669b9ac on setup/preserve-author-edits-2026-09-30.
- Official frozen use table: data/raw/isoc_ai_iaiu.tsv, retrieved 2026-09-21T15:13:28Z, SHA-256 7f668f7be9aaefaa5662ab2ab059875de8ccbe050c5c38a8de4b2c33a96896ab.
- Retrieval URL: https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/isoc_ai_iaiu/?format=TSV&compressed=false . A current download may differ; record current hash/date and any difference without replacing the manuscript snapshot.
- The article uses the 2025 EU27 core; other covered geographies are separate. Published aggregate cells do not supply complete joint respondent records or sampling standard errors for gender gaps. Resident-population counts are not survey sample sizes.
- Existing source-validation report says four hashes checked and zero common official/mirror value, flag or missingness differences. You cannot independently reproduce that frozen validation without those inputs; state this limitation.

## Acceptance and boundaries

Use primary sources for new verification and retain URLs, exact releases, retrieval dates and reproducible checks. Date previous versus current findings separately. Document a finite failed attempt plus a reasonable alternative before recording blocked access. Download only openly accessible permitted aggregate data/documentation into ignored local scratch paths; never commit raw/individual-level records, third-party archives, credentials or restricted text.

Global ambition does not justify averaging incompatible surveys or treating globally collected platform messages as a representative population survey. Keep country count, world-population coverage, geographic diversity, measurement comparability and population representativeness separate. Do not infer individual gender from occupation or text. Preserve negative gaps, nulls and missingness; no composite, global ranking, causal explanation, new modelling or empirical effect estimates.

No source-owner messages, registration forms, terms acceptance, purchases, manuscript edits, website publishing, old-session resumption or changes outside ownership. Broader full verification remains a later task. If core verification uses most of the budget, save the geographic matrix as an explicitly provisional triage and explain the needed next assignment.

Run python3 team/validate_setup.py and git diff --check, plus any narrowly relevant parsing checks. Inspect staged files for unintended data. Finish with commit SHA, written paths, checks, verified findings, limitations and proposed next action. The coordinator records actual usage in team/RUNS.csv; do not edit that shared ledger yourself.
