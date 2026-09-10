# Model APIs and Provider Abstraction

## Purpose

AI systems should benefit from improving models without becoming permanently dependent on one provider.

The goal is not to hide every difference between models. The goal is to create intentional boundaries.

## The naive approach

```text
Application
    |
    v
Single provider API
```

Risks:

- vendor lock-in;
- difficult migration;
- duplicated integrations;
- limited experimentation.

## Provider abstraction pattern

```text
                 Application
                      |
                      v
              AI Gateway Layer
                      |
        +-------------+-------------+
        |             |             |
        v             v             v
      GPT          Claude        Gemini
        |             |             |
        +-------------+-------------+
                      |
              Normalised interface
```

## What should be abstracted?

Useful abstractions:

- authentication;
- request handling;
- response formats;
- telemetry;
- cost tracking;
- retries;
- fallback behaviour;
- policy enforcement.

## What should not be hidden?

Do not pretend all models are identical.

Important differences remain:

- reasoning ability;
- context handling;
- latency;
- tool-use capability;
- pricing;
- safety behaviour;
- multimodal support.

## Model independence principle

Architecture should depend on capabilities, not marketing names.

A future model router should be able to decide:

```text
Simple classification
        -> efficient model

Complex analysis
        -> reasoning model

Private workload
        -> local model
```

## Practical exercise

Design an AI gateway interface supporting multiple providers while preserving provider-specific capabilities.

## Mastery gate

You understand this module when you can explain both:

- why abstraction protects architecture;
- why excessive abstraction can hide useful model differences.
