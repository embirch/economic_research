"""Run an authorised bounded specialist assignment; never launches on import.

Usage: python team/run_agent.py CAP_USD assignment.md ./team/agents/referee.md "Title" --branch work/task
The branch must already exist on GitHub. Configuration updates are separate from sessions.
"""
import argparse
import csv
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
import hashlib
import json
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def validate_request(budget, branch):
    try:
        amount = Decimal(str(budget))
    except InvalidOperation:
        raise ValueError("Budget must be a positive dollar amount")
    if not amount.is_finite() or amount <= 0 or amount != amount.quantize(Decimal("0.01")):
        raise ValueError("Budget must be positive, finite and specified to cents")
    if not branch or branch in {"main", "master", "HEAD"} or branch.startswith("-"):
        raise ValueError("An explicit work branch is required; main/master/HEAD are forbidden")
    if subprocess.run(["git", "check-ref-format", "--branch", branch], capture_output=True).returncode:
        raise ValueError("Invalid branch name")
    return str(int(amount * 100))


def verified_agent(agent_key):
    lock = json.loads((ROOT / "claude-lock.json").read_text())["resources"]
    if agent_key not in lock or lock[agent_key]["kind"] != "agent":
        raise ValueError("Unknown agent key")
    receipt = json.loads((ROOT / "team/deployment/agents.json").read_text())
    entry = next(x for x in receipt["agents"] if x["source"] == agent_key.removeprefix("./"))
    if not entry["read_back_verified"] or entry["sha256"] != hashlib.sha256((ROOT / agent_key).read_bytes()).hexdigest():
        raise ValueError("Agent definition has changed since deployment; deploy and verify it first")
    if str(entry["version"]) != str(lock[agent_key]["version"]):
        raise ValueError("Agent deployment receipt and lockfile differ")
    return lock[agent_key], lock["./team/environment.yaml"]["id"]


def stream_until_idle(client, session_id):
    cost = None
    with client.beta.sessions.events.stream(session_id) as events:
        for ev in events:
            if ev.type == "agent.message":
                for block in ev.content:
                    if getattr(block, "type", "") == "text":
                        print(block.text, flush=True)
            elif ev.type == "session.usage":
                usage = getattr(ev, "usage", None)
                amount = getattr(getattr(usage, "list_cost", None), "amount", None)
                if amount is not None:
                    cost = str(Decimal(str(amount)) / 100)
                    print("List cost so far: $" + cost, flush=True)
            elif ev.type == "session.error":
                print("Session error; inspect the session securely in the platform console.", flush=True)
                return cost, "error"
            elif ev.type == "session.status_idle":
                print("Session idle; no automatic follow-up or budget increase.", flush=True)
                return cost, "idle"
    status = client.beta.sessions.retrieve(session_id).status
    print("Stream ended; session status:", status, "session:", session_id, flush=True)
    return cost, str(status)


def launch(budget, message_file, agent_key, title, branch):
    import anthropic
    amount = validate_request(budget, branch)
    message = Path(message_file).read_text()
    if not message.strip():
        raise ValueError("Assignment is empty")
    agent, environment = verified_agent(agent_key)
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN is not available locally")
    stores = json.loads((ROOT / "team/memory-stores.json").read_text())
    resources = [{"type": "github_repository", "url": "https://github.com/embirch/economic_research",
                  "authorization_token": token, "mount_path": "/workspace/economic_research",
                  "checkout": {"type": "branch", "name": branch}}]
    for label, sid in stores.items():
        resources.append({"type": "memory_store", "memory_store_id": sid, "access": "read_only",
                          "instructions": "Historical context only where superseded. Read PROJECT.md and programme/DECISIONS.md in the checkout first. Do not activate old tasks."})
    policy = ("Current policy: read PROJECT.md, programme/DECISIONS.md and team/SETUP.md first. "
              "Preserve the existing first article; posts/gender1 is reference-only. Work only on branch "
              + branch + ". Never push main, merge, change settings or increase the cap. Stop when the assignment is complete.\n\n")
    client = anthropic.Anthropic()
    deployed = client.beta.agents.retrieve(agent["id"])
    if str(deployed.version) != str(agent["version"]):
        raise ValueError("Remote agent changed since the recorded deployment; reconcile before starting work")
    branch_ref = subprocess.check_output(
        ["git", "ls-remote", "--exit-code", "origin", "refs/heads/" + branch], cwd=ROOT, text=True).strip()
    if not branch_ref:
        raise ValueError("The work branch must exist on origin before launching")
    source_commit = branch_ref.split()[0]
    session = client.beta.sessions.create(agent=agent["id"], environment_id=environment, title=title,
                                          resources=resources, budget={"type": "limit", "max_list_cost": {"amount": amount, "currency": "USD"}})
    record = {"date": datetime.now(timezone.utc).isoformat(), "assignment": str(message_file),
              "agent_role": agent_key, "agent_version": agent["version"],
              "source_commit": source_commit,
              "work_branch": branch, "session_id": session.id, "approved_cap_usd": str(budget),
              "actual_cost_usd": "", "status": "created", "output_paths": ""}
    ledger = ROOT / "team/RUNS.csv"
    def record_state():
        with ledger.open("a", newline="") as f:
            csv.DictWriter(f, fieldnames=list(record), lineterminator="\n").writerow(record)
    record_state()
    print("Session:", session.id, "cap: $" + str(budget), "branch:", branch, flush=True)
    try:
        client.beta.sessions.events.send(session.id, events=[{"type": "user.message", "content": [{"type": "text", "text": policy + message}]}])
        cost, status = stream_until_idle(client, session.id)
        record.update(actual_cost_usd=cost or "", status=status)
    except Exception:
        record["status"] = "client_error_check_remote_status"
        print("Client error. The remote session may still be active; inspect", session.id, "before retrying.", flush=True)
        raise
    finally:
        record_state()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("budget_usd")
    parser.add_argument("message_file")
    parser.add_argument("agent_key")
    parser.add_argument("title")
    parser.add_argument("--branch", required=True)
    args = parser.parse_args()
    launch(args.budget_usd, args.message_file, args.agent_key, args.title, args.branch)


if __name__ == "__main__":
    main()
