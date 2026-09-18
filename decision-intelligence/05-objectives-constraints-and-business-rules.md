# 05 — Objectives, Constraints and Business Rules

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **05 — Objectives, Constraints and Business Rules** within Decision Intelligence;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Make the goal of a decision explicit and prevent optimization from violating non-negotiable rules.

## Objective

Examples include profit, service level, throughput, quality, risk reduction or customer outcome.

Avoid vague goals such as "optimize operations."

## Multiple objectives

Real decisions trade off cost, speed, quality, risk, fairness, resilience and other concerns.

Document the trade-off instead of hiding it inside model behaviour.

## Hard constraints

Legal restrictions, permissions, capacity, budget ceilings, inventory limits and safety rules should be deterministic constraints where applicable.

## Soft constraints

Preferences can influence ranking while remaining negotiable.

## Proxy risk

Optimizing a measurable proxy can damage the actual objective when the proxy stops representing it.

## Feasible set

```text
Possible actions
      ↓
Hard constraints
      ↓
Feasible actions
      ↓
Objective optimization
```

## Exercise

Define objective, hard constraints, soft preferences and anti-gaming metrics for a resource-allocation decision.

## Takeaway

> Optimization should search only inside the space the organization is actually allowed and willing to choose from.

Next: **06 — Optimization, Recommendations and Decision Policies**.
