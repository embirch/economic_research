# Operating model: gender and AI

Effective 30 September 2026, following Emily's approval in Codex. Supersedes the September 16 operating model, preserved under `team/archive/`. Current user instructions and `PROJECT.md` govern conflicts.

## Coordination and scope

Emily sets direction, budgets and publication decisions. Codex coordinates the programme here; Claude's existing specialists provide bounded research or review tasks. Use the director for genuinely multi-stage coordination, not as a mandatory intermediary for a single specialist. No paid session starts from setup authorisation alone.

Read `PROJECT.md`, `programme/DECISIONS.md`, the assignment, and relevant current files. Do not reread every historical room message or restart corpus construction. The article in `gender-gap-generative-ai` is authoritative; `posts/gender1` is reference-only. Emily already compared the versions and chose the existing manuscript.

Clarification, 1 October 2026: the programme combines synthesis, original empirical deep-dive papers and interpretation informed by multiple kinds of evidence. Follow `programme/gender-index/RESEARCH-AGENDA.md` for paper selection and triangulation. The first paper can evolve through explicit revisions; preserving author edits is not a permanent freeze on its findings or discussion. Keep source snapshots reproducible, record analytical changes and preserve the current author copy when preparing a revision.

## Assignment contract

Every assignment records the question, task type, inputs, required output, writable paths, work branch, validation, stopping point and approved dollar cap. Use `team/templates/ASSIGNMENT.md`. Record session ID, deployed agent version, source commit, cap and actual spend in `team/RUNS.csv`. Existing session history is historical, not a continuing authorisation. Do not resume a session with superseded instructions for new work.

The coordinator gives each contributor a distinct branch and non-overlapping files. One integration owner resolves conflicts. Reviewer independence means independently examining evidence and calculations; a second LLM review is not journal peer review or a guarantee of correctness.

## Proportionate research sequence

1. **Brief and feasibility:** a standalone question, contribution relative to the wider literature, measurement assumptions, actual available fields and access terms. Emily approves a new study's scope and budget.
2. **Analysis plan:** definitions, sample and exclusions, estimands, primary comparisons, uncertainty and robustness. Disclose prior inspection. Use hypotheses, power and formal decision rules only where appropriate. Review the plan before new primary analysis; honour any existing approval instead of asking again.
3. **Analysis and verification:** maintain immutable source snapshots locally, provenance, code and logged deviations. Reviewers independently reproduce key results and challenge interpretations.
4. **Draft and publication:** editor preserves Emily's voice and existing work, uses verified results and citations, and performs a cold-reader check. Emily sees the draft before a new draft-review agent is commissioned. Publication and additional spending require her instruction.

Reviews can be scoped to changed material. Do not repeat completed work merely to satisfy a template. Inconclusive, null and female-advantage findings are valid; insufficient measurement is a separate outcome. A statistically non-significant estimate does not establish no effect or an effect smaller than the minimum detectable effect.

## Ownership

| Role | Default writable outputs |
|---|---|
| Codex coordinator / director | Current project and operating record, assignments, integration notes, calendar and current memory; cross-cutting setup changes explicitly authorised by Emily |
| Programme lead | Literature records, programme questions and study briefs |
| Data steward | Source atlas, evidence/indicator inventory, licence/access records, fetch scripts and feasibility notes |
| Analyst | Assigned study's analysis plan, scripts, derived results, figures and lab notebook |
| Referee | Review verdicts, independent re-derivations, evidence/claims boundaries and red-team notes |
| Second-read referee | Narrow follow-up review of revisions; refer substantive new issues to full review |
| Editor | Assigned manuscript, claims map, presentation and source-linked prose; never changes empirical outputs to fit wording |

Exact assigned paths override defaults. Read other roles' work; request corrections rather than silently editing it. No specialist may edit the first-paper repository unless its assignment explicitly authorises it. Current setup authorises preserving its edits, not rewriting the article.

## Git and authentication

- `economic_research` is the shared programme repository; `gender-gap-generative-ai` remains the article repository. The parent folder is not a repository.
- Use the existing local `GITHUB_TOKEN` through GitHub CLI or the Git credential helper. Never paste, print, commit or put it in a remote URL. Use the narrowest repository permissions that support the task. Tokens are separate from the Anthropic API key.
- A fine-grained token must include each required private repository. Contents read/write supports code; repository administration is needed for visibility/protection changes. Keep administrative actions with the coordinator/user, even when the current credential permits them.
- Specialists create/use the assignment's work branch. Stage only intended files, commit and push that branch; never push directly to `main`, force-push, merge or change settings. Review the diff and relevant checks before the coordinator integrates an authorised setup change; substantive research/publication changes go to Emily for the relevant decision.
- Branch protection is enforced where the account plan supports it. The setup report distinguishes a verified server rule from a documented workflow. Local hooks/checks are additional safeguards, not access controls.
- No raw/individual-level survey data in this shared repository. Keep fetch scripts, hashes, schemas and permitted aggregates. Private visibility does not grant redistribution rights.

## Agents, memory and configuration

`team/agents/*.md` are deployed with `ant apply`; `claude-lock.json` records resource IDs and versions. Keep model settings unchanged unless Emily requests otherwise. Updating configuration does not launch a paid research session.

`team/sync_memory.py` synchronises current standards and a programme-status note. It preserves the journal history and writes a local deployment receipt. Old journal entries remain dated history. The runners use a current-policy preamble and require a work branch and explicit budget for new sessions. Run new work against the updated agents; old sessions keep historical context.

## Research and release record

Use the evidence register under `programme/gender-index/evidence/`, not a fresh disconnected inventory. Distinguish file-verified, documentation-only and unverified leads. Record source/sample families to avoid double-counting publications of the same study. Store retrieval dates separately from fieldwork and publication dates.

Papers and dashboard indicators should use the same checked derived results, with stable IDs and provenance. Version releases when they are ready; include reproduction instructions, licence decisions, source versions and AI-assistance disclosure. Do not invent a refresh timetable or claim global representativeness from incompatible sources.

## Checks and reporting

`python3 team/validate_setup.py` checks local setup consistency. For empirical changes run the relevant study's checks, not an unrelated blanket test suite. Every handoff reports paths, branch/commit, changes, checks, remaining limitations and spend. A concise human-readable explanation accompanies the file pointers.
