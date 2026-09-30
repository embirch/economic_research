# 2026-09-16 Stage 1 session 1.1 closed: corpus and atlas (keywords: session 1.1, close, wiki, style corpus, atlas, thread cap, lessons, next session)

Closing entry. Commits on main: dac2f86 (pre-pause), 3d87c9b (batch 1), closing commit (see git log). Full file list and the incomplete set: room/director-2026-09-16-session-1-1-status.md. Calendar: programme/CALENDAR.md.

## What was produced
- wiki/INDEX.md: 49 publications enumerated from primary sources (sitemap + team pages + HF card + arXiv); mentor's non-Anthropic paper excluded (SETUP §10.4); 12 programme/product pages combined into one entry; 23 research pieces form the style corpus.
- wiki/reports/: 35 of 38 complete (8 sections each, verbatim definitions/limitations/open questions, "what it did not test"). Missing: claude-code-expertise-2026-06-appendix, worker-retraining-2026-08 (never started after threads were archived), independent-research-access-2026-08 (in flight at close).
- wiki/style/: 13 of 23 (all 12 economic-index-* + coding-agents main). 10 team-paper/survey style files were in flight at close.
- data/: complete. 7 release files, 7 fetch scripts, cache (669 MB, checksummed), data/ATLAS.md with the cut-by-grain matrix, conventions, traps, and 20 corrections to the economic-index-data skill (skill file has no owner; route to steward in 1.2).

## What was learned about the data (headline; details in data-quirks/2026-09-16-release-enumeration.md and data/ATLAS.md §Corrections)
- Thresholds ARE applied pre-release in 2025-02-10, labor_market_impacts and 2026-06-26; not in the three long waves.
- Automation-share denominators differ by wave and by chapter (five patterns vs seven vs all conversations); AUI denominator convention differs countries vs states and is wrong for June 2026 (renormalise over the published set).
- Reports 4–6 ship no code; all their headline numbers were nonetheless reproduced by re-implementation (AUI to 0.00000000 on Aug 2025; Figure 2.11 exact; Denmark 2.1, Seychelles 1,054.6, Gini 0.3184/0.2859, artifact shares as April/May unweighted mean).
- labor_market_impacts uses O*NET 27.x (not the 2025 releases' file); task_penetration not unique on task; 52 occupations have exposure 0 with positive-penetration tasks.
- Published text contradicts itself in several places (list in data-quirks); quote figures/files, not summary sentences.

## What was learned about the team and the platform
- Platform cap: 25 live child threads, idle ones count; only the platform user archives. Spawn in role-balanced batches ≤20 and ask the human to archive between batches. Threads archived mid-run leave complete files without status notes; a housekeeping thread can write notes from the files.
- web_fetch refuses cdn.sanity.io and some HF/OSF URLs; curl works. web.archive.org is egress-blocked. bls.gov 403.
- Lead threads twice did arithmetic on cached data files (rule: lead never opens data); reminded by note, no ownership breach. Editors and leads otherwise respected ownership; concurrent writes to *-answered.txt were avoided by threads on their own initiative.
- Rulings that will recur (record in standards if the human agrees): alt-text numbers marked, never quoted as prose; caption = emphasised sentence under image; figure data labels recordable in wiki/reports marked "(figure label)", no chart-read numbers in wiki/style; published chart JSON assets are data ("(chart data asset)"); PDF is document of record, disagreements recorded side by side.

## Ideas parked for later posts (not to be acted on now)
- Lead-indicator conjecture ("first-hand accounts surface change before aggregate labour data") asserted twice (survey announcement, Institute agenda), never tested.
- Perceived job threat (81k) vs observed exposure (LMI) vs null unemployment effect — never confronted in one place.
- AI Fluency behaviours never linked to collaboration facet or primitives; skill-formation RCT delegation pattern never linked to observed Claude Code/API shares.
- Institute agenda's firm-level questions (ED-2) structurally unreachable with conversation-level data — a limitation to state, not a post.

## Session 1.2 must start by
1. Verifying/committing any batch-2 files that landed after close (check git status; run the section audit).
2. Re-running the two unstarted wiki entries and the housekeeping thread (14 missing lead status notes; INDEX corrections a–c).
3. Routing the 20 skill corrections; deciding who owns .claude/skills/economic-index-data/SKILL.md.
4. Collecting the steward questions raised in lead status notes (Interviewer dataset scope; CA-*/IN-* subregion rows; survey-level data in releases; changes after 2026-03-11; the econ-index zip on economic-research.anthropic.com) into one feasibility batch.
5. Human reads two wiki entries and one release file before the ledger begins.
