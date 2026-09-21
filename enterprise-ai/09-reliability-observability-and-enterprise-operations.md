# 09 — Reliability, Observability and Enterprise Operations

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **09 — Reliability, Observability and Enterprise Operations** within Enterprise AI;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Operate AI as a production enterprise service with explicit reliability and response ownership.

## SLOs

Define availability, latency, quality, critical-error, tool success and recovery objectives appropriate to each workflow.

## Observability

Trace identity/tenant, release, model route, retrieval, tools, policy decisions, latency, cost and verified outcome while minimizing sensitive payload logging.

## Dependency map

Know which providers, models, indexes, APIs, queues, databases, identity services and tools each workflow requires.

## Incident classes

Prepare for provider outage, model quality regression, prompt/config change, retrieval corruption, authorization failure, tenant leakage, tool side effects, cost runaway, rate limit and data/privacy incident.

## Degradation

Define approved fallback models, deterministic alternatives, read-only mode, queueing, human handling or safe unavailability.

## Change control

Use versioned releases, evaluation gates, canaries and rollback from Domain 17.

## Business continuity

Back up configuration, registries, policy, indexes/source lineage and operational evidence according to recovery requirements. Test restoration.

## Operations ownership

Every production workflow needs an owner, escalation path and runbook. "The AI team" is not a sufficient incident owner.

## Exercise

Create an SLO and incident runbook for a business-critical AI workflow with two model providers and several enterprise dependencies.

## Takeaway

> Enterprise AI becomes infrastructure when the organization can operate it predictably during both normal use and failure.

Next: **10 — Enterprise AI Capstone**.
