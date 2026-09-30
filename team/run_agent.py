"""Run ONE specialist agent in its own managed-agents session (no director), streaming events to stdout.

Usage (from the repository root, with ANTHROPIC_API_KEY and GITHUB_TOKEN in the environment):
  python team/run_agent.py <budget_usd> <kickoff_message_file> <agent_key> "<session title>"
  e.g. python team/run_agent.py 20 /tmp/kickoff.txt ./team/agents/referee.md "gender1 · referee: draft review"

<agent_key> is the agent's path as recorded in claude-lock.json (./team/agents/referee.md, ./team/agents/referee-second-read.md,
./team/agents/editor.md, ./team/agents/analyst.md, ./team/agents/steward.md, ./team/agents/lead.md).

This is how every session after 18 September 2026 was run: a direct single-agent session is far cheaper than routing a
one-agent task through the director (editor rewrite $17, referee reviews $2-13). The session mounts the GitHub repository
and both memory stores (read-only here), sets a hard budget, sends the kick-off message, and exits when the session goes
idle. Recreated on 30 September 2026 for the handover; the original lived in a temporary scratchpad that was cleared.
"""
import json, os, sys, time
import anthropic

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCK = json.load(open(os.path.join(ROOT, "claude-lock.json")))["resources"]
STORES = json.load(open(os.path.join(ROOT, "team", "memory-stores.json")))
REPO_URL = "https://github.com/embirch/economic_research"
MOUNT = "/workspace/economic_research"


def main():
    budget = float(sys.argv[1]); msg = open(sys.argv[2]).read(); agent_key = sys.argv[3]; title = sys.argv[4]
    agent = LOCK[agent_key]["id"]; env = LOCK["./team/environment.yaml"]["id"]
    tok = os.environ.get("GITHUB_TOKEN")
    if not tok:
        sys.exit("GITHUB_TOKEN is not set in the environment")
    resources = [
        {"type": "github_repository", "url": REPO_URL, "authorization_token": tok, "mount_path": MOUNT,
         "checkout": {"type": "branch", "name": "main"}},
        {"type": "memory_store", "memory_store_id": STORES["standards"], "access": "read_only",
         "instructions": "House standards: criteria, terminology, register, file ownership. Read before writing."},
        {"type": "memory_store", "memory_store_id": STORES["research-journal"], "access": "read_only",
         "instructions": "The team's durable memory: lessons, data quirks, decisions, per-post status. Read at session start."},
    ]
    c = anthropic.Anthropic()
    s = c.beta.sessions.create(agent=agent, environment_id=env, title=title, resources=resources,
                               budget={"type": "limit", "max_list_cost": {"amount": str(int(budget * 100)), "currency": "USD"}})
    print("session", s.id, flush=True)
    c.beta.sessions.events.send(s.id, events=[{"type": "user.message", "content": [{"type": "text", "text": msg}]}])
    while True:
        stop = None
        with c.beta.sessions.events.stream(s.id) as st:
            for ev in st:
                t = ev.type
                if t == "agent.message":
                    for b in ev.content:
                        if getattr(b, "type", "") == "text":
                            print(b.text, flush=True)
                elif t in ("agent.tool_use", "agent.mcp_tool_use"):
                    print(f"  [tool] {getattr(ev, 'name', '')}", flush=True)
                elif t == "session.usage":
                    u = getattr(ev, "usage", None)
                    lc = getattr(getattr(u, "list_cost", None), "amount", None) if u else None
                    if lc:
                        print(f"  [usage] ${int(lc) / 100:.2f}", flush=True)
                elif t == "session.error":
                    print(f"  [error] {ev}", flush=True)
                elif t == "session.status_idle":
                    stop = getattr(ev, "stop_reason", None)
                    print(f"\n=== idle: {stop}", flush=True)
                    break
        if stop is not None:
            break
        if c.beta.sessions.retrieve(s.id).status != "running":
            print("[stream ended; not running]")
            break
        print("[reconnecting]", flush=True)
        time.sleep(3)


if __name__ == "__main__":
    main()
