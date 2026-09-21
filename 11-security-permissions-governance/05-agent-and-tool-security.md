# 05 — Agent and Tool Security

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **05 — Agent and Tool Security** within Security, Permissions and Governance;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Tools convert model reasoning into real-world effects.

This makes the tool boundary one of the most important security boundaries in an AI system.

## Core Principle

> A tool call is a proposed privileged operation, not trusted model output.

## Tool Threat Surface

Tools can:

- read sensitive data;
- modify records;
- send messages;
- execute code;
- spend money;
- change infrastructure.

Risk depends on tool authority.

## Narrow Tools

Prefer focused operations.

Example:

```text
create_draft_invoice(customer_id, items)
```

is easier to control than:

```text
execute_arbitrary_database_query(sql)
```

## Structured Inputs

Use explicit schemas.

Validate:

- type;
- range;
- resource;
- tenant;
- allowed values.

Do not pass raw model text directly into dangerous interpreters when avoidable.

## Server-Side Authorization

Never trust the model to enforce permissions.

The tool or service should verify authority independently.

## Side Effects

Mark and design side effects explicitly.

Examples:

- read-only;
- reversible write;
- irreversible write;
- external communication;
- financial action.

Use stronger controls as consequence increases.

## Idempotency

Side-effecting tools should support safe retry where possible.

Use:

- idempotency key;
- operation identifier;
- deduplication.

## Approval

Require approval for actions such as:

- external communication;
- high-value transaction;
- destructive delete;
- privilege change;
- production deployment.

The threshold depends on context.

## Tool Output Validation

Tool output is also untrusted input.

Validate:

- schema;
- source;
- status;
- error;
- suspicious instructions.

Do not let a tool response silently modify system policy.

## MCP Servers

Third-party MCP servers introduce tool supply-chain risk.

Assess:

- source;
- publisher;
- version;
- permissions;
- update process;
- data handling;
- outbound connections.

## Agent-to-Agent Security

When agents delegate, pass:

- minimal context;
- minimal capabilities;
- bounded task;
- trace identity.

Do not automatically copy parent privilege.

## Tool Chaining

A sequence of individually valid tools can produce a dangerous overall effect.

Policy should consider action chains.

Example:

```text
read private file
+
upload file
=
possible exfiltration
```

## Rate Limits

Limit:

- calls;
- concurrency;
- spend;
- affected resources.

Rate limits help contain loops and abuse.

## Exercise

Threat-model a toolset containing:

- search;
- read file;
- send email;
- delete file.

Assign control requirements to each.

## Takeaway

> The safest agent tool is a narrow capability with explicit authority, validation and observable side effects.

Next: **06 — Policy Engines, Approvals and Action Controls**.
