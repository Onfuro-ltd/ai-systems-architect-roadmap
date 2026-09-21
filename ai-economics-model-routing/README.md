# Domain 21 — AI Economics and Model Routing

## Learning objectives

By the end of this domain, you should be able to:

- explain the core concepts and distinctions across AI cost, capability profiles, routing, cascades, caching, specialist/local economics, online optimisation and FinOps.
- build or evaluate a representative implementation rather than relying on a demo;
- make architecture decisions that account for reliability, security, cost, scale and operations;
- define the evidence, evaluation and governance required before production adoption.

## Purpose

AI systems should select models and infrastructure from measured task requirements rather than brand loyalty or benchmark prestige.

> The cheapest token is not necessarily the cheapest outcome, and the strongest model is not necessarily the best model for every task.

## Domain structure

01 AI Cost Fundamentals  
02 Quality, Latency and Cost Trade-offs  
03 Model Capability Profiles and Task Taxonomy  
04 Routing Architectures and Policy Gates  
05 Cascades, Escalation and Fallback  
06 Caching, Batching and Context Economics  
07 Specialist, Local and Open-Model Economics  
08 Routing Evaluation and Online Optimization  
09 FinOps, Budgets and Economic Governance  
10 AI Economics and Model Routing Capstone

## Core architecture

```text
Task
 ↓
Risk / privacy / residency / permissions
 ↓
Capability requirements
 ↓
Eligible model + infrastructure set
 ↓
Router
 ↓
Execution
 ↓
Validation / evaluation
 ↓
Quality + latency + cost + outcome
 ↓
Routing evidence
```

Policy eligibility comes before price optimization.

## Principles

1. Optimize cost per successful outcome.
2. Measure quality by task, not global model reputation.
3. Treat latency and reliability as economic variables.
4. Route only among policy-eligible options.
5. Escalate based on evidence, not model vanity.
6. Include retries, tools, context and failures in cost.
7. Use caching only when semantics and privacy permit.
8. Re-evaluate routes as models and prices change.
9. Keep provider-specific logic behind adapters.
10. Budget and attribute AI spend by useful workload.

## Takeaway

> Model routing is an economic control system built on capability evidence and deterministic policy constraints.

Next: **01 — AI Cost Fundamentals**.

## Canonical curriculum navigation

- [AI Cost Fundamentals](./01-ai-cost-fundamentals.md)
- [Quality, Latency and Cost Trade-offs](./02-quality-latency-and-cost-trade-offs.md)
- [Model Capability Profiles and Task Taxonomy](./03-model-capability-profiles-and-task-taxonomy.md)
- [Routing Architectures and Policy Gates](./04-routing-architectures-and-policy-gates.md)
- [Cascades, Escalation and Fallback](./05-cascades-escalation-and-fallback.md)
- [Caching, Batching and Context Economics](./06-caching-batching-and-context-economics.md)
- [Specialist, Local and Open-Model Economics](./07-specialist-local-and-open-model-economics.md)
- [Routing Evaluation and Online Optimization](./08-routing-evaluation-and-online-optimization.md)
- [FinOps, Budgets and Economic Governance](./09-finops-budgets-and-economic-governance.md)
- [AI Economics and Model Routing Capstone](./10-ai-economics-and-model-routing-capstone.md)

## Prerequisites and next steps

**Recommended prerequisites:** [03 — AI Application Engineering](../application-engineering/README.md), [10 — Evaluation and Reliability](../10-evaluation-reliability/README.md), [14 — Open-Source and Local AI](../open-source-local-ai/README.md), [16 — GPU and Inference Infrastructure](../gpu-inference-infrastructure/README.md)

**Useful next domains:** [22 — Enterprise AI](../enterprise-ai/README.md), [23 — AI Product Design](../ai-product-design/README.md), [28 — Build an AI Operating System](../ai-operating-system/README.md)

See the [full prerequisite map](../roadmap/prerequisites-and-paths.md) and [domain status matrix](../roadmap/domain-status.md).
