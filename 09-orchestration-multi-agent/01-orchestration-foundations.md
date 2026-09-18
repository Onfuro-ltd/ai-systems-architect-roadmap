# 01 — Orchestration Foundations

## Purpose

Orchestration coordinates steps, models, tools, agents, approvals and external systems toward an outcome.

It is the control structure around work.

## Core Principle

> Orchestration decides who does what, in what order, under what conditions and with what recovery behaviour.

## The Coordination Spectrum

AI systems can be organised along a spectrum:

```text
Deterministic Code
      |
LLM-Assisted Workflow
      |
Single-Agent Loop
      |
Agent + Specialist Delegation
      |
Multi-Agent System
```

Moving right increases flexibility but also increases coordination cost and uncertainty.

## Deterministic Workflow

Use deterministic orchestration when:

- steps are known;
- branching rules are explicit;
- inputs and outputs are structured;
- auditability matters;
- model autonomy adds little value.

Example:

```text
Receive
  |
Validate
  |
Classify
  |
Route
  |
Execute
  |
Verify
```

A model can still participate inside individual steps.

## Agent Loop

Use an agent when the next step cannot be fully predetermined.

```text
Goal
 |
Observe
 |
Reason
 |
Choose Action
 |
Act
 |
Observe
 |
Stop or Continue
```

The harness should enforce:

- limits;
- permissions;
- tool access;
- validation;
- stopping conditions.

## Multi-Agent System

Use multiple agents when the task benefits from true decomposition.

Possible reasons include:

- independent parallel exploration;
- specialised context;
- specialised tools;
- separate permissions;
- fault isolation;
- independent critique;
- organisational ownership boundaries.

Do not use multiple agents merely because several prompts exist.

## Orchestration State

Every non-trivial orchestration needs explicit state.

State may include:

- goal;
- current step;
- completed work;
- pending work;
- assigned worker;
- attempts;
- approvals;
- evidence;
- errors;
- final status.

State should not live only in natural-language conversation history.

## Control Plane and Work Plane

A useful distinction is:

```text
Control Plane
- scheduling
- routing
- policy
- retries
- approvals
- state transitions

Work Plane
- model reasoning
- tool execution
- specialist analysis
- external operations
```

Keeping these concerns distinct improves observability and recovery.

## Task Topology

Before choosing orchestration, understand the task structure.

Questions include:

- Is the task sequential?
- Can work run in parallel?
- Are branches predictable?
- Are subtasks independent?
- Is there shared mutable state?
- Is synthesis required?
- Are there irreversible actions?

The task topology should drive the architecture.

## Human Participation

Humans can appear as first-class orchestration nodes.

Examples:

- approve;
- review;
- resolve ambiguity;
- supply missing information;
- choose among alternatives.

Human involvement is not architectural failure.

## Stopping Conditions

Agentic execution needs explicit stopping rules.

Examples:

- objective satisfied;
- evaluation threshold reached;
- no more valid actions;
- retry budget exhausted;
- time budget exceeded;
- human intervention required.

## Cost of Coordination

Coordination adds:

- latency;
- model calls;
- tokens;
- network traffic;
- state management;
- failure modes;
- operational complexity.

Compare the gain against these costs.

## Exercise

Take a generic research task and design three alternatives:

1. deterministic workflow;
2. single agent;
3. orchestrator with parallel workers.

Explain the tradeoffs.

## Takeaway

> Orchestration architecture should follow the structure of the work, not the popularity of an agent framework.

Next: **02 — Workflows, State Machines and Agent Loops**.
