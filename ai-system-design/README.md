# Domain 12 — AI System Design

## Learning objectives

By the end of this domain, you should be able to:

- explain the core concepts and distinctions across service boundaries, synchronous and asynchronous execution, queues, state machines, fault tolerance, caching, idempotency and scalability.
- build or evaluate a representative implementation rather than relying on a demo;
- make architecture decisions that account for reliability, security, cost, scale and operations;
- define the evidence, evaluation and governance required before production adoption.

## Purpose

AI system design is the discipline of turning probabilistic model capabilities into reliable production systems. The architect must decide where probabilistic reasoning belongs, where deterministic software must enforce invariants, how work is executed, how state is maintained, and how failures are contained.

## Core principle

> Put probabilistic capability inside deterministic system boundaries wherever correctness, permissions, money, or irreversible state matters.

AI systems should be designed as complete socio-technical systems rather than model calls.

## Domain map

This domain will cover:

1. Service boundaries
2. Synchronous vs asynchronous execution
3. Queues and workflow engines
4. State machines
5. Fault tolerance
6. Caching
7. Idempotency
8. Scalability
9. Graceful degradation
10. AI-specific architecture trade-offs
11. System design capstone

## Reference architecture

```text
                 User / Event
                      |
                      v
               API / Entry Point
                      |
                Orchestrator
               /      |      \
              v       v       v
         Retrieval   Model    Tools
              \       |       /
               \      v      /
                 Validation
                      |
                Policy / Rules
                      |
                State / Workflow
                      |
              Business Systems
                      |
                   Events
                      |
             Evaluation / Metrics
```

The exact boundaries depend on workload, risk, latency, and consistency requirements.

## Architectural questions

For every AI workflow, determine:

- What starts the workflow?
- What must happen synchronously?
- What can be queued?
- What state must survive retries?
- Which operations are idempotent?
- What happens if the model is unavailable?
- What happens if a tool times out?
- Where are business invariants enforced?
- What can be safely retried?
- What requires human intervention?
- How is the final outcome measured?

## What completion means

A learner should be able to take an AI workload and produce a production architecture with explicit boundaries, state, failure modes, scaling strategy, observability, and recovery behaviour.

The following chapters will build that capability progressively.

## Canonical curriculum navigation

- [Service Boundaries](./01-service-boundaries.md)
- [Synchronous vs Asynchronous Execution](./02-synchronous-vs-asynchronous-execution.md)
- [Queues and Workflow Engines](./03-queues-and-workflow-engines.md)
- [State Machines](./04-state-machines.md)
- [Fault Tolerance](./05-fault-tolerance.md)
- [Caching](./06-caching.md)
- [Idempotency](./07-idempotency.md)
- [Scalability](./08-scalability.md)
- [Graceful Degradation](./09-graceful-degradation.md)
- [AI Architecture Trade-offs](./10-ai-architecture-trade-offs.md)
- [System Design Capstone](./11-system-design-capstone.md)
