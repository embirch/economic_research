"""Sync current standards/status only; does not start sessions or rewrite journal history."""
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone
import anthropic

ROOT = Path(__file__).resolve().parents[1]


def main():
    client = anthropic.Anthropic(timeout=30, max_retries=0)
    stores = json.loads((ROOT / "team/memory-stores.json").read_text())
    targets = [("standards", "/" + name, name) for name in
               ("criteria.md", "file-ownership.md", "register.md", "terminology.md")]
    targets += [("research-journal", "/status/programme.md", "programme-status.md"),
                ("research-journal", "/decisions/2026-09-30-current-programme.md", "programme-status.md")]
    existing = {label: {m.path: m for m in client.beta.memory_stores.memories.list(sid)
                        if getattr(m, "type", "memory") == "memory"}
                for label, sid in stores.items()}
    receipt = {"updated_at": datetime.now(timezone.utc).isoformat(), "memories": []}
    for label, path, filename in targets:
        sid = stores[label]
        content = (ROOT / "team/memory-current" / filename).read_text()
        prior = existing[label].get(path)
        if prior:
            current = client.beta.memory_stores.memories.retrieve(prior.id, memory_store_id=sid)
            if current.content == content:
                result = current
            else:
                result = client.beta.memory_stores.memories.update(
                    prior.id, memory_store_id=sid, content=content,
                    precondition={"type": "content_sha256", "content_sha256": current.content_sha256})
        else:
            result = client.beta.memory_stores.memories.create(sid, path=path, content=content)
        verified = client.beta.memory_stores.memories.retrieve(result.id, memory_store_id=sid)
        if verified.content != content:
            raise RuntimeError("Memory read-back mismatch: " + path)
        receipt["memories"].append({"store": label, "path": path, "memory_id": result.id,
                                    "source": "team/memory-current/" + filename,
                                    "sha256": hashlib.sha256(content.encode()).hexdigest(),
                                    "read_back_verified": True})
        print("Verified", label, path)
    output = ROOT / "team/deployment/memory-sync.json"
    output.parent.mkdir(exist_ok=True)
    output.write_text(json.dumps(receipt, indent=2) + "\n")


if __name__ == "__main__":
    main()
