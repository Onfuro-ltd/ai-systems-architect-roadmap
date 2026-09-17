# 11 — Open-Source and Local AI Capstone

## Purpose

Design a model-independent inference platform that can use local CPU inference, private accelerated serving, rented open-weight infrastructure, and hosted frontier APIs without coupling business workflows to one provider.

> Own the inference boundary where it creates measurable value; preserve the ability to move it when requirements change.

## Scenario

A multitenant platform supports interactive assistance, background extraction/classification, retrieval-grounded reasoning, privacy-sensitive workloads, and high-capability reasoning. Restricted workloads must remain inside approved infrastructure.

## Required architecture

```text
Business workflows / agents
          ↓
Canonical AI capability interface
          ↓
Policy + privacy + governance
          ↓
Model router
   ┌──────┼─────────┬──────────┐
   ↓      ↓         ↓          ↓
Local   Private   Rented     Hosted
CPU     GPU       open       frontier
   └──────┴─────────┴──────────┘
          ↓
Validation + evaluation
          ↓
Observable business outcome
```

## Deliverables

Create a workload catalogue with quality, latency, throughput, context, privacy, availability, and budget requirements.

Create a model registry containing revision, artifact hash, architecture, parameter/quantization information, runtime, license lineage, approval state, evaluation result, hardware target, and retirement state.

Define governance from discovery through experiment, production approval, restriction, upgrade, and retirement.

Design the artifact pipeline: approved source → verified artifact → conversion/quantization → integrity check → evaluation → registry → deployment.

Design local CPU, private GPU, rented open-weight GPU, and hosted API serving tiers. Explain which workload belongs on each.

Size hardware using weight memory, KV cache, runtime overhead, context distribution, concurrency, bandwidth, utilization, storage, power, and redundancy. Separate "can execute" from "meets SLO."

Define portable and production serving adapters so workflows do not depend directly on runtime implementation.

Design routing where policy/privacy eligibility precedes capability, latency, and cost optimization. Restricted data must never fall back to a disallowed route.

Define safe fallback/degradation, including queueing, human handling, or rejection when no compliant route exists.

Build a representative evaluation suite and benchmark matrix covering quality, schema/tool reliability, context behaviour, cold/warm TTFT, decode/throughput, memory, utilization, failures, and cost per successful task.

Map privacy across prompts, retrieval, logs, telemetry, caches, backups, servers, tools, and administrators. Enforce authentication, authorization, tenant isolation, network controls, artifact integrity, secrets, quotas, and audit.

Design model rollout with immutable versions, shadow/canary where safe, acceptance gates, health checks, and rollback. Treat routing-policy changes as production changes.

Build a failure matrix for load failure, OOM, overload, accelerator failure, corrupt artifact, provider/network outage, context overflow, quality regression, governance withdrawal, and unavailable compliant fallback.

Observability must record workload class, privacy class, eligible routes, selected model/tier, routing reason/version, artifact/runtime version, queue/TTFT/total latency, utilization, tokens, cost, validation, fallback, and evaluated outcome.

Compare API, rental, and owned infrastructure using realistic utilization, engineering, power, redundancy, and lifecycle costs.

Produce at least three ADRs covering major deployment/routing choices.

## Acceptance review

Challenge whether self-hosting solves a real requirement, license rights are known, every quantization passed evaluation, hardware calculations include context/KV cache, privacy is end-to-end, servers are protected, fallbacks are compliant and load-tested, business logic is runtime-independent, economics use realistic utilization, quality clears representative tasks, and rollbacks are proven.

## Final principle

> The winning deployment is not the most open, largest, or fastest in isolation. It is the compliant architecture that achieves the required outcome with the best sustainable balance of quality, control, latency, reliability, and cost.

**Domain 14 — Open-Source and Local AI complete.**

Next domain: **15 — Fine-Tuning and Specialist Models**.
