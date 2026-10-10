#!/usr/bin/env python3
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "records.json"
ID_RE = re.compile(r"^(?:C|H|O|E|CE|D|Q|WP)-\d{3}$|^EXP-\d{3}$")
ALLOWED_TYPES = {"concept","hypothesis","observation","experiment","evidence","counterexample","decision","question","work-package"}
ALLOWED_STATUS = {"SPECULATIVE","FORMALIZED","TESTABLE","UNDER_TEST","SUPPORTED","REPLICATED","WEAKENED","REFORMULATED","FALSIFIED","OBSERVED","PROPOSED","RECORDED","OPEN","CLOSED"}


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def main() -> None:
    data = json.loads(REGISTRY.read_text())
    if data.get("schema_version") != 1:
        fail("registry schema_version must be 1")
    records = data.get("records")
    if not isinstance(records, list):
        fail("records must be a list")
    seen = set()
    for record in records:
        rid = record.get("id", "")
        if not ID_RE.match(rid):
            fail(f"invalid record id: {rid}")
        if rid in seen:
            fail(f"duplicate record id: {rid}")
        seen.add(rid)
        if record.get("type") not in ALLOWED_TYPES:
            fail(f"invalid type for {rid}: {record.get('type')}")
        if record.get("status") not in ALLOWED_STATUS:
            fail(f"invalid status for {rid}: {record.get('status')}")
        path = ROOT / record.get("path", "")
        if not path.is_file():
            fail(f"missing file for {rid}: {path.relative_to(ROOT)}")
        text = path.read_text()
        if rid not in text.splitlines()[0]:
            fail(f"{rid} must appear in first line of {path.relative_to(ROOT)}")
        if f"**Status:** {record['status']}" not in text:
            fail(f"registry/file status mismatch for {rid}")
    print(f"OK: validated {len(records)} Faraday records")

if __name__ == "__main__":
    main()
