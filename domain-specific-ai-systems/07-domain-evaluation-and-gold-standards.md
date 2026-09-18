# 07 — Domain Evaluation and Gold Standards

## Purpose

Define correctness using domain evidence rather than generic model benchmarks.

## Evaluation set

Include common cases, difficult cases, exceptions, historical failures, adversarial inputs, ambiguous cases and high-consequence scenarios.

## Gold standards

Gold answers need source evidence, domain-expert review and versioning. Some tasks permit multiple acceptable answers; encode criteria rather than forcing one string.

## Evaluation layers

Measure extraction/classification accuracy, evidence grounding, rule compliance, tool correctness, workflow success, critical errors and downstream outcome separately.

## Slice analysis

Break results down by important domain segments so aggregate scores do not hide weak populations or case types.

## Critical failures

Define failures that cannot be averaged away: unauthorized action, incorrect high-consequence recommendation, tenant leakage or violation of hard policy.

## Regression

Every material production failure should become a candidate regression case after validation and sanitization.

## Exercise

Build a domain evaluation suite with explicit acceptance gates and catastrophic-failure criteria.

## Takeaway

> Domain expertise becomes an engineering asset when it is encoded into reproducible tests of correctness.

Next: **08 — Feedback, Outcomes and Knowledge Evolution**.
