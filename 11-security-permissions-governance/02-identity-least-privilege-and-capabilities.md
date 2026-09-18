# 02 — Identity, Least Privilege and Capabilities

## Purpose

Identity and permissions determine what an AI system may actually do.

Agent security becomes dangerous when a model inherits broad authority without explicit boundaries.

## Core Principle

> Give each capability only the authority required for the current task.

## Identity Layers

A system may have:

- human user identity;
- application identity;
- service identity;
- agent identity;
- tool identity;
- tenant identity.

Keep these concepts distinct.

## Authentication

Authentication establishes identity.

Examples:

- user login;
- API credential;
- OAuth token;
- workload identity;
- certificate.

Authentication does not decide whether a requested action is allowed.

## Authorization

Authorization decides whether the authenticated identity may perform an action on a resource.

Questions include:

- who;
- may do what;
- to which resource;
- under what conditions.

## Least Privilege

Prefer:

```text
read specific records
```

over:

```text
database administrator
```

Prefer:

```text
send draft for approval
```

over:

```text
send arbitrary email
```

## Capability-Based Thinking

A capability is a bounded authority to perform an operation.

Examples:

- read document;
- create draft;
- query report;
- submit approval request.

Exposing narrow capabilities helps prevent arbitrary use of backend credentials.

## Delegated Authority

An agent often acts on behalf of a user.

Delegation should preserve:

- delegating identity;
- scope;
- duration;
- resource;
- action.

Do not replace user-level authorization with one shared agent credential if the system can avoid it.

## Tenant Isolation

Every resource request should be bound to tenant context by trusted application logic.

Never rely on a model-provided tenant ID alone.

## Read vs Write

Separate read and write capabilities.

A research agent may need broad read access but no write access.

A write-capable worker may need a much smaller resource scope.

## Time-Bounded Privilege

Some operations can use short-lived credentials.

Benefits include:

- reduced exposure;
- easier revocation;
- clearer audit.

## Just-in-Time Access

High-risk authority can be granted only when needed.

Example:

```text
Agent proposes action
   |
Policy allows request
   |
Human approves
   |
Temporary capability issued
   |
Action executes
```

## Permission Inheritance

Avoid accidental inheritance where a child agent receives every capability of its parent.

Delegation should pass an explicit subset.

## Deny by Default

If a capability is not required, do not expose it.

This is stronger than exposing everything and relying on model instructions not to use it.

## Exercise

Design permissions for:

- research agent;
- execution agent;
- reviewer;
- administrator.

Define read, write, approval and tenant boundaries.

## Takeaway

> Agent authority should be deliberately delegated, narrowly scoped and independently enforceable.

Next: **03 — Prompt Injection and Untrusted Content**.
