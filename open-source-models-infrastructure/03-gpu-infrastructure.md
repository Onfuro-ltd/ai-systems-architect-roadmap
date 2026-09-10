# 03 — GPU Infrastructure

## Principle

GPU infrastructure is a business decision, not an AI status symbol.

The correct question is not:

> How many GPUs can we own?

The correct question is:

> What workloads justify dedicated compute?

## GPU decisions

A GPU platform decision depends on:

- model size;
- required VRAM;
- inference volume;
- latency requirements;
- privacy requirements;
- operating cost;
- engineering capability.

## GPU memory matters

The most important specification is often VRAM.

A 96GB GPU system can be valuable for:

- large model inference;
- private AI services;
- experimentation;
- running multiple smaller models.

It is not automatically the best choice for every company.

## Cloud vs owned hardware

### Cloud GPU

Advantages:

- flexible capacity;
- no hardware maintenance;
- easy experimentation.

Disadvantages:

- ongoing rental cost;
- availability constraints;
- less infrastructure ownership.

### Owned GPU server

Advantages:

- predictable workloads;
- long-term usage;
- private processing;
- infrastructure control.

Disadvantages:

- upfront investment;
- depreciation;
- power and cooling requirements;
- maintenance responsibility.

## Enterprise pattern

A mature AI company normally uses a hybrid approach:

```
Production workloads
        |
        +-- Dedicated infrastructure where justified

Experimentation
        |
        +-- Cloud GPU resources
```

## SEMLIS relevance

The future architecture should not start with GPUs.

It should start with workloads:

```
Business problem
        |
AI capability required
        |
Model selection
        |
Infrastructure decision
```

The competitive advantage is the intelligence layer, not ownership of hardware.
