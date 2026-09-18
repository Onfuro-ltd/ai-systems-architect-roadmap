# 02 — Identity, Access and Tenancy

## Purpose

Ensure every AI request and action is evaluated in the correct organizational identity and permission context.

## Identity chain

```text
Human / service identity
        ↓
Organization / tenant
        ↓
Role + attributes + delegated authority
        ↓
AI session / workflow
        ↓
Tool and data permissions
```

## Authentication vs authorization

Authentication establishes identity. Authorization determines what that identity may read, generate, approve or change.

The model does neither.

## Tenancy

Carry tenant identity through retrieval, memory, caches, queues, logs, vector indexes, tools, cost attribution and evaluation data.

Do not rely on prompts such as "only use this customer's data" for isolation.

## Delegation

An agent acts with delegated authority, not its own unlimited identity. Scope credentials to workload, resource, action and time where possible.

## RBAC and ABAC

Roles are useful for broad permissions; attributes and policy conditions can handle resource ownership, geography, sensitivity and transaction thresholds.

## Service identities

Background agents need explicit machine identities, owners and scopes. Avoid shared credentials.

## Break glass

Exceptional access should be rare, time-bound, strongly authenticated and audited.

## Exercise

Design authorization for a multitenant assistant that can read documents, prepare changes and execute only actions permitted to the current user.

## Takeaway

> The AI can reason about permission context, but deterministic identity systems must enforce it.

Next: **03 — Enterprise Data, Residency and Knowledge Boundaries**.
