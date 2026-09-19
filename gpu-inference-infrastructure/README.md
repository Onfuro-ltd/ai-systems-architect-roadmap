# Domain 16 — GPU and Inference Infrastructure

## Purpose

AI inference infrastructure converts model capability into a dependable production service. GPUs are central to much modern inference, but accelerator selection is only one part of the architecture.

> Do not buy or rent GPUs because a model fits in VRAM. Design infrastructure from workload quality, latency, throughput, availability, utilization, and total cost.

This domain develops practical judgement across GPU execution, VRAM and memory bandwidth, KV cache, batching, parallelism, inference servers, scheduling, cloud GPUs, owned hardware, capacity planning, resilience, observability, and cost engineering.

## Learning objectives

By the end of this domain, you should be able to explain inference-relevant GPU architecture; distinguish compute, memory capacity, and bandwidth; estimate runtime memory; reason about prefill, decode, KV cache, context, batching, and concurrency; understand multi-GPU parallelism; design serving and admission-control layers; compare cloud and owned accelerators; calculate utilization and total cost; benchmark exact deployments; and design resilient serving behind a model-independent router.

## Domain structure

01 GPU Architecture for AI Inference  
02 VRAM, Memory Bandwidth and Model Sizing  
03 Prefill, Decode and KV Cache  
04 Batching, Concurrency and Throughput  
05 Parallelism and Multi-GPU Inference  
06 Inference Servers, Scheduling and Admission Control  
07 Cloud GPUs vs Owned Hardware  
08 Capacity, Utilisation and Cost Engineering  
09 Resilience, Observability and Scaling  
10 GPU and Inference Infrastructure Capstone

## 1. Start with workload

```text
Required model quality
        ↓
Workload shape
        ↓
Context distribution
        ↓
Concurrency
        ↓
Latency / throughput SLO
        ↓
Availability + privacy
        ↓
Cost envelope
        ↓
Hardware + runtime architecture
```

Choosing hardware first reverses the engineering process.

## 2. GPU architecture through an inference lens

Understand compute units, matrix/tensor acceleration, VRAM, memory bandwidth, caches, interconnect, host memory/PCIe, precision support, kernels, and runtime software.

Headline compute alone does not predict inference performance.

## 3. Capacity, bandwidth and compute differ

A model can fit in memory but run too slowly; have abundant compute but be bandwidth constrained; run quickly for one request but collapse under concurrency; or fit weights but exhaust memory through KV cache.

Keep these dimensions separate.

## 4. Model memory

A first approximation is parameter count multiplied by bytes per represented parameter.

Production memory also includes quantization metadata, KV cache, temporary buffers, runtime workspace, allocator fragmentation, communication buffers, and concurrent sequences.

Never size a server from model-file size alone.

## 5. Prefill and decode

```text
Prompt tokens → PREFILL → first token → DECODE → subsequent tokens
```

Prefill and decode have different characteristics. Track time to first token separately from decode throughput.

## 6. KV cache and context

KV cache stores attention state used during generation. Its demand depends on architecture, sequence length, concurrent sequences, representation, and serving strategy.

Long context increases prefill work, KV memory, scheduling pressure, cost, contention, and tail latency. Advertised context is not free capacity.

## 7. Batching and concurrency

Batching can improve utilization but may increase queueing or latency. Continuous batching dynamically schedules active sequences as requests arrive and finish.

Concurrency includes active sequences, tokens, KV occupancy, batch composition, queue depth, and priority—not merely open HTTP connections.

## 8. Parallelism

Large models or throughput requirements may use tensor, pipeline, replica/data, or expert parallelism.

Each introduces communication, scheduling, and failure trade-offs. Interconnect topology matters; several GPUs are not automatically equivalent to one large logical accelerator.

## 9. Scale up vs scale out

Scale up adds capability within a serving node. Scale out adds nodes or replicas.

Scale up may be required to fit one model. Scale out often improves throughput and resilience when a model fits per serving unit. Distributed complexity needs evidence.

## 10. Inference serving

```text
Clients
  ↓
Authentication / quotas
  ↓
Admission control
  ↓
Queue / scheduler
  ↓
Inference workers
  ↓
Streaming / response
  ↓
Metrics + tracing + accounting
```

Model servers are infrastructure components, not business-policy engines.

## 11. Admission control and backpressure

When demand exceeds safe capacity, deliberately queue within limits, reject, route elsewhere, reduce approved workload size, defer background work, or degrade noncritical capability.

Unbounded queues convert overload into an outage.

If arrival rate remains above service capacity, queueing increases latency, timeouts can trigger retries, and retries can amplify load. Use bounded queues, retry discipline, prioritization, and upstream backpressure.

## 12. Workload classes and tenancy

Separate interactive, asynchronous, batch, premium, background, and consequential workloads when their SLOs differ.

Shared serving requires authenticated tenant/workload identity, quotas, rate limits, concurrency controls, priority/fairness, accounting, isolation, and per-tenant observability.

## 13. Cloud GPUs

Cloud or rented accelerators offer fast provisioning, elasticity, hardware choice, regional deployment, and lower capital commitment.

Costs can include hourly rates, storage/network, idle reservations, availability constraints, and provider dependency.

## 14. Owned hardware

Owned infrastructure may suit stable high-utilization demand or strong control requirements.

Total cost includes hardware, financing/depreciation, power, cooling, facilities, networking, storage, redundancy, maintenance, engineering, spares, downtime risk, and refresh cycles.

Purchase price is not total cost.

## 15. Utilization changes economics

An owned accelerator sitting idle can cost more per useful task than an expensive API. Sustained predictable demand can reverse the equation.

Model realistic utilization.

## 16. Capacity planning

Plan normal load, peaks, failure capacity, rollout overlap, maintenance, and growth. Do not size only for average traffic.

Ask what happens when one serving unit disappears during peak demand.

## 17. Autoscaling and cold starts

GPU scaling can be slow because of provisioning, artifact transfer, runtime initialization, model load, compilation/warmup, and cache population.

Measure the complete path from node provisioning to traffic readiness. Consider warm pools, queue-aware scaling, scheduled capacity, and predictive capacity where justified.

## 18. Reliability

Plan for GPU/node failure, runtime/driver failure, OOM, model-load failure, corrupted artifacts, interconnect failure, scheduler failure, provider capacity loss, power/thermal issues, and network/storage failures.

Availability is not model correctness. Observe both.

## 19. Rollout and rollback

Model, quantization, runtime, driver, kernel, serving configuration, and hardware changes can all affect performance.

Use immutable versions, controlled rollout, benchmark gates, health checks, and rollback.

## 20. Observability

Capture model/artifact/runtime version, hardware identity, workload/tenant class, queue depth/time, TTFT, prefill/decode throughput, tokens, active sequences, batch size, KV utilization, VRAM/RAM, GPU utilization, errors/OOM, fallback/routing, cost allocation, and evaluated outcome.

Where useful, include memory-bandwidth and power/thermal signals.

## 21. Benchmark exact deployments

Benchmark the exact model, precision/quantization, runtime/server, kernels, driver stack, hardware, topology, context distribution, concurrency, and generation lengths.

A tokens-per-second number without workload conditions is weak evidence.

## 22. Cost per successful outcome

```text
Total serving cost / successful useful outcomes
```

A cheaper configuration that causes quality regression, queueing, or failures may cost more in practice.

## 23. Hybrid infrastructure

```text
Model Router
   ├── Hosted frontier API
   ├── Rented GPU serving
   ├── Owned/private GPU cluster
   ├── CPU/local inference
   └── Specialist serving tier
```

Policy determines eligible routes; measured capability, latency, availability, and economics select among them.

## 24. Model independence

Keep business workflows above canonical inference interfaces and routing. GPU infrastructure should be replaceable without rewriting business logic.

## Architecture principles

1. Start from workload, not hardware.
2. Capacity, bandwidth, compute, latency, and throughput are different.
3. Include KV cache and concurrency in memory sizing.
4. Optimize TTFT and decode according to workload.
5. Use parallelism only when justified.
6. Bound queues and apply backpressure.
7. Treat utilization as an economic variable.
8. Compare full lifecycle cost of cloud and owned hardware.
9. Benchmark exact deployed combinations.
10. Connect infrastructure metrics to successful outcomes.
11. Preserve model and infrastructure portability.
12. Design for failure and recovery before peak load.

## Capstone direction

The capstone will design an inference platform serving interactive and asynchronous workloads across hosted APIs, rented GPUs, and owned/private accelerators.

It must include workload SLOs, model/hardware sizing, KV/context planning, batching/concurrency, multi-GPU strategy, serving architecture, admission control, tenant fairness, capacity planning, cloud-vs-owned economics, scaling/cold starts, failure recovery, rollout/rollback, observability, cost per successful outcome, and model-router integration.

## Takeaway

> GPU infrastructure is not a collection of expensive devices. It is a capacity, scheduling, reliability, and economic system that turns model inference into a dependable service.

Next: **01 — GPU Architecture for AI Inference**.

## Canonical curriculum navigation

- [GPU Architecture for AI Inference](./01-gpu-architecture-for-ai-inference.md)
- [VRAM, Memory Bandwidth and Model Sizing](./02-vram-memory-bandwidth-and-model-sizing.md)
- [Prefill, Decode and KV Cache](./03-prefill-decode-and-kv-cache.md)
- [Batching, Concurrency and Throughput](./04-batching-concurrency-and-throughput.md)
- [Parallelism and Multi-GPU Inference](./05-parallelism-and-multi-gpu-inference.md)
- [Inference Servers, Scheduling and Admission Control](./06-inference-servers-scheduling-and-admission-control.md)
- [Cloud GPUs vs Owned Hardware](./07-cloud-gpus-vs-owned-hardware.md)
- [Capacity, Utilisation and Cost Engineering](./08-capacity-utilisation-and-cost-engineering.md)
- [Resilience, Observability and Scaling](./09-resilience-observability-and-scaling.md)
- [GPU and Inference Infrastructure Capstone](./10-gpu-inference-infrastructure-capstone.md)


## Primary references

The detailed chapters use current primary/official references such as the NVIDIA CUDA guides, vLLM documentation and PagedAttention paper, PyTorch distributed documentation, TensorRT-LLM documentation and MLPerf Inference. Benchmark claims should always identify the exact model/runtime/hardware/workload combination.

## Prerequisites and next steps

**Recommended prerequisites:** [01 — AI Foundations](../foundations/README.md), [02 — Modern Foundation Models](../foundations/README.md), [03 — AI Application Engineering](../application-engineering/README.md), [14 — Open-Source and Local AI](../open-source-local-ai/README.md)

**Useful next domains:** [17 — MLOps and LLMOps](../mlops-llmops/README.md), [21 — AI Economics and Model Routing](../ai-economics-model-routing/README.md), [22 — Enterprise AI](../enterprise-ai/README.md), [28 — Build an AI Operating System](../ai-operating-system/README.md)

See the [full prerequisite map](../roadmap/prerequisites-and-paths.md) and [domain status matrix](../roadmap/domain-status.md).
