#!/usr/bin/env python3
"""Synthetic, offline evidence-contract demonstration. No execution authority."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def contract_violations(e):
    checks = {
        "missing_or_failed_telemetry": e["success"] is True,
        "identity_mismatch": e["device"] == "relay-7",
        "intent_revision_mismatch": e["intent_revision"] == 3,
        "untrusted_producer": e["producer"] == "trusted-collector",
        "authorization_missing_or_revoked": e["authorized"] is True,
        "evidence_precedes_authorization": e["observed_at"] >= e["authorized_at"],
        "stale_or_future_evidence": 0 <= e["decision_at"] - e["observed_at"] <= 30,
        "contradictory_or_unknown_observation": e["contradiction"] is False,
    }
    return [reason for reason, satisfied in checks.items() if not satisfied]


def run():
    intact = dict(success=True, device="relay-7", intent_revision=3,
                  producer="trusted-collector", authorized=True,
                  authorized_at=90, observed_at=100, decision_at=110,
                  contradiction=False)
    cases = [
        ("intact", {}, True),
        ("missing_telemetry", {"success": None}, False),
        ("failed_telemetry", {"success": False}, False),
        ("wrong_device", {"device": "relay-8"}, False),
        ("old_intent", {"intent_revision": 2}, False),
        ("stale", {"decision_at": 131}, False),
        ("untrusted_collector", {"producer": "self-report"}, False),
        ("revoked_authorization", {"authorized": False}, False),
        ("before_authorization", {"authorized_at": 101}, False),
        ("contradiction", {"contradiction": True}, False),
        ("unknown_authorization", {"authorized": None}, False),
        ("freshness_boundary", {"decision_at": 130}, True),
    ]
    results = []
    for name, change, expected in cases:
        evidence = intact | change
        violations = contract_violations(evidence)
        results.append(dict(case=name, input=evidence, expected_allow=expected,
                            success_only_allow=evidence["success"] is True,
                            contract_allow=not violations, violations=violations))
    summary = {}
    for rule in ("success_only", "contract"):
        key = rule + "_allow"
        summary[rule] = dict(
            false_continuations=sum(r[key] and not r["expected_allow"] for r in results),
            false_denials=sum(not r[key] and r["expected_allow"] for r in results))
    paths = ["scripts/evidence_traps.py", "experiments/EXP-002-evidence-traps/spec.md"]
    return dict(experiment="EXP-002", evidence_kind="synthetic",
                source_sha256={p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
                               for p in paths},
                cases=results, summary=summary,
                limitation="Fixture conformance only; no real ecosystem implementation tested.")


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
