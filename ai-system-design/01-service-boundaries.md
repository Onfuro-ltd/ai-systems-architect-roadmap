# 01 — Service Boundaries

## Purpose

Service boundaries define where responsibilities, data ownership, failure domains, permissions, and scaling decisions begin and end. In AI systems, boundaries are especially important because probabilistic model behaviour must not be allowed to silently redefine critical business invariants.

## Core principle

> A service boundary should represent a coherent responsibility and a meaningful operational boundary—not merely a convenient code folder.

## 1. Why boundaries matter

Poor boundaries create:

- shared mutable state;
- hidden coupling;
- cascading failures;
- difficult deployments;
- unclear ownership;
- security leakage;
- inability to scale individual workloads.

Good boundaries provide:

- explicit contracts;
- isolated failure domains;
- clear data ownership;
- independent scaling where justified;
- controlled permissions.

## 2. AI-specific boundary rule

Do not make the model the system boundary.

A model should normally sit inside an application capability with deterministic controls around it.

```text
API / Event
    ↓
Application Service
    ↓
AI Orchestrator
    ├── Model
    ├── Retrieval
    └── Tools
    ↓
Validation / Policy
    ↓
Business System
```

## 3. Capability-oriented boundaries

A useful boundary represents a business or technical capability such as:

- catalogue intelligence;
- pricing analysis;
- order processing;
- inventory management;
- notification delivery;
- AI evaluation.

Avoid creating a separate service for every model call or tiny abstraction.

## 4. Data ownership

Each important dataset should have a clear owner.

```text
Service A → owns Dataset A
Service B → owns Dataset B
```

Other services should interact through explicit contracts rather than directly mutating another service's internal state.

This becomes critical in multi-tenant AI systems because tenant isolation must survive service boundaries.

## 5. Synchronous vs asynchronous boundaries

Use synchronous execution when the caller needs an immediate bounded result and latency is predictable.

Use asynchronous execution when work is:

- long-running;
- expensive;
- retryable;
- bursty;
- dependent on external APIs;
- suitable for eventual completion.

AI inference, agent workflows, document processing, and large-scale analysis often benefit from asynchronous boundaries.

## 6. Failure-domain design

A boundary should help contain failure.

For example:

```text
Marketplace API failure
        ↓
Integration boundary
        ↓
Retry / queue
        ↓
Core platform remains available
```

Do not allow a slow or unavailable AI provider to bring down unrelated transactional operations.

## 7. Security boundaries

Different capabilities should have different permissions.

For example:

```text
Read analytics
      ≠
Modify inventory
      ≠
Execute financial action
```

AI agents should cross these boundaries only through explicit, authorised capabilities.

## 8. Transactional boundaries

Critical state changes should have deterministic transactional handling where possible.

An AI recommendation should not directly become an irreversible database mutation without validation.

```text
AI proposal
    ↓
Domain validation
    ↓
Transaction
    ↓
Committed state
```

## 9. Avoid distributed systems prematurely

A modular monolith can be the correct architecture when:

- the team is small;
- deployment scale is modest;
- transaction boundaries are closely coupled;
- independent scaling is unnecessary.

Microservices should solve a demonstrated organisational or operational problem—not be adopted because AI systems sound sophisticated.

## 10. SEMLIS application

SEMLIS can maintain strong internal domain boundaries even while operating as a modular platform.

Potential boundaries include:

```text
Marketplace Integrations
        ↓
Commerce Data
        ↓
Intelligence / Decision Engine
        ↓
AI Orchestration
        ↓
Policy / Permissions
        ↓
Execution
```

This allows the intelligence layer to evolve without giving it ownership of transactional marketplace state.

## 11. Boundary decision checklist

For every proposed service or module, ask:

1. What responsibility does it own?
2. What data does it own?
3. What contract does it expose?
4. What permissions does it require?
5. What happens when it fails?
6. Can it be tested independently?
7. Does it need independent scaling?
8. Does the boundary reduce or increase coupling?
9. Is a separate service actually justified?
10. Can an AI component fail without corrupting critical state?

## Takeaway

> Good AI architecture does not isolate everything. It creates the right boundaries around responsibility, state, permissions, and failure.

The most important boundary is often between **probabilistic intelligence** and **deterministic business state**.
