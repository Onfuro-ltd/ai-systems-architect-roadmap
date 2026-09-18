# 04 — Summarisation, Consolidation and Compression

## Purpose

Memory stores can grow indefinitely if every detail is retained at full fidelity.

Summarisation and consolidation reduce volume while preserving information expected to matter later.

## Core Principle

> Compression trades detail for utility. Preserve evidence when the lost detail may matter.

## Raw Evidence vs Derived Memory

A strong architecture distinguishes:

```text
Raw Event / Source
        |
        v
Derived Memory
```

Derived memory may be:

- summary;
- extracted fact;
- preference;
- pattern;
- classification.

The derived memory should preserve provenance back to the underlying evidence where practical.

## Summarisation

Summarisation condenses information.

Examples:

- conversation summary;
- incident summary;
- project status summary;
- interaction history summary.

Summaries are lossy representations.

They should not automatically replace original evidence where exact detail matters.

## Consolidation

Consolidation combines multiple related memories into a more useful representation.

Example:

```text
Episode 1
Episode 2
Episode 3
   |
   v
Validated recurring preference
```

Consolidation should require enough evidence to justify the abstraction.

## Compression Levels

Systems may maintain several levels:

```text
Raw Events
   |
Session Summary
   |
Topic Summary
   |
Long-Term Semantic Memory
```

Each level trades fidelity for retrieval efficiency.

## Hierarchical Memory

Hierarchical memory allows the system to retrieve a compact summary first and drill into detail when needed.

Example:

```text
Project Summary
   |
   +-- Decision Summaries
   +-- Incident Summaries
   +-- Raw Events
```

This is useful when histories become large.

## Incremental Summaries

A summary can be updated as new events occur.

The update process should avoid:

- silently dropping prior important facts;
- reinforcing old errors;
- losing provenance;
- treating model-generated summaries as ground truth.

## Consolidation Windows

Consolidation can happen:

- after each interaction;
- at session end;
- periodically;
- after threshold volume;
- after milestone completion.

Choose timing according to cost and freshness requirements.

## Importance

Some events deserve to remain individually accessible.

Examples:

- user corrections;
- approvals;
- commitments;
- incidents;
- exceptions;
- safety-relevant decisions.

Do not compress away critical evidence.

## Contradiction Handling

When new information conflicts with an existing summary, the system can:

- update;
- mark uncertain;
- preserve both with timestamps;
- request confirmation;
- escalate.

A summary should not hide disagreement.

## Model-Based Compression

Models are useful for summarisation but can:

- omit details;
- invent relationships;
- overgeneralise;
- merge conflicting events.

Use deterministic metadata and validation around model-generated summaries.

## Evaluation

Evaluate compression by asking:

- Did important facts survive?
- Were contradictions preserved?
- Can the system recover supporting evidence?
- Did retrieval improve?
- Did token use fall?
- Did task quality remain acceptable?

## Exercise

Take ten generic interaction events and design:

1. session summary;
2. long-term semantic memory;
3. evidence links;
4. update rule;
5. conflict rule.

Explain what you intentionally discard and why.

## Takeaway

> Compression is an information-design decision, not just a token-saving trick.

Next: **05 — Forgetting, Staleness and Conflict**.
