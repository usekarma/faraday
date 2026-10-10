# E-002 — IoT workflow inventory and optional-context probe

**Status:** RECORDED

## Provenance

Collected locally on 2026-10-10 under WP-001 following the human's instruction to continue. Selected the existing program's candidate, `/home/ted/dev/iot-digital-twin`. Read its AGENTS.md; made no target-repository edits and performed no cloud or device operations.

Target HEAD: `0b303604e741dd642e93834842ed86c78f03e5b4`. The working tree had edits to `docs/architecture.md` and `docs/aws-sandbox-plan.md`; their contents are working proposals, not attributable solely to that commit. [Source manifest](WP-001-source-manifest.json) records hashes of the exact inspected files. [Probe output](EXP-003-run-001.json) records the executed source and harness hashes, synthetic inputs, and results. Source references below are relative to the target repository.

## Observations: boundary trace

| Boundary | Source artifact | What inspection establishes | Gap |
| --- | --- | --- | --- |
| Human intent | `PROJECT_BRIEF.md`, `docs/acceptance-criteria.md` | Explicit prototype objective, measurable live-demo criteria, and human cloud-approval requirement | No signed runtime intent/authorization binding inspected |
| Device identity and permission | `infra/sandbox/main.tf`, `docs/aws-sandbox-plan.md` | Terraform declares Thing/policy attachments and a device-scoped topic; plan requires authoritative identity | Declaration is not deployed identity or current permission evidence |
| Ingestion | `infra/sandbox/main.tf` | Topic rule uses `SELECT *`; Lambda points to `ingest_placeholder.zip` | Inspected rule does not explicitly project a trusted identity field; no implemented handler inspected |
| Validation | `src/business_app/telemetry.py` | Shape, freshness, derived state, optional identity comparison and optional sequence-history comparison exist | Caller must supply trusted identity and authoritative sequence history |
| State and visibility | `src/business_app/adapters.py`, `infra/sandbox/main.tf` | Protocols describe persistence/TwinMaker boundaries; Terraform declares a latest-state table | No concrete AWS ingestion/store/TwinMaker implementation established by these artifacts |
| Verification and correction | `docs/verification.md`, `docs/prototype-review.md` | Historical reviews explicitly distinguish local checks from missing live proof, and record required corrections | Review narratives are not independently replayed live observations; no automatic correction-to-intent chain established |
| Continuation | `PROJECT_BRIEF.md`, `docs/prototype-review.md` | Human gates are specified | No implemented evidence-linked continuation decision established |

## Executed observation: EXP-003

Five direct calls to the real standalone telemetry module, with fixed synthetic inputs and time, matched the pre-execution expectations:

- Matching identity and previous sequence 41: sequence 42 accepted.
- Mismatched supplied identity: rejected.
- Missing identity context and previous sequence 41: accepted.
- Matching identity and previous sequence 42: rejected.
- Matching identity and missing sequence history: accepted.

No target quality gates were run; no target implementation was changed. This narrow probe is not a replacement for its checks.

## Derived fact and interpretation

The observed domain function does not require identity or sequence history to accept this payload. Mandatory authenticated ingestion and durable replay prevention therefore require additional enforcement at its caller or another boundary.

This is an integration obligation, not evidence of an exploitable deployed vulnerability. The domain API may deliberately support isolated validation; a correctly implemented adapter could always supply context. A topic rule declaration and a successful domain test cannot establish that adapter behavior.

## Skeptical and verification passes

The simpler checklist explanation from Q-002 remains viable. Separate ecosystem components are not shown necessary. The source hashes bind this report to inspected bytes, but do not authenticate device observations. All execution evidence here is synthetic input against local code. The target's historical review claims and cloud design have not been independently validated. Q-002 remains OPEN; no hypothesis is promoted.

## Program consequence and next human decision

WP-001's bounded inventory is complete; the full ecosystem loop remains unverified. A follow-up proposal, WP-002, defines an offline ingestion-boundary test requiring context before any state write. Decide whether to authorize that implementation in `iot-digital-twin` under its own instructions. This report grants no deployment, cloud access, or target mutation authority.
