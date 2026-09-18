# 03 — Enterprise Data, Residency and Knowledge Boundaries

## Purpose

Give AI useful organizational context without dissolving existing data boundaries.

## Data classes

Classify information by sensitivity, ownership, tenant, jurisdiction, retention, purpose and permitted processing.

## Systems of record

Databases, ERP, CRM, document repositories and other authoritative systems remain sources of truth. AI indexes and memories are derived views.

## Retrieval authorization

```text
Identity + purpose
      ↓
Authorized source set
      ↓
Retrieval
      ↓
Minimum relevant evidence
      ↓
Model
```

Filtering after unauthorized retrieval is too late.

## Residency

Model endpoints, storage, logs, backups, indexes and support access can all affect residency. Treat residency as an end-to-end data-flow property.

## Knowledge boundaries

Separate public knowledge, enterprise-wide knowledge, team/domain knowledge, tenant/customer knowledge and personal/user context.

## Retention and deletion

Derived embeddings, caches, transcripts and evaluation samples need lifecycle rules tied to source policy.

## Lineage

Track source, version/time, transformation and access context for evidence used in consequential outputs.

## Exercise

Map a global enterprise RAG system where some documents may never leave a specified jurisdiction or business unit.

## Takeaway

> Enterprise AI should inherit data governance from authoritative systems rather than creating a parallel ungoverned knowledge universe.

Next: **04 — Integration Architecture and AI Gateways**.
