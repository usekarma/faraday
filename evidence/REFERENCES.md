# Portable evidence references

These logical IDs replace machine locations. Resolve a repository-relative path in an independently available checkout or request access from its custodian; no particular local directory is assumed. Evidence marked private/local is not independently accessible from Faraday. No public URLs are inferred.

[Reference catalog](references.json) carries classifications and captured identities. [Live source manifest](live-program-source-manifest.json) and [inventory manifest](WP-001-source-manifest.json) preserve the original SHA-256 values, HEAD context, and worktree status. A hash identifies bytes, not truth, availability, or label correctness. Worktree HEADs not captured originally remain unknown.

## Portability revision

Machine location metadata was replaced explicitly, including in the historical EXP-003 JSON representation. Each revised JSON records its original document hash and source Faraday commit. Case inputs, outputs, source hashes, and reported conclusions are unchanged; no experiment was rerun. Historical source/spec hashes refer to their original versions, not newly edited documentation or harnesses.

No committed machine-specific links are intentionally retained. Repository-relative paths into private `artifacts/` directories are retained as custodian locators, not public links. Existing external documentation URLs remain public prior-art references.

## SRC-LAMBDA-VALIDATION

Repository: `aws-lambda`. Path: `iot-digital-twin-ingest/validation.py`. Classification: `private-local`.

SHA-256: `5229478719e1af7d9a922eef743ff295f0473791f33d1147accfb5466b03cc92`.

Recorded parent HEAD: `497f41716af2a1e0d7ebf83166fec6217a1d070c`. Worktree: `primary`.

Inspected working-tree bytes; recorded HEAD does not imply these bytes are committed. See source manifest status.

## SRC-LAMBDA-TESTS

Repository: `aws-lambda`. Path: `iot-digital-twin-ingest/tests/test_ingest.py`. Classification: `private-local`.

SHA-256: `8090490aa6c123f9e74481b11f6ef661df5bb752152704a91e72d3a16fdfcd5f`.

Recorded parent HEAD: `497f41716af2a1e0d7ebf83166fec6217a1d070c`. Worktree: `primary`.

Inspected working-tree bytes; recorded HEAD does not imply these bytes are committed. See source manifest status.

## SRC-IAC-IOT-RULE

Repository: `aws-iac`. Path: `components/iot-digital-twin/main.tf`. Classification: `private-local`.

SHA-256: `d3575c1ae9f1e071fbf970d55d8e2bcc0079ea3484c09fc419d099c2012c0406`.

Recorded parent HEAD: `155e424f1e970a523ed765d299c91138c458148a`. Worktree: `primary`.

Inspected working-tree bytes; recorded HEAD does not imply these bytes are committed. See source manifest status.

## SRC-CONFIG-ARTIFACT-BINDING

Repository: `aws-config`. Path: `specs/iot-ingest-artifact-binding.md`. Classification: `private-local`.

SHA-256: `904563b5f97031a952aed0cd7d1080ff00873ed8f937644fa29e27f3d1fe0ff5`.

Recorded parent HEAD: `9a4a1deb556a8c7d2a3a517843fcd849064ba40c`. Worktree: `iot-ingest-artifact-binding`.

Worktree revision was not captured. Parent repository HEAD must not be attributed to these bytes; use the recorded SHA-256.

## SRC-IAC-PUBLISHER-SPEC

Repository: `aws-iac`. Path: `specs/iot-artifact-publisher.md`. Classification: `private-local`.

SHA-256: `25a7875732dae3b3772738b29c6eb63a073ce2af8c251ce7f90687456aa59152`.

Recorded parent HEAD: `155e424f1e970a523ed765d299c91138c458148a`. Worktree: `primary`.

Inspected working-tree bytes; recorded HEAD does not imply these bytes are committed. See source manifest status.

## SRC-IAC-RECHECK

Repository: `aws-iac`. Path: `scripts/recheck_artifact_publisher.py`. Classification: `private-local`.

SHA-256: `aa088e9867483671af5d51df15b8ff0348f087678ab7c04493cc72c9003bbcb0`.

Recorded parent HEAD: `155e424f1e970a523ed765d299c91138c458148a`. Worktree: `primary`.

Inspected working-tree bytes; recorded HEAD does not imply these bytes are committed. See source manifest status.

## SRC-IAC-RECHECK-TESTS

Repository: `aws-iac`. Path: `tests/test_artifact_publisher_recheck.py`. Classification: `private-local`.

SHA-256: `fb2e296ed12736ad124cc79736f13ddbbbe4c624acb402bb8ee55be41458a6b5`.

Recorded parent HEAD: `155e424f1e970a523ed765d299c91138c458148a`. Worktree: `primary`.

Inspected working-tree bytes; recorded HEAD does not imply these bytes are committed. See source manifest status.

## SRC-IAC-PLANNER-READ

Repository: `aws-iac`. Path: `specs/iot-ingest-config-read.md`. Classification: `private-local`.

SHA-256: `73dabe49eea672f00ddf7085b866d57b6dd5986baaea2ffeaff700c19c920154`.

Recorded parent HEAD: `155e424f1e970a523ed765d299c91138c458148a`. Worktree: `iot-ingest-config-read`.

Worktree revision was not captured. Parent repository HEAD must not be attributed to these bytes; use the recorded SHA-256.

## RECEIPT-PUBLISHER-APPLY

Repository: `aws-iac`. Path: `artifacts/identity-center-bootstrap/review-uhd86fs8/maintenance-reviews/artifact-publisher-hrrbk83v/apply-result.json`. Classification: `retained-receipt`.

SHA-256: not captured.

Private artifact revision and hash were not captured; no public URL or content copy supplied.

## RECEIPT-PUBLISHER-POSTFLIGHT-FAILURE

Repository: `aws-iac`. Path: `artifacts/identity-center-bootstrap/review-uhd86fs8/maintenance-reviews/artifact-publisher-hrrbk83v/post-apply.json`. Classification: `retained-receipt`.

SHA-256: not captured.

Private artifact revision and hash were not captured; no public URL or content copy supplied.

## RECEIPT-PUBLISHER-RECHECK

Repository: `aws-iac`. Path: `artifacts/identity-center-bootstrap/review-uhd86fs8/maintenance-reviews/artifact-publisher-hrrbk83v/postflight-rechecks/review-7yolru5o/postflight.json`. Classification: `retained-receipt`.

SHA-256: not captured.

Private artifact revision and hash were not captured; no public URL or content copy supplied.

## REVIEW-IOT-BLOCKERS

Repository: `aws-iac`. Path: `artifacts/iot-ingestion-blockers/review-f_jc7k76/review-summary.json`. Classification: `private-local`.

SHA-256: not captured.

Private artifact revision and hash were not captured; no public URL or content copy supplied.

## REPORT-ARTIFACT-VERIFICATION

Repository: `aws-config`. Path: `specs/iot-ingest-artifact-binding.md`. Classification: `human-reported`.

Human-reported exact-version/checksum/SHA-256/byte-equality checks; report-source hash is not a hash of a publication receipt.
