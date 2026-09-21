# 09 — Data Lineage, Provenance and Audit

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **09 — Data Lineage, Provenance and Audit** within Data and Event Architecture;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Reliable AI-native systems must explain where important data came from, how it changed, what used it, and what caused a consequential outcome.

> If a fact can influence an important decision, preserve enough provenance to trace that decision back to its evidence and transformations.

## Lineage, provenance and audit

**Lineage** explains how data moves and transforms. **Provenance** establishes origin and evidence for a particular value or result. **Audit** records relevant actions, decisions, actors, controls, and outcomes.

They overlap but are not interchangeable.

## End-to-end lineage

Operational source → event/CDC → transformation → warehouse/index → context builder → AI proposal → validation/policy → business action → verified outcome.

For consequential paths, authorized investigators should be able to traverse this chain.

Technical lineage identifies data movement. Semantic lineage also preserves meaning, units, policy, and transformation semantics.

## Provenance

Depending on consequence, preserve source IDs and versions, event IDs, retrieval time, transformation versions, instruction version, model/configuration identity, tool observations, validation results, policy decisions, approvals, execution IDs, and verified outcomes.

Capture purposefully rather than logging every sensitive payload forever.

## AI provenance

The objective is not to reconstruct hidden chain-of-thought. Preserve observable evidence and controls:

Evidence snapshot → context builder version → instruction/model configuration → tool observations → structured proposal → validation/policy → approval → execution outcome.

This is enough to support investigation and evaluation without treating private model reasoning as the audit record.

## Freshness and human provenance

Correctly sourced evidence may still be stale. Preserve when critical evidence was observed.

Human approval should bind to a specific object/version. Do not attribute a later changed state to someone who approved an earlier version.

## Audit integrity

High-consequence audit may require restricted write paths, append-oriented storage, independent retention, tamper-evidence, or other controls appropriate to threat and regulation.

A table named audit_log is not automatically immutable.

## Multi-tenancy and privacy

Tenant identity must survive lineage, transformations, AI context, actions, and audit. Cross-tenant lineage must require explicit authorization.

Lineage systems can expose an enterprise data map, so minimize payload copies and protect access. Identifiers, hashes, versions, classifications, and references may be preferable to full sensitive content.

## Retention and deletion

Provenance does not justify indefinite retention. Define policy by purpose and data class. Where permitted, deletion may remove content while retaining minimal non-sensitive evidence that an event occurred.

## Debugging and evaluation

Lineage turns vague failure claims into diagnosable questions: was the defect in source data, propagation, transformation, retrieval, model output, validation, or execution?

Versioned provenance also allows outcomes to be joined to the exact system configuration that produced them, enabling controlled evaluation and improvement.

## Observability vs audit

Observability operates the system; audit establishes durable evidence. Logs may be sampled and short-lived, while audit may require stronger completeness and retention. Design them separately even when infrastructure overlaps.

## Anti-patterns

Avoid logging everything without classification, losing tenant identity, storing model output without evidence, treating citations as complete provenance, mutable high-consequence audit, approvals without object versions, missing transformation versions, indefinite sensitive retention, or relying on hidden model reasoning as evidence.

## Architect checklist

Define which decisions need traceability, what sources/versions are preserved, how transformations are reproduced, how AI configuration is identified, how approvals bind to versions, how tenant/privacy controls survive lineage, and whether an outcome can be traced back to evidence.

## Exercise

Trace a generic AI-assisted operational action from authoritative source through event/CDC, projection, retrieval, AI proposal, validation, approval, external execution, and verified outcome. Define the minimum provenance at every boundary.

## Takeaway

> Lineage tells you how data moved, provenance tells you where a result came from, and audit tells you what happened. Together they create system-level accountability.

Next: **10 — Data Quality and Observability**.
