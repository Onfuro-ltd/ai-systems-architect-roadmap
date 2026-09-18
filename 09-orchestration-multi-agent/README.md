# Domain 09 — Orchestration and Multi-Agent Systems

## Learning objectives

By the end of this domain, you should be able to:

- explain the core concepts and distinctions across workflows, state machines, routing, delegation, multi-agent coordination, long-running execution, recovery and observability.
- build or evaluate a representative implementation rather than relying on a demo;
- make architecture decisions that account for reliability, security, cost, scale and operations;
- define the evidence, evaluation and governance required before production adoption.

## Purpose

This domain explains how AI systems coordinate work across deterministic workflows, model-driven loops, specialist agents and long-running processes.

The goal is not to maximise the number of agents.

The goal is to choose the simplest coordination architecture that produces the required reliability, flexibility and operating value.

## Core Principle

> Use deterministic workflows where the path is known, a single agent where reasoning must choose the path, and multiple agents only where decomposition creates measurable value.

A useful decision order is:

```text
Can software handle it deterministically?
        |
        +-- Yes -> deterministic workflow
        |
        v
Does one agent have enough context, tools and capability?
        |
        +-- Yes -> single agent
        |
        v
Does decomposition improve parallelism, specialisation,
context isolation, reliability or operational control?
        |
        +-- Yes -> multi-agent architecture
        |
        v
Do not add agents merely for architectural novelty.
```

## What This Domain Covers

1. Orchestration foundations
2. Workflows, state machines and agent loops
3. Delegation and specialist agents
4. Routing, parallelism and coordination
5. Event-driven and long-running orchestration
6. Validation, consensus and recovery
7. Multi-agent failure modes and anti-patterns
8. Production orchestration and observability
9. Capstone architecture

## Workflow vs Agent

A workflow follows a defined control path.

An agent can choose its own next step within the boundaries provided by the system.

```text
Workflow
Input -> Step A -> Step B -> Gate -> Step C -> Output
```

```text
Agent
Goal -> Observe -> Reason -> Act -> Observe -> ... -> Stop
```

Both can use models and tools.

The difference is who controls the path.

## Single-Agent vs Multi-Agent

A single agent is usually easier to:

- understand;
- evaluate;
- secure;
- operate;
- debug;
- control for cost.

Multi-agent systems introduce additional coordination surfaces:

- delegation;
- shared state;
- communication;
- concurrency;
- conflict;
- duplicate work;
- partial failure;
- synthesis.

Those costs should be justified by measurable benefit.

## Common Patterns

Production systems commonly use combinations of:

- sequential workflow;
- routing;
- parallel execution;
- orchestrator-worker;
- evaluator-optimizer;
- specialist delegation;
- event-driven coordination;
- human approval gates.

These are patterns, not mandatory framework abstractions.

## Domain Boundaries

- **Domain 06 — Skills and Agent Harnesses:** packages reusable capability and controls one agent's execution.
- **Domain 07 — MCP and Tool Ecosystems:** connects systems to external capabilities.
- **Domain 08 — Memory Systems:** persists useful information across interactions.
- **Domain 10 — Evaluation and Reliability:** measures behaviour and outcomes.
- **Domain 11 — Security, Permissions and Governance:** controls authority, trust and consequential actions.

Orchestration coordinates these components.

## Mastery Outcomes

### Understand

Explain the difference between workflows, agents, routers, orchestrators, workers, specialist agents and event-driven processes.

### Build

Implement deterministic, single-agent and multi-agent coordination patterns with explicit state and stopping conditions.

### Architect

Choose coordination patterns according to task topology, reliability, latency, cost and operational risk.

### Lead

Define organisational standards for orchestration, agent boundaries, concurrency, recovery, observability and human control.

## Architectural Rule

> Complexity must earn its place through measurable improvement.

Do not turn one understandable process into five interacting agents without evidence that the decomposition improves the system.

Next: **01 — Orchestration Foundations**.

## Canonical curriculum navigation

- [Orchestration Foundations](./01-orchestration-foundations.md)
- [Workflows, State Machines and Agent Loops](./02-workflows-state-machines-and-agent-loops.md)
- [Delegation and Specialist Agents](./03-delegation-and-specialist-agents.md)
- [Routing, Parallelism and Coordination](./04-routing-parallelism-and-coordination.md)
- [Event-Driven and Long-Running Orchestration](./05-event-driven-and-long-running-orchestration.md)
- [Validation, Consensus and Recovery](./06-validation-consensus-and-recovery.md)
- [Multi-Agent Failure Modes and Anti-Patterns](./07-multi-agent-failure-modes-and-anti-patterns.md)
- [Production Orchestration and Observability](./08-production-orchestration-and-observability.md)
- [Capstone: Design a Production Orchestration System](./09-capstone.md)
