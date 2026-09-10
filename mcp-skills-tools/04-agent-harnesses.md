# 04 — Agent Harnesses

## Introduction

A common misunderstanding in AI systems is that the model itself is the agent. The model is only the reasoning engine. The agent harness is the software architecture that turns model capability into a reliable operational system.

## Core Principle

> The model provides intelligence. The harness provides control.

## What an Agent Harness Provides

A production harness manages:

- execution loops;
- tool access;
- memory;
- state management;
- permissions;
- error handling;
- observability;
- evaluation.

## Architecture

```
User Goal
    |
    v
Agent Harness
    |
 +-- Model
 +-- Memory
 +-- Tools
 +-- State
 +-- Policies
 +-- Monitoring
```

## Model vs Harness

A model answers:

> What should happen next?

The harness controls:

> What is allowed to happen next?

This separation is critical for enterprise systems.

## Why This Matters

Without a harness, AI systems become:

- difficult to debug;
- unsafe;
- impossible to audit;
- unreliable at scale.

## SEMLIS Relevance

A future SEMLIS AI worker would not be only a language model. It would include:

- reasoning model;
- marketplace tools;
- business rules;
- memory;
- approval workflows;
- audit trails;
- monitoring.

The harness becomes the operational layer around AI capability.

## Key Lesson

> Building agents is less about choosing a powerful model and more about designing the system around the model.
