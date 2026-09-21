# 08 — Evaluation and Observability

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **08 — Evaluation and Observability** within Computer Use and Interface Agents;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Measure whether interface agents complete tasks correctly, safely and efficiently.

## Evaluation dimensions

Measure task success, step success, grounding accuracy, action correctness, verification quality, recovery, permission compliance, unnecessary actions, latency, cost and human intervention.

## Environment variation

Test different screen sizes, responsive layouts, loading delays, popups, reordered elements, language variants, stale sessions and controlled interface changes.

## Consequence-aware scoring

A harmless extra scroll and a duplicate payment are not equivalent errors. Weight critical failures separately from average task completion.

## Replay

Store privacy-safe observations, structured actions, state transitions, tool outcomes and release versions so failures can be reconstructed.

Do not depend on hidden chain-of-thought.

## Tracing

```text
Goal → observation → grounded target → proposed action → permission result → execution → observed result → verification
```

## Production monitoring

Track completion, failure stage, retries, UNKNOWN outcomes, escalations, approval rates, layout drift, latency, spend and critical incidents by agent/release/site.

## Benchmarks

Synthetic UI benchmarks are useful but must be complemented by production-shaped workflows and real application variation.

## Exercise

Build an evaluation suite for a browser agent with ten workflows and explicit catastrophic-failure criteria.

## Takeaway

> A computer-use agent should be evaluated on verified task outcomes and safe behaviour, not on whether its clicks look human.

Next: **09 — Production Browser and Desktop Agent Infrastructure**.
