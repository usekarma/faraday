# O-001 — Provider normalization caused a postflight false negative

**Status:** OBSERVED

## Raw observation

A reviewed Terraform plan represented `aws_ssoadmin_permission_set.artifact_publisher.relay_state` as `null`. After the exact saved plan applied successfully, Terraform state represented the same optional field as an empty string.

The strict postflight verifier detected the difference and stopped.

## Investigation

- Exact saved-plan apply: 3 added / 0 changed / 0 destroyed.
- Account assignment matched known planned attributes.
- Inline policy matched known planned attributes.
- Publisher permission set differed only on `relay_state`: planned `null`, state `""`.
- A narrow read-only recheck normalized only this documented provider representation and then verified postflight.

## Interpretation

This is one engineering case supporting C-002. It does not establish a general equivalence rule for null/empty values.

## Program lesson

Preserve the discrepancy first. Determine its meaning before changing infrastructure or weakening verification.
