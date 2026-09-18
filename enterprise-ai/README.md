# Domain 22 — Enterprise AI

## Learning objectives

By the end of this domain, you should be able to:

- explain the core concepts and distinctions across enterprise architecture, identity, tenancy, data residency, gateways, governance, procurement, adoption, platform teams and operations.
- build or evaluate a representative implementation rather than relying on a demo;
- make architecture decisions that account for reliability, security, cost, scale and operations;
- define the evidence, evaluation and governance required before production adoption.

## Purpose

Enterprise AI is the discipline of operating AI across real organizations: many users, teams, tenants, systems, jurisdictions, data classes, vendors and risk levels.

> Enterprise AI is not a chatbot purchased by a large company. It is an organizational capability with identity, governance, integration, evidence and accountable operating ownership.

## Domain structure

01 Enterprise AI Architecture and Operating Model  
02 Identity, Access and Tenancy  
03 Enterprise Data, Residency and Knowledge Boundaries  
04 Integration Architecture and AI Gateways  
05 Governance, Risk, Compliance and Audit  
06 Procurement, Vendors and Model Independence  
07 Human Oversight, Change Management and Adoption  
08 Enterprise AI Platform and Team Topology  
09 Reliability, Observability and Enterprise Operations  
10 Enterprise AI Capstone

## Core architecture

```text
Employees / customers / systems
            ↓
Identity + tenant + authorization
            ↓
Enterprise AI control plane
 policy / routing / governance / audit
            ↓
Knowledge + models + agents + tools
            ↓
Enterprise integration layer
            ↓
Systems of record / action
            ↓
Verified outcomes
            ↓
Evaluation + operations + governance
```

## Principles

1. Identity and authorization travel with every AI action.
2. Tenant and data boundaries are deterministic.
3. AI receives only the minimum context and tools required.
4. Systems of record remain authoritative.
5. Governance is risk-based and executable, not paperwork alone.
6. Human approval must occur at meaningful decision points.
7. Provider/model choice remains replaceable where practical.
8. Enterprise integrations use explicit contracts and ownership.
9. Production AI needs SLOs, incident response and audit.
10. Adoption is an organizational systems problem, not merely a model-quality problem.

## Takeaway

> Enterprise AI succeeds when probabilistic intelligence is integrated into deterministic organizational controls without losing ownership, accountability or human authority.

Next: **01 — Enterprise AI Architecture and Operating Model**.

## Canonical curriculum navigation

- [Enterprise AI Architecture and Operating Model](./01-enterprise-ai-architecture-and-operating-model.md)
- [Identity, Access and Tenancy](./02-identity-access-and-tenancy.md)
- [Enterprise Data, Residency and Knowledge Boundaries](./03-enterprise-data-residency-and-knowledge-boundaries.md)
- [Integration Architecture and AI Gateways](./04-integration-architecture-and-ai-gateways.md)
- [Governance, Risk, Compliance and Audit](./05-governance-risk-compliance-and-audit.md)
- [Procurement, Vendors and Model Independence](./06-procurement-vendors-and-model-independence.md)
- [Human Oversight, Change Management and Adoption](./07-human-oversight-change-management-and-adoption.md)
- [Enterprise AI Platform and Team Topology](./08-enterprise-ai-platform-and-team-topology.md)
- [Reliability, Observability and Enterprise Operations](./09-reliability-observability-and-enterprise-operations.md)
- [Enterprise AI Capstone](./10-enterprise-ai-capstone.md)
