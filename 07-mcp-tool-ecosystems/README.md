# Domain 07 — MCP and Tool Ecosystems

## Purpose

This domain explains how AI systems connect to external capabilities through the Model Context Protocol (MCP), direct APIs, function calling, events and related integration patterns.

The goal is not to treat MCP as a universal replacement for APIs or orchestration. The goal is to understand what MCP standardises, where it fits, how to use it safely, and when another integration pattern is the better choice.

## Protocol Snapshot

This domain is aligned to the **MCP 2026-07-28 specification**.

That revision materially changed the protocol:

- the protocol core is stateless;
- the old `initialize` / `notifications/initialized` handshake was removed;
- the `Mcp-Session-Id` transport session model was removed;
- each request carries protocol version and client capabilities in `_meta`;
- `server/discover` provides optional server capability discovery;
- Multi Round-Trip Requests provide a request/response mechanism for additional client input;
- Tasks moved to an official extension;
- Roots, Sampling and Logging are deprecated;
- the standard transports are stdio and Streamable HTTP;
- authorization for HTTP-based deployments is aligned with OAuth 2.1 and related standards.

Protocol details evolve. When implementing MCP, verify the specification version supported by the client, server and SDK rather than assuming examples from an older revision remain current.

## Core Principle

> MCP standardises capability exchange. It does not replace application architecture, authorization policy, workflow orchestration or domain logic.

A useful placement is:

```text
User / System Intent
        |
        v
Agent Harness / Application
        |
        +-- Skills
        +-- Context
        +-- Policy
        +-- Orchestration
        |
        v
Capability Interface Layer
        |
        +-- MCP
        +-- Direct APIs
        +-- Function / Tool Calling
        +-- Events / Queues
        |
        v
External Systems
```

## What This Domain Covers

1. MCP foundations
2. Tools, resources and prompts
3. Clients, servers and transports
4. Contracts, schemas and discovery
5. Authentication, authorization and trust
6. MCP vs APIs, function calling and events
7. Failure handling, observability and lifecycle
8. Enterprise capability ecosystems
9. Capstone architecture

## What MCP Is

MCP is an open protocol for connecting AI applications with external context and capabilities.

At the server boundary, its central primitives are:

- **tools** — executable capabilities;
- **resources** — contextual data;
- **prompts** — reusable interaction templates.

MCP also defines protocol mechanics for discovery, requests, results, capabilities, notifications, authorization and optional extensions.

## What MCP Is Not

MCP is not, by itself:

- an agent;
- an orchestration engine;
- a memory system;
- a workflow engine;
- a complete authorization policy;
- a business-rules engine;
- an API gateway;
- an evaluation framework;
- a guarantee that exposed tools are safe.

These concerns may surround MCP, but they should remain architecturally explicit.

## Domain Boundaries

- **Domain 06 — Skills and Agent Harnesses:** packages reusable capability and controls model-driven execution.
- **Domain 08 — Memory Systems:** retains information across interactions and events.
- **Domain 09 — Orchestration and Multi-Agent Systems:** coordinates work across workflows and agents.
- **Domain 10 — Evaluation and Reliability:** measures behaviour and outcomes.
- **Domain 11 — Security, Permissions and Governance:** defines authority, trust boundaries and governance.

This domain focuses on capability interfaces and tool ecosystems.

## Mastery Outcomes

### Understand

Explain MCP architecture, primitives, transports, discovery, schemas, authorization and protocol-version concerns.

### Build

Implement or integrate an MCP capability with explicit schemas, validation, error handling and observability.

### Architect

Choose between MCP, direct APIs, tool calling and event-driven integration based on the characteristics of the workload.

### Lead

Define enterprise standards for capability exposure, ownership, permissions, lifecycle, compatibility, observability and retirement.

## Architecture Rule

> Standardise interfaces where interoperability creates value, but keep business authority and safety controls outside the protocol boundary.

## Official References

- MCP Specification 2026-07-28: https://modelcontextprotocol.io/specification/2026-07-28
- MCP specification repository: https://github.com/modelcontextprotocol/modelcontextprotocol
- MCP 2026-07-28 release overview: https://blog.modelcontextprotocol.io/posts/2026-07-28/

Next: **01 — MCP Foundations**.
