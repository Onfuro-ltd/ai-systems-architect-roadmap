# 03 — Proprietary Knowledge and Evidence Architecture

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **03 — Proprietary Knowledge and Evidence Architecture** within Domain-Specific AI Systems;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Make private organizational knowledge useful to AI while preserving authority, permissions and provenance.

## Knowledge sources

Sources may include policies, manuals, contracts, product information, research, tickets, decisions, structured databases and expert-authored guidance.

## Authority

Classify sources by authority and purpose. A historical support message should not silently override an approved policy.

## Retrieval architecture

```text
Identity + domain task
      ↓
Authorized source scope
      ↓
Hybrid retrieval / query / tools
      ↓
Reranking + freshness
      ↓
Minimum sufficient evidence
      ↓
Model
```

## Current facts

Use live authoritative systems for volatile state rather than stale embedded documents when possible.

## Provenance

Preserve source, section/record, version, timestamp and transformation for material evidence.

## Conflicts

When authoritative sources conflict, surface the conflict or apply an explicit precedence rule.

## Knowledge lifecycle

Support review, supersession, deletion and re-indexing so derived AI knowledge follows source governance.

## Exercise

Design a domain knowledge layer containing both approved policies and rapidly changing operational data.

## Takeaway

> Proprietary knowledge creates value when the system knows not only what information says, but how authoritative and current it is.

Next: **04 — Policies, Rules and Decision Boundaries**.
