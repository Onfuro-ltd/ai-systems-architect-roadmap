# 08 — Agent Security

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
