# Canada editorial pilot: authorised assignment

Authorised by Emily Birch on 9 October 2026 with “ok yes go” in response to the proposed Canada-first method and $30 maximum. This covers the scoped remote input branch, managed editor, standalone native reader, managed referee, bounded coordinator corrections and a conditional managed second read. Brazil and US paid work are not authorised by this pilot.

- Task: developmental editing and evidential review of the existing E08 article, not new analysis.
- Coordinator: Codex, integration owner in the existing local checkout.
- Baseline: current local working files, including uncommitted work. HEAD alone is not the input version.
- Input branch: `work/canada-editorial-pilot-2026-10-09-safe`. This replaces the initial branch after removing an internal results file containing a suppressed time-off aggregate; use released tables only.
- Managed roles: Editor v5; Referee v3; second-read referee v2 if required. Keep deployed settings.
- External maximum: $30. Task allocations $15/$10/$5; initial service limits $13.50/$9/$4.50. No automatic budget increases, extra sessions or reuse of unused allocations for new work.
- Governing method: `../editorial-method-2026-10-09/PROPOSED-METHOD.md`.
- Writable pilot outputs: this directory only; each assignment further narrows ownership.
- Protected: active study masters and all empirical outputs, the report/explorer, historical editions and `gender-gap-generative-ai/paper/author-edits/blog.html`.
- Stop: completed Canada pilot for author judgement, or a specific unresolved issue/budget limit. No public deployment, main-branch merge, new study or restart of completed calculations.

The author must see the proposed complete draft before new manuscript readers are commissioned. The present approval covers those subsequent stages within the cap; a separate spending approval is not required for each specified stage. Preserve any further author direction.

## Current stage

Preparing the verified remote input snapshot and managed Editor assignment. No paid session has started as of preparation. Session and actual spend will be recorded in `team/RUNS.csv`; the immutable input manifest and remote commit identify exactly what the Editor receives.

## Delivery route

The Editor writes a proposed manuscript and companion editorial files in `editor/`, never the live study directory. Codex retrieves and inspects only those outputs, renders a separate proposed article with the existing builders and displays it to Emily. A fresh native reader then receives only the article package, with no inherited conversation or internal rationale. Its first-read record is fixed before the managed Referee receives the full dossier. The coordinator resolves one bounded correction cycle; a conditional second-read assignment checks material corrections and regressions. Final format checks concern the actual delivered version.
