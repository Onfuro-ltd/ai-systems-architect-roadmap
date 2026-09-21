# Domain 26 — Domain-Specific AI Systems

## Learning objectives

By the end of this domain, you should be able to:

- explain the core concepts and distinctions across domain adaptation, data/knowledge boundaries, specialist workflows, domain evaluation, governance and durable domain intelligence.
- build or evaluate a representative implementation rather than relying on a demo;
- make architecture decisions that account for reliability, security, cost, scale and operations;
- define the evidence, evaluation and governance required before production adoption.

## Purpose

Domain-specific AI turns an organization's terminology, knowledge, data, policies, workflows, tools and evaluation criteria into durable capability without unnecessarily coupling that capability to one model vendor.

> The durable asset is not the model call. It is the encoded domain system surrounding the model.

## Domain structure

01 Domain Intelligence and Capability Mapping  
02 Domain Ontologies, Semantics and Canonical Models  
03 Proprietary Knowledge and Evidence Architecture  
04 Policies, Rules and Decision Boundaries  
05 Domain Skills, Workflows and Tool Contracts  
06 Specialist Models, Tuning and Routing  
07 Domain Evaluation and Gold Standards  
08 Feedback, Outcomes and Knowledge Evolution  
09 Production Domain AI Architecture and Governance  
10 Domain-Specific AI Systems Capstone

## Core architecture

```text
Domain intent
    ↓
Canonical domain model
    ↓
Authorized knowledge + current state
    ↓
Policies / deterministic rules
    ↓
Domain skills / workflows
    ↓
Model router / specialist models
    ↓
Typed domain tools
    ↓
Validation + permissions
    ↓
Verified domain outcome
    ↓
Evaluation + curated learning
```

## Principles

1. Capture domain intelligence outside model weights wherever practical.
2. Make terminology and entities explicit.
3. Keep current facts in authoritative systems.
4. Keep deterministic policies deterministic.
5. Encode reusable procedures as skills/workflows.
6. Tune models only for stable learned behaviour.
7. Evaluate against domain-specific failure criteria.
8. Preserve provenance and temporal correctness.
9. Learn from verified outcomes, not raw interaction volume.
10. Make models replaceable beneath stable domain contracts.

## Takeaway

> A domain AI system becomes strategically durable when replacing the foundation model does not erase the organization's accumulated intelligence.

Next: **01 — Domain Intelligence and Capability Mapping**.

## Canonical curriculum navigation

- [Domain Intelligence and Capability Mapping](./01-domain-intelligence-and-capability-mapping.md)
- [Domain Ontologies, Semantics and Canonical Models](./02-domain-ontologies-semantics-and-canonical-models.md)
- [Proprietary Knowledge and Evidence Architecture](./03-proprietary-knowledge-and-evidence-architecture.md)
- [Policies, Rules and Decision Boundaries](./04-policies-rules-and-decision-boundaries.md)
- [Domain Skills, Workflows and Tool Contracts](./05-domain-skills-workflows-and-tool-contracts.md)
- [Specialist Models, Tuning and Routing](./06-specialist-models-tuning-and-routing.md)
- [Domain Evaluation and Gold Standards](./07-domain-evaluation-and-gold-standards.md)
- [Feedback, Outcomes and Knowledge Evolution](./08-feedback-outcomes-and-knowledge-evolution.md)
- [Production Domain AI Architecture and Governance](./09-production-domain-ai-architecture-and-governance.md)
- [Domain-Specific AI Systems Capstone](./10-domain-specific-ai-systems-capstone.md)

## Prerequisites and next steps

**Recommended prerequisites:** [04 — Knowledge Systems and RAG](../knowledge-systems-rag/README.md), [10 — Evaluation and Reliability](../10-evaluation-reliability/README.md), [11 — Security, Permissions and Governance](../11-security-permissions-governance/README.md), [12 — AI System Design](../ai-system-design/README.md), [13 — Data and Event Architecture](../data-event-architecture/README.md), [15 — Fine-Tuning and Specialist Models](../fine-tuning-specialist-models/README.md), [25 — Decision Intelligence](../decision-intelligence/README.md)

**Useful next domains:** [27 — AI-Native Commerce and Operations](../ai-native-commerce-operations/README.md), [28 — Build an AI Operating System](../ai-operating-system/README.md)

See the [full prerequisite map](../roadmap/prerequisites-and-paths.md) and [domain status matrix](../roadmap/domain-status.md).
