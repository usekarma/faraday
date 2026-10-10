# H-001 — Care preserves agency at matched safety

**Status:** TESTABLE

## Hypothesis

Under matched safety outcomes, a care-oriented policy preserves a larger set of viable future states for the dependent agent than a control-oriented policy while selectively increasing predictability when risk is high.

## Candidate variables

- `S`: dependent/environment state
- `A`: caregiver/controller action
- `R`: risk or harm indicator
- `V`: viable/reachable future-state set
- `H(A|S)`: conditional action entropy
- `I(S;A)`: mutual information between observed state and intervention

## Predictions

1. When risk is low, the care policy intervenes less and preserves more viable options.
2. When risk rises, the care policy becomes more predictable in safety-relevant action.
3. A control policy can achieve similar safety by collapsing the dependent's option set more broadly.

## Falsification / weakening

The hypothesis is weakened if, under matched safety and comparable resources, control-oriented policies preserve equal or greater viable agency, or if the proposed measurements cannot reliably distinguish the policies.

## Risks

- defining `viable` embeds values;
- reachable-state count may reward unsafe or meaningless options;
- entropy metrics can be Goodharted;
- learned preferences and context may dominate any general caregiving principle.

## Proposed experiment

EXP-001

## Program assessment — 2026-10-10

E-003's identity, artifact, verifier, and IAM observations do not measure agency under matched safety/resources. Leave this claim TESTABLE without strengthening or weakening its empirical support. CE-001 challenges uncertainty and option-count proxies and policy labels; meaningful agency needs an independently specified metric and preference-sensitive baseline before testing. No care/alignment conclusion follows from a successful engineering gate.
