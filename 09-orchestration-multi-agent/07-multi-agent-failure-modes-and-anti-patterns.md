# 07 — Multi-Agent Failure Modes and Anti-Patterns

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **07 — Multi-Agent Failure Modes and Anti-Patterns** within Orchestration and Multi-Agent Systems;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Multi-agent systems introduce failure modes that do not exist in a single model call or simple workflow.

Understanding these failures is more important than learning another framework.

## Core Principle

> Every additional agent adds a coordination boundary that can fail.

## Anti-Pattern: Agents for Everything

Turning every step into an agent increases:

- latency;
- cost;
- failure surfaces;
- tracing complexity.

Use software functions for deterministic work.

## Anti-Pattern: Role-Playing Architecture

Creating agents named:

- Manager;
- Researcher;
- Critic;
- Supervisor;
- Expert

does not automatically create useful decomposition.

Each agent should have a real architectural reason to exist.

## Context Duplication

Sending the same large context to every worker wastes tokens and can recreate the same reasoning errors.

Use focused context.

## Correlated Failure

Multiple workers using the same model and prompt family may make the same mistake.

Apparent consensus can be false confidence.

## Coordination Loops

Agents may repeatedly ask each other for clarification without making progress.

Controls include:

- bounded turns;
- explicit contracts;
- orchestrator ownership;
- escalation.

## Delegation Explosion

An agent that can create agents recursively may create unbounded work.

Control:

- delegation depth;
- worker count;
- cost;
- time.

## Duplicate Work

Workers may unknowingly perform the same task.

Use:

- task IDs;
- assignment records;
- shared task registry;
- partitioning.

## Conflicting Writes

Parallel agents modifying the same resource can overwrite each other.

Use:

- ownership;
- locks;
- transactions;
- merge protocols;
- isolated branches.

## Shared-State Contamination

One worker may place incorrect information into shared state and influence every other worker.

Prefer:

- provenance;
- append-only evidence;
- validation before promotion.

## Deadlock

Two workers may wait on each other.

Avoid circular dependencies.

Use timeouts and dependency graphs.

## Livelock

Agents can remain active but make no progress.

Detect:

- repeated actions;
- repeated messages;
- unchanged state;
- evaluator stagnation.

## Premature Completion

An orchestrator may synthesize before required work is finished.

Track required branches explicitly.

## Orphaned Workers

A parent can terminate while children continue consuming resources.

Propagate cancellation and lease work.

## Hidden Cost

Multi-agent systems can multiply model usage quickly.

Track cost per:

- root task;
- child task;
- agent;
- tool;
- retry.

## Evaluation Blindness

If you only score final output, you may miss:

- unsafe tool calls;
- duplicate work;
- unnecessary agents;
- invalid delegation;
- excessive retries.

Evaluate process as well as outcome.

## When Not to Use Multi-Agent

Prefer a simpler design when:

- one agent can handle the context;
- steps are predictable;
- tools are shared;
- decomposition is artificial;
- latency matters;
- coordination cost exceeds benefit.

## Exercise

Take a proposed five-agent architecture and remove every agent that does not need independent reasoning, tools, context or authority.

Compare the simplified design.

## Takeaway

> Multi-agent architecture is justified by task structure, not by the number of roles you can name.

Next: **08 — Production Orchestration and Observability**.
