# 09 — Capstone: Design a Production Memory System

## Objective

Design a memory subsystem for an AI application that retains useful information across interactions while remaining bounded, explainable and privacy-aware.

## Scenario

Choose a generic application such as:

- research assistant;
- project assistant;
- support assistant;
- learning assistant;
- operations assistant.

Do not begin with a database.

Begin with what the system should and should not remember.

## Part 1 — Memory Policy

Define:

- memory purpose;
- subjects;
- scopes;
- memory types;
- retention;
- prohibited categories;
- user controls.

## Part 2 — Memory Types

Identify where the system uses:

- working memory;
- episodic memory;
- semantic memory;
- procedural memory.

Explain which information should instead live in:

- context;
- knowledge;
- workflow state;
- explicit skill or rule.

## Part 3 — Write Pipeline

Design:

```text
Interaction / Event
        |
Candidate Extraction
        |
Policy
        |
Sensitivity
        |
Deduplication
        |
Provenance
        |
Write / Update / Reject
```

Define which stages are deterministic and which may use model reasoning.

## Part 4 — Retrieval Pipeline

Design:

```text
Task
 |
Query
 |
Candidate Retrieval
 |
Scope / Freshness
 |
Ranking
 |
Conflict Handling
 |
Context Injection
```

Define the retrieval budget.

## Part 5 — Consolidation

Create a strategy for:

- session summaries;
- repeated episodes;
- semantic promotion;
- evidence links;
- contradiction preservation.

## Part 6 — Forgetting

Define:

- expiry;
- supersession;
- delete;
- decay;
- reconfirmation;
- tombstones.

Explain how deletion propagates through indexes and derived summaries.

## Part 7 — Storage Architecture

Choose storage for:

- structured memory;
- episodic evidence;
- semantic search;
- large artefacts.

Explain consistency and backup behaviour.

## Part 8 — Privacy and Security

Define controls for:

- subject isolation;
- tenant isolation;
- sensitive information;
- poisoning;
- user correction;
- user deletion;
- logging.

## Part 9 — Evaluation

Build tests for:

- write precision;
- write recall;
- retrieval precision;
- retrieval recall;
- staleness;
- conflicts;
- current-intent override;
- deletion;
- wrong-subject leakage.

Compare task quality with and without memory.

## Part 10 — Observability

Specify metrics for:

- writes;
- reads;
- injections;
- stale memory;
- conflicts;
- corrections;
- deletes;
- latency;
- cost.

## Architectural Review Questions

Before completion, answer:

1. What does the system remember?
2. Why is each category worth retaining?
3. What should never become durable memory?
4. How is provenance preserved?
5. How does current intent override history?
6. How are contradictions handled?
7. How can a user correct memory?
8. How does deletion propagate?
9. How is memory quality evaluated?
10. What happens when memory is disabled?

## Completion Criteria

Another engineer should be able to determine:

- what is stored;
- where it is stored;
- why it is stored;
- who may retrieve it;
- how it is ranked;
- when it expires;
- how it is corrected;
- how it is deleted;
- how its usefulness is measured.

## Takeaway

> A production memory system is a governed data system for future relevance, not an infinite transcript.

Next: **Domain 09 — Orchestration and Multi-Agent Systems**.
