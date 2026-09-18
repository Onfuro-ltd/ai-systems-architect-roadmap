# 03 — Identity, Context, Memory and Knowledge Plane

## Purpose

Construct the minimum authorized context required for each task.

## Context assembly

```text
Identity + tenant + purpose
          ↓
Task state
          ↓
Authorized memory
          ↓
Authorized knowledge
          ↓
Fresh authoritative data
          ↓
Context budget / selection
          ↓
Model
```

## Identity first

Authorization happens before retrieval. Tenant and user boundaries propagate through memory, indexes, caches and tools.

## Memory types

Separate working/session state, durable user preferences, episodic history and organizational/domain memory. Each needs retention and permission rules.

## Knowledge

Use provenance-aware retrieval for documents and direct tools/queries for volatile authoritative facts.

## Context economics

Context has latency and cost. Select sufficient evidence rather than sending everything available.

## Conflict

Define precedence between authoritative current state, approved policy, curated knowledge, remembered preference and model inference.

## Deletion

Deleting or revoking source information must propagate to derived indexes, caches and memories according to policy.

## Exercise

Design context assembly for a multitenant agent that can use personal preference, company policy and current operational data without crossing boundaries.

## Takeaway

> Context engineering at platform scale is an authorization and data-governance problem before it is a prompting problem.

Next: **04 — Agents, Skills, Workflows and Orchestration**.
