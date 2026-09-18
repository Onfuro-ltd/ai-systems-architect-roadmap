# 01 — Memory Foundations

## Purpose

Memory allows an AI system to carry useful information across interactions and events.

Without memory, every interaction begins from the information supplied in the current context.

With poorly designed memory, old or irrelevant information can distort future behaviour.

## Core Principle

> Memory is a controlled persistence layer for information that may matter later.

## The Memory Loop

A basic memory system can be represented as:

```text
Observe
  |
Decide What Matters
  |
Write
  |
Store
  |
Retrieve
  |
Rank / Filter
  |
Use
  |
Evaluate
  |
Update / Forget
```

Each stage needs explicit policy.

## Memory Unit

A memory unit should be more than raw text where possible.

Useful metadata can include:

- content;
- type;
- source;
- subject;
- timestamp;
- confidence;
- scope;
- expiry;
- provenance;
- sensitivity;
- version.

Metadata allows future retrieval and governance decisions.

## Memory Subject

A memory should have a clear subject.

Examples:

- user;
- account;
- project;
- organisation;
- workflow;
- device;
- system.

A memory about one subject should not silently influence another.

## Scope

Scope determines where a memory may be used.

Possible scopes include:

- current conversation;
- user;
- workspace;
- tenant;
- project;
- organisation.

Scope is both a relevance and security control.

## Authority

A memory is not necessarily authoritative.

For example:

> "The user said they prefer weekly summaries."

is different from:

> "Company policy requires weekly summaries."

The first may be memory.

The second should usually come from an authoritative knowledge source.

## Provenance

Memory should preserve where information came from.

Provenance helps answer:

- Who said this?
- What event created it?
- Was it inferred or explicit?
- When was it observed?
- Has it been confirmed?

Without provenance, old assumptions can be mistaken for facts.

## Confidence

Some memories are explicit.

Others are inferred.

Examples:

**Explicit**
- user selected a setting;
- user confirmed a preference;
- workflow produced a final decision.

**Inferred**
- likely preference;
- likely recurring pattern;
- likely relationship between events.

Inferred memory should carry lower confidence and stronger review requirements where consequences matter.

## Freshness

Memory can age.

Some memories remain stable for years.

Others become stale quickly.

A memory architecture should consider:

- created time;
- last confirmed time;
- expiry;
- superseding evidence.

## Memory Write Policy

Not every interaction should create durable memory.

A write policy can consider:

- future utility;
- confidence;
- sensitivity;
- duplication;
- explicit user intent;
- retention policy;
- cost.

## Memory Read Policy

Not every stored memory should be injected into every task.

Read policy can consider:

- relevance;
- scope;
- freshness;
- authority;
- sensitivity;
- user intent;
- current task.

## Anti-Pattern: Infinite Transcript

Keeping a full transcript forever is not the same as designing memory.

Transcripts are useful evidence.

Memory is selective, structured retention.

## Anti-Pattern: Memory as Ground Truth

A memory store can contain:

- old information;
- mistaken information;
- inferred information;
- user-changed preferences.

Memory should not automatically override current instructions or authoritative knowledge.

## Exercise

Design a memory record for a generic preference.

Include:

1. subject;
2. content;
3. source;
4. scope;
5. confidence;
6. created time;
7. expiry;
8. sensitivity;
9. update rule.

## Takeaway

> Memory is useful only when the system can reason about why it exists and whether it still applies.

Next: **02 — Working, Episodic, Semantic and Procedural Memory**.
