# Domain 08 — Memory Systems

## Learning objectives

By the end of this domain, you should be able to:

- explain the core concepts and distinctions across working, episodic, semantic and procedural memory, retrieval, consolidation, forgetting, privacy and memory evaluation.
- build or evaluate a representative implementation rather than relying on a demo;
- make architecture decisions that account for reliability, security, cost, scale and operations;
- define the evidence, evaluation and governance required before production adoption.

## Purpose

This domain explains how AI systems retain, retrieve, update and forget information across interactions and events.

The goal is not to make systems remember everything. The goal is to design memory that is useful, bounded, inspectable, privacy-aware and appropriate to the task.

## Core Principle

> Memory is selective retention across time, not an unlimited transcript.

A useful architecture separates:

```text
Context   = what the model sees now
Knowledge = authoritative information it can retrieve
Memory    = retained information derived across interactions or events
State     = current execution or workflow condition
```

These layers can interact, but they solve different problems.

## What This Domain Covers

1. Memory foundations
2. Working, episodic, semantic and procedural memory
3. Memory write, retrieval and ranking
4. Summarisation, consolidation and compression
5. Forgetting, staleness and conflict
6. Memory architecture and storage patterns
7. Privacy, security and user control
8. Memory evaluation and observability
9. Capstone architecture

## Why Memory Needs Architecture

A system that simply stores every conversation can become:

- expensive;
- noisy;
- privacy-invasive;
- difficult to correct;
- vulnerable to stale information;
- difficult to explain;
- hard to govern.

Useful memory requires decisions about what is retained, why it is retained, how long it remains valid and when it should be ignored or removed.

## Memory Is Not Context

Context is the information currently presented to the model.

Memory is a source of retained information that may later contribute to context.

A memory system therefore usually sits upstream of context assembly:

```text
Past Interactions / Events
          |
          v
Memory Write Pipeline
          |
          v
Memory Store
          |
          v
Retrieve / Rank / Filter
          |
          v
Context Assembly
          |
          v
Model
```

## Memory Is Not Knowledge

Knowledge systems primarily expose authoritative reference information.

Memory often contains information derived from past interactions, observations or decisions.

Examples:

**Knowledge**
- policy;
- documentation;
- product catalogue;
- reference data.

**Memory**
- user preference;
- prior decision;
- recurring constraint;
- previous outcome;
- learned workflow pattern.

A fact can move between these categories depending on system design, but the distinction helps engineers reason about authority and freshness.

## Memory Is Not State

Workflow state tells the system where an execution currently is.

Memory can persist beyond a workflow and influence future interactions.

Examples of state:

- current task;
- pending approval;
- retry count;
- current workflow step.

Examples of memory:

- preferred output format;
- recurring business preference;
- previous approved decision;
- remembered interaction history.

## Memory Quality

High-quality memory should be:

- relevant;
- attributable;
- fresh enough for its purpose;
- scoped;
- correctable;
- deletable where required;
- observable.

The objective is not retention volume. It is useful future decision support.

## Mastery Outcomes

### Understand

Explain the differences between context, knowledge, memory and state, and identify major memory types.

### Build

Implement a memory pipeline with explicit write, retrieval, ranking, update and forgetting behaviour.

### Architect

Design a memory subsystem with provenance, lifecycle, privacy, conflict handling and evaluation.

### Lead

Define standards for what an organisation's AI systems may remember, how memory is governed, how users control it and how quality is measured.

## Architectural Rule

> A memory should earn its right to persist.

Do not store information merely because it is available.

Next: **01 — Memory Foundations**.

## Canonical curriculum navigation

- [Memory Foundations](./01-memory-foundations.md)
- [Working, Episodic, Semantic and Procedural Memory](./02-working-episodic-semantic-and-procedural-memory.md)
- [Memory Write, Retrieval and Ranking](./03-memory-write-retrieval-and-ranking.md)
- [Summarisation, Consolidation and Compression](./04-summarisation-consolidation-and-compression.md)
- [Forgetting, Staleness and Conflict](./05-forgetting-staleness-and-conflict.md)
- [Memory Architecture and Storage Patterns](./06-memory-architecture-and-storage-patterns.md)
- [Privacy, Security and User Control](./07-privacy-security-and-user-control.md)
- [Memory Evaluation and Observability](./08-memory-evaluation-and-observability.md)
- [Capstone: Design a Production Memory System](./09-capstone.md)

## Prerequisites and next steps

**Recommended prerequisites:** [04 — Knowledge Systems and RAG](../knowledge-systems-rag/README.md), [05 — Agents](../agents/README.md), [06 — Skills and Agent Harnesses](../06-skills-agent-harnesses/README.md)

**Useful next domains:** [09 — Orchestration and Multi-Agent Systems](../09-orchestration-multi-agent/README.md), [10 — Evaluation and Reliability](../10-evaluation-reliability/README.md), [11 — Security, Permissions and Governance](../11-security-permissions-governance/README.md)

See the [full prerequisite map](../roadmap/prerequisites-and-paths.md) and [domain status matrix](../roadmap/domain-status.md).
