# 04 — State Machines

## Purpose

State machines make workflow behaviour explicit. They define which states are valid, which transitions are allowed, what events cause transitions, and what the system must do when a transition fails.

## Core principle

> If a business process has meaningful states, model those states explicitly rather than allowing them to emerge accidentally from scattered flags, timestamps, and side effects.

## 1. State machine fundamentals

A state machine consists of:

- states;
- events;
- transitions;
- guards / conditions;
- actions;
- terminal states.

Example:

```text
CREATED
   ↓ start
RUNNING
   ↓ complete
COMPLETED
```

Alternative transitions might include:

```text
RUNNING → FAILED
RUNNING → CANCELLED
FAILED  → RETRYING
RETRYING → RUNNING
```

## 2. Why explicit states matter

Without explicit state, systems often infer status from:

- nullable columns;
- timestamps;
- queue presence;
- log messages;
- partially written records.

This produces ambiguity.

A single authoritative state makes operational behaviour easier to understand, test and audit.

## 3. Valid transitions

Not every state should transition to every other state.

```text
CREATED → RUNNING
RUNNING → COMPLETED
RUNNING → FAILED
FAILED → RETRYING
RETRYING → RUNNING
```

An invalid transition such as:

```text
COMPLETED → RUNNING
```

should be rejected unless the domain explicitly defines a reopening operation.

## 4. Guards

A transition can require conditions.

```text
READY
  ↓ execute
[permission valid?]
  ↓ yes
EXECUTING
```

Guards are particularly important for AI systems where a model recommendation must satisfy deterministic business rules before execution.

## 5. Events vs states

A state describes **where the process is**.

An event describes **what happened**.

Example:

```text
State: WAITING_APPROVAL
Event: APPROVAL_GRANTED
Transition: WAITING_APPROVAL → APPROVED
```

Do not use event names as if they were persistent states unless the domain requires that representation.

## 6. State ownership

Each workflow should have a clear authoritative owner for its state.

Distributed systems may receive duplicate or out-of-order events, so consumers should validate whether an incoming event is legal for the current state.

## 7. Idempotent transitions

A repeated event should not accidentally repeat an irreversible side effect.

For example:

```text
APPROVED
   ↓ EXECUTE
EXECUTING
```

If `EXECUTE` is delivered twice, the system should recognise the existing transition or use an idempotency mechanism rather than executing the external action twice.

## 8. State persistence

For long-running workflows, state should be durable.

Persist enough information to reconstruct:

- current state;
- transition history;
- initiating event;
- actor / service identity;
- timestamps;
- relevant identifiers;
- failure information.

## 9. State history and audit

For high-value workflows, storing only the current state may be insufficient.

A transition history can provide:

```text
State A
  ↓ event X
State B
  ↓ event Y
State C
```

This supports debugging, compliance and incident investigation.

## 10. AI workflow states

AI workflows can use explicit states such as:

```text
REQUESTED
   ↓
CONTEXT_LOADING
   ↓
REASONING
   ↓
VALIDATING
   ↓
AWAITING_APPROVAL
   ↓
EXECUTING
   ↓
VERIFYING
   ↓
COMPLETED
```

Failure paths should be explicit:

```text
REASONING → FAILED
VALIDATING → REJECTED
EXECUTING → EXECUTION_FAILED
VERIFYING → VERIFICATION_FAILED
```

This prevents the system from treating an uncertain AI outcome as successful completion.

## 11. Human approval

Human approval should be represented as a real state when it is part of the business process.

```text
AI_RECOMMENDED
      ↓
AWAITING_APPROVAL
      ↓ approve
APPROVED
      ↓
EXECUTING
```

The approval should identify the actor and the decision timestamp.

## 12. Timeouts

States that can wait indefinitely should have explicit timeout policies.

Example:

```text
AWAITING_APPROVAL
      ↓ timeout
EXPIRED
```

Timeout behaviour should be deterministic and auditable.

## 13. Compensation

A state machine can represent compensation after partial failure.

```text
EXECUTING
   ↓ partial success
PARTIALLY_COMPLETED
   ↓ compensate
COMPENSATING
   ↓
COMPENSATED
```

Do not claim a distributed operation is atomic when external systems cannot provide that guarantee.

## 14. State-machine testing

Test at least:

- every valid transition;
- every invalid transition;
- guard failures;
- duplicate events;
- out-of-order events where relevant;
- timeout behaviour;
- retry behaviour;
- cancellation;
- crash/recovery;
- terminal-state protection.

Property-based testing can also be useful for complex state graphs.

## 15. SEMLIS application

SEMLIS can use explicit states for synchronisation and AI decision workflows.

Example marketplace sync:

```text
REQUESTED
   ↓
QUEUED
   ↓
FETCHING
   ↓
NORMALISING
   ↓
PERSISTING
   ↓
COMPLETED
```

Example AI action:

```text
DETECTED
   ↓
ANALYSING
   ↓
RECOMMENDED
   ↓
AWAITING_APPROVAL
   ↓
APPROVED
   ↓
EXECUTING
   ↓
VERIFIED
```

The important architectural separation is:

```text
AI decides / recommends
        ↓
State machine controls lifecycle
        ↓
Domain rules control validity
        ↓
Execution layer changes external state
```

## 16. Enterprise checklist

For every important workflow, ask:

1. What are the authoritative states?
2. What events cause transitions?
3. Which transitions are legal?
4. What guards are required?
5. Who owns state?
6. Are transitions durable?
7. Can duplicate events be handled safely?
8. What happens after failure?
9. What happens after timeout?
10. Can an operator reconstruct the history?
11. Which states are terminal?
12. Can an AI component bypass the state machine?

## Takeaway

> State machines turn implicit workflow behaviour into explicit, testable and auditable system behaviour.

For AI systems, they provide a deterministic lifecycle around probabilistic reasoning and prevent “the model said so” from becoming an uncontrolled state transition.
