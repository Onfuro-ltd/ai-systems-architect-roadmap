# 05 — AI SaaS Architecture

## Core Principle

An AI SaaS product is not simply a web application with an AI button.

A production AI SaaS platform requires:

- application architecture;
- AI orchestration;
- data architecture;
- security;
- scalability;
- observability;
- commercial foundations.

## Reference Architecture

```text
Users
  |
Application Layer
  |
AI Orchestration Layer
  |
Models + Tools + Knowledge Systems
  |
Business Data Systems
```

## Multi-Tenant AI Architecture

Enterprise AI SaaS platforms must separate:

- customer data;
- permissions;
- configurations;
- AI behaviour;
- usage limits.

Example:

```text
Tenant A
  |
AI Workspace

Tenant B
  |
AI Workspace
```

## AI Application Layers

A mature AI SaaS system contains:

1. User experience layer
2. Application logic layer
3. AI orchestration layer
4. Knowledge and retrieval layer
5. Model layer
6. Monitoring and evaluation layer

## Model Orchestration

The product should decide:

- which model to use;
- when tools are required;
- when human approval is required;
- when to escalate.

## Why This Matters for SEMLIS

SEMLIS already follows many SaaS principles:

- multi-tenancy;
- marketplace integrations;
- business workflows;
- permissions;
- operational data.

The AI layer should become an additional intelligence layer on top of the platform, not a replacement for the existing system.

```text
Business Data
      |
      v
SEMLIS Intelligence Layer
      |
      v
Recommendations + Controlled Actions
```
