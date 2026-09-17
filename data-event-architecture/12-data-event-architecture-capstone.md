# 12 — Data and Event Architecture Capstone

## Purpose

Design the data and event backbone of an enterprise-grade, multitenant, AI-assisted operational platform.

> Move facts through deterministic contracts; let AI interpret them inside controlled boundaries; make every consequential transition back into business state explicit, validated, authorized, and auditable.

## Scenario

Design a generic platform integrating several external operational systems. It maintains authoritative business state, serves isolated tenants, ingests APIs/webhooks/files/events/CDC, builds operational and analytical projections, maintains AI search/vector context, performs asynchronous AI enrichment, and lets AI propose selected consequential actions.

The system must survive duplicates, delays, outages, stale context, schema evolution, replay, and ambiguous external outcomes.

## 1. Data classification and ownership

Inventory:

1. authoritative facts;
2. events;
3. commands/intents;
4. derived information;
5. AI interpretations.

For each critical fact document authoritative owner, write path, read copies, freshness requirement, conflict rule, reconciliation, tenant scope, and sensitivity.

## 2. Command, event and state model

For at least three workflows show:

Intent → command → validation → authoritative transition → event → consumers/projections.

AI proposals must remain separate from commands and completed facts.

## 3. Event contracts and evolution

Design versioned contracts with stable event ID, type/version, producer, occurred time, tenant, aggregate/entity identity, correlation/causation, and purpose-limited payload.

Demonstrate one additive evolution and one breaking semantic evolution, including consumer migration, historical replay, compatibility testing, deprecation, and retirement.

## 4. Delivery and idempotency

Assume duplicates, delays, retries, restarts, and out-of-order delivery.

Define event identity, business idempotency keys, ordering scope, sequence/version rules, poison handling, retries, quarantine, backpressure, and tenant fairness.

## 5. Outbox and inbox

Design:

Authoritative mutation + outbox → publisher/CDC → broker → inbox + consumer mutation → next outbox.

Walk through crash points and prove each path completes, retries safely, or enters an explicit recoverable state.

## 6. External actions

For one consequential external operation:

Accepted intent → durable action record → external call with idempotency where available → verified outcome.

Support UNKNOWN and reconciliation before unsafe retry.

## 7. CDC

Choose where CDC is justified and where explicit domain events are better. Define snapshot bootstrap, checkpoint position, schema evolution, deletes, lag, source-log retention margin, tenant identity, recovery, and reconciliation.

Do not expose raw database mutations as permanent business contracts without justification.

## 8. Streaming, batch and hybrid processing

Define freshness requirements first. Use streaming only where justified, batch where simpler, and hybrid processing where both freshness and rebuildability matter.

Include event-time semantics, late-data policy, checkpoints, recovery storms, tenant fairness, batch partitioning, and reconciliation.

## 9. Event sourcing and replay

Choose one domain and write an ADR deciding whether event sourcing is justified. Compare it with current-state persistence plus outbox/audit.

Define projection replay, historical simulation, business re-execution, and external side effects separately. Replay must not accidentally recreate consequential effects.

## 10. Lineage and provenance

For one AI-assisted action trace:

Authoritative source → event/CDC → projection → context → AI proposal → validation → policy/permission → human approval where required → idempotent execution → verified outcome → audit/evaluation.

Preserve observable evidence, not hidden model reasoning.

## 11. Data quality

Define controls for correctness, completeness, freshness, uniqueness, consistency, validity, provenance, and tenant isolation.

Specify quality SLOs, quarantine, reconciliation, ownership, and incident response.

## 12. AI context boundary

Design a provider-neutral context layer:

Authorized sources → freshness/schema/tenant validation → canonical context → model adapter → structured proposal.

Before consequential execution: re-read critical authoritative state, verify version/preconditions, apply policy/permission, obtain approval where required, then execute idempotently.

## 13. Feedback-loop protection

Show how AI-generated data is labeled with provenance and verification state so it cannot silently become independent ground truth through CDC, analytics, vector indexing, memory, or future training.

## 14. Multi-tenancy

Prove tenant identity survives request → database → event → queue → CDC → consumer → cache/index → AI context → action → audit.

Test cross-tenant access attempts and noisy-tenant pressure.

## 15. Failure matrix

Your design must explicitly handle duplicate events, out-of-order events, broker outage, consumer crash after commit, external timeout after possible success, CDC outage, schema incompatibility, streaming backlog, stale AI context, wrong-tenant context, projection corruption, and replay attempts against side-effect consumers.

## 16. Observability

The platform must answer:

Where did this fact originate? Which version was used? How fresh was it? Which event moved it? Was delivery duplicated? Which consumer processed it? What transformation occurred? Did AI use it? What policy applied? Who approved? What action was attempted? What outcome was verified? Can derived state be rebuilt?

Use metrics, traces, logs, audit records, lineage metadata, and alerts according to purpose.

## 17. Required deliverables

Produce a system/data context diagram, source-of-truth registry, command/event/state model, event contract catalogue, schema-evolution plan, outbox/inbox design, delivery/idempotency design, CDC architecture, streaming/batch decision matrix, replay plan, event-sourcing ADR, lineage graph, quality SLOs, AI context boundary, tenant-isolation model, failure matrix, observability/audit plan, and at least three ADRs.

## 18. Architecture review

Challenge every important assumption:

- Why is each fact authoritative where it is?
- What happens when copies disagree?
- What happens when events duplicate, disappear, or reorder?
- Can every important derived representation be repaired?
- What happens after a long outage and during backlog recovery?
- Can old schemas still be replayed?
- Can replay trigger side effects?
- Can one tenant affect another?
- Can sensitive data leak through events or lineage?
- Can AI-generated content become false ground truth?
- Can stale AI context cause action?
- Can outcomes be explained without hidden chain-of-thought?
- Is every piece of complexity justified?

## 19. Acceptance criteria

The design passes only if ownership is explicit; commands/events/state/derived data/AI interpretations are separated; contracts evolve safely; duplicates and ordering failures are controlled; dual writes are safe; CDC recovers and reconciles; streaming has measurable justification; derived state is rebuildable where required; replay cannot recreate side effects accidentally; provenance connects evidence to outcome; quality failures are visible; tenant isolation survives every path; AI context is authorized and freshness-aware; consequential execution revalidates truth; and AI output cannot silently redefine authoritative state.

## Final architecture

Authoritative facts → versioned deterministic contracts → reliable delivery/CDC → derived operational and analytical views → authorized provenance-aware AI context → probabilistic reasoning → structured proposal → fresh authoritative revalidation → policy/permission/approval → idempotent execution → verified outcome → audit/evaluation/controlled learning.

> AI may interpret the data plane. It must not silently become the data plane.

## Takeaway

> A trustworthy AI-native system has an explicit architecture for truth: who owns facts, how changes propagate, how copies are repaired, how evidence is traced, and how probabilistic reasoning is prevented from silently becoming authoritative state.

**Domain 13 — Data and Event Architecture complete.**

Next domain: **14 — Open-Source and Local AI**.
