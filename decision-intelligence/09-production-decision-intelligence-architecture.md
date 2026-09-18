# 09 — Production Decision Intelligence Architecture

## Purpose

Operate decision services as versioned, observable and governed production systems.

## Architecture

```text
Events / authoritative data
          ↓
Point-in-time feature layer
          ↓
Forecast / prediction services
          ↓
Causal / scenario evidence
          ↓
Constraint engine
          ↓
Optimization / decision policy
          ↓
Recommendation API
          ↓
Approval / execution
          ↓
Decision + outcome store
          ↓
Evaluation / monitoring
```

## Versioning

Track feature definitions, data snapshots, predictive models, causal assumptions/estimators, objectives, constraints and decision-policy versions.

## Observability

Monitor input freshness, feature health, prediction drift, constraint failures, recommendation distribution, overrides, execution, outcome and cost.

## Shadow mode

Run new policies without executing them to compare recommendations and collect evidence before promotion.

## Rollback

Decision policies must be independently reversible from underlying application releases where practical.

## Governance

Maintain decision inventory, owner, objective, affected population, authority, risk class, evaluation and review cadence.

## Exercise

Design a production control plane supporting several independent decision services sharing feature and evaluation infrastructure.

## Takeaway

> A production decision system must make both its recommendations and the machinery that produced them reproducible.

Next: **10 — Decision Intelligence Capstone**.
