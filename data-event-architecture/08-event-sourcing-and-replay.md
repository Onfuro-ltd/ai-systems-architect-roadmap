# 08 — Event Sourcing and Replay

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **08 — Event Sourcing and Replay** within Data and Event Architecture;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Event sourcing stores domain events as the authoritative history from which current state can be reconstructed.

> Event-driven architecture uses events to communicate. Event sourcing uses events as the authoritative record of state change.

## Core distinction

A conventional event-driven system can keep current database state as authority and publish events for integration. An event-sourced aggregate makes its event history authoritative and derives current state by replay.

Event sourcing therefore is not a synonym for using a broker, keeping audit logs, or publishing domain events.

## Aggregate lifecycle

Command → load history → reconstruct state → validate invariants → produce new events → append using expected aggregate version.

Optimistic concurrency prevents competing writers from silently creating incompatible histories.

## Event store

Durable events need stable event identity, aggregate identity, sequence/version, event type/version, occurrence time, payload, and appropriate correlation, tenant, and provenance metadata.

Events represent facts that happened. Commands represent requests.

## Snapshots

Long histories may use snapshots for performance. A snapshot at version 900 plus events 901 through current can reconstruct current state faster.

Snapshots are derived acceleration structures, not replacements for authoritative event history.

## Projections

Events can build operational views, dashboards, search representations, analytics, and other read models. Important projections should be rebuildable where replayability is part of the design.

## Replay

Replay can rebuild projections, repair bugs, introduce new read models, test new logic, and perform historical analysis. It can also accidentally repeat payments, messages, shipments, refunds, or external actions.

A replay plan must define scope, event range, schema versions, consumer version, side-effect suppression, tenant boundary, capacity limits, checkpoints, validation, and recovery.

## Historical rules

Old events describe facts produced under historical rules. Replaying them through current command rules can create a state that never historically existed.

Version event interpretation where needed. Never invent information that old events did not contain.

## Event sourcing and CQRS

They are separate patterns. CQRS can exist without event sourcing, and event sourcing does not require elaborate distributed CQRS infrastructure.

## When to use it

Event sourcing is strongest when temporal reconstruction, historical transitions, replay, complex aggregate invariants, or rebuildable projections create substantial domain value.

For straightforward CRUD domains, current-state persistence plus outbox and audit history is often simpler.

Selective event sourcing is valid: use it only for domains where benefits exceed lifecycle cost.

## Privacy and governance

Append-only history does not remove privacy obligations. Define retention, deletion/redaction strategy, encryption, access controls, tenant isolation, administrative replay permissions, and audit requirements.

An event store can support auditability but is not automatically a complete compliance audit system.

## AI boundary

Event histories can provide rich temporal evidence to AI, but do not dump unbounded history directly into prompts. Build deterministic, provenance-aware temporal projections.

AI proposal → validation/policy/permission → accepted command/transition → authoritative event.

Unverified model output must not silently become authoritative history.

Historical events can also support counterfactual AI evaluation. Simulation outputs must remain isolated from production facts.

## Observability and testing

Monitor append failures, concurrency conflicts, projection lag, replay progress, snapshot age, schema/upcaster failures, tenant backlog, and reconciliation.

Test reconstruction, concurrency, historical schema versions, snapshots, projection rebuild, replay isolation, side-effect suppression, long histories, and privacy controls.

## Anti-patterns

Avoid event-sourcing every table, mutating historical facts casually, replaying into live side effects, treating snapshots as authority, blindly applying current rules to historical events, using unversioned events, or placing unverified AI output into authoritative history.

## Architect checklist

Ask whether history is valuable enough to justify the pattern; how concurrency, schema evolution, snapshots, privacy, replay, projections, side effects, tenancy, and recovery work; and whether a simpler state-plus-outbox design satisfies the requirement.

## Exercise

Design a generic approval workflow twice: first as an event-sourced aggregate with commands, events, invariants, snapshots, projections, replay and AI recommendation; then as conventional state plus outbox/audit. Explain the trade-offs.

## Takeaway

> Event sourcing is a deliberate choice to make domain history authoritative. Use it when temporal reconstruction and replay create real value, not simply because events exist.

Next: **09 — Data Lineage, Provenance and Audit**.
