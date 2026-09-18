# 03 — Memory Write, Retrieval and Ranking

## Purpose

A useful memory system needs two disciplined pipelines:

1. deciding what to write;
2. deciding what to retrieve later.

Weak write policy creates noisy stores.

Weak retrieval policy injects irrelevant or stale information into reasoning.

## Core Principle

> Memory quality is controlled at both write time and read time.

## Write Pipeline

A memory write pipeline can be represented as:

```text
Interaction / Event
        |
Candidate Extraction
        |
Relevance Check
        |
Sensitivity Check
        |
Deduplication
        |
Confidence / Provenance
        |
Write / Update / Reject
```

## Candidate Extraction

Candidate memories can come from:

- explicit user statements;
- workflow outcomes;
- system events;
- model inference;
- human annotation.

Source type should remain visible.

## Write Threshold

A candidate should be stored only when expected future utility justifies persistence.

Questions include:

- Will this likely matter again?
- Is it already represented elsewhere?
- Is it sensitive?
- Is it authoritative?
- Can it be corrected?
- Is retention allowed?

## Deduplication

Repeated interactions can create duplicate memories.

Deduplication can use:

- exact identifiers;
- structured keys;
- semantic similarity;
- subject + type + value comparison.

Deduplication should not merge conflicting facts without evidence.

## Update vs Append

Some information should update an existing memory.

Other information should create a new episode.

Example:

**Preference change**
- old semantic memory may be superseded.

**Repeated event**
- new episodic record may be appended.

## Retrieval Pipeline

```text
Current Task
    |
Build Memory Query
    |
Candidate Retrieval
    |
Scope Filter
    |
Freshness Filter
    |
Authority / Confidence
    |
Rank
    |
Return Top Relevant Memory
```

## Retrieval Methods

Memory systems can use:

- exact lookup;
- metadata filters;
- keyword search;
- vector similarity;
- graph traversal;
- recency;
- hybrid ranking.

No single retrieval method fits every memory type.

## Ranking

A ranking function may consider:

- relevance;
- recency;
- confidence;
- authority;
- frequency;
- importance;
- user confirmation;
- task fit.

A common error is over-weighting semantic similarity while ignoring freshness or authority.

## Recency

Recent memory is not always better.

Stable identity information may be old but valid.

Temporary intent may become stale within minutes.

Recency should be interpreted by memory type.

## Frequency

Repeated observations can increase confidence.

But repetition is not proof.

A repeated incorrect inference can still be wrong.

## Retrieval Budget

Only a small set of memories may deserve entry into current context.

A retrieval budget can limit:

- number of records;
- token volume;
- sensitivity exposure;
- memory categories.

## Query Expansion

A task may require multiple memory queries.

Example:

- subject preferences;
- previous related decisions;
- unresolved issues.

Avoid one broad similarity search over the entire memory store when structured retrieval is possible.

## User Intent Override

Current explicit user instructions should generally outweigh old remembered preferences unless policy or authoritative constraints say otherwise.

Memory should assist current intent, not trap the user in historical behaviour.

## Write Evaluation

Measure:

- useful memories written;
- unnecessary memories rejected;
- duplicates;
- incorrect inferences;
- sensitive over-retention.

## Retrieval Evaluation

Measure:

- relevant memory recall;
- irrelevant injection;
- stale memory usage;
- conflict handling;
- task outcome improvement.

## Exercise

Design a write and retrieval policy for a generic assistant that remembers user preferences.

Specify:

1. candidate rules;
2. write threshold;
3. deduplication;
4. update behaviour;
5. retrieval filters;
6. ranking;
7. budget;
8. current-intent override.

## Takeaway

> Storing memory is only half the problem. The harder problem is retrieving the right memory at the right time.

Next: **04 — Summarisation, Consolidation and Compression**.
