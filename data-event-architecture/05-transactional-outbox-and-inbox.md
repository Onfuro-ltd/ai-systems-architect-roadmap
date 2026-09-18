# 05 — Transactional Outbox and Inbox

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **05 — Transactional Outbox and Inbox** within Data and Event Architecture;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Distributed systems often need to change authoritative state and communicate that change to other systems. Doing those as two unrelated writes creates a dangerous failure window.

> If a business transaction and its integration event must agree, make their durable recording part of one local transaction, then deliver asynchronously.

## 1. The dual-write problem

Consider:

```text
1. Update authoritative database
2. Publish event to broker
```

If the process crashes after step 1 but before step 2, the business state changes while downstream consumers never learn about it.

Reversing the order is not safer:

```text
1. Publish event
2. Update database
```

A crash between the steps can publish an event describing a state change that never committed.

Two independent durable systems cannot be made atomic merely by placing two function calls next to each other.

## 2. Why retries alone do not solve it

Retrying the whole request may duplicate either the database mutation or the event publication.

The problem is not simply transient failure. It is uncertainty about which side committed.

You need a durable record of the intent to publish that participates in the same transaction as the authoritative state mutation.

## 3. Transactional outbox

The outbox pattern writes the business change and an event-to-publish record in one local database transaction.

```text
BEGIN TRANSACTION
    mutate business state
    insert outbox record
COMMIT
        ↓
Outbox publisher
        ↓
Broker / event transport
        ↓
Consumers
```

If the transaction rolls back, neither exists.

If it commits, both the new state and durable publication intent exist.

## 4. Outbox record

A generic outbox record might contain:

```text
outbox_id
event_id
event_type
event_version
aggregate_type
aggregate_id
tenant_id
payload
occurred_at
created_at
publication_status
attempt_count
next_attempt_at
published_at
correlation_id
causation_id
```

Do not add metadata without purpose. Include what is needed for identity, routing, observability, retry, governance, and safe publication.

## 5. The outbox is not the broker

The outbox proves that an event should be published. It does not replace a broker's distribution, retention, partitioning, or consumer capabilities.

Think:

```text
Database transaction → durable publication intent
Broker                → event distribution
Consumer inbox        → durable consumption control
```

## 6. Publishing the outbox

A publisher can discover pending rows through polling, database notifications, or change data capture.

A polling publisher commonly:

1. selects eligible pending records;
2. claims a bounded batch;
3. publishes them;
4. records publication progress;
5. retries failures with backoff.

The claiming strategy must support multiple publisher workers without causing unsafe concurrent processing.

## 7. Publication is normally at-least-once

A classic uncertainty remains:

```text
Publish event
    ↓
Broker accepts it
    ↓
Publisher crashes before marking row published
    ↓
Publisher retries
    ↓
Broker receives duplicate
```

The outbox solves lost publication caused by the database/broker dual write. It does not magically eliminate duplicate delivery.

Consumers must remain idempotent.

## 8. Stable event identity

The event ID must be created before publication and stored in the outbox.

Retries publish the same logical event identity.

```text
outbox row → event_id E123
retry      → event_id E123
retry      → event_id E123
```

Generating a fresh ID on every attempt destroys useful deduplication semantics.

## 9. Do not hold database transactions open across brokers

Avoid:

```text
BEGIN
update business data
call remote broker
wait...
COMMIT
```

Long transactions increase lock time, couple database health to remote latency, and still do not create a true distributed atomic transaction unless a suitable distributed transaction protocol is deliberately used.

The outbox keeps the local transaction short.

## 10. Payload vs reference

An outbox may store the full event payload or enough information to construct it later.

Storing the final payload at transaction time preserves the event as it was when the business change occurred.

Reconstructing later from current state risks publishing a different fact if the entity changes again before publication.

For domain events, prefer preserving the historical semantics required by the contract.

## 11. Outbox ordering

If event order matters for an aggregate, preserve an aggregate sequence/version and publish consistently with that requirement.

Global ordering is rarely necessary.

```text
aggregate_id + aggregate_version
```

is often more useful than attempting to serialize the entire platform.

## 12. Outbox retention

Do not let the outbox grow forever without policy.

Define:

- how long successfully published rows remain;
- whether payloads contain sensitive data;
- archival requirements;
- audit requirements;
- cleanup jobs;
- indexes needed for pending publication;
- how cleanup is monitored.

Retention and deletion rules should match the event architecture's governance requirements.

## 13. Transactional inbox

The inbox pattern protects a consumer from duplicate processing by durably recording received event identity.

```text
Receive event
    ↓
BEGIN TRANSACTION
    insert/check inbox event_id
    apply business mutation
COMMIT
    ↓
Acknowledge transport
```

If the same event arrives again, the inbox record shows that the local business effect has already been committed.

## 14. Inbox uniqueness

Use a durable uniqueness rule appropriate to the identity boundary.

For example:

```text
UNIQUE(consumer_name, event_id)
```

may be useful when several independent consumers share a database but each legitimately processes the same event once.

The exact key depends on consumer semantics.

## 15. Inbox and business idempotency are related but different

Event deduplication asks:

> Have I processed this event before?

Business idempotency asks:

> Has this business operation already happened?

A single business operation may arrive through different events, commands, retries, or reconciliation paths.

For consequential actions, use the business identity that actually expresses the invariant.

## 16. Outbox + inbox together

A robust flow can look like:

```text
Service A
Business state + Outbox
        ↓
Publisher
        ↓
Broker
        ↓
Service B
Inbox + Business state
        ↓
Service B Outbox
        ↓
Next event
```

Each service maintains local atomicity without pretending there is one global database transaction.

## 17. The pattern creates local guarantees

The outbox/inbox pattern does not provide instant global consistency.

It provides composable local guarantees:

```text
Local mutation + publication intent → atomic
Consumer dedupe + local mutation    → atomic
Cross-service propagation           → asynchronous
```

This is a powerful foundation for reliable eventual consistency.

## 18. Failure matrix

| Failure | Expected behaviour |
|---|---|
| Business transaction rolls back | No committed outbox event |
| App crashes after commit | Outbox remains publishable |
| Broker unavailable | Outbox retries later |
| Broker accepts but publisher loses response | Event may be republished with same ID |
| Consumer crashes before commit | Message can be redelivered |
| Consumer commits but acknowledgement fails | Inbox prevents duplicate local effect |
| Downstream dependency unavailable | Consumer retry/workflow policy applies |

Architecture becomes easier to reason about when failures are written explicitly.

## 19. Poison outbox records

A malformed or permanently unpublishable event should not block the entire outbox.

Use bounded attempts, failure classification, quarantine, alerting, and an operator-safe repair/replay process.

Never silently discard a business event merely because publication is inconvenient.

## 20. Backpressure

If the broker is unavailable or publication slows, the outbox backlog grows.

Monitor:

```text
pending count
oldest pending age
publish throughput
failure rate
retry count
quarantined count
per-tenant backlog where relevant
```

Oldest pending age is often more informative than row count alone.

## 21. Multi-tenant systems

Tenant identity should be captured in the outbox transaction and propagated through publication and consumption.

Consider fairness when one tenant creates disproportionate event volume.

Do not derive tenant identity later from mutable or ambiguous context.

## 22. Security and privacy

Outbox and inbox tables are durable copies of integration data.

Apply:

- least-privilege database access;
- payload minimization;
- encryption where required;
- retention policy;
- tenant isolation;
- audit controls;
- safe operational tooling.

Do not treat an internal table as exempt from data governance.

## 23. Schema evolution

Outbox rows can remain pending while software versions change.

Store event type/version with the durable record. A deployment must not make already-committed pending events impossible to publish correctly.

Migration tests should include old pending outbox rows.

## 24. Deployments

A safe deployment sequence considers producers, pending outbox records, publishers, brokers, and consumers.

For breaking contract changes, follow the compatibility strategy from the previous chapter rather than assuming deployment order will always save you.

## 25. Change data capture as an outbox publisher

CDC can observe committed outbox inserts and forward them to event infrastructure.

This can reduce application polling, but it does not remove the need for:

- stable event contracts;
- ownership;
- deduplication;
- consumer idempotency;
- observability;
- schema governance.

CDC is transport machinery, not semantic architecture.

## 26. Why not publish every database change?

An outbox should contain intentional integration/domain events, not necessarily every changed column.

```text
Database mutation
      ↓
Domain rules
      ↓
Meaningful event
      ↓
Outbox
```

This preserves business meaning and avoids turning internal persistence details into public contracts.

## 27. External API side effects

The outbox can also represent durable intent to perform an external action.

For example:

```text
Business workflow state + action intent
        ↓ same transaction
Worker executes external API
        ↓
Persist verified outcome
```

But external execution still needs provider idempotency, UNKNOWN states, verification, and reconciliation where applicable.

The outbox does not make a third-party API transactional.

## 28. AI workflows

AI systems benefit from the same deterministic boundary.

```text
AI proposal
    ↓
Validation + policy + approval
    ↓
BEGIN TRANSACTION
    persist accepted workflow transition
    persist outbox action/event
COMMIT
    ↓
Durable worker
    ↓
External execution
    ↓
Outcome verification
```

This keeps model reasoning outside the atomic business transaction while making an accepted decision durable.

## 29. Never let the model publish directly

Avoid:

```text
Model → broker → consequential consumer
```

for actions requiring authorization or business validation.

Prefer:

```text
Model
 ↓
Structured proposal
 ↓
Deterministic validation
 ↓
Policy / permission / approval
 ↓
Authoritative transition + outbox
 ↓
Execution
```

The outbox becomes part of the deterministic handoff from probabilistic reasoning to durable business execution.

## 30. Observability

Trace the complete lifecycle:

```text
business transaction
      ↓
outbox record
      ↓
publication attempt(s)
      ↓
broker message
      ↓
consumer delivery
      ↓
inbox record
      ↓
business mutation
      ↓
next event / outcome
```

Useful identifiers include event ID, aggregate/business ID, correlation ID, causation ID, tenant ID, outbox ID, consumer identity, attempt number, and workflow ID.

## 31. Operational tooling

Enterprise systems need safe ways to:

- inspect stuck outbox records;
- inspect failed inbox processing;
- retry or quarantine records;
- replay a bounded set;
- view event payload/version safely;
- trace correlation chains;
- confirm cleanup/retention jobs;
- prevent accidental mass replay.

Operational tooling should enforce permissions and produce audit evidence.

## 32. Testing

Test:

1. crash before transaction commit;
2. crash immediately after commit;
3. broker outage;
4. broker success with lost acknowledgement;
5. duplicate broker delivery;
6. consumer crash before local commit;
7. consumer crash after commit but before acknowledgement;
8. schema deployment with pending old-version rows;
9. poisoned event;
10. backlog recovery after a long outage;
11. multi-tenant fairness;
12. replay of quarantined events.

The happy path alone proves very little about an outbox architecture.

## 33. Anti-patterns

Avoid:

- database write followed by best-effort publish;
- publish followed by best-effort database write;
- generating a new event ID on retry;
- marking outbox rows published before broker acceptance;
- assuming the outbox provides exactly-once business effects;
- reconstructing historical events from later mutable state without explicit semantics;
- unbounded outbox retention;
- one poisoned row blocking all publication;
- direct AI-to-broker consequential actions;
- using an in-memory dedupe cache as the only inbox;
- replaying inbox/outbox traffic without side-effect controls;
- treating CDC as a substitute for domain-event design.

## 34. Architect checklist

Before approving an outbox/inbox design, ask:

- Which state change and publication intent must be atomic?
- Is the outbox insert in the same local transaction?
- Is event identity stable across retries?
- How are rows claimed concurrently?
- What happens if broker success is uncertain?
- Are consumers idempotent?
- Is event dedupe distinct from business idempotency where needed?
- How is ordering scoped?
- How are poison records quarantined?
- What is the retry/backoff policy?
- How is backlog age monitored?
- What retention and privacy rules apply?
- Can pending old-schema events survive deployments?
- Is replay operationally safe?
- Are tenant boundaries and fairness preserved?
- Are external side effects verified and reconciled?
- Does AI enter only through validated, authorized durable transitions?

## 35. Exercise

Design an outbox/inbox flow for a generic multitenant operational platform where an accepted business transition must notify two independent downstream capabilities and may later trigger an external API.

Document:

1. local transaction boundary;
2. outbox schema;
3. stable event identity;
4. publisher claiming strategy;
5. retry and quarantine policy;
6. broker delivery assumption;
7. consumer inbox uniqueness rule;
8. business idempotency rule;
9. external UNKNOWN/reconciliation path;
10. tenant isolation/fairness;
11. schema migration handling;
12. observability and replay controls.

Then walk through every crash point and prove that the system either completes safely, retries safely, or enters an explicit recoverable state.

## Takeaway

> The transactional outbox turns a fragile dual write into a durable local transaction plus asynchronous delivery. The inbox makes redelivery safe. Together they provide reliable building blocks for event-driven systems without pretending distributed work is one global transaction.

Next: **06 — Change Data Capture**.
