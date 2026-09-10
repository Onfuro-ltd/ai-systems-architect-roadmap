# Agent Architectures

## Purpose

Agents are not a single pattern. Different problems require different levels of autonomy and control.

The correct question is not:

> How do we make everything an agent?

The correct question is:

> What level of reasoning and autonomy does this problem require?

## Core Agent Patterns

### 1. Workflow Agents

A controlled sequence of steps:

```
Input
 ↓
Step 1
 ↓
Step 2
 ↓
Validation
 ↓
Output
```

Best for predictable business processes.

### 2. ReAct Agents

Reasoning and action loop:

```
Goal
 ↓
Reason
 ↓
Choose Tool
 ↓
Observe Result
 ↓
Continue
```

Useful when the path is not known in advance.

### 3. Planning Agents

The agent creates a plan before execution:

```
Goal
 ↓
Plan
 ↓
Execute Steps
 ↓
Review
```

Useful for complex multi-step tasks.

### 4. Supervisor Architectures

One agent coordinates specialised agents:

```
Supervisor
    |
    +-- Research Agent
    +-- Data Agent
    +-- Action Agent
```

Useful when responsibilities need separation.

## When NOT To Use Agents

Agents add complexity.

Use normal software when:

- the workflow is deterministic;
- rules are clear;
- failure cost is high;
- no reasoning is required.

## Enterprise Principle

The best agent architecture is the minimum autonomy required to solve the problem safely.

## Connection To Business Systems

For enterprise systems such as commerce intelligence:

```
Business Goal
 ↓
Knowledge Retrieval
 ↓
Reasoning
 ↓
Tools
 ↓
Validation
 ↓
Human Approval
 ↓
Action
```

Agents should operate inside controlled systems, not replace them.
