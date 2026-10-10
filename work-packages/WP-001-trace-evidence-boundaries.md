# WP-001 — Trace one workflow's evidence and authority boundaries

**Status:** PROPOSED

**Target repository:** Unresolved; candidate: `iot-digital-twin`, with references to relevant Adage, Fabric, and Karma artifacts.
**Source question/hypothesis:** Q-002; related C-001 and C-002.
**Experiment:** No execution experiment authorized by this package; prepare a bounded replay proposal after inventory.

## Objective

Inspect one existing workflow to establish which links in intent → action → evidence → correction are implemented, which are proposed, and which are missing. Read the target repository's AGENTS.md before inspection and respect its boundaries.

## Required evidence

- Repository revision and exact paths for intent, constraints, authorization, action, observation, verification, and correction artifacts where present.
- Producer and collection method for each observation, including identity and integrity limitations.
- One available discrepancy or failed verification, if present; explicitly report absence.
- A trace mapping each boundary to source artifacts, with missing links labeled unknown.

## Acceptance / falsification criteria

The inventory is complete when each boundary has a source reference or an explicit gap and a concrete next test. A diagram alone does not support Q-002. Missing identity binding, decision rules, provenance, or source artifacts prevents a claim that continuation is evidence-justified.

## Allowed actions

Read local source and existing artifacts within target-repository permissions. Prepare a report and offline replay specification for return to Faraday. Redact secrets rather than copying them into records.

## Prohibited actions

No deployment, infrastructure apply, credential use, physical-device operation, production execution, policy relaxation, external mutation, or modification of target-repository files. Do not manufacture evidence or silently normalize discrepancies.

## Human approval boundaries

Routing is pending selection of the workflow and target location. Any later execution or implementation requires a separately scoped package and the target repository's applicable authorization; this proposal grants none.

## Return contract

Return source revisions and artifact paths, the boundary trace, raw findings separately from interpretation, competing explanations, unresolved gaps, and the smallest proposed replay with expected outcomes. State whether findings bear on Q-002 and what remains unverified. No claim promotion is implied by completing the inventory.

## Execution update — 2026-10-10

Following the human's instruction to continue, selected the local `iot-digital-twin` candidate and completed the read-only inventory in Faraday. E-002 contains the return report and source manifest; EXP-003 records a narrow direct-domain probe. No package was sent externally and no target files were changed. This original proposal remains preserved with status PROPOSED; the completed inventory and proposed follow-up are linked rather than rewriting its authorization text. Next proposed package: WP-002.
