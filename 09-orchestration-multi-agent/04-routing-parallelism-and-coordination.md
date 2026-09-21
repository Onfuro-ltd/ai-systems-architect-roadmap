# 04 — Routing, Parallelism and Coordination

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **04 — Routing, Parallelism and Coordination** within Orchestration and Multi-Agent Systems;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Routing chooses who should handle work.

Parallelism allows independent work to happen concurrently.

Coordination ensures the pieces can be combined safely.

## Core Principle

> Parallelise independent work; coordinate only where dependencies require it.

## Routing

A router maps an input to an appropriate capability.

Routing can be:

- rule-based;
- classifier-based;
- model-based;
- hybrid.

Example:

```text
Request
  |
Router
  |
  +-- Billing
  +-- Technical
  +-- General
```

## Routing Quality

A routing failure can invalidate an otherwise capable system.

Evaluate:

- classification accuracy;
- fallback behaviour;
- unknown-category handling;
- confidence;
- cost.

## Parallel Sectioning

Sectioning splits a task into independent pieces.

Example:

```text
Document Set
   |
   +-- Worker A: documents 1-10
   +-- Worker B: documents 11-20
   +-- Worker C: documents 21-30
   |
Merge
```

This can reduce latency.

## Parallel Perspectives

Workers can analyse the same input from different perspectives.

Example:

- factual accuracy;
- security;
- compliance;
- usability.

This is useful when different criteria deserve focused attention.

## Voting

Multiple agents can independently answer the same question and a system aggregates results.

Voting can improve some decisions, but it is not automatically truth.

Correlated model errors can produce confident consensus.

## Consensus

Consensus mechanisms may include:

- majority vote;
- weighted vote;
- confidence;
- rule-based arbitration;
- human review.

Choose according to the error cost.

## Fan-Out / Fan-In

A common pattern is:

```text
        +-> Worker A -+
Input --+-> Worker B -+-> Aggregator -> Output
        +-> Worker C -+
```

The fan-in step needs:

- deduplication;
- ordering;
- conflict handling;
- completeness checks.

## Dependency Graph

Some tasks form a directed acyclic graph.

Example:

```text
A -> B -> D
 \-> C -/
```

A DAG scheduler can run B and C in parallel after A, then D after both complete.

## Concurrency Limits

Parallel execution should have limits.

Control:

- worker count;
- tool concurrency;
- API rate limits;
- cost;
- memory;
- downstream load.

## Backpressure

If downstream systems cannot keep up, orchestration should slow or queue work rather than overwhelm dependencies.

## Stragglers

One slow worker can delay the entire fan-in.

Strategies include:

- timeout;
- partial completion;
- replacement worker;
- speculative duplicate;
- degraded output.

The choice depends on task criticality.

## Cancellation

When the parent task is cancelled, child tasks should not continue indefinitely.

Propagate cancellation where appropriate.

## Exercise

Design an orchestration graph for analysing 100 independent records and producing one summary.

Include:

- partitioning;
- concurrency;
- retries;
- straggler policy;
- fan-in;
- validation.

## Takeaway

> Parallelism is valuable when work is independent; otherwise it turns dependencies into race conditions.

Next: **05 — Event-Driven and Long-Running Orchestration**.
