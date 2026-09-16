# Claude Managed Agents: design digest for a research team of agents

Source: the 27 pages under `platform.claude.com/docs/en/managed-agents/` (fetched 2026-09-16). Purpose: decide how to build a team of managed agents (research director, brief writer, data specialist, Python analyst over hundreds-of-MB CSVs, QC reviewer, editor) that produce empirical research blog posts from public datasets over days or weeks, using Python, git and the web.

Each page section gives (1) facts that matter, (2) stated best practice and gotchas, (3) constraints on a multi-agent research pipeline. Numbers are quoted as the docs state them. A synthesis follows at the end.

---

## 1. Overview

**Facts.** Four concepts: Agent (model, system prompt, tools, MCP servers, skills), Environment (cloud sandbox or self-hosted), Session (a running agent instance in an environment), Events (messages between your app and the agent). Built-in tools: bash, file ops (read/write/edit/glob/grep), web search and fetch (with domain allow/block lists), MCP servers. Harness includes prompt caching and compaction. All endpoints need the `managed-agents-2026-04-01` beta header (SDK sets it). Access is on by default for API accounts. MCP tunnels and dreaming are a gated research preview.

**Gotchas.** Managed Agents is stateful by design and therefore **not eligible for Zero Data Retention or HIPAA BAA**. You can delete sessions and uploaded files yourself. Positioned for "tasks that run for minutes or hours"; days/weeks is achieved by resuming idle sessions, not by one continuous run.

**Pipeline constraint.** Sessions persist history, sandbox state and outputs server-side; that is the foundation for a long-lived research project, subject to the 30-day sandbox window (see Events page).

## 2. Quickstart

**Facts.** CLI install: `brew install anthropics/tap/ant` (macOS) or the release tarball `VERSION=1.30.0`; `go install github.com/anthropics/anthropic-cli/cmd/ant@latest` needs Go 1.25+. SDK: `pip install anthropic`. Memory-store endpoints use a different header, `agent-memory-2026-07-22`. The full toolset is `{"type": "agent_toolset_20260401"}`. `ant apply` takes a markdown agent file (YAML frontmatter, body = system prompt) or a YAML environment file and records IDs in `claude-lock.json`:

```markdown
---
name: Coding Assistant
model: claude-opus-5
tools:
  - type: agent_toolset_20260401
---
You are a helpful coding assistant.
```

Session loop: open the event stream, then send `user.message`, then iterate events until `session.status_idle`. Sending returns when events are queued. Interactive alternative: `/claude-api managed-agents-onboard` in Claude Code.

**Gotchas.** Open the stream **before** sending the first event (only events emitted after the stream opens are delivered). A "knowledge wiki" quickstart exists: distil a corpus once, answer repeatedly at lower cost — the same shape as a research knowledge base.

## 3. Build in Console (onboarding)

**Facts.** Console gives a visual agent builder (model, system prompt, MCP servers, tools, skills), shows the equivalent API request, and has an inline session runner. You then copy the agent and environment IDs into `client.beta.sessions.create(agent=..., environment_id=..., title=...)`.

**Use.** Fastest place to iterate on each specialist's system prompt and tool selection before committing the definitions to `ant apply` files.

## 4. Define your agent (agent-setup)

**Facts.** Fields: `name` (required), `model` (required; string or object; Claude 4.5+ supported), `system`, `tools`, `mcp_servers`, `skills`, `multiagent`, `description`, `metadata`. Model object form: `{"id": "claude-opus-5", "effort": "high", "speed": "fast", "inference_geo": "us"}`. `effort` accepts `low`, `medium`, `high`, `xhigh`, `max`; the create response fills defaults, e.g. `"effort": {"type": "high"}, "speed": "standard"`. Fast mode: Opus 5 or Opus 4.8 only. `inference_geo` is `"us"` or `"global"`. `version` starts at 1 and increments on each change. Response shows the toolset's `default_config.permission_policy` is `always_allow`.

Updates: `client.beta.agents.update(agent.id, version=agent.version, system=...)`. `version` is optional; supplying it gives optimistic concurrency (409 on mismatch), omitting it is last-write-wins (suited to CI apply loops). Omitted fields are preserved; scalar fields replaced; `system`/`description` clearable with `null`; array fields (`tools`, `mcp_servers`, `skills`) fully replaced; `multiagent` replaced whole; `metadata` merged per key (`null` deletes a key); no-op updates create no version. Within `model`, omitting `effort` keeps the stored effort only if `id` is unchanged; supplying `model` without `inference_geo` clears the pin. `ant beta:agents:versions list --agent-id ...` lists history. Archive is read-only and irreversible; running sessions continue.

**Gotchas.** A per-session `model` override **does not apply `effort`** and drops the agent's effort, running at the model default; set effort on the agent instead. Coordinator rosters do **not** follow agent updates: they keep the version pinned at coordinator create/update time even when the reference omitted `version`.

**Pipeline constraint.** Every specialist is a versioned resource; pin sessions to versions for reproducible runs, and re-apply the coordinator whenever a specialist changes.

## 5. Define outcomes

**Facts.** A `user.define_outcome` event carries `description`, `rubric` (`{"type": "text", "content": ...}` or `{"type": "file", "file_id": ...}`; required) and optional `max_iterations` (default 3, max 20). The harness provisions a **grader in a separate context window**; it returns per-criterion pass/fail explanation, fed back to the agent. Events: `span.outcome_evaluation_start` (0-indexed `iteration`), `_ongoing` heartbeat, `_end` with `result` in `satisfied` (idle), `needs_revision` (new iteration), `max_iterations_reached` (one acknowledgment turn then idle), `failed` (rubric does not apply / contradicts description), `interrupted`. `_end` includes `usage`. Poll `GET /v1/sessions/{id}` and read `outcome_evaluations[].result` (`pending`, `running`, `evaluating` before completion). One outcome at a time; chain by sending the next after the terminal `_end`. Can be placed in `initial_events`. Deliverables go in `/mnt/session/outputs/`; list with `client.beta.files.list(scope_id=session.id, betas=["managed-agents-2026-04-01"])` and download by ID.

**Best practice.** Write explicit, gradeable criteria ("The CSV contains a price column with numeric values"), not "the data looks good"; vague criteria give noisy grades. If you lack a rubric, give Claude a known-good artifact and have it derive one. The grader runs **without** `web_search`/`web_fetch`. Output files can appear a few seconds after idle; re-list if missing.

**Pipeline constraint.** Outcomes are the platform's built-in QC loop: rubric-driven self-revision with an independent grader. Useful for "the post must contain X, Y, Z" checks, but the grader is opaque and cannot fetch sources, so factual verification against the web still needs your reviewer agent.

## 6. Multiagent orchestration

**Facts.** Declared on the coordinator: `multiagent: {type: coordinator, agents: [...]}`. Roster entries: `{"type": "agent", "id": ...}` (pinned to latest at coordinator create time), `{"type": "agent", "id", "version"}`, `{"type": "self"}` (copies of the coordinator; session overrides apply to these), `{"type": "advisor", "model": ...}` (at most one; reserved name `anthropic.advisor`; advisor must be at least as capable as the agent; Opus 5 advice is redacted on the stream, Opus 4.8 advice is readable). In `ant apply` files, roster entries can be paths such as `./reviewer.md`; apply creates them first and substitutes pinned references.

**All agents share the same sandbox, filesystem and vault credentials**, but each runs in its own **session thread** with isolated context. Threads persist: the coordinator can follow up with an agent it called earlier and it remembers prior turns. Each agent uses its own model, system prompt, tools, MCP servers and skills; tools and context are not shared. Limits: **one level of delegation** (a roster member with its own roster fails validation); **maximum 20 unique agents** in a roster (multiple copies allowed); **maximum 25 concurrent threads** (advisor threads exempt); archive idle threads to free slots. Inference-geo pins must all match or all be unset.

The session-level stream is the **primary thread**: a condensed view (start/end of subagent work, blocking events). Each thread has its own stream at `/v1/sessions/{id}/threads/{thread_id}/stream`. Events: `session.thread_created`, `session.thread_status_running/idle/terminated`, `agent.thread_message_received` (subagent report to coordinator), `agent.thread_message_sent` (coordinator task to subagent). Tool confirmations and custom-tool calls from subagents are cross-posted to the primary thread with `session_thread_id`; reply with `user.tool_confirmation` / `user.custom_tool_result` and the server routes them. `user.interrupt` with `session_thread_id` stops one thread; without it, all. The coordinator has `list_agents` and `send_to_agent` tools. Session status is `running` if any thread is. Session budget is one shared cap across threads.

**Best practice.** Delegate for parallelisation, specialisation, escalation. MCP servers are agent-scoped; vault credentials are session-scoped (`vault_ids` apply to every thread). To limit an agent, declare only the servers it needs. Web domain lists of roster agents **intersect** with the coordinator's; keep each roster allowlist inside the coordinator's or every call fails with `url_not_allowed`. Under `auto`, denials inside a subagent thread are not cross-posted.

**Pipeline constraint.** The shared filesystem is the hand-off mechanism: the analyst writes CSV summaries and figures to disk, the editor reads them. Messages between threads are the control channel. Because delegation is one level deep, the director cannot delegate to a "data lead" who in turn delegates; all six roles sit directly under one coordinator.

## 7. Using agent memory

**Facts.** Memory stores are workspace-scoped text collections mounted read/write inside the sandbox at `/mnt/memory/<slugified-name>/` (read `mount_path` from the session resource rather than constructing it). Beta header for store endpoints: `agent-memory-2026-07-22` (do not combine with `managed-agents-2026-04-01`: 400). Create: `client.beta.memory_stores.create(name=..., description=...)` (description is shown to the agent). Attach at session creation only, in `resources[]`: `{"type": "memory_store", "memory_store_id": ..., "access": "read_write" | "read_only", "instructions": ...}`; `instructions` ≤ 4,096 characters; default access `read_write`. Limits: **100 kB (~25k tokens) per memory**, **10,000 memories per store**, **8 stores per session**. Requires the agent toolset. Every write creates an immutable version (`memver_...`); versions retained 30 days (recent versions of live memories kept longer); redact available; rollback is manual (retrieve version, write back). API CRUD with `path`, `content`, `content_sha256` precondition for optimistic concurrency; `path_prefix` (must end with `/`) and `depth` (0 or 1) for listing. Archive is one-way.

**Best practice.** Many small focused files, not a few large ones. Use `read_only` for reference material and for any store the agent does not need to modify: with `read_write`, a prompt injection from fetched web content can poison memory that later sessions trust. Use focused stores (per user, shared domain knowledge, per project). When a store nears 10,000 memories, prune, run a dream, or attach a fresh store and make the old one `read_only`. Writes to any path under `/mnt/memory/` outside a mount fail.

**Pipeline constraint.** Memory is how house style, dataset quirks, prior mistakes and project state survive across sessions. All threads in a multiagent session see the same mounts, so specialists can share one project store and one read-only "standards" store.

## 8. Skills

**Facts.** Two sources: the agent's `skills` array (`{"type": "anthropic", "skill_id": "xlsx"}` for pre-built `pptx`, `xlsx`, `docx`, `pdf`; `{"type": "custom", "skill_id": "skill_01...", "version": "latest"}`), or a mounted GitHub repository's root `.claude/skills/<skill-name>/SKILL.md` (exactly one level deep, scanned once at session start, requires the `read` tool). Custom skills are a directory with `SKILL.md` plus supporting files, uploaded with `client.skills.create(files=files_from_dir("example_skill"))` or `ant skills create --file example_skill.zip`; `display_name` ≤ 255 chars. Up to **500 skills per session** (deduplicated across all agents).

**Gotchas.** Each skill costs context; more skills slow sandbox start, so attach only what each agent needs. Repository skills are part of the trust boundary: anyone who can commit can change agent instructions with no review step. Commits pushed mid-session are not picked up. Self-hosted sandboxes do not support repository resources.

**Pipeline constraint.** Skills are the right place for procedural know-how (how to profile a CSV, how to structure a post, the QC checklist), versioned either in the workspace or in the project's git repo.

## 9. Tools

**Facts.** Toolset names: `bash`, `read`, `write`, `edit`, `glob`, `grep`, `web_fetch`, `web_search`. All enabled by default; disable with `configs: [{name: web_fetch, enabled: false}]` or start from `default_config: {enabled: false}`. **Tool output over 100,000 characters (~25,000 tokens) is written to a sandbox file** and the model gets a truncated preview plus the path. Web settings per entry: `allowed_domains` or `blocked_domains` (never both; 1–64 plain ASCII hostnames, subdomains covered, no IPs, no bare TLDs, no `localhost`; `web_fetch` domains cannot carry paths), `max_content_tokens` (`web_fetch`), `user_location` (`web_search`). Validation at agent create/update and session create/update; a setting that later becomes invalid emits `session.error` and the session returns to idle. Environment `networking` does **not** govern `web_search`/`web_fetch` (they run on Anthropic's servers); Console org-level web settings apply only to the Messages API. Not available on the toolset: `max_uses`, `citations`, `cache_control`. Custom tools: `{"type": "custom", "name", "description", "input_schema"}`; the agent emits `agent.custom_tool_use` and your code answers.

**Best practice.** Very detailed tool descriptions (three to four sentences); consolidate related operations into one tool with an `action` parameter; namespace names; return only high-signal fields.

**Pipeline constraint.** The 100k-character spill-to-file rule means `head`-style previews of big CSVs are safe; bulk output lands on disk, not in context. Restrict the analyst's `web_*` to data portals and the reviewer's to citation domains.

## 10. Adding files

**Facts.** Upload with `client.files.upload(file=Path("data.csv"))` or `ant files upload --file data.csv`. Mount at session creation: `resources: [{type: file, file_id, mount_path: "/data.csv"}]`; the file appears at `/mnt/session/uploads/data.csv` (omit `mount_path` and it lands at `/mnt/session/uploads/<file_id>`). Mounted files are **read-only copies**; session copies do not count toward Files API storage limits. **Maximum 500 files per session.** Add/remove files on a running session with `client.beta.sessions.resources.add/list/delete`. Files the agent writes to `/mnt/session/outputs/` are retrievable through the Files API scoped by `scope_id` (beta header required) and appear a few seconds after idle. Any file type; archives can be extracted with bash.

**Pipeline constraint.** Files in: upload once, mount many times, or have the agent `curl`/`wget` public datasets directly (unrestricted networking). Files out: `/mnt/session/outputs/`, which is deleted with the session, so download or push to git before deleting.

## 11. Accessing GitHub

**Facts.** Mount with `resources: [{type: github_repository, url: "https://github.com/<owner>/<repo>", authorization_token: "ghp_...", mount_path: "/workspace/repo", checkout: {type: branch, name: main} | {type: commit, sha}}]`. URL must be the HTTPS form without `.git`. `mount_path` defaults to `/workspace/<repo-name>`. Repositories are cached so later sessions start faster. Token is never echoed; rotate with `resources.update(..., authorization_token=...)`. Repositories are attached for the session's lifetime (new session to change the set). Token scopes: `repo` for private clone/PRs; `public_repo` for public issues. GitHub MCP server: `{"type": "url", "name": "github", "url": "https://api.githubcopilot.com/mcp/"}` plus `{"type": "mcp_toolset", "mcp_server_name": "github"}`; with it the agent can create branches, commit and push. `git` is preinstalled in cloud sandboxes.

**Best practice.** Fine-grained PATs with minimum scopes. Mounting also loads `.claude/skills`.

**Pipeline constraint.** Git is the durable, human-reviewable output channel: the mounted repo holds notebooks, scripts, figures and the draft post; the editor pushes a branch and opens a PR. Cloud environments only.

## 12. Authenticate with vaults

**Facts.** Vault = collection of credentials, workspace-scoped (any workspace API key can reference it). Credential types: `mcp_oauth` (with optional `refresh` block; Anthropic refreshes), `static_bearer` (keyed by `mcp_server_url`), `environment_variable` (keyed by `secret_name`; the sandbox sees an opaque placeholder substituted **at egress**; `networking.allowed_hosts` limits which hosts get the real value; `injection_location: {header, body}`, Console defaults to header-only). **Maximum 20 credentials per vault**; keys are unique and immutable. Secret values are write-only. Pass `vault_ids=[...]` at session creation; credentials apply to every thread. Re-resolved periodically, so rotation propagates without restart. Validate OAuth with `mcp_oauth_validate` (`valid`/`invalid`/`unknown`).

**Gotchas.** Egress substitution breaks clients that validate key format locally or sign requests (AWS SigV4). Substitution is outbound only; a token fetched with the secret arrives unredacted. Both the vault `allowed_hosts` and the environment networking must permit the host. `environment_variable` credentials are not supported on self-hosted sandboxes.

**Pipeline constraint.** Use `environment_variable` for data-API keys (e.g. a statistics portal) and `static_bearer`/`mcp_oauth` for the GitHub MCP; the GitHub clone token itself goes on the `github_repository` resource, not the vault.

## 13. MCP connector

**Facts.** `mcp_servers: [{type: url, name (1–255 chars, unique), url (≤ 2,048 chars)}]`; **up to 20 servers per agent**; every server needs a matching `mcp_toolset` and vice versa. MCP toolsets **default to `always_ask`**. Restrict tools with `default_config: {enabled: false}` plus explicit `configs` (`name`, `enabled`, `permission_policy` only). MCP outputs over 100,000 characters are spilled to a file. Session creation does not validate connectivity; failures emit `session.error` with `mcp_connection_failed_error` or `mcp_authentication_failed_error` and are retried at the next idle→running transition. Credential URLs are normalised (scheme/host case, default port, trailing slash) but a different path or subdomain does not match.

**Pipeline constraint.** Only the agents that need GitHub PR tools should declare the server; set `always_allow` only on a curated tool subset if you want unattended runs.

## 14. Permission policies

**Facts.** Policies: `always_allow` (agent toolset default), `always_ask` (MCP default), `auto` (server evaluates each call: runs, denies with `Permission to use {tool_name} has been denied.` and `is_error: true`, or pauses with `reason_code: indeterminate`). Set on `default_config.permission_policy` or per tool in `configs`. Running sessions keep the policy they started with. Each `agent.tool_use` / `agent.mcp_tool_use` carries `evaluated_permission` (`allow`/`ask`/`deny`) and an `evaluation` object. A paused call surfaces as `session.status_idle` with `stop_reason.type: requires_action` and `event_ids`; answer with `user.tool_confirmation {tool_use_id, result: allow|deny, deny_message}`; the session **waits indefinitely**. `ant beta:sessions connect` answers interactively. Custom tools are not governed by policies.

**Gotchas.** `auto` is **not a human checkpoint**; if a person must review, use `always_ask`. Under `auto`, text in your `user.message` counts as intent and can get a call allowed; relayed untrusted input therefore does too. Clients cannot override server denials.

**Pipeline constraint.** Human-in-the-loop can be placed exactly on the risky actions (e.g. `always_ask` on the GitHub MCP's push/PR tools, `always_allow` on bash for the analyst), with every pause visible on the primary thread even when a subagent triggered it.

## 15. Cloud environment setup

**Facts.** `config: {type: cloud, packages: {pip: [...], apt: [...], npm, cargo, gem, go}, networking: {...}}`. Packages are installed before the agent starts and cached across sessions sharing the environment; pin versions like `"sqlalchemy==2.0.30"`. Networking: `unrestricted` (default; general safety blocklist) or `limited` with `allowed_hosts` (bare hostnames or `*.example.com`), `allow_mcp_servers` (default false), `allow_package_managers` (default false; **required** whenever `packages` is set, else 400). Environments are not versioned; each session gets its own fresh container; delete only when no sessions reference it.

**Best practice.** Production: `limited` networking with explicit `allowed_hosts`, least privilege, regular audit.

**Pipeline constraint.** Sessions do not share filesystem state with each other; only threads within one session do. Pre-install `pandas`, `pyarrow`, `duckdb`, `statsmodels`, `polars` etc. via `packages.pip` so each new session starts warm.

## 16. Cloud sandbox reference

**Facts.** Ubuntu 24.04 LTS, x86_64, **memory up to 8 GB, disk up to 10 GB**. Python 3.10–3.13 with pip, uv, poetry; NumPy, pandas, Matplotlib, openpyxl, python-docx, python-pptx, pypdf preinstalled for `python3`. Node 20–22, Go, Rust, Java 21, Ruby, PHP, C/C++. PostgreSQL 16 and Redis 7 installed but not running; SQLite via bindings. Tools: git, curl, wget, jq, yq, ripgrep, tmux, pandoc, LibreOffice headless, Poppler, tesseract, TeX Live, ffmpeg, ImageMagick, Playwright + Chromium (Firefox/WebKit absent). API-created environments default to `unrestricted` networking; Claude Studio ones default to `limited`.

**Pipeline constraint.** Hundreds-of-MB CSVs fit on the 10 GB disk but a naive `pandas.read_csv` of several such files can exceed 8 GB RAM; the analyst needs chunked/`dtype`-specified reads, Parquet conversion, or DuckDB/SQLite over the CSV. PostgreSQL is available locally if you want SQL over the data.

## 17. Start a session

**Facts.** `agent` accepts a string (latest version), `{type: agent, id, version}` (pinned), or `{type: agent_with_overrides, id, model?, system?, tools?, mcp_servers?, skills?}`. Override rules: omit = inherit; `null`/`[]` = clear (except `model`, and `tools` when skills are attached because skills need `read`); a value replaces in full (no merge); effort in a model override is ignored. `initial_events`: up to 50 `user.message` / `user.define_outcome` events, processed in order; a non-empty list starts the session directly in `running`. Rejections: more than one `define_outcome` (400), outcome without rubric (400), more than 100 file-sourced document blocks (400), body over 32 MB (413). Sandbox provisioning starts at session creation even without events. `budget` (see Budgets) can only be attached at creation. `vault_ids` supplies MCP/env credentials. `title` and `metadata` available.

**Pipeline constraint.** A "project session" can be created once with repo, datasets, memory stores and budget, then driven for weeks by successive `user.message` events.

## 18. Session operations

**Facts.** Statuses: `idle`, `running`, `rescheduling` (transient error, auto-retry), `terminated` (unrecoverable error or archived; finished work goes `idle`, not `terminated`). Mid-session you can update only `agent.tools` and `agent.mcp_servers` (full replacement; session must be idle; interrupt first if running); model, system, skills, inference geo are fixed for the session's life, though `system.message` events can append guidance on supported models. Budget can be raised/lowered (must exceed consumed cost) or removed (one-way). Listing is cursor-paginated (`limit`, `page`, `order` asc/desc). Archive and delete require idle. **Delete removes the sandbox and all files the session produced**; uploaded Files API files, memory stores, vaults, skills, environments and agents survive.

**Pipeline constraint.** Download `/mnt/session/outputs/` or push to git before deleting a session; wait for files to appear in the list first.

## 19. Session event stream

**Facts.** User events: `user.message`, `user.interrupt`, `user.tool_confirmation`, `user.custom_tool_result`, `user.define_outcome`, `user.tool_result` (self-hosted only). `system.message` appends system context for the current and later turns; supported on Claude Fable 5.1, Mythos 5.1, Fable 5, Mythos 5, Opus 5 and Opus 4.8 (else `model_does_not_support_mid_conversation_system`); content 1–1,000 text items; primary thread only. Agent events include `agent.message`, `agent.thinking` (progress only, no content), `agent.tool_use`/`tool_result`, `agent.mcp_tool_use`/`result`, `agent.custom_tool_use`, `agent.thread_context_compacted`, and the thread message events. Span events: `span.model_request_start/end` (with `model_usage`), outcome spans. `session.usage` is emitted immediately before every idle transition, with tokens, `list_cost` (whole cents as a string), `active_seconds`, `server_tool_use` counts and the budget. Interrupt: model output stops immediately, tool calls may finish first; the idle `stop_reason` is `end_turn`. Reconnect: open a new stream, list history to seed seen IDs, tail and skip duplicates. Event deltas (`event_deltas=["agent.message"]`) give best-effort text previews on that connection only, never persisted, never replayed. Prompt cache entries use a 5-minute TTL, so back-to-back turns are cheaper. **Sandbox state is preserved for 30 days after the sandbox is created; activity does not extend it**; after that a resumed session starts from a fresh sandbox while history persists. Console session viewer shows a per-thread timeline, transcript, tools, resources and threads; `?event={event_id}` deep-links.

**Best practice.** Add logging instructions to the system prompt; watch `session.error` and tool results when behaviour is odd; enforce spend with a budget rather than polling.

**Pipeline constraint.** The 30-day sandbox clock is the hard limit on a single "project session"; for multi-week projects, write everything that matters to git, memory stores or outputs, and plan to start a fresh session (re-mount repo and stores) before day 30.

## 20. Subscribe to webhooks

**Facts.** Events carry `type` and `id` only; fetch the object. Session events: `session.status_run_started`, `session.status_idled`, `session.budget_reached` (once per budget value), `session.status_rescheduled`, `session.status_terminated`, `session.thread_created/idled/terminated`, `session.outcome_evaluation_ended`, `session.updated`, `session.deleted`. Also vault, agent, deployment, deployment_run, environment and memory_store lifecycle events. Endpoint: HTTPS on 443, public hostname; signing secret `whsec_` (32 bytes, shown once); verify with `client.beta.webhooks.unwrap(body, headers=...)`, which rejects payloads older than 5 minutes. Delivery: up to three attempts with jittered backoff of 5–120 seconds, then dropped; duplicates share `event.id`; **ordering not guaranteed**; no backfill for events emitted before subscribing or while disabled; a `3xx` disables the endpoint immediately.

**Pipeline constraint.** Wake your orchestration (and notify a human) on `session.status_idled` and `session.budget_reached`; treat webhooks as hints and reconcile from the API.

## 21. Session budgets

**Facts.** `budget: {type: limit, max_list_cost: {amount: "2500", currency: "USD"}}`; `amount` is whole cents as a string (`"125"` = $1.25), no decimals, > 0; USD only. List cost = model tokens at list price + **web searches at $10 per 1,000** + **session running time at $0.08 per hour**; contracted discounts do not change the cap. Enforced between model requests; overshoot bounded by one request per thread. At cap: threads pause, `session.usage`, then `session.status_idle` with `stop_reason: budget_reached`; only settle events (`user.tool_confirmation`, `user.tool_result`, `user.custom_tool_result`, `user.interrupt`) accepted; `user.message` is 400. Resume by updating the budget above the consumed cost (base it on reported `usage.list_cost` plus at least a cent) or removing it (`budget=None`, one-way). Multiagent: one shared cap, per-thread pricing at the served model; advisor tokens count. A pending `requires_action` outranks `budget_reached`. Deployments copy the cap onto each run. Models with no public list price are rejected on budgeted sessions.

**Pipeline constraint.** This is the primary cost control: one hard cap per project session, raised deliberately by a human at each checkpoint.

## 22. Scheduled deployments

**Facts.** `client.beta.deployments.create(name, agent, environment_id, initial_events=[...], schedule={type: cron, expression: "0 20 * * 5", timezone: "America/New_York"}, budget?)`. Standard POSIX cron, minute granularity, IANA timezone, literal wall-clock DST matching (non-existent times skipped, repeated times fire twice; avoid 1–3 AM local). Jitter up to 15% of the interval (min 5 s, max 9 min). At least one initial event (`user.message` or `user.define_outcome`; deployment `initial_events` also accept `system.message`). Resources (files, GitHub, memory stores, vaults) accepted; file/GitHub need a cloud environment. **Max 1,000 deployments per organization.** Each firing creates a `deployment_run` with `session_id` or `error` (`environment_archived_error`, `agent_archived_error`, `session_rate_limited_error`). Rate-limited runs are not retried until the next occurrence; unrecoverable errors auto-pause the deployment. Pause/unpause (no backfill), archive (terminal), manual `run`.

**Pipeline constraint.** Each run is a **new session** with a fresh sandbox, so recurring jobs (e.g. nightly "refresh the dataset and rerun the notebooks", or weekly "consolidate memory") must reload state from the mounted repo and memory stores.

## 23. Dreams

**Facts.** Research preview gated by `dreaming-2026-04-21`. Inputs: one memory store plus 1–100 sessions; `model` from `claude-opus-5`, `claude-fable-5`, `claude-opus-4-8`, `claude-opus-4-7`, `claude-sonnet-5`, `claude-sonnet-4-6`; optional `instructions` ≤ 4,096 chars. Produces a **new** output store (input untouched); takes minutes to hours; billed at token rates, roughly linear in transcript volume. Statuses `pending`, `running`, `completed`, `failed`, `canceled`; the running pipeline's `session_id` can be streamed. Errors include `input_memory_store_too_large` and `timeout`.

**Pipeline constraint.** The intended way to turn weeks of messy memory writes into a clean knowledge base between projects; start with a small batch of sessions.

## 24. Reference

**Facts.** Rate limits per organization: **create endpoints 300 requests/minute, read endpoints 1,200 requests/minute**, plus org spend and usage-tier limits. Full event-type catalogue (user, agent, session, span, system, deltas). MCP servers must expose streamable HTTP (SSE-only works via fallback). Self-hosted worker flags: `--environment-id`, `--environment-key`, `--workdir` (default `.`; system default `/workspace`), `--on-work`, `--unrestricted-paths`, `--max-idle` (default `60s`), `--log-format`. The CLI worker does not mount memory stores. Branding: "Claude Agent" allowed; "Claude Code"/"Claude Cowork" not.

## 25. Migration

**Facts.** From a Messages API loop: history, tool execution, sandbox and loop termination move server-side; you keep system prompt, model, custom tools (now answered via events), web settings (now on the toolset). From the Claude Agent SDK: `ClaudeAgentOptions` → persisted agent; `query()` → session events; `@tool` → `custom` tools; `cwd`/`add_dirs` → mounted files; `CLAUDE.md` hierarchy → single `system` string; `permission_mode` → per-tool `permission_policy`. Things that move to your client: plan mode (run a planning session, then an execution session), `PreToolUse`/`PostToolUse` hooks (`always_ask` or custom-tool handling), `max_turns` (count client-side). Model upgrades are a one-field change; `max_tokens`/`thinking` are managed by the runtime and not exposed.

**Pipeline constraint.** Turn limits and "plan then execute" gates are your orchestrator's job, expressed as outcomes, budgets and separate messages.

## 26. Self-hosted sandboxes

**Facts.** Orchestration stays with Anthropic; tools run in your infrastructure via a worker that polls the environment's work queue (`ant beta:worker poll --workdir /workspace` or the SDK `EnvironmentWorker`; webhook-triggered variant wakes on `session.status_run_started`). Needs a Linux host with `/bin/bash`. Auth is an environment key (Console-only generation) plus a per-session `secret` for memory stores. **File and GitHub resources are not supported** (400); pass pointers such as an S3 path in session `metadata` and stage files yourself. Memory stores work only with the SDK worker: downloaded to `/mnt/memory/`, synced at most every 15 s (min 5 s), final flush up to 30 s, conflicts resolve in favour of the store, one session per filesystem per store. Outputs land wherever the agent writes them (no `/mnt/session/outputs` instruction). Custom tools can be served from the sandbox, including wrapping an internal MCP server (declare tools up front; ≤ 128 entries in `tools`; names 1–128 chars; no `$ref`/top-level `oneOf`). Ops: `work.stats` (`depth`, `pending`, `workers_polling`), `work.stop`. Platform guides exist for AWS Lambda MicroVMs, Modal, E2B, Daytona, Cloudflare, Fly.io, GKE, Vercel and others.

**Pipeline constraint.** Self-hosting removes the 8 GB/10 GB ceiling and lets the analyst sit next to the data, at the cost of losing GitHub/file mounts, egress-substituted secrets and the outputs convention. Only worth it if the datasets outgrow the cloud sandbox.

## 27. Self-hosted security model

**Facts.** You own: image hardening (non-root, read-only rootfs, dropped capabilities), egress firewalling, `ANTHROPIC_ENVIRONMENT_KEY` storage and rotation, isolation of untrusted workloads (separate workspace/environment per trust boundary), per-session `secret` handling, tool blast radius, log retention, and cleanup of `/mnt/memory` copies. Read-only stores are protected from upload, not from local modification by `bash`; disable `bash` if the local view must be immutable. Anthropic cannot detect a leaked key, verify your image, isolate tools inside your sandbox, or enforce retention on your side.

---

## Design implications for a research team of agents

**Topology: one coordinator session with a roster, not six separate sessions.** The decisive fact is that roster agents share one sandbox and filesystem while keeping isolated context. A single "research director" coordinator (`claude-opus-5`, `effort: high` or `xhigh`) with a roster of brief-writer, data-specialist, analyst, QC-reviewer and editor agents gives you file-based hand-offs (the analyst writes `analysis/results.parquet` and `figures/*.png`; the editor reads them) plus persistent per-agent threads the director can revisit. Separate sessions would each get a fresh container and would have to exchange everything through the Files API or git. The constraints fit the team: six agents is well under the 20-agent and 25-thread limits, and one level of delegation is enough if the director is the only orchestrator. Give the analyst and data specialist `claude-opus-5` (correctness on data work), the brief writer and editor `claude-opus-5` or `claude-sonnet-5`, and consider `claude-opus-4-8` as an advisor so its advice is readable on the stream. Define all of this as `ant apply` markdown files with roster paths, checked into the project repo, and re-apply the director whenever a specialist changes (rosters pin versions).

**Persisting knowledge: git for artefacts, memory for judgement, skills for procedure.** The sandbox lives at most 30 days from creation and is deleted with the session, so nothing durable should live only on its disk. Mount the project GitHub repository at session start; the editor commits scripts, figures and drafts and opens PRs (GitHub MCP with `always_ask` on push/PR tools, or plain `git` over bash with a fine-grained PAT). Attach two memory stores: a read-only "standards" store (house style, statistical checklist, citation rules, seeded via the API) and a read-write "project" store (dataset quirks, decisions, prior mistakes), kept as many small files under the 100 kB limit. Because the agents fetch untrusted web content, the standards store must be read-only. Put repeatable procedures (CSV profiling recipe, post template, QC rubric) in `.claude/skills/<name>/SKILL.md` in the repo so they are versioned with the code. Between projects, run a dream over the project store to consolidate it. Start a fresh project session before day 30, re-mounting repo and stores.

**Large datasets.** Hundreds of MB per CSV is fine for the 10 GB disk but risky for 8 GB RAM if loaded naively. Have the data specialist download directly from the public source with `curl` (unrestricted networking, or `limited` with the portal hosts allowlisted), convert to Parquet or load into the preinstalled PostgreSQL/SQLite/DuckDB, and record the source URL, checksum and schema in the project memory store. Pre-install `pyarrow`, `duckdb`, `polars`, `statsmodels` via `packages.pip` so every session starts warm. Keep raw data out of git; commit only the fetch script and derived summaries. The 100k-character tool-output spill means the analyst can run big scripts without flooding context, but instruct it to write results to files and print summaries. If datasets outgrow the sandbox, self-hosting is the escape hatch, accepting the loss of repo and file mounts.

**Human in the loop.** Use `always_allow` on the toolset (the analyst must run bash freely), `always_ask` on the GitHub MCP's write tools, and treat every `session.status_idle` with `requires_action` on the primary thread as a review point; `ant beta:sessions connect` lets a person answer interactively. Structure the project as a chain of outcomes: brief → data audit → analysis → draft → reviewed draft, each a `user.define_outcome` with an explicit, gradeable rubric (`max_iterations` around 5). The grader cannot browse, so the QC reviewer agent does source verification and the outcome rubric checks structure and completeness. Subscribe to `session.status_idled`, `session.budget_reached` and `session.outcome_evaluation_ended` webhooks to notify the human, and read the Console session viewer for audits. Only trusted people should post `user.message`, since under `auto` those messages count as intent.

**Cost controls.** Attach a hard `budget` at session creation (for example `"amount": "5000"` for $50 per phase) and raise it deliberately at each human checkpoint; the platform pauses rather than overspends, and one shared cap covers all threads. Remember running time is billed at $0.08/hour and web searches at $10 per 1,000, so archive idle threads, keep the session idle between phases, and restrict `web_search` domains. Watch `session.usage` before each idle and per-thread `list_cost` to see which specialist is expensive; run the writer/editor on `claude-sonnet-5` if they dominate. Skills and MCP servers cost context and sandbox start time, so attach only what each role needs. Pin agent versions on sessions so a cost regression is traceable to a definition change, and use scheduled deployments only for genuinely recurring jobs (nightly data refresh, weekly memory consolidation), each with its own per-run cap.
