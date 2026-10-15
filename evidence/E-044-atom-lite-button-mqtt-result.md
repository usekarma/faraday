# E-044 — EXP-007 ATOM Lite button MQTT result

**Status:** RECORDED — bounded successful transport; partial LED observation.

Recorded on 2026-10-14 (America/Chicago); exact execution timestamp was not retained.
[Sanitized receipt](atom-lite/button-events-001/receipt.json),
[checksum](atom-lite/button-events-001/SHA256SUMS), and
[experiment](../experiments/EXP-007-atom-lite-button-mqtt.md).

## Provenance and observations

The executed firmware source was `iot-digital-twin` commit
`ee5d6da90c952278a19566bd2969d324c6793683`, app SHA-256
`8d89947bb0c20c165980803bb69ef6ba0ffa69053842ef4d0b3ca229c3808445`.
All four flash ranges verified and private configuration returned CONFIG_READY.
The user separately confirmed subscription/readiness before one ARM_BUTTON.
The retained helper/device receipt reports Wi-Fi, TLS and MQTT readiness for each
event, matching PUBACKs and SESSION_COMPLETE. No reboot, configuration resend,
automatic retry or AWS mutation occurred during the window. Existing identity
and narrow topic policy were reused; Core2 was untouched.

| Sequence | Event ID | Device PUBACK | AWS console |
| --- | --- | --- | --- |
| 1 | `647bb6cc603583773f122a97e938ab84-1` | received | operator confirmed |
| 2 | `647bb6cc603583773f122a97e938ab84-2` | received | operator confirmed |
| 3 | `647bb6cc603583773f122a97e938ab84-3` | received | operator confirmed |

The operator confirmed all three exact IDs in AWS; this is human-reported
corroboration, not agent inspection of the console. No screenshot/export is retained.
The raw private window receipt remains unchanged with its then-pending confirmation
fields; a separate private confirmation appends this later observation. Only
allowlisted statuses, public payloads, hashes and qualified findings are copied here.
No credentials, SSID, private key, PEM, account identifiers or endpoint are included.

## LED observations and limits

| Color | Observation |
| --- | --- |
| Blue (connecting) | tentatively observed by operator |
| Yellow (publishing) | unconfirmed |
| Green (after matching PUBACK) | tentatively observed by operator |
| Red (failure) | untested |

Software tests and linked driver establish implementation intent, not physical
color/timing validation. This run does not establish full LED acceptance. No
additional device tests are authorized by recording or opening review PRs.

## Interpretation and remaining unknowns

This one bounded run supports three button-triggered MQTT events with distinct
session-scoped IDs, sequences1..3, broker acknowledgements and operator-confirmed
cloud visibility. The fresh random session improves correlation over E-043's
fixed diagnostic nonce; it does not prove physical identity, server-enforced
freshness, global persistent sequencing, or replay resistance. QoS1 does not
establish exactly-once cloud delivery; console duplicate counts were not reported.

No fault-path/red LED, expiry, held-at-arm, bounce, fourth-press rejection or
repeatability hardware qualification is claimed. No precise latency measurement,
durable ingestion, TwinMaker integration or production readiness is established.
Existing claim maturities and current-state snapshots are unchanged. Recording
this result performed no new AWS or device operations. **STOP_FOR_HUMAN.**
