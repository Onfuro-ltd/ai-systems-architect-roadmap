# 06 — Optimization, Recommendations and Decision Policies

## Purpose

Turn forecasts and objectives into explicit candidate actions.

## Optimization

Depending on the problem, use rules, mathematical optimization, heuristics, simulation, search, ranking, reinforcement learning or combinations.

Do not use an LLM merely because the system is called AI.

## Decision policy

A policy maps observed state to a recommended or executable action under constraints.

## Scenario analysis

Evaluate candidate actions across plausible futures rather than only one forecast.

## Robustness

A slightly lower expected-value action may be preferable if it performs much better under uncertainty or tail scenarios.

## Recommendation contract

Return proposed action, alternatives, expected effect, uncertainty, binding constraints, evidence and reason codes.

## Execution boundary

Recommendation and execution remain separate permissions. High-consequence actions may require approval.

## Exercise

Design a recommendation service that chooses among several feasible actions using expected outcome and downside constraints.

## Takeaway

> A recommendation is a structured decision proposal, not a natural-language opinion from a model.

Next: **07 — Explanations, Confidence and Human Decisions**.
