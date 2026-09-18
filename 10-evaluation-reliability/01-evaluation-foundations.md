# 01 — Evaluation Foundations

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **01 — Evaluation Foundations** within Evaluation and Reliability;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Evaluation converts vague claims such as "the agent works well" into testable evidence.

A useful evaluation begins with the behaviour that matters, not with the metric that is easiest to collect.

## Core Principle

> Define success before measuring it.

## Evaluation Object

First define what is being evaluated.

Examples:

- model response;
- retrieval system;
- skill;
- tool selection;
- agent trajectory;
- workflow;
- complete product experience.

The evaluator should match the object.

## Unit of Evaluation

A unit can be:

- one prompt;
- one document;
- one tool call;
- one agent run;
- one workflow;
- one user task;
- one business outcome.

Choose the unit that reflects the decision you need to make.

## Offline Evaluation

Offline evaluation runs against controlled task suites.

Useful for:

- development;
- regression;
- model comparison;
- prompt changes;
- tool changes;
- release gates.

Offline evaluation is repeatable but cannot perfectly reproduce production.

## Online Evaluation

Online evaluation measures live behaviour.

Useful for:

- real distributions;
- changing user behaviour;
- production failures;
- cost and latency;
- downstream outcomes.

Online evaluation introduces operational and privacy considerations.

## Leading vs Lagging Metrics

### Leading

Signals available during or immediately after execution.

Examples:

- schema validity;
- correct tool selection;
- grounded evidence;
- policy compliance.

### Lagging

Signals observed later.

Examples:

- user correction;
- task completion;
- refund;
- business outcome;
- incident.

Both can matter.

## Exact vs Behavioural Criteria

Some requirements are exact.

Examples:

- valid JSON;
- correct calculation;
- required field;
- no prohibited tool.

Others are behavioural.

Examples:

- answer is relevant;
- reasoning is supported;
- summary is complete;
- escalation is appropriate.

Do not force subjective behaviour into false exactness.

## Multi-Metric Evaluation

A system may need separate metrics for:

- correctness;
- completeness;
- groundedness;
- safety;
- tool use;
- latency;
- cost.

Avoid collapsing every dimension into one opaque score too early.

## Baseline

Every improvement claim needs a comparison.

Useful baselines include:

- previous production version;
- no-memory system;
- single-agent version;
- deterministic workflow;
- simpler model;
- human process.

## Thresholds

Thresholds should connect to the risk of the use case.

A high-consequence action may require near-perfect deterministic checks even if the model quality threshold is lower elsewhere.

## Statistical Thinking

Evaluation results are estimates from samples.

Consider:

- sample size;
- variance;
- confidence;
- task mix;
- repeated runs.

A small improvement on a tiny dataset may be noise.

## Repeated Sampling

Probabilistic systems can produce different results on repeated runs.

For unstable tasks, evaluate multiple samples.

Measure:

- mean performance;
- variance;
- failure frequency;
- worst-case patterns.

## Exercise

Choose a generic AI task.

Define:

1. evaluation object;
2. evaluation unit;
3. three success dimensions;
4. offline metric;
5. online metric;
6. baseline;
7. release threshold.

## Takeaway

> Evaluation is a measurement design problem before it is a tooling problem.

Next: **02 — Task Suites, Golden Datasets and Holdouts**.
