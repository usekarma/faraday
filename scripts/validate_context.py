#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text())


def fail(msg):
    raise SystemExit(f"FAIL: {msg}")


def main():
    records = load("registry/records.json")["records"]
    record_ids = {r["id"] for r in records}

    ecosystem = load("registry/ecosystem.json")
    if ecosystem.get("schema_version") != 1:
        fail("ecosystem schema_version must be 1")
    systems = ecosystem.get("systems", [])
    ids = [s.get("id") for s in systems]
    if not ids or len(ids) != len(set(ids)):
        fail("ecosystem system ids must be unique and non-empty")
    repositories = [s.get("repository") for s in systems]
    if len(repositories) != len(set(repositories)):
        fail("ecosystem repositories must be unique")
    for system in systems:
        authority = system.get("authority", {})
        if system["id"] == "faraday" and authority.get("may_execute_downstream"):
            fail("Faraday may not execute downstream")
        if authority.get("may_authorize"):
            fail(f"{system['id']} may not claim final authorization")

    epistemic = load("registry/epistemic.json")
    kinds = [k["id"] for k in epistemic.get("epistemic_kinds", [])]
    required = {
        "observation",
        "measurement",
        "derived_fact",
        "interpretation",
        "hypothesis",
        "counterexample",
        "decision",
        "authorization",
    }
    if set(kinds) != required:
        fail("epistemic kinds must exactly match the required vocabulary")

    system_ids = set(ids)
    current_repos = load("current-state/repositories.json")
    for item in current_repos.get("repositories", []):
        if item.get("system") not in system_ids:
            fail(f"unknown current-state system: {item.get('system')}")
        expected_repo = next(s["repository"] for s in systems if s["id"] == item["system"])
        if item.get("repository") != expected_repo:
            fail(f"repository mismatch for {item['system']}")

    programs = load("current-state/programs.json")
    program_ids = {p["id"] for p in programs.get("programs", [])}
    for program in programs.get("programs", []):
        for field in ("active_question_ids", "active_hypothesis_ids"):
            for rid in program.get(field, []):
                if rid not in record_ids:
                    fail(f"unknown record id in {program['id']}: {rid}")
        exp = program.get("recommended_experiment_id")
        if exp and exp not in record_ids:
            fail(f"unknown experiment id in {program['id']}: {exp}")

    blockers = load("current-state/blockers.json")
    for blocker in blockers.get("blockers", []):
        if blocker.get("program") not in program_ids:
            fail(f"unknown blocker program: {blocker.get('program')}")
        if blocker.get("question_id") not in record_ids:
            fail(f"unknown blocker question id: {blocker.get('question_id')}")
        for eid in blocker.get("evidence_ids", []):
            if eid not in record_ids:
                fail(f"unknown blocker evidence id: {eid}")
        if not blocker.get("decision_if_resolved") or not blocker.get("decision_if_unresolved"):
            fail(f"blocker {blocker.get('id')} must state decision consequences")

    freshness = load("current-state/evidence-freshness.json")
    for item in freshness.get("tracked", []):
        if item.get("evidence_id") not in record_ids:
            fail(f"unknown freshness evidence id: {item.get('evidence_id')}")

    authority = load("registry/authority.json")
    if authority.get("required_authority") != "human_or_target_repository_approved_execution_path":
        fail("authority boundary changed unexpectedly")

    print(f"OK: validated ecosystem knowledge layer for {len(systems)} systems")


if __name__ == "__main__":
    main()
