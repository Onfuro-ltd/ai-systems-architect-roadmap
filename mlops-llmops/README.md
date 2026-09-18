# Domain 17 — MLOps and LLMOps

## Purpose

Production AI systems change across models, prompts, datasets, retrieval, tools, runtimes, policies and infrastructure. MLOps and LLMOps make those changes traceable, testable, deployable, observable and reversible.

> An AI capability is not production-ready until you can identify what is running, prove why it was promoted, observe how it behaves, and safely roll it back.

## Domain structure

01 Experiment Tracking and Reproducibility  
02 Model, Prompt, Dataset and Artifact Versioning  
03 Evaluation Pipelines and Quality Gates  
04 Deployment Strategies and Release Engineering  
05 Observability, Tracing and Production Telemetry  
06 Drift, Feedback and Continuous Improvement  
07 Rollback, Incident Response and Recovery  
08 Operational Governance and Model Registry  
09 LLMOps Platform Architecture  
10 MLOps and LLMOps Capstone

## Core lifecycle

```text
Change hypothesis
      ↓
Versioned experiment
      ↓
Offline evaluation
      ↓
Approval / quality gate
      ↓
Shadow / canary / controlled release
      ↓
Production telemetry + outcomes
      ↓
Drift / incident detection
      ↓
Rollback or curated improvement
```

The deployable unit is often a system configuration, not merely a model: model + prompt + retrieval + tools + policy + runtime + data contracts + evaluation evidence.

## Principles

1. Version every behaviour-affecting dependency.
2. Reproduce experiments from immutable references.
3. Evaluation gates deployment.
4. Production telemetry includes quality, not only uptime.
5. Separate raw feedback from verified learning evidence.
6. Drift triggers diagnosis, not automatic retraining.
7. Every release needs rollback.
8. Registries record lineage and approval, not just files.
9. Keep business workflows independent of specific model vendors.
10. Connect operational metrics to successful outcomes.

## Takeaway

> LLMOps is the operating discipline that keeps probabilistic AI changes controlled inside deterministic production systems.

Next: **01 — Experiment Tracking and Reproducibility**.
