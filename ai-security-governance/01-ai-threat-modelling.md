# AI Threat Modelling

## Purpose

AI systems introduce new attack surfaces beyond traditional software security. A secure AI architect must understand how models, data, agents, tools, and users can be manipulated.

## Core Principle

> Security starts by understanding what can fail, who can exploit it, and what controls reduce the risk.

## AI Threat Surface

A production AI system includes:

- User inputs
- Models
- Prompts and instructions
- Retrieval systems
- Knowledge sources
- Tools and APIs
- Agent memory
- Business workflows
- External content

Each layer can become an attack path.

## Traditional Security vs AI Security

Traditional applications focus on:

- authentication;
- authorisation;
- code vulnerabilities;
- infrastructure protection.

AI systems additionally require:

- prompt injection protection;
- model abuse prevention;
- data leakage controls;
- output validation;
- agent action governance.

## Threat Modelling Process

```text
Identify Assets

↓

Identify Threats

↓

Assess Impact

↓

Design Controls

↓

Monitor Continuously
```

## Important AI Threat Categories

### Prompt Injection

Malicious instructions attempt to override system behaviour.

Example:

```text
External Document

↓

Hidden Instruction

↓

AI Agent

↓

Unsafe Action
```

### Data Leakage

Risks include exposing:

- private documents;
- customer information;
- credentials;
- internal knowledge.

### Tool Abuse

Agents with tools can create real-world impact.

Secure pattern:

```text
AI Recommendation

↓

Permission Check

↓

Business Rules

↓

Approved Action

↓

Audit Record
```

## Why This Matters

For enterprise AI platforms, the goal is not to prevent AI from acting. The goal is to enable useful actions with appropriate controls.

## SEMLIS Example

A commerce AI agent may access:

- marketplace APIs;
- inventory data;
- customer information;
- financial calculations.

Therefore every action requires:

- identity;
- permissions;
- validation;
- monitoring;
- auditability.
