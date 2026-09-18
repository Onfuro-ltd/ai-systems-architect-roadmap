# 02 — Working, Episodic, Semantic and Procedural Memory

## Purpose

Memory is not one thing.

Different types of retained information support different system behaviours.

A useful taxonomy helps architects decide where information belongs and how it should be retrieved.

## Core Principle

> Match the memory type to the job it performs.

## Working Memory

Working memory supports the current task.

Examples include:

- current subgoal;
- intermediate result;
- temporary plan;
- recent tool output;
- current hypothesis.

Working memory is usually short-lived.

It often belongs in execution state or context rather than durable long-term storage.

## Episodic Memory

Episodic memory represents past events or experiences.

Examples:

- a previous interaction;
- a completed workflow;
- an incident;
- an earlier decision;
- a user correction.

A useful episodic record can answer:

- what happened;
- when;
- who was involved;
- what outcome occurred.

## Semantic Memory

Semantic memory represents facts or stable learned information.

Examples:

- remembered preference;
- established relationship;
- recurring constraint;
- derived fact.

Semantic memory should not silently compete with authoritative knowledge sources.

Where a fact belongs in a source-of-truth system, move it there rather than leaving it only in memory.

## Procedural Memory

Procedural memory captures reusable ways of doing something.

Examples:

- preferred review process;
- learned workflow pattern;
- recurring sequence;
- proven decision procedure.

In production systems, durable procedural knowledge often belongs in explicit skills, rules or workflows rather than opaque model memory.

This is why Domain 06 and Domain 08 overlap conceptually but remain distinct.

## Memory Type vs Storage Technology

A memory type is an information-design concept.

It is not a database choice.

For example, episodic memories could be stored in:

- relational tables;
- document stores;
- object storage;
- vector indexes;
- event logs.

Choose storage according to query and lifecycle needs.

## Hybrid Records

A single event can produce multiple memory forms.

Example:

```text
Event: user rejects a recommendation
        |
        +-- Episodic: rejection occurred
        +-- Semantic: user prefers alternative category
        +-- Procedural: future workflow should ask before recommending
```

The architecture should avoid creating all three automatically without evidence.

## Promotion

Information can be promoted across memory types.

For example:

1. repeated episodes show a pattern;
2. the pattern is validated;
3. a semantic memory is created;
4. later it becomes explicit product or business configuration.

Promotion should be deliberate.

## Demotion and Retirement

A semantic memory may become uncertain or stale.

The system may:

- reduce confidence;
- mark superseded;
- move to historical evidence;
- delete according to policy.

Memory type should not imply permanence.

## Procedural Memory Warning

Procedural memory can become hidden policy.

If an organisation depends on it operationally, extract it into explicit:

- skill contracts;
- workflows;
- rules;
- documentation.

Opaque procedural memory is difficult to audit.

## Exercise

Classify the following:

- current calculation;
- last week's failed workflow;
- preferred reporting format;
- approved review procedure;
- repeated observed preference;
- current retry count.

Explain whether each should remain temporary, become memory, or move into an authoritative system.

## Takeaway

> Memory types describe what information means over time, not where it is stored.

Next: **03 — Memory Write, Retrieval and Ranking**.
