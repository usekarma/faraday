# C-002 — Meaningful difference

**Status:** FORMALIZED

## Idea

A detected representational difference is not necessarily a decision-relevant difference. Verification should preserve discrepancies, then determine whether they carry information about the underlying system or only about representation/normalization.

## Example

O-001 records a Terraform plan/state mismatch where `relay_state: null` became `relay_state: ""` while the intended AWS resource semantics remained unchanged.

## Open problem

Define when two observations should be considered semantically equivalent without making verifiers permissive enough to hide real drift.
