# 08 — Enterprise AI Platform and Team Topology

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **08 — Enterprise AI Platform and Team Topology** within Enterprise AI;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Build shared enterprise capabilities without creating a central team that becomes a bottleneck.

## Platform capabilities

Common services can include model gateway/routing, identity propagation, tool registry, RAG/knowledge services, evaluation, prompt/skill registry, observability, policy, secrets, cost management and deployment tooling.

## Paved road

Provide templates, SDKs, reference architectures and automated controls so teams can build safely without reinventing infrastructure.

## Team topology

A common pattern:

```text
Central AI platform / enablement
        ↕
Security, data, legal/risk
        ↕
Domain product teams
        ↕
Business/domain experts
```

## Ownership

Domain teams own task correctness and business outcomes. Platform teams own shared reliability and controls. Governance functions define/assure requirements without owning every product decision.

## Build vs buy

Buy commodity capabilities when they satisfy requirements; build where proprietary workflow, integration, control or economics create strategic value.

## Standards

Standardize contracts, telemetry, evaluation evidence, identity, release manifests and tool permissions—not every implementation detail.

## Internal developer experience

Fast local development, test environments, safe credentials, reproducible evals and clear documentation reduce shadow systems.

## Exercise

Design the platform/team boundaries for an enterprise supporting twenty AI products across several business units.

## Takeaway

> A strong enterprise AI platform centralizes reusable controls while keeping domain accountability decentralized.

Next: **09 — Reliability, Observability and Enterprise Operations**.
