# Domain 21 — AI Economics and Model Routing

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
