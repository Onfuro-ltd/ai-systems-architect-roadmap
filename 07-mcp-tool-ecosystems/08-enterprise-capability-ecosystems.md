# 08 — Enterprise Capability Ecosystems

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **08 — Enterprise Capability Ecosystems** within MCP and Tool Ecosystems;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

An enterprise MCP strategy should produce a governed capability ecosystem, not an uncontrolled collection of servers.

## Core Principle

> Standardise capability exposure without centralising every implementation.

## Capability Catalog

Maintain a catalog containing:

- server;
- owner;
- capabilities;
- protocol versions;
- deployment type;
- authorization model;
- data classification;
- lifecycle state;
- support contact;
- evaluation status.

A catalog improves discoverability for engineers without exposing every capability to every model.

## Server Boundaries

Prefer servers aligned to coherent responsibility boundaries.

Possible boundaries include:

- business domain;
- data domain;
- platform capability;
- external SaaS integration.

Avoid one global server with unrestricted access to every enterprise system.

## Gateway Pattern

Remote MCP servers may sit behind an enterprise gateway.

A gateway can provide:

- TLS termination;
- authentication integration;
- routing;
- policy enforcement;
- rate limiting;
- telemetry;
- network controls.

The gateway should not become a substitute for server-side authorization.

## Capability Broker

Some organisations may introduce a broker or registry that helps hosts discover approved MCP servers.

The broker can expose metadata without granting automatic access.

Discovery and authority remain separate.

## Environment Separation

Separate:

- development;
- staging;
- production

capabilities and credentials.

A model testing against staging should not accidentally receive production tools.

## Tenant Isolation

Multi-tenant systems need explicit tenant boundaries.

Tenant context should be validated by application identity and policy, not trusted because a model supplied a tenant identifier.

## Data Classification

Capabilities should identify the sensitivity of data they expose or mutate.

This can influence:

- which hosts may connect;
- logging rules;
- retention;
- human approval;
- model eligibility;
- geographic processing constraints.

## Ownership

Every production server should have:

- technical owner;
- security owner or escalation route;
- operational runbook;
- lifecycle status;
- compatibility policy.

Unowned capability servers create hidden enterprise risk.

## Capability Minimisation

Expose the smallest useful capability surface.

Prefer:

```text
purpose-built operation
```

over:

```text
generic unrestricted backend access
```

when the business requirement allows it.

## Internal vs Third-Party Servers

Third-party MCP servers introduce external trust dependencies.

Assess:

- vendor identity;
- authorization;
- requested scopes;
- data handling;
- retention;
- update process;
- incident history;
- server provenance.

Do not install a server merely because its tool descriptions look useful.

## Supply Chain

MCP servers are software dependencies.

Apply software supply-chain controls such as:

- source review;
- signed packages where available;
- pinned versions;
- dependency scanning;
- controlled deployment;
- update review.

## Evaluation

Evaluate the ecosystem at several levels:

- individual capability quality;
- correct tool selection;
- authorization behaviour;
- failure handling;
- host compatibility;
- end-to-end outcome.

A protocol-conformant server can still be a poor enterprise capability.

## Cost Governance

Track costs attributable to capability use:

- external API charges;
- compute;
- model tokens triggered by large outputs;
- long-running tasks;
- repeated failures.

Capability design can affect model cost by changing tool descriptions and payload size.

## Enterprise Architecture

A mature pattern may look like:

```text
AI Hosts
   |
Policy / Identity / Gateway
   |
Approved MCP Capability Layer
   |
Domain Services
   |
Systems of Record
```

The MCP layer should make capabilities easier to consume without bypassing systems of record or domain ownership.

## Exercise

Design governance for an enterprise catalog of twenty MCP servers.

Define:

1. onboarding;
2. ownership;
3. security review;
4. authorization;
5. observability;
6. versioning;
7. deprecation;
8. incident response.

## Takeaway

> Enterprise MCP is a capability-management problem as much as a protocol problem.

Next: **09 — Capstone**.
