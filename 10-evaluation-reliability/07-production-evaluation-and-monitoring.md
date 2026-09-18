# 07 — Production Evaluation and Monitoring

## Purpose

Offline evaluation cannot capture every production condition.

Production evaluation closes the loop between controlled testing and real-world behaviour.

## Core Principle

> Offline evals prevent known regressions; production evaluation discovers the unknown ones.

## Production Signals

Useful signals include:

- task completion;
- user correction;
- user retry;
- escalation;
- abandonment;
- tool errors;
- policy blocks;
- latency;
- cost;
- downstream business outcome.

## Sampling

Not every production run must receive full behavioural grading.

Use sampling based on:

- risk;
- novelty;
- failure signals;
- random sample;
- model version;
- workflow version.

## Shadow Evaluation

A candidate system can run in shadow mode without affecting users.

Compare its outputs or decisions against production.

Shadowing is useful before high-risk changes.

## Canary

A canary exposes a new version to a small traffic slice.

Monitor:

- quality;
- failures;
- latency;
- cost;
- policy events.

Expand only if evidence is acceptable.

## A/B Testing

A/B tests measure user or business outcomes between variants.

They are useful for product behaviour but are not substitutes for hard safety or correctness gates.

Do not knowingly expose unsafe variants merely to measure conversion.

## Drift

Monitor changes in:

- input distribution;
- task mix;
- language;
- context length;
- tool usage;
- user behaviour.

Performance can degrade without any code change.

## Model Drift

Provider model updates or routing changes can alter behaviour.

Track the actual model/version used for each run where available.

## External Dependency Drift

Tool APIs, schemas and data can change.

Evaluation should detect integration drift.

## User Feedback

Feedback is useful but biased.

Users report some failures more than others.

Combine explicit feedback with behavioural and system metrics.

## Automatic Production Grading

Model judges can grade samples in production.

Use:

- calibrated rubrics;
- sampling;
- privacy controls;
- versioned judge;
- human audit.

## Alerting

Alert on:

- critical policy violation;
- large quality drop;
- unusual tool failure;
- cost spike;
- latency spike;
- escalation spike.

Avoid alerting on noisy metrics without actionability.

## Evaluation Store

Keep evaluation records separate enough to support analysis.

Useful fields include:

- run;
- system version;
- dataset or production slice;
- evaluator;
- score;
- failure class;
- timestamp.

## Feedback to Development

Production findings should feed:

- new task cases;
- new slices;
- new regressions;
- architecture changes.

## Exercise

Design production evaluation for a generic support agent.

Specify:

1. sampling;
2. metrics;
3. judge use;
4. human review;
5. canary;
6. rollback triggers;
7. feedback loop.

## Takeaway

> Production is where the real task distribution reveals itself.

Next: **08 — Cost, Latency and Outcome Economics**.
