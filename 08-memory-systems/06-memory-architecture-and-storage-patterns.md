# 06 — Memory Architecture and Storage Patterns

## Purpose

Memory architecture combines information models, storage systems and retrieval paths.

The database choice should follow the memory workload, not define the memory concept.

## Core Principle

> Store memory according to access pattern, lifecycle and governance needs.

## Reference Architecture

```text
Events / Interactions
        |
Memory Write Service
        |
        +-- Validation
        +-- Deduplication
        +-- Classification
        +-- Provenance
        |
        v
Memory Stores
        |
        +-- Structured Store
        +-- Search Index
        +-- Vector Index
        +-- Event Archive
        |
        v
Memory Retrieval Service
        |
        +-- Filters
        +-- Ranking
        +-- Conflict Handling
        |
        v
Context Assembly
```

Not every system needs every component.

## Relational Storage

Relational databases are useful for:

- structured semantic memories;
- strong subject relationships;
- metadata filters;
- lifecycle fields;
- auditing;
- transactions.

They are often underused in memory systems.

## Document Stores

Document stores are useful for:

- flexible episode structures;
- nested metadata;
- variable records.

They can simplify evolving schemas but still require governance.

## Vector Indexes

Vector indexes support semantic retrieval.

They are useful for:

- approximate conceptual similarity;
- episode recall;
- related-context discovery.

Vector search should usually be combined with structured filters.

## Search Indexes

Lexical or hybrid search helps with:

- names;
- identifiers;
- exact phrases;
- metadata;
- temporal filtering.

Semantic retrieval should not replace exact lookup where exact identity matters.

## Event Logs

Event logs preserve history.

They are useful for:

- replay;
- audit;
- episode reconstruction;
- consolidation pipelines.

An event log may be the evidence layer while memory stores hold derived views.

## Graphs

Graph storage can help represent:

- relationships;
- dependencies;
- conflicts;
- provenance;
- entity connections.

Graphs are useful when relationships are first-class query needs.

Do not introduce graph infrastructure purely because memory sounds relational.

## Hybrid Architecture

A mature system may combine:

```text
Event Store = evidence
Relational DB = current structured memory
Vector Index = semantic retrieval
Search Index = lexical retrieval
Object Store = large artefacts
```

This is a pattern, not a requirement.

## Memory Service Boundary

A memory service can centralise:

- write policy;
- read policy;
- lifecycle;
- deletion;
- provenance;
- evaluation.

This helps prevent every application from implementing memory differently.

## Tenant Isolation

Memory must respect tenant and workspace boundaries.

Tenant identity should be enforced by application identity and storage policy, not trusted from model-generated parameters.

## Consistency

Decide where strong consistency matters.

Examples:

**Strong consistency**
- deletion;
- user setting;
- authoritative preference.

**Eventual consistency**
- semantic index update;
- background consolidation.

## Backup and Recovery

Memory recovery should account for:

- deleted memories;
- tombstones;
- indexes;
- derived summaries.

A restored backup should not silently resurrect information that must remain deleted.

## Exercise

Design storage for:

- user preferences;
- episodic history;
- semantic similarity search;
- audit evidence.

Choose storage types and explain lifecycle and consistency requirements.

## Takeaway

> Memory architecture is a data architecture problem with AI-specific retrieval and lifecycle requirements.

Next: **07 — Privacy, Security and User Control**.
