# 03 — Model Formats and Quantization

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **03 — Model Formats and Quantization** within Open-Source and Local AI;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Separate model architecture, weights, numeric representation, quantization, file/container format, inference runtime, and serving layer.

Approximate raw weight memory begins with parameter count multiplied by represented bytes per parameter, but runtime capacity also includes KV cache, temporary tensors, buffers, metadata, and concurrency.

Quantization reduces precision to lower memory/bandwidth and can improve speed on compatible hardware, with possible quality loss. Two artifacts both called 4-bit can behave differently because of grouping, scales, mixed precision, calibration, kernels, and metadata.

GGUF is important in portable local-inference ecosystems as a container for tensors and metadata with multiple quantization options. Other runtimes use other representations.

Treat every conversion/quantization as a new deployable artifact: record base revision, converter/version, quantization, tokenizer, hashes, license lineage, runtime target, and evaluation result. Measure task quality rather than choosing the smallest file.

For sparse/MoE models distinguish total parameters, active parameters, storage, expert placement, routing, and bandwidth.

## Architecture lens

Evaluate this topic through **Understand → Build → Architect → Lead**. Separate model capability from system guarantees, and measure representative workloads rather than relying on model-size or benchmark marketing.

## Production rules

Keep business workflows above a stable model/runtime interface. Preserve artifact identity and provenance. Test quality, latency, reliability, privacy, security, and cost. Treat model/runtime changes as versioned production changes with rollback.

## AI-system boundary

```text
Business workflow
      ↓
Canonical AI capability
      ↓
Policy / governance
      ↓
Runtime or model adapter
      ↓
Inference
      ↓
Validation + evaluation
```

Probabilistic output never replaces deterministic authorization, state, or consequential execution controls.

## Exercise

Create an architecture decision record for this topic using a representative workload. Define requirements, alternatives, measurements, failure modes, governance, observability, and the evidence required for adoption.

## Takeaway

Choose technology from measured requirements and lifecycle cost, not novelty.

Next: **04 — Local Inference Fundamentals**.
