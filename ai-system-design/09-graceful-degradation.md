# 09 — Graceful Degradation

## Purpose

Graceful degradation is the ability of a system to continue providing safe, useful service when part of the architecture is slow, unavailable, or operating below normal capacity.

The goal is not to hide failure. The goal is to reduce capability deliberately while preserving critical functions and preventing unsafe behaviour.

## Core principle

> When a dependency degrades, reduce capability intentionally instead of allowing the whole system to fail unpredictably.

## 1. Systems are rarely only "up" or "down"

Real systems often operate in intermediate conditions:

- a model provider is slow;
- one marketplace API is unavailable;
- search is degraded;
- a queue has a backlog;
- analytics is stale;
- one database replica is unhealthy;
- a recommendation service is unavailable;
- a human-approval team is overloaded.

Architecture should define what the product does in each condition.

## 2. Critical vs optional capabilities

Not every feature deserves the same availability target.

Classify capabilities, for example:

```text
Critical
- authentication
- transactional state
- permissions
- core order/inventory operations

Important
- synchronisation
- reporting
- notifications

Optional / degradable
- AI explanations
- recommendations
- advanced analytics
- background enrichment
```

The exact classification is domain-specific.

## 3. Degradation hierarchy

A useful strategy is to define progressive service levels.

```text
FULL SERVICE
     ↓
REDUCED AI CAPABILITY
     ↓
READ-ONLY / STALE-SAFE MODE
     ↓
CRITICAL OPERATIONS ONLY
     ↓
SAFE REJECTION
```

A system can move down this hierarchy as dependencies fail or capacity becomes constrained.

## 4. Fail open vs fail closed

Every control should define whether failure permits or blocks the action.

Examples:

- recommendation generation may fail open to a manual workflow;
- permission validation should usually fail closed;
- payment or irreversible execution should fail closed when required controls are unavailable;
- optional analytics may fail open with a visible degraded-state warning.

The choice must be based on risk, not convenience.

## 5. AI should often be optional to core transactions

A strong AI-native system should not necessarily make every fundamental business operation dependent on a model being online.

Prefer:

```text
Deterministic core operation
        ↓
AI enhancement where available
```

rather than:

```text
Core business operation
        ↓
Mandatory AI call
        ↓
Provider outage blocks everything
```

AI can be deeply integrated without becoming an unnecessary single point of failure.

## 6. Model fallback

If a primary model is unavailable, options may include:

- another evaluated model;
- a smaller model;
- a rules-based fallback;
- a cached safe response;
- a deferred workflow;
- human review.

Fallback quality must be known.

```text
Primary model unavailable
        ↓
Evaluated fallback available?
   ├── yes → use with appropriate policy
   └── no  → degrade safely
```

Do not silently route high-risk work to an unvalidated fallback.

## 7. Feature flags and kill switches

Degradable features should be independently controllable.

Examples:

```text
Disable AI recommendations
Disable bulk enrichment
Pause one external integration
Force read-only mode
Disable autonomous execution
```

A kill switch is particularly valuable for consequential AI actions.

## 8. Read-only mode

When safe writes cannot be guaranteed, the system may preserve read access.

```text
Writes unsafe/unavailable
        ↓
READ-ONLY MODE
        ↓
Users retain visibility
```

Read-only mode should be explicit in both backend policy and user interface.

## 9. Stale data with disclosure

Some workflows can safely serve slightly stale information.

```text
Authoritative source unavailable
        ↓
Recent cached snapshot
        ↓
Visible freshness timestamp
```

This is useful only where staleness is acceptable.

Never present stale data as current when freshness affects a financial, operational, or safety-critical decision.

## 10. Queue degradation

If worker capacity falls below incoming demand:

- preserve high-priority jobs;
- delay low-priority jobs;
- stop creating non-essential work;
- apply tenant fairness;
- expose backlog age;
- shed disposable work if required.

```text
Overload
   ↓
Prioritise
   ↓
Defer
   ↓
Shed optional work
```

This is preferable to allowing an unlimited backlog to destabilise the platform.

## 11. External integration degradation

An unavailable third-party API should usually affect only the capability that depends on it.

Example:

```text
Marketplace A unavailable
      ↓
Pause A-specific writes
      ↓
Queue safe retries
      ↓
Keep Marketplace B and C operational
```

This requires good service and failure boundaries.

## 12. Database degradation

Possible strategies include:

- failover to a healthy replica where architecture permits;
- read-only operation;
- disable expensive reporting queries;
- shed background work;
- preserve transactional capacity.

Do not allow optional analytics workloads to consume capacity needed by critical transactions during database pressure.

## 13. Search and retrieval degradation

If advanced retrieval fails, the system may fall back to:

- simpler keyword search;
- smaller retrieval scope;
- cached results;
- no-AI search results;
- manual navigation.

For RAG systems, missing retrieval should not result in an AI model confidently inventing the missing context.

```text
Retrieval unavailable
       ↓
No grounded context
       ↓
Do not fabricate grounded answer
```

## 14. Analytics degradation

Analytics and reporting are often good candidates for degradation before transactional systems.

Options include:

- pause expensive recomputation;
- serve last-known results with timestamps;
- reduce dashboard refresh frequency;
- disable non-critical drill-downs.

## 15. Human-in-the-loop degradation

Human review itself can become a bottleneck.

If an approval queue becomes overloaded:

- prioritise high-risk cases;
- defer low-value automation;
- reduce autonomous proposal volume;
- tighten thresholds so fewer ambiguous cases enter review.

Human capacity should be treated as a finite system resource.

## 16. Progressive quality degradation

AI systems can sometimes reduce quality before reducing availability.

Example:

```text
High-capability model
       ↓ capacity pressure
Standard model
       ↓
Template/rules fallback
       ↓
Deferred processing
```

This is appropriate only where the quality reduction remains acceptable for the task.

## 17. Cost-triggered degradation

Degradation can also be economic rather than technical.

For example, when model spend exceeds a defined budget:

```text
Budget threshold reached
        ↓
Route low-risk work to cheaper model
        ↓
Defer non-critical generation
        ↓
Preserve high-value workflows
```

Cost control can be part of reliability architecture.

## 18. Degradation must be visible

Operators need to know which mode the system is in.

Useful signals include:

- dependency health;
- active degradation level;
- disabled capabilities;
- queue backlog age;
- data freshness;
- fallback model usage;
- rejected/deferred operations.

Users may also need clear messaging when results are stale or a capability is temporarily unavailable.

## 19. Do not create hidden semantic changes

A dangerous degradation is one that silently changes meaning.

Example:

```text
Normal mode:
"live inventory"

Degraded mode:
"24-hour-old cached inventory"
```

If the interface presents both as identical, users may make incorrect decisions.

Degradation should preserve semantic honesty.

## 20. Recovery from degraded mode

Recovery should be controlled.

Avoid immediately releasing all deferred work after a dependency recovers.

```text
Dependency recovers
      ↓
Health confirmation
      ↓
Gradual concurrency increase
      ↓
Backlog drain
      ↓
Normal service
```

This helps prevent recovery storms.

## 21. Degradation state machine

Service condition itself can be modelled explicitly.

```text
HEALTHY
   ↓
DEGRADED
   ↓
SEVERELY_DEGRADED
   ↓
RECOVERING
   ↓
HEALTHY
```

Transitions may be driven by measurable thresholds rather than manual intuition alone.

## 22. Generic multichannel commerce example

Consider a platform that manages multiple sales channels and uses AI for recommendations.

```text
Users / APIs / Webhooks
          ↓
Core transactional services
          ↓
Queues and integrations
          ↓
AI / analytics / enrichment
```

If the AI provider fails:

```text
Core orders and inventory continue
AI recommendations pause
Existing deterministic rules remain available
Pending AI work is deferred
High-risk actions remain blocked without required validation
```

If one sales-channel API fails:

```text
That channel enters degraded sync mode
Other channels remain operational
Safe retries are queued
Freshness is exposed
Writes requiring uncertain external state are blocked
```

The architecture degrades by capability rather than collapsing globally.

## 23. Testing degradation paths

Degraded modes must be tested before incidents.

Test:

- model provider outage;
- partial external API outage;
- queue saturation;
- database pressure;
- cache loss;
- retrieval failure;
- analytics overload;
- human-review backlog;
- fallback provider failure;
- recovery after extended outage.

A fallback path that has never been exercised is only a theory.

## 24. Enterprise checklist

For every major capability, answer:

1. Is it critical, important, or optional?
2. Which dependencies does it require?
3. What happens if each dependency is unavailable?
4. Should the function fail open or fail closed?
5. Is there a validated fallback?
6. Can the feature be disabled independently?
7. Is read-only mode possible?
8. Is stale data acceptable, and for how long?
9. Is freshness visible to users/operators?
10. What work is delayed first under overload?
11. What work is shed entirely?
12. Can one tenant or integration cause global degradation?
13. Can an AI failure block deterministic core operations unnecessarily?
14. Is degradation state observable?
15. How does the system recover without causing a retry/backlog storm?
16. Have degradation paths been load- and failure-tested?

## Takeaway

> Graceful degradation is controlled loss of capability, not uncontrolled loss of reliability.

A strong AI system preserves critical business functions, blocks unsafe actions, exposes reduced confidence or freshness honestly, and recovers gradually rather than treating every partial failure as a total outage.
