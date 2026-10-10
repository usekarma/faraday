# EXP-003 — What happens when trusted identity context is absent?

**Status:** PROPOSED

## Question and source

Q-002 and WP-001. Read-only inspection of the local `iot-digital-twin` repository found that `validate_telemetry` checks identity only when `authenticated_device_id` is supplied, and checks sequence history only when `last_sequence` is supplied. Its documentation calls these caller-provided inputs. Can the domain function accept the same payload with and without those contexts?

## Expected outcomes before execution

Use a fixed valid synthetic payload and a fixed validation time. Directly invoke the existing domain function in isolation:

| Case | Identity context | Sequence history | Expected |
| --- | --- | --- | --- |
| Matching context | Matching device | 41 | Accept sequence 42 |
| Mismatched context | Different device | 41 | Reject |
| Absent identity | None | 41 | Accept under current domain API |
| Known replay | Matching device | 42 | Reject |
| Absent history | Matching device | None | Accept sequence 42 |

These expectations describe the inspected API, not a deployment acceptance policy. Acceptance without context would establish that this function alone is insufficient to enforce mandatory authenticated ingestion or durable replay prevention. It would not prove that a deployed ingestion adapter omits context, that the API is defective, or that an attacker can bypass AWS authentication.

## Competing explanation and controls

The domain validator may intentionally allow isolated validation while a trusted adapter guarantees the context. Inspecting or executing the domain function cannot falsify that possibility. Matching identity and known replay rejection are controls for the optional checks. All measurements are synthetic local inputs against real repository code.

## Apparatus, stopping criteria, and provenance

Run `python3 scripts/identity_context_probe.py "$IOT_DIGITAL_TWIN_REPO"`. Only the standalone telemetry module is loaded; no adapters, cloud SDKs, gates, credentials, or network calls. Disable bytecode writes. Execute all five cases once and record unexpected results without changing expectations. Report target revision, dirty paths, exact source hashes, executable/spec hashes, inputs, outputs, and expected-outcome agreement. Preserve the raw report separately from interpretation.

## Portability clarification

`IOT_DIGITAL_TWIN_REPO` is an operator-supplied checkout location, not a committed machine path. The first historical run retains its original source/spec hashes; its explicit portability_revision changes only location metadata. No run was repeated.
