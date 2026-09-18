# 09 — Capstone: Secure an Agentic AI System

## Objective

Design the security, permission and governance architecture for a production agent that can read sensitive data and perform external actions.

## Scenario

Choose a generic agent such as:

- support operations agent;
- research-and-email agent;
- document processing agent;
- project operations agent;
- infrastructure assistant.

The agent must have at least one consequential tool.

## Part 1 — Threat Model

Identify:

- assets;
- actors;
- entry points;
- trust boundaries;
- abuse cases;
- impact.

Include indirect prompt injection.

## Part 2 — Identity

Define:

- user identity;
- application identity;
- agent identity;
- service identity;
- tenant identity.

Explain how delegation works.

## Part 3 — Least Privilege

For every tool, define:

- allowed action;
- resource scope;
- read/write;
- credential;
- duration;
- rate limit.

## Part 4 — Untrusted Content

Define how the system treats:

- web pages;
- documents;
- email;
- tool output;
- MCP resources;
- memory.

Prevent untrusted content from becoming privileged instruction.

## Part 5 — Data Security

Map:

- sensitive data;
- context exposure;
- storage;
- logs;
- memory;
- backups;
- third parties.

## Part 6 — Tool Security

For each consequential tool define:

- schema;
- server-side authorization;
- idempotency;
- side effect;
- validation;
- approval.

## Part 7 — Policy and Approval

Design policy outcomes:

- allow;
- deny;
- escalate.

Create an approval record with meaningful action details.

## Part 8 — Runtime Security

Define:

- secret handling;
- sandbox;
- filesystem;
- network;
- package controls;
- runtime limits.

## Part 9 — Audit

Specify audit fields for:

- action;
- identity;
- policy;
- approval;
- tool;
- result;
- trace.

## Part 10 — Incident Response

Create response procedures for:

- prompt injection;
- credential exposure;
- unauthorised write;
- malicious tool;
- cross-tenant data access.

Include kill-switch behaviour.

## Part 11 — Security Evaluation

Build adversarial tests for:

- direct injection;
- indirect injection;
- tool misuse;
- excessive privilege;
- memory poisoning;
- secret extraction;
- unsafe code execution.

## Architectural Review Questions

Before completion, answer:

1. Can the model see any secret it does not need?
2. Can it access any tool it does not need?
3. Can untrusted content change policy?
4. Is tenant isolation enforced outside the model?
5. Are consequential actions independently authorised?
6. Are retries safe?
7. Can the runtime exfiltrate data?
8. Can operators reconstruct every important action?
9. Can operators disable the capability quickly?
10. Do security failures become regression tests?

## Completion Criteria

Another engineer should be able to determine:

- what the agent can access;
- what it cannot access;
- who grants authority;
- where secrets live;
- how untrusted content is contained;
- how tools enforce permissions;
- how actions are approved;
- how incidents are detected;
- how the system is stopped;
- how evidence is preserved.

## Takeaway

> Secure agentic AI is not achieved by trusting the model more. It is achieved by limiting, validating and governing the authority around it.

Next: **Domain 12 — AI System Design**.
