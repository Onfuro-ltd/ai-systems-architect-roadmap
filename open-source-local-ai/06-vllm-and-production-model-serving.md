# 06 — vLLM and Production Model Serving

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **06 — vLLM and Production Model Serving** within Open-Source and Local AI;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Production serving is a scheduling and resource-management problem around model inference.

A vLLM-style serving architecture addresses many concurrent requests using queueing, scheduling, continuous batching, and efficient KV-cache management. Throughput and individual latency trade against one another, so define SLOs by workload class.

Use admission control when demand exceeds safe capacity. Replicas, health-aware routing, model versions, warm state, quotas, rate limits, and priority classes support resilience and multi-tenancy.

Large models may require multi-device parallelism, adding communication and failure complexity. Familiar API compatibility does not make models semantically equivalent; structured outputs, tool use, tokenization, context, and generation behaviour still require evaluation/adapters.

Use immutable artifacts, canary/shadow evaluation where appropriate, health checks, rollback, and observability for queue time, TTFT, throughput, KV cache, memory, utilization, errors, and workload cost.

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

Next: **07 — Hardware, Memory and Performance**.
