# 05 — Event-Driven and Long-Running Orchestration

## Purpose

Some AI work lasts longer than one request, one process or one context window.

Long-running orchestration requires durable state and explicit events.

## Core Principle

> Long-running work needs durable progress outside the model context.

## Why Long-Running Work Is Different

Long tasks can encounter:

- process restarts;
- context limits;
- credential expiry;
- human delay;
- external system delay;
- deployment changes;
- partial completion.

A chat transcript is not sufficient durability.

## Durable Workflow

A durable workflow persists:

- current state;
- completed steps;
- pending steps;
- external side effects;
- retries;
- approvals;
- checkpoints.

## Event-Driven Coordination

An event represents something that happened.

Examples:

- task.created;
- analysis.completed;
- approval.granted;
- tool.failed;
- workflow.cancelled.

Events can trigger orchestration transitions.

## Commands vs Events

A command requests an action.

An event reports that something occurred.

Example:

```text
Command: GenerateReport
Event: ReportGenerated
```

Confusing them makes recovery harder.

## Queues

Queues decouple producers and workers.

They help with:

- background execution;
- retries;
- load smoothing;
- worker scaling.

Queue delivery semantics do not remove the need for idempotency.

## Idempotency

A long-running workflow may receive duplicate deliveries.

Actions should have:

- idempotency key;
- deduplication;
- safe retry strategy.

Especially important for writes.

## Checkpointing

An agent crossing context windows should leave durable artefacts.

Useful checkpoint content includes:

- completed work;
- remaining work;
- key decisions;
- evidence;
- unresolved issues;
- current environment state.

The next execution can resume from evidence rather than reconstruct from memory.

## Human Wait States

Some workflows pause for human input.

A wait state should persist:

- what is needed;
- who can provide it;
- deadline;
- workflow context;
- resume transition.

Do not keep compute resources busy while waiting unnecessarily.

## External Wait States

Examples:

- asynchronous job;
- external approval;
- file upload;
- third-party callback.

Represent the wait explicitly.

## Timers

Durable timers support:

- deadline;
- retry delay;
- escalation;
- inactivity timeout.

Timers should survive process restart.

## Recovery

After restart, the orchestrator should determine:

- current state;
- completed side effects;
- pending operations;
- safe next step.

## Versioning

A long-running workflow can span software releases.

Decide whether in-flight work:

- stays on original workflow version;
- migrates;
- restarts.

Silent migration can be dangerous.

## Exercise

Design a 24-hour workflow that:

- starts from a user request;
- performs research;
- waits for approval;
- triggers an external action;
- handles a restart;
- resumes safely.

## Takeaway

> Long-running agents need workflow durability, not just longer context windows.

Next: **06 — Validation, Consensus and Recovery**.
