# 05 — Rules, Hooks and Lifecycle Controls

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **05 — Rules, Hooks and Lifecycle Controls** within Skills and Agent Harnesses;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Rules, hooks and lifecycle controls let an agent harness apply deterministic behaviour around probabilistic reasoning.

They provide predictable intervention points before, during and after model-driven execution.

## Core Principle

> Important controls should be enforced by the system, not remembered by the model.

## Rules

Rules define conditions the system must enforce.

Examples include:

- deny a prohibited operation;
- require approval above a threshold;
- restrict available tools;
- require evidence before completion;
- stop after a retry limit;
- reject invalid output.

Rules can be evaluated independently of the model.

## Hooks

Hooks are defined intervention points in the execution lifecycle.

Common examples include:

- before execution;
- before model invocation;
- after model response;
- before tool execution;
- after tool execution;
- before state mutation;
- before completion;
- on error;
- on escalation.

Hooks allow cross-cutting controls to be added without embedding every concern inside every skill.

## Lifecycle

A generic lifecycle can be represented as:

```text
Receive
  |
Validate
  |
Authorise
  |
Prepare
  |
Reason
  |
Propose
  |
Validate
  |
Act
  |
Observe
  |
Evaluate
  |
Complete / Escalate
```

Each transition is an opportunity for deterministic control.

## Preconditions and Postconditions

Preconditions determine whether an operation may begin.

Postconditions determine whether its result can be accepted.

This enables explicit gates around model-generated behaviour.

## Time, Cost and Step Limits

Agentic execution can become unbounded unless the harness imposes limits.

Useful limits include:

- maximum steps;
- maximum retries;
- timeouts;
- token budgets;
- monetary budgets;
- tool-call limits.

Limits should fail safely rather than silently truncating consequential work.

## Approval Hooks

Some actions should pause for approval.

An approval hook can capture:

- proposed action;
- affected resource;
- expected consequence;
- evidence;
- requester;
- policy reason;
- approval decision.

Approval design is expanded in Domain 11.

## Idempotency and Re-entry

Lifecycle design should account for retries and interrupted execution.

Where an action may be repeated, the system should consider whether it is idempotent or requires a deduplication strategy.

This matters especially for external side effects.

## Error Hooks

Errors should produce structured handling rather than uncontrolled loops.

An error hook can decide whether to:

- retry;
- change strategy;
- use a fallback;
- escalate;
- terminate.

The model can help diagnose an error, but retry authority should remain bounded.

## Cross-Cutting Concerns

Hooks are useful for concerns such as:

- policy enforcement;
- telemetry;
- validation;
- cost accounting;
- redaction;
- approvals;
- audit logging.

The goal is not to create a maze of callbacks. Lifecycle controls should remain explicit and observable.

## Anti-Pattern: Prompt-Only Control

Telling a model "never do X" can be useful instruction, but it is not equivalent to system enforcement.

Where a requirement matters operationally, enforce it outside the model when possible.

## Exercise

Take a generic action-producing skill and define hooks for:

1. request validation;
2. context preparation;
3. pre-tool authorisation;
4. post-tool validation;
5. error handling;
6. approval;
7. completion.

Classify each hook as advisory, validating or enforcing.

## Takeaway

> Lifecycle controls turn policy and reliability requirements into enforceable execution boundaries.

Next: **06 — Skill Composition and Discovery**.
