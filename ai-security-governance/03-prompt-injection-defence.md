# Prompt Injection Defence

## Core Principle

Prompt injection is an AI-specific security problem where untrusted content attempts to influence an AI system's behaviour.

The key rule:

> Treat external content as data, not instructions.

## Types of Injection

### Direct Prompt Injection

A user attempts to override system instructions.

### Indirect Prompt Injection

Malicious instructions are hidden inside documents, web pages, emails, retrieved knowledge, or files.

This is especially dangerous for RAG and agent systems.

## Secure Architecture

Weak:

```
Input
↓
LLM
↓
Action
```

Enterprise:

```
Input
↓
Classification
↓
Context filtering
↓
Policy checks
↓
Reasoning
↓
Tool permission checks
↓
Action
```

## Defence Strategies

- Separate instructions from data.
- Apply least-privilege tool access.
- Validate outputs before execution.
- Use allowlists for sensitive actions.
- Monitor suspicious behaviour.
- Maintain audit logs.

## Agent Security

A secure agent should follow:

```
Observe
↓
Analyse
↓
Recommend
↓
Validate
↓
Execute
```

## SEMLIS Relevance

Commerce agents may consume marketplace data, supplier documents, customer messages, and product content.

These sources must never automatically gain authority over the AI system.
