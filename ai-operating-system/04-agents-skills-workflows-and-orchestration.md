# 04 — Agents, Skills, Workflows and Orchestration

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **04 — Agents, Skills, Workflows and Orchestration** within Build an AI Operating System;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Coordinate reasoning and deterministic execution without building an unbounded autonomous loop.

## Responsibility

Use agents for adaptive reasoning, skills for reusable procedures, durable workflows for stateful processes and deterministic services for exact operations.

## Orchestration

```text
Intent
 ↓
Task plan / workflow
 ↓
Bounded reasoning
 ↓
Skill invocation
 ↓
Tool proposal
 ↓
Policy / approval
 ↓
Execution
 ↓
Observation / verification
 ↓
Next state
```

## Durable state

Persist workflow progress, attempts, approvals and external references outside model context.

## Budgets

Bound time, model calls, tool calls, cost and recursion. A failed plan must terminate or escalate.

## Multi-agent

Add multiple agents only when role separation, specialization, parallelism or independent checking produces measured value.

## Deterministic boundaries

Agents do not own permissions, secrets, transaction truth or hard policy.

## Recovery

Support pause, resume, retry, compensation, cancellation and human takeover.

## Exercise

Design one workflow that uses an agent for investigation, a skill for procedure and a durable state machine for execution.

## Takeaway

> The orchestrator should make autonomy bounded, stateful and recoverable rather than merely giving a model more opportunities to call itself.

Next: **05 — Model Routing and Inference Plane**.
