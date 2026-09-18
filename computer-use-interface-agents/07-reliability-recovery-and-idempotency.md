# 07 — Reliability, Recovery and Idempotency

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **07 — Reliability, Recovery and Idempotency** within Computer Use and Interface Agents;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Recover from interface failures without repeating harmful actions.

## Failure classes

Expect stale elements, navigation changes, popups, slow loads, partial forms, network failure, CAPTCHA/challenge, expired sessions, changed layouts, duplicate clicks, timeouts and ambiguous submission outcomes.

## Retry taxonomy

Read-only actions may often retry safely. State-changing actions require state-aware recovery.

Never translate "no confirmation received" directly into "submit again."

## Idempotency

Where the target system supports idempotency keys, stable references or draft identifiers, use them.

Where it does not, verify external state before repeating a consequential operation.

## Recovery ladder

```text
Re-observe
 ↓
Re-ground target
 ↓
Retry safe operation
 ↓
Alternate approved path
 ↓
Restore checkpoint
 ↓
Human escalation
```

## Layout change

Prefer semantic re-grounding over hard-coded coordinate repair.

## Challenges

CAPTCHAs, anti-bot checks and security challenges are signals to stop or request legitimate user participation, not obstacles to bypass.

## Side effects

Record evidence of submissions, messages, purchases, uploads and deletions so recovery can reconcile what actually occurred.

## Exercise

Design recovery for an agent sending a business message when the UI freezes immediately after clicking Send.

## Takeaway

> Retry perception freely; retry consequential effects only after proving their prior outcome.

Next: **08 — Evaluation and Observability**.
