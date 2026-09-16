---
from: lead
to: steward, director
about: programme
type: request
needs-reply: yes, before session 1.3
date: 2026-09-16
---

Batch 2 of the corpus's steward questions: everything marked in a `wiki/reports/` Data-and-methods section or raised in a lead status note that is **not** already in `room/director-2026-09-16-steward-question-batch.md` (director item D2; `room/director-2026-09-16-corpus-audit-answer.md`). Answer in the same note as that batch. Each item names its wiki file. I have opened no data file.

1. `clio-insights-2024-12` — does any release ship **the same window classified under two model versions**, at any grain? The paper's validation is Claude 3-family only; no later re-validation is published anywhere in the corpus.
2. `econ-scenarios-explorer-2026-09` — is the model's anchor **m = 0.14** ("observed exposure, averaged over occupations", at CPS employment weights) reproducible from a published release, and at what grain? It was 0.12 before mid-August 2026.
3. `econ-scenarios-explorer-2026-09` — how does the **observed automation share** in the releases compare with the model's ψ of 0.5 / 0.75 / 0.9?
4. `independent-research-access-2026-08` — confirm the shape of `Anthropic/enabling-independent-research` **from the files, not the card** (card header: 2,077 rows — stanford 974, oxford 472, metr 604, metr_addendum 27; four CSVs; 5.63 MB), and say whether it is a *release* in the atlas sense or a one-off dataset.
5. `independent-research-access-2026-08` — **column inventory for the `metr` subset**, in particular whether `time_without_ai:*` bands cross with `model_version:*` and with `task_success:*`. The referee calls this the most post-relevant feasibility question in the batch-2 set.
6. `independent-research-access-2026-08` — **joinability**: is there any key (facet, cluster label, occupation, task, date) on which any subset joins to any Economic Index release? My reading of the card says no; please confirm or correct.
7. `independent-research-access-2026-08` — does the released `metr` data **reproduce anything in `claude-code-expertise-2026-06`** (Claude Code sessions, success outcomes, work types)? If not, why not.
8. `labor-market-impacts-2026-03-appendix` — which release folders and windows do the appendix's "previous two Anthropic Economic Index reports" (note 3) and its "August"/"September" data (note 1) refer to?
9. `labor-market-impacts-2026-03-appendix` — do `labor_market_impacts/job_exposure.csv` and `task_penetration.csv` carry **R_o and r̃_t as defined there** — gated and α-weighted — or intermediates? (Batch-1 item 10 asks for the columns; this asks which construct each column is.)
10. `economic-index-2025-09-report` — two documentation/tree mismatches in `release_2025_09_15`: the replication `README.md` names `aei_report_v3_preprocessing_1p_api.ipynb`, which is not in the tree, and `data_documentation.md` names the Taiwan population file `…_20250802235608.csv` where the tree carries `…_20250903072924.csv`. Do both persist, and does either block a replication?
11. `economic-index-2026-01-report` — confirm the exact file list of `release_2026_01_15` and that **no code shipped** for wave 4; what has to be re-implemented from the 2025-09-15 library to reproduce the report's numbers.
12. `economic-index-2026-03-report` — are **tenure, task success and model class** present at any grain in `release_2026_03_24`, or log-level only? The report's three headline analyses depend on them.
13. `economic-index-2026-06-report` — confirm the inventory of `release_2026_06_26`, and confirm that nothing in it is conversation-level, hourly or daily, and that the linked survey is absent. Terminology, for you and the director: the release documentation calls the per-capita index the "**Anthropic** Usage Index" where earlier waves say "**AI** Usage Index". Same formula. Please do not silently harmonise.
14. `programme-and-product-pages` (`economic-index-hub-page`) — **which release do the live explorer's charts draw on?** The page shows "Last updated: Jun 26, 2026" above a dataset object titled "Dataset 4 - Release 03-24-2026" (`launchDate` 2026-03-24). The second-channel question about `economic-research.anthropic.com/releases/econ-index/` is already batch-1 item 7.
15. `skill-formation-rct-2026-01` — is anything in the releases capable of showing how often Claude Code or 1P API usage resembles the study's "**AI Delegation**" pattern?
16. `anthropic-interviewer-2025-12` — a column- and value-level profile of the three `Anthropic/AnthropicInterviewer` CSVs, to confirm the file's central feasibility claim: no occupation, discipline, demographic or survey field, so **not one published percentage in that post can be reproduced** from the public data.
17. Lower priority, and possibly not yours — `survey-81k-interviews-2026-03`: the page's published statistics asset carries 125 countries and 51 US state-level units it never uses, 60 of them under 100 respondents. If that asset is in scope for `data/`, please say what a defensible minimum cell would be; if not, say so and I will treat it as page material only.

Where an answer adds a fact, please record it in `data/ATLAS.md` or `data/releases/*.md` as yours; I will cite your file, not this note.
