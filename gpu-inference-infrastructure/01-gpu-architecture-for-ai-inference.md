# 01 — GPU Architecture for AI Inference

## Purpose

Accelerator specifications are ingredients; workload performance is the result. This chapter builds the hardware/software mental model needed to reason about inference without reducing the decision to peak FLOPS or VRAM capacity.

## Learning outcomes

By the end of this module, you should be able to:
- explain the GPU execution and memory hierarchy at an inference-architecture level
- distinguish compute-, bandwidth-, capacity-, communication- and scheduler-bound workloads
- explain why precision, kernels, runtime software and topology change observed performance
- design a benchmark that reflects a real workload rather than a vendor headline

## Why GPUs change inference economics

GPUs provide large amounts of parallel arithmetic and high-bandwidth device memory. Transformer inference maps well to matrix operations, but end-to-end performance also depends on memory movement, kernel efficiency, sequence shape, batching and communication.

## Execution model

A useful abstraction is `host orchestration -> kernel launch -> GPU compute/memory -> result`. Warps/threads, tensor/matrix units, caches and HBM all contribute. Architects do not need to hand-write CUDA kernels, but they need to understand which resource a serving workload is exhausting.

## Compute vs memory bandwidth

Prefill can expose substantial matrix-compute demand while autoregressive decode can become dominated by repeatedly reading model weights and KV state. The bottleneck can change with model architecture, batch size and sequence length.

## Precision and kernels

FP32, FP16/BF16, FP8 and lower-bit quantized representations trade numerical behaviour, memory footprint and hardware support. A lower-precision format is valuable only if the model quality and runtime kernels support the intended workload.

## Host, PCIe and interconnect

CPU orchestration, host RAM, PCIe and GPU-to-GPU links can become limiting when models are sharded, data is frequently moved, or preprocessing is heavy. Several accelerators do not behave like one larger accelerator unless communication costs are acceptable.

## Software stack

Driver, CUDA/runtime, framework, compiler, kernel library, inference server and model artifact form one deployed system. Benchmark and version the stack as a unit.

## Failure modes

- selecting hardware from peak FLOPS without measuring the workload
- assuming a model that fits in VRAM will meet latency or throughput targets
- host/device or GPU/GPU transfer becoming the hidden bottleneck
- runtime or driver changes causing performance or compatibility regressions
- thermal, power or memory pressure causing degraded or unstable service

## Security and governance

GPU infrastructure should not hold broad business credentials. Keep tenant identity, authorization and consequential policy above the serving layer. Restrict administrative access, isolate workloads where required, and treat drivers, kernels and serving images as supply-chain dependencies.

## Economics and operations

Measure cost per successful task, not cost per GPU-hour alone. Include utilization, idle time, power, reserved capacity, engineering effort and quality regressions. High theoretical performance has little value if the deployed workload cannot use it.

## Practical exercise

Choose two accelerators or accelerator classes for the same representative LLM workload. Define prompt/output lengths, concurrency and SLOs; predict the likely bottleneck on each; then define measurements that would falsify your prediction.

## Architect checklist

- [ ] workload shape is documented before hardware choice
- [ ] capacity, bandwidth, compute and communication are evaluated separately
- [ ] software versions and topology are part of the benchmark identity
- [ ] normal, peak and degraded-capacity tests exist
- [ ] cost and quality are tied to successful outcomes

## Primary reading

- [NVIDIA CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/)
- [NVIDIA CUDA C++ Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)
- [MLPerf Inference documentation](https://docs.mlcommons.org/inference/index_gh/)

## Mastery gate

Explain when **GPU Architecture for AI Inference** changes the architecture materially, identify the evidence you would collect before making the decision, and state which controls remain outside the inference runtime.

## Takeaway

> Treat the accelerator as one component in a measured serving system, not as a performance guarantee.

Next: **02 — VRAM, Memory Bandwidth and Model Sizing**.
