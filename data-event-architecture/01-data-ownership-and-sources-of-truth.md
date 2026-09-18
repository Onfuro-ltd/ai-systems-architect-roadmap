# 01 — Data Ownership and Sources of Truth

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **01 — Data Ownership and Sources of Truth** within Data and Event Architecture;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Before designing events, streams, agents, analytics, or AI context, an architect must determine who owns each business fact.

When several systems can independently redefine the same fact, disagreement is inevitable. Reliable architectures therefore establish authoritative ownership, controlled mutation paths, and explicit rules for derived copies.

> Every important business fact should have a clearly defined authoritative owner.

## 1. What does ownership mean?

Data ownership is not merely where a row is stored. The owner is the domain or system responsible for defining the meaning, validity, lifecycle, and accepted mutations of that fact.

An owner should answer:

- What does this field or entity mean?
- Which transitions are valid?
- Who may change it?
- Which validations apply?
- How are corrections made?
- How are changes exposed to other systems?

Storage location and ownership can differ. Copies may exist in caches, warehouses, indexes, vector stores, analytics systems, or downstream services without becoming authoritative.

## 2. System of record vs source of truth

These terms are often used loosely.

A **system of record** is the authoritative system responsible for maintaining a class of business records.

A **source of truth** is the authoritative value a consumer should rely on for a particular decision.

In a distributed system there may be many legitimate systems of record, each owning a different domain.

```text
Identity service      → user identity
Permissions service   → current authorisation
Order domain          → internal order lifecycle
Inventory domain      → available internal stock
External provider     → provider-side execution status
Ledger                → posted financial entries
```

The goal is not one database for everything. The goal is one clearly defined authority for each fact.

## 3. Authoritative vs derived data

A derived representation must not silently become authoritative.

```text
Authoritative database
        ↓
Domain event
        ↓
Search index
Analytics warehouse
Cache
Vector store
AI context store
```

These downstream representations can be useful and fast, but they may be delayed, transformed, incomplete, or rebuilt.

If a consequential action depends on current truth, the system may need to re-read the authoritative owner before execution.

## 4. Copies need semantics

Every important copy should have an understood relationship to its source.

Ask:

- Where did it come from?
- When was it observed?
- How is it updated?
- What lag is acceptable?
- Can it be rebuilt?
- Can consumers act directly from it?
- What happens when it disagrees with the owner?

A cache with no freshness semantics is a future correctness bug.

## 5. Ownership should follow domain responsibility

Good ownership usually follows business capability rather than database convenience.

For example, a commerce system may separate:

```text
Catalogue domain  → product definitions
Inventory domain  → stock state
Order domain      → order lifecycle
Pricing domain    → approved commercial prices
Identity domain   → users and principals
Policy domain     → permissions and controls
```

Other domains consume those facts through contracts rather than independently redefining them.

## 6. The shared-database trap

A shared database can be operationally convenient, especially in a modular monolith. The danger begins when modules treat each other's tables as undocumented internal APIs.

```text
Module A writes table owned by B
Module C derives different meaning from B
Module D bypasses B's validation
```

Physical co-location does not remove logical ownership.

Even inside one database, define which module owns each entity and require mutations to pass through its rules.

## 7. External systems can own facts

Sometimes the authoritative state lives outside your platform.

An external provider may be authoritative for whether it accepted a remote operation, while your system remains authoritative for the workflow that requested and reconciled that operation.

This creates two distinct facts:

```text
Our intent:        "We requested operation X"
External outcome:  "Provider confirms X occurred"
```

Never collapse them into one assumption.

A timeout does not prove that an external operation failed. Reconciliation may be required before retrying.

## 8. Authority can be contextual

Two values that appear to conflict may answer different questions.

For example:

```text
Physical stock observed locally
Reserved stock
Available-to-promise stock
External-channel reported stock
Projected stock
```

There may be no single useful field called `stock`.

The architecture should define the semantic meaning and owner of each quantity rather than trying to force all representations into one ambiguous value.

## 9. Write ownership

The strongest ownership rule is often about writes.

```text
Many readers
     ↓
One controlled mutation boundary
     ↓
Authoritative state
```

Other services should normally request a change through an API, command, domain service, or controlled workflow rather than directly mutating another domain's records.

This preserves invariants and auditability.

## 10. Read models are allowed to differ

Different consumers need different representations.

A transactional service may need normalized entities. A dashboard may need aggregates. Search may need denormalized documents. AI may need a compact contextual representation.

That is healthy when lineage remains clear:

```text
Authoritative state
      ↓
Transformation
      ↓
Purpose-specific read model
```

Do not confuse a purpose-specific view with a competing truth.

## 11. AI introduces a dangerous new copy

Once business information enters a prompt or context window, it becomes another snapshot.

```text
Authoritative state at T0
        ↓
Context assembled at T1
        ↓
Model reasons until T2
        ↓
Action proposed at T3
```

The world may have changed between T0 and T3.

For consequential actions:

```text
AI proposal
    ↓
Re-read critical facts
    ↓
Validate current preconditions
    ↓
Permission / policy check
    ↓
Execute
```

The model's context is evidence for reasoning, not a transaction lock.

## 12. AI outputs are not authoritative facts by default

A model may produce:

- a classification;
- an extracted field;
- a forecast;
- a recommendation;
- a summary;
- a proposed action.

Those outputs should carry appropriate semantics.

```text
prediction ≠ fact
recommendation ≠ approval
extraction ≠ verified record
proposal ≠ execution
```

An AI-generated value can become authoritative only through a defined validation and acceptance process appropriate to its risk.

## 13. Provenance

Important data should retain enough provenance to answer where it came from.

Useful metadata may include:

```text
source_system
source_record_id
observed_at
received_at
schema_version
tenant_id
correlation_id
transformation_version
confidence/status where applicable
```

Do not collect metadata merely because it is possible. Preserve what is needed for correctness, audit, debugging, reconciliation, and governance.

## 14. Freshness is part of meaning

Some facts change slowly. Others become dangerous when stale.

A product description may tolerate minutes of lag. A permission decision or rapidly changing operational quantity may require a fresh authoritative read.

Define freshness expectations by use case:

```text
Data class → acceptable age → consequence if stale → refresh strategy
```

Do not use one global TTL as a substitute for reasoning about business risk.

## 15. Conflict resolution

When copies disagree, the architecture should not improvise.

Define:

1. authoritative owner;
2. precedence rules;
3. reconciliation mechanism;
4. correction process;
5. audit trail;
6. downstream repair or replay strategy.

A conflict is often evidence that ownership or synchronization semantics were never made explicit.

## 16. Multi-tenant ownership

In multi-tenant systems, ownership includes tenant scope.

A record is not fully identified merely by its business identifier if that identifier is only unique within a tenant.

```text
tenant_id + domain identifier
```

Tenant identity must propagate through database access, events, jobs, caches, indexes, AI retrieval, observability, and audit records.

Never rely on the model to enforce tenant isolation.

## 17. Data ownership and permissions are different

The system that owns a fact does not automatically grant every caller permission to read or mutate it.

```text
Ownership answers:    Who defines truth?
Authorisation answers: Who may access/change it?
```

Both boundaries are required.

## 18. Data contracts

Consumers should depend on intentional contracts rather than implementation details.

A contract should communicate enough meaning to use data correctly:

- identifiers;
- semantics;
- units;
- nullability;
- timestamps;
- versioning;
- ownership;
- tenant scope;
- freshness expectations where relevant.

Later chapters will extend this into event contracts and schema evolution.

## 19. Reconciliation

Distributed systems eventually disagree.

Reconciliation compares authoritative state with external or derived representations and repairs divergence safely.

```text
Expected state
      ↓
Observed state
      ↓
Compare
      ↓
Classify difference
      ↓
Repair / investigate / accept
      ↓
Audit result
```

Reconciliation is not evidence that the architecture failed. For external and eventually consistent systems, it is often part of the architecture.

## 20. Ownership registry

For complex systems, maintain a lightweight ownership catalogue.

| Data / entity | Authoritative owner | Allowed writers | Consumers | Freshness | Rebuildable? |
|---|---|---|---|---|---|
| Example entity | Domain A | Domain A | B, C | seconds | no |
| Search projection | Derived index | projector | UI | minutes | yes |
| AI summary | AI workflow | workflow | reviewer | contextual | yes |

The exact tooling is less important than making responsibility discoverable.

## 21. Generic multichannel commerce example

Consider a platform integrating several external sales channels.

A useful ownership model might distinguish:

```text
External channel
    owns provider-side acknowledgement/status

Integration boundary
    owns normalized observation + sync cursor

Order domain
    owns internal order lifecycle

Inventory domain
    owns internal availability rules

Analytics projection
    owns no transactional truth

AI decision service
    owns recommendations, not underlying facts
```

An AI system can combine these sources to recommend an action. Before executing a consequential change, deterministic services revalidate the required authoritative state.

## 22. Anti-patterns

Avoid:

- multiple services independently writing the same business fact;
- treating a warehouse as transactional truth without explicit design;
- letting search indexes become accidental systems of record;
- treating cached values as current merely because they exist;
- allowing AI-generated fields to overwrite authoritative data without validation;
- copying data without provenance;
- querying another module's private tables as a permanent integration contract;
- assuming an external timeout means nothing happened;
- using ambiguous names such as `status` or `stock` without domain semantics;
- resolving conflicts with "last write wins" when business meaning requires more.

## 23. Architect checklist

For every important data class, ask:

- What exactly does this fact mean?
- Who owns its definition?
- Who may write it?
- Where is authoritative state stored?
- Which copies exist?
- How fresh must each copy be?
- How are changes propagated?
- How are conflicts detected?
- How are conflicts reconciled?
- What provenance is required?
- What tenant/security boundary applies?
- Can derived copies be rebuilt?
- Can AI consume this representation safely?
- Must current state be revalidated before action?
- What happens if the owner is unavailable?

## 24. Exercise

Choose one business entity with at least three downstream consumers.

Document:

1. its authoritative owner;
2. allowed writers;
3. invariants;
4. derived copies;
5. freshness requirements;
6. propagation method;
7. reconciliation strategy;
8. tenant/security boundary;
9. how an AI system may consume it;
10. which facts must be revalidated before an AI-proposed action executes.

Then draw the complete path from authoritative mutation to downstream consumption.

## Takeaway

> Data ownership is the foundation of reliable distributed and AI systems. Define who owns each fact, treat every downstream representation as a copy with explicit semantics, and never allow probabilistic reasoning to silently redefine authoritative state.

Next: **02 — Events, Commands and State**.
