# Domain 08 — Memory Systems

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
