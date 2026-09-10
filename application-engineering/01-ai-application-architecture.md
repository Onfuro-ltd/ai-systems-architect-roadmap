# AI Application Architecture

## Why this matters

A common mistake in AI development is starting with the model:

> Which model should we use?

The better first question is:

> Where does intelligence belong inside the system?

A production AI application is not an LLM call. It is a system containing intelligence, controls, data, software boundaries and feedback.

## The basic architecture

```text
Input
 |
 v
Context Preparation
 |
 v
Model Invocation
 |
 v
Validation
 |
 v
Business Rules
 |
 v
Action
 |
 v
Measurement / Feedback
```

## AI is a component, not the whole application

Traditional software often follows:

```text
Input
 |
Business Logic
 |
Output
```

AI applications introduce a probabilistic component:

```text
Input
 |
Context + Instructions
 |
Model
 |
Validation
 |
Deterministic Software
 |
Output
```

The surrounding engineering is what makes the system reliable.

## Core architectural questions

Before selecting a model, define:

- What decision or task is being improved?
- What information does the system require?
- What actions can it take?
- What must always be deterministic?
- Where is human approval required?
- How will success be measured?

## Common failure pattern

Weak AI architecture:

```text
User
 |
Prompt
 |
LLM
 |
Answer
```

Problems:

- no validation;
- no visibility into context;
- no evaluation;
- no recovery strategy;
- no control boundary.

## Production principle

The model should provide intelligence. The application should provide trust.

## Practical exercise

Design an AI application and document:

- inputs;
- context sources;
- model responsibilities;
- deterministic components;
- security boundaries;
- evaluation metrics.

## Mastery gate

You understand this module when you can explain why a better model alone does not automatically create a better AI product.
