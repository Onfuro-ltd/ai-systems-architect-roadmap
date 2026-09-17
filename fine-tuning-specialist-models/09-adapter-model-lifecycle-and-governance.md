# 09 — Adapter and Model Lifecycle and Governance

## Purpose
Fine-tuned models and adapters become production dependencies needing identity, ownership, approval, monitoring, rollback, and retirement.

> Training creates an artifact. Governance turns it into an operable production capability.

## Artifact identity

```text
Base revision + tokenizer + dataset + training code/config + adapter/weights hash + license lineage + evaluation + approval + runtime
```

Any critical change creates a new candidate.

## Registry lifecycle
Use explicit states such as experiment, evaluation, approved, canary, production, restricted, deprecated, and retired.

## Reproducibility
Store immutable references to data, code, configuration, environment, and artifacts. Exact bitwise reproduction may vary, but provenance must explain and rebuild the experiment.

## Upgrades
A base-model upgrade is not transparent. Re-run compatibility, quality, safety, serving, and economic tests. Adapters may require retraining.

## Rollout
Use immutable versions, shadow/canary where appropriate, health monitoring, traffic control, and rollback. Never overwrite the sole production artifact in place.

## Monitoring and drift
Track task outcomes, critical errors, input drift, escalation, latency, throughput, cost, and serving health.

Drift triggers investigation, not automatic retraining. Root cause may be data, workflow, upstream systems, or business change.

## Feedback
Production examples enter a candidate store, then verification and curation before training. Avoid uncontrolled self-training loops.

## Security and privacy
Restrict model/adapter registration, promotion, activation, download, and replacement. Verify artifact integrity.

Maintain source-data lineage so privacy/deletion changes can be assessed before and after training.

## Multi-tenancy
Tenant-specific artifacts require strict ownership, serving isolation, access, retention, deletion, and routing controls.

## Retirement and ownership
Retirement stops new traffic, preserves required evidence, handles rollback windows, removes artifacts according to policy, and updates routing dependencies.

Assign accountable owners for data, model quality, infrastructure, governance, and business outcomes.

## Exercise
Design lifecycle management for ten specialist adapters sharing two base models.

## Takeaway
> Specialization cost grows with every model and adapter. Build lifecycle controls before the fleet becomes too large to understand.

Next: **10 — Fine-Tuning and Specialist Models Capstone**.
