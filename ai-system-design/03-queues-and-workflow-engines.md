# 03 — Queues and Workflow Engines

## Purpose

Queues and workflow engines provide the execution backbone for reliable asynchronous AI systems. They solve different problems: a queue manages work delivery, while a workflow engine manages the state and lifecycle of a multi-step process.

## Core principle

> Use a queue to move work; use a workflow abstraction to manage durable business process state.

## 1. Queue fundamentals

A queue decouples producers from workers.

```text
Producer
   ↓
 Queue
   ↓
Worker(s)
```

Benefits include:

- burst absorption;
- concurrency control;
- retry handling;
- workload isolation;
- horizontal worker scaling.

## 2. Queue is not a workflow

A queue answers:

> What work should a worker process next?

A workflow answers:

> What state is this business process in, what happens next, and how do we recover?

Example:

```text
Queue:
"Analyse SKU 123"
```

Workflow:

```text
Sync data
 ↓
Validate
 ↓
Analyse
 ↓
Generate recommendation
 ↓
Approve
 ↓
Execute
 ↓
Verify
```

## 3. Delivery semantics

Architects should understand that distributed delivery commonly involves at-least-once processing. Therefore workers should be designed for safe retries.

Do not assume that a message is processed exactly once merely because the queue API appears simple.

## 4. Durable jobs

A production job should have enough persisted state to determine:

- what was requested;
- who/which tenant requested it;
- current status;
- attempt count;
- timestamps;
- last checkpoint;
- result or error;
- correlation/idempotency identifiers.

## 5. Retries

Retry only when failure is plausibly transient.

```text
Transient failure → retry with backoff
Permanent failure → record and escalate
Unknown failure   → bounded retry + investigation
```

Use exponential backoff and jitter where appropriate to avoid retry storms.

## 6. Dead-letter handling

Repeatedly failing work should not remain in an endless retry loop.

```text
Queue
 ↓
Retry
 ↓
Retry limit
 ↓
Dead-letter / failed state
 ↓
Operator or automated recovery
```

Dead-letter queues are operational safety mechanisms, not places where failures disappear.

## 7. Concurrency

Worker concurrency must respect:

- database capacity;
- external API limits;
- model-provider limits;
- memory/CPU;
- tenant fairness;
- downstream transaction capacity.

More workers can make a system less reliable if the bottleneck is downstream.

## 8. Fairness and isolation

A single large tenant or runaway workflow should not consume all capacity.

Useful controls include:

- per-tenant quotas;
- priority queues;
- concurrency limits;
- rate limits;
- workload classes.

## 9. Workflow state

Long-running workflows should make state explicit.

```text
CREATED
  ↓
RUNNING
  ↓
WAITING
  ↓
RUNNING
  ↓
COMPLETED
```

Failure and cancellation states should also be explicit rather than inferred from missing records.

## 10. Checkpointing

Long workflows should persist meaningful progress.

For example:

```text
Step 1 complete → checkpoint
Step 2 complete → checkpoint
Step 3 failed
       ↓
resume from safe boundary
```

Do not blindly replay expensive or irreversible steps.

## 11. Scheduling

Scheduled work should create durable jobs rather than relying on an in-process timer remaining alive.

Examples:

- nightly marketplace synchronisation;
- daily forecasting;
- periodic anomaly scans;
- token renewal;
- report generation.

Scheduling determines **when work is created**. The queue/workflow system determines **how that work executes reliably**.

## 12. Workflow orchestration

A workflow engine becomes useful when a process contains:

- multiple dependent steps;
- waits for external events;
- retries;
- timers;
- compensation;
- human approvals;
- long execution periods.

Avoid introducing a workflow engine for a single simple queue job.

## 13. Compensation and irreversible actions

Distributed transactions often cannot be rolled back globally.

Instead, workflows may use compensating actions.

```text
Create marketplace change
       ↓
External confirmation fails
       ↓
Compensating action / manual review
```

For irreversible actions, require stronger validation before execution rather than assuming rollback will always be possible.

## 14. AI agent workflows

Agentic systems should have explicit execution budgets:

- maximum steps;
- maximum elapsed time;
- maximum tool calls;
- maximum cost;
- permitted tools;
- escalation conditions.

```text
Agent
 ↓
Workflow boundary
 ↓
Policy
 ↓
Tool call
 ↓
Checkpoint
```

This turns an open-ended agent loop into a governed workflow.

## 15. Observability

Every job/workflow should be traceable using correlation identifiers.

Operators should be able to see:

```text
Tenant
 → Workflow
   → Job
     → Attempt
       → Tool/API call
         → Outcome
```

This is essential for diagnosing production AI behaviour.

## 16. SEMLIS application

SEMLIS already relies on queues and scheduled processing. The architectural goal should be to make those workloads durable, observable and tenant-aware.

Example:

```text
Scheduled sync
      ↓
Create workflow
      ↓
Queue marketplace job
      ↓
Fetch pages / batches
      ↓
Persist checkpoint
      ↓
Normalise data
      ↓
Emit domain event
      ↓
Run intelligence workflow
      ↓
Store recommendation
```

A failure in one marketplace integration should not invalidate unrelated tenant work.

## 17. Enterprise checklist

For every important asynchronous workflow, answer:

1. What creates the work?
2. Where is state persisted?
3. What is the delivery semantic?
4. Is processing idempotent?
5. Which errors are retryable?
6. What is the retry limit?
7. Where do permanently failed jobs go?
8. What is the concurrency limit?
9. Can work resume from a checkpoint?
10. How is tenant isolation enforced?
11. How is the workflow observed and audited?
12. What happens if a dependency is unavailable for hours?

## Takeaway

> Queues provide controlled work distribution; workflow engines provide durable process orchestration.

The right architecture uses the simplest mechanism that provides the reliability and state management the business actually requires.
