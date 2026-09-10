# Structured Outputs and Schemas

## Why this matters

Large language models produce probabilistic text. Production software requires predictable data.

Structured outputs create the boundary between model capability and reliable application behaviour.

The goal is not to make the model less intelligent. The goal is to place the model inside a controlled system.

## The problem with free-form output

A human can understand:

> "This product appears profitable. Increase advertising gradually."

A software system cannot safely determine:

- which product;
- what profitability calculation was used;
- what action is allowed;
- what confidence exists;
- whether approval is required.

## Structured output pattern

```text
User / System Input
        |
        v
      Model
        |
        v
 Structured Response
        |
        v
 Schema Validation
        |
        v
 Business Rules
        |
        v
 Application Action
```

## Core concepts

### Schemas

A schema defines the expected shape of data:

- fields;
- data types;
- required values;
- allowed options;
- constraints.

Example:

```json
{
  "product_id": "12345",
  "recommendation": "increase_ads",
  "confidence": 0.91,
  "requires_review": false
}
```

### Validation

Never assume a model response is correct because it matches a schema.

Validation should check:

- format;
- business rules;
- permissions;
- data freshness;
- allowed actions.

## AI output vs business authority

A critical production principle:

```text
AI recommendation
        |
        v
Validation layer
        |
        v
Policy engine
        |
        v
Action
```

The model should not automatically become the authority for consequential decisions.

## Common failure modes

### Valid but wrong

The output matches the schema but the conclusion is incorrect.

### Missing context

The model produces a valid answer from incomplete information.

### Schema gaming

The model fills required fields but does not provide meaningful reasoning.

### Overly rigid schemas

A schema can become so restrictive that useful model capability is lost.

## Architecture decisions

Use structured outputs when:

- another system consumes the result;
- workflows depend on the response;
- evaluation requires consistent comparison;
- auditing is required.

Avoid forcing structure where:

- creative exploration is the goal;
- human conversation is the product;
- uncertainty cannot be represented.

## Practical exercise

Build a product analysis service:

Input:
- product data;
- sales history;
- advertising data.

Output schema:

```text
ProductAnalysis
- product_id
- opportunity_score
- risks
- recommendation
- confidence
- human_review_required
```

Add validation before any action is taken.

## Mastery gate

You understand this topic when you can:

- design schemas for AI workflows;
- explain why valid JSON is not equal to correctness;
- add validation and business controls;
- decide where AI output stops and deterministic software begins.
