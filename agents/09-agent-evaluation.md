# 09 — Agent Evaluation

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
