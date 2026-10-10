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

Split evenly into 12 disclosed design cases and 12 held-out cases, stratified across groups. Hold-out creation/review must be independent of comparator authoring; a later human-approved workflow may use distinct reviewers. Disclose the design subset and its labels only after the corpus/oracle freeze. Keep held-out inputs, labels, rationales, and variant details hidden from comparator authors until all comparator implementations and exception lists are frozen. Do not tune after seeing hold-out results; revisions require a new run with new held-out variants and retained failure history.

## Required freeze and blinding evidence

Before future implementation or evaluation, define an append-only run/version record with six independently calculated SHA-256 commitments. Hash each artifact's exact retained bytes, or a deterministic file manifest containing repository-relative paths and per-file hashes for a multi-file artifact. Specify the byte encoding/serialization and file ordering before hashing. A single aggregate hash cannot replace these separate commitments.

| Frozen artifact | Required commitment |
| --- | --- |
| Full corpus definition | Case IDs, input definitions, decision contracts, source references, and split membership |
| Oracle labels and rationales | Each label, rationale, supporting source, disagreement record, and UNKNOWN disposition |
| Disclosed design subset | Exact 12 design cases and their case-ID membership, distinct from the full corpus |
| Held-out subset | Exact 12 held-out cases and their case-ID membership; protected from comparator authors until reveal |
| Comparator implementations | Separate hashes/manifests for strict, broad, and scoped implementations, including executable/configuration dependencies used by evaluation |
| Scoped exception set | Independently hashed exception rules, applicability scope, direction, and supporting rationale; even if embedded in comparator code, retain a separately hashed representation and verify it agrees with the evaluated code |

Freeze the corpus definition, oracle labels/rationales, and both subsets before comparator authoring wherever practical, and always before held-out evaluation. The independent custodian records each artifact's logical ID, version, hash, freeze time/order, author/reviewer role, access boundary, and subsequent disclosure event. Disclose only the design material to comparator authors. Then freeze comparator implementations and the scoped exception set before revealing held-out inputs or labels. Preserve an independent review/acknowledgment of this ordering; timestamps or hashes alone do not prove that authors lacked prior access.

If pre-authoring freeze is impractical, record the reason and any prior author exposure before evaluation, require human review of the deviation, and label the run exploratory unless fresh independent hold-out material restores the declared blinding procedure. No exposure or freeze-order exception may be silently treated as confirmatory evidence.

At reveal/evaluation, verify all six commitments against the retained artifacts and record the exact versions used, reveal order, outputs, and any mismatch. Missing freeze artifacts, commitment mismatches, or undocumented held-out exposure prevent confirmatory interpretation; do not regenerate an artifact merely to match a desired hash. Hashes prove which bytes were committed to, not the correctness of oracle labels, independence of reviewers, or truth of source claims. Label disagreements become UNKNOWN, with the disagreement preserved, rather than forced consensus.

Comparator or exception tuning after held-out reveal invalidates that run for confirmatory interpretation. Retain it with that limitation and its results. Any revision to corpus, labels, split, comparator, or exceptions requires a new retained run/version with new commitments and an explicit link to the prior record. Reusing revealed hold-out cases is exploratory; a new confirmatory run needs fresh independently prepared held-out material. Never rewrite the prior record, its hashes, labels, or negative results.

These are requirements for a future human-approved workflow. No corpus, oracle, comparator, exception set, or execution is created by this specification update.

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
