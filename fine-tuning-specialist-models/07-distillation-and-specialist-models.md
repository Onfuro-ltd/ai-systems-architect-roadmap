# 07 — Distillation and Specialist Models

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **07 — Distillation and Specialist Models** within Fine-Tuning and Specialist Models;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose
Distillation transfers useful behaviour from a stronger teacher or system into a smaller model optimized for a bounded workload.

> A specialist does not need to become a smaller frontier model. It needs to become reliably excellent at its assigned task.

## Teacher-student flow

```text
Representative inputs → strong teacher/system → verified targets → student training → held-out evaluation
```

The teacher can be an entire system containing retrieval, tools, validators, and human correction.

## Why distill
Potential benefits include lower latency/cost, higher throughput, private/local deployment, and predictable capacity.

## Specialist contract
Define supported inputs, outputs, domains, languages, context sizes, quality threshold, and out-of-domain behaviour.

Route outside the boundary elsewhere.

## Teacher quality
Validate teacher outputs. Distillation reproduces teacher errors as easily as strengths.

Do not remove retrieval or tools if current facts are still required in production.

## Cascades and routing

```text
Task → eligibility → specialist
                 ↘ stronger/general route when needed
```

Use measured eligibility and escalation rather than model confidence alone.

## Evaluation and drift
Compare specialist with the teacher/system and production threshold. Measure task success, critical errors, out-of-domain detection, latency, throughput, and cost.

Monitor input-distribution and outcome drift.

## Economics
Include teacher generation, verification, training, serving, escalation, monitoring, and retraining. Evaluate total lifecycle economics.

## Exercise
Design a student for a high-volume task handled by a frontier system. Define teacher pipeline, verification, specialist boundary, data, escalation, evaluation, drift monitoring, and break-even economics.

## Takeaway
> Distillation is system compression: preserve verified behaviour that matters, route around the specialist's limits, and measure whether the smaller system improves economics.

Next: **08 — Evaluation and Regression Testing**.
