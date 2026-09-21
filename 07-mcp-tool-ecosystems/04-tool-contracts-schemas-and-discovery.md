# 04 — Tool Contracts, Schemas and Discovery

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **04 — Tool Contracts, Schemas and Discovery** within MCP and Tool Ecosystems;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Interoperability depends on contracts.

MCP provides standard discovery and schema mechanisms, but the quality of a capability still depends on how precisely the server describes and validates it.

## Core Principle

> A protocol can standardise the envelope. Engineers must still design the contract.

## JSON Schema

MCP uses JSON Schema for validation in protocol structures.

For the 2026-07-28 specification, JSON Schema 2020-12 is the default dialect when a schema does not explicitly declare another supported dialect.

Implementations should verify the schema rules of the protocol revision and SDK they use.

## Tool Contract

A well-designed tool defines:

- name;
- title or human-readable identity where useful;
- description;
- input schema;
- output schema where appropriate;
- side-effect semantics;
- errors;
- authorization expectations.

## Naming

Names should be:

- stable;
- unambiguous;
- machine-friendly;
- meaningful within the server's capability namespace.

Renaming a widely consumed tool can be a breaking integration change.

## Descriptions

Descriptions influence both humans and models.

A description should explain:

- what the capability does;
- when it should be used;
- important constraints;
- meaningful side effects.

Do not rely on descriptions as the only safety mechanism.

## Input Schemas

Prefer explicit structure.

For consequential operations, avoid replacing structured fields with a single free-form instruction string when the operation can be represented deterministically.

Explicit schemas improve validation and testing.

## Output Schemas

Structured outputs can make downstream automation safer.

They can help distinguish:

- successful result;
- partial result;
- business rejection;
- validation failure.

The protocol's transport success should not be confused with business success.

## Discovery

Current MCP provides capability-list operations and `server/discover`.

These solve different problems.

### `server/discover`

Provides supported protocol versions and server capabilities. The response may also carry self-reported server identity in result `_meta['io.modelcontextprotocol/serverInfo']`; identity is not a standalone `DiscoverResult.serverInfo` field.

### Primitive list operations

Provide specific exposed objects such as tools, resources or prompts.

An architecture can use both.

## Caching

Current MCP supports cacheable discovery/list results.

Clients should respect the caching semantics of the protocol version rather than invent permanent caches.

Capability exposure can change because of:

- server deployment;
- authorization;
- configuration;
- lifecycle changes.

## Authorization-Scoped Discovery

A server may expose only capabilities permitted by the credentials on a request.

This is preferable to exposing every capability and relying on later denial as the only boundary.

Discovery still does not replace enforcement on actual invocation.

## Capability Changes

Clients need a strategy for changed capability sets.

Options can include:

- cache expiry;
- change notifications;
- fresh discovery at workflow boundaries;
- recovery from not-found or incompatible calls.

## Compatibility

Compatibility concerns include:

- renamed tools;
- changed schemas;
- changed semantics;
- new required fields;
- changed authorization scopes;
- protocol-version changes.

Version tool contracts deliberately.

## Server Instructions

Discovery may include natural-language server instructions intended to help use the server.

Treat such instructions as server-provided content, not as authority that can override host policy.

## Contract Testing

Test:

- valid inputs;
- invalid inputs;
- boundary values;
- output conformance;
- error responses;
- permission failures;
- compatibility with target client SDKs.

## Exercise

Design a schema-defined tool for a generic approval request.

Specify:

1. input schema;
2. output shape;
3. side effects;
4. business rejection;
5. authorization requirement;
6. versioning strategy.

## Takeaway

> Discovery tells a client what exists. Contracts determine whether those capabilities are dependable.

Next: **05 — Authentication, Authorization and Trust**.
