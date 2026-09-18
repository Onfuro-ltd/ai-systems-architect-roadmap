# 03 — Clients, Servers and Transports

## Purpose

MCP separates protocol semantics from the transport used to carry messages.

Understanding this boundary prevents infrastructure assumptions from leaking into application logic.

## Core Principle

> Transport moves MCP messages. It does not define their business meaning.

## Client-Server Relationship

A host can maintain multiple MCP clients.

Each client connects to a server providing focused capabilities.

```text
Host
 |
 +-- MCP Client A ---> Server A
 |
 +-- MCP Client B ---> Server B
 |
 +-- MCP Client C ---> Server C
```

This separation supports capability isolation and independent server ownership.

## Standard Transports

The 2026-07-28 specification defines two standard transport bindings:

- stdio;
- Streamable HTTP.

Custom transports are possible, but interoperability costs should be considered before introducing them.

## stdio

With stdio:

- the client launches the server as a subprocess;
- messages flow through standard input and output;
- standard error can be used for logs.

This is useful for local capability servers.

The process connection itself should not be treated as conversation identity.

## Streamable HTTP

Streamable HTTP uses HTTP requests against an MCP endpoint.

Responses may be ordinary JSON responses or request-scoped streams where the protocol allows it.

The current stateless core means MCP protocol state does not depend on a sticky HTTP session.

## Legacy HTTP + SSE

Older MCP material may describe a legacy HTTP+SSE transport model.

That older transport should not be treated as the current default architecture.

When supporting older clients or servers, isolate compatibility behaviour rather than teaching it as the modern baseline.

## Statelessness and Infrastructure

A stateless protocol core improves infrastructure options.

Requests can be handled by different server instances without requiring protocol session affinity.

Application state may still exist.

The important distinction is:

```text
Protocol statefulness != application statefulness
```

A long-running job, business workflow or server-side handle may still require durable application state.

## Request Routing

HTTP infrastructure can route requests using ordinary web infrastructure.

Production systems may use:

- load balancers;
- gateways;
- service meshes;
- reverse proxies.

Routing infrastructure must preserve protocol requirements and authorization information.

## Cancellation and Termination

Transports need to represent cancellation and termination according to the protocol binding.

Application code should distinguish:

- user cancellation;
- transport failure;
- server error;
- timeout;
- business rejection.

They are not the same failure.

## Multi Round-Trip Behaviour

Current MCP can request additional client input through Multi Round-Trip Requests.

The server returns an input-required result.

The client fulfils the requested input and retries the original operation.

This design avoids requiring a stateful server-to-client RPC channel for normal protocol semantics.

## Subscriptions and Notifications

Where supported by the current protocol or extensions, subscriptions can deliver change notifications.

Notification streams should not become hidden workflow state.

Consumers need explicit handling for:

- reconnects;
- duplicate or missed business events;
- ordering expectations;
- cache invalidation.

If durable event processing is required, a dedicated event architecture may be more appropriate.

## Connection Is Not Identity

Never infer authorization from a transport connection alone.

Authorization should be based on validated credentials and policy.

Similarly, server self-identification metadata is useful for logging and display but is not a cryptographic identity guarantee.

## Local vs Remote Servers

Local servers and remote servers create different trust boundaries.

### Local

Consider:

- subprocess permissions;
- environment credentials;
- filesystem access;
- local code trust.

### Remote

Consider:

- TLS;
- OAuth;
- network policy;
- resource indicators;
- audience validation;
- gateway controls.

Domain 11 expands the broader security model.

## Exercise

Design two deployments for the same read-only capability:

1. local stdio server;
2. remote Streamable HTTP server.

Compare identity, credentials, network exposure, observability and failure handling.

## Takeaway

> Choose transport according to deployment needs, but keep protocol semantics and application authority explicit.

Next: **04 — Tool Contracts, Schemas and Discovery**.
