# Fine-Tuning Fundamentals

## Purpose

Fine-tuning is one of the most misunderstood parts of modern AI engineering.

The goal is not to make a model magically know everything. The goal is to adapt a model for a specific behaviour, domain, style, or task.

## Core Principle

> Use fine-tuning to change behaviour. Use retrieval and tools to provide knowledge.

## Fine-Tuning vs RAG

### RAG is best for:

- changing information;
- company documents;
- policies;
- product catalogues;
- frequently updated knowledge.

### Fine-tuning is best for:

- consistent output style;
- specialised behaviours;
- classification patterns;
- structured responses;
- domain-specific workflows.

## Common Fine-Tuning Approaches

### Supervised Fine-Tuning (SFT)

Training a model using high-quality examples of desired behaviour.

### Instruction Tuning

Teaching a model how to follow specific task instructions.

### Domain Adaptation

Adapting a general model to a specialised field.

## Risks

Fine-tuning can introduce:

- overfitting;
- reduced general capability;
- poor data behaviour;
- hidden biases;
- maintenance burden.

## Enterprise Decision Framework

Before fine-tuning ask:

1. Is the problem actually solved by better data retrieval?
2. Do we have enough high-quality examples?
3. Is the behaviour stable over time?
4. Can we evaluate improvement objectively?

## SEMLIS Example

Possible fine-tuning candidates:

- product categorisation;
- listing quality scoring;
- structured recommendation formats;
- domain-specific analysis style.

Less suitable:

- current marketplace policies;
- changing fees;
- live inventory knowledge.

Those should use tools and retrieval.
