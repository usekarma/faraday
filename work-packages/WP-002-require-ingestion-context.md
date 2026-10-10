# WP-002 — Prove ingestion rejects missing trust context before writes

**Status:** PROPOSED

**Target repository:** `iot-digital-twin` (repository identity; checkout location is supplied by its custodian)
**Source question/hypothesis:** Q-002; findings E-002 and EXP-003.
**Experiment:** Proposed offline adapter-boundary tests, distinct from direct domain validation.

## Objective and competing explanation

Demonstrate that an ingestion boundary can require trusted identity and authoritative sequence history without making the domain validator responsible for authentication. Preserve the possibility that the optional domain API is intentional. Compare with an ordinary explicit checklist; do not claim architectural superiority from the result.

## Required behavior and evidence

Before any state write, reject missing/empty trusted identity, identity mismatch, unavailable sequence history, stale messages, and known replay. A verified first-seen device may have no previous sequence, but that must be distinguished from a failed or unavailable lookup. Accept a valid authenticated first message and a later strictly newer message. Derive identity from a trusted injected context, never a payload field merely named `trusted_principal`.

Use an injected in-memory store and recording writer. Tests must observe zero writes for rejected inputs and exactly one intended write for accepted inputs. Model compare-and-swap behavior and demonstrate that two competing updates cannot regress stored sequence. Preserve test inputs and actual outcomes with source revision and hashes; label all evidence synthetic.

## Acceptance and falsification criteria

The offline boundary claim fails if a rejected case writes state, payload data can create trusted context, history-lookup failure is treated as first use, or a replay/concurrent update regresses state. Passing does not establish live AWS identity binding, durable-store behavior, or TwinMaker latency. Those need separate evidence.

## Allowed and prohibited actions

Pending human scope decision: prepare local implementation and behavioral tests under the target AGENTS.md, run its required checks, and return evidence. Do not change the optional domain API simply to make the probe reject all missing-context cases. Do not deploy, use credentials, invoke devices/cloud services, relax permissions, or claim live assurance.

## Human approval boundaries and return contract

This is prepared in Faraday and has not been routed or implemented. A human must select this target implementation scope before target edits; applicable filesystem permissions and target authority also govern execution. Return exact changes, checks, case results, provenance limitations, unresolved cloud identity assumptions, and the next discriminating experiment.
