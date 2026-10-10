# EXP-001 — Care versus control toy model

**Status:** PROPOSED

## Question

Can a simple environment distinguish a safety-preserving policy that intervenes selectively from one that achieves safety by broadly constraining the dependent agent?

## Competing policies

- `care`: intervene strongly only when modeled risk exceeds a threshold; otherwise preserve choices.
- `control`: constrain behavior toward a narrow safe region regardless of immediate risk.

## Measurements

- safety violations;
- intervention frequency;
- reachable viable-state count over a fixed horizon;
- conditional action entropy by risk band;
- mutual information between risk state and intervention;
- sensitivity analysis over thresholds and environment noise.

## Success criterion

The experiment is informative only if it can produce outcomes that would weaken H-001. A simulation designed so the care policy wins by construction is invalid.

## Before implementation

Skeptic must review the environment definition for baked-in preference toward either policy.
