# Domain 10 — Evaluation and Reliability

## Purpose

This domain explains how to measure whether AI systems behave acceptably, detect regressions, diagnose failures and improve reliability over time.

The goal is not to collect benchmark scores for their own sake.

The goal is to build evidence that a system performs the work it is intended to perform, under realistic operating conditions, at acceptable cost and risk.

## Core Principle

> Evaluate the system you operate, not only the model you selected.

Modern AI applications combine:

- models;
- prompts;
- context;
- retrieval;
- memory;
- tools;
- orchestration;
- policies;
- human review;
- external systems.

A model benchmark cannot prove that the complete application is reliable.

## Evaluation Loop

```text
Define Intended Behaviour
        |
Build Task Suite
        |
Run System
        |
Measure Outcomes
        |
Classify Failures
        |
Improve
        |
Regression Test
        |
Production Monitor
```

Evaluation is an engineering loop, not a one-time gate.

## What This Domain Covers

1. Evaluation foundations
2. Task suites, golden datasets and holdouts
3. Deterministic and behavioural evaluation
4. Human evaluation and model judges
5. Agent, tool and workflow evaluation
6. Reliability, regression and failure analysis
7. Production evaluation and monitoring
8. Cost, latency and outcome economics
9. Capstone architecture

## Evaluation Levels

A useful evaluation stack is:

```text
Component
  |
Capability
  |
Workflow / Agent
  |
End-to-End System
  |
Production Outcome
```

A system can pass one level and fail another.

## Reliability

Reliability means more than average quality.

It includes questions such as:

- Does the system fail safely?
- Does it recover correctly?
- Does it remain stable across model changes?
- Does it handle edge cases?
- Does it select tools correctly?
- Does it preserve policy boundaries?
- Does it know when to escalate?

## Evidence Types

Evidence can include:

- deterministic assertions;
- task success;
- behavioural rubrics;
- human judgement;
- model-based grading;
- trace evaluation;
- production metrics;
- business outcomes.

No single evaluator is sufficient for every problem.

## Domain Boundaries

- **Domain 06 — Skills and Agent Harnesses:** defines capability-level contracts and local quality gates.
- **Domain 09 — Orchestration and Multi-Agent Systems:** coordinates workflows and agents.
- **Domain 11 — Security, Permissions and Governance:** defines security and policy requirements.
- **Domain 17 — MLOps and LLMOps:** operationalises evaluations in release and deployment pipelines.

This domain focuses on evaluation design and reliability science: what to evaluate, how to evaluate it and how to reason about failures.

## Mastery Outcomes

### Understand

Explain offline vs online evaluation, exact vs behavioural checks, human evaluation, model judges, regression and production monitoring.

### Build

Create representative task suites, evaluators, failure taxonomies and quality gates.

### Architect

Design end-to-end evaluation for models, tools, agents and workflows using multiple evidence sources.

### Lead

Define organisational standards for evaluation ownership, release gates, reliability targets, incident learning and outcome economics.

## Architectural Rule

> If a system can change behaviour, it needs evidence that the change is acceptable.

Next: **01 — Evaluation Foundations**.
