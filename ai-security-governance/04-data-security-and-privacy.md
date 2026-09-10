# Data Security & Privacy

## Core Principle

AI systems must protect data throughout its lifecycle.

Data security is not only about storage. It includes collection, processing, retrieval, model interaction, and output handling.

## AI Data Lifecycle

```
Collection
    ↓
Classification
    ↓
Storage
    ↓
Processing
    ↓
AI Usage
    ↓
Output Controls
    ↓
Retention / Deletion
```

## Key Risks

- Sensitive data exposure
- Accidental data leakage through prompts
- Unauthorised knowledge retrieval
- Excessive retention
- Weak access controls
- Third-party model exposure

## Enterprise Controls

### Data Classification

Identify:

- Public data
- Internal data
- Confidential data
- Restricted data

### Access Control

AI systems should only access information required for their role.

### Encryption

Protect:

- Data at rest
- Data in transit
- Secrets and credentials

### Privacy by Design

Build privacy into architecture rather than adding controls later.

## AI Knowledge Systems

RAG systems require controls around:

- document permissions;
- source validation;
- retrieval filtering;
- audit trails.

## SEMLIS Example

A commerce AI platform may process:

- customer information;
- marketplace credentials;
- financial data;
- supplier information.

The architecture should ensure:

```
Data Request
      ↓
Permission Check
      ↓
Approved Retrieval
      ↓
AI Processing
      ↓
Audited Output
```

## Final Principle

Secure AI is not achieved by restricting intelligence. It is achieved by controlling data flow, permissions, and accountability.