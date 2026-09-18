# 01 — MCP Foundations

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **01 — MCP Foundations** within MCP and Tool Ecosystems;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

MCP provides a standard protocol boundary between AI applications and external capabilities.

The important architectural idea is not that every integration should become MCP. It is that AI hosts, clients and servers can exchange capabilities through a common protocol instead of each application inventing a bespoke integration contract.

## Core Principle

> MCP is an interoperability layer between AI applications and capabilities.

## Host, Client and Server

The architecture separates three roles.

### Host

The host is the AI application or runtime.

It owns concerns such as:

- user interaction;
- model access;
- orchestration;
- policy;
- approvals;
- application state.

### Client

An MCP client operates inside the host and communicates with an MCP server.

A host can maintain multiple clients for different servers.

### Server

An MCP server exposes focused capabilities through the protocol.

Servers may expose:

- tools;
- resources;
- prompts;
- supported extensions.

A server should remain focused on the capabilities it owns rather than become the entire agent application.

## Stateless Core

The 2026-07-28 protocol core is stateless.

This means protocol continuity is not inferred from a transport connection or old session identifier.

Each request is self-contained and carries protocol metadata required for interoperability.

This has architectural consequences:

- requests can be handled independently;
- HTTP deployments do not require sticky transport sessions merely for MCP;
- a connection is not the same thing as a conversation;
- application-level state should be represented explicitly.

## Per-Request Metadata

Current requests carry protocol metadata in `_meta`.

Important protocol-level metadata includes the protocol version and client capabilities.

Client and server identity metadata can also be carried for display, logging and debugging.

Self-reported identity metadata is not an authorization mechanism and should not be used as a trust decision by itself.

## JSON-RPC

MCP uses JSON-RPC 2.0 message structures.

The protocol defines requests, responses and notifications on top of JSON-RPC.

A production implementation should use an SDK or schema appropriate to the negotiated protocol version rather than reconstruct message formats from old examples.

## Versioning

MCP is versioned.

Clients and servers therefore need to account for:

- supported protocol versions;
- compatibility;
- deprecations;
- extension support;
- SDK version.

A protocol name alone is not sufficient compatibility information.

## Server Discovery

The current protocol provides `server/discover`.

It lets a client query supported protocol versions, server capabilities and server identity before making other calls.

Discovery is useful but not required for every request flow. A client can also make a request directly and handle an unsupported-version response.

## Capabilities

Clients and servers advertise supported capabilities.

Capability declarations are important because optional features should not be assumed.

The general pattern is:

```text
Client
  |
  | request + version + client capabilities
  v
Server
  |
  | result + server metadata / supported behaviour
  v
Client
```

## Multi Round-Trip Requests

The 2026-07-28 protocol introduced Multi Round-Trip Requests.

A server processing a request may determine that it needs additional client-side input.

Instead of relying on the older server-initiated request pattern, it can return an input-required result describing the information it needs.

The client obtains the required input and retries the original request with the corresponding responses.

This preserves a stateless request/response model.

## Result Types

Current results include a `resultType`.

Ordinary completed results use the complete result form.

Flows requiring additional input can use the input-required result form.

Extensions can introduce additional result forms where defined by the extension specification.

## Extensions

MCP supports optional extensions.

Extensions are not automatically part of the core protocol.

Examples in the 2026 ecosystem include:

- Tasks for long-running work;
- MCP Apps for interactive application surfaces;
- Skills over MCP.

A production architecture should explicitly track which extensions it depends on.

## Deprecation Awareness

The 2026-07-28 revision deprecated several older features, including Roots, Sampling and Logging.

Deprecated does not necessarily mean immediately removed.

It means new architectures should avoid adopting deprecated mechanisms without a compatibility reason and should follow the protocol lifecycle guidance.

## MCP and the Harness

MCP does not decide whether a tool should be exposed to a model.

The host or harness remains responsible for:

- policy;
- capability selection;
- permissions;
- approvals;
- context;
- validation;
- observability.

This distinction prevents the protocol layer from becoming an accidental authority layer.

## Exercise

Draw an MCP architecture with:

1. one host;
2. two MCP clients;
3. two focused servers;
4. a model;
5. a policy layer;
6. an approval boundary.

Mark which responsibilities belong to the host and which belong to the servers.

## Takeaway

> MCP standardises communication with capabilities, not the entire AI system.

Next: **02 — Tools, Resources and Prompts**.
