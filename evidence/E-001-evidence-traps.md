# E-001 — Synthetic evidence traps, first run

**Status:** RECORDED

## Source and provenance

Local execution of `python3 scripts/evidence_traps.py` on 2026-10-10. All inputs are fictional fixtures. Raw output is [EXP-002-run-001.json](EXP-002-run-001.json), which records SHA-256 hashes of the executable and the pre-execution specification. No target repository, device, production service, or existing Karma/Adage/Fabric implementation was tested.

EXP-002 remains PROPOSED as an ecosystem experiment; this record captures its executed synthetic demonstration only. WP-001 remains unrouted.

## Observed result

Twelve cases ran. The success-only rule had eight false continuations and zero false denials against the declared expectations. The explicit contract rule had zero false continuations and zero false denials. Per-case inputs, outputs, and violations are preserved in the raw report.

## Interpretation and counterexample

Successful telemetry alone was insufficient for this declared continuation contract. In the revoked-authorization case, the action was reported successful but continuation was forbidden. This illustrates the distinction between observing an outcome and having permission to continue.

The explicit rule is an ordinary checklist. Its success does not show that separate Adage, Fabric, and Karma components are necessary or better. The suite was selected to expose the baseline's omissions, so eight failures cannot be interpreted as a deployment failure rate.

## Limitations and remaining unknowns

The checker trusts fixture fields. A forged trusted-collector label or invented authorization could satisfy it. Timestamp comparisons do not verify clock integrity. The fixture suite omits many combined failures and malformed inputs. It establishes neither evidence authenticity nor rule sufficiency, agency preservation, alignment, or production safety. No existing hypothesis is promoted.

## Next discriminating step and human decision

Choose a real workflow and its repository for WP-001. Establish how identity, authorization, intent revision, and observation provenance are actually bound before proposing a real replay. Compare any proposed ecosystem integration with a simple checklist baseline.
