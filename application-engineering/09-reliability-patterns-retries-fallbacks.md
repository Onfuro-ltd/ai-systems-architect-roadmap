# Reliability Patterns: Retries, Fallbacks and Failure Recovery

## Why reliability is different in AI applications

Traditional software usually fails in predictable ways:

- an API returns an error;
- a database connection fails;
- a service times out;
- a dependency becomes unavailable.

AI applications introduce additional failure categories:

- the model returns a plausible but incorrect answer;
- the model follows instructions incorrectly;
- a tool is selected incorrectly;
- context is incomplete or stale;
- output quality changes after a model update;
- latency and cost vary depending on task complexity.

A reliable AI system does not assume the model is always correct. It designs for uncertainty.

## Core principle

> Reliability comes from engineering boundaries around intelligence, not from expecting intelligence to be perfect.

A production AI workflow should be designed like:

```
Request
  |
  v
Context preparation
  |
  v
Model execution
  |
  v
Validation
  |
  v
Recovery / fallback logic
  |
  v
Business action
  |
  v
Monitoring and learning
```

## Failure taxonomy

Before designing recovery, identify the type of failure.

## 1. Infrastructure failures

Examples:

- provider outage;
- network failure;
- timeout;
- rate limit;
- unavailable dependency.

These are similar to traditional software failures.

Controls:

- retries;
- timeouts;
- circuit breakers;
- fallback providers;
- queues.

## 2. Model failures

Examples:

- hallucination;
- incorrect reasoning;
- poor instruction following;
- inconsistent output.

Controls:

- structured outputs;
- validation;
- retrieval grounding;
- evaluation suites;
- human review for high-risk cases.

## 3. Tool failures

Examples:

- API rejects request;
- tool returns incomplete data;
- permissions fail;
- external system changes.

Controls:

- explicit tool schemas;
- error-aware tool responses;
- retry policies;
- idempotent operations;
- audit trails.

## Retry design

Retries are useful, but blindly retrying AI calls can increase cost and make failures worse.

A good retry strategy defines:

- which failures are retryable;
- maximum attempts;
- delay strategy;
- cost limits;
- alternative action after failure.

Example:

```
Temporary API timeout
        |
        v
Retry with backoff
        |
        v
Still failing?
        |
        v
Fallback model or queue for later
```

## Exponential backoff

Common pattern:

```
Attempt 1: wait 1 second
Attempt 2: wait 2 seconds
Attempt 3: wait 4 seconds
```

This reduces pressure on failing services.

## Idempotency

Critical for AI systems that can repeat actions.

An operation is idempotent when repeating it does not create unintended duplicate effects.

Bad:

```
Agent retries
        |
        v
Create second customer refund
```

Better:

```
Agent retries
        |
        v
Same request identifier detected
        |
        v
Existing action returned
```

## Model fallback strategies

Fallback does not simply mean:

"Use another model."

A good fallback considers:

- capability;
- cost;
- latency;
- privacy;
- context compatibility.

Example:

```
Complex analysis
       |
       v
Frontier model

Simple classification
       |
       v
Efficient model

Private information
       |
       v
Approved local model
```

## Graceful degradation

A reliable system should have useful behaviour when AI is unavailable.

Example:

Customer support:

Level 1:
AI resolves automatically

Level 2:
AI drafts response for human review

Level 3:
Traditional support workflow continues

The goal is not zero failures. The goal is controlled failure.

## Circuit breakers

A circuit breaker prevents repeated failures from damaging the system.

Pattern:

```
Healthy
  |
  v
Failures detected
  |
  v
Open circuit
  |
  v
Stop sending requests temporarily
  |
  v
Test recovery
```

Useful for:

- AI providers;
- external APIs;
- tool integrations;
- databases.

## Agent loop protection

Later agent systems require additional controls:

- maximum iterations;
- maximum cost;
- time limits;
- tool permission limits;
- progress checks;
- human escalation.

A system that can continue indefinitely is not autonomous. It is uncontrolled.

## Observability requirements

Every AI request should record:

- input category;
- context provided;
- model selected;
- tools called;
- retries performed;
- latency;
- cost;
- validation result;
- final outcome.

Without traces, improvement becomes guesswork.

## Architecture pattern

```
                 AI REQUEST
                      |
                      v
              Reliability Layer
                      |
       +--------------+--------------+
       |              |              |
       v              v              v
   Retry Logic   Fallbacks    Circuit Breaker
       |              |              |
       +--------------+--------------+
                      |
                      v
                Validation
                      |
                      v
                  Action
```

## Common mistakes

### Mistake 1: Retry everything

Some failures are logical, not temporary.

### Mistake 2: Add more agents to fix reliability

More agents can multiply failure opportunities.

### Mistake 3: Hide failures from users

Trust improves when uncertainty is handled transparently.

### Mistake 4: Optimise cost before measuring success

A cheap incorrect answer is more expensive than a slightly more expensive correct decision.

## Practical exercise

Build an AI service that:

- calls a model;
- validates output;
- retries temporary failures;
- switches to a fallback model;
- logs traces;
- escalates uncertain cases.

## Mastery gate

You understand this topic when you can:

- classify AI failures correctly;
- design retry and fallback rules;
- prevent duplicate actions;
- explain when not to retry;
- design graceful degradation;
- add observability before production deployment;
- balance reliability, cost and user experience.

## Strategic perspective

The competitive advantage of AI systems will not come only from having access to powerful models. It will come from building reliable systems around those models that can operate safely under real-world conditions.
