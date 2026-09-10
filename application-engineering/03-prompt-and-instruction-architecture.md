# Prompt and Instruction Architecture

## From prompts to instructions

Early AI usage focused on prompt tricks. Production systems require a more disciplined approach:

> Instruction architecture is the design of constraints, goals, context and expected behaviour supplied to a model.

## Components

A robust instruction layer usually defines:

- objective;
- role/context;
- available information;
- allowed actions;
- constraints;
- output format;
- uncertainty handling;
- escalation rules.

## Weak approach

```text
"Analyse this data and give advice."
```

Problems:

- unclear objective;
- unclear authority;
- unclear output;
- no handling of uncertainty.

## Stronger approach

```text
Goal:
Analyse product profitability.

Available data:
Orders, fees, advertising cost.

Rules:
Do not recommend actions without margin calculation.

Output:
Structured recommendation with confidence.
```

## Important principle

Instructions guide behaviour. They do not replace software controls.

A prompt saying:

> "Never expose customer data"

is not a security system.

Security requires:

- permissions;
- filtering;
- validation;
- monitoring;
- architecture.

## HumanScope principle

Complex ideas should be explained clearly, but technical precision must remain.

The purpose is understanding, not simplification that creates incorrect mental models.

## Practical exercise

Convert a vague AI request into a production instruction specification containing goals, constraints, inputs, outputs and failure handling.

## Mastery gate

You understand this module when you can design instructions as part of a larger system rather than treating prompts as magic commands.
