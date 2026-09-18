# 07 — Reconciliation, Idempotency and Recovery

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **07 — Reconciliation, Idempotency and Recovery** within Business Automation;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Prevent duplicate, missing or inconsistent business effects.

## Idempotency

Assign stable operation identifiers and use native idempotency support where available.

## Unknown outcome

A timeout after an external write creates UNKNOWN, not automatically FAILED.

```text
Attempt action
   ↓
No definitive response
   ↓
UNKNOWN
   ↓
Query authoritative external state
   ↓
Exists → record success
Missing → safely retry
Ambiguous → human/recovery path
```

## Reconciliation

Periodically compare expected workflow state with authoritative external records to detect missing, duplicated or divergent effects.

## Compensation

Some operations can be reversed with compensating transactions rather than database rollback.

## Dead letters

Failed items need ownership, evidence, replay rules and resolution—not permanent abandonment in a queue.

## Recovery

Restore from durable checkpoints and never repeat completed consequential steps merely because a worker restarted.

## Exercise

Design recovery for a payment-like action where network failure occurs after the external system accepts the request.

## Takeaway

> Reliable automation proves external state before repeating a side effect.

Next: **08 — Automation Evaluation and Process Intelligence**.
