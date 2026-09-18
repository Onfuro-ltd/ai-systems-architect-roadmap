# 01 — AI Cost Fundamentals

## Purpose

Understand the complete cost of delivering an AI outcome.

## Cost stack

```text
Input/context
+ output/generation
+ reasoning/inference
+ retrieval
+ tool/API calls
+ media processing
+ storage/network
+ retries/fallback
+ infrastructure idle capacity
+ engineering/operations
= lifecycle serving cost
```

Provider token price is only one component.

## Unit selection

Measure cost per request, token, document, conversation, workflow or user when useful, but connect decisions to cost per successful outcome.

## Failure economics

A cheap model that causes retries, escalation, correction or business errors can have higher effective cost.

## Fixed vs variable

Hosted APIs are largely usage-linked; owned infrastructure contains substantial fixed capacity cost. Utilization changes the comparison.

## Marginal vs total cost

Use marginal cost for some routing decisions but total lifecycle cost for architecture and ownership decisions.

## Attribution

Carry tenant, product, workflow, model and route identity into cost telemetry.

## Exercise

Create a cost model for one workflow including model calls, retrieval, tools, retries, human escalation and failed outcomes.

## Takeaway

> AI economics begins by measuring the entire workflow, not the invoice line for model tokens.

Next: **02 — Quality, Latency and Cost Trade-offs**.
