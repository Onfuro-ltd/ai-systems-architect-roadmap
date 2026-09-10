# 07 — MCP Architecture

## Core Principle

MCP is a capability connection architecture. It connects AI systems to tools and resources, but it does not replace application architecture.

## High-Level Architecture

```text
AI Application
      |
      v
MCP Client
      |
      v
MCP Server
      |
      +---- Tools
      +---- Resources
      +---- Prompts
      |
      v
Business Systems
```

## MCP Components

### MCP Client

The component used by an AI application to communicate with MCP servers.

Responsibilities:
- Discover capabilities
- Request tools
- Send context
- Receive results

### MCP Server

A controlled gateway exposing capabilities.

Responsibilities:
- Authentication
- Authorisation
- Tool execution
- Data access
- Validation

### Tools

Actions an AI system can request.

Examples:
- Query database
- Call marketplace API
- Create report
- Execute workflow

### Resources

Information available to the AI system.

Examples:
- Documents
- Files
- Business data
- Knowledge sources

## Enterprise Pattern

```text
                 AI Agent
                    |
                    v
              MCP Gateway
                    |
     +--------------+--------------+
     |              |              |
 Amazon Service  Finance       Knowledge
 Connector       Service       Service
```

## Important Rules

MCP should not bypass:

- existing APIs
- permissions
- security controls
- audit requirements

It should expose capabilities safely.

## SEMLIS Application

Future SEMLIS MCP capabilities could expose:

- Amazon SP-API tools
- eBay tools
- Shopify tools
- Inventory services
- Profit calculations
- VAT analysis
- Reporting systems

The AI layer reasons, while MCP provides controlled access to business capabilities.
