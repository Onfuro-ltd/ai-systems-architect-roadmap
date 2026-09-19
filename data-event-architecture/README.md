# Domain 13 — Data and Event Architecture

AI systems are only as trustworthy as the data, events, state transitions, and contracts that connect them to the real world.

This domain teaches how to design the data and event backbone of an AI-native system: authoritative operational state, event contracts, change propagation, streaming, lineage, quality, governance, replay, and the boundary between deterministic business facts and probabilistic AI interpretation.

> AI can reason about data. It must not be allowed to invent authoritative state.

## Why this domain matters

A production AI system consumes changing information from applications, databases, APIs, users, queues, documents, and external platforms. It may then recommend or trigger actions that create further state changes.

Without disciplined data and event architecture, teams face conflicting sources of truth, duplicate or missing events, stale AI context, broken schema changes, cross-tenant leakage, untraceable derived data, unreliable analytics, and agents acting on facts that are no longer valid.

The objective is not to make every system event-driven. The objective is to make state, ownership, change, provenance, and data movement explicit.

## Learning outcomes

By the end of this domain, you should be able to:

- distinguish operational state from events, commands, derived data, and AI interpretations;
- define authoritative data ownership and system-of-record boundaries;
- design stable event contracts and schema evolution strategies;
- reason about delivery semantics, ordering, duplication, replay, and idempotent consumers;
- use transactional outbox and inbox patterns where cross-system reliability requires them;
- understand change data capture and when it is appropriate;
- design batch, streaming, and hybrid data flows;
- evaluate event sourcing without treating it as a default architecture;
- design lineage, provenance, retention, and auditability;
- enforce tenant, identity, privacy, and permission boundaries throughout data movement;
- build data-quality controls suitable for deterministic software and AI systems;
- separate raw facts, curated data, model outputs, and business decisions;
- design AI consumers that tolerate late, duplicated, stale, incomplete, or corrected information;
- document the trade-offs behind a data architecture.

## Domain structure

```text
data-event-architecture/
├── README.md
├── 01-data-ownership-and-sources-of-truth.md
├── 02-events-commands-and-state.md
├── 03-event-contracts-and-schema-evolution.md
├── 04-delivery-ordering-and-idempotent-consumers.md
├── 05-transactional-outbox-and-inbox.md
├── 06-change-data-capture.md
├── 07-streaming-batch-and-hybrid-dataflows.md
├── 08-event-sourcing-and-replay.md
├── 09-data-lineage-provenance-and-audit.md
├── 10-data-quality-and-observability.md
├── 11-ai-data-boundaries-and-context-freshness.md
└── 12-data-event-architecture-capstone.md
```

## The architectural model

```text
External systems / Users
        ↓
Ingestion boundary
        ↓
Authoritative domain state
        ↓
Durable change/event
   ↙       ↓       ↘
Operations Analytics  AI consumers
   \        |        /
    Derived information
            ↓
     Decision/proposal
            ↓
Validation + policy + permission
            ↓
       Business action
            ↓
    New authoritative state
```

The important distinction is that an AI output is not automatically a business fact.

```text
Model prediction != authoritative state
Agent proposal   != completed action
Retrieved text   != verified truth
Event            != command
Command          != outcome
```

## Five classes of information

### 1. Authoritative facts

Persisted facts owned by a defined system or domain.

### 2. Events

Events describe something that has happened, such as `OrderCreated`, `InventoryAdjusted`, or `WorkflowFailed`.

### 3. Commands or intents

Commands request that something should happen, such as `CreateShipment` or `RefreshCatalogue`.

### 4. Derived information

Aggregates, projections, search indexes, features, embeddings, reports, and cached views. Derived data may be useful without being authoritative.

### 5. AI interpretations

Classifications, summaries, predictions, extracted fields, recommendations, confidence estimates, and agent plans. These require provenance and validation appropriate to their consequences.

## Deterministic boundaries around probabilistic systems

```text
Authoritative facts
        ↓
Context construction
        ↓
Probabilistic reasoning
        ↓
Structured output
        ↓
Schema + business validation
        ↓
Policy / permission
        ↓
Action or human review
```

This prevents probabilistic reasoning from silently becoming authoritative data mutation.

## Event architecture is not an excuse for complexity

Do not introduce streaming platforms, event sourcing, or distributed data infrastructure merely because they appear in large-system diagrams. A database transaction plus a durable job queue may be enough.

Use more sophisticated infrastructure when requirements justify it through independent consumers, high volume, replay, integration fan-out, low-latency propagation, audit requirements, service boundaries, or data-platform needs.

## Data architecture for AI requires extra discipline

Traditional software often fails visibly when required data is missing. AI can produce a plausible answer anyway.

An AI consumer should know, where relevant:

```text
What is this data?
Who owns it?
When was it observed?
How fresh is it?
How was it derived?
Which tenant/user does it belong to?
What permissions apply?
Has it been corrected?
Can it be trusted for this decision?
```

## Freshness is part of correctness

A value can be structurally valid and still be operationally wrong because it is stale. For consequential decisions, revalidate critical facts immediately before execution.

```text
Reason using snapshot
        ↓
Propose action
        ↓
Re-read critical authoritative state
        ↓
Validate preconditions
        ↓
Execute
```

## Multi-tenant data isolation

Tenant identity must survive every data path:

```text
Request → Database → Event → Queue → Consumer → Cache/Index → AI Context → Audit
```

A missing tenant boundary in any one layer can become a data leak.

## Replay changes the design

If an event can be replayed, consumers must be designed with replay in mind. Ask whether the consumer is idempotent, whether replay repeats external side effects, which schema version is used, and whether replay is isolated from live execution.

## Data quality is operational

Monitor completeness, validity, uniqueness, consistency, freshness, referential integrity, unexpected nulls, event lag, distribution shifts, and reconciliation differences.

For AI systems, also monitor whether model context represents the intended authoritative state.

## Evidence and provenance

For consequential AI outputs, preserve enough provenance to reconstruct why the system reached a result. Depending on risk, this can include input identifiers, data versions, event IDs, retrieval sources, instruction version, model version, tool results, validation results, policy decisions, human approvals, and execution outcomes.

## Architecture principle

> Move facts through deterministic contracts; let AI interpret them inside controlled boundaries; make every consequential transition back into business state explicit, validated, authorised, and auditable.

## Mastery lenses

### Understand
Explain state, events, commands, CDC, streaming, replay, lineage, and data quality.

### Build
Implement durable data/event flows with schemas, idempotent consumers, validation, provenance, and observability.

### Architect
Choose data ownership, integration, consistency, streaming, replay, and governance patterns based on requirements and trade-offs.

### Lead
Establish standards for contracts, ownership, lineage, quality, privacy, AI provenance, and architectural decision-making.

## What comes next

Start with **01 — Data Ownership and Sources of Truth**.

Before designing streams, events, models, or agents, an architect must answer a more fundamental question:

> Which system is allowed to say what is true?

## Prerequisites and next steps

**Recommended prerequisites:** [03 — AI Application Engineering](../application-engineering/README.md), [12 — AI System Design](../ai-system-design/README.md)

**Useful next domains:** [17 — MLOps and LLMOps](../mlops-llmops/README.md), [22 — Enterprise AI](../enterprise-ai/README.md), [24 — Business Automation](../business-automation/README.md), [25 — Decision Intelligence](../decision-intelligence/README.md), [27 — AI-Native Commerce and Operations](../ai-native-commerce-operations/README.md)

See the [full prerequisite map](../roadmap/prerequisites-and-paths.md) and [domain status matrix](../roadmap/domain-status.md).
