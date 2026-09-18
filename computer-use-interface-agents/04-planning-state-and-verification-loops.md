# 04 — Planning, State and Verification Loops

## Purpose

Make interface execution resilient to changing state and uncertain outcomes.

## Plan locally

High-level plans are useful, but do not precompute a long click sequence and assume the interface will remain unchanged.

Use short-horizon execution:

```text
Goal → next safe step → execute → observe → verify → re-plan
```

## State machine

Represent important workflow states explicitly, such as not-started, authenticated, form-open, draft-complete, awaiting-approval, submitted, verified, failed and unknown.

## Verification

Verification may use URL/page identity, semantic element state, confirmation IDs, persisted records, downloaded receipts, API checks or other authoritative evidence.

A toast message alone may be weak evidence for a consequential operation.

## UNKNOWN

If a submission times out after activation, the outcome may be UNKNOWN rather than failed.

Re-check authoritative state before retrying.

## Checkpoints

Persist durable progress for long workflows so recovery does not repeat completed actions.

## Human intervention

Escalate with current state, attempted actions, evidence and the exact decision needed. Do not merely say "it failed."

## Exercise

Model a checkout-like workflow where the final action can time out and design safe recovery without duplicate submission.

## Takeaway

> Reliable agents repeatedly reconcile their internal plan with external reality.

Next: **05 — Authentication, Sessions and Identity**.
