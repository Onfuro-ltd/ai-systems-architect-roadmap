# Domain 05 — Agents

This section explains how to design, build, evaluate and operate AI agents as reliable software systems.

The goal is not to follow AI hype around fully autonomous systems. The goal is to understand the engineering principles behind useful agents.

## Learning objectives

By the end of this domain, you should be able to:

- explain the core concepts and distinctions across agent loops, planning, execution, observation, recovery, tool selection, autonomy boundaries and long-horizon work.
- build or evaluate a representative implementation rather than relying on a demo;
- make architecture decisions that account for reliability, security, cost, scale and operations;
- define the evidence, evaluation and governance required before production adoption.

## Core Definition

An agent is a system that combines:

- A goal
- Reasoning or planning capability
- Tools and actions
- State management
- Memory
- Constraints and permissions
- Evaluation and feedback

```
Goal
 ↓
Reasoning
 ↓
Planning
 ↓
Tool Selection
 ↓
Execution
 ↓
Observation
 ↓
Evaluation
 ↓
Improvement
```

## Learning Path

1. What is an agent?
2. Agent architectures
3. Planning and reasoning
4. Tool use and action execution
5. Agent memory
6. Orchestration
7. Multi-agent systems
8. Agent security
9. Agent evaluation
10. Production agent patterns
11. Agent capstone

## Philosophy

Agents are not magical autonomous employees. They are controlled software systems that use AI capabilities inside defined boundaries.

A good agent is not the one that can do everything. It is the one that can reliably complete the right tasks with appropriate controls.

## Canonical curriculum navigation

- [What Is an Agent?](./01-what-is-an-agent.md)
- [Agent Architectures](./02-agent-architectures.md)
- [Planning and Reasoning](./03-planning-and-reasoning.md)
- [Tool Use and Action](./04-tool-use-and-action.md)
- [Agent Memory](./05-agent-memory.md)
- [Agent Orchestration](./06-agent-orchestration.md)
- [Multi-Agent Systems](./07-multi-agent-systems.md)
- [Agent Security](./08-agent-security.md)
- [Agent Evaluation](./09-agent-evaluation.md)
- [Agent Production Patterns](./10-agent-production-patterns.md)
- [Agent Capstone — AI Business Operations Agent System](./11-agent-capstone.md)

## Prerequisites and next steps

**Recommended prerequisites:** [03 — AI Application Engineering](../application-engineering/README.md), [04 — Knowledge Systems and RAG](../knowledge-systems-rag/README.md)

**Useful next domains:** [06 — Skills and Agent Harnesses](../06-skills-agent-harnesses/README.md), [07 — MCP and Tool Ecosystems](../07-mcp-tool-ecosystems/README.md), [09 — Orchestration and Multi-Agent Systems](../09-orchestration-multi-agent/README.md), [10 — Evaluation and Reliability](../10-evaluation-reliability/README.md), [11 — Security, Permissions and Governance](../11-security-permissions-governance/README.md)

See the [full prerequisite map](../roadmap/prerequisites-and-paths.md) and [domain status matrix](../roadmap/domain-status.md).
