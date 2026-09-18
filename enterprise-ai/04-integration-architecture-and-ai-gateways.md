# 04 — Integration Architecture and AI Gateways

## Purpose

Connect AI to enterprise systems through controlled, reusable interfaces.

## Integration layers

Use APIs, events, MCP/tool adapters, workflow engines, queues and legacy/interface automation according to system capability.

## AI gateway

A shared gateway can provide provider abstraction, authentication, routing, rate limits, policy, telemetry, cost attribution and approved model access.

Do not turn the gateway into a monolith containing every business rule.

## Tool gateway

Expose enterprise actions as typed capabilities with explicit schemas, permissions, risk classification and audit.

## Read vs write

Separate read/query capabilities from state-changing actions. Writes require stronger validation, idempotency and authorization.

## Contracts

Version API/tool schemas and define ownership, timeouts, error semantics and compatibility.

## Events

For long-running business processes, durable workflows and events are often more reliable than keeping a model request open.

## Legacy systems

Use interface agents only when supported APIs/integration paths are absent or inadequate, and apply the controls from Domain 19.

## Exercise

Design an enterprise integration layer where multiple AI products share CRM, ERP and document capabilities without each embedding separate credentials and vendor logic.

## Takeaway

> Enterprise AI should consume governed capabilities, not accumulate uncontrolled direct connections to every system.

Next: **05 — Governance, Risk, Compliance and Audit**.
