# 09 — Capstone: Design an Enterprise MCP Capability

## Objective

Design an MCP capability from protocol boundary to enterprise operation.

The capstone should demonstrate when MCP is appropriate, how the capability is contracted, how authority is controlled and how the integration is operated.

## Scenario

Choose a generic enterprise capability such as:

- document repository access;
- project-management actions;
- analytics queries;
- customer-support operations;
- inventory lookup;
- approval workflow integration.

Avoid an unrestricted generic API proxy.

## Part 1 — Integration Decision

Explain why MCP is appropriate.

Compare it against:

- direct API;
- function calling without MCP;
- event-driven integration;
- webhook.

Identify what interoperability benefit justifies MCP.

## Part 2 — Server Boundary

Define:

- server responsibility;
- owner;
- deployment;
- protocol version;
- transport;
- consumers;
- data classification.

Explain why the boundary is neither too broad nor too narrow.

## Part 3 — Primitives

Design at least:

- two tools;
- one resource;
- one prompt where appropriate.

For each, explain why that primitive is the right abstraction.

## Part 4 — Contracts

Define:

- tool names;
- descriptions;
- input schemas;
- structured outputs;
- errors;
- side effects;
- idempotency considerations.

Include contract tests.

## Part 5 — Discovery

Design how clients learn:

- supported protocol versions;
- server capabilities;
- available tools;
- available resources;
- available prompts.

Define caching and capability-change behaviour.

## Part 6 — Authorization

For a remote server, define:

- protected resource;
- authorization server relationship;
- client registration;
- token audience;
- scopes;
- tool-level enforcement;
- approval requirements.

For a local server, define the alternative credential boundary.

## Part 7 — Host Controls

Design the host or harness controls around MCP:

- capability filtering;
- model exposure;
- policy;
- approvals;
- validation;
- context handling;
- audit.

Demonstrate that MCP connectivity does not become automatic authority.

## Part 8 — Failure Handling

Define behaviour for:

- unsupported protocol version;
- network timeout;
- expired token;
- insufficient scope;
- invalid tool arguments;
- upstream dependency failure;
- ambiguous business failure;
- retry after possible side effect.

## Part 9 — Observability

Specify:

- traces;
- logs;
- metrics;
- correlation IDs;
- server identity;
- protocol version;
- capability version;
- authorization outcome;
- latency;
- business outcome.

## Part 10 — Lifecycle

Define:

- ownership;
- release process;
- compatibility policy;
- schema evolution;
- deprecation;
- rollback;
- incident runbook.

## Part 11 — Current MCP Features

Explain whether the design needs:

- Multi Round-Trip Requests;
- subscriptions;
- Tasks extension;
- other extensions.

Do not include an extension merely because it exists.

## Architectural Review Questions

Before completion, answer:

1. Is MCP creating real interoperability value?
2. Are tools focused and schema-defined?
3. Are resources separated from executable actions?
4. Is authorization enforced at invocation?
5. Can the host restrict what the model sees?
6. Are side effects explicit?
7. Are retries safe?
8. Can failures be diagnosed by layer?
9. Is the capability owned and versioned?
10. Can the server evolve without forcing every consumer to change simultaneously?

## Completion Criteria

Another engineer should be able to determine:

- what the server exposes;
- which protocol version it supports;
- who may use it;
- what each capability does;
- how errors behave;
- how it is monitored;
- how it changes safely.

## Takeaway

> A good MCP server is not just protocol-compliant. It is a well-owned, well-contracted, well-authorized production capability.

Next: **Domain 08 — Memory Systems**.
