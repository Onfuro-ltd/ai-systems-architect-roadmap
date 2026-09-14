# 11 — System Design Capstone

## Purpose

This capstone brings the entire AI System Design domain together. The goal is not to memorise individual patterns. It is to design one coherent system in which service boundaries, queues, state machines, failure handling, caching, idempotency, scaling, degradation, permissions, AI reasoning, observability, and recovery work together.

## Core principle

> Good system design is not the sum of isolated components. It is the quality of the boundaries, contracts, failure behaviour, and trade-offs between them.

---

## Capstone scenario

Design an enterprise-grade AI-assisted commerce operations platform for multiple organisations.

The platform connects to external marketplaces and business systems, ingests operational data, detects issues and opportunities, generates AI-assisted recommendations, optionally requires human approval, and executes authorised actions through deterministic integration services.

The platform must support:

- multiple tenants;
- external marketplace APIs;
- webhooks and scheduled synchronisation;
- long-running workflows;
- AI reasoning and recommendations;
- human approval for consequential actions;
- retries and duplicate delivery;
- partial external failure;
- queue backlogs;
- provider/model outages;
- high-volume tenants;
- auditability;
- cost control;
- safe degraded operation.

The platform must never allow model output alone to become an uncontrolled business action.

---

## 1. Start with business capabilities

Do not begin with microservices, queues, agents, or model providers.

Start with coherent capabilities.

Example:

```text
Identity & Tenancy
Integration Management
Commerce Data
Workflow Orchestration
Decision Intelligence
AI Reasoning
Policy & Permissions
Action Execution
Audit & Observability
```

Each capability should have clear responsibility and ownership.

---

## 2. High-level architecture

A possible logical architecture is:

```text
Users / External Webhooks / Schedulers
                 ↓
        API & Intake Layer
                 ↓
        Domain/Application Layer
                 ↓
        Durable Workflow Layer
          ↙       ↓       ↘
   Integration   AI     Analytics
     Workers   Workers    Workers
          \       |       /
          Decision / Policy Layer
                 ↓
         Approval Boundary
                 ↓
          Execution Layer
                 ↓
        External Platforms

Surrounding controls:
Security • Audit • Observability • Cost • Tenant Isolation
```

This is a logical model, not a requirement to deploy every box independently.

---

## 3. Choose service boundaries deliberately

For each capability, answer:

- what responsibility does it own?
- what data does it own?
- what failure domain does it create?
- what permissions does it require?
- does it genuinely need independent deployment/scaling?

A modular monolith may be the correct initial deployment while preserving these logical boundaries.

Do not split services merely to imitate large technology companies.

---

## 4. Separate probabilistic reasoning from deterministic control

The most important architecture boundary is:

```text
Probabilistic AI
      ↓
Recommendation / structured proposal
      ↓
Deterministic validation
      ↓
Policy
      ↓
Permission
      ↓
Approval where required
      ↓
Deterministic execution
```

The AI system can recommend an action.

It should not bypass domain rules, permission checks, state machines, or execution controls.

---

## 5. Define synchronous and asynchronous paths

Interactive work should stay bounded.

Example synchronous path:

```text
User request
   ↓
Authenticate
   ↓
Read authorised data
   ↓
Bounded computation
   ↓
Response
```

Long-running work becomes asynchronous:

```text
User / webhook / schedule
          ↓
Create durable workflow
          ↓
Queue
          ↓
Worker
          ↓
Checkpoint
          ↓
Continue / retry / complete
```

Do not hide long-running workflows inside an HTTP request.

---

## 6. Model important workflows as state machines

Example AI-assisted action lifecycle:

```text
DETECTED
   ↓
ANALYSING
   ↓
RECOMMENDED
   ↓
VALIDATING
   ↓
AWAITING_APPROVAL
   ↓
APPROVED
   ↓
EXECUTING
   ↓
VERIFYING
   ↓
COMPLETED
```

Failure states may include:

```text
ANALYSIS_FAILED
REJECTED
EXPIRED
EXECUTION_FAILED
OUTCOME_UNKNOWN
VERIFICATION_FAILED
```

Every transition should be explicit and testable.

---

## 7. Design for duplicate delivery

Assume:

- queue jobs can redeliver;
- webhooks can duplicate;
- users can repeat requests;
- schedulers can overlap;
- agents can retry tools;
- network responses can be lost.

For consequential operations:

```text
Logical intent
   ↓
Idempotency key
   ↓
Atomic claim
   ↓
Execute once
   ↓
Persist authoritative outcome
```

The expected result of retrying the same logical intent is one intended business effect.

---

## 8. Handle uncertain external outcomes

A timeout does not prove failure.

Example:

```text
Execution service
      ↓
External API
      ↓
Action succeeds
      ↓
Response lost
```

The correct state may be:

```text
OUTCOME_UNKNOWN
       ↓
Reconciliation
       ↓
Confirmed success / safe retry / escalation
```

Never blindly repeat an irreversible external action because the acknowledgement was lost.

---

## 9. Use queues as control surfaces

Queues should do more than move work.

They should help control:

- workload isolation;
- priority;
- concurrency;
- retry behaviour;
- backpressure;
- tenant fairness.

Example:

```text
Critical transactional queue
Interactive AI queue
Marketplace sync queue
Bulk analytics queue
Low-priority recomputation queue
```

Do not force all workloads into one global queue if they have materially different service objectives.

---

## 10. Add backpressure

Suppose incoming workload exceeds safe processing capacity.

Without control:

```text
More work
  ↓
Larger queue
  ↓
More workers
  ↓
Downstream throttling
  ↓
More retries
  ↓
Even larger queue
```

Instead use:

- admission control;
- bounded concurrency;
- tenant quotas;
- priority queues;
- deferred low-value work;
- load shedding.

The platform should protect critical workloads first.

---

## 11. Design caching around correctness

Useful candidates include:

- stable metadata;
- repeated expensive calculations;
- embeddings;
- retrieval artefacts;
- safe repeated AI explanations.

But cache keys may need to include:

```text
Tenant
Data version
Prompt version
Policy version
Model version
Permission context
```

Do not cache rapidly changing business state without an explicit freshness policy.

A fast stale answer can be worse than a slower correct answer.

---

## 12. Define fault-tolerance behaviour per dependency

For every dependency, specify:

```text
Timeout
Retry policy
Circuit breaker
Fallback
Recovery path
Observability
```

Example external API dependency:

```text
Call
 ↓ timeout
Bounded retry
 ↓ repeated failure
Circuit opens
 ↓
Workflow pauses/degrades
 ↓
Later recovery
```

Do not use unlimited retries.

---

## 13. Design graceful degradation explicitly

The system should have meaningful degradation levels.

Example:

```text
FULL SERVICE
    ↓
AI ENHANCEMENTS REDUCED
    ↓
BACKGROUND ANALYTICS DEFERRED
    ↓
READ-ONLY / STALE-SAFE MODE
    ↓
CRITICAL OPERATIONS ONLY
    ↓
SAFE REJECTION
```

Core deterministic workflows should not fail merely because one optional AI provider is unavailable.

---

## 14. Fail closed where safety requires it

Some failures should stop execution.

Examples:

- permission service unavailable;
- approval state uncertain;
- required financial data stale;
- identity cannot be verified;
- policy validation unavailable.

In those cases:

```text
Uncertain control state
        ↓
Do not execute
```

Availability does not outrank authority or correctness.

---

## 15. Define AI fallbacks carefully

A fallback model is useful only if it is sufficiently capable for the task.

Do not assume:

```text
Model B available
      =
Model B safe replacement
```

Evaluate fallback models on:

- task quality;
- structured-output reliability;
- tool-use reliability;
- policy behaviour;
- latency;
- cost.

For high-risk workflows, the correct fallback may be human review rather than another model.

---

## 16. Protect tenants from noisy neighbours

Each unit of work should carry tenant identity.

Use:

- per-tenant concurrency limits;
- fair queue scheduling;
- API quota isolation;
- model budget controls;
- workload accounting.

One tenant should not consume all workers, provider quota, database connections, or AI budget.

---

## 17. Scale the bottleneck

Measure end-to-end throughput.

```text
API
 ↓
Application
 ↓
Queue
 ↓
Workers
 ↓
Database
 ↓
External provider
```

If the provider limit is the bottleneck, adding workers will not improve useful throughput.

Capacity decisions should follow evidence.

---

## 18. Design observability before incidents

For every workflow, capture enough information to reconstruct what happened.

Useful dimensions include:

- tenant;
- workflow ID;
- correlation ID;
- state;
- queue;
- retry count;
- dependency;
- model/provider;
- prompt/policy version;
- actor;
- approval decision;
- idempotency key;
- external request identifier;
- latency;
- token usage;
- cost;
- final outcome.

Logs alone are not observability.

Use metrics, traces, workflow history, and audit records together.

---

## 19. Separate operational logs from audit history

Operational logs answer:

> Why did the system fail?

Audit history answers:

> Who or what caused this business action, under which policy and approval state?

For consequential operations, retain durable audit data even after ordinary logs expire.

---

## 20. Define recovery procedures

The architecture should support recovery after:

- worker crash;
- queue outage;
- provider outage;
- database failover;
- deployment interruption;
- external API uncertainty.

Use durable state and checkpoints so workflows can resume rather than restart blindly.

Recovery should be rehearsed, not merely documented.

---

## 21. Prevent recovery storms

When a dependency recovers, thousands of delayed tasks may become runnable at once.

Use:

- gradual concurrency increase;
- jitter;
- rate-aware replay;
- priority ordering;
- tenant fairness;
- controlled queue draining.

A recovering dependency should not immediately be overloaded again.

---

## 22. Make architecture decisions explicit

For major choices, record an Architecture Decision Record (ADR).

Example:

```text
Context
Decision
Alternatives considered
Trade-offs
Consequences
Review trigger
```

Useful ADRs might cover:

- modular monolith vs services;
- sync vs async processing;
- managed vs self-hosted models;
- model routing strategy;
- queue architecture;
- cache policy;
- human approval boundary;
- data consistency model.

Architecture should be explainable, not accidental.

---

## 23. Required capstone deliverables

Produce the following artefacts.

### A. System context diagram

Show:

- users;
- external systems;
- platform boundary;
- model providers;
- identity provider where relevant.

### B. Logical component diagram

Show:

- application/domain layer;
- workflow layer;
- queues;
- workers;
- AI layer;
- policy/permission layer;
- execution layer;
- authoritative data stores;
- audit/observability.

### C. Workflow state machine

Model one consequential AI-assisted action from detection through verification.

### D. Failure matrix

For each critical dependency, document:

```text
Failure mode
Detection
Timeout
Retry
Fallback
Degraded behaviour
Recovery
```

### E. Idempotency design

Define:

- logical intent;
- idempotency key;
- storage;
- retention;
- concurrency behaviour;
- uncertain-outcome handling.

### F. Scaling plan

Identify:

- expected workloads;
- current bottlenecks;
- scaling signals;
- tenant fairness;
- external provider constraints;
- cost limits.

### G. Degradation matrix

Define which capabilities remain available at each degradation level.

### H. Security and approval boundary

Show where:

- identity is verified;
- permissions are checked;
- policy is evaluated;
- human approval is required;
- execution is allowed.

### I. Observability plan

Define:

- metrics;
- traces;
- audit records;
- alerts;
- operator dashboards;
- correlation identifiers.

### J. Architecture Decision Records

Write at least three ADRs explaining important design choices.

---

## 24. Evaluation rubric

### Understand

Can explain:

- why each major component exists;
- why AI reasoning is separated from execution;
- why duplicate delivery is expected;
- why failures require explicit degraded states.

### Build

Can implement:

- a durable asynchronous workflow;
- explicit state transitions;
- idempotent execution;
- retries with backoff;
- cache freshness rules;
- failure-aware external integrations.

### Architect

Can justify:

- service boundaries;
- consistency choices;
- synchronous vs asynchronous paths;
- scaling strategy;
- fallback behaviour;
- human approval boundaries;
- recovery design.

### Lead

Can define:

- operational standards;
- reliability objectives;
- cost controls;
- audit requirements;
- architecture review criteria;
- incident/recovery expectations.

---

## 25. Failure exercises

The design should be tested against scenarios such as:

1. AI provider unavailable for 30 minutes.
2. External marketplace API returns intermittent 500 errors.
3. Queue worker crashes after an external action succeeds.
4. Duplicate webhook arrives three times.
5. One tenant produces 50× normal workload.
6. Database becomes slow but remains reachable.
7. Cache becomes unavailable.
8. Permission service cannot be reached.
9. Human approval backlog grows dramatically.
10. Model begins returning structurally valid but lower-quality recommendations.
11. External provider recovers after a long outage and thousands of jobs are queued.
12. A scheduled job accidentally runs concurrently on two scheduler instances.

For each scenario, explain:

```text
Detection
Containment
User-visible behaviour
State transition
Recovery
Audit evidence
```

---

## 26. Anti-pattern review

Reject designs that rely on assumptions such as:

- “The queue delivers exactly once.”
- “The webhook will not duplicate.”
- “The model returned 200, therefore the result is correct.”
- “The external timeout means the action failed.”
- “We can retry forever.”
- “More workers always means more throughput.”
- “The cache is close enough to the source of truth.”
- “Microservices automatically make the system scalable.”
- “The fallback model will behave the same.”
- “AI can decide whether it has permission to act.”

An enterprise architecture should make these assumptions unnecessary.

---

## 27. Final architecture principle

The capstone should ultimately preserve this control flow:

```text
Intent
  ↓
Authorised context
  ↓
AI / deterministic reasoning
  ↓
Structured proposal
  ↓
Validation
  ↓
Policy
  ↓
Permission
  ↓
Human approval when required
  ↓
Idempotent execution
  ↓
External outcome verification
  ↓
Audit
  ↓
Evaluation and learning
```

AI increases the intelligence available to the system.

It does not remove the need for deterministic control.

---

## Takeaway

> The defining skill of an AI systems architect is not knowing more patterns. It is knowing how to combine the right patterns into a system that remains correct, observable, recoverable, economical, and safe under real-world uncertainty.

A strong design assumes failures, duplicates, stale data, changing workloads, imperfect models, unavailable dependencies, and human intervention will all occur—and still preserves controlled business behaviour.
