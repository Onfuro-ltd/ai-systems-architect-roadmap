# 07 — Idempotency

## Purpose

Distributed systems retry work, receive duplicate events, lose acknowledgements, and recover after partial failures. Idempotency ensures that repeating the same logical operation does not accidentally repeat its business effect.

For AI systems, this becomes critical when models and agents can trigger tools that modify external state.

## Core principle

> Design every retryable or externally triggered business operation so the same logical intent can be processed more than once without creating an unintended duplicate effect.

## 1. What idempotency means

An idempotent operation can be repeated while preserving the intended final business state.

Conceptually:

```text
apply(operation)
apply(operation)
apply(operation)

→ one intended business effect
```

This does not necessarily mean every request returns byte-for-byte identical metadata. It means the business effect is not duplicated.

## 2. Why duplicates happen

Duplicates are normal in distributed systems.

Examples:

- a queue redelivers a job;
- a webhook is delivered twice;
- an HTTP client retries after a timeout;
- a worker crashes after committing but before acknowledging;
- a scheduler overlaps;
- a user double-clicks;
- an agent retries a tool call because it did not observe the first result.

The architecture should assume these events will happen.

## 3. At-least-once delivery

Many practical queue and event systems provide at-least-once delivery semantics.

That means:

```text
Message
  ↓
May be delivered once
or
May be delivered multiple times
```

The consumer must therefore protect the business operation.

## 4. Idempotency keys

An idempotency key identifies one logical intent.

Example:

```text
Tenant
+
Operation type
+
Business identifier
+
Intent/version
=
Idempotency key
```

The key should be stable across retries of the same intent but different for a genuinely new operation.

## 5. Request lifecycle

A common pattern is:

```text
Request + Idempotency Key
          ↓
Lookup existing operation
          ├── completed → return recorded result
          ├── running   → return/await existing state
          └── absent
               ↓
          create operation atomically
               ↓
             execute
               ↓
          persist outcome
```

The check and claim must be concurrency-safe.

## 6. Database constraints

Application-level checks alone can race.

Prefer database-enforced uniqueness where possible.

```text
UNIQUE(tenant_id, idempotency_key)
```

Two workers may both ask whether an operation exists. A unique constraint gives the system a deterministic winner.

## 7. Idempotency is not deduplication alone

Deduplication asks:

> Have I seen this message before?

Idempotency asks:

> Can processing this logical operation again cause an unintended business effect?

A duplicate event may legitimately be reprocessed if downstream state has changed, while an irreversible external action may require strict intent-level idempotency.

## 8. Side effects

The difficult cases involve external side effects:

- changing marketplace price;
- cancelling an order;
- creating a shipment;
- issuing a refund;
- sending a customer message;
- modifying advertising state.

For these operations, persist intent and execution state before or around the external call according to the guarantees available from the external API.

## 9. External API idempotency

If an external API supports an idempotency or request key, use it where appropriate.

If it does not, the application may need to use:

- its own operation ledger;
- provider object identifiers;
- read-before-write checks where safe;
- reconciliation after uncertain outcomes.

Never assume a timeout means the external action did not happen.

## 10. The uncertain-outcome problem

Consider:

```text
AI platform → external marketplace: execute action
                     ↓
               action succeeds
                     ↓
              response is lost
```

The AI platform sees a timeout, but the marketplace may already have changed.

Blindly retrying can duplicate the action.

The correct response may require:

```text
UNKNOWN outcome
      ↓
Reconcile external state
      ↓
Confirm success / retry safely / escalate
```

`UNKNOWN` is a legitimate state in distributed workflows.

## 11. Queue jobs

A queue worker should be safe if the same job is delivered again.

Example:

```text
Receive job
   ↓
Claim logical operation
   ↓
Already completed?
   ├── yes → acknowledge safely
   └── no  → continue
```

Do not make the queue message identifier the only business idempotency mechanism if retries can create new message IDs.

## 12. Webhooks

Webhook consumers should expect duplicates and out-of-order delivery.

Useful controls include:

- provider event IDs;
- signature verification;
- event ledger;
- state/version checks;
- idempotent domain handlers.

```text
Webhook
   ↓
Authenticate
   ↓
Record event ID
   ↓
Validate current domain state
   ↓
Apply safe transition
```

## 13. Scheduled jobs

Schedulers can overlap because of:

- slow prior runs;
- duplicate scheduler processes;
- failover;
- clock or deployment behaviour.

Protect scheduled business work with explicit locking, job identity, or state-based claims rather than assuming only one scheduler will ever run.

## 14. AI agent tool calls

An agent may reason:

```text
"The tool call appears to have failed. I should try again."
```

That is dangerous for state-changing tools.

The safer architecture is:

```text
Agent proposes action
       ↓
Create deterministic operation intent
       ↓
Assign idempotency key
       ↓
Policy / permission / validation
       ↓
Execution service
       ↓
Persist result
       ↓
Agent observes authoritative outcome
```

The model should not invent idempotency semantics itself.

## 15. State machines and idempotency

State machines reinforce idempotency.

Example:

```text
APPROVED
   ↓ execute
EXECUTING
   ↓
COMPLETED
```

A repeated `execute` request against `COMPLETED` should not execute the business action again unless the domain explicitly creates a new intent/version.

## 16. Outbox pattern

A common consistency problem is:

```text
Database commit succeeds
Event publish fails
```

The transactional outbox pattern records the domain change and an event-to-publish in the same local database transaction.

```text
Transaction
 ├── update domain state
 └── insert outbox event

Publisher
   ↓
reads outbox
   ↓
publishes event
   ↓
marks delivered
```

Consumers must still be idempotent because publication itself can be retried.

## 17. Inbox / processed-event pattern

Consumers can maintain a durable record of handled event identifiers.

```text
Receive event
   ↓
Atomic processed-event check/claim
   ↓
Apply domain transition
   ↓
Commit
```

This is useful when duplicate delivery is expected, but retention and storage strategy must be defined.

## 18. Idempotency key lifetime

Keys should not automatically live forever.

Define retention based on:

- business risk;
- provider retry windows;
- audit requirements;
- operation semantics.

A payment-like or irreversible operation may require much stronger retention than a disposable read-side computation.

## 19. Multi-tenant systems

Idempotency must be scoped correctly.

Prefer:

```text
tenant_id + logical_operation_key
```

rather than a globally ambiguous key that could allow one tenant's request to collide with another tenant's operation.

## 20. Observability

Track:

- duplicate requests received;
- duplicate operations prevented;
- uncertain external outcomes;
- reconciliation results;
- key collisions;
- retries per operation;
- idempotency-store failures.

A rising duplicate rate may indicate a deeper queue, scheduler, webhook, or networking problem.

## 21. Testing

Test scenarios such as:

- same request submitted twice;
- concurrent duplicate requests;
- worker crash before external call;
- worker crash after external success but before local acknowledgement;
- duplicate webhook;
- out-of-order webhook;
- timeout with unknown provider outcome;
- queue redelivery;
- overlapping scheduled run;
- agent repeating a state-changing tool call.

The expected result should be one intended business effect.

## 22. Generic application

For an AI-native operations platform, idempotency should be treated as a cross-cutting concern for marketplace integrations, queue jobs, notifications, imports, and AI actions.

Example controlled marketplace action:

```text
Recommendation
      ↓
Approval
      ↓
Operation Intent
      ↓
Idempotency Key
      ↓
Execution Service
      ↓
Amazon / eBay / Shopify
      ↓
Persist Provider Outcome
      ↓
Verify / Reconcile
      ↓
Completed
```

This is especially important where duplicate processing could change price twice, send duplicate communication, recreate a resource, or perform another irreversible action.

## 23. Enterprise checklist

For every state-changing operation, ask:

1. What defines one logical intent?
2. What is the idempotency key?
3. Is it scoped by tenant?
4. Is the claim concurrency-safe?
5. Is uniqueness enforced at the database layer where possible?
6. What happens on queue redelivery?
7. What happens on duplicate webhook delivery?
8. What happens if the external action succeeds but the response is lost?
9. Does the external API support idempotency keys?
10. How is `UNKNOWN` outcome represented?
11. How is reconciliation performed?
12. Can an AI agent repeat the action directly?
13. How long is the idempotency record retained?
14. Are duplicate-prevention events observable?

## Takeaway

> Retries are normal. Duplicate business effects are not.

Idempotency is the deterministic safety layer that lets distributed systems retry, recover and redeliver work without turning infrastructure uncertainty into duplicated real-world actions.
