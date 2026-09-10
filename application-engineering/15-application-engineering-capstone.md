# Application Engineering Capstone

## Purpose

This capstone combines the principles from the Application Engineering curriculum into a complete production-style AI system design.

The goal is not to build a chatbot. The goal is to design an AI capability that can operate inside a real software system with controls, measurement and business outcomes.

## Capstone scenario

### AI Business Operations Intelligence System

A system that analyses operational information, provides recommendations, uses approved tools and supports human decision-making.

Examples of domains:

- commerce operations;
- customer support;
- finance analysis;
- internal knowledge workflows;
- software operations.

The architecture principles remain the same across domains.

## System architecture

```text
                         USER / BUSINESS EVENT
                                  |
                                  v
                         REQUEST UNDERSTANDING
                                  |
                                  v
                         CONTEXT ENGINEERING
                    (knowledge, history, policies)
                                  |
                                  v
                            MODEL ROUTER
                                  |
              +-------------------+-------------------+
              |                   |                   |
          Fast Model        Reasoning Model      Private Model
              |                   |                   |
              +-------------------+-------------------+
                                  |
                                  v
                          STRUCTURED OUTPUT
                                  |
                                  v
                           VALIDATION LAYER
                                  |
              +-------------------+-------------------+
              |                                       |
              v                                       v
        APPROVED TOOL CALLS                    HUMAN REVIEW
              |                                       |
              +-------------------+-------------------+
                                  |
                                  v
                         BUSINESS SYSTEM ACTION
                                  |
                                  v
                           AUDIT + OBSERVABILITY
                                  |
                                  v
                         EVALUATION + FEEDBACK
```

## Component requirements

## 1. Model layer

The system must:

- support more than one model provider where practical;
- understand capability differences between models;
- route tasks according to quality, cost, latency and privacy requirements;
- record model decisions for analysis.

## 2. Context layer

The system must define:

- what information the model receives;
- where that information comes from;
- how freshness is managed;
- how irrelevant or unsafe information is excluded.

Context is an engineered input, not an accidental collection of text.

## 3. Output layer

The model must not directly produce uncontrolled actions.

Use:

```text
Model output
      |
      v
Schema validation
      |
      v
Business rules
      |
      v
Allowed action
```

## 4. Tool layer

Tools must have:

- clear schemas;
- limited permissions;
- authentication boundaries;
- audit logging;
- failure handling.

A tool is a privileged capability, not just a function call.

## 5. Reliability layer

The system must handle:

- model failures;
- API failures;
- tool failures;
- timeouts;
- duplicate requests;
- partial completion;
- human escalation.

## 6. Security layer

Required controls:

- least privilege;
- tenant isolation;
- secret protection;
- prompt injection defence;
- data access boundaries;
- approval workflows for high-impact actions.

## 7. Observability layer

Capture:

- request;
- context supplied;
- model selected;
- latency;
- token/cost usage;
- tool calls;
- validation results;
- final outcome.

If a decision cannot be explained after the fact, the system is not production ready.

## 8. Evaluation layer

The system requires:

- baseline measurements;
- golden datasets;
- regression tests;
- quality metrics;
- safety tests;
- business outcome tracking.

## Example workflow

```text
Business user asks:
"Which products need pricing attention?"

        |
        v
System gathers:
- sales history
- margin
- stock
- advertising data
- competitor signals
- business rules

        |
        v
AI analyses information

        |
        v
Returns structured recommendation

        |
        v
Policy engine checks:
- margin protection
- approval limits
- account rules

        |
        v
Human approves or rejects

        |
        v
Action executed

        |
        v
Outcome measured
```

## Capstone acceptance criteria

A successful implementation should demonstrate:

### Architecture
- clear separation between AI capability and business control;
- replaceable model providers;
- explicit system boundaries.

### Engineering
- structured outputs;
- validation;
- retries and failure handling;
- asynchronous processing where required;
- observability.

### Security
- controlled permissions;
- auditability;
- safe tool usage;
- protection against malicious inputs.

### Evaluation
- measurable quality;
- regression protection;
- evidence of improvement over baseline.

### Business value
- a clear user problem;
- measurable outcome improvement;
- sustainable operating cost.

## Lessons from the capstone

The final lesson of Application Engineering is:

> The model is not the product. The engineered system around the model creates the value.

A reliable AI application is built from:

```text
Models
+
Context
+
Tools
+
Validation
+
Security
+
Observability
+
Evaluation
+
Business outcomes
```

This architecture becomes the foundation for the next roadmap sections: Knowledge Systems, Agents, Memory, MCP, Orchestration and the AI Operating System.