# 05 — Fault Tolerance

## Purpose

Fault tolerance is the ability of a system to continue providing safe, useful service when components fail. In AI systems, failures can occur in models, providers, retrieval systems, queues, workers, databases, networks, tools, and external business APIs.

## Core principle

> Design for failure as a normal operating condition, while preventing failures from becoming unsafe business actions.

## 1. Failure domains

Identify failures by dependency:

```text
Application
Model provider
Database
Cache
Queue
Worker
External API
Network
Storage
Identity provider
```

Each dependency should have an explicit failure behaviour.

## 2. Failure modes

Common failure modes include:

- timeout;
- connection failure;
- rate limiting;
- authentication failure;
- malformed response;
- partial response;
- stale data;
- capacity exhaustion;
- dependency outage;
- corrupted or inconsistent state.

AI systems also face:

- invalid structured output;
- hallucinated tool arguments;
- low-confidence results;
- model refusal;
- context retrieval failure;
- unexpected agent loops.

## 3. Timeouts

Every remote dependency should have bounded timeouts.

```text
Request
  ↓
Timeout budget
  ↓
Dependency
  ↓
Success / controlled failure
```

A missing timeout can turn a dependency problem into thread, worker, or connection exhaustion.

## 4. Retries

Retries are appropriate for transient failures, not all failures.

Use:

- bounded attempts;
- exponential backoff;
- jitter;
- retry classification.

Avoid retrying:

- invalid credentials;
- invalid requests;
- permanent validation errors;
- unsafe operations without idempotency.

## 5. Circuit breakers

A circuit breaker can prevent repeated calls to an unhealthy dependency.

```text
CLOSED
  ↓ repeated failures
OPEN
  ↓ recovery window
HALF-OPEN
  ↓ successful probe
CLOSED
```

This protects both the application and the failing dependency.

## 6. Bulkheads

Separate workloads so one failure does not consume all resources.

Example:

```text
Interactive traffic
        ↓ isolated capacity

Background AI jobs
        ↓ isolated capacity

Marketplace synchronisation
        ↓ isolated capacity
```

Tenant or priority isolation may also be required.

## 7. Graceful failure

When a dependency fails, the system should choose a defined degraded behaviour.

Examples:

- return cached information;
- queue work for later;
- provide a partial result;
- disable one optional feature;
- require human review;
- safely reject the action.

Never silently invent a successful result because a dependency failed.

## 8. AI provider failure

Do not assume one model provider is always available.

Possible strategies:

```text
Primary model
     ↓ failure
Fallback model
     ↓ failure
Safe non-AI path / queue / human review
```

Fallbacks must be evaluated for capability and safety before production use.

## 9. Model failure vs infrastructure failure

A model returning a low-quality answer is different from the model service being unavailable.

Infrastructure failure:

```text
No response → retry / fallback
```

Quality failure:

```text
Response received
      ↓
Evaluation fails
      ↓
Reject / regenerate / escalate
```

Do not treat successful HTTP responses as successful AI outcomes.

## 10. Partial failure

Distributed workflows often partially succeed.

```text
Step A ✓
Step B ✓
Step C ✗
Step D not started
```

The system should preserve the completed state and provide a safe recovery path rather than pretending the whole transaction failed or succeeded atomically.

## 11. Dependency degradation

External systems may be slow before they become unavailable.

Architect for:

- latency thresholds;
- queue growth;
- backpressure;
- stale-data indicators;
- reduced concurrency.

A slow dependency can be more dangerous than a hard outage because it consumes resources gradually.

## 12. Data consistency

AI systems can amplify stale or inconsistent data.

Use:

- freshness metadata;
- version identifiers;
- transaction boundaries;
- validation;
- reconciliation jobs.

An AI recommendation should know whether the underlying data is current enough for the decision.

## 13. Recovery

Fault tolerance requires recovery, not just detection.

Define:

- restart strategy;
- checkpoint recovery;
- replay rules;
- compensation;
- operator intervention;
- recovery time objective (RTO);
- recovery point objective (RPO) where applicable.

## 14. Chaos and failure testing

Test realistic failures deliberately:

- provider timeout;
- provider 5xx;
- rate limit;
- queue outage;
- worker crash;
- database connection exhaustion;
- stale credentials;
- partial marketplace response;
- malformed model output.

A system is not fault tolerant merely because its happy path works.

## 15. Safety boundary

The most important rule for AI failures:

```text
Dependency failure
       ↓
Controlled failure
       ↓
NOT
       ↓
Unvalidated business action
```

If confidence, validation, permissions, or required data are unavailable, high-impact execution should stop or escalate.

## 16. SEMLIS application

For SEMLIS, critical dependency failures may include:

- Amazon/eBay/Shopify API outage;
- expired marketplace credentials;
- Redis/queue failure;
- database pressure;
- AI provider outage;
- malformed AI output.

A resilient workflow might be:

```text
Marketplace request
      ↓
Timeout
      ↓
Bounded retry
      ↓
Circuit breaker if dependency remains unhealthy
      ↓
Queue / delayed retry
      ↓
Resume from checkpoint
```

For an AI-generated marketplace action:

```text
AI output
   ↓
Validation
   ↓
Policy
   ↓
Permission
   ↓
Execution
```

If any critical control is unavailable, the action should not be silently executed.

## 17. Enterprise checklist

For every critical dependency, document:

1. What can fail?
2. What is the timeout?
3. Which errors are retryable?
4. What is the retry limit?
5. Is the operation idempotent?
6. Is there a circuit breaker?
7. What is the degraded mode?
8. Is capacity isolated?
9. How is recovery performed?
10. What happens to partial work?
11. How is the failure observed and alerted?
12. Can an AI failure result in an unsafe business action?

## Takeaway

> Fault-tolerant AI systems do not assume components will remain healthy; they define what happens when they do not.

The highest standard is not “the system never fails.” It is **the system fails predictably, contains the impact, recovers safely, and never converts uncertainty into uncontrolled action.**
