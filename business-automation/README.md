# Domain 24 — Business Automation

## Learning objectives

By the end of this domain, you should be able to:

- explain the core concepts and distinctions across workflow discovery, decomposition, deterministic automation, durable workflows, tool actions, exceptions, recovery and process intelligence.
- build or evaluate a representative implementation rather than relying on a demo;
- make architecture decisions that account for reliability, security, cost, scale and operations;
- define the evidence, evaluation and governance required before production adoption.

## Purpose

Business automation turns repeatable operational work into controlled systems that combine deterministic software, AI reasoning, tools and human judgment.

> The goal is not to automate every step. It is to remove unnecessary human effort while preserving human authority where ambiguity, consequence or exception requires it.

## Domain structure

01 Workflow Discovery and Automation Selection  
02 Process Decomposition and Automation Boundaries  
03 Deterministic Automation vs AI Reasoning  
04 Durable Workflows, State and Orchestration  
05 Tool-Enabled Automation and System Actions  
06 Exceptions, Approvals and Human-in-the-Loop Operations  
07 Reconciliation, Idempotency and Recovery  
08 Automation Evaluation and Process Intelligence  
09 Production Automation Architecture and Governance  
10 Business Automation Capstone

## Core architecture

```text
Business trigger
      ↓
Workflow state
      ↓
Deterministic rules
      ↓
AI reasoning where ambiguity exists
      ↓
Policy + permission gate
      ↓
Tool / system action
      ↓
Verification + reconciliation
      ↓
Exception / approval if required
      ↓
Business outcome
      ↓
Measurement + improvement
```

## Principles

1. Understand the process before automating it.
2. Automate outcomes, not historical inefficiency.
3. Keep exact rules deterministic.
4. Use AI where interpretation or uncertainty adds value.
5. Persist workflow state outside the model.
6. Make consequential actions explicit and authorized.
7. Design exception paths before happy-path scale.
8. Reconcile external state before retrying effects.
9. Measure business outcomes, not automation volume.
10. Preserve manual recovery and operational ownership.

## Takeaway

> Good automation does not remove humans indiscriminately; it moves human attention from repetitive execution toward exceptions, judgment and improvement.

Next: **01 — Workflow Discovery and Automation Selection**.

## Canonical curriculum navigation

- [Workflow Discovery and Automation Selection](./01-workflow-discovery-and-automation-selection.md)
- [Process Decomposition and Automation Boundaries](./02-process-decomposition-and-automation-boundaries.md)
- [Deterministic Automation vs AI Reasoning](./03-deterministic-automation-vs-ai-reasoning.md)
- [Durable Workflows, State and Orchestration](./04-durable-workflows-state-and-orchestration.md)
- [Tool-Enabled Automation and System Actions](./05-tool-enabled-automation-and-system-actions.md)
- [Exceptions, Approvals and Human-in-the-Loop Operations](./06-exceptions-approvals-and-human-in-the-loop-operations.md)
- [Reconciliation, Idempotency and Recovery](./07-reconciliation-idempotency-and-recovery.md)
- [Automation Evaluation and Process Intelligence](./08-automation-evaluation-and-process-intelligence.md)
- [Production Automation Architecture and Governance](./09-production-automation-architecture-and-governance.md)
- [Business Automation Capstone](./10-business-automation-capstone.md)

## Prerequisites and next steps

**Recommended prerequisites:** [07 — MCP and Tool Ecosystems](../07-mcp-tool-ecosystems/README.md), [09 — Orchestration and Multi-Agent Systems](../09-orchestration-multi-agent/README.md), [10 — Evaluation and Reliability](../10-evaluation-reliability/README.md), [11 — Security, Permissions and Governance](../11-security-permissions-governance/README.md), [12 — AI System Design](../ai-system-design/README.md), [13 — Data and Event Architecture](../data-event-architecture/README.md), [23 — AI Product Design](../ai-product-design/README.md)

**Useful next domains:** [25 — Decision Intelligence](../decision-intelligence/README.md), [27 — AI-Native Commerce and Operations](../ai-native-commerce-operations/README.md), [28 — Build an AI Operating System](../ai-operating-system/README.md)

See the [full prerequisite map](../roadmap/prerequisites-and-paths.md) and [domain status matrix](../roadmap/domain-status.md).
