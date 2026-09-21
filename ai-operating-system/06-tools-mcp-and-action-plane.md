# 06 — Tools, MCP and Action Plane

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **06 — Tools, MCP and Action Plane** within Build an AI Operating System;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Expose real-world capabilities to AI through typed, permissioned and verifiable interfaces.

## Action plane

Tools may be internal APIs, MCP servers, databases, workflow services, SaaS connectors, event publishers or controlled interface agents.

## Tool registry

Track schema, owner, version, read/write class, permissions, risk, idempotency, timeout, rate limits and audit requirements.

## Execution path

```text
Tool proposal
     ↓
Identity + delegated authority
     ↓
Fresh authoritative state
     ↓
Policy + input validation
     ↓
Human approval if required
     ↓
Execution
     ↓
Re-fetch / verify
     ↓
Confirmed / failed / UNKNOWN
```

## MCP

Use MCP as a standardized tool/context interface where appropriate, but keep business authorization and policy outside the protocol boundary.

## Credentials

Broker short-lived/scoped credentials outside model context.

## Consequence

Separate read, draft, reversible write and irreversible/high-consequence capabilities.

## Unknown outcomes

Never blindly retry a consequential action after ambiguous network failure. Reconcile authoritative state first.

## Exercise

Design a tool/MCP gateway where the same capability can be used by several agents while permissions differ by user and tenant.

## Takeaway

> Standardized tools make capabilities portable; deterministic authorization makes them safe.

Next: **07 — Policy, Security, Governance and Human Authority**.
