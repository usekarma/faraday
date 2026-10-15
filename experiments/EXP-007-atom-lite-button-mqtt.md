# EXP-007 — ATOM Lite physical-button MQTT events

**Status:** RECORDED

## Question, baseline, and preparation authority (historical)

Can one deliberate physical ATOM Lite button press produce one generated MQTT
event with a fresh event ID and sequence, observed in AWS IoT Core? The human
initially requested preparation only: implementation, checks and reviewed flash plan.
Separate later approvals authorized the flash, private configuration, and one bounded
button window; execution results and their limits are recorded in E-044 below.
Flashing, provisioning, arming, publishing and AWS mutation are not authorized
by this proposal. No device or AWS operations occurred during preparation.

E-043 recorded a serial-triggered message, device PUBACK, and human console
confirmation. Its fixed zero nonce does not establish freshness. This experiment
adds physical input and session-scoped event correlation, not physical identity
attestation or closure of Q-003. Core2 records remain historical and unchanged.

## Prepared apparatus and input/output contract

Target: `iot-digital-twin`, local branch `feature/atom-lite-button-events`,
commit `ee5d6da90c952278a19566bd2969d324c6793683` (based on the E-043 firmware source).
Changed files: firmware README, src/main.cpp, include/button.hpp,
test/native_contract.cpp, tools/send_once.py, tests/test_atom_mqtt_proof.py,
include/status_led.hpp, and specs/atom-lite-button-events.md. The spec contains the acceptance contract,
threat limits, runbook and failure handling. The primary checkout's two existing
document edits were not modified. Firmware compile passed; app SHA-256
`8d89947bb0c20c165980803bb69ef6ba0ffa69053842ef4d0b3ca229c3808445`.
Frozen images, exact four-image flash plan and recovery-tested source bundle are
retained privately outside Git; operational evidence and credentials are excluded.

Reuse existing ATOM certificate, client `atom-lite-001`, narrow policy and exact
topic `devices/atom-lite-001/probe`. No new certificate, policy, Thing or infrastructure.
M5Stack documents active-low GPIO39:
https://docs.m5stack.com/en/homeassistant/devices/atom_lite.

Private CONFIG loads credentials in RAM. Explicit ARM_BUTTON opens one 120-second
window, at most three accepted presses. No RUN_ONCE in this firmware. Require 50ms
stable release then 50ms stable press; hold/bounce does not repeat. Presses during
blocking connection/publish are ignored and not queued; require another stable
release afterward. An admitted network attempt may finish after the window closes.
Any failure or unknown outcome stops the session; no automatic retry/reconnect.

Host generates a fresh 128-bit session ID (`secrets.token_hex(16)`); firmware rejects
the all-zero value. Sequence 1..3 is consumed before network I/O, resets with a new
session, and is not globally persistent. Event ID is session_id + '-' + sequence.

```json
{"device_id":"atom-lite-001","event":"button_press","session_id":"<fresh 32 lowercase hex>","event_id":"<session_id>-1","sequence":1}
```

QoS1, no DUP/RETAIN requested, verified TLS, same topic and client. Payload labels
are not attestation. QoS1 does not guarantee exactly-once delivery: compare distinct
event IDs and report repeated deliveries of the same ID separately. Session IDs
provide probabilistic correlation, not server-enforced freshness or replay protection.

## Predeclared execution and falsification plan (historical)

1. Review frozen source/images, preserved factory and E-043 images, existing identity
   and exact policy, serial permissions, chip/capacity and read-only security settings.
   Stop on mismatch. No eFuse writes, forced flash or automatic repair/rollback.
2. After approved flash, verify all four write hashes and ATOM_BUTTON_V1 READY.
   Obtain fresh human confirmation of the AWS topic subscription before arming.
3. Configure and arm with the reviewed paced helper. Before pressing, verify no
   event appears. A button already held at arm must not trigger one.
4. Release then press and hold. Match event_id/session_id/sequence1 in sanitized
   serial output, device PUBACK and operator's AWS console receipt. Hold produces
   no extra generated event. Deliberately repeat twice for sequences2 and3.
5. Record exact source/image hashes, observed IDs, per-event results, duplicate
   deliveries and separate console provenance. Expiry/cap/failure ends the session.

Fail on spontaneous events, repeated events from hold/bounce, unexpected sequence,
identity mismatch, missing acknowledgement or absent console observation. The recorded
result follows below. If preparation passes but live operation fails, retain negative
results and distinguish physical input, UART, Wi-Fi/TLS, MQTT and console boundaries.

## Verification and limits

Native C++ tests cover arm gating, held-at-arm, stable-release requirement, bounce,
hold, sequence1..3, cap, rearm refusal, timeout including timer wrap, event-ID changes,
invalid session/sequence and QoS1 wire payload. Python tests cover paced exact-byte
transfer and no retry after partial write. Full engineering checks passed: 48 tests,
94% reported Python business-app coverage, validators/security/format/lint/types and
locked dependency audit. That coverage does not measure C++ hardware paths. Compile
passed; no hardware or cloud runtime result is inferred from these checks.

Private keys remain software-held; trusted USB host and software execution are
assumptions. No secure-boot/flash-encryption assurance, durable ingestion, TwinMaker,
production reliability or global persistent sequence is established. No existing
claim maturity or program snapshot changes. **STOP_FOR_HUMAN before flashing or execution.**

## LED feedback revision (historical preparation before approved flash)

The original eb2a86d candidate and proposal omitted LED control. They are preserved
in Git and the private pre-LED packet; they are not evidence of LED behavior.
The current source/image above adds blue during Wi-Fi/TLS/MQTT connection, yellow
from PUBLISH until PUBACK validation, green only after exact matching PUBACK,
and red on failure or unknown outcome (including configuration/command errors).
Idle/startup/accepted configuration and normal expiry are off. A new attempt
replaces prior green with blue; final successful completion keeps green. Green
indicates broker acknowledgement, not independent AWS console visibility.

The installed Arduino core includes neopixelWrite, using RMT 24-bit GRB output;
the driver is linked into the compiled ELF. No new dependency was added. M5Stack
specifies one SK6812 at GPIO27 and GRB order; reference is above. Dim channel values
are 24/255. No deliberate LED delay was added; two-minute window and max three
button events remain unchanged. Native tests cover color mapping and prevent green
on premature, invalid or post-failure ACK transitions. Full 48-test engineering
checks and compile passed, and updated source bundle recovery was tested.

Physical validation still required: actual board wiring/revision, channel order,
brightness and visibility, RMT timing/latch compatibility with the SK6812 alongside
Wi-Fi, and visibility of a potentially brief yellow interval. The cached driver has
no error return, so an electrical or driver problem may leave colors incorrect
without detection; sanitized serial and cloud evidence are required independently.
The revised exact images and hashes are in the private approval packet. No device,
AWS, flash or publish action occurred during this revision. **STOP_FOR_HUMAN.**

## Recorded EXP-007 result

[E-044](../evidence/E-044-atom-lite-button-mqtt-result.md) records one approved
window ending SESSION_COMPLETE: three events, sequences 1,2,3, unique event IDs,
matching PUBACKs, and the operator's confirmation of all three exact IDs in AWS.
No automatic retries, reboot or configuration resend occurred within that window.
LED evidence is partial: blue and green tentatively observed; yellow unconfirmed;
red untested. Do not mark visual feedback fully validated. No held-button, bounce,
expiry or fault-path hardware qualification is inferred from this successful run.
The earlier preparation sections and predeclared plan are retained as history;
this recorded outcome does not authorize another execution. No broader claim
maturity or program snapshot changes. **STOP_FOR_HUMAN for further device tests.**
