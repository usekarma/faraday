# Q-003 — What would establish authenticated physical identity end-to-end?

**Status:** OPEN

## Source and related records

E-003; Q-002; C-004. The current declared rule injects `principal()` and the runtime compares the event principal, device ID, and topic with configured expectations. `trusted_principal` remains unresolved until independently verified.

## Question

Can a reviewed chain connect this physical device, provisioned credential, IoT authenticated connection, server-originated principal, validated event, and persisted observation without allowing payload-controlled identity or topic fields to substitute for authenticated context?

## Weakening observations and alternatives

Payload collisions may affect injected field semantics; a valid credential can be copied or used by a compromised device; registry bindings can change; stale authorized telemetry can be replayed. Credential-possession evidence may be all this apparatus can establish. Distinguish that narrower claim from proof of truthful physical sensing.

## Minimal future experiment and authority

After independent principal/certificate mapping review, compare matching real-device publish with mismatched payload ID, forged principal/topic fields, unauthorized topic, and changed/revoked credential cases. Declare expected rejects and require no state mutation plus authenticated context provenance. This is not the selected next experiment and authorizes no device, certificate, IAM, or cloud actions. STOP_FOR_HUMAN before creating its cross-repository work package.
