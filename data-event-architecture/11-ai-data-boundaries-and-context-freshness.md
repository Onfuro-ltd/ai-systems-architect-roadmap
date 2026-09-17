# 11 — AI Data Boundaries and Context Freshness

## Purpose

AI systems reason over representations of reality. Those representations can be stale, incomplete, derived, unauthorized, or probabilistically generated.

> AI context is a temporary evidence snapshot, not an authoritative transaction boundary.

## Separate the categories

Keep authoritative facts, derived representations, retrieved evidence, AI interpretations, and accepted business state distinct.

A model does not gain authority merely by transforming information.

## Context is a snapshot

Authoritative systems → retrieval/projection → context at time T → model reasoning.

Reality may change during inference. A proposal valid at T does not automatically remain executable later.

## Freshness by consequence

A historical summary may tolerate hours of lag. A consequential workflow, permission, stock, or financial action may require an authoritative read immediately before execution.

Define freshness by fact and use case.

## Read-before-write validation

For consequential actions:

AI reasons from snapshot → structured proposal → re-read critical authoritative state → validate versions/preconditions → policy/permission → approval if required → idempotent execution.

If a critical version changed, reject, re-evaluate, or rebuild context.

## Context provenance

Preserve source identity/version, retrieval time, transformations, and authorization context. The model is not the provenance database.

## Authorization before retrieval

Identity → authorization → permitted retrieval → context → model.

Do not retrieve broadly and rely on a prompt telling the model not to reveal unauthorized data.

Tenant isolation must be deterministic across retrieval, caches, vector stores, tools, events, and context construction.

## Derived stores

Search indexes, vector stores, caches, warehouses, and AI memory are useful copies, not automatically authoritative truth. They can lag, omit, transform, or conflict.

For high-consequence execution, verify critical facts with their authoritative owner.

## Memory

AI memory can contain preferences, summaries, and historical conclusions. Treat it according to provenance and freshness. It must not silently override current authoritative state.

## Retrieved content and prompt injection

Retrieved text is data, not trusted instruction.

System policy and authorized instructions must remain separate from untrusted retrieved content. Tool permissions and execution policy stay outside the control of documents being processed.

## Tool observations

A tool response is an observation at a point in time, not necessarily a verified business outcome.

Timeout or ambiguity must produce an explicit uncertain/reconciliation state rather than a model-invented success or failure.

## Generated summaries

AI-generated summaries can compress context but introduce another probabilistic transformation. Preserve source references and verification status. Prefer deterministic validation for critical fields.

## Context compaction

Long-running agents may summarize earlier state. Compaction must preserve critical invariants, unresolved obligations, permissions, identifiers, and provenance.

Do not keep authoritative workflow state only inside conversation memory.

## Freshness invalidation

Use versions, events/CDC, dependency tracking, re-indexing, invalidation, and TTLs according to the requirement. TTL alone is insufficient where correctness must update immediately.

## Concurrency

Two agents can reason correctly from the same snapshot and propose conflicting actions.

Proposal A + Proposal B → deterministic version/precondition check → only valid transitions commit.

Agent coordination never replaces database/workflow concurrency control.

## Data minimization

More context is not always better. Retrieve the minimum authorized evidence needed. This improves privacy, relevance, cost, latency, and resistance to injection/noise.

## Context quality gate

Before inference validate tenant, authorization, source/version, freshness, schema, required facts, provenance, duplication, relevance, and token budget.

Fail safely or reduce capability when critical evidence is untrustworthy.

## Model independence

Build provider-neutral canonical context where practical:

Authorized sources → canonical context object → provider adapter → model.

This improves portability and comparative evaluation.

## Evaluation

Test stale data, missing facts, conflicting sources, unauthorized documents, prompt injection, wrong tenant, delayed indexes, malformed tool results, compaction, version races, and model/provider changes.

Capture observable metadata rather than hidden chain-of-thought.

## Anti-patterns

Avoid treating vector search as truth, prompt-based tenant isolation, letting retrieved documents define permissions, acting on stale snapshots without revalidation, allowing memory to override current state, converting timeout into assumed failure, trusting generated summaries without provenance, or storing business state only in agent conversation.

## Architect checklist

Identify authoritative facts, freshness requirements, source versions, pre-retrieval authorization, tenant controls, stale derived stores, pre-action revalidation, ambiguous tool outcomes, provider-neutral context, and end-to-end evaluation.

## Exercise

Design context construction for a generic AI operations assistant that can read operational data and propose consequential actions. Define authoritative and derived sources, memory, permissions, tenant boundary, freshness classes, version checks, injection boundary, revalidation, idempotent action, provenance, and evaluation cases.

## Takeaway

> Let AI reason over well-governed evidence, but keep authoritative truth, authorization, concurrency, and consequential state transitions inside deterministic system boundaries.

Next: **12 — Data and Event Architecture Capstone**.
