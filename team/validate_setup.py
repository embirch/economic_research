"""Offline checks of setup/provenance; no API calls or empirical research certification."""
from pathlib import Path
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]


def main():
    required = ["PROJECT.md", "AGENTS.md", "CLAUDE.md", "programme/DECISIONS.md",
                "programme/FILE-MAP.md", "team/SETUP.md", "team/templates/ASSIGNMENT.md"]
    for path in required:
        assert (ROOT / path).is_file(), path
    manifest = json.loads((ROOT / "programme/gender-index/migration-manifest.json").read_text())
    for item in manifest:
        artifact = ROOT / item["destination"]
        assert hashlib.sha256(artifact.read_bytes()).hexdigest() == item["sha256"], str(artifact)
    agent_paths = list((ROOT / "team/agents").glob("*.md"))
    assert len(agent_paths) == 7, "Expected seven configured roles"
    for path in agent_paths:
        text = path.read_text()
        assert "PROJECT.md" in text and "Never push to main" in text, str(path)
        assert "posts/gender1 is reference-only" in text, str(path)
        for obsolete in ["git push origin main", "every finding says Claude",
                         "foundation of every post", "MDE beside every null"]:
            assert obsolete not in text, (str(path), obsolete)
    with (ROOT / "programme/gender-index/evidence/indicators.csv").open(newline="") as f:
        rows = list(csv.DictReader(f))
    assert len({x["indicator_id"] for x in rows}) == len(rows)
    for row in rows:
        assert None not in row, "CSV has excess fields"
        for key in ["source_url", "sample_family", "denominator", "gender_measure",
                    "verification_status", "next_check", "new_check_this_setup"]:
            assert row[key], (row["indicator_id"], key)
    for name in ["RESULTS.schema.json", "RESULTS.example.json"]:
        json.loads((ROOT / "team/templates" / name).read_text())
    for receipt_file in ["memory-sync.json", "agents.json"]:
        p = ROOT / "team/deployment" / receipt_file
        if not p.exists():
            print("Pending deployment receipt:", receipt_file)
            continue
        receipt = json.loads(p.read_text())
        for item in receipt.get("memories", receipt.get("agents", [])):
            source = ROOT / item["source"]
            assert hashlib.sha256(source.read_bytes()).hexdigest() == item["sha256"], str(source)
            assert item["read_back_verified"], str(source)
    print("PASS: setup links, imported hashes, seven-role policy, evidence fields and available deployment receipts.")


if __name__ == "__main__":
    main()
