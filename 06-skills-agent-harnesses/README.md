# Domain 06 — Skills and Agent Harnesses

## Learning objectives

By the end of this domain, you should be able to:

- explain the core concepts and distinctions across reusable skills, contracts, context engineering, harnesses, rules, hooks, lifecycle controls, quality gates and portability.
- build or evaluate a representative implementation rather than relying on a demo;
- make architecture decisions that account for reliability, security, cost, scale and operations;
- define the evidence, evaluation and governance required before production adoption.

## Purpose

This domain explains how reusable expertise is packaged into skills and how agent harnesses turn probabilistic model capability into controlled, testable and observable execution.

The goal is not to create collections of prompts. The goal is to build durable capability that can be versioned, evaluated, governed and reused across models and systems.

## Core Principle

> Models provide intelligence. Skills package reusable expertise. Harnesses provide operational control.

A production capability can be viewed as:

```text
User / System Intent
        |
        v
Agent Harness
        |
        +-- Model
        +-- Context
        +-- Skills
        +-- Tools
        +-- State
        +-- Rules & Policies
        +-- Lifecycle Controls
        +-- Evaluation
        +-- Observability
```

## What This Domain Covers

1. Skills and capabilities
2. Skill design and contracts
3. Context engineering for skills
4. Agent harness architecture
5. Rules, hooks and lifecycle controls
6. Skill composition and discovery
7. Testing, evaluation and quality gates
8. Portability, versioning and governance
9. Capstone architecture

## Skills Are Not Prompts

A prompt is an instruction supplied to a model.

A production skill may combine:

- instructions;
- domain knowledge;
- input and output contracts;
- tool requirements;
- context requirements;
- workflow logic;
- validation rules;
- permissions;
- evaluation criteria;
- failure and escalation behaviour.

The distinction matters because reusable organisational capability should not depend on one prompt, model or vendor.

## Domain Boundaries

This domain focuses on packaging and operating reusable AI capability.

Related concerns are covered separately:

- **Domain 07 — MCP and Tool Ecosystems:** connecting AI systems to external capabilities;
- **Domain 08 — Memory Systems:** retaining information across interactions and events;
- **Domain 09 — Orchestration and Multi-Agent Systems:** coordinating workflows and agents;
- **Domain 10 — Evaluation and Reliability:** system-wide measurement and reliability engineering;
- **Domain 11 — Security, Permissions and Governance:** authority, trust boundaries and governance.

These layers interact, but they should not be collapsed into one abstraction.

## Mastery Outcomes

### Understand

Explain the difference between prompts, skills, tools, agents, harnesses, workflows, context, memory and knowledge.

### Build

Create a reusable skill with explicit inputs, outputs, validation, tool dependencies and failure behaviour.

### Architect

Design a harness that controls model execution, context, tools, state, policies, lifecycle events, evaluation and observability.

### Lead

Define standards for reusable skills, portability, ownership, versioning, testing, governance and retirement across an organisation.

## Architectural Rule

> Put probabilistic reasoning inside deterministic boundaries wherever the system requires control, safety or repeatability.

A capable model does not remove the need for software architecture. As AI capability increases, the surrounding control system becomes more important.

## Canonical curriculum navigation

- [Skills and Capabilities](./01-skills-and-capabilities.md)
- [Skill Design and Contracts](./02-skill-design-and-contracts.md)
- [Context Engineering for Skills](./03-context-engineering-for-skills.md)
- [Agent Harness Architecture](./04-agent-harness-architecture.md)
- [Rules, Hooks and Lifecycle Controls](./05-rules-hooks-and-lifecycle-controls.md)
- [Skill Composition and Discovery](./06-skill-composition-and-discovery.md)
- [Testing, Evaluation and Quality Gates](./07-testing-evaluation-and-quality-gates.md)
- [Portability, Versioning and Governance](./08-portability-versioning-and-governance.md)
- [Capstone: Design a Production Skill and Harness](./09-capstone.md)

## Prerequisites and next steps

**Recommended prerequisites:** [03 — AI Application Engineering](../application-engineering/README.md), [05 — Agents](../agents/README.md)

**Useful next domains:** [08 — Memory Systems](../08-memory-systems/README.md), [09 — Orchestration and Multi-Agent Systems](../09-orchestration-multi-agent/README.md), [10 — Evaluation and Reliability](../10-evaluation-reliability/README.md)

See the [full prerequisite map](../roadmap/prerequisites-and-paths.md) and [domain status matrix](../roadmap/domain-status.md).
