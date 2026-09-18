# 04 — Durable Workflows, State and Orchestration

## Purpose

Run business processes reliably across minutes, days, failures and human waits.

## Durable state

Persist workflow identity, current state, completed steps, external references, approvals, attempts, timestamps and outcome.

Model conversation is not a workflow database.

## State machine

```text
RECEIVED
 → VALIDATED
 → PROCESSING
 → AWAITING_APPROVAL
 → EXECUTING
 → VERIFYING
 → COMPLETED
```

Also define FAILED, CANCELLED and UNKNOWN.

## Orchestration

Use queues/workflow engines/schedulers appropriate to the workload for retries, timers, callbacks, parallel work and long waits.

## Correlation

Carry stable workflow and business identifiers through events, tools and external actions.

## Time

Business processes may have deadlines, cutoffs, waiting periods and escalation timers. Model these explicitly.

## Concurrency

Protect shared records from duplicate workers and conflicting state transitions.

## Exercise

Design a durable workflow that waits up to 48 hours for human approval and survives worker/server restarts.

## Takeaway

> Business automation becomes dependable when workflow state survives the process that is currently executing it.

Next: **05 — Tool-Enabled Automation and System Actions**.
