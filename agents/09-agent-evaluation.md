# 09 — Agent Evaluation

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **09 — Agent Evaluation** within Agents;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

An agent is not production ready because it completes a demo. It is production ready when its performance can be measured, improved, and trusted.

## Core Principle

> Agents must be evaluated as systems, not only as model outputs.

A complete evaluation considers:

- goal completion;
- planning quality;
- tool selection;
- execution reliability;
- safety;
- cost;
- business outcomes.

## Evaluation Layers

```text
Goal
 ↓
Plan Quality
 ↓
Tool Decisions
 ↓
Execution Trace
 ↓
Final Result
 ↓
Business Impact
```

## Important Metrics

### Task Success

Did the agent achieve the intended objective?

### Tool Accuracy

Did it select the correct tools and provide valid inputs?

### Trajectory Quality

Was the sequence of actions efficient and appropriate?

### Reliability

Can the agent repeat successful behaviour consistently?

### Cost Efficiency

Did the outcome justify the resources used?

## Evaluation Methods

### Golden Tasks

Maintain realistic tasks with expected outcomes.

### Regression Testing

Test changes to:

- prompts;
- models;
- tools;
- memory;
- workflows.

### Human Evaluation

Useful for complex tasks where automated scoring is insufficient.

## Failure Analysis

Capture:

- wrong plans;
- failed tool calls;
- missing context;
- unsafe actions;
- unnecessary steps.

Failures become future improvements.

## Continuous Improvement Loop

```text
Production Feedback
        ↓
Evaluation Dataset
        ↓
System Improvement
        ↓
More Reliable Agent
```

## Enterprise Principle

An agent without evaluation is an unreliable automation.

An evaluated agent becomes an engineered capability.

## Architect exercise

Design or inspect a representative system that uses **09 — Agent Evaluation**. Produce an architecture sketch, identify at least three failure modes, state one security or governance control where relevant, define one measurable success criterion, and compare the design with a simpler baseline. Record what evidence would justify keeping the added complexity.
