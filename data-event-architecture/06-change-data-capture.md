# 06 — Change Data Capture

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **06 — Change Data Capture** within Data and Event Architecture;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Change Data Capture (CDC) observes committed database changes and makes them available downstream without requiring every consumer to repeatedly query the operational database.

> CDC is a powerful change-propagation mechanism. It is not automatically a domain-event architecture.

## 1. Core model

```text
Application
    ↓
Database transaction
    ↓
Database commit log
    ↓
CDC connector
    ↓
Change stream
    ↓
Consumers / broker / data platform
```

CDC commonly reads transaction logs, write-ahead logs, or binary logs. The exact mechanism depends on the database and CDC technology.

## 2. Why CDC exists

Polling can work, but at scale it can create source load and awkward handling of timestamp races, deletes, scan cost, and freshness.

Log-based CDC can capture committed changes efficiently with lower query overhead.

## 3. CDC is not a domain event

A CDC record may say:

```text
table: orders
operation: UPDATE
before: {...}
after: {...}
```

A domain event says:

```text
OrderApproved
PaymentCaptured
InventoryReserved
```

CDC asks what changed in storage. A domain event explains what happened in the business domain.

One business operation may modify several tables, while one table update may have no meaningful business significance.

## 4. Strong CDC use cases

CDC is useful for analytical pipelines, search indexing, cache/view synchronization, warehouses/lakehouses, replication, legacy integration, stream processing, derived read models, and publishing transactional outbox rows.

## 5. CDC as outbox transport

A strong pattern is:

```text
Business transaction
    ↓
Authoritative state + intentional outbox event
    ↓ commit
CDC reads committed outbox insert
    ↓
Broker
    ↓
Consumers
```

The application owns business semantics. The outbox records durable publication intent. CDC transports committed records efficiently.

## 6. Avoid accidental public database APIs

If consumers depend directly on raw CDC, an internal schema refactor can break unrelated systems.

Where long-lived semantics matter, introduce a transformation or contract boundary:

```text
Raw CDC
   ↓
Schema-aware ingestion
   ↓
Canonical transformation
   ↓
Stable downstream contract
```

## 7. Transaction boundaries

One application transaction may update several tables. Consumers need to know whether they are observing row-level changes or a completed higher-level business operation.

Preserve transaction metadata where required so consumers do not interpret partial state as completed business truth.

## 8. Initial snapshots

CDC often starts with an initial snapshot followed by continuous changes.

A safe bootstrap conceptually requires:

```text
Consistent snapshot
      +
Known log position
      +
Continue streaming from that position
```

Otherwise changes occurring during bootstrap can be missed or duplicated.

Consumers should tolerate the snapshot-to-stream transition.

## 9. Ordering

CDC may preserve useful source-log ordering, but brokers, partitions, transformations, concurrency, and multiple sources can change observed ordering.

Do not assume universal global order. Preserve transaction positions, entity versions, or other ordering metadata where required.

## 10. Deletes and tombstones

CDC can capture deletes that timestamp polling may miss.

Downstream systems must distinguish hard delete, soft delete, logical deactivation, projection tombstone, and privacy deletion. These are not interchangeable.

A technical tombstone does not by itself prove that all legally relevant downstream copies were erased.

## 11. Schema evolution

Raw CDC is closely coupled to source schema. Column renames, type changes, table splits, removals, enum changes, and precision changes can affect consumers.

Schema governance therefore applies to CDC too.

## 12. Before and after images

Some CDC systems expose previous and new values. These can support delta calculations, change classification, auditing, projections, and anomaly detection.

They also increase volume and may expose sensitive data. Capture only what the use case justifies.

## 13. Large payloads

Wide tables and large text/blob fields can create enormous change volume.

Do not replicate every column merely because CDC makes it possible. Filter, project, reference, and transform according to consumer need.

## 14. Backpressure and retention

If consumers fall behind, source logs or CDC infrastructure may have finite retention.

Monitor:

```text
source log retention
connector lag
oldest unread position
broker lag
consumer lag
throughput
error rate
```

If lag exceeds retained history, recovery may require a fresh snapshot or rebuild.

## 15. Checkpoints and offsets

A checkpoint means that processing through a source position is durably complete according to the consumer's semantics.

Do not advance checkpoints before required downstream work is durable.

## 16. Failure recovery

A robust design answers:

- Where does the connector resume?
- Can changes be redelivered?
- What happens after database failover?
- How are unsupported records handled?
- Can destinations rebuild?
- What if schema changes while the connector is offline?
- How is a no-gap recovery verified?

Recovery must be tested.

## 17. Reconciliation still matters

CDC reduces missed-change risk but downstream state can still drift because of bugs, expired logs, failed transformations, manual edits, or operational mistakes.

```text
Authoritative source
        ↘
        Compare → repair / rebuild / investigate
        ↗
Derived representation
```

Use reconciliation wherever consequence justifies it.

## 18. Multi-tenancy

Raw logs can contain changes for many tenants.

Tenant identity must remain explicit through:

```text
source row → CDC → transformation → broker → consumer → derived store
```

Never rely on an AI model, search filter, or UI layer to repair missing tenant isolation.

## 19. Security

CDC infrastructure can have broad data access. Protect replication credentials, connector configuration, brokers, snapshots, schema metadata, dead-letter records, operational consoles, and replay capabilities.

A compromised CDC pipeline can expose data at scale.

## 20. Data minimization

Do not propagate every available field.

A downstream AI context service may need descriptive and operational fields but not credentials, private notes, payment details, or unrelated personal information.

## 21. Privacy deletion

CDC can propagate deletion or redaction signals, but deletion governance requires lineage across downstream copies:

```text
Authoritative deletion
      ↓
CDC / deletion event
      ↓
Search
Analytics
Cache
Vector store
AI context store
Archives according to policy
```

## 22. CDC and analytics

A common architecture is:

```text
Operational DB
    ↓ CDC
Raw change layer
    ↓
Transformations
    ↓
Curated analytical models
    ↓
Metrics / ML / AI
```

Keep heavy analytical workloads away from production transactional databases where appropriate.

## 23. Search and vector indexes

Search and vector stores are derived representations.

CDC can trigger incremental updates, but preserve provenance such as source identity, source version, observed time, transformation version, and index version.

This helps identify stale or incorrectly transformed AI context.

## 24. AI context freshness

Fast propagation is not the same as safe execution.

```text
CDC-fed context
      ↓
AI reasoning
      ↓
Proposal
      ↓
Re-read critical authoritative state
      ↓
Validation + permission
      ↓
Execute
```

Near-real-time derived context can support reasoning while consequential execution verifies current truth.

## 25. Model-generated data contamination

If AI outputs are persisted, CDC may propagate them into analytics, retrieval indexes, training datasets, and future model context.

Without provenance, generated content can be mistaken for independently verified data.

Tag AI-derived information and preserve its validation/acceptance status.

## 26. Feedback-loop poisoning

A dangerous loop is:

```text
Model output
   ↓
Database
   ↓ CDC
Knowledge/index/training data
   ↓
Model input
   ↓
More model output
```

If generated information is treated as independent evidence, errors can reinforce themselves.

Preserve provenance and prevent unverified model output from silently becoming ground truth.

## 27. CDC vs APIs and explicit events

Prefer APIs or explicit domain events when business semantics matter more than row changes, the source database is not controlled by you, access should be capability-limited, consumers should not know persistence structure, or authorization semantics must be enforced.

CDC is strongest when efficient observation of committed data changes is the actual requirement.

## 28. CDC vs polling

Polling remains valid for simple, low-volume, low-freshness integrations.

```text
Polling
+ simple
+ easy to operate
- source load can grow
- delete/gap handling can be awkward

CDC
+ low-latency committed changes
+ efficient at scale
+ captures deletes
- more infrastructure/governance complexity
- closer coupling to source schema
```

Choose from requirements, not fashion.

## 29. Observability

For every CDC pipeline, know:

- current source position;
- connector health;
- lag in time and records;
- snapshot status;
- schema/version;
- last durable checkpoint;
- error/quarantine count;
- destination throughput;
- tenant skew where relevant;
- source-log retention margin;
- reconciliation status.

A green process indicator is insufficient if the connector is silently hours behind.

## 30. Testing

Test initial snapshot during writes, connector restart, duplicate delivery, source failover, compatible and breaking schema changes, deletes/tombstones, high lag, retention pressure, unsupported records, destination outage, tenant isolation, projection rebuild, and propagation of AI-derived data.

## 31. Anti-patterns

Avoid:

- treating every row mutation as a domain event;
- exposing raw database schema as a permanent enterprise contract;
- assuming CDC eliminates duplicates;
- checkpointing before downstream work is durable;
- ignoring log retention;
- sending every database column everywhere;
- treating search/vector indexes as authoritative because CDC keeps them fresh;
- allowing missing tenant context;
- propagating AI-generated data without provenance;
- assuming a running connector is a current connector;
- eliminating reconciliation because CDC exists;
- introducing CDC where simple polling meets the requirement.

## 32. Architect checklist

Before approving CDC, ask:

- Why is CDC preferable to explicit events, APIs, or polling?
- Which changes are captured?
- Are consumers depending on storage details or stable semantics?
- How is the initial snapshot made consistent?
- What ordering guarantees actually exist?
- How are deletes represented?
- How are schema changes governed?
- Where are offsets/checkpoints stored?
- What happens if lag exceeds log retention?
- Are consumers idempotent?
- Can derived state be rebuilt?
- How is drift reconciled?
- Are tenant/privacy boundaries preserved?
- Is sensitive data minimized?
- Can AI-generated data be distinguished from authoritative facts?
- Does consequential AI execution revalidate authoritative state?

## 33. Exercise

Design a CDC pipeline for a generic multitenant operational database feeding an analytical warehouse, a search index, and an AI context service.

Document snapshot strategy, checkpointing, schema evolution, deletion semantics, tenant isolation, data minimization, lag objectives, failure recovery, reconciliation, AI provenance, and the point where raw CDC becomes a stable canonical contract.

Then identify which business events should still be published explicitly rather than inferred from database mutations.

## Takeaway

> CDC efficiently propagates committed database changes, but storage changes are not automatically business meaning. Use CDC deliberately, preserve schema and tenant boundaries, monitor lag and recoverability, and keep AI consumers behind provenance-aware deterministic data contracts.

Next: **07 — Streaming, Batch and Hybrid Dataflows**.
