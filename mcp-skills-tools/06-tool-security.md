# Tool Security

## Principle

AI tools are not just features. They are controlled access points into real systems.

A production AI system must treat every tool as a security boundary.

## Security Model

```
User Identity
      ↓
Authentication
      ↓
Authorisation
      ↓
AI Agent
      ↓
Tool Permission Check
      ↓
External System
      ↓
Audit Record
```

## Least Privilege

Agents should only receive the minimum capabilities required.

Examples:

Allowed:
- Read sales analytics
- Generate reports
- Analyse customer feedback

Restricted:
- Change pricing
- Issue refunds
- Modify financial records

## MCP Security Considerations

MCP standardises capability access, but it does not automatically provide security.

Secure MCP implementations require:

- authenticated clients;
- authorised tools;
- scoped permissions;
- logging;
- monitoring;
- approval controls.

## Dangerous Actions

Actions should be classified by risk.

Low risk:

- Search
- Analysis
- Reporting

Medium risk:

- Drafting communication
- Preparing changes
- Workflow execution

High risk:

- Financial transactions
- Deleting data
- External system modifications

Higher impact requires stronger controls.

## Human Approval

For important business actions:

```
AI Recommendation
        ↓
Validation Rules
        ↓
Human Approval
        ↓
Execution
        ↓
Audit
```

## Why This Matters

Enterprise AI will not succeed because agents have unlimited access.

It will succeed because agents have controlled, measurable and secure capabilities.

For systems like SEMLIS, marketplace tools should expose business capabilities while maintaining strict permission boundaries.
