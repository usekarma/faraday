# Q-002 — Can evidence justify continuation across the ecosystem?

**Status:** OPEN

## Source and related records

The human requested that Faraday drive ideas about Karma, Adage, Fabric, and related systems. PROGRAM_BRIEF.md and programs/karma-adage-ecosystem/README.md propose an intent → action → evidence → correction loop. This question operationalizes that proposal; it does not report an observed capability.

Related: C-001 (upstream correction), C-002 (semantic versus representational difference), C-004 (relational alignment), and O-001 (a reported verification discrepancy). O-001's narrative is not independently verified evidence for this question.

## Question and operational terms

Can one bounded workflow connect an explicit human intent and authorized action to a provenance-preserving observation, then use that observation to justify continuation, denial, or correction?

- **Intent:** a versioned statement of the desired outcome and constraints.
- **Action:** an identified operation linked to that intent and its authorization.
- **Evidence:** an artifact with producer, collection method, identity binding, time or ordering, and integrity limitations stated.
- **Continuation:** a proposed next action assessed against a named rule and the available evidence. Assessment is distinct from permission to execute.
- **Correction:** a traceable proposal to revise action or specification while preserving the original discrepancy.

## Design decision

Determine what evidence contract Fabric needs to expose, what constraints Adage needs to specify, and what Karma must check before recommending continuation. These are proposed responsibilities, not verified interfaces.

## Competing explanations and skeptical pass

1. Explicit boundaries allow missing or contradictory evidence to stop continuation and produce a useful correction.
2. An ordinary workflow log and human checklist provide the same benefit with less machinery.
3. The apparent assurance depends on trusting self-reported identity or an unverified evidence producer.
4. The happy path works, but replayed, stale, missing, or contradictory evidence defeats the intended boundary.

## Smallest proposed test

First inventory one existing workflow through WP-001. If suitable artifacts exist, propose an offline replay with an intact case and controlled missing, contradictory, stale, and identity-mismatched variants. Define expected decisions and freshness/identity rules before building the replay; synthetic variants must be labeled and kept separate from original evidence.

The architecture claim is weakened if any invalid variant permits continuation under the declared rules, if the evidence cannot establish the necessary identity/ordering, or if a simpler checklist performs equivalently. An offline replay cannot establish production safety, physical identity, or general alignment.

## Expected evidence and failure modes

Return artifact references and versions, provenance limitations, declared decision rules, case inputs, observed decisions, and a comparison with the simpler baseline. Missing source artifacts are a finding, not permission to reconstruct successful results. Do not change claim maturity merely because a trace diagram can be drawn.

## Next human decision

A first synthetic demonstration is specified in EXP-002 and recorded in E-001. It illustrates evidence-contract omissions without establishing any actual ecosystem capability; this question remains OPEN.

Choose the first workflow and target repository for the read-only inventory. The IoT digital twin is the existing program's candidate, pending confirmation of its location and available artifacts.

## Revision — 2026-10-10

The continued investigation selected local `iot-digital-twin` and completed WP-001's inventory (E-002). EXP-003 reproduced optional-context acceptance in its domain validator. The next decision is whether to implement WP-002's offline ingestion-boundary tests. The full continuation question remains OPEN; neither synthetic experiment establishes live evidence authenticity.

## Director-cycle clarification — RDC-001, 2026-10-10

The earlier WP-002 next-step suggestion was superseded by the first-live-program direction, not accepted as authorization. E-003 distinguishes the separate Lambda implementation from the prototype domain API. E-004 rechecks historical source identity without running runtime tests or certifying live context. [RDC-001](../programs/karma-adage-ecosystem/cycles/RDC-001.md) recommends Q-004's independent-oracle qualification before the still-proposed EXP-004. This is a decision proposal; Q-002 remains OPEN and new downstream packages remain behind STOP_FOR_HUMAN.
