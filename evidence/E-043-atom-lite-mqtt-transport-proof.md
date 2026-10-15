# E-043 — ATOM Lite single-message MQTT transport proof

**Status:** RECORDED — bounded live transport observation plus human console confirmation.

Recorded on 2026-10-14 (America/Chicago). The attempt receipt did not capture an exact execution timestamp; the private preparation directory date is not an execution timestamp.

## Evidence and provenance

[Sanitized receipt](atom-lite/mqtt-proof-001/receipt.json) and [checksum manifest](atom-lite/mqtt-proof-001/SHA256SUMS) retain the public payload and allowlisted status sequence. The original private attempt receipt is retained unchanged, including its then-pending console-confirmation field; a separate private operator confirmation appends the later observation. No credentials, keys, PEMs, provisioning frames, SSID, account identity, endpoint, or raw serial output are copied here.

Apparatus: M5Stack ATOM Lite, ESP32-PICO-D4 revision 1.1. Firmware source: `iot-digital-twin` local branch `feature/atom-lite-mqtt-proof`, commit `b3495e59a67c728a3a5d2ff4ced12c3f2fd6de7c`; app SHA-256 `56248a2a153516d5fc9d432a8c99470be3db4d82980bbf88f526081b93ddaba4`. The private host helper subsequently received the reviewed pacing-only patch; the firmware was unchanged.

## Observations

- Retained device/helper receipt: exactly one `RUN_ONCE` write attempt using configuration already in RAM; no reboot, configuration resend, or automatic retry during this publish attempt.
- Device statuses: `WIFI_READY`, `TLS_READY`, `MQTT_READY`, `PUBACK_RECEIVED`; the host also checked the reported probe payload against the loaded configuration.
- Human-reported independent console observation: the operator confirmed that the exact payload below appeared in the subscribed AWS IoT MQTT test client on `devices/atom-lite-001/probe`. The recording agent did not inspect the console; no screenshot or console export is retained.

```json
{"device_id":"atom-lite-001","probe":"mqtt-proof","nonce":"00000000000000000000000000000000"}
```

Earlier preparation included an acknowledgement timeout, a paced transfer returning `COMMAND_REJECTED`, then one separately approved controlled reboot and paced configuration transfer returning `CONFIG_READY`. These negative results remain in private evidence. The initial timeout's root cause is unresolved; the later success does not prove UART overflow caused it.

## Interpretation and limits

The broker PUBACK and operator console confirmation support one successful ATOM-to-AWS IoT MQTT transport demonstration with the reviewed image. PUBACK alone would not establish console visibility. This record does not promote any broader research claim or close Q-003.

The nonce is the fixed, all-zero diagnostic value already loaded in RAM, not a freshly generated run-unique challenge. Matching it is consistent with this attempt but cannot independently exclude another message using the same payload, replay, or stale matching evidence. It is not a freshness or anti-replay proof.

The device_id payload is a label, not physical identity attestation. Software-held key material, disabled secure boot/flash encryption, lack of repeatability testing, and absence of durable downstream-ingestion evidence bound this proof. Historical Core2 evidence, including E-041, remains applicable to that separate apparatus and is not rewritten by this ATOM result.

## Final state and authority

The successful firmware path disconnects MQTT/Wi-Fi, wipes configured credential strings, and enters terminal state; this is source-defined behavior, not a new post-run device inspection. No further publishing, serial interaction, or AWS change was performed while recording this evidence. The prior dedicated ATOM certificate/policy remain provisioned; no new cloud inventory read was made here. Core2 was not touched. Future runs, identity cleanup, or broader engineering work require their own scoped direction. No new work package, claim-maturity transition, or current-state snapshot rewrite is made.
