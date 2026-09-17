# 04 — LoRA and QLoRA

## Purpose
Parameter-efficient fine-tuning adapts a model without updating every base-model parameter.

> Smaller trainable deltas reduce training cost and artifact size; they do not reduce the need for rigorous data, evaluation, governance, and serving design.

## LoRA
LoRA adds trainable low-rank updates to selected transformations while most base weights remain frozen.

```text
Frozen base transformation + small trainable update → adapted behaviour
```

The deployable capability is tied to both base revision and adapter.

## QLoRA
QLoRA-style training combines a quantized base representation with trainable adapters to reduce training-memory requirements.

Training feasibility does not establish production quality.

## Configuration
Rank, scaling, dropout, and target modules affect adapter capacity. Treat them as measured experiment parameters.

## Compatibility and merging
Bind base revision, tokenizer, adapter, dataset, and training configuration. A new base revision may invalidate an adapter.

If adapters are merged into weights, the merged result becomes a distinct artifact and requires evaluation.

## Adapter fleets
Multiple specialists can share a base model, but routing, loading, cache, isolation, and lifecycle complexity grow quickly.

Per-tenant adapters need particularly strict rights, isolation, deletion, serving, evaluation, and upgrade policy. Tenant-specific retrieval or skills may be preferable.

## Quantization and security
Training quantization and inference quantization are separate choices. Evaluate the exact deployed combination.

Treat adapters as production dependencies: verify provenance and restrict upload, activation, and promotion.

## Exercise
Design three specialists from one base using LoRA/QLoRA. Define datasets, registry, compatibility, evaluation, routing, serving, and base-upgrade strategy.

## Takeaway
> The real deployable unit is the governed combination of base model, adapter, runtime, and evaluation evidence.

Next: **05 — Preference Optimisation**.
