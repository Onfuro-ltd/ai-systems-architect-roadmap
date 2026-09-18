# 06 — Validation, Consensus and Recovery

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **06 — Validation, Consensus and Recovery** within Orchestration and Multi-Agent Systems;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Orchestrated systems need mechanisms to detect bad intermediate results and recover before errors propagate.

## Core Principle

> Validate at boundaries before downstream work amplifies an error.

## Boundary Validation

Validate when data crosses:

- worker to orchestrator;
- model to tool;
- tool to model;
- agent to agent;
- workflow stage to workflow stage.

## Deterministic Validation

Use deterministic checks for:

- schema;
- required fields;
- numeric constraints;
- file existence;
- test results;
- permissions.

## Model-Based Validation

Use model judgement when criteria are semantic.

Examples:

- completeness;
- argument quality;
- relevance;
- consistency.

Model-based validation should itself be evaluated.

## Independent Review

A reviewer can inspect a worker result without sharing the worker's reasoning process.

Independence can reduce some correlated errors.

It does not guarantee correctness.

## Evaluator-Optimizer Pattern

```text
Generator
   |
Draft
   |
Evaluator
   |
Feedback
   |
Generator
   |
Improved Draft
```

Use it when:

- evaluation criteria are clear;
- feedback can improve output;
- iteration cost is justified.

Set iteration limits.

## Consensus

Consensus can combine multiple independent attempts.

Possible methods:

- vote;
- score;
- rank;
- evidence-weighted synthesis;
- human decision.

Consensus should consider correlated failure.

## Recovery Levels

Recovery can occur at different scopes.

### Step Retry

Repeat one operation.

### Worker Replacement

Reassign one failed subtask.

### Branch Recompute

Re-run a dependent branch.

### Workflow Rollback

Undo reversible effects.

### Human Escalation

Stop automation and request judgement.

## Retry Safety

Before retrying, determine:

- did the action execute;
- is it idempotent;
- did partial state change;
- is the failure transient.

Retry is a state transition, not a default reflex.

## Compensation

Some workflows cannot truly roll back.

Use compensating actions.

Example:

```text
Create booking
   |
later failure
   |
Cancel booking
```

Compensation should be designed before production.

## Circuit Breaker

If a dependency repeatedly fails, stop sending more work temporarily.

This prevents cascading failure.

## Partial Success

A multi-agent task may complete some branches successfully.

The orchestrator can:

- return partial result;
- retry failed branches;
- degrade capability;
- escalate.

Do not discard valid work unnecessarily.

## Recovery Evidence

Record:

- failed component;
- input;
- error;
- attempts;
- side effects;
- recovery action;
- final outcome.

## Exercise

Design recovery for a three-worker workflow where one worker writes to an external system and another times out.

Define retry, compensation and escalation.

## Takeaway

> Reliability comes from detecting and containing failure before it spreads through the orchestration graph.

Next: **07 — Multi-Agent Failure Modes and Anti-Patterns**.
