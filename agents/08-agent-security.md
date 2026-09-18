# 08 — Agent Security

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **08 — Agent Security** within Agents;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Overview

Agents introduce a new security model because they can reason, access tools, retrieve information, and perform actions.

The principle:

> An agent should have the minimum capability required to complete its task, with every important action controlled and observable.

## Security Boundaries

A production agent system separates:

- model reasoning
- user identity
- permissions
- tools
- data access
- execution environment
- audit records

The model should never be the final authority for security decisions.

## Main Risks

### Prompt Injection

Instructions can arrive through:

- users
- documents
- emails
- websites
- retrieved knowledge

Trusted system instructions must remain separate from untrusted content.

### Tool Abuse

Tools are privileged operations. Controls should include:

- authentication
- authorisation
- validation
- rate limits
- audit logs
- approval workflows

### Data Leakage

Agents may expose information through:

- memory
- retrieval
- logs
- tool responses
- shared context

Enterprise systems require permission-aware access.

## Autonomy Levels

Low risk:

- analysis
- search
- reporting

Medium risk:

- recommendations
- drafts
- workflow preparation

High risk:

- financial actions
- system changes
- external communication

Higher impact actions require stronger controls.

## Secure Agent Architecture

User

↓

Identity and permissions

↓

Agent reasoning layer

↓

Policy enforcement

↓

Approved tools

↓

Business systems

↓

Audit trail

## Enterprise Principle

The future is not unlimited autonomous agents.

The future is controlled autonomy:

Capability + Permission + Validation + Observability.

## Architect exercise

Design or inspect a representative system that uses **08 — Agent Security**. Produce an architecture sketch, identify at least three failure modes, state one security or governance control where relevant, define one measurable success criterion, and compare the design with a simpler baseline. Record what evidence would justify keeping the added complexity.
