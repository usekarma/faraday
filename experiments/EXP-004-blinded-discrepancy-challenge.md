# EXP-004 — Blinded challenge for decision-relevant discrepancies

**Status:** PROPOSED

## Question and hypothesis

H-002, C-002, Q-002: can explicit scoped equivalence accept harmless representation changes while retaining sensitivity to consequential drift and uncertainty? C-001/H-003 may be explored through diagnosis outputs, but are not tested by classification accuracy alone.

## Competing methods

1. Strict equality: any changed known representation stops verification.
2. Broad normalization: generic null/empty and formatting equivalence, specified and frozen before evaluation; a deliberately permissive baseline, never used operationally.
3. Scoped equivalence: documented directional exceptions keyed to the relevant resource, field, and applicability evidence; every other mismatch remains strict.

All methods receive the same input observations and metadata. Unknown required provenance yields STOP in every method. Count ACCEPT, REJECT, and STOP separately; STOP is not successful acceptance of an equivalence.

## Corpus and independent oracle

Prepare 24 synthetic offline cases in four groups of six: confirmed representational equivalence, decision-relevant drift, uncertain semantics/provenance, and compound benign-plus-material differences. No private state, live credentials, or full plans enter fixtures.

Seed with the exact publisher `relay_state` null→empty incident. Include controls for nonempty relay targets, inverse conversion, missing versus explicit null, a different resource, different provider applicability, policy/assignment changes, rule-name validity, artifact VersionId/digest changes, and principal mismatches. An object-version difference is not automatically operational drift: distinguish an exact reviewed-version contract from a bytes-only contract, and label insufficient retrieval evidence UNKNOWN. A name correction is a desired-state change, not a generic representational equivalence.

Before coding or running methods, freeze each case's decision contract, independent label (EQUIVALENT, MATERIAL, UNKNOWN), supporting specification/source, and rationale. Reviewer must be able to disagree with a label. Unresolved disagreements become UNKNOWN; do not force agreement or use the comparator as oracle. Exact incident facts support only their documented scope. Synthetic variants do not inherit observed operational equivalence automatically.

Split evenly into 12 disclosed design cases and 12 held-out cases, stratified across groups. Hold-out creation/review must be independent of comparator authoring; a later human-approved workflow may use distinct reviewers. Hide labels and variant details until all comparator implementations and exception lists are hashed/frozen. Do not tune after seeing hold-out results; revisions require a new run with new held-out variants and retained failure history.

## Measurements and predictions

Record per-case raw inputs, declared contract, actual comparator decision, oracle label, rationale, preserved discrepancy, exception scope, and source hashes. Measure false acceptance of MATERIAL, false rejection/stopping on confirmed EQUIVALENT, acceptance of UNKNOWN, and correct STOP on UNKNOWN. Report design and held-out results separately. Do not call the fraction a deployment risk estimate.

H-002 predicts zero MATERIAL or UNKNOWN acceptances, acceptance of every scoped confirmed EQUIVALENT case, and fewer false equivalence alarms than strict equality on held-out cases. Broad normalization is expected to accept at least one material/compound trap; if it is equally safe and useful, report that simpler result rather than asserting scoped superiority.

## Falsification criterion and stopping rule

Any held-out material/compound drift accepted, unknown case verified, or raw discrepancy erased falsifies H-002's safety/conformance claim on the declared corpus. Rejecting/stopping on any confirmed equivalence or no false-alarm improvement over strict equality falsifies its usefulness claim. If labels cannot be justified independently, report the experiment inconclusive. Execute the frozen corpus once; retain all outputs and errors. Do not change rules to get green results.

## Interpretation limits

Passing supports bounded comparator behavior, not general semantic understanding, correct cloud state, physical identity, care, alignment, or live safety. If broad normalization performs equally, prefer the simpler explanation within this scope. Replication requires independent cases or a meaningfully distinct resource/provider domain. H-003 needs a separate root-cause/intervention evaluation; H-001 needs agency outcomes at matched safety and resources.

## Conditional apparatus and human boundary

Faraday holds the specification, evaluation, and interpretation. If approved, aws-iac supplies verifier behavior; aws-config supplies schema/desired-state cases; aws-lambda/iot-digital-twin may supply runtime contract cases. No infrastructure is required for this offline experiment. No downstream changes or cross-repository package is created in this task.

**STOP_FOR_HUMAN: Approve, revise, or reject the experiment scope, oracle procedure, and acceptance criteria before any cross-repository work package is created.** This approval would concern preparation of scoped packages, not cloud mutation, deployment, IAM changes, or device operations.
