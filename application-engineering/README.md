# Domain 03 — AI Application Engineering

## Purpose

Foundation models provide intelligence, but production value comes from engineering reliable systems around them.

AI Application Engineering teaches the transition from:

> A model that can generate responses

into:

> A dependable software system that uses AI capabilities safely and measurably.

This section focuses on the engineering layer between models and real-world outcomes.

## Core principle

AI outputs are probabilistic. Production systems must introduce deterministic boundaries.

```text
User / System Input
        |
        v
 Context Preparation
        |
        v
 AI Model
        |
        v
 Validation + Policies
        |
        v
 Business Logic
        |
        v
 Action + Feedback
```

## The AI Application Engineering Triangle

Every production AI application balances:

```
              Intelligence
                  ▲
                  |
                  |
Reliability ◄─────┼─────► Control
```

Increasing autonomy without reliability and control creates fragile systems.

## Curriculum

1. AI application architecture
2. Model APIs and provider abstraction
3. Prompt and instruction architecture
4. Structured outputs and schemas
5. Context engineering
6. Function calling and tool use
7. State management
8. Validation and deterministic boundaries
9. Reliability engineering
10. Streaming and long-running tasks
11. Model routing and cost optimisation
12. Observability and tracing
13. Security foundations
14. Testing AI applications
15. Application engineering capstone

## Mastery expectation

A learner completing this section should be able to design AI applications that are:

- reliable;
- observable;
- secure;
- cost-aware;
- testable;
- independent from unnecessary vendor lock-in.

## Canonical curriculum navigation

- [AI Application Architecture](./01-ai-application-architecture.md)
- [Model APIs and Provider Abstraction](./02-model-apis-and-provider-abstraction.md)
- [Prompt and Instruction Architecture](./03-prompt-and-instruction-architecture.md)
- [Structured Outputs and Schemas](./04-structured-outputs-and-schemas.md)
- [Context Engineering](./05-context-engineering.md)
- [Function Calling and Tool Use](./06-function-calling-and-tool-use.md)
- [State Management and Conversations](./07-state-management-and-conversations.md)
- [Validation and Deterministic Boundaries](./08-validation-and-deterministic-boundaries.md)
- [Reliability Patterns: Retries, Fallbacks and Failure Recovery](./09-reliability-patterns-retries-fallbacks.md)
- [Streaming and Long-Running AI Tasks](./10-streaming-and-long-running-tasks.md)
- [Model Routing and Cost Optimisation](./11-model-routing-and-cost-optimisation.md)
- [Observability, Tracing and Debugging AI Systems](./12-observability-tracing-and-debugging.md)
- [Security Basics for AI Applications](./13-security-basics-for-ai-applications.md)
- [Testing AI Applications](./14-testing-ai-applications.md)
- [Application Engineering Capstone](./15-application-engineering-capstone.md)

## Prerequisites and next steps

**Recommended prerequisites:** [01 — AI Foundations](../foundations/README.md), [02 — Modern Foundation Models](../foundations/README.md)

**Useful next domains:** [04 — Knowledge Systems and RAG](../knowledge-systems-rag/README.md), [05 — Agents](../agents/README.md), [10 — Evaluation and Reliability](../10-evaluation-reliability/README.md), [12 — AI System Design](../ai-system-design/README.md)

See the [full prerequisite map](../roadmap/prerequisites-and-paths.md) and [domain status matrix](../roadmap/domain-status.md).
