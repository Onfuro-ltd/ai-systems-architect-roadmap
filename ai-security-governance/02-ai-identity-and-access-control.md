# AI Identity & Access Control

## Core Principle

AI systems should not receive unlimited authority. An AI agent must have an identity, permissions, boundaries, and accountability.

## AI Identity Model

Enterprise AI introduces new identities:

- human users;
- AI agents;
- service accounts;
- tools;
- automated workflows.

Each identity should be uniquely identifiable and auditable.

## Least Privilege

AI systems should only access the minimum capabilities required.

Weak architecture:

```
AI Agent
  |
  +-- Full system access
```

Secure architecture:

```
AI Agent
  |
Permission Layer
  |
Approved Capability
  |
Business System
```

## Capability-Based Access

Instead of giving an agent broad permissions, expose controlled capabilities:

- read inventory;
- analyse orders;
- create draft recommendations;
- request approval;
- execute approved actions.

## Human Approval Workflows

High-impact actions should include validation:

```
AI Recommendation
        ↓
Policy Check
        ↓
Human Approval (if required)
        ↓
Execution
        ↓
Audit Log
```

## Why This Matters

For enterprise AI platforms such as SEMLIS, agents may interact with marketplaces, finance systems, customer data, and operational tools. Security must be built into the architecture rather than added afterwards.
