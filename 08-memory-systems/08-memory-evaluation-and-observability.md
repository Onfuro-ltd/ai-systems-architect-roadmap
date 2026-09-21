# 08 — Memory Evaluation and Observability

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **08 — Memory Evaluation and Observability** within Memory Systems;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Memory should improve future system behaviour.

If memory quality is not measured, systems can accumulate incorrect, irrelevant or stale information without noticing.

## Core Principle

> Evaluate memory by its effect on future outcomes.

## Evaluation Layers

A memory system can be evaluated at:

- write quality;
- storage integrity;
- retrieval quality;
- ranking quality;
- context usefulness;
- downstream task outcome;
- privacy and deletion behaviour.

## Write Precision

Write precision asks:

> Of the memories stored, how many should actually have been stored?

Low precision creates memory clutter.

## Write Recall

Write recall asks:

> Of the information worth retaining, how much did the system capture?

Low recall causes repeated forgetting of useful context.

## Retrieval Recall

Retrieval recall measures whether relevant stored memories were found for the task.

## Retrieval Precision

Retrieval precision measures how much retrieved memory was actually useful.

Too many irrelevant memories can degrade model behaviour.

## Freshness Accuracy

Measure whether retrieved memories were still valid.

A retrieval system can be semantically accurate but temporally wrong.

## Conflict Accuracy

Test whether the system detects:

- superseded values;
- contradictory memories;
- uncertain inferences.

## Current-Intent Respect

A critical behavioural test is whether current explicit instructions override old remembered preferences when they should.

## Outcome Evaluation

Compare task performance:

```text
No Memory
vs
Memory Enabled
```

Measure whether memory improves:

- accuracy;
- completion rate;
- user effort;
- consistency;
- latency;
- cost.

Memory that adds complexity without outcome improvement may not be worth keeping.

## Counterfactual Tests

Counterfactual evaluation can ask:

- What if an old memory is removed?
- What if a conflicting new preference is added?
- What if the memory is stale?
- What if the subject changes?

These tests reveal hidden dependence.

## Privacy Tests

Test:

- tenant isolation;
- user isolation;
- delete propagation;
- retention expiry;
- sensitive-memory filtering;
- poisoning resistance.

## Observability

Useful metrics include:

- memories written;
- memories rejected;
- memory reads;
- retrieval hit rate;
- average memories injected;
- stale-memory rate;
- conflict rate;
- deletion latency;
- correction rate.

## Traceability

For important outcomes, the system should be able to answer:

- Which memories influenced this response?
- Why were they retrieved?
- What was their source?
- When were they created?
- Were any conflicts ignored?

## Cost

Memory affects:

- storage;
- indexing;
- retrieval;
- context tokens;
- model latency;
- consolidation jobs.

Measure total system cost rather than storage cost alone.

## Failure Taxonomy

Useful failure classes include:

- failed write;
- unnecessary write;
- incorrect inference;
- missed retrieval;
- irrelevant retrieval;
- stale retrieval;
- conflict failure;
- deletion failure;
- scope leakage.

## Domain Boundary

This lesson focuses on memory-specific evaluation.

Domain 10 covers evaluation and reliability as a general discipline.

## Exercise

Create an evaluation suite for a generic preference-memory system.

Include:

1. useful write;
2. unnecessary write;
3. changed preference;
4. stale memory;
5. conflicting memory;
6. wrong-user isolation;
7. delete request;
8. no-memory baseline.

## Takeaway

> Memory is successful when it improves future outcomes without creating unacceptable privacy, correctness or operational cost.

Next: **09 — Capstone**.
