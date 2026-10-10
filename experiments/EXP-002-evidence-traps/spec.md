# EXP-002 — Evidence traps

**Status:** PROPOSED

## Question

Related: Q-002. Can an offline continuation rule distinguish successful telemetry from evidence that actually satisfies an explicit intent and authorization contract?

## Hypotheses distinguished

This is a synthetic demonstration, not a test of existing Karma, Adage, or Fabric implementations. Compare a success-only rule with a rule that also checks identity, intent revision, ordering, provenance, authorization, and contradiction. The competing explanation is that any benefit comes entirely from an ordinary explicit checklist; the experiment cannot distinguish that explanation from architectural benefit.

## Apparatus and contract

Run `python3 scripts/evidence_traps.py`. Python standard library only; no network, credentials, devices, or other repositories.

The fictional intent is: allow device `relay-7` to continue at intent revision 3, with a valid authorization and an observed success from the trusted collector. Evidence must occur after authorization, be no more than 30 seconds old at decision time, and contain no contradictory observation. Unknown required evidence must deny continuation in this toy contract.

Trust is an input assumption, not something a producer label establishes. Authorization booleans, device identities, timestamps, and collector labels are simulated; no cryptographic verification is performed.

## Controls and expected outcomes, defined before execution

- Intact evidence: allow.
- Missing telemetry, failed telemetry, wrong device, old intent revision, stale evidence, untrusted collector, revoked authorization, evidence before authorization, contradictory telemetry, or unknown authorization: deny.
- Freshness boundary at exactly 30 seconds: allow; 31 seconds: deny.

Each case changes one dimension of the intact case. Compare both rules against these declared expectations. This suite deliberately targets omissions in the success-only rule; its failure fraction is not an estimate of real-world risk.

## Measurements and interpretation

Record every input, expected decision, actual decisions, rule violations, false continuations, and false denials. A contract-rule mismatch falsifies its conformance on this suite. Perfect conformance establishes only fixture-level consistency with these chosen rules. It cannot establish that the rules are sufficient, that evidence is truthful, or that the ecosystem is safe.

## Stopping criteria and evidence

Run every declared case once; preserve failures rather than changing expectations after seeing output. Return a JSON report with SHA-256 hashes of this specification and the executable. A later change requires a new report, preserving the original. Raw report: `evidence/EXP-002-run-001.json`; interpretation: E-001.
