# 03 — Delegation and Specialist Agents

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **03 — Delegation and Specialist Agents** within Orchestration and Multi-Agent Systems;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Delegation allows one agent or orchestrator to assign bounded work to another agent.

Specialisation is useful when a worker benefits from focused context, focused tools or focused responsibility.

## Core Principle

> Delegate bounded work, not vague responsibility.

## Orchestrator-Worker Pattern

```text
User Goal
   |
Orchestrator
   |
   +-- Worker A
   +-- Worker B
   +-- Worker C
   |
Synthesis
   |
Outcome
```

The orchestrator determines the decomposition and integrates the results.

## When Delegation Helps

Delegation can add value when:

- subtasks are genuinely distinct;
- parallel work is possible;
- workers need different tools;
- context would overwhelm one agent;
- independent analysis is useful;
- permission boundaries differ.

## Specialist Agent

A specialist agent has a narrow operating role.

Examples:

- research specialist;
- code-review specialist;
- data-analysis specialist;
- policy-review specialist.

Specialisation should be expressed through explicit:

- role;
- skills;
- tools;
- context;
- permissions;
- output contract.

## Delegation Contract

A delegation request should define:

- objective;
- scope;
- inputs;
- expected output;
- constraints;
- deadline or budget;
- evidence requirements.

Avoid:

> "Handle this for me."

Prefer:

> "Analyse these three documents for contradictions and return structured findings with evidence."

## Context Isolation

A worker should receive only the context it needs.

Benefits include:

- lower token use;
- reduced distraction;
- lower data exposure;
- clearer responsibility.

## Permission Isolation

Specialists may have different tool permissions.

Example:

```text
Research Worker -> read-only tools
Execution Worker -> bounded write tools
Reviewer -> no write tools
```

This can be safer than giving one general agent every capability.

## Hierarchical Delegation

A worker may itself delegate.

Hierarchy can scale complex tasks, but it makes:

- cost;
- tracing;
- permissions;
- termination;
- evaluation

harder.

Limit recursive delegation unless it clearly improves the task.

## Delegation Depth

Track delegation depth.

Useful controls include:

- maximum depth;
- maximum number of children;
- maximum total workers;
- cost budget.

Without controls, agent trees can grow unexpectedly.

## Worker Independence

Parallel workers should be independent enough to avoid constant synchronisation.

If every worker must coordinate on every step, the architecture may be decomposed incorrectly.

## Shared Mutable State

Shared writable state creates conflict.

Prefer:

- isolated worker outputs;
- append-only evidence;
- orchestrator-controlled merge;
- explicit locking where necessary.

## Synthesis

The orchestrator should not simply concatenate worker results.

Synthesis can include:

- deduplication;
- contradiction detection;
- evidence comparison;
- prioritisation;
- uncertainty.

## Failure

A worker can:

- succeed;
- partially succeed;
- fail;
- time out;
- return invalid output.

The orchestrator should know what to do in each case.

## Exercise

Design a three-worker research system.

Define each worker's:

1. scope;
2. tools;
3. context;
4. output;
5. permissions;
6. failure behaviour.

Then define the synthesis contract.

## Takeaway

> Specialisation works when boundaries are clearer than the coordination overhead they introduce.

Next: **04 — Routing, Parallelism and Coordination**.
