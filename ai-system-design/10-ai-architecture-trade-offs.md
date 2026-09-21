# 10 — AI Architecture Trade-offs

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **10 — AI Architecture Trade-offs** within AI System Design;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Architecture is the discipline of choosing between competing qualities under real constraints. AI systems make these choices harder because they combine probabilistic models, deterministic software, external APIs, variable workloads, cost-sensitive inference, security boundaries, and human decision points.

The goal is not to find the universally “best” architecture. It is to choose the design whose trade-offs best match the system’s actual requirements.

## Core principle

> Architecture is not a collection of best practices. It is a set of explicit trade-offs made against measurable requirements.

## 1. Start with constraints, not patterns

Before choosing an architecture, define the system constraints:

- latency target;
- throughput;
- reliability;
- recovery requirements;
- consistency requirements;
- security sensitivity;
- tenant isolation;
- cost ceiling;
- team size and expertise;
- operational maturity;
- data residency;
- auditability;
- human approval requirements.

A technically elegant design can still be the wrong design if it violates the business constraints.

## 2. Simplicity vs flexibility

A simple architecture is easier to understand, test, deploy, and operate.

A flexible architecture can adapt to more use cases but usually adds abstraction and operational cost.

```text
Simple system
  → easier operation
  → faster delivery
  → fewer failure modes

Highly flexible system
  → more extension points
  → more configuration
  → more coordination
```

Build for demonstrated variation, not imagined future complexity.

## 3. Modular monolith vs microservices

A modular monolith can provide strong internal boundaries without distributed-system overhead.

Advantages:

- simpler transactions;
- easier local debugging;
- fewer network failure modes;
- simpler deployment;
- lower operational burden.

Microservices may be justified when there is a demonstrated need for:

- independent scaling;
- independent deployment;
- separate security boundaries;
- distinct ownership;
- different infrastructure requirements;
- clear failure isolation.

The trade-off is autonomy vs distributed complexity.

## 4. Synchronous vs asynchronous execution

Synchronous execution is easier for short interactive operations.

Asynchronous execution improves resilience and throughput for long-running or retryable work.

```text
Synchronous
  + immediate result
  + simpler interaction
  - caller waits
  - tighter coupling

Asynchronous
  + durable execution
  + retryability
  + burst absorption
  - state tracking required
  - eventual completion
```

Use both where appropriate.

## 5. Strong consistency vs eventual consistency

Strong consistency simplifies reasoning when users or systems must immediately observe the latest state.

Eventual consistency can improve availability and scalability where temporary divergence is acceptable.

The key question is not:

> Which model is more modern?

It is:

> How stale can this information safely be?

## 6. Availability vs correctness

Some degraded reads may remain useful during dependency failure.

Some writes should stop completely if correctness cannot be guaranteed.

Example:

```text
Dashboard recommendation
  → stale data may be acceptable if labelled

Irreversible financial action
  → stale or uncertain state may require rejection
```

The acceptable trade-off depends on the consequence of being wrong.

## 7. Latency vs quality

Larger models, deeper retrieval, reranking, multiple agents, and more validation can improve output quality but increase latency.

```text
More reasoning
+ more context
+ more validation
=
potentially higher quality
but
higher latency and cost
```

Interactive workflows may need strict latency budgets. Background workflows can afford deeper analysis.

## 8. Quality vs cost

The strongest available model is not automatically the correct default.

Use evaluations to determine whether smaller or cheaper models meet the required quality threshold.

```text
Low-risk classification
       ↓
smaller model

Complex/high-risk reasoning
       ↓
higher-capability model
```

The goal is not minimum model cost. It is minimum cost for the required outcome quality.

## 9. Model independence vs provider optimisation

A provider abstraction can reduce lock-in and support failover.

However, strict abstraction may hide valuable provider-specific capabilities.

Trade-off:

```text
Model independence
  + portability
  + negotiating leverage
  + fallback options
  - lowest-common-denominator risk

Provider optimisation
  + access to unique capabilities
  + potentially better performance
  - deeper lock-in
```

A practical architecture often abstracts core capabilities while allowing controlled provider-specific extensions.

## 10. Build vs buy

Do not build commodity infrastructure merely because it is technically interesting.

Buy or adopt managed capability when:

- differentiation is low;
- operational burden is high;
- the provider is trustworthy;
- switching risk is acceptable.

Build when the capability is strategically important because it contains:

- proprietary domain logic;
- unique data;
- critical workflow knowledge;
- control requirements;
- important economics.

The strongest moat is usually not generic infrastructure.

## 11. Managed AI vs self-hosted AI

Managed providers offer:

- rapid deployment;
- reduced infrastructure burden;
- elastic capacity;
- access to leading models.

Self-hosting may provide:

- stronger deployment control;
- predictable data boundaries;
- specialised model optimisation;
- potentially favourable economics at sustained scale.

But self-hosting introduces:

- GPU operations;
- serving infrastructure;
- model upgrades;
- capacity planning;
- security responsibility;
- reliability engineering.

The decision should be based on total cost and strategic requirements, not ideology.

## 12. RAG vs fine-tuning

RAG is useful when the system needs access to changing or attributable knowledge.

Fine-tuning is useful when the objective is to alter behaviour, style, task performance, or model specialisation.

They solve different problems and can be combined.

Do not fine-tune merely to make frequently changing business data available to a model.

## 13. Deterministic workflow vs autonomous agent

A deterministic workflow provides predictable control.

An autonomous agent provides adaptive reasoning where the correct path cannot be fully predefined.

```text
Deterministic workflow
  + predictable
  + easier to test
  + easier to audit

Agent
  + adaptable
  + handles ambiguity
  - less predictable
  - requires stronger controls
```

Use deterministic orchestration around probabilistic reasoning whenever possible.

## 14. Single agent vs multi-agent

Multi-agent systems can provide role separation and parallel reasoning, but they also introduce:

- coordination overhead;
- more model calls;
- harder debugging;
- emergent failure modes;
- higher cost.

Use multiple agents only when independent roles or parallelisation produce measurable benefit.

Do not treat agent count as a measure of system sophistication.

## 15. Central orchestration vs decentralised events

Central orchestration makes workflow state easier to see and control.

Event-driven choreography can reduce coupling between consumers.

Trade-off:

```text
Central workflow
  + explicit lifecycle
  + strong observability
  - orchestrator responsibility

Event choreography
  + loose coupling
  + independent consumers
  - harder global reasoning
  - emergent process flow
```

Critical business processes often benefit from explicit orchestration, while peripheral reactions can be event-driven.

## 16. Shared infrastructure vs isolation

Shared infrastructure improves utilisation and lowers cost.

Dedicated infrastructure improves isolation and predictability.

Dimensions include:

- shared vs tenant-specific database;
- shared vs dedicated queues;
- shared vs dedicated model quota;
- shared vs isolated workers.

Choose isolation based on security, performance, regulatory, and noisy-neighbour risk.

## 17. Caching vs freshness

Caching improves performance and cost but increases the risk of stale state.

The correct trade-off depends on data semantics.

```text
Static metadata
  → long cache may be safe

Inventory / price / financial state
  → freshness may dominate
```

Every cache is a consistency decision.

## 18. Retry aggressiveness vs system stability

Retries improve recovery from transient failures.

Too many retries can amplify an outage.

```text
Dependency slows
   ↓
Requests fail
   ↓
Aggressive retries
   ↓
More dependency pressure
   ↓
Worse failure
```

Use bounded retries, backoff, jitter, and circuit breakers.

## 19. Automation vs human control

More automation can improve speed and scale.

Human approval increases friction but may be necessary for consequential actions.

A useful framework is to classify actions by risk:

```text
Low risk
  → automatic

Medium risk
  → automatic with verification / rollback

High risk
  → human approval
```

Autonomy should increase only when reliability evidence supports it.

## 20. Observability depth vs operational cost

Collecting more telemetry improves diagnosis but adds:

- storage cost;
- ingestion cost;
- privacy considerations;
- signal-to-noise problems.

Instrument what supports concrete operational questions.

For AI systems, valuable observability may include:

- model/provider;
- prompt/version;
- retrieved context identifiers;
- tool calls;
- token usage;
- latency;
- cost;
- evaluation outcome;
- policy decision;
- workflow correlation ID.

## 21. Security vs convenience

Security controls often add friction.

But removing controls from high-impact AI workflows can create unacceptable risk.

Examples:

- broad tool permissions vs least privilege;
- long-lived credentials vs short-lived tokens;
- automatic execution vs approval;
- unrestricted context access vs scoped retrieval.

Good architecture minimises unnecessary friction without weakening required controls.

## 22. Generalisation vs domain specificity

Generic AI platforms are easier to reuse broadly.

Domain-specific systems can produce much stronger outcomes because they encode:

- terminology;
- workflows;
- constraints;
- policies;
- decision logic;
- evaluation criteria.

Do not abstract away the domain knowledge that creates actual product value.

## 23. Real-time vs batch processing

Real-time systems provide immediacy but require continuous capacity and stricter reliability.

Batch systems can be more efficient for workloads that do not need immediate results.

Examples:

```text
Order event
  → near real-time

Historical catalogue analysis
  → batch
```

Choose based on decision latency, not habit.

## 24. Precomputation vs on-demand computation

Precomputation reduces request latency but can waste compute on results nobody uses.

On-demand computation conserves compute but increases response latency.

A hybrid architecture can precompute high-value/common results and calculate uncommon results when needed.

## 25. Normalisation vs source fidelity

Normalising external data makes cross-system reasoning easier.

But excessive normalisation can lose provider-specific information.

A robust pattern is often:

```text
Raw source record
      ↓
Normalised domain model
```

Preserve enough source fidelity for audit, reconciliation, and provider-specific behaviour.

## 26. Fail-fast vs degrade

Some failures should terminate an operation immediately.

Others should fall back to degraded functionality.

Fail fast when continuing would produce invalid or unsafe state.

Degrade when reduced functionality still provides safe value.

## 27. Reversibility

Prefer architectural decisions that are easy to change when uncertainty is high.

Examples:

- provider adapters;
- modular boundaries;
- versioned schemas;
- feature flags;
- reversible deployments.

Irreversible decisions require stronger evidence.

## 28. Architecture decision records

Important trade-offs should be documented.

A lightweight ADR can capture:

```text
Context
Decision
Alternatives considered
Trade-offs
Consequences
Review trigger
```

This prevents teams from forgetting why an architectural choice was made.

## 29. Trade-off matrix

For important components, score relevant dimensions rather than discussing technology abstractly.

Example:

| Option | Latency | Reliability | Cost | Complexity | Control |
|---|---:|---:|---:|---:|---:|
| Managed model API | High | High | Medium | Low | Medium |
| Self-hosted model | Medium | Depends | Depends | High | High |

The scores are context-specific, not universal truths.

## 30. Generic commerce platform example

Consider an AI system that recommends and executes changes across external commerce platforms.

A balanced architecture may be:

```text
External events / users
        ↓
Application services
        ↓
Durable workflow
        ↓
AI reasoning
        ↓
Deterministic validation
        ↓
Policy + permissions
        ↓
Human approval where required
        ↓
Idempotent execution
        ↓
External platform
        ↓
Verification / reconciliation
```

The architecture intentionally trades maximum autonomy for stronger control, traceability, and business safety.

As evidence improves, selected low-risk workflows can move toward greater automation.

## 31. Architect’s decision checklist

For every significant architectural choice, ask:

1. What requirement are we optimising for?
2. What constraint makes this decision necessary?
3. What do we gain?
4. What do we give up?
5. What new failure modes are introduced?
6. What becomes harder to operate?
7. What happens at 10× workload?
8. What happens when the dependency fails?
9. What is the cost impact?
10. What security boundary changes?
11. How reversible is the decision?
12. What evidence would cause us to revisit it?
13. Can a simpler architecture satisfy the requirement?

## Takeaway

> Mature architecture is the ability to make explicit, evidence-based compromises—not the ability to use the most advanced technology available.

A strong AI systems architect understands that latency, quality, autonomy, reliability, security, cost, simplicity, scalability, and control pull in different directions. The job is to choose the balance that best serves the real system and to document why.
