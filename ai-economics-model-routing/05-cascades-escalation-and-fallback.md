# 05 — Cascades, Escalation and Fallback

## Purpose

Use cheaper or faster models where they work while escalating uncertain or failed tasks safely.

## Cascade

```text
Lower-cost eligible model
        ↓
Validation / confidence evidence
   pass ─┴─ fail
 outcome   stronger eligible model
```

The validation signal must correlate with actual task correctness.

## Escalation triggers

Possible triggers include schema failure, low calibrated confidence, disagreement, missing evidence, complex task class, tool failure or deterministic validation failure.

## Fallback

Fallback handles unavailability or failure, not merely quality escalation. An alternate provider must still satisfy privacy, residency, modality and workload approval.

## Retry economics

Repeated calls to a cheap failing model can cost more and add more latency than immediate escalation.

## Human escalation

Some consequential or ambiguous tasks should leave the model cascade and enter human review.

## Loop prevention

Bound attempts and track route history so fallbacks do not cycle.

## Exercise

Design a two-model extraction cascade with deterministic validation, escalation and human review for unresolved critical fields.

## Takeaway

> Cascades save money only when failure detection is trustworthy and escalation is bounded.

Next: **06 — Caching, Batching and Context Economics**.
