# 02 — Synchronous vs Asynchronous Execution

## Purpose

Execution strategy is a fundamental system-design decision. AI workloads vary greatly in latency, cost, reliability and duration, so treating every operation as a synchronous request creates fragile systems.

## Core principle

> Keep interactive work bounded and responsive; move long, expensive, retryable or externally dependent work into durable asynchronous workflows.

## 1. Synchronous execution

The caller waits for the result.

```text
Request
  ↓
Service
  ↓
Bounded operation
  ↓
Response
```

Good for:

- authentication;
- simple reads;
- short deterministic calculations;
- interactive AI responses with predictable latency;
- validation required before returning a response.

Risks:

- request timeouts;
- connection exhaustion;
- cascading latency;
- poor resilience to slow providers.

## 2. Asynchronous execution

The caller submits work and the system completes it independently.

```text
Request
  ↓
Create Job
  ↓
Queue
  ↓
Worker
  ↓
Result / Event
```

Good for:

- long AI analysis;
- batch processing;
- document ingestion;
- marketplace synchronisation;
- large-scale embedding;
- scheduled intelligence;
- external API workflows;
- retryable work.

## 3. Do not confuse async with background threads

A production asynchronous architecture needs durable state and recovery.

A useful model is:

```text
Intent
 ↓
Durable Job Record
 ↓
Queue
 ↓
Worker
 ↓
Checkpoint / Result
 ↓
Event
```

An in-memory background task is not equivalent to a durable workflow.

## 4. Choosing the boundary

Ask:

1. Does the user need the result immediately?
2. Can the work reliably finish within the request budget?
3. Can it be retried safely?
4. Is the workload bursty?
5. Does it depend on external systems?
6. Can partial progress be persisted?
7. What happens if the worker crashes?

If the work is long-running or failure-prone, asynchronous execution is usually safer.

## 5. Hybrid request patterns

Many AI applications use a hybrid model.

```text
User Request
    ↓
Fast validation
    ↓
Create workflow
    ↓
Return job/status
    ↓
Async processing
    ↓
Notify / poll / stream result
```

This preserves responsive UX without forcing the entire workflow into one HTTP request.

## 6. Streaming is not asynchronous execution

Streaming can improve perceived latency while the caller remains connected to the operation.

```text
Synchronous streaming:
Request → connected model operation → streamed tokens
```

This is different from:

```text
Asynchronous:
Request → durable job → disconnect → worker → result
```

A system may use both.

## 7. AI-specific considerations

AI workloads can have unpredictable latency because of:

- model queueing;
- provider rate limits;
- tool calls;
- retrieval;
- multi-step agent loops;
- retries;
- large contexts.

Therefore, agent workflows should normally have explicit:

- time budgets;
- step limits;
- retry limits;
- cancellation;
- checkpoints;
- status transitions.

## 8. Marketplace integration example

Do not make a customer-facing request wait for an entire marketplace synchronisation.

Prefer:

```text
User requests sync
      ↓
Create sync job
      ↓
Queue
      ↓
Integration worker
      ↓
Amazon / eBay / Shopify
      ↓
Persist normalised data
      ↓
Emit event
      ↓
Trigger downstream intelligence
```

This isolates external API latency from the interactive application.

## 9. Idempotency and retries

Asynchronous systems retry. Therefore operations must be designed so a retry does not accidentally duplicate a business action.

```text
Job ID / Idempotency Key
          ↓
Check prior execution
          ↓
Execute if required
          ↓
Persist outcome
```

Idempotency becomes especially important when AI agents can invoke external tools.

## 10. Backpressure

If work arrives faster than workers can process it, queues grow.

A mature system needs:

- queue limits;
- concurrency controls;
- rate limiting;
- prioritisation;
- admission control;
- monitoring.

Never assume adding workers indefinitely solves the problem; external APIs and databases often become the bottleneck.

## 11. Priority classes

Not all AI work has equal urgency.

Example:

```text
P0 — security / critical operational action
P1 — customer-facing workflow
P2 — normal intelligence
P3 — batch / enrichment
```

Priority should be explicit rather than emerging accidentally from queue timing.

## 12. SEMLIS application

SEMLIS should distinguish interactive and background workloads.

Interactive:

- dashboard queries;
- bounded explanations;
- quick recommendations.

Asynchronous:

- marketplace synchronisation;
- catalogue analysis;
- large-scale anomaly detection;
- scheduled forecasting;
- agent workflows;
- bulk listing analysis;
- historical recomputation.

A useful pattern is:

```text
SEMLIS UI
   ↓
Application API
   ↓
Command / Query decision
   ├── Query → immediate result
   └── Command → durable job
                     ↓
                  Queue
                     ↓
                  Worker
                     ↓
              Domain events
                     ↓
              AI / analytics
```

## 13. Operational requirements

Every asynchronous workflow should expose enough state to answer:

- What is running?
- What is waiting?
- What failed?
- Why did it fail?
- How many retries occurred?
- What was the last successful checkpoint?
- Can it safely be resumed?
- What customer/tenant is affected?

This is essential for enterprise observability.

## Takeaway

> Synchronous execution is a user-interaction mechanism; asynchronous execution is a reliability and workload-management mechanism.

Good AI architecture deliberately chooses between them rather than defaulting to either one.
