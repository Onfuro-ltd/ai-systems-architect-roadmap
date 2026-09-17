# 07 — Streaming, Batch and Hybrid Dataflows

## Purpose

Not every data problem needs real-time streaming, and not every problem can wait for a nightly batch.

> Real-time is a business requirement, not an architectural status symbol.

## 1. Processing models

**Batch** processes a bounded collection at intervals.

```text
Accumulated data → Scheduled job → Transform → Persist
```

**Streaming** continuously processes an ongoing sequence.

```text
Event → Event → Event → Continuous processing → Updated result
```

**Hybrid** uses streaming for freshness and batch for correction, recomputation, historical processing, or work that does not require immediacy.

Many mature systems are hybrid.

## 2. Start with latency requirements

Ask how stale a result may safely be: seconds, minutes, hours, daily, or on demand.

If a report is reviewed once each morning, processing it every second may add cost and complexity without customer value.

## 3. Batch

Batch is strong for historical recomputation, reporting periods, model-training datasets, reconciliation, bulk enrichment, low-urgency analytics, exports/imports, and rebuilding projections.

Its weaknesses include stale results, processing spikes, long recovery windows, and repeated scans. These matter only when they violate actual requirements.

## 4. Streaming

Streaming supports low-latency propagation and incremental computation for operational alerts, anomaly signals, event-driven workflows, live monitoring, incremental projections, fast personalization, and rapidly changing AI context.

Its costs include ordering, duplicates, checkpoints, partitions, consumer lag, state, late events, backpressure, schema evolution, replay, and continuous capacity.

The latency benefit must justify the complexity.

## 5. Micro-batching

Micro-batching groups short windows and processes them frequently.

```text
Events → 30-second window → Batch transform → Result
```

It can provide near-real-time behaviour while preserving some batch simplicity.

## 6. Event time and processing time

```text
event time      = when the business event occurred
processing time = when the data system handled it
```

They can differ because of outages, retries, offline systems, imports, network delay, or backlog.

Historical analysis based only on processing time can be wrong.

## 7. Late data and watermarks

A streaming window may appear complete and later receive an older valid event.

Define whether to update the result, wait for allowed lateness, issue a correction, route the record separately, or reconcile later in batch.

A watermark estimates event-time progress. It is not proof that an older event can never arrive.

## 8. Stateful streaming

Running totals, session windows, deduplication, joins, state machines, and anomaly baselines require processor state.

Stateful processing needs durable checkpoints, bounded state, recovery behaviour, and explicit consistency semantics.

## 9. Windows and joins

Tumbling, sliding, and session windows answer different questions. A rolling 24-hour metric is not the same as a calendar-day batch.

Stream joins are harder than static joins because both sides arrive independently. Define join keys, time boundaries, lateness, missing counterparts, retention, and correction rules.

If low latency is unnecessary, batch joins are often simpler and easier to reproduce.

## 10. Hybrid architecture

```text
Authoritative systems
      ↓
Events / CDC
      ↓
Streaming path ──→ Fresh operational views
      ↓
Durable history
      ↓
Batch path ──────→ Reconciliation / analytics / rebuilds
```

Streaming provides freshness. Batch provides recomputation and repair.

## 11. Rebuildability

Ask:

> If this projection is corrupted today, can we recreate it from authoritative data or durable history?

A streaming architecture is fragile when the stream processor state is the only surviving representation.

## 12. Shared transformation semantics

Where practical:

```text
Canonical transformation logic
        ↙          ↘
Incremental path   Rebuild path
```

Avoid two unrelated definitions of the same business metric.

## 13. Materialized views

A materialized view stores a derived result so consumers do not repeatedly recompute it.

Streaming may update it incrementally. Batch may rebuild or reconcile it. It remains derived unless deliberately designated authoritative.

## 14. Freshness objectives

Replace vague claims such as real-time with measurable objectives, for example:

```text
95% of eligible changes visible within 60 seconds
99.9% visible within 5 minutes
```

The actual numbers must follow business requirements. Also define behaviour when the objective is missed.

## 15. Backpressure and recovery storms

When input exceeds safe processing capacity, use bounded concurrency, buffering, throttling, admission control, tenant quotas, load shedding, or degraded modes.

After an outage:

```text
Normal traffic + Backlog recovery ≤ Safe downstream capacity
```

Aggressive autoscaling can otherwise overwhelm recovering dependencies.

## 16. Priority and tenant fairness

Consequential operational events may deserve priority over analytics enrichment or optional AI summaries.

One noisy tenant should not monopolize worker capacity. Use quotas, partitioning, concurrency controls, or fair scheduling where needed.

## 17. Resumable batch

Large batch jobs should use bounded partitions and checkpoints.

```text
Job → Partitions → Checkpointed completion
```

This improves retry, parallelism, observability, and recovery.

Incremental batches can use versions, watermarks, CDC positions, or changed-record sets, but they still need a rebuild path if a checkpoint becomes wrong.

## 18. Reconciliation batch

Even real-time systems benefit from periodic authoritative comparison.

```text
Streaming projection
        ↘
        Compare → Repair
        ↗
Authoritative snapshot
```

This detects missed events, bugs, schema problems, and drift.

## 19. AI inference dataflows

Interactive inference prioritizes user latency.

```text
User → Context → Model → Response
```

Asynchronous inference suits enrichment, extraction, classification, summaries, and recommendations.

```text
Event/job → Queue → Model worker → Validated result
```

Batch inference suits backfills, embedding generation, evaluation, and large-scale reprocessing.

## 20. Do not stream expensive AI by default

If hundreds of updates affect one entity in a minute, hundreds of model calls may be wasteful.

Consider debounce, coalescing, filtering, material-change thresholds, micro-batching, latest-state processing, deterministic prefilters, and cheaper model routing.

Real-time data does not imply real-time inference.

## 21. AI context pipelines

```text
Authoritative changes
      ↓
Streaming / CDC
      ↓
Fast context projection
      ↓
AI reasoning

Durable history
      ↓
Batch rebuild / evaluation
      ↓
Corrected projection
```

The fast path provides freshness. The batch path provides repair and reproducibility.

## 22. Embedding pipelines and stale work

Embedding generation is naturally asynchronous.

```text
Content change
    ↓
Material-change check
    ↓
Embedding job
    ↓
Generate
    ↓
Verify source version
    ↓
Write vector projection
```

If a job was created for version 12 but the source is now version 15, discard or recompute it rather than letting stale work overwrite a newer result.

## 23. Cost-aware dataflows

Measure records, bytes, broker/storage cost, compute, model tokens, accelerator utilization, duplicate work, recomputation cost, and the business value of lower latency.

A faster architecture that multiplies model calls by 100 may be commercially worse.

## 24. Observability

For streaming track input/output rate, consumer lag, oldest event age, processing latency, event-time lateness, checkpoint age, retries, state size, and tenant skew.

For batch track schedule, actual start, duration, records scanned/changed, partition progress, retries, failure point, output freshness, and cost.

For hybrid systems also observe the reconciliation gap.

## 25. Correctness and governance

Low-latency wrong data is still wrong.

Preserve schema validation, completeness, uniqueness, consistency, freshness, referential integrity, tenant identity, access control, lineage, retention, deletion, provenance, and auditability.

## 26. Decision sequence

```text
What freshness is actually required?
        ↓
Can batch satisfy it?
 yes → prefer simpler batch
 no
        ↓
Can micro-batch satisfy it?
 yes → consider micro-batch
 no
        ↓
Use streaming where justified
        ↓
Add rebuild / reconciliation path
```

## 27. Testing

Test delayed, late, duplicate, and out-of-order events; processor restart; checkpoint recovery; backlog after outage; downstream throttling; noisy tenants; batch partition failure; partial rerun; full rebuild; stale AI completion; reconciliation drift; and peak-volume cost.

## 28. Anti-patterns

Avoid streaming for prestige, nightly batch when safety needs seconds, assuming processing time equals event time, unlimited concurrency, no late-data policy, no rebuild path, inconsistent batch/stream definitions, model inference on every raw change, stale AI jobs overwriting new results, ignoring recovery storms, and calling a pipeline real-time without a measurable freshness objective.

## 29. Architect checklist

Ask:

- What freshness is actually required?
- What happens when data is stale?
- Can batch or micro-batch satisfy it?
- What event-time semantics matter?
- How are late records handled?
- Is stateful streaming necessary?
- Can derived state be rebuilt?
- How are checkpoints recovered?
- How is backlog drained safely?
- Is tenant fairness enforced?
- Is reconciliation available?
- Are batch and streaming semantics aligned?
- Are AI calls filtered and cost-controlled?
- Can stale AI work be suppressed?
- Are freshness, correctness, and cost observable?

## 30. Exercise

Design a hybrid dataflow for a generic multitenant platform requiring operational changes visible within one minute, daily authoritative reconciliation, near-real-time anomaly detection, asynchronous AI classification, nightly analytical aggregates, and full projection rebuild capability.

Document the streaming path, batch path, event-time rules, checkpoints, late-data policy, backpressure, tenant fairness, recovery-storm controls, AI stale-work suppression, reconciliation, observability, and cost controls.

Then identify which workloads do not need streaming and explain why.

## Takeaway

> Choose processing latency from business need. Use streaming for justified freshness, batch for simplicity and recomputation, and hybrid architectures when you need both fast reaction and a dependable path to repair, reproduce, and control cost.

Next: **08 — Event Sourcing and Replay**.
