# 02 — Events, Commands and State

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **02 — Events, Commands and State** within Data and Event Architecture;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Reliable distributed and AI systems distinguish three ideas that are often blurred together: **state**, **commands**, and **events**.

> State describes what is true now. A command requests a change. An event records something that has happened.

Confusing these concepts creates ambiguous workflows, unsafe retries, broken audit trails, and AI agents that mistake an intention for an outcome.

## 1. State

State is the current authoritative representation of relevant facts.

Examples:

```text
order.status = shipped
available_quantity = 14
approval.status = pending
user.access_level = editor
```

State answers a question about the present. It is usually mutable over time, even when its history is preserved elsewhere.

## 2. Commands

A command expresses intent for a system to perform an operation.

Examples:

```text
CreateOrder
ReserveInventory
ApproveRequest
RefreshCatalogue
SendNotification
```

Commands are normally imperative. They can be accepted, rejected, delayed, retried, or fail.

A command is not evidence that its requested outcome occurred.

```text
SendPayment command
        !=
PaymentSent event
```

## 3. Events

An event records a fact that the producing system says has already occurred.

Examples:

```text
OrderCreated
InventoryReserved
RequestApproved
CatalogueRefreshed
NotificationSent
```

Events are normally expressed in past tense because they describe completed facts.

## 4. The basic lifecycle

```text
Intent
  ↓
Command
  ↓
Validation
  ↓
Authoritative mutation
  ↓
Event
  ↓
Consumers update their own state
```

Not every internal operation needs an explicit command or externally published event. Use these abstractions where they clarify ownership and coordination.

## 5. Event notification vs event-carried state transfer

An event can merely announce that something changed:

```json
{
  "type": "ProductUpdated",
  "product_id": "P123"
}
```

The consumer then queries the owner for current state.

Or an event can carry useful state:

```json
{
  "type": "ProductPriceChanged",
  "product_id": "P123",
  "old_price": 24.99,
  "new_price": 22.99,
  "currency": "GBP"
}
```

The first approach reduces duplicated data but creates read dependencies. The second can improve decoupling but increases contract and privacy responsibilities.

Choose deliberately.

## 6. Domain events vs integration events

A domain event represents something meaningful inside a bounded domain. An integration event is a contract intentionally exposed to other domains or systems.

They do not have to be identical.

```text
Internal domain change
        ↓
Domain event
        ↓
Integration boundary
        ↓
Stable integration event
```

This prevents internal implementation details from becoming permanent public contracts.

## 7. Events should represent facts, not instructions

An event such as `OrderCreated` should not secretly mean “please perform these five mandatory actions.” Consumers decide whether the fact is relevant to them.

If another component must perform an operation as part of a controlled process, an explicit command or workflow step may communicate the requirement more clearly.

## 8. Commands need an owner

A command should target a capability that owns the requested mutation.

```text
Caller
  ↓
ReserveInventory
  ↓
Inventory owner
  ↓
validate + mutate
  ↓
InventoryReserved
```

Do not let callers bypass the owner and directly modify authoritative records.

## 9. Events need identity

Useful event metadata commonly includes:

```text
event_id
event_type
schema_version
occurred_at
producer
aggregate/entity identifier
tenant_id where applicable
correlation_id
causation_id
```

Metadata should support correctness, tracing, replay, governance, and debugging without becoming an uncontrolled dumping ground.

## 10. Correlation and causation

Correlation connects related activity across a workflow. Causation records what directly caused a new command or event.

```text
User request
 correlation: C1
      ↓
Command A
 correlation: C1
      ↓
Event A
 correlation: C1
      ↓ causes
Command B
 correlation: C1
 causation: Event A
```

This becomes valuable when a workflow crosses queues, services, tools, AI steps, and external providers.

## 11. Event time vs processing time

`occurred_at` describes when the business event happened. `received_at` or processing time describes when a consumer observed it.

These can differ substantially because of network delay, retries, offline systems, imports, and replay.

Do not use consumer processing time as a substitute for business-event time when semantics require the latter.

## 12. Late and out-of-order events

Distributed systems can deliver events after newer events have already been processed.

Possible protections include:

- entity versions;
- sequence numbers;
- monotonic offsets within a partition;
- business timestamps with careful conflict rules;
- authoritative rereads;
- reconciliation.

Never assume global arrival order unless the architecture explicitly guarantees it.

## 13. Duplicate events

At-least-once delivery means a consumer may receive the same event more than once.

```text
Event E42
  ↓
Consumer processes
  ↓
Acknowledgement lost
  ↓
Event E42 delivered again
```

Consumers that create consequential effects should be idempotent or deduplicate using stable event/operation identities.

## 14. Events are immutable records

Once published, an event should normally not be edited in place. If a previously published business fact requires correction, represent the correction explicitly or rebuild the relevant projection according to the system's design.

Immutability does not mean every event must be retained forever. Retention is a separate governance decision.

## 15. State transitions should remain authoritative

An event stream is not permission to let arbitrary consumers mutate another domain's state.

```text
Event received
    ↓
Consumer interprets
    ↓
If mutation elsewhere is required
    ↓
Send command to owning capability
```

Ownership remains intact even in event-driven systems.

## 16. AI agents must distinguish observation from action

This distinction is especially important for agents.

```text
Event: InventoryLow
        ↓
AI reasons
        ↓
Proposal: replenish 50 units
        ↓
Policy / permission / validation
        ↓
Command: CreateReplenishment
        ↓
Owning service executes
        ↓
Event: ReplenishmentCreated
```

The agent's proposal is neither a command nor an event until the deterministic system deliberately turns it into one.

## 17. Tool responses are observations, not necessarily truth

An agent calling a tool may receive a response from a cache, external API, replica, or eventually consistent system.

The tool contract should communicate authority and freshness where those matter. For consequential actions, current authoritative state may need to be checked again before execution.

## 18. Event-driven does not mean everything is asynchronous

A system can combine synchronous commands and asynchronous events:

```text
Client
  ↓ synchronous
CreateOrder command
  ↓
Order service commits
  ↓
Return order ID
  ↓ asynchronous
OrderCreated event
  ↓
Analytics / notification / AI consumers
```

This is often simpler than forcing every interaction through a message broker.

## 19. Choreography vs orchestration

With choreography, components react to events without one central workflow controller.

With orchestration, a workflow component explicitly coordinates steps and state.

Choreography can reduce central coupling but may create invisible process logic spread across many consumers. Orchestration makes long-running process state explicit but introduces a coordinator.

Choose based on process complexity, auditability, failure handling, ownership, and change frequency.

## 20. Event storms and semantic quality

Publishing every database update as a business event does not create a good event architecture.

Useful events have meaningful semantics.

Prefer:

```text
CustomerAddressVerified
```

over an unexplained low-level signal such as:

```text
customer_table_row_updated
```

unless low-level change capture is intentionally what consumers require.

## 21. Generic commerce example

```text
External order observed
        ↓
Integration records observation
        ↓
Command: ImportOrder
        ↓
Order capability validates + persists
        ↓
Event: OrderImported
        ↓
Inventory projection updates
Analytics consumes
AI workflow may evaluate
```

If AI recommends an operational action, it produces a proposal. A deterministic boundary validates the current facts and issues a command to the capability that owns the mutation. Only after execution is an outcome event produced.

## 22. Anti-patterns

Avoid:

- naming commands as if they were completed events;
- treating an event as a request for mandatory hidden behaviour;
- publishing raw database changes as domain semantics without intent;
- assuming arrival order is business order;
- assuming delivery is exactly once;
- using timestamps alone as universal ordering guarantees;
- allowing consumers to mutate another domain's records directly;
- treating an AI recommendation as an executed command;
- treating a command acknowledgement as proof of external outcome;
- building long workflows through invisible chains of event reactions with no operational visibility.

## 23. Architect checklist

For each message or transition ask:

- Is this state, a command, an event, or a derived interpretation?
- Who owns the underlying fact?
- Is the message describing intent or completed outcome?
- What stable identity does it have?
- What schema/version applies?
- What tenant/security context applies?
- Can it arrive twice?
- Can it arrive late or out of order?
- Does the consumer create external side effects?
- Is the consumer idempotent?
- Is choreography still understandable, or should the process be orchestrated?
- Can the complete causal path be traced?
- Is AI proposing an action or actually authorized to issue the command?

## 24. Exercise

Model a workflow with at least four state transitions.

For every transition document:

1. initiating intent;
2. command, if any;
3. owning capability;
4. validation;
5. authoritative state mutation;
6. resulting event;
7. downstream consumers;
8. duplicate handling;
9. ordering assumptions;
10. failure and recovery behaviour;
11. where AI may observe, recommend, or act;
12. which deterministic boundary authorizes any consequential action.

Then draw the causal chain from user/system intent to final verified outcome.

## Takeaway

> Commands request change, events record completed facts, and state represents current truth. Keeping those concepts separate makes distributed workflows easier to reason about and prevents AI-generated intent from being mistaken for authoritative outcome.

Next: **03 — Event Contracts and Schema Evolution**.
