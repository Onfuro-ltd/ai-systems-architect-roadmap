# 04 — Delivery, Ordering and Idempotent Consumers

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **04 — Delivery, Ordering and Idempotent Consumers** within Data and Event Architecture;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Event-driven systems must remain correct when messages are delayed, duplicated, retried, delivered out of order, or processed after a consumer restarts.

> Reliable event architecture does not depend on perfect delivery. It makes imperfect delivery safe.

## 1. Delivery is not business completion

A broker acknowledging a message means the infrastructure accepted or delivered something according to its contract. It does not prove that the intended business outcome occurred.

Keep these concepts separate:

```text
Event published
    ≠
Event delivered
    ≠
Event processed
    ≠
Business effect committed
    ≠
External outcome confirmed
```

Each boundary can fail independently.

## 2. Common delivery semantics

### At-most-once

A message is delivered zero or one time. Duplicates are avoided, but failures can cause loss.

### At-least-once

The system retries until acknowledgement or policy limits are reached. This reduces loss risk but means duplicates are normal.

### Exactly-once

"Exactly once" is meaningful only inside clearly defined boundaries. Infrastructure may provide transactional guarantees for specific operations, but end-to-end business effects—especially across databases and external APIs—still require careful design.

Do not use the phrase without stating exactly what is guaranteed and where.

## 3. Assume duplicates

In an at-least-once architecture:

```text
Consumer performs work
        ↓
Process crashes before acknowledgement
        ↓
Broker redelivers
        ↓
Same event arrives again
```

This is expected behaviour, not an exceptional edge case.

Consumers should therefore be designed so duplicate delivery does not create duplicate business effects.

## 4. Event identity

Every durable event should have a stable event identifier.

```text
event_id = identity of this occurrence
```

Do not generate a new event ID merely because the same stored event is retried. Otherwise the consumer cannot distinguish retry from a genuinely new event.

## 5. Idempotent consumers

An idempotent consumer can process the same logical event more than once without incorrectly repeating its business effect.

A simple pattern is:

```text
Receive event
    ↓
Check processed-event record
    ↓
Already processed? ── yes → acknowledge safely
    ↓ no
Apply business mutation
    ↓
Record event as processed
    ↓
Commit atomically
    ↓
Acknowledge
```

The business mutation and deduplication marker should normally share the same transactional boundary when possible.

## 6. Idempotency is about effects, not code execution

A handler may execute twice while the business effect occurs once.

That is acceptable.

The objective is not necessarily:

```text
function runs exactly once
```

It is:

```text
logical business effect occurs no more than intended
```

## 7. Natural idempotency

Some operations are naturally idempotent.

```text
set status = "approved"
```

may be safe to repeat if the transition rules permit it.

Other operations are not:

```text
increment balance by 10
send payment
create shipment
send customer notification
```

These require stronger controls.

## 8. Business idempotency keys

Sometimes event ID is not the right deduplication boundary.

A business action may be triggered through several paths or retried after a new event is created. Use a deterministic business idempotency key when the requirement is "perform this business operation once."

For example:

```text
tenant + order + operation + operation_version
```

The exact key must reflect business semantics.

## 9. Deduplication storage

Possible approaches include:

- a processed-events/inbox table;
- unique constraints on business operation keys;
- idempotency records;
- transactional state-machine transitions;
- broker-supported deduplication within a documented boundary.

Avoid relying only on short-lived in-memory caches for consequential deduplication.

## 10. Ordering is scoped, not global

Distributed systems rarely provide meaningful global ordering.

What usually matters is ordering within a business key:

```text
order A: event 1 → event 2 → event 3
order B: event 1 → event 2
```

Partitioning by aggregate or entity key can preserve useful local ordering while allowing parallelism across independent entities.

## 11. Out-of-order events

Even if a producer emits events in order, retries, network paths, partitions, consumer concurrency, and multiple producers can change observation order.

A consumer may see:

```text
ShipmentDispatched
        ↓
OrderApproved
```

even though approval happened first.

Design consumers to detect when order matters.

## 12. Sequence and version numbers

For entity state transitions, include a monotonic aggregate version or sequence when useful.

```text
order_id: O-42
version: 18
```

A projection that currently holds version 18 can identify version 17 as stale and version 20 as evidence that version 19 may be missing.

Sequence numbers help detect ordering problems; they do not automatically repair them.

## 13. Late events

A late event may still be valid.

Do not reject an event merely because its timestamp is old. Determine whether the consumer operates on:

- current state;
- historical facts;
- event-time windows;
- processing-time windows;
- an ordered state machine.

Analytics and AI features often care deeply about the distinction between event time and processing time.

## 14. Stale events

An event can be valid historically but obsolete for a current-state projection.

Example:

```text
Current entity version = 12
Incoming state event version = 9
```

The consumer may record the historical event while refusing to overwrite the newer current projection.

## 15. Missing events

If a consumer observes a sequence gap, possible strategies include:

- pause the entity partition;
- retry later;
- fetch authoritative current state;
- request replay;
- rebuild the projection;
- reconcile against the source of truth;
- quarantine for investigation.

The correct choice depends on consequence and whether intermediate history matters.

## 16. Poison messages

Some messages repeatedly fail because they are malformed, unsupported, semantically invalid, or trigger a deterministic bug.

Infinite retry loops waste capacity and can block healthy work.

Use bounded retries and a quarantine/dead-letter path with enough evidence to diagnose and safely replay.

## 17. Retry policy

Retry transient failures, not every failure.

A robust policy considers:

```text
failure classification
attempt count
backoff
jitter
maximum retry horizon
consumer capacity
dependency health
business deadline
```

Permanent schema or validation failures should not be hammered indefinitely.

## 18. Backpressure

If producers create work faster than consumers can safely process it, queue depth grows.

Measure more than queue length:

- oldest-message age;
- processing latency;
- throughput;
- retry rate;
- failure rate;
- consumer saturation;
- per-tenant backlog;
- dependency latency.

Autoscaling consumers without protecting downstream dependencies can amplify an outage.

## 19. Fairness and multi-tenancy

One noisy tenant should not indefinitely starve others.

Depending on architecture, use partitioning, quotas, weighted scheduling, concurrency limits, or separate queues for workloads with different priorities.

Tenant identity must remain available through retries, dead-letter handling, replay, and observability.

## 20. Consumer transaction boundary

A classic failure occurs when a consumer changes its database and then crashes before acknowledging the message.

If the broker retries, the database mutation may repeat.

Design the consumer around a clear atomic boundary:

```text
Begin transaction
  validate event
  check dedupe
  apply mutation
  record processed event
Commit
Acknowledge message
```

If acknowledgement fails, redelivery is safe because the committed dedupe record remains.

## 21. External side effects are harder

A local database transaction cannot atomically include an unrelated external API.

```text
Call external provider
        ↓
Provider succeeds
        ↓
Connection fails before response
        ↓
Outcome = UNKNOWN
```

Do not interpret timeout as failure.

Use provider-supported idempotency keys where available, persist intent, verify outcome, and reconcile before repeating consequential operations.

## 22. UNKNOWN is a legitimate state

Distributed workflows need more than SUCCESS and FAILED.

```text
PENDING
IN_PROGRESS
SUCCEEDED
FAILED
UNKNOWN
RECONCILING
```

When an external outcome cannot be established, moving to UNKNOWN and reconciling is safer than blindly retrying.

## 23. Idempotent notifications

Even "small" effects such as emails, webhooks, and alerts can become harmful when duplicated.

Give notification delivery its own durable identity and retry semantics where duplicates matter.

## 24. Reprocessing and replay

Replay intentionally redelivers old events. A consumer safe under normal retries may still be unsafe under large historical replay.

Before replay ask:

- Will external side effects fire again?
- Should historical notifications be suppressed?
- Are current permissions applied?
- Is the target a disposable projection?
- Are old schemas supported?
- Can live and replay traffic interfere?
- Can replay overload dependencies?

Prefer isolated replay modes for high-risk consumers.

## 25. AI consumers

AI makes duplicate and out-of-order handling more subtle because the same input may not produce byte-identical output across runs.

Do not use model determinism as an idempotency mechanism.

```text
Event
  ↓
Deterministic event/business identity
  ↓
Context/version capture
  ↓
AI reasoning
  ↓
Structured proposal
  ↓
Deterministic validation
  ↓
Idempotent business action
```

The business-effect boundary remains deterministic even when reasoning is probabilistic.

## 26. Duplicate AI work vs duplicate action

Repeated inference may waste money but repeated action can corrupt state.

Treat them separately:

```text
Inference dedupe → cost/performance concern
Action dedupe    → correctness/safety concern
```

For expensive inference, caching or job identity can reduce duplicate work. For consequential actions, durable idempotency is required regardless.

## 27. Eventual consistency

A system can be correct even when all views are not instantly identical.

The architecture must define:

- which state is authoritative;
- expected propagation delay;
- what consumers may do while stale;
- when reconciliation occurs;
- which decisions require a fresh read.

"Eventually consistent" should never mean "we do not know when the data becomes trustworthy."

## 28. Observability

For every important event flow, be able to answer:

```text
Was it published?
Was it delivered?
How many times?
Which consumer handled it?
What version was processed?
Was it rejected?
Was a business mutation committed?
Was an external action attempted?
What is its verified outcome?
Can we replay it safely?
```

Correlation IDs, event IDs, business IDs, tenant IDs, attempt numbers, and state transitions should connect the evidence.

## 29. Testing

Test failure paths deliberately:

1. duplicate the same event;
2. deliver events out of order;
3. omit one event;
4. delay an event;
5. crash after business commit but before acknowledgement;
6. fail an external call before response;
7. redeliver a dead-letter event;
8. replay historical events;
9. saturate a consumer;
10. create a noisy-tenant backlog.

Correctness under these conditions is part of the feature.

## 30. Anti-patterns

Avoid:

- assuming one delivery means one effect;
- using timestamps as unique event IDs;
- relying on global ordering;
- acknowledging before durable work is committed;
- retrying permanent failures forever;
- treating timeout as proof of external failure;
- using model output equality for deduplication;
- replaying directly into live side-effect consumers without controls;
- deduplicating consequential actions only in memory;
- scaling consumers without backpressure;
- allowing one tenant to monopolize worker capacity;
- claiming "exactly once" without defining the boundary.

## 31. Architect checklist

Before approving an event consumer, ask:

- What delivery guarantee does the transport actually provide?
- What is the event identity?
- What is the business-operation identity?
- Can duplicates occur?
- Is the business effect idempotent?
- Where is deduplication persisted?
- What ordering is required and at what scope?
- How are stale, late, missing, and out-of-order events handled?
- What happens after a crash between commit and acknowledgement?
- What happens when an external outcome is unknown?
- Are retries bounded and classified?
- Is there a dead-letter/quarantine process?
- Is replay safe?
- Is tenant fairness protected?
- Can the complete path be observed and audited?
- Are AI proposals separated from idempotent execution?

## 32. Exercise

Design a consumer for a generic event that may trigger a consequential external action.

Your design must survive:

- duplicate delivery;
- out-of-order delivery;
- consumer crash after local commit;
- external timeout after possible success;
- replay of historical events;
- temporary downstream outage;
- one tenant generating 100x normal traffic.

Document the event ID, business idempotency key, state machine, retry policy, reconciliation path, replay mode, fairness controls, and observability evidence.

## Takeaway

> Duplicates, retries, delays, and reordering are normal properties of distributed systems. Correct architecture makes them safe through explicit identity, scoped ordering, durable idempotency, reconciliation, and observable state transitions.

Next: **05 — Transactional Outbox and Inbox**.
