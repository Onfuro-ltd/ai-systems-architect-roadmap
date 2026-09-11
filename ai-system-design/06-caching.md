# 06 — Caching

## Purpose

Caching reduces latency, dependency load, and cost by reusing data or computation that does not need to be recomputed for every request. In AI systems, caching can also reduce model and retrieval spend—but stale cached intelligence can become a business risk.

## Core principle

> Cache only what can safely be reused, define freshness explicitly, and never let performance optimisation silently override correctness.

## 1. What can be cached

Common layers include:

- HTTP responses;
- database query results;
- application objects;
- permissions or configuration;
- external API responses;
- embeddings;
- retrieval results;
- model responses;
- computed analytics.

Each layer has different consistency requirements.

## 2. Cache-aside pattern

A common pattern is:

```text
Request
  ↓
Cache lookup
  ├── hit → return
  └── miss
       ↓
    Source
       ↓
    Store cache
       ↓
    Return
```

The application remains responsible for obtaining authoritative data.

## 3. TTL and freshness

Every cache should have an explicit freshness policy.

```text
Freshness requirement
       ↓
TTL / invalidation strategy
       ↓
Cached value
```

A short TTL may be appropriate for rapidly changing marketplace data. Longer TTLs may be suitable for stable reference data.

## 4. Invalidation

The classic difficulty is knowing when cached data is no longer valid.

Strategies include:

- TTL expiration;
- explicit invalidation;
- event-driven invalidation;
- versioned keys;
- write-through updates;
- stale-while-revalidate.

Use the simplest strategy that meets the correctness requirement.

## 5. Cache consistency

A cache should not become an alternative source of truth by accident.

For critical state:

```text
Authoritative database
        ↓
Cache
```

not:

```text
Cache
  ↕
Database
```

unless the architecture explicitly defines the consistency model.

## 6. Cache stampede

If a popular key expires, many requests may simultaneously rebuild it.

Mitigations include:

- request coalescing;
- locking;
- jittered TTLs;
- stale-while-revalidate;
- prewarming.

## 7. Negative caching

Caching known failures or empty results can reduce repeated expensive requests.

However, negative caches require short or carefully chosen TTLs because a previously missing resource may become available.

## 8. Distributed caching

Distributed caches such as Redis can provide shared cache state across application instances.

Consider:

- network latency;
- eviction policy;
- memory limits;
- availability;
- serialisation;
- key namespaces;
- tenant isolation.

A cache outage should have a defined fallback where possible.

## 9. Tenant isolation

Multi-tenant systems must ensure cache keys cannot collide across tenants.

Prefer explicit namespaces:

```text
tenant:{tenant_id}:resource:{resource_id}
```

Never rely on resource IDs alone when they are not globally unique and authorised.

## 10. AI response caching

Caching model responses can reduce cost and latency for identical or safely equivalent requests.

However, AI caching requires considering:

- prompt changes;
- model version;
- system-policy version;
- retrieved context;
- user permissions;
- data freshness;
- tool state.

A cache key that ignores these dimensions can return an answer generated under obsolete assumptions.

## 11. Semantic caching

Semantic caches attempt to reuse results for meaningfully similar prompts rather than exact matches.

This can be useful, but it introduces additional risk:

```text
Similar question
      ≠
Same required answer
```

Semantic caching should therefore be restricted to workflows where approximate equivalence is acceptable and validated.

## 12. RAG caching

Useful candidates include:

- embeddings;
- document parsing;
- retrieval results;
- reranking results.

But invalidation should occur when source content or retrieval configuration changes.

Versioning can help:

```text
Document version
+
Embedding model version
+
Chunking version
+
Retrieval configuration
```

## 13. Business-critical data

Do not cache data whose freshness is essential to an irreversible decision unless the decision explicitly tolerates that staleness.

Example:

```text
Cached stock = 20
Actual stock = 2
```

An AI recommendation based on the cached value may be economically wrong even though the cache technically worked.

## 14. Stale-while-revalidate

For some read-heavy workloads:

```text
Request
 ↓
Return recent cached value
 ↓
Refresh asynchronously
```

This provides low latency while maintaining eventual freshness.

It should not be used blindly for transactional decisions.

## 15. Cache invalidation through events

A domain event can trigger invalidation:

```text
Inventory changed
      ↓
Domain event
      ↓
Invalidate inventory cache
      ↓
Next read fetches authoritative value
```

Event-driven invalidation should tolerate duplicate or delayed events.

## 16. SEMLIS application

SEMLIS can use caching at several levels:

```text
Marketplace API responses
        ↓
Normalisation cache
        ↓
Computed analytics
        ↓
Retrieval / intelligence cache
        ↓
UI response cache where appropriate
```

Examples:

- cache relatively stable marketplace metadata;
- cache expensive catalogue calculations with versioned keys;
- cache embeddings until source content changes;
- cache repeated read-only AI explanations when context and policy versions match.

Do not cache rapidly changing stock, order or financial state without an explicit freshness policy.

## 17. Cache observability

Monitor:

- hit rate;
- miss rate;
- eviction rate;
- latency;
- memory utilisation;
- stale-data incidents;
- rebuild frequency;
- stampede events;
- cost saved.

A high hit rate is not automatically good if the cached data is wrong or too stale.

## 18. Enterprise checklist

For every cache, document:

1. What is being cached?
2. What is the authoritative source?
3. What is the acceptable staleness?
4. What is the TTL?
5. How is invalidation triggered?
6. What is the cache key?
7. Does it include tenant/security context?
8. What happens when the cache is unavailable?
9. Can cache stampedes occur?
10. Can stale data cause financial, operational or safety harm?
11. How are model/prompt/data versions represented?
12. How is cache correctness monitored?

## Takeaway

> A cache is a performance mechanism, not a source of truth.

In AI systems, caching must be designed around **freshness, context, permissions and correctness**, not simply hit rate and latency.
