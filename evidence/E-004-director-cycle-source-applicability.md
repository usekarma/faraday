# E-004 — Director-cycle source applicability check

**Status:** RECORDED

## Scope and provenance

Cycle RDC-001, 2026-10-10. [Collected comparison](RDC-001-source-comparison.json) records exact local HEADs, branch names, tracked worktree status, pinned paths, old/new SHA-256 values, and collection time. Faraday HEAD before this cycle was `c9bd9d42bef2a2a962a687fc59c5ad7725405578`. Inputs were the existing current-state snapshot, E-002/E-003 source manifests, and local checkouts of the four implementation/apparatus repositories identified by the ecosystem registry.

Only Git metadata and the listed source files were read. No fetch or remote-main comparison, downstream tests, private-receipt refresh, experiment, cloud, device, configuration publication, or infrastructure operation occurred. No source contents are copied into this evidence record. References remain repository-relative. This is an applicability measurement, not a truth or authorization certificate.

## Classified observations and measurements

| Statement | Epistemic kind | Provenance | Scope |
| --- | --- | --- | --- |
| The local aws-lambda HEAD is `497f41716af2a1e0d7ebf83166fec6217a1d070c` on `plan/iot-ingest-artifact-publication` | observation | inspected_source | Local checkout only |
| The local aws-iac HEAD is `155e424f1e970a523ed765d299c91138c458148a` on `feature/iot-artifact-publisher` | observation | inspected_source | Local checkout only |
| The local aws-config HEAD is `9a4a1deb556a8c7d2a3a517843fcd849064ba40c` on `feature/iot-artifact-bucket-config` | observation | inspected_source | Local checkout only |
| The local iot-digital-twin HEAD is `0b303604e741dd642e93834842ed86c78f03e5b4` on `plan/aws-sandbox-first-implementation` | observation | inspected_source | Local checkout only |
| SHA-256 was computed for 16 E-003 manifest entries and 12 E-002 entries | measurement | reproduced | Exact working-tree bytes at collection; two entries overlap across manifests |
| All 28 measured entries match their recorded hashes; none changed or was unavailable | derived_fact | reproduced | Equality of computed/captured digests; no semantic execution implied |
| The four local HEADs match the snapshot revisions but their branch names differ from its main labels | derived_fact | inspected_source | Snapshot-to-local-checkout comparison, not proof that remote main differs |
| The Faraday snapshot names `77a248aaa9452f147f7dd98c90cf13c3c7196cb3`; local HEAD before this cycle is a descendant, `c9bd9d42bef2a2a962a687fc59c5ad7725405578` | observation / derived_fact | inspected_source | `git rev-parse HEAD` and successful `git merge-base --is-ancestor` check |

## Applicability interpretation

**Interpretation / inferred:** no source-byte change in the inspected paths currently demands a repeat of the historical local tests solely for that reason. The same hashes do not exclude changes in uninspected dependencies, execution environment, deployed artifact, certificate mapping, IAM, or remote repository state. Historical test output remains a historical measurement, not newly reproduced behavior.

**Derived fact / inspected_source:** the current-state snapshot is incomplete as a description of these local branch contexts. Its historical main labels are not disproven for the remote repository; their basis was insufficient to infer which local worktree was examined. The proposal records local branches separately rather than declaring remote main refreshed.

**Interpretation / inferred:** E-002 remains historical for current-runtime claims and valid for the prototype source scope. E-003 remains a bounded assessment; its pinned source identity is rechecked locally, while live identity, artifact retrieval, private receipts, and IAM sufficiency remain unrefreshed. Neither record is false because it is historical. Worktree revisions absent from the original manifests remain unknown; matching file hashes do not recover those revisions.

## Counterarguments and limits

**Counterexample / inferred:** identical validator bytes can process forged authenticated-context fields if the surrounding injection boundary or credential mapping changes. A successful hash refresh is therefore inadequate for Q-003. **Counterexample / inferred:** code and a receipt can stay unchanged while AWS configuration drifts. No current operational claim is warranted here.

**Interpretation / inferred:** an ordinary source/dependency applicability check explains this cycle's benefit; no learning, causal inference, alignment, or architectural superiority has been demonstrated. Branch names are context metadata, not evidence that behavior changed.

## Proposed knowledge use

Use this record to annotate applicability and correct snapshot scope through the [review proposal](../current-state/proposals/RDC-001.json). Do not overwrite old capture dates or historical evidence. No claim maturity or blocker is cleared by this measurement. See the [director assessment](../programs/karma-adage-ecosystem/cycles/RDC-001.md) for the next investigation recommendation.
