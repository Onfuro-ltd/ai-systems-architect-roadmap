# 07 — Rollback, Incident Response and Recovery

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **07 — Rollback, Incident Response and Recovery** within MLOps and LLMOps;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Every AI release and dependency change needs a safe recovery path.

## Incident classes

Plan for quality regression, unsafe behaviour, model/provider outage, retrieval corruption, tool failure, cost runaway, latency/capacity failure, bad prompt/configuration, compromised artifact and data/privacy incident.

## Kill switches

Provide scoped controls to disable a model, tool, agent capability, adapter, route or autonomous action without taking down unrelated functionality.

## Rollback

Maintain the last known-good release manifest and compatible artifacts. Roll back model, prompt, retrieval/index, tool schema, policy/config or runtime as needed.

## Data compatibility

A code rollback is not enough if state or indexes changed incompatibly. Design reversible migrations or forward-compatible recovery.

## Degradation

Fallback can mean alternate approved model/provider, deterministic workflow, read-only mode, human escalation, delayed background work or safe rejection.

Fallback must preserve policy and privacy.

## Incident evidence

Preserve timestamps, release IDs, traces, routing, inputs/outputs where permitted, tool effects, approvals and verified outcomes.

Do not rely on hidden reasoning as forensic evidence.

## Post-incident learning

Convert incidents into regression tests, monitoring, runbook changes, architecture corrections and controlled backlog items.

## Exercise

Write a response plan for a newly deployed model that passes health checks but begins producing materially incorrect structured actions.

## Takeaway

> Rollback is a product capability of the AI platform, not an emergency script written after the incident.

Next: **08 — Operational Governance and Model Registry**.
