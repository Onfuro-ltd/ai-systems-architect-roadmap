# 06 — MCP vs APIs, Function Calling and Events

## Purpose

MCP is one integration option among several.

Good architecture chooses the interface based on the workload instead of adopting MCP simply because the workload involves AI.

## Core Principle

> Use MCP where interoperability with AI hosts creates value. Use simpler or more specialised interfaces where they fit better.

## Direct APIs

A direct API is often the best option when:

- one application owns both sides;
- the contract is stable;
- low overhead matters;
- the integration is deterministic;
- no cross-host discovery is required.

Direct APIs remain a foundational enterprise integration mechanism.

## Model Function Calling

Function calling is typically a model-provider or model-runtime mechanism for expressing structured tool requests.

It can be used inside a harness without MCP.

MCP can expose capabilities that a host then represents to a model through its own tool-calling mechanism.

The two layers can therefore coexist.

## MCP

MCP is valuable when:

- multiple AI hosts may consume the same capabilities;
- standard discovery matters;
- the capability ecosystem is modular;
- provider independence is desirable;
- tools, resources or prompts need a common protocol boundary.

MCP should not be introduced solely to add another abstraction layer.

## Events and Queues

Events are useful when work is:

- asynchronous;
- durable;
- fan-out;
- integration-heavy;
- independent of an immediate model request.

Examples include:

- order-created events;
- audit events;
- workflow transitions;
- background processing.

MCP request/response calls are not a replacement for durable event architecture.

## Webhooks

Webhooks are useful for notifying another service that something happened.

A webhook can trigger an AI workflow, but the webhook itself does not need to become MCP.

## Tasks Extension

The MCP Tasks extension addresses long-running MCP operations through durable task handles and polling semantics.

It is useful when long-running work belongs inside an MCP capability interaction.

It does not automatically replace a general job queue, workflow engine or event bus.

## Decision Matrix

| Need | Likely starting point |
| --- | --- |
| AI host interoperability | MCP |
| Tight internal service integration | Direct API |
| Model asks for structured capability | Function/tool calling |
| Durable asynchronous business event | Event / queue |
| External change notification | Webhook |
| Long-running MCP operation | Tasks extension |

This is a starting heuristic, not a universal rule.

## Layering

A common architecture may use several patterns together:

```text
Model
  |
Function Calling
  |
Harness
  |
MCP Client
  |
MCP Server
  |
Internal API
  |
Business Service
  |
Event Bus
```

Each layer has a purpose.

Avoid duplicating the same responsibilities across all layers.

## Anti-Pattern: MCP Everywhere

Converting every service endpoint into an MCP tool can create:

- excessive tool lists;
- unclear authority;
- poor discoverability;
- duplicated contracts;
- model confusion;
- unnecessary operational complexity.

Expose capabilities at the level useful to AI consumers.

## Anti-Pattern: Generic API Proxy Tool

A tool such as `call_any_api(method, url, body)` removes many of the benefits of an explicit capability contract.

It creates a broad authority surface and weak semantics.

Prefer focused capabilities unless unrestricted access is truly the intended design.

## Anti-Pattern: Tool as Workflow Engine

A giant tool that accepts a natural-language goal and performs an opaque multi-system workflow hides orchestration and audit boundaries.

If the work is a business workflow, model it as a workflow.

## Exercise

For five integrations in a generic enterprise system, choose between:

- MCP;
- direct API;
- function calling;
- event;
- webhook.

Explain the architectural reason for each choice.

## Takeaway

> MCP complements APIs, tool calling and events. It does not eliminate them.

Next: **07 — Failure Handling, Observability and Lifecycle**.
