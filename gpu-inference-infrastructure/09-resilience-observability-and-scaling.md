# 09 — Resilience, Observability and Scaling

## Purpose

Inference reliability requires visibility from user request to accelerator and a recovery design for hardware, runtime, artifact and capacity failures.

## Learning outcomes

By the end of this module, you should be able to:
- define inference SLOs and the telemetry required to explain them
- design failure containment and degraded-mode behaviour
- separate model correctness from service availability
- plan controlled rollout, rollback and scaling

## Failure taxonomy

Include GPU/node failure, OOM, runtime/driver error, artifact corruption, scheduler failure, network/storage failure and provider capacity loss.

## Observability

Capture request/workload identity, model/artifact/runtime version, hardware, queue time, TTFT, decode throughput, active sequences, KV/VRAM occupancy, errors and routing/fallback.

## Tracing

A request trace should connect gateway, scheduler, worker and downstream evaluation so operators can distinguish queueing, inference and application failures.

## Scaling

Scale replicas, serving units or workload routing based on measured bottlenecks. Do not scale GPU count when the bottleneck is upstream or downstream.

## Rollout

Model, quantization, kernel, runtime, driver and hardware changes can all shift quality/performance. Use canary/shadow benchmarks and rollback.

## Graceful degradation

Possible modes include smaller eligible model, reduced context, background deferral or read-only capability. Fallbacks must still satisfy policy and quality floors.

## Failure modes

- availability dashboard hides model-quality regression
- fallback violates data/residency policy
- rollout changes several stack layers with no isolation
- OOM/retry loop amplifies an incident
- telemetry lacks version identity needed for diagnosis

## Security and governance

Observability data can contain prompts, outputs or tenant metadata. Minimise sensitive logging, enforce access and preserve audit evidence without creating an unrestricted shadow data store.

## Economics and operations

Reliability consumes spare capacity, redundant paths and engineering time. Include those costs in unit economics instead of treating them as waste.

## Practical exercise

Design an incident drill where one serving unit begins OOMing after a runtime rollout. Define detection, containment, rollback, traffic routing, evidence and the regression test added afterward.

## Architect checklist

- [ ] SLOs distinguish availability, latency and quality
- [ ] all stack versions are traceable
- [ ] fallbacks preserve policy
- [ ] rollback is rehearsed
- [ ] incident learning becomes a regression test

## Primary reading

- [vLLM documentation](https://docs.vllm.ai/en/stable/)
- [NVIDIA TensorRT-LLM documentation](https://docs.nvidia.com/tensorrt-llm/)
- [MLPerf Inference documentation](https://docs.mlcommons.org/inference/index_gh/)

## Mastery gate

Explain when **Resilience, Observability and Scaling** changes the architecture materially, identify the evidence you would collect before making the decision, and state which controls remain outside the inference runtime.

## Takeaway

> Reliable inference is an observable, recoverable service—not a GPU that usually responds.

Next: **10 — GPU and Inference Infrastructure Capstone**.
