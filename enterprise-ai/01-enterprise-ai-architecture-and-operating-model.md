# 01 — Enterprise AI Architecture and Operating Model

## Purpose

Define how AI capabilities fit into enterprise architecture and organizational ownership.

## Layers

```text
Experience / workflow layer
        ↓
AI application / agent layer
        ↓
Shared AI platform
        ↓
Integration + data platform
        ↓
Systems of record
```

Security, identity, governance, observability and cost management cross all layers.

## Capability vs product

A shared model gateway, evaluation service or knowledge platform is a capability. A support assistant or document workflow is a product. Separate ownership so shared infrastructure does not become an unowned internal project.

## Federated model

A practical enterprise often combines a central platform/governance team with domain teams that own workflows and outcomes.

Centralize controls that benefit from consistency; keep domain decisions near domain expertise.

## Portfolio

Classify AI use cases by value, consequence, data sensitivity, autonomy and maturity. Apply proportionate engineering and approval.

## Architecture review

Require explicit data sources, model/runtime, tools, permissions, evaluation, human controls, SLOs, owner, cost model and retirement plan.

## Shadow AI

If approved paths are too difficult, teams may use unmanaged tools. Provide usable governed alternatives rather than relying only on prohibition.

## Exercise

Design the operating model for an organization with five business units that share an AI platform but own different workflows and regulated data.

## Takeaway

> Enterprise AI needs both a technical architecture and an operating model that makes ownership explicit.

Next: **02 — Identity, Access and Tenancy**.
