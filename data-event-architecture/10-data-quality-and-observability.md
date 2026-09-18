# 10 — Data Quality and Observability

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **10 — Data Quality and Observability** within Data and Event Architecture;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

AI quality depends on the operational trustworthiness of the data and context on which the system relies.

> A pipeline is healthy only when its data is sufficiently correct, complete, fresh, and fit for its intended decision.

## Infrastructure health is not data health

A connector can be running, a queue empty, and a job successful while the delivered data is wrong. Observe both machinery and meaning.

## Quality dimensions

Important dimensions include correctness, completeness, freshness, uniqueness, consistency, validity, referential integrity, timeliness, provenance, and fitness for purpose.

Thresholds should reflect consequence and consumer need.

## Data contracts

A data contract can define schema, semantics, ownership, freshness, quality rules, privacy classification, and compatibility expectations.

Validate at useful boundaries: ingestion, canonicalization, transformation, publication, derived storage, AI context construction, and consequential execution.

## Freshness

Measure freshness from authoritative change to safe consumer availability. Queue depth alone is insufficient.

Define measurable SLOs rather than saying near-real-time.

## Completeness, correctness and consistency

Detect missing records using sequence gaps, counts, reconciliation, and domain invariants. Validate semantics, not just types.

When representations disagree, know which source is authoritative and whether the difference is expected propagation lag or real drift.

## Quarantine

Malformed or semantically invalid data may be quarantined with source identity, tenant, reason, evidence, and safe repair/replay procedures. Never silently discard consequential data.

## Data observability

Monitor volume, freshness, schema change, null rates, distributions, duplicates, referential failures, lineage, reconciliation differences, and tenant/cohort health where appropriate.

Historical baselines help detect anomalies but must account for seasonality, migrations, launches, and genuine growth.

## Reconciliation

Periodic comparison with authoritative state is one of the strongest controls:

Authoritative state ↔ compare ↔ derived state → explain and repair differences.

CDC, streaming, and successful jobs do not eliminate reconciliation.

## AI context quality

Before inference validate tenant scope, authorization, source/version, freshness, schema, required facts, duplication, provenance, relevance, and size limits.

Do not ask the model to repair missing deterministic guarantees.

## Retrieval quality

Evaluate retrieval separately from generation: was the right source indexed, current, authorized, retrievable, selected, and then used correctly by generation?

This isolates failure domains.

## AI-generated data

Generated summaries, classifications, extractions, and recommendations need their own evaluation and acceptance criteria. Model confidence is not verified correctness.

If AI output feeds future data, label provenance and verification state to prevent feedback contamination.

## Incident response

A data incident needs detection, impact analysis, containment, correction/rebuild, downstream invalidation, root cause, prevention, and audit evidence.

If bad data influenced AI-assisted decisions, identify the affected outputs and actions.

## Telemetry design

Use metrics for aggregate health, traces/logs for workflow diagnosis, and audit stores for durable evidence. Avoid forcing high-cardinality workflow identity into every metric.

Track economic waste from duplicate events, repeated transformations, unnecessary embeddings, stale AI jobs, runaway replay, oversized payloads, and excessive retention.

## Multi-tenancy

Global averages can hide a completely broken tenant. Preserve tenant-level or cohort-level quality visibility where feasible while controlling privacy and telemetry cardinality.

## Anti-patterns

Avoid monitoring only job success, equating schema validity with correctness, hiding tenant failures in averages, silently dropping bad data, trusting AI to infer missing required facts, using model confidence as truth, alerting without ownership, lacking reconciliation, or leaving corrected source data stale in AI context.

## Architect checklist

Define quality ownership, dimensions and thresholds, freshness measurement, gap/duplicate/drift detection, quarantine, tenant visibility, AI-context validation, retrieval/generation evaluation, rebuild procedures, and incident traceability.

## Exercise

Design quality controls from an operational database through CDC, broker, warehouse, search/vector index, AI context builder, and AI-assisted action. Specify SLOs, checks, alerts, quarantine, reconciliation, tenancy, incident response, and affected-decision tracing.

## Takeaway

> Data observability must tell you whether information is trustworthy for its intended use, not merely whether the pipeline process is alive.

Next: **11 — AI Data Boundaries and Context Freshness**.
