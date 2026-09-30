# Handover · economic_research · 30 September 2026

Prepared by the Claude Code session that has coordinated this project since 2 September 2026 (session `d0dd900a-348c-43aa-b607-a2f548570fae`), for coordination to move to Codex. Owner and principal: Emily Birch. No new research was started in preparing this document.

Every statement below is marked **AGREED** (the human decided it, in words recorded here or in `room/`), **DONE** (completed and in the repository), or **PROPOSAL** (suggested by the assistant or an agent; not decided). Where the record is ambiguous it says so.

## 0. Read this first

1. **This repository is public.** GitHub reports `visibility: public` as of 30 September 2026 (it was created private). Everything in it, including `room/`, `wiki/` and every draft, is world-readable. See §9 for what that exposes.
2. **Nothing is running.** All twelve managed-agent sessions are idle; no local driver process is alive.
3. **`main` is fully pushed.** There are no unpushed commits. Completed work that exists only outside the repository is listed in §8.
4. **Two pieces of work are waiting on the human**, not on an agent: the write-up of `posts/gender1` (results signed off; go-ahead not yet given), and the third draft of post 1 on branch `post1-draft` (pull request #1 open, unread).
5. The human controls every spending cap and every gate. Do not raise a cap, merge a pull request or start a stage without her instruction.

## 1. Objectives and agreed scope

**AGREED · programme focus (21 September 2026, `room/human-2026-09-21-gender-series-kickoff.md`).** The central question is how gender differences in AI exposure, adoption and workplace conditions translate into differences in economic opportunity. The Anthropic Economic Index remains a source but is no longer the only one. Gates, stages, templates, the referee procedure, the claims-list boundary, file ownership and the style standard are unchanged.

**AGREED · the wider purpose.** The work is evidence for an application to the Anthropic Fellows programme (economics and policy). It should demonstrate empirical research of the standard Anthropic's economics team publishes, in a register both a general reader and an expert can use.

**AGREED · first post of the series, `posts/gender1`.** "Where is the gender gap in generative AI use widest, and how much of that is measurement?" on Eurostat's 2025 table `isoc_ai_iaiu`. Brief v1.1 approved (Gate 1b); pre-registration revision 2 approved with the word "run" (Gate 2a); built in this repository at the human's instruction.

**AGREED · post 1 (LL-07, "Is AI delegated more on low-wage work or on high-wage work?")** ran as the pilot of the full pipeline. Gates 1b, 2a and 2b were approved. Gate 3 was **sent back** by the human on 18 September (`room/human-2026-09-18-post1-rewrite-brief.md`).

**PROPOSAL · a "Gender Index for AI".** The human's idea of 30 September: an instrument modelled on the Anthropic Economic Index, assembled from public data, with about three spin-off empirical papers, `gender1` being the first. She asked for a landscape scan, which is done (`programme/gender-index/`). The index itself, its pillars, the no-composite-score design and the next step (an indicator inventory and a one-country prototype) are proposals awaiting her decision.

**PROPOSAL · spin-off papers 2 and 3** (the exposure–use mismatch; whether encouragement and training close the gap outside Denmark) and a reserve (topic convergence on OpenAI Signals). Not commissioned.

**PROPOSAL · the editor should build the `gender1` post from the human's own independent draft** (`posts/gender1/notes/independent-draft-emily-2026-09-21.pdf`), binding it to `results.json`. Recommended by the assistant; not approved.

**Not in scope, by the human's decision:** the scenarios thread of the first short-list; reasons for non-use and causal explanation in `gender1`; work by the mentor outside Anthropic.

## 2. Decisions and rejected approaches

| Date | Decision (AGREED unless marked) | Rejected or superseded |
|---|---|---|
| 15 Sep | Single-session research is too fragile; run a team on Claude Managed Agents with gated stages | Single long sessions (`team/LESSONS.md` records why) |
| 15–16 Sep | Start fresh: no inherited briefs; each agent writes only its own files; three stages (briefs, research, write-up) | Reusing the earlier posts' briefs (kept read-only in `reference/`) |
| 16 Sep | Three hard gates for any candidate: a real gap; data confirmed at column level; one standalone question with a clear why-it-matters. First long-list generated with no steer from the human | Steered long-list (later relaxed, see 21 Sep) |
| 16 Sep | All nine short-listed posts to run; scenarios thread left out | — |
| 17 Sep | Pause batch 2 briefs; run post 1 end to end as a pilot | Running all briefs first |
| 17 Sep | The referee's claims list is the boundary of what a post may say; the human reads results and claims before any prose | — |
| 18 Sep | Post 1's first draft rejected: accurate but unreadable to any cold reader. Standard set: understandable to an interested non-specialist, defensible to an expert; the why-it-matters first; what is known with hyperlinked sources; findings as headings; recommendations as action, what it looks like, evidence, why it matters | The template heading "The puzzle Anthropic left open" and any template-label heading; the editor transcribing the claims list into the body |
| 18 Sep | Editor brief rewritten (`team/agents/editor.md`, agent version 4); single-agent tasks run as direct sessions without the director | Routing one-agent tasks through the director (cost) |
| 21 Sep | Programme focus moves to gender; build `gender1` in this repository | A separate repository |
| 21 Sep | `gender1` reports classes, not ranks; a sampling bound from national sample sizes, labelled a lower bound; no invented confidence intervals; every verdict carries its distinguishable count (pre-registration, approved) | Country rankings; bootstrap of published cells; p-values |
| 21 Sep | Frame correction: Eurostat fieldwork ran mostly late March to early August 2025 (Greece July–September), not the first quarter | The pre-registration's "first quarter by convention" |
| 21 Sep | Triangulation leg on Henseke's country gaps dropped (values exist only as a figure image) | Reading values off a chart |
| 30 Sep | PROPOSAL: the index should be a dashboard of parity ratios with absolute gaps, blanks shown, no composite score | Weighted composite score (assistant's recommendation; undecided) |

**Found infeasible with public data (recorded so nobody retries):** person-level gender on any Anthropic release (no demographics anywhere; the June 2026 survey is unreleased); time-of-day analysis (no hour or day grain released); attitudes by usage; tenure or expertise at person level; sex within employment or occupation on the Eurostat table.

**Earlier work, parked:** the pre-team posts on culture and cohort (countries) and on US states, under `reference/posts/`, read-only.

## 3. The human's preferences (working style)

- She holds every gate and every budget cap. Report costs honestly, including overruns; estimates ran low early on.
- Always the why: mechanisms over description; the invisible force behind a published pattern; what each result changes and for whom.
- Surface hidden assumptions and value judgements unprompted; verify every construct, definition and number against the source text or file before writing it.
- Writing: plain and sophisticated at once; no filler or machine-sounding phrasing; short declaratives at claims; enumerations broken out with numbers or (i), (ii); key terms bold at first definition; headings that are synthesised top-down statements; hyperlinks to every Anthropic source drawn on; no first person in posts.
- She reads outputs as rendered pages, not raw files, and asks "where do I read". She wants to see a draft before it goes to any reviewer.
- She dislikes stale background processes and wants to know what is running.
- Security: never paste tokens or keys into a chat; keys live in her shell profile; each agent writes only its own files.
- She cross-checks independently (her own `gender1` draft matched every number) and expects discrepancies to be reconciled, not explained away.

## 4. Completed work (DONE) and outstanding work

### Infrastructure
- DONE: team of seven agents, environment, templates, six skills, session driver (`team/`, `.claude/skills/`, `claude-lock.json`). `team/SETUP.md` is the operating model.
- DONE: knowledge base (`wiki/reports/`, 38 files; `wiki/style/`, 23 annotated files plus `STYLE-GUIDE.md`), data atlas (`data/ATLAS.md`), release profiles and fetch scripts (`data/releases/`, `data/fetch/`), programme files (`programme/LEDGER.md`, `THREADS.md`, `LONGLIST.md`, `SHORTLIST.md`, `CALENDAR.md`).
- DONE: page builder and verifier `site/tools/` exist **on branch `post1-draft` only**, not on `main`.

### Post 1 (LL-07)
- DONE on `main`: brief, feasibility, replication, pre-registration, scripts 01–09, `results.json`, figures, lab notebook, claims list, red-team memo, referee verdicts (brief, pre-registration, results, draft).
- DONE on `post1-draft` (head `16c0955`): third draft of `POST.md` by the editor, claims map, built page, verifier PASS (258 bindings). Pull request #1 is open against `main`.
- OUTSTANDING: the human has not read the third draft. It is about 9,800 words; the assistant recommended a cut pass to about 4,500 (PROPOSAL). No referee review of the third draft has been run. Gate 3 is open.
- OUTSTANDING: the programme lead owes the ledger update for what post 1 answered and opened.

### Posts 2–5 and 6–9 of the first short-list
- DONE: briefs for posts 1–5 (`posts/post1..5/BRIEF.md`). Post 2 passed its sweep; posts 3 and 4 were blocked with fixes written; post 5 had no sweep.
- NOT STARTED: briefs for posts 6–9. No decision has been taken on whether any of posts 2–9 still run after the change of focus.

### `posts/gender1`
- DONE: brief v1.1 and its review; data profile (`data/releases/eurostat_isoc_ai_iaiu.md`) and fetch script; national sample sizes; sampling bound (script 01); pre-registration revision 2 (content `6050e38`); scripts 02–08; `results.json`; five figures; lab notebook with deviations D1–D4; referee verdicts on the pre-registration (BLOCK, then second-read sign-off) and on the results (pass with changes, second read, **SIGN OFF** at `acda4f7`); claims list and red-team memo refreshed; cross-check against the human's independent draft (every number agrees).
- OUTSTANDING: the human's go-ahead for the write-up (Gate 2b page was presented; she replied by cross-checking, not by approving). Then: editor draft, claims map, page build and verifier, referee draft review, second read, Gate 3.
- OUTSTANDING (referee's carried conditions): four items it could not verify, listed at the end of `posts/gender1/notes/referee-results.md`.

### Gender Index for AI
- DONE: landscape scan (`programme/gender-index/LANDSCAPE.md` and three strand reports).
- OUTSTANDING: source verification of the entries marked `[S]`, `†` or "secondary" (LANDSCAPE §8); the indicator inventory and prototype are PROPOSALS.

### Themed long-list
- DONE as a draft only: `programme/LONGLIST-2-themed-DRAFT.md` (twelve candidates, steward and referee checks never run). Superseded in practice by the gender focus; its three gender candidates are a reserve.

## 5. Agent sessions and platform resources

All sessions are **idle**; none is running. Total list cost across the twelve is **$1,307.68** (platform figure, 30 September; an earlier running tally of about $1,650 quoted in conversation was wrong).

| Session | Title | Cost |
|---|---|---|
| `sesn_01HvwCi4cLpaSmRXdRFSy4xY` | Dry run | $3.29 |
| `sesn_01M1zEFQCvbZHzxsw5cvZagj` | Stage 1.1: corpus, style corpus, data atlas | $308.83 |
| `sesn_01UYshDYUpcn3ZmiM6GST3oz` | Stage 1.2: corpus, ledger, threads, criteria | $290.77 |
| `sesn_011WNrwgsL6qj4yrzhGd36Na` | Stage 1.3: long-list, short-list | $180.36 |
| `sesn_01EqtBDUQg7yM1ShX6Gm8D35` | Stage 1.4: briefs | $304.35 |
| `sesn_013yctGFkgUsW7H1gQDQhZEJ` | Post 1 research and write-up | $173.63 |
| `sesn_015TZhXMCXoRmLSfpC3Y8XzV` | Post 1 editor rewrite | $17.32 |
| `sesn_016KhWjfXPeHZcwrE3cyHmg3` | gender1 referee: pre-registration | $7.08 |
| `sesn_01Y8aLQVf6cTBsdHDNffWezw` | gender1 second read: pre-registration | $2.24 |
| `sesn_01J46cb6JHXZWzA3d9jpA64H` | gender1 referee: results | $12.55 |
| `sesn_017BqKaB8BgfAWz9tGMzzxqb` | gender1 second read: results | $3.82 |
| `sesn_01NVw41RLwdUYMhTC8a3HDqk` | gender1 referee: close results | $3.44 |

- **Agents** (IDs in `claude-lock.json`): director, programme lead, data steward, analyst, referee, referee second read, editor. The editor's definition was rewritten on 18 September.
- **Environment:** `team/environment.yaml`. **Memory stores:** IDs in `team/memory-stores.json` (standards, read-only; research journal, written by the director). Both are exported to `team/handover/memory-stores/` as of today.
- **How sessions are run:** `team/run_session.py` (director-led, interactive) and `team/run_agent.py` (one specialist, direct). Both need `ANTHROPIC_API_KEY` and `GITHUB_TOKEN` in the environment.
- **Operating facts learned the hard way:** at most 25 live child threads per session including idle ones; archive idle threads when the director posts `ARCHIVE REQUEST`; sandboxes live at most 30 days, so the September sessions expire between mid and late October and should be treated as closed; three separate billing limits (credits, organisation monthly, workspace monthly) have each stopped a session once; the sandbox has no git identity, so agents pass it per command.
- **Agents push their own files to `main` by design.** `main` has no branch protection. A second coordinator writing to the tree must respect the ownership table in `README.md`.

## 6. Authoritative files and branches

| What | Authoritative location |
|---|---|
| Operating model, gates, stages | `team/SETUP.md`, `README.md` |
| What the team guards against | `team/LESSONS.md` and `team/handover/memory-stores/research-journal/lessons__*` |
| Programme decisions by the human | `room/human-*.md`, `programme/CALENDAR.md` |
| Post 1 research record | `main`: `posts/post1/` |
| Post 1 current draft and page, builder and verifier | branch `post1-draft` at `16c0955` (PR #1) |
| Post 1 earlier drafts | first draft at `e98d27a` on the same branch's history; second draft `posts/post1/notes/human-draft-v2.md` on `main` |
| gender1: what may be said | `posts/gender1/notes/claims.md` (boundary), `data/processed/results.json` (numbers), `prereg/prereg.md` (rules), `notes/lab-notebook.md` (deviations) |
| gender1: the human's own draft | `posts/gender1/notes/independent-draft-emily-2026-09-21.pdf` and its cross-check |
| Eurostat data facts | `data/releases/eurostat_isoc_ai_iaiu.md` |
| Anthropic data facts | `data/ATLAS.md`, `.claude/skills/economic-index-data/` |
| Writing standard | `team/agents/editor.md`, `wiki/style/STYLE-GUIDE.md`, `.claude/skills/anthropic-style/` |
| Gender index idea | `programme/gender-index/LANDSCAPE.md` |

Branches: `main` (default; everything except the post 1 page and tools) and `post1-draft`. Raw data are not in the repository (`data/cache/` is ignored); the fetch scripts rebuild them and the profiles record checksums.

## 7. Information that lived only in conversation or memory, now recorded here

- **Spend and cost pattern.** Discovery and briefs cost about $1,090 across four sessions; post 1 end to end $174 plus $17 for the rewrite; `gender1` about $29 in referee sessions with the analysis run locally. Direct single-agent sessions are the cheap path.
- **Why the editor's first draft failed:** it was told the claims list was the boundary and transcribed it; the lead's why-it-matters note addressed one reader; no gate tested a cold reader. The rewritten editor brief requires a cold-reader test.
- **The referee is the highest-value agent.** It caught non-partitioning decision rules, a false title premise, wrong sample sizes, a backwards ratio ranking and a mislabelled figure. Use it at the pre-registration, results and draft review points.
- **Unreleased agreements about presentation:** results go to the human as a rendered page before any prose; drafts go to her before any reviewer.
- **Data facts not obvious from the files:** the OpenAI Signals bundle carries gender by topic by country by month (name-inferred, message shares); Eurostat's API was down on the morning of 21 September and up that afternoon, and the official extract matches the EIGE mirror cell for cell; Eurostat's table has been revised since February 2026.
- **The exported memory stores** (`team/handover/memory-stores/`) hold the director's per-session status notes, lessons 1–11, data quirks and the house standards. They were previously readable only on the platform.
- **Private context is not in this repository** because the repository is public: the fellowship application materials, personal background notes and a parallel job application. They are in a private handover file on the owner's machine (see §8).

## 8. Completed work that is not on GitHub

`main` has no unpushed commits and the working tree is clean. The following exists only on the owner's machine (`~/Desktop/Anthropic/`):

| Local item | What it is | Note |
|---|---|---|
| `bible/` (about 660 MB, not a git repository) | The owner's reading site: rendered gate pages (`post1-results.html`, `gender1-prereg.html`, `gender1-results.html`, `gender-brief.html`, `gender-index-landscape.html`, `longlist2.html` and others), frozen post 1 drafts v1–v3 under `research-outputs/post1/`, and `research-outputs/LOG.md`, the log of saved versions | Rendered from repository files; the log is the only copy |
| `gender_ai_audit/` (about 100 MB) | The owner's original data audit: scripts, outputs, and `raw/` with downloaded sources | **Contains individual-level survey data (the Spanish study). Do not publish or commit `raw/`.** Its brief, review and audit note are already copied into `posts/gender1/notes/` |
| `economic_research_kb/` and `economic_research_kb.zip` | A mirror of the wiki and data layer built for sharing | Redundant now that the repository is public |
| `site/` | Draft personal website | Not published |
| `research/` (about 530 MB) | The pre-team single-session work and a Python environment | Superseded; source copies of early team files |
| `HANDOVER-PRIVATE.md` and `handover-private/` | Private supplement to this document, with the assistant's memory files | Deliberately outside the repository |
| Local render scripts for the reading site and the first version of the direct session runner | Were in a temporary folder that has been cleared | The runner is recreated as `team/run_agent.py`; the render scripts are lost but their outputs exist in `bible/` and they can be rebuilt from the session transcript |

## 9. Risks and open flags

1. **Public repository.** Now world-readable: the agents' room notes; extended page-referenced extracts from 38 Anthropic publications in `wiki/`; unfinished and rejected drafts; commit metadata with the owner's name and email. Whether to keep it public, trim the wiki to paraphrase and short quotes, or move drafts out is the owner's decision.
2. **Pull request #1 is open and unreviewed.** Merging it would publish a 9,800-word draft the owner has not approved.
3. **Unverified figures in the landscape scan** must be checked at source before use.
4. **No branch protection on `main`**, and agents push there. Adding protection requires changing the agents' push step first.
5. **Session sandboxes expire** about 30 days after creation. Nothing unrecoverable lives in them; the repository is the record.
6. **Licences unchecked:** Eurostat reuse terms, the ILO score repository, the OpenAI Signals README.

## 10. Suggested first actions for the new coordinator (PROPOSALS)

1. Ask the owner three questions: go-ahead for the `gender1` write-up and whether to base it on her draft; what to do with post 1's third draft and PR #1; whether the repository should stay public.
2. If the write-up is approved: one direct editor session with the owner's draft, `claims.md` and `results.json` as inputs; then the referee's draft review and a second read.
3. If the index is approved: the indicator inventory described in `programme/gender-index/LANDSCAPE.md` §9, starting with source verification.
