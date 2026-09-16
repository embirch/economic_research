"""Drive one managed-agents session for the economic_research team.

Usage (from the repository root, with ANTHROPIC_API_KEY and GITHUB_TOKEN in the environment):
  python team/run_session.py --title "Stage 1 discovery" --budget-usd 40 --message "Begin Stage 1. Build the corpus, ..."
  python team/run_session.py --resume sess_... --message "GATE 1a: approved. Proceed to briefs."

What it does: creates (or resumes) a session with the director agent, mounts the GitHub repository and the two memory
stores, sets a hard budget, sends the kick-off message, then streams every event: agent text, tool use per thread,
thread lifecycle, usage. When the session goes idle it prints the reason and waits for you to type the next message.
Commands at the prompt:  <text> = send as a user message;  budget <usd> = raise the cap;  quit = leave the session
idle (you can resume later with --resume).  The GitHub token is read from GITHUB_TOKEN and never printed.
"""
import argparse, json, os, sys, time
import anthropic

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCK = json.load(open(os.path.join(ROOT, "claude-lock.json")))["resources"]
STORES = json.load(open(os.path.join(ROOT, "team", "memory-stores.json")))
DIRECTOR = LOCK["./team/agents/director.md"]["id"]
ENVIRONMENT = LOCK["./team/environment.yaml"]["id"]
REPO_URL = "https://github.com/embirch/economic_research"
MOUNT = "/workspace/economic_research"

def cents(usd): return str(int(round(usd * 100)))

def resources():
    tok = os.environ.get("GITHUB_TOKEN")
    if not tok: sys.exit("GITHUB_TOKEN is not set in the environment")
    return [
        {"type": "github_repository", "url": REPO_URL, "authorization_token": tok, "mount_path": MOUNT,
         "checkout": {"type": "branch", "name": "main"}},
        {"type": "memory_store", "memory_store_id": STORES["standards"], "access": "read_only",
         "instructions": "House standards: the working criteria, verified terminology, register and file ownership. Read before briefing, analysing, reviewing or writing. Do not attempt to write here."},
        {"type": "memory_store", "memory_store_id": STORES["research-journal"], "access": "read_write",
         "instructions": "The team's durable memory: lessons, data quirks, decisions, per-post status. Read at session start. Only the director writes here, at the close of a phase, as small dated files under /lessons, /data-quirks, /decisions or /status."},
    ]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", default="economic_research session")
    ap.add_argument("--budget-usd", type=float, default=40.0)
    ap.add_argument("--message", required=True, help="the first (or next) user message")
    ap.add_argument("--resume", help="existing session id")
    args = ap.parse_args()
    client = anthropic.Anthropic()

    if args.resume:
        session_id = args.resume
    else:
        s = client.beta.sessions.create(
            agent=DIRECTOR, environment_id=ENVIRONMENT, title=args.title, resources=resources(),
            budget={"type": "limit", "max_list_cost": {"amount": cents(args.budget_usd), "currency": "USD"}},
        )
        session_id = s.id
        print(f"session {session_id}  (Console: https://platform.claude.com/sessions/{session_id})")

    pending = args.message
    while True:
        with client.beta.sessions.events.stream(session_id) as stream:
            client.beta.sessions.events.send(session_id, events=[{"type": "user.message", "content": [{"type": "text", "text": pending}]}])
            print(f"\n>>> sent: {pending[:120]}\n")
            stop = None
            for ev in stream:
                t = ev.type
                if t == "agent.message":
                    for b in ev.content:
                        if getattr(b, "type", "") == "text": print(b.text, end="", flush=True)
                    print()
                elif t in ("agent.tool_use", "agent.mcp_tool_use"):
                    print(f"  [{t.split('.')[1]}] {getattr(ev, 'name', '')}")
                elif t.startswith("session.thread_"):
                    print(f"  <{t}> {getattr(ev, 'agent_name', '')} {getattr(ev, 'session_thread_id', '')}")
                elif t == "agent.thread_message_sent":
                    print(f"  -> to {getattr(ev, 'to_agent_name', '')}: {str(getattr(ev, 'content', ''))[:200]}")
                elif t == "agent.thread_message_received":
                    print(f"  <- from {getattr(ev, 'from_agent_name', '')}: {str(getattr(ev, 'content', ''))[:200]}")
                elif t == "session.usage":
                    lc = getattr(ev, "list_cost", None); print(f"  [usage] list_cost cents={lc} active_seconds={getattr(ev, 'active_seconds', None)}")
                elif t == "session.error":
                    print(f"  [error] {ev}")
                elif t == "session.status_idle":
                    stop = getattr(ev, "stop_reason", None); print(f"\n=== idle: {stop}"); break
        # idle: decide what to do
        sr = getattr(stop, "type", None) or (stop.get("type") if isinstance(stop, dict) else str(stop))
        if sr == "requires_action":
            print("The session is waiting for a tool confirmation (a push or pull request). Answer it in the Console session viewer or with `ant beta:sessions connect`, then press Enter here.")
        elif sr == "budget_reached":
            print("Budget reached. Type: budget <usd> to raise it.")
        try:
            reply = input("\nyour message (or: budget <usd> | quit) > ").strip()
        except EOFError:
            reply = "quit"
        if reply == "quit": print(f"leaving session {session_id} idle; resume with --resume {session_id}"); return
        if reply.startswith("budget "):
            usd = float(reply.split()[1]); client.beta.sessions.update(session_id, budget={"type": "limit", "max_list_cost": {"amount": cents(usd), "currency": "USD"}})
            print(f"budget now ${usd:.2f}"); pending = input("your message > ").strip() or "Continue."
        elif reply == "":
            pending = "Continue."
        else:
            pending = reply

if __name__ == "__main__":
    main()
