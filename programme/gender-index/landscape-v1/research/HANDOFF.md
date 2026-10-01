# Handoff: landscape v1 evidence synthesis

Programme lead (existing v3 agent), 1 October 2026. Branch `work/index-v1-landscape-2026-10-01`, from launch commit `198acf4`. Writable path used: `programme/gender-index/landscape-v1/research/` only. No other file was touched; `literature.csv`, `indicators.csv`, steward files, coordinator records, `RUNS.csv` and the article repository are unchanged.

## Outputs

| File | What it is |
|---|---|
| `SYNTHESIS.md` | ~2,300-word dated landscape narrative across participation, purposes and intensity, experience and barriers, workplace opportunity and economic context, with a disagreements section and an explicit account of who is not measured |
| `claims-evidence.csv` | 32 claims, each with exact source location, population, reference period, unit and denominator, gender measure, design, verification status, limits, sample family and contrary evidence |
| `literature-updates.csv` | 25 proposed additions and corrections to the central literature record, covering all 11 existing records plus 6 proposed new entries |
| `emerging-questions.md` | 17 unranked questions tied to specific patterns, contradictions and gaps, including Emily's clickstream candidate as an explicitly to-be-decided item |
| `search-log.csv` | 17 dated entries with routes, outcomes and selection reasons, including the three documented access blockers and two deliberate omissions |

## What was verified, and what was not

Read in full at source on 1 October 2026: the foundational HBS working paper (25-023, May 2026), the Pew gender chapter with its chart data tables, the ILO March 2026 research brief, the Allas post, the Eurostat Statistics Explained article, the Cetic.br Brazil table M1, and the GIRAI landing page. Abstracts only: Henseke (arXiv:2604.18849v3) and Stephany and Duszynski (arXiv:2601.03880v2).

**Unverified and marked as such:** Humlum and Vestergaard (PNAS DOI returned `url_not_accessible`; all detail is secondary from the foundational review, and the circulating "11.9 to 5 points with encouragement, 3.6 with training" figures were not confirmed and should be withheld from v1). Noy and Zhang (OSF page returned an empty shell). The Women in AI Index (not retrieved; deliberate omission against the cap). The OpenAI jobs framework (not re-attempted; direct PDF link captured). The AIM-WORK EU null result (secondary only).

**Delivered rather than self-verified:** the UK DSIT cells were reused from the coordinator extract as instructed, and the Statistics Canada cells were supplied by the coordinator within this assignment after the source URL was refused by the fetch service. Both are attributed accordingly and not claimed as this session's verification.

## Four things the coordinator should act on

1. **Emily's foundational designation is implemented.** `SYNTHESIS.md` opens with the HBS paper's role in discovery, synthesis and novelty assessment, and `literature-updates.csv` corrects the register's adoption-only framing: the paper also covers intensity, tool and product differences and mechanisms. Its pooled figures are kept explicitly distinct from population prevalence, and its overlap with four records already in this register is documented.
2. **A sample-family assignment needs correcting.** The register assigns `HENSEKE_WORK` to `EWCS_2024`; the abstract does not name the underlying survey. Treat the family as unconfirmed until the full text is read, or the record and the `EWCS_WORK` indicator row risk being double-counted.
3. **One register identifier needs resolving.** The Pew chapter gives 5,119 US adults surveyed 17–23 February 2026 but no wave number, so `PEW_ATP_W187` is unsupported by the published pages.
4. **Two claims should be blocked from v1 as published numbers.** GIRAI's "53% of the global population has used generative AI tools" has no traceable denominator or source on its page, and the foundational review's "hundreds of billions" extrapolation is an illustration that assumes use causes the gains. Both are recorded as cautions, not evidence.

## Suggested v1 narrative

Lead with the measurement problem, not the gap. A modest male-favouring difference in generative-AI use appears nearly everywhere it has been measured, and it is small beside age and education differences in the same tables. It is closing on the broadest measures — US ever-use is now 50% against 47% — while persisting on frequency, on tool mix, on frontier tools, and most durably in confidence and perceived benefit. Women's work is more exposed to the technology on task-based measures, with 29% of female-dominated occupations exposed against 16% of male-dominated ones, and that exposure sits mainly in clerical and administrative work where automation rather than augmentation is the expected channel. Nobody has yet measured who gains: no source in this register observes pay, hours or promotion in relation to generative-AI use by sex, and that absence is a finding worth printing.

The four apparent disagreements are definitional — outcome, denominator, estimand, construct — so v1 should resolve them by labelling rather than by choosing a number. Report absolute and relative differences together with both underlying rates, keep participation and intensity as separate constructs, hold platform proxies in a separately labelled group, and leave the outcomes cells visibly empty. Do not publish a pooled world rate, do not rank countries whose denominators and age ranges differ, and do not treat men's rate as the target.

## Completion limits

The four regional strands outside Europe and North America remain thin: the only non-European participation cells verified here are Brazilian, and the only non-European workplace cells are Canadian and coordinator-supplied. Four of the six permitted additional primary studies were used; the fifth is logged as a queued unverified record and the sixth was not spent. No new empirical calculation was performed beyond reading published cells. Non-binary and trans populations remain effectively unmeasured across the register, and this synthesis does not establish a direction of causation anywhere.

## Checks

`python3 team/validate_setup.py` passes. CSV shape, quoting, unique IDs, cross-file ID consistency and referenced repository paths were validated with a script run from `/tmp`; `git diff --check` is clean. Source links in all five files were taken from pages fetched in this session or from coordinator records, except the four explicitly marked unverified or not attempted.

## Spend and authorisation

Within the $20 envelope and $18 service limit for this assignment. Codex records actual spend; this session did not edit `team/RUNS.csv`. No delegation, no additional session, no cap increase, no scope expansion, no author contact, no data purchase, no registration and no external publication. Deep-dive selection remains for after v1, and Emily sees v1 before any draft-review session is commissioned.
