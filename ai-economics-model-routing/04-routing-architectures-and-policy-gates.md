# 04 — Routing Architectures and Policy Gates

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **04 — Routing Architectures and Policy Gates** within AI Economics and Model Routing;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Design a routing control plane that separates eligibility from optimization.

## Architecture

```text
Request
 ↓
Task classification
 ↓
Policy gate
 privacy / residency / risk / tenant / modality
 ↓
Eligible candidates
 ↓
Economic/capability router
 ↓
Provider/runtime adapter
 ↓
Validation + outcome telemetry
```

## Deterministic eligibility

A cheaper model cannot be selected if it violates privacy, residency, license, workload approval or capability requirements.

## Router strategies

Strategies include static rules, task-to-model maps, threshold routers, learned routers, bandits/online optimization and cascades.

Start with the simplest strategy that can be evaluated and explained.

## Canonical interface

Normalize requests and responses behind internal contracts. Keep provider-specific parameters in adapters.

## Routing features

Use permitted features such as task type, context size, modality, latency class, tenant policy, required tools and evaluated difficulty. Avoid unnecessary sensitive data.

## Explainability

Record candidate set, policy exclusions, selected route, router version and reason/features needed for audit.

## Exercise

Design a router where confidential documents must remain private while public low-risk extraction can choose among several hosted or local models.

## Takeaway

> Policy determines where a task may run; routing determines the best eligible place to run it.

Next: **05 — Cascades, Escalation and Fallback**.
