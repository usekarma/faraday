#!/usr/bin/env python3
"""Read-only local probe of a standalone domain module; synthetic inputs."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]


def run(target):
    source = target / "src/business_app/telemetry.py"
    source_bytes = source.read_bytes()
    spec = importlib.util.spec_from_file_location("faraday_probe_telemetry", source)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    payload = dict(device_id="core2-aws-001", timestamp="2026-10-10T12:00:00Z",
                   accel_x=0.03, accel_y=-0.02, accel_z=1.01,
                   gyro_x=0.4, gyro_y=0.1, gyro_z=-0.2,
                   operating_state="NORMAL", sequence=42)
    cases = [
        ("matching_context", "core2-aws-001", 41, True),
        ("mismatched_context", "another-device", 41, False),
        ("absent_identity", None, 41, True),
        ("known_replay", "core2-aws-001", 42, False),
        ("absent_history", "core2-aws-001", None, True),
    ]
    results = []
    for name, identity, history, expected in cases:
        try:
            result = module.validate_telemetry(
                payload, authenticated_device_id=identity, last_sequence=history,
                now=datetime(2026, 10, 10, 12, tzinfo=timezone.utc))
            accepted, output = True, result.to_asset_state()
        except (TypeError, ValueError) as exc:
            accepted, output = False, dict(error_type=type(exc).__name__, message=str(exc))
        results.append(dict(case=name, authenticated_device_id=identity,
                            last_sequence=history, expected_accept=expected,
                            observed_accept=accepted, output=output,
                            expectation_matched=accepted == expected))
    if source.read_bytes() != source_bytes:
        raise RuntimeError("Target source changed during probe; discard this run")
    def git(*args):
        return subprocess.check_output(["git", "-C", str(target), *args], text=True).strip()
    paths = ["scripts/identity_context_probe.py", "experiments/EXP-003-identity-context.md"]
    return dict(experiment="EXP-003", evidence_kind="synthetic inputs against local source",
                target=str(target), target_revision=git("rev-parse", "HEAD"),
                target_worktree_status=git("status", "--short"),
                target_source="src/business_app/telemetry.py",
                target_source_sha256=hashlib.sha256(source_bytes).hexdigest(),
                source_sha256={p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths},
                payload=payload, validation_time="2026-10-10T12:00:00Z", cases=results,
                limitation="Direct domain invocation only; no deployed ingestion path tested.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: identity_context_probe.py TARGET_REPOSITORY")
    print(json.dumps(run(Path(sys.argv[1]).resolve()), indent=2))
