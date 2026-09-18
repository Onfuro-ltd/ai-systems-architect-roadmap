# Domain 14 — Open-Source and Local AI

## Purpose

Open-weight and locally deployed models change the architecture of AI systems. They can provide stronger control over data paths, deployment, customization, latency, availability, and economics, but they also transfer operational responsibility from a model provider to the system owner.

> Local AI is not automatically cheaper, more private, or more independent. It becomes valuable when control over the model and inference boundary solves a measured requirement.

This domain develops the judgement to evaluate open-weight models, licenses, quantization, local inference formats, serving engines, privacy boundaries, edge deployment, and trade-offs between APIs, rented infrastructure, owned hardware, and hybrid routing.

## Learning objectives

By the end of this domain, you should be able to distinguish open source, open weight, source-available, and proprietary distribution; evaluate licenses; reason about precision, quantization, memory and inference constraints; understand GGUF, portable runtimes and production serving; choose deployment hardware; benchmark quality, latency, throughput and cost; and design model-independent hybrid routing.

## Domain structure

01 Open Source vs Open Weight AI  
02 Model Licensing and Governance  
03 Model Formats and Quantization  
04 Local Inference Fundamentals  
05 llama.cpp and Portable Inference  
06 vLLM and Production Model Serving  
07 Hardware, Memory and Performance  
08 Local, Edge and Private Deployment  
09 Benchmarking Quality, Latency and Cost  
10 Hybrid Routing and Model Independence  
11 Open-Source and Local AI Capstone

## 1. Open does not have one meaning

Keep open-source software, open-weight models, source-available releases, research-only releases, commercially usable models, and proprietary hosted models separate.

A downloadable checkpoint does not automatically grant unrestricted commercial use, redistribution, modification, or deployment.

Architecture review must include license review.

## 2. Model access and control

Hosted inference typically looks like:

Application → provider API → provider infrastructure → model.

Self-hosting moves the inference boundary:

Application → your inference service → model weights → your infrastructure.

This can increase control, but transfers responsibility for capacity, patching, isolation, observability, availability, upgrades, and cost.

## 3. Model size is not enough

Local feasibility depends on total parameters, active parameters for sparse models, numeric precision, quantization, architecture, RAM/VRAM, memory bandwidth, KV cache, context length, concurrency, storage bandwidth, serving engine, target throughput, and quality loss from compression.

A model that can technically execute may still be operationally useless.

## 4. Memory hierarchy

Inference can use multiple storage tiers:

```text
Fastest / smallest
accelerator cache
      ↓
VRAM
      ↓
System RAM
      ↓
NVMe / local storage
      ↓
Remote storage
Slowest / largest
```

Architecture can trade capacity against latency by staging data across tiers.

> A model too large for one memory tier is not necessarily impossible to execute. Capacity, latency, throughput, power, and economic viability are separate questions.

## 5. Quantization

Quantization reduces numeric precision to reduce memory footprint and potentially improve inference efficiency.

```text
Higher precision
      ↓
Quantization
      ↓
Smaller representation
      ↓
Lower memory / possible speed improvement
      ↓
Possible quality degradation
```

The correct quantization is empirical. Measure task quality rather than file size alone.

## 6. Separate the layers

Do not confuse model architecture, model weights, file format, quantization, inference runtime, and serving API.

They are different architectural layers and can often evolve independently.

## 7. Portable local inference

Lightweight runtimes make experimentation possible across laptops, desktops, servers, and CPU/GPU combinations.

They can be excellent for learning, offline use, privacy-sensitive workflows, prototyping, and selected production workloads.

A runtime optimized for one-user local inference is not automatically the correct engine for high-concurrency production serving.

## 8. Production serving

Production inference introduces request queueing, batching, KV-cache management, memory allocation, parallelism, model loading, health checks, admission control, metrics, tenant isolation, rate limits, rollout, and rollback.

Serving architecture must match workload shape.

## 9. Privacy

Self-hosting can reduce exposure to external providers, but privacy is end-to-end.

Data may still leak through application logs, prompt traces, vector stores, telemetry, backups, shared infrastructure, misconfigured endpoints, administrators, or tool integrations.

## 10. Security

A local model server is privileged infrastructure. Protect it with identity, authorization, network isolation, resource limits, tenant controls, monitoring, and safe tool boundaries.

Local deployment does not remove prompt-injection or unsafe-agent risks.

## 11. Edge AI

Edge inference can reduce network dependence and keep data near its source.

Constraints include compute, memory, power, thermals, model size, updates, and device heterogeneity.

Use edge inference when those trade-offs create measurable product value.

## 12. Economics

Compare total cost of hosted APIs, rented accelerators, owned hardware, and CPU/local inference.

Include utilization, idle capacity, engineering, electricity, cooling, storage, bandwidth, redundancy, maintenance, and upgrade cost.

Low utilization can make an apparently expensive API cheaper overall. High sustained utilization can change the equation.

## 13. Benchmarking

Measure task quality, time to first token, tokens per second, concurrent throughput, RAM, VRAM, storage activity, CPU/GPU utilization, power, context size, failures, cost per hour, and cost per successful task.

Benchmark the workload you actually intend to run.

## 14. Quality before size

A larger model is not automatically better for a specific system.

Evaluate quality, latency, reliability, cost, privacy, and operability. A smaller specialist model can be the better architectural component for a bounded task.

## 15. Hybrid architecture

```text
Application
     ↓
Model router
  ↙    ↓       ↘
Local  Private  Hosted
model  GPU      frontier API
```

Route by task sensitivity, capability, latency, availability, and economics.

## 16. Model independence

```text
Business workflow
      ↓
Canonical AI request
      ↓
Model router
      ↓
Runtime/provider adapter
      ↓
Local or hosted model
```

Do not spread model-specific assumptions throughout business code.

## 17. Evaluation before migration

Do not move workloads to local models because a benchmark or demo looks impressive.

Compare representative task success, structured-output reliability, tool use, error modes, latency, concurrency, context behaviour, operational burden, and cost per successful outcome.

## 18. Technology Radar

Classify technologies as IGNORE, WATCH, EXPERIMENT, ADOPT, or BUILD AROUND.

A technically impressive implementation can remain unsuitable for production. Separate the underlying architectural idea from the maturity of one project.

## 19. Architecture principles

1. License before deployment.
2. Measure quality before celebrating compression.
3. Execution feasibility is not production viability.
4. Privacy is end-to-end, not a property of model location.
5. Own infrastructure only when control or economics justify it.
6. Keep model choice replaceable where practical.
7. Benchmark cost per useful outcome, not merely tokens per second.
8. Use hybrid routing when workloads have different requirements.
9. Do not confuse open weights with an open system.
10. Operational responsibility grows as provider abstraction decreases.

## 20. Capstone direction

The capstone will design a model-independent inference platform routing workloads among local CPU inference, local/private GPU inference, open-weight models on rented infrastructure, and hosted frontier APIs.

It must include licensing, model registry, evaluation gates, quantization policy, hardware sizing, privacy classification, tenant isolation, serving, routing, fallback, observability, cost accounting, upgrade, and rollback.

## Takeaway

> Open-weight and local AI expand the architecture space. The goal is not to run the biggest downloadable model on the nearest machine; it is to choose the deployment boundary that delivers the required quality, privacy, latency, reliability, control, and economics.

Next: **01 — Open Source vs Open Weight AI**.

## Canonical curriculum navigation

- [Open Source vs Open Weight AI](./01-open-source-vs-open-weight-ai.md)
- [Model Licensing and Governance](./02-model-licensing-and-governance.md)
- [Model Formats and Quantization](./03-model-formats-and-quantization.md)
- [Local Inference Fundamentals](./04-local-inference-fundamentals.md)
- [llama.cpp and Portable Inference](./05-llama-cpp-and-portable-inference.md)
- [vLLM and Production Model Serving](./06-vllm-and-production-model-serving.md)
- [Hardware, Memory and Performance](./07-hardware-memory-and-performance.md)
- [Local, Edge and Private Deployment](./08-local-edge-and-private-deployment.md)
- [Benchmarking Quality, Latency and Cost](./09-benchmarking-quality-latency-and-cost.md)
- [Hybrid Routing and Model Independence](./10-hybrid-routing-and-model-independence.md)
- [Open-Source and Local AI Capstone](./11-open-source-local-ai-capstone.md)
