# 04 — Tool Use and Action

## Core Principle

Agents become useful when they can safely interact with external capabilities. Tools are not just functions; they are controlled action boundaries.

## Agent Capability Model

```
Goal
 ↓
Reasoning
 ↓
Tool Selection
 ↓
Tool Execution
 ↓
Observation
 ↓
Validation
 ↓
Next Action
```

## Tools Are Capabilities

Examples:

- APIs
- Databases
- Search systems
- File systems
- Business applications
- Marketplace integrations

The model decides what may be useful, but the application controls what is actually allowed.

## Tool Design Principles

Good tools should have:

- clear purpose
- strict input schemas
- predictable outputs
- permission boundaries
- audit logging
- failure handling

## Tool Permissions

Never give an agent unrestricted access.

```
Agent
 ↓
Allowed tools
 ↓
Permission checks
 ↓
Business rules
 ↓
Action
```

## Reversible vs Irreversible Actions

Low risk:

- search
- analyse
- calculate

Higher risk:

- changing prices
- sending communications
- deleting data
- financial actions

Higher impact actions require more controls.

## MCP and Tool Ecosystems

Modern AI systems are moving toward standardised tool interfaces. MCP and similar approaches allow models to discover and use capabilities through controlled interfaces.

The important architecture principle remains:

Tools expand capability. They do not remove the need for security, validation and governance.

## SEMLIS Example

A marketplace agent should not directly change prices.

Instead:

```
Analyse market
 ↓
Generate recommendation
 ↓
Check pricing rules
 ↓
Approval workflow
 ↓
Update marketplace
 ↓
Measure outcome
```

The agent assists the business process; it does not bypass it.
