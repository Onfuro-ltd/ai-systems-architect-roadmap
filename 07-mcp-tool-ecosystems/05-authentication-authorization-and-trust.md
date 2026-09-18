# 05 — Authentication, Authorization and Trust

## Purpose

MCP can transport requests to powerful capabilities.

That makes identity, authorization and trust boundaries part of the architecture even though MCP is not itself a complete enterprise permission system.

## Core Principle

> Connectivity is not authority.

A client being able to reach an MCP server does not mean every exposed capability should be usable by every caller or model.

## Authentication vs Authorization

### Authentication

Establishes who or what is presenting credentials.

### Authorization

Determines what that identity is permitted to access or do.

### Policy

Applies broader rules such as approvals, risk thresholds, tenant boundaries and business constraints.

These layers should not be collapsed.

## HTTP Authorization

For HTTP-based MCP transports, the current authorization framework is aligned with OAuth 2.1 and related OAuth/OpenID standards.

Implementations supporting protected remote MCP servers should follow the current MCP authorization specification rather than generic OAuth examples from older tutorials.

## Protected Resource Role

A protected MCP server acts as an OAuth resource server.

The client obtains an access token intended for that MCP resource and presents it on protected requests.

The server validates the token before accepting it.

## Protected Resource Metadata

Current MCP authorization uses OAuth Protected Resource Metadata so clients can discover the authorization server associated with the MCP resource.

This separates resource-server identity from authorization-server discovery.

## Client Registration

Current MCP prefers Client ID Metadata Documents where supported.

Dynamic Client Registration remains for compatibility but is deprecated in the 2026-07-28 generation of the protocol.

An implementation should follow the exact registration mechanisms supported by its authorization server and MCP client.

## Resource Indicators

Clients request tokens for the intended MCP resource.

The `resource` parameter binds authorization to the target resource.

This reduces the risk of a token intended for one service being replayed to another.

## Audience Validation

The MCP server must validate that a presented token was issued for it.

Token passthrough between unrelated services is dangerous.

A server should not accept tokens merely because they are valid tokens somewhere.

## Bearer Tokens

Bearer access tokens should be carried through the Authorization header.

They should not be placed in URL query strings.

Secrets should not appear in model context, tool descriptions or ordinary logs.

## stdio Credentials

The HTTP OAuth authorization framework is not the model for stdio transport.

Local stdio servers commonly receive credentials through the environment or another host-controlled mechanism.

This creates a different trust boundary.

The host must control what credentials a local process can access.

## Least Privilege

Capability exposure should be narrower than infrastructure access whenever practical.

Examples:

- read-only server instead of read/write;
- scoped token instead of broad account credential;
- limited tool set instead of unrestricted API proxy;
- tenant-specific access instead of global access.

## Tool-Level Authorization

Authorization must be enforced when the operation executes.

Filtering discovery is useful, but it is not enough.

The server should still validate authority for each consequential call.

## User Approval

Protocol authorization and user approval are different.

A token may technically permit an action while product policy still requires confirmation.

The harness can therefore enforce:

```text
Credential permits action
        +
Policy permits action
        +
Required approval obtained
        =
Action may execute
```

## Confused Deputy Risk

An MCP server can become a deputy acting on behalf of callers.

Architectures should prevent callers from tricking a privileged server into using authority outside the caller's intended scope.

Resource binding, scope checks, explicit target validation and policy boundaries are important controls.

## Trusting Server Content

Tool descriptions, prompts, resources and server instructions originate outside the host.

Treat them according to their trust level.

They should not automatically override:

- system policy;
- user intent;
- authorization boundaries;
- data-handling rules.

## Enterprise Identity

Enterprise environments may place MCP behind:

- identity providers;
- gateways;
- policy engines;
- service identities;
- workload identity;
- zero-trust network controls.

MCP should integrate with that architecture rather than create an isolated parallel identity system.

## Exercise

Design the authorization path for a remote MCP server exposing both read and write capabilities.

Define:

1. caller identity;
2. OAuth resource;
3. scopes;
4. discovery filtering;
5. invocation enforcement;
6. approval requirement;
7. audit evidence.

## Takeaway

> MCP provides an integration protocol. Authority must still be engineered explicitly.

Next: **06 — MCP vs APIs, Function Calling and Events**.
