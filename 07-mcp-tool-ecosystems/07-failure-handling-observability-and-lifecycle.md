# 07 — Failure Handling, Observability and Lifecycle

## Purpose

Capability ecosystems fail in more ways than a single API call.

Production MCP integrations need explicit handling for protocol errors, transport failures, tool failures, authorization failures, version mismatches and business failures.

## Core Principle

> Make failures typed, observable and recoverable.

## Failure Layers

A useful classification is:

```text
Application / Business Failure
Protocol Failure
Capability Contract Failure
Authorization Failure
Transport Failure
Infrastructure Failure
```

Diagnosing the correct layer prevents meaningless retries.

## Transport Failure

Examples include:

- process termination;
- network interruption;
- timeout;
- broken response stream.

A transport retry is not always safe if the original operation may already have produced a side effect.

## Protocol Failure

Examples include:

- unsupported protocol version;
- invalid request;
- unknown method;
- malformed result;
- unsupported capability.

These usually require compatibility handling rather than blind retry.

## Authorization Failure

Examples include:

- missing token;
- expired token;
- wrong audience;
- insufficient scope;
- policy denial.

Refreshing a token may solve some failures.

It should not be used to bypass a legitimate authorization denial.

## Tool Failure

A tool can execute correctly at the protocol layer and still fail at the business layer.

Examples:

- record not found;
- validation rejected;
- upstream API unavailable;
- insufficient inventory;
- approval required.

Return errors in a form the host can reason about.

## Retry Policy

Retries should account for:

- idempotency;
- error class;
- retry count;
- backoff;
- side effects.

Do not let the model independently retry consequential actions without a bounded strategy.

## Stream Failure

Under the modern Streamable HTTP model, a broken request-scoped stream can require the client to issue a new request.

Clients should follow the current protocol semantics rather than assume old SSE resume behaviour.

For side-effecting operations, application idempotency remains important.

## Observability

Useful telemetry includes:

- trace or correlation ID;
- protocol version;
- client and server identity metadata;
- server;
- capability name;
- tool version;
- latency;
- result type;
- authorization outcome;
- retry count;
- error classification;
- payload size;
- cost attribution where relevant.

Do not log secrets indiscriminately.

## Capability Metrics

Useful aggregates can include:

- call volume;
- success rate;
- business rejection rate;
- p95 latency;
- error class;
- authorization denial rate;
- retry rate;
- model-selected tool accuracy;
- downstream outcome quality.

## Lifecycle

Capabilities evolve.

Track:

- owner;
- version;
- deployment;
- protocol support;
- schema version;
- deprecation state;
- consumers;
- evaluation status.

## Compatibility Windows

When clients and servers upgrade at different times, define compatibility expectations.

Possible strategies include:

- support multiple MCP protocol revisions;
- use a compatibility adapter;
- coordinate upgrade windows;
- reject unsupported versions explicitly.

Do not silently interpret incompatible messages.

## Deprecation

A deprecation plan should identify:

- replacement;
- affected clients;
- migration guidance;
- final support date;
- rollback plan.

Protocol deprecation and business-capability deprecation are separate concerns.

## SLOs

Critical capability servers may need service-level objectives for:

- availability;
- latency;
- error rate;
- recovery time.

An MCP server is still production software.

## Incident Response

During an incident, teams should be able to answer:

- Which capability failed?
- Which callers were affected?
- Which version was running?
- Were side effects produced?
- Was the failure retried?
- Were permissions involved?
- Can requests be replayed safely?

## Exercise

Design an incident dashboard for a remote write-capable MCP server.

Include metrics, logs and traces needed to distinguish transport, protocol, auth, tool and business failures.

## Takeaway

> An interoperable capability is only useful when operators can understand how it behaves under failure.

Next: **08 — Enterprise Capability Ecosystems**.
