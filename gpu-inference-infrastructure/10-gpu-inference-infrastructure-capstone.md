# 10 — GPU and Inference Infrastructure Capstone

## Objective

Design a model-independent inference platform that serves interactive, long-context, specialist and asynchronous workloads across hosted APIs, rented accelerators and private/owned infrastructure.

## Required evidence

Your design must include measurable workload assumptions rather than generic statements.

Document:

- model and quality requirements;
- prompt/output/context distributions;
- concurrency and arrival patterns;
- TTFT, inter-token latency and throughput SLOs;
- availability and recovery objectives;
- privacy/residency constraints;
- expected demand growth.

## Architecture

Produce a diagram covering:

```text
Clients / Workflows
        |
Identity + Quotas
        |
Model / Capability Router
        |
Admission Control
        |
Queues / Scheduler
        |
+-------------------------------+
| Hosted API | Rented | Private |
+-------------------------------+
        |
Streaming / Results
        |
Evaluation + Telemetry + Cost
```

Business authorization and irreversible action policy must remain above the inference layer.

## Capacity model

Show:

- weight/runtime memory;
- KV/context assumptions;
- concurrency;
- headroom;
- normal capacity;
- peak capacity;
- one-serving-unit failure;
- deployment overlap.

Explain which assumptions are estimates and how they will be measured.

## Scheduling and tenancy

Define workload classes, priorities, queue bounds, rate/concurrency limits, cancellation and fairness.

Demonstrate how background demand cannot destroy interactive SLOs.

## Multi-GPU decision

If the design uses tensor, pipeline or expert parallelism, justify it against simpler alternatives such as quantization, smaller models, replicas or routing.

Include topology and failure implications.

## Cloud vs owned economics

Build a lifecycle TCO comparison including utilization, power/facilities, engineering, spares, storage/network, downtime risk and hardware refresh.

Use **cost per successful outcome** as the final comparison metric.

## Reliability

Create a failure matrix for:

- GPU/node loss;
- OOM;
- scheduler failure;
- artifact/model-load failure;
- network/storage failure;
- provider capacity loss;
- degraded model/runtime rollout.

For each define detection, containment, fallback and recovery.

## Observability

Specify:

- model/artifact/runtime/hardware identity;
- queue depth/time;
- TTFT;
- prefill/decode throughput;
- active sequences/batches;
- KV and VRAM occupancy;
- errors/OOM;
- route/fallback;
- cost attribution;
- evaluated outcome.

## Evaluation

Benchmark the exact deployed combination rather than a generic GPU.

Run:

1. normal interactive load;
2. long-context load;
3. peak/burst load;
4. background/batch load;
5. degraded-capacity load;
6. rollout/canary comparison.

Record quality as well as speed.

## Architecture decision records

Write at least three ADRs:

1. serving/runtime choice;
2. cloud/rented/owned capacity strategy;
3. model-routing and fallback policy.

A fourth ADR for multi-GPU topology is required if sharding is used.

## Security and governance

Show tenant isolation, administrative access, secret handling, supply-chain controls, data-residency constraints and logging policy.

## Primary reading

- [NVIDIA CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/)
- [vLLM documentation](https://docs.vllm.ai/en/stable/)
- [PagedAttention / vLLM paper](https://arxiv.org/abs/2309.06180)
- [PyTorch Tensor Parallel documentation](https://docs.pytorch.org/docs/stable/distributed.tensor.parallel)
- [NVIDIA TensorRT-LLM documentation](https://docs.nvidia.com/tensorrt-llm/)
- [MLPerf Inference documentation](https://docs.mlcommons.org/inference/index_gh/)

## Mastery gate

The capstone passes only if another architect can reproduce the assumptions, challenge the bottlenecks, see how the platform fails, understand why each infrastructure choice exists, and replace one model/runtime/provider without rewriting business logic.

## Takeaway

> The production unit is not a GPU or a model. It is a measured inference service that turns compute into reliable outcomes at acceptable cost.

Next: **Domain 17 — MLOps and LLMOps**.
