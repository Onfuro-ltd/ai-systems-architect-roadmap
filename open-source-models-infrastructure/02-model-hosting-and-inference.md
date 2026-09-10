# Model Hosting & Inference

## Principle

Running an AI model is not only about downloading weights. Production inference requires architecture, optimisation, monitoring, and cost control.

## Model Execution Layers

```text
Application
    ↓
AI Gateway
    ↓
Inference Server
    ↓
Model Runtime
    ↓
GPU / Accelerator Hardware
```

## Hosting Options

### API Hosted Models

Best for:
- rapid development;
- frontier intelligence;
- avoiding infrastructure operations.

Trade-offs:
- usage cost;
- external dependency;
- data governance considerations.

### Self Hosted Models

Best for:
- privacy requirements;
- predictable workloads;
- specialised models;
- high-volume inference.

Trade-offs:
- GPU investment;
- maintenance;
- optimisation responsibility.

### Hybrid Architecture

Most enterprises will use a combination:

```text
General reasoning → Frontier models

Private workloads → Self-hosted models

High-volume tasks → Optimised specialist models
```

## Inference Optimisation

Important techniques:

- quantisation;
- batching;
- caching;
- model compression;
- efficient serving runtimes.

## GPU Decisions

The question is not:

> How many GPUs can we own?

The question is:

> What workload justifies dedicated infrastructure?

Evaluate:

- utilisation;
- latency requirements;
- security needs;
- model size;
- expected growth.

## SEMLIS Relevance

A future AI platform may use:

```text
AI Gateway

    ↓

Model Router

    ↓

Frontier Models + Private Models + Specialist Models

    ↓

Business AI Agents
```

The model should be replaceable. The business intelligence layer is the long-term asset.
