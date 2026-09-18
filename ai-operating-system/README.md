# Domain 28 — Build an AI Operating System

## Learning objectives

By the end of this domain, you should be able to:

- explain the core concepts and distinctions across a model-independent AI operating system integrating identity, orchestration, models, agents, skills, memory, tools, policy, evaluation and learning.
- build or evaluate a representative implementation rather than relying on a demo;
- make architecture decisions that account for reliability, security, cost, scale and operations;
- define the evidence, evaluation and governance required before production adoption.

## Purpose

This final domain integrates the roadmap into a model-independent AI operating platform.

An AI operating system is not a new kernel or a single autonomous agent. It is the control architecture through which people and software can safely use models, knowledge, memory, skills and tools to produce verified outcomes.

> Models provide probabilistic intelligence. The operating system owns identity, context, policy, orchestration, tools, evaluation, observability and learning.

## Master architecture

```text
Human / System Intent
          ↓
Identity + Tenant + Purpose
          ↓
Intent / Task Classification
          ↓
Policy + Risk + Permissions
          ↓
ORCHESTRATION
          ↓
MODEL ROUTING
          ↓
Agents / Durable Workflows
          ↓
Skills + Memory + Knowledge
          ↓
MCP / Typed Tools
          ↓
Authoritative Business Systems
          ↓
Verified Outcomes
          ↓
Evaluation + Feedback + Learning
```

Surrounding every layer:

```text
Security • Governance • Observability • Auditability
Cost Control • Data Governance • Human Control • Reliability
```

## Domain structure

01 AI Operating System Foundations and Boundaries  
02 Control Plane and Capability Architecture  
03 Identity, Context, Memory and Knowledge Plane  
04 Agents, Skills, Workflows and Orchestration  
05 Model Routing and Inference Plane  
06 Tools, MCP and Action Plane  
07 Policy, Security, Governance and Human Authority  
08 Evaluation, Observability, Economics and Learning  
09 Building and Evolving the AI Operating System  
10 Final AI Operating System Capstone

## Non-negotiable properties

The platform should be model-independent, multitenant where required, permission-aware, evidence-grounded, observable, auditable, cost-aware, resilient, evaluable and progressively autonomous.

## Build philosophy

Start with stable contracts and one valuable workflow. Add autonomy only after the system can observe, evaluate, recover and prove outcomes.

## Final objective

The organization should be able to replace a model, provider or agent framework without losing its durable intelligence: data, semantics, knowledge, memory, skills, workflows, tools, policies, evaluations and outcome history.

Next: **01 — AI Operating System Foundations and Boundaries**.

## Canonical curriculum navigation

- [AI Operating System Foundations and Boundaries](./01-ai-operating-system-foundations-and-boundaries.md)
- [Control Plane and Capability Architecture](./02-control-plane-and-capability-architecture.md)
- [Identity, Context, Memory and Knowledge Plane](./03-identity-context-memory-and-knowledge-plane.md)
- [Agents, Skills, Workflows and Orchestration](./04-agents-skills-workflows-and-orchestration.md)
- [Model Routing and Inference Plane](./05-model-routing-and-inference-plane.md)
- [Tools, MCP and Action Plane](./06-tools-mcp-and-action-plane.md)
- [Policy, Security, Governance and Human Authority](./07-policy-security-governance-and-human-authority.md)
- [Evaluation, Observability, Economics and Learning](./08-evaluation-observability-economics-and-learning.md)
- [Building and Evolving the AI Operating System](./09-building-and-evolving-the-ai-operating-system.md)
- [Final AI Operating System Capstone](./10-final-ai-operating-system-capstone.md)
