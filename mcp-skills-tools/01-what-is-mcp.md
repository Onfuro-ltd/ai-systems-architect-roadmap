# What Is MCP?

## Introduction

The Model Context Protocol (MCP) is a standard for connecting AI systems with external capabilities such as tools, data sources, and services.

The key idea is not that MCP makes models intelligent. Instead, MCP creates a consistent interface through which AI systems can discover and use capabilities.

## The Problem MCP Addresses

Before standard protocols, every AI application created custom integrations:

```text
AI Application
    |
    +-- Custom Database Integration
    +-- Custom API Integration
    +-- Custom File Access
```

This created duplication and made tool ecosystems difficult to scale.

MCP introduces a common communication layer.

## Where MCP Fits

```text
User
 |
AI Application / Agent
 |
MCP Client
 |
MCP Server
 |
Tools / Data / Services
```

The model reasons about tasks, while MCP provides access to external capabilities.

## MCP Is Not

MCP is not:

- a replacement for APIs;
- a replacement for databases;
- an autonomous agent;
- a security system;
- a guarantee of correctness.

It is a protocol layer.

## MCP vs APIs

APIs define how software communicates.

MCP standardises how AI systems discover and interact with capabilities.

A business API may expose orders, products, or payments. An MCP server can expose those capabilities in a form designed for AI systems.

## MCP vs Function Calling

Function calling allows a model to request a function execution.

MCP expands this concept by providing a standard ecosystem for exposing tools and resources across applications.

## Enterprise Importance

For enterprise AI, MCP can become part of a capability ecosystem:

```text
AI Agent
    |
    +-- Commerce Tools
    +-- Finance Tools
    +-- Knowledge Tools
    +-- Internal Systems
```

However, permissions, auditing, and security remain the responsibility of the architecture around MCP.

## Key Principle

> MCP standardises access to capabilities. It does not replace good software architecture.
