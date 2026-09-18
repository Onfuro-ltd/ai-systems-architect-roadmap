# 08 — Enterprise AI Platform and Team Topology

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
