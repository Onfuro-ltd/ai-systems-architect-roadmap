# 08 — Routing Evaluation and Online Optimization

## Purpose

Evaluate the router itself as a decision system.

## Offline routing evaluation

Replay representative tasks across candidate routes and compare selected-route quality, latency, cost and critical failures against baselines.

## Oracle gap

Estimate how far the router is from the best eligible route that could have been selected with hindsight.

## Router errors

Track under-routing to a model that fails, over-routing to unnecessarily expensive capacity, policy violations, excessive escalation and unstable route switching.

## Online experiments

Use controlled experiments for eligible low-risk workloads. Protect hard policy and quality floors outside the optimization algorithm.

## Bandits and learning

Online learning can adapt to changing economics, but reward design matters. Optimizing immediate cost alone can learn harmful behaviour.

## Exploration

Exploration must be bounded by workload risk and eligibility. Consequential traffic may require offline evidence before exposure.

## Drift

Model quality, prices, latency and provider availability change. Re-evaluate profiles and routing policies continuously or on defined triggers.

## Exercise

Define offline and online metrics for a router choosing among three models and prove how you would detect both quality under-routing and wasteful over-routing.

## Takeaway

> A model router is itself an AI/decision component and needs independent evaluation, guardrails and rollback.

Next: **09 — FinOps, Budgets and Economic Governance**.
