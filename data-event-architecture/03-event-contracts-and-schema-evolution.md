# 03 — Event Contracts and Schema Evolution

## Purpose

Events become long-lived integration contracts. Once multiple consumers depend on them, changing a payload is no longer a local refactor.

> Treat published events as versioned public contracts: evolve them deliberately, preserve meaning, and assume old events and old consumers will exist longer than expected.

## 1. An event is more than JSON

An event contract includes semantics as well as fields. Consumers need to know what happened, when it happened, which entity it concerns, who produced it, what version it uses, and what guarantees apply.

A structurally valid message can still be semantically wrong.

## 2. Contract anatomy

A useful event envelope may contain:

```json
{
  "event_id": "evt_...",
  "event_type": "inventory.adjusted",
  "event_version": 2,
  "occurred_at": "...",
  "producer": "inventory",
  "tenant_id": "...",
  "correlation_id": "...",
  "causation_id": "...",
  "subject_id": "...",
  "payload": {}
}
```

Not every system needs every field. Standardize only metadata that has clear operational value.

## 3. Separate envelope from payload

The envelope carries cross-cutting transport and tracing metadata. The payload describes the domain fact.

This separation makes infrastructure concerns consistent while allowing domain schemas to evolve independently.

## 4. Events describe facts, not database rows

Avoid publishing raw table snapshots as the integration contract merely because they are easy to serialize.

```text
Bad contract:
row_updated { every database column }

Better contract:
order_shipping_address_changed { order_id, relevant business fields }
```

Database schemas optimize persistence. Event schemas communicate business meaning.

## 5. Schema compatibility

Changes generally fall into compatibility categories:

- **backward compatible** — new consumers can read older data;
- **forward compatible** — old consumers can tolerate newer data;
- **full compatible** — both directions are supported;
- **breaking** — coordinated migration or a new contract is required.

The exact guarantees depend on serialization technology and consumer behaviour.

## 6. Additive changes are usually safer

Adding an optional field is often easier to evolve than renaming, removing, changing type, changing units, or changing semantic meaning.

But additive does not automatically mean safe. A consumer that rejects unknown fields can still break.

Compatibility must be tested, not assumed.

## 7. Semantic changes are schema changes

Changing `amount` from tax-exclusive to tax-inclusive without changing the field name may pass every schema validator while corrupting downstream logic.

Changing meaning requires explicit migration even if the wire type remains identical.

## 8. Units and representation

Make units unambiguous.

Prefer contracts such as:

```text
weight_grams
currency + amount_minor
occurred_at UTC timestamp
quantity integer with documented semantics
```

over context-dependent fields such as `weight`, `price`, or `date` whose meaning consumers must guess.

## 9. Required vs optional fields

A required field creates a stronger dependency. Require fields when the event cannot be interpreted correctly without them.

Optional fields should have defined absence semantics. Missing should not ambiguously mean zero, false, unknown, not applicable, or not yet calculated.

## 10. Null is part of the contract

Distinguish where necessary:

```text
field absent
field present with null
field present with empty value
field present with zero
```

These may represent different domain states.

## 11. Versioning strategies

Common approaches include:

### In-schema evolution
Keep the same event type while making compatible changes.

### Explicit version field
Use `event_version` and support multiple payload versions.

### Versioned event names
For major semantic breaks, publish a new contract such as `customer.registered.v2`.

No strategy removes the need for migration discipline.

## 12. Upcasting

Historical events can sometimes be transformed into the current in-memory representation when read.

```text
Stored v1 event
      ↓
Upcaster
      ↓
Current representation
```

Upcasting can simplify consumers, but transformations must be deterministic and must not invent historical facts that were never captured.

## 13. Downcasting and dual publishing

During migration, a producer may temporarily support old and new contracts or publish both representations.

This can reduce coordination risk but creates operational complexity. Define an explicit migration window and retirement condition rather than supporting both forever.

## 14. Consumer-driven compatibility

Before changing a shared contract, understand real consumer dependencies.

Useful controls include schema registries, contract tests, compatibility checks in CI, consumer inventories, deprecation notices, and telemetry showing which versions remain in use.

## 15. Unknown fields should usually be tolerated

Consumers that deserialize only what they understand are easier to evolve than consumers that fail because a producer added unrelated information.

Strict validation still matters for fields the consumer relies upon.

## 16. Never silently reuse a field

Do not repurpose a deprecated field for a new meaning merely because the type happens to fit. Historical consumers, replay, analytics, and audit systems may still interpret the original semantics.

Create a new field or contract.

## 17. Event time vs processing time

Contracts should distinguish when the business event occurred from when infrastructure received or processed it.

```text
occurred_at  → domain time
received_at  → ingestion time
processed_at → consumer time
```

This matters for late events, analytics, replay, reconciliation, and AI context freshness.

## 18. Identity, correlation and causation

`event_id` identifies the event itself.

`correlation_id` groups activity belonging to the same broader workflow.

`causation_id` identifies the command or event that directly caused this event.

These fields make distributed workflows far easier to trace.

## 19. Tenant and security context

Multi-tenant event systems should carry enough trusted context to enforce isolation, but consumers must not blindly trust security-sensitive metadata from untrusted producers.

Tenant identity should be validated at trusted boundaries and propagated consistently.

Do not place secrets or unnecessary sensitive information into broad event streams.

## 20. Data minimization

Events are often copied into brokers, logs, warehouses, replay stores, and observability systems. Publishing sensitive data creates many downstream obligations.

Prefer identifiers and purpose-limited fields when consumers can retrieve protected details through authorized interfaces.

## 21. Event retention affects contract evolution

If events are retained for years, old schemas become part of the long-term architecture.

Ask whether historical events must remain readable, replayable, auditable, or legally deletable. Schema strategy must match retention strategy.

## 22. Replay compatibility

A new consumer may encounter events produced years earlier. Test replay across supported historical versions.

Never assume that because today's producer emits v4, every stored event is v4.

## 23. AI consumers need contracts too

Do not feed arbitrary evolving event payloads directly into prompts and hope the model adapts.

Use a deterministic adaptation layer:

```text
Versioned event
      ↓
Schema validation
      ↓
Canonical internal representation
      ↓
Context builder
      ↓
AI model
```

This preserves model independence and prevents infrastructure changes from silently altering prompt semantics.

## 24. AI-derived events require provenance

If a system publishes an event based on probabilistic interpretation, distinguish the interpretation from verified business truth.

Useful metadata may include model/instruction version, source identifiers, confidence or validation status where meaningful, and whether human or deterministic acceptance occurred.

For example:

```text
DocumentClassificationProposed
```

is semantically different from:

```text
DocumentClassificationApproved
```

## 25. Contract ownership

Every published contract needs an accountable owner responsible for semantics, evolution, documentation, deprecation, and migration communication.

Shared ownership often becomes no ownership.

## 26. Contract documentation

For each important event document:

- event name and purpose;
- producer/owner;
- triggering business condition;
- payload semantics;
- identifiers and units;
- ordering assumptions;
- delivery assumptions;
- versioning policy;
- privacy classification;
- retention expectations;
- example payload;
- known consumers where practical.

## 27. Contract testing

Test more than serialization.

Include producer schema validation, consumer compatibility, old-event replay, unknown-field tolerance, missing optional fields, invalid enum values, timestamp handling, tenant isolation, and semantic invariants.

## 28. Migration pattern

A controlled breaking migration can look like:

```text
Define new contract
      ↓
Add producer support
      ↓
Deploy compatible consumers
      ↓
Dual publish / translate if required
      ↓
Measure old-version usage
      ↓
Migrate remaining consumers
      ↓
Stop old publication
      ↓
Retire old compatibility path
```

Each stage should have rollback and observability.

## 29. Anti-patterns

Avoid:

- publishing database rows as permanent public contracts;
- renaming fields without migration;
- changing units without versioning;
- treating JSON as self-documenting;
- deleting old schemas while retained events still use them;
- consumers rejecting harmless unknown fields;
- event types such as `entity_updated` with no domain meaning;
- putting secrets into broadly consumed events;
- embedding unversioned AI prompt text as business truth;
- changing event semantics because only one known consumer exists today;
- dual publishing forever with no retirement plan.

## 30. Architect checklist

Before approving an event contract, ask:

- What business fact does this event represent?
- Who owns the contract?
- Is the event name semantically precise?
- Are identifiers, units, timestamps, and null semantics explicit?
- What compatibility guarantee is required?
- How will the schema evolve?
- Can old consumers tolerate new events?
- Can new consumers process retained old events?
- Are tenant and privacy boundaries preserved?
- Is unnecessary sensitive data excluded?
- Are correlation and causation traceable?
- Can replay work across versions?
- Are AI consumers isolated behind canonical adapters?
- How is deprecation measured and completed?

## 31. Exercise

Design a versioned event contract for a generic operational system. Start with v1, then introduce three changes:

1. an additive optional field;
2. a semantic change that requires migration;
3. a new privacy constraint that means one field should no longer be broadly published.

Document compatibility, migration steps, replay handling, consumer tests, and retirement criteria.

## Takeaway

> Event schemas are long-lived interfaces between independently changing systems. Preserve meaning, evolve them deliberately, test compatibility, and isolate AI from raw contract churn through deterministic canonical representations.

Next: **04 — Delivery, Ordering and Idempotent Consumers**.
