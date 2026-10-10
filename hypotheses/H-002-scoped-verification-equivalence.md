# H-002 — Scoped equivalence distinguishes normalization from consequential drift

**Status:** TESTABLE

## Source and operational claim

Motivated by O-001, C-002, and E-003. On EXP-004's frozen labeled corpus, a resource/attribute/provider-scoped equivalence comparator will accept all confirmed representational variants that strict equality rejects, while rejecting all labeled decision-relevant drift and stopping on unknown semantics.

The decision is whether the observed state satisfies a named reviewed specification sufficiently for a verifier to recommend continuation. A recommendation is not execution authorization. Scope must include resource, attribute, conversion direction, and the provider version or explicit applicability evidence. The label oracle is defined independently of comparator output.

## Competing hypotheses

Strict equality's stops are necessary because normalization evidence is too weak; broad normalization is equally safe and simpler on this corpus; scoped equivalence only memorizes a single incident; or the oracle cannot determine operational meaning without additional live evidence.

## Falsification and limits

One held-out meaningful drift accepted, one unknown case reported verified, or any failure to preserve the raw discrepancy falsifies the safety/conformance claim on this corpus. Failure to reduce false alarms on confirmed equivalences falsifies its usefulness claim. Passing supports only the frozen domain; wider reliability requires independent cases and future evidence.

## Experiment and maturity

EXP-004 is PROPOSED, not run. E-003 supplies a motivating case, not independent validation of H-002. No maturity promotion is requested.
