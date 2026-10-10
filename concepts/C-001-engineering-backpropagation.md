# C-001 — Engineering backpropagation

**Status:** FORMALIZED

## Claim

When downstream verification reveals a discrepancy, correction should propagate backward to the earliest decision that needs revision rather than automatically patching the latest implementation layer.

## Candidate chain

```text
observation → verifier → implementation → architecture → specification → assumption
```

## Non-claim

This is an engineering-feedback analogy, not numerical gradient descent and not automatic model training.

## Falsification / weakening

The concept is weakened if backward tracing adds complexity without improving diagnosis, correction quality, recurrence prevention, or evidence quality compared with local remediation.

## Evidence links

- O-001
