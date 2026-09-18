# 08 — Scalability

## Purpose

Scalability is the ability of a system to handle increasing workload without unacceptable degradation in latency, reliability, cost, or correctness. In AI systems, scaling is not only about web traffic: models, queues, databases, retrieval, external APIs, tenant workloads, and human-review capacity can each become the limiting resource.

## Core principle

> Scale the demonstrated bottleneck, not the architecture diagram.

Adding machines, services, workers, or GPUs does not automatically increase useful system capacity. The constraint may simply move somewhere else.

## 1. Define the workload first

Before choosing a scaling strategy, identify what is growing:

- requests per second;
- concurrent users;
- tenants;
- records/documents;
- marketplace events;
- queue jobs;
- tokens processed;
- model inference requests;
- retrieval queries;
- tool/API calls;
- background workflows;
- storage;
- human approvals.

Different workloads require different architectures.

## 2. Capacity is end-to-end

A system's useful throughput is constrained by its bottleneck.

```text
API
 ↓
Application
 ↓
Queue
 ↓
Workers
 ↓
Database
 ↓
External API
```

If the external API permits only a bounded request rate, adding 100 workers may only create rate-limit errors and a larger retry backlog.

## 3. Vertical scaling

Vertical scaling increases the resources of one machine or process:

```text
More CPU
More RAM
Faster storage
Larger GPU
```

Advantages:

- operational simplicity;
- fewer distributed-system problems;
- often effective early.

Limits:

- hardware ceilings;
- larger failure domain;
- cost curves;
- maintenance/restart impact.

Vertical scaling is not inherently inferior. It can be the correct engineering decision.

## 4. Horizontal scaling

Horizontal scaling adds more instances:

```text
Load balancer
   ├── App 1
   ├── App 2
   └── App 3
```

This works best when instances are stateless or when state is stored in shared/durable systems.

Horizontal scaling introduces coordination, consistency, observability, deployment, and cost complexity.

## 5. Stateless application services

Interactive application instances are easier to scale when durable state is externalised.

Avoid relying on one process's local memory for critical:

- sessions;
- workflow state;
- locks;
- idempotency records;
- job progress.

```text
App instances
      ↓
Shared durable state
```

Local caches can still be useful, but they must not become accidental sources of truth.

## 6. Queue and worker scaling

Queues decouple incoming workload from processing capacity.

```text
Producers
    ↓
 Queue
    ↓
Worker pool
```

Scale workers based on more than queue depth. Useful signals include:

- age of oldest job;
- arrival rate;
- completion rate;
- worker utilisation;
- retry rate;
- downstream rate limits;
- job cost/duration.

## 7. Backpressure

When incoming work exceeds safe processing capacity, the system must resist unlimited growth.

Possible mechanisms:

- bounded queues;
- rate limiting;
- admission control;
- tenant quotas;
- reduced concurrency;
- deferred low-priority work;
- load shedding.

```text
Demand > Safe capacity
          ↓
Backpressure
          ↓
Controlled degradation
```

Without backpressure, overload propagates through the system.

## 8. Database scaling

The database often becomes the real bottleneck after application servers scale.

Start with fundamentals:

- correct indexes;
- efficient queries;
- bounded result sets;
- connection management;
- query observability;
- archival/retention strategy.

Then consider, where justified:

- read replicas;
- caching;
- partitioning;
- workload separation;
- sharding.

Do not shard a database merely because the system is called “enterprise.” Sharding creates significant operational complexity.

## 9. Connection limits

Horizontal application scaling can accidentally exhaust databases and external services.

```text
10 app instances
×
50 DB connections
=
500 potential connections
```

Connection pools and concurrency limits must be considered as part of scaling design.

## 10. Partitioning

Large workloads can be partitioned by dimensions such as:

- tenant;
- region;
- time;
- resource identifier;
- workload class.

A good partition key distributes load while preserving useful locality.

Poor partitioning can create hot partitions.

## 11. Multi-tenant scaling

Multi-tenant platforms must protect tenants from one another.

A large tenant should not monopolise:

- queue workers;
- API quotas;
- database capacity;
- model budget;
- retrieval capacity.

Use controls such as:

```text
Tenant quotas
Priority classes
Concurrency limits
Rate limits
Fair scheduling
```

This is the noisy-neighbour problem.

## 12. External API limits

Marketplace, SaaS, model, and payment APIs impose their own capacity limits.

Your theoretical infrastructure capacity may be irrelevant if a provider allows less throughput.

Architect around:

- per-account quotas;
- per-tenant quotas;
- burst limits;
- retry-after signals;
- token budgets;
- concurrency caps.

Provider limits should be treated as explicit system constraints.

## 13. AI model scaling

AI workloads add unusual scaling dimensions:

- input tokens;
- output tokens;
- context size;
- model size;
- batching;
- inference concurrency;
- latency targets;
- GPU memory;
- provider rate limits;
- cost per request.

Two requests can consume radically different resources even if both count as one HTTP request.

## 14. Model routing as a scaling tool

Not every task needs the largest model.

```text
Task
 ↓
Complexity / risk classification
 ├── small model
 ├── standard model
 └── high-capability model
```

Routing can improve throughput and economics, provided quality is evaluated rather than assumed.

## 15. GPU/inference scaling

For self-hosted models, useful capacity depends on more than GPU count.

Consider:

- model memory footprint;
- quantisation;
- batching;
- tokens per second;
- KV-cache pressure;
- context length;
- interconnect/networking;
- loading time;
- redundancy.

Optimise for the real service objective: latency, throughput, quality, cost, or some combination.

## 16. Retrieval scaling

RAG systems may bottleneck in:

- embedding generation;
- vector search;
- metadata filtering;
- reranking;
- document storage;
- ingestion pipelines.

Measure each stage independently.

Scaling the vector database will not fix a slow reranker or overloaded embedding service.

## 17. Autoscaling

Autoscaling should respond to signals related to actual workload.

For synchronous services:

- CPU/memory;
- request concurrency;
- latency.

For workers:

- queue age;
- queue depth;
- arrival/completion rates;
- downstream capacity.

For AI inference:

- token throughput;
- active sequences;
- latency;
- accelerator utilisation.

Avoid scaling purely on a convenient metric that does not represent the bottleneck.

## 18. Cold starts and scale-up delay

Capacity does not always appear instantly.

Potential delays include:

- container startup;
- model loading;
- GPU provisioning;
- cache warming;
- connection establishment.

Capacity planning must account for how quickly the system can respond to a spike.

## 19. Load shedding

During overload, protecting critical operations may require rejecting or delaying less important work.

Example priority:

```text
1. Transactional operations
2. User-facing reads
3. Important synchronisation
4. AI recommendations
5. Bulk recomputation
6. Experimental/background jobs
```

The exact hierarchy is domain-specific.

A system that attempts to serve everything during overload can end up serving nothing reliably.

## 20. Cost-aware scalability

Scalability without economic control can create an architecture that technically works but is commercially unsustainable.

Measure:

```text
Cost per request
Cost per workflow
Cost per tenant
Cost per model task
Cost per successful business outcome
```

Scaling decisions should preserve acceptable unit economics.

## 21. Read vs write scaling

Read-heavy and write-heavy systems have different strategies.

Read-heavy workloads may benefit from:

- caching;
- replicas;
- materialised views;
- precomputation.

Write-heavy workloads may require:

- batching;
- partitioning;
- asynchronous processing;
- reduced contention;
- careful transaction design.

## 22. Event-driven scaling

Events can allow downstream capabilities to scale independently.

```text
Domain change
     ↓
Event
 ├── analytics consumer
 ├── search consumer
 ├── AI consumer
 └── notification consumer
```

But events do not remove capacity limits. Consumers still need idempotency, backpressure, observability, and failure handling.

## 23. Measure before redesign

Useful metrics include:

- p50/p95/p99 latency;
- throughput;
- saturation;
- queue age;
- error/retry rate;
- database query time;
- connection usage;
- external rate-limit events;
- tokens per second;
- cost per operation;
- per-tenant resource consumption.

Architecture decisions should follow evidence.

## 24. Capacity testing

Test beyond the expected average load.

Include:

- sustained load;
- bursts;
- large tenants;
- slow dependencies;
- retry storms;
- queue backlog recovery;
- database contention;
- model-provider throttling;
- mixed interactive/background traffic.

Determine where the system bends and where it breaks.

## 25. Generic application

A scalable AI platform architecture should separate workload classes while keeping capacity governed.

```text
Users / Webhooks / Schedulers
            ↓
        API / Intake
            ↓
     Durable queues/events
       ↙      ↓       ↘
Marketplace  AI     Analytics
 workers   workers   workers
       \      |       /
        Domain services
              ↓
       Authoritative data
```

Key principles include:

- tenant-aware workload identity;
- fair queue capacity;
- marketplace-specific rate limits;
- bounded AI concurrency;
- database protection;
- priority separation;
- observable backlog age;
- controlled retries;
- cost visibility.

Adding workers should occur only when downstream systems can safely absorb the additional throughput.

## 26. Enterprise checklist

Before scaling a component, answer:

1. What workload is growing?
2. What metric proves a capacity problem exists?
3. Where is the current bottleneck?
4. Is vertical scaling sufficient?
5. Can the component scale horizontally safely?
6. Where is durable state stored?
7. What downstream dependency becomes the next bottleneck?
8. Are database connections bounded?
9. Are external API limits represented?
10. Is backpressure implemented?
11. Are tenants isolated fairly?
12. What happens during a traffic spike?
13. What is the cost per unit of useful work?
14. How long does new capacity take to become available?
15. Can low-priority work be delayed or shed?
16. Has the architecture been load-tested under failure conditions?

## Takeaway

> Scalability is controlled growth of useful capacity—not simply adding infrastructure.

The strongest architecture measures the end-to-end workload, finds the actual constraint, protects downstream systems, preserves tenant fairness and reliability, and scales only where evidence shows additional capacity is valuable.
