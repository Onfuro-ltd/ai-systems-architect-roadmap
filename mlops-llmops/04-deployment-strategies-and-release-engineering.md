# 04 — Deployment Strategies and Release Engineering

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **04 — Deployment Strategies and Release Engineering** within MLOps and LLMOps;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

AI releases need controlled exposure because offline evaluation cannot predict every production interaction.

## Release stages

```text
Development → offline eval → shadow → canary → progressive rollout → production
```

Not every change needs every stage, but risk determines rigor.

## Shadow

Run a candidate on production-shaped inputs without allowing it to control outcomes. Compare quality, latency, cost and failure behaviour while respecting privacy and provider policies.

## Canary

Route a small eligible traffic slice to the candidate with explicit rollback thresholds.

## Feature flags and routing

Decouple deployment from exposure. Flags and model-routing policies allow controlled cohorts, fast rollback and experiments without rebuilding the application.

## Compatibility

Check prompt/tool/schema/runtime compatibility before release. Model changes can expose hidden assumptions in downstream parsers and workflows.

## Migration

For stateful memory, indexes or data contracts, plan forward and backward compatibility. Avoid releases that cannot roll back because the data layer has already irreversibly changed.

## Promotion evidence

Record evaluation report, approver, release manifest, rollout plan and rollback target.

## Exercise

Design a progressive release for a new model and retrieval pipeline serving a consequential workflow.

## Takeaway

> AI deployment is controlled exposure of a versioned system configuration, not simply replacing one model name with another.

Next: **05 — Observability, Tracing and Production Telemetry**.
