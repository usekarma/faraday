# E-003 — Interpretation of the first live program's engineering history

**Status:** RECORDED

## Provenance and evidence grades

Assessment dated 2026-10-10. The human supplied ten historical observations. Faraday inspected local source, specs, review summaries, and selected fields in retained private execution receipts. No AWS operation, artifact retrieval, Terraform execution, or device operation was performed. Source inspection corroborates code and recorded history; it is not independent re-observation of remote state.

[Source manifest](live-program-source-manifest.json) pins exact working-tree files, revisions, and dirty-file status. Some relevant specs/worktrees are uncommitted; HEAD alone is insufficient provenance. Private plans, state, raw receipts, and account/identity data remain downstream. Links below refer to local paths, not published evidence accessible to every reader.

Grades used here: **reproduced local behavior**, **inspected implementation**, **retained local receipt**, and **human-reported operation**. Hashing a record establishes which bytes were inspected, not the truth of its contents. Classifications can overlap: an observation can yield a bounded finding without becoming support for a broader hypothesis.

The private historical receipt references are [successful apply result](/home/ted/dev/aws-iac/artifacts/identity-center-bootstrap/review-uhd86fs8/maintenance-reviews/artifact-publisher-hrrbk83v/apply-result.json), [original failed postflight](/home/ted/dev/aws-iac/artifacts/identity-center-bootstrap/review-uhd86fs8/maintenance-reviews/artifact-publisher-hrrbk83v/post-apply.json), and [later recheck receipt](/home/ted/dev/aws-iac/artifacts/identity-center-bootstrap/review-uhd86fs8/maintenance-reviews/artifact-publisher-hrrbk83v/postflight-rechecks/review-7yolru5o/postflight.json). They remain private local records; their existence and selected assertions do not amount to independently rerunning those operations.

## 1. Authenticated identity outranks payload device_id

**Classification:** inspected implementation; reproduced local evidence; bounded finding; unresolved end-to-end question.

**Sources:** [Lambda validation](/home/ted/dev/aws-lambda/iot-digital-twin-ingest/validation.py), [tests](/home/ted/dev/aws-lambda/iot-digital-twin-ingest/tests/test_ingest.py), and [IaC rule](/home/ted/dev/aws-iac/components/iot-digital-twin/main.tf). The runtime requires principal and topic fields and compares all three identity dimensions with configuration; IaC declares `principal()`/`topic()` injection. All 17 runtime unit tests passed in this task, including mismatched identity and missing required fields.

**Justified:** this implementation requires supplied matching context; payload identity alone does not satisfy its declared validation contract. **Not justified:** the event context is authentic, collision-proof, physically bound, or deployed; a copied valid credential may still emit false telemetry.

**Competing interpretation:** ordinary authentication/context validation explains the benefit; the fields might still be forgeable if injection/invocation provenance is wrong. **Links/action:** Q-002/Q-003, C-004; leave C-004 and H-001 unchanged. E-002/EXP-003 remain valid for the separate prototype domain module. Their absent-context finding cannot be generalized to this Lambda implementation; narrow that interpretation explicitly.

## 2. Device-authored OFFLINE is rejected

**Classification:** reproduced local evidence; finding about state authority.

**Sources:** runtime validation and `test_device_offline_and_states`; prototype telemetry source also rejects OFFLINE. **Justified:** device OFFLINE is rejected by the tested local boundary; connectivity authority is separated from device operational claims. **Not justified:** an actual server scheduler detects missing heartbeat correctly, or any live offline transition is observed.

**Competing interpretation:** simple state-machine/schema ownership suffices; losing connectivity still leaves the server uncertain, and authoritative does not mean correct. **Links/action:** C-002, Q-002; no support for care or relational alignment. Leave all existing hypothesis maturity unchanged. Investigate missing-data handling separately from uncertainty reduction.

## 3. trusted_principal remains unresolved

**Classification:** unresolved question; inspected blocked planning declaration; negative evidence against readiness.

**Sources:** [artifact-binding spec](/home/ted/dev/aws-config/artifacts/worktrees/iot-ingest-artifact-binding/specs/iot-ingest-artifact-binding.md), [blocker review summary](/home/ted/dev/aws-iac/artifacts/iot-ingestion-blockers/review-f_jc7k76/review-summary.json). Both preserve the dependency and absence of EXPECTED_PRINCIPAL.

**Justified:** these records explicitly retain unknown identity and distinguish structural validity from readiness. **Not justified:** the principal is known, deployed, or a Thing name can substitute for it. **Competing interpretation:** this may be only a useful static gate; another path could bypass it. **Links/action:** Q-003, Q-002, C-004; leave claims unchanged and refuse readiness promotion. This is a question to resolve, not a failed authentication experiment.

## 4. Artifact published at a content-addressed key and exact VersionId

**Classification:** human-reported operation recorded in an inspected binding spec; artifact-identity finding conditional on that report.

**Sources:** binding spec and blocker review summary identify the same content-addressed digest and exact version. The spec explicitly attributes retrieval verification to the human. **Justified:** the intended binding names particular bytes/version rather than an unversioned latest object, and the recorded coordinates agree. **Not justified:** Faraday independently observed publication, the object cannot be deleted/replaced in every sense, or the running Lambda uses those bytes. A content-addressed name is not itself write protection; exact-version binding and publication controls are distinct.

**Competing interpretation:** standard artifact pinning provides this property without the broader architecture. **Links/action:** Q-002, C-002; no hypothesis promotion. Split artifact identity from artifact correctness, provenance, availability, deployment, and authorization claims.

## 5. Retrieval, checksum, SHA-256, and byte equality verified publication

**Classification:** human-reported verification evidence; bounded content-integrity finding.

**Source:** binding spec explicitly reports successful exact-version retrieval and checks. Raw publication/download receipt was not independently located or replayed in this task. **Justified:** if the report is accurate, the retrieved exact-version object equaled the compared local ZIP at that time. **Not justified:** source/build provenance, benignness, correct runtime behavior, or independent replication. Checksum, SHA-256, and byte equality here are related checks on bytes, not three independent replications.

**Competing interpretation:** the local comparison artifact or trusted reporter could be wrong; identity assurance is standard supply-chain verification. **Links/action:** Q-002; leave C-004/H-001 unchanged. Keep reported content integrity separate from independently verified evidence provenance.

## 6. Terraform apply succeeded; postflight initially failed on relay_state

**Classification:** historical observation O-001; retained local execution receipts; counterexample to treating verifier failure as proof of failed apply.

**Sources:** [publisher spec](/home/ted/dev/aws-iac/specs/iot-artifact-publisher.md), private `apply-result.json` (returncode 0), private `post-apply.json` (failure status), and retained recheck receipt beneath the publisher maintenance review directory. The spec reports 3 added / 0 changed / 0 destroyed.

**Justified:** local historical records distinguish successful apply from failed comparison. **Not justified:** every effect was correct or a successful Terraform exit is sufficient operational assurance. **Competing interpretation:** strict stopping was prudent while semantics were unknown; postflight may reveal a real omission elsewhere. **Links/action:** C-002 gets additional bounded support, maturity remains FORMALIZED; motivates H-002, without treating the original failure as erased.

## 7. The null/empty difference was representational for this incident

**Classification:** derived finding/interpretation supported by the specific recheck; bounded support for C-002.

**Sources:** recheck receipt says verified, exact policy/assignment checks true, existing planning/other permission sets unchanged; [recheck code](/home/ted/dev/aws-iac/scripts/recheck_artifact_publisher.py) and [tests](/home/ted/dev/aws-iac/tests/test_artifact_publisher_recheck.py) restrict the exception to the publisher's planned-null/applied-empty relay field. Provider 6.68.0 scope is recorded in the spec.

**Justified:** the inspected recheck treats this exact representation as equivalent for its stated point-in-time decision. **Not justified:** generic null/empty equivalence, equivalence under other consumers/provider versions, or an audit of all AWS operations. **Competing interpretation:** the exception could be a post-hoc allowlist fitted to one case; another consumer may distinguish absent and empty. **Links/action:** C-002 strengthened in case-level support only; split general usefulness into new H-002 and test it with held-out drift.

## 8. Narrow verifier correction, no AWS change

**Classification:** inspected implementation and retained receipt; finding; suggestive support for C-001.

**Sources:** recheck deep-copies state, applies only the directional comparison exception, retains historical executor/manifest/failure, and records `aws_mutations_performed=false` and `apply_reexecuted=false`. Its tests cover nearby meaningful mismatches, preservation, and unchanged historical failure. These downstream tests were inspected, not rerun here.

**Justified:** code and receipt support correction at the comparison boundary rather than repeating apply; the receipt's point-in-time limitations remain. **Not justified:** backwards tracing generally finds the earliest causal error, or correction is safe outside this scope. **Competing interpretation:** ordinary debugging/root-cause analysis explains it; the earliest error may be the original assumption that strict representation equality implied semantic equality, not just verifier code. **Links/action:** C-001 unchanged FORMALIZED, add measurable H-003; no general causal claim promoted.

## 9. Invalid IoT rule naming detected upstream, not silently normalized

**Classification:** inspected review history and local test logs; bounded finding and counterexample to blanket normalization.

**Sources:** binding spec records the old hyphenated rule name, explicit human-authorized desired-state correction, and schema enforcement; blocker summary records the separate concern and no cloud mutation. **Justified:** this documented path exposed a contract error and changed desired state explicitly while preserving device/topic identity and artifact binding. **Not justified:** the new rule was deployed, detection always occurs, or a naming error is semantically harmless formatting.

**Competing interpretation:** a standard schema/API constraint check would have caught it; consumer-only normalization would conceal the upstream mismatch. **Links/action:** C-001 suggestive case support, C-002 requires decision-specific equivalence; leave maturity unchanged. H-002 must reject treating invalid→valid renaming as an approved null/empty-style equivalence.

## 10. Restricted planners expanded through separate least-privilege reviews

**Classification:** human-reported history; inspected scoped maintenance proposal/review evidence; unresolved longitudinal claim.

**Sources:** [planner-read spec](/home/ted/dev/aws-iac/artifacts/worktrees/iot-ingest-config-read/specs/iot-ingest-config-read.md), blocker summary, publisher spec. The IoT read proposal adds one exact SSM resource, no action delta, and preserves existing conditions/assignments. The inspected summary explicitly says its IAM apply was NOT performed; prior reviewed changes and publisher execution are different operations.

**Justified:** the inspected changes/proposals are separately scoped rather than a broad fallback; an access blocker was not declared permission to expand access automatically. **Not justified:** every proposed expansion was applied, global least privilege is proven, or no bypass/privilege accumulation exists. **Competing interpretation:** ordinary IAM review explains the benefit; separately approved small changes can cumulatively create excessive access. **Links/action:** Q-002, C-004; leave alignment/care claims unchanged and separate proposal, approval, execution, and longitudinal privilege sufficiency.

## Prior art and strongest simpler explanations

NIST separates authentication and authorization and rejects implicit trust based on location or ownership; this provides an existing security framing for the identity/permission distinction. See [NIST SP 800-207](https://www.nist.gov/publications/zero-trust-architecture).

HashiCorp documents provider data-consistency issues, including API normalization and downstream errors. This supports treating the incident as a familiar provider/verifier problem, not evidence of a novel law. It does not certify this particular relay-state equivalence. See [HashiCorp data consistency guidance](https://docs.hashicorp.com/terraform/plugin/sdkv2/resources/data-consistency-errors).

SLSA distinguishes provenance that describes where/when/how an artifact was produced from its bytes alone. Inference: our reported byte checks establish a narrower property than verified build provenance. See [SLSA provenance](https://slsa.dev/spec/v1.2/provenance). No novelty or SLSA conformance is claimed.

CE-001 gives analytical counterexamples to uncertainty, predictability, reachable-state count, and authentication as care/alignment measures. No matched-safety evidence in this history supports H-001. Standard security controls, constrained optimization, and human review remain sufficient competing explanations.

## Program decision recommendation and completed checks

Recommend EXP-004, not infrastructure completion. Its frozen oracle and three baselines can distinguish a useful general verification rule from incident-specific fitting and permissive normalization. No numerical information-gain estimate is justified.

Executed: `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/home/ted/dev/aws-lambda/iot-digital-twin-ingest python3 -B -m unittest discover -s /home/ted/dev/aws-lambda/iot-digital-twin-ingest/tests -v`; 17 tests passed. Synthetic/mocked tests establish local behavior only. No downstream files changed, source rebuilt, artifact published/retrieved, or infrastructure implemented.

**STOP_FOR_HUMAN: Approve, revise, or reject EXP-004 before creating any cross-repository work packages.** No H-001/C-003/C-004 promotion, no package routing, and no deployment authority follow from this assessment.
