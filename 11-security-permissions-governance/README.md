# Domain 11 — Security, Permissions and Governance

## Learning objectives

By the end of this domain, you should be able to:

- explain the core concepts and distinctions across threat modelling, identity, least privilege, prompt injection, data isolation, tool security, approvals, sandboxing, audit and governance.
- build or evaluate a representative implementation rather than relying on a demo;
- make architecture decisions that account for reliability, security, cost, scale and operations;
- define the evidence, evaluation and governance required before production adoption.

## Purpose

This domain explains how to secure AI applications and agents by controlling what they may see, what they may do, how authority is delegated, and how actions are governed and audited.

The goal is not to make models perfectly safe through instructions alone.

The goal is to build layered controls around probabilistic systems.

## Core Principle

> Treat model output as untrusted input to the systems that hold real authority.

An AI system may reason about an action.

That does not mean it should automatically be allowed to execute the action.

## Security Model

A useful control stack is:

```text
Identity
   |
Authentication
   |
Authorization
   |
Capability Exposure
   |
Policy
   |
Approval
   |
Execution Boundary
   |
Validation
   |
Audit
```

Each layer reduces a different class of risk.

## What This Domain Covers

1. AI threat modelling
2. Identity, least privilege and capabilities
3. Prompt injection and untrusted content
4. Data security, privacy and isolation
5. Agent and tool security
6. Policy engines, approvals and action controls
7. Secrets, sandboxing and runtime security
8. Audit, incident response and governance
9. Capstone architecture

## Current Security Context

Modern agentic AI introduces risks beyond conventional prompt injection.

Current industry guidance includes:

- OWASP Top 10 for Agentic Applications for 2026;
- OWASP GenAI LLM Top 10 2026;
- NIST AI RMF and its Generative AI Profile;
- MITRE ATLAS and related adversarial AI knowledge bases.

These frameworks are useful references, not substitutes for system-specific threat modelling.

## Agentic Risk

Agentic systems can:

- choose tools;
- call external systems;
- manipulate data;
- delegate work;
- persist state;
- act over long periods.

The risk therefore depends on both model behaviour and the authority of the surrounding system.

## Trust Boundaries

Important boundaries can exist between:

- user and application;
- model and harness;
- harness and tool;
- application and MCP server;
- tenant and tenant;
- agent and memory;
- trusted instructions and untrusted content;
- internal and third-party systems.

Threat models should make these boundaries explicit.

## Security Is Not One Prompt

Instructions such as:

> "Never reveal secrets."

are useful but insufficient.

Where possible, enforce critical requirements through:

- data minimisation;
- access control;
- isolated credentials;
- tool filtering;
- policy engines;
- approvals;
- sandboxing;
- validation.

## Governance

Governance decides:

- who owns the system;
- what risks are acceptable;
- who can approve changes;
- what must be audited;
- how incidents are handled;
- when capabilities should be disabled.

Governance should be proportionate to consequence.

## Domain Boundaries

- **Domain 06 — Skills and Agent Harnesses:** packages capability and local control.
- **Domain 07 — MCP and Tool Ecosystems:** exposes external capabilities.
- **Domain 08 — Memory Systems:** governs persistent information.
- **Domain 09 — Orchestration and Multi-Agent Systems:** coordinates work.
- **Domain 10 — Evaluation and Reliability:** measures behaviour and failures.

This domain defines the security and authority boundaries around all of them.

## Mastery Outcomes

### Understand

Explain AI-specific threat surfaces including prompt injection, tool misuse, excessive agency, memory poisoning, identity abuse and supply-chain risk.

### Build

Implement least privilege, capability filtering, approval gates, secret isolation, sandboxing and audit.

### Architect

Design a layered security model across model, harness, tools, data, identity and runtime.

### Lead

Define governance, review, incident response, capability ownership and security evaluation for production AI systems.

## Architectural Rule

> The model may recommend an action; only trusted software and policy should grant authority to perform it.

## Reference Frameworks

- OWASP Top 10 for Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- OWASP GenAI LLM Top 10 2026: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/
- NIST AI RMF Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence

Next: **01 — AI Threat Modelling**.

## Canonical curriculum navigation

- [AI Threat Modelling](./01-ai-threat-modelling.md)
- [Identity, Least Privilege and Capabilities](./02-identity-least-privilege-and-capabilities.md)
- [Prompt Injection and Untrusted Content](./03-prompt-injection-and-untrusted-content.md)
- [Data Security, Privacy and Isolation](./04-data-security-privacy-and-isolation.md)
- [Agent and Tool Security](./05-agent-and-tool-security.md)
- [Policy Engines, Approvals and Action Controls](./06-policy-engines-approvals-and-action-controls.md)
- [Secrets, Sandboxing and Runtime Security](./07-secrets-sandboxing-and-runtime-security.md)
- [Audit, Incident Response and Governance](./08-audit-incident-response-and-governance.md)
- [Capstone: Secure an Agentic AI System](./09-capstone.md)
