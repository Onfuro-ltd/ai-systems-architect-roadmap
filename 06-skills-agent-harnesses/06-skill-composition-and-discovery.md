# 06 — Skill Composition and Discovery

## Purpose

As systems accumulate reusable capabilities, they need ways to combine skills and select the right capability without creating uncontrolled complexity.

## Core Principle

> Compose capabilities through explicit contracts, and discover them through explicit metadata.

## Composition

A composed workflow connects the output of one capability to the input of another.

```text
Intent
  |
Skill A
  |
Validated Output
  |
Skill B
  |
Validated Output
  |
Skill C
  |
Outcome
```

Each boundary should preserve meaning, validation and failure behaviour.

## Contract Compatibility

Two skills are easier to compose when they agree on:

- data shape;
- semantics;
- required context;
- authority;
- failure states;
- version expectations.

Schema compatibility alone is not enough if the meaning of the data differs.

## Deterministic vs Model-Selected Composition

Composition can be controlled in different ways.

### Deterministic

Software selects the sequence in advance.

Useful when the process is stable and predictable.

### Model-Selected

The model chooses among available capabilities.

Useful when the correct next capability depends on reasoning.

### Hybrid

Software defines a bounded set of possible transitions while the model selects within those boundaries.

Hybrid control is often useful for production systems.

## Skill Discovery

Discovery answers:

> Which capability is appropriate for this task?

A registry can expose metadata such as:

- name;
- purpose;
- supported inputs;
- outputs;
- required tools;
- permissions;
- owner;
- version;
- evaluation status;
- deprecation state.

## Progressive Disclosure

A system does not always need to expose the entire skill library to the model.

It can first narrow the candidate set and expose only relevant capabilities.

This reduces confusion, token usage and accidental access.

## Routing

Routing may use:

- deterministic rules;
- classifiers;
- embeddings;
- model reasoning;
- capability metadata;
- policy filters;
- historical evaluation data.

Routing itself should be evaluated because incorrect capability selection can fail even when every individual skill works correctly.

## Capability Graphs

Larger systems may represent relationships between capabilities as a graph.

Relationships can include:

- depends on;
- produces input for;
- replaces;
- conflicts with;
- requires approval before;
- deprecated by.

The graph should support architecture, not become unnecessary abstraction.

## Failure Isolation

Composition increases the number of failure points.

The system should preserve which component failed and avoid converting every downstream failure into a generic agent error.

Useful failure metadata includes:

- skill;
- version;
- step;
- input;
- validation result;
- retry state.

## Ownership

Every production capability should have a clear owner or responsible team.

Ownership supports:

- maintenance;
- incident response;
- evaluation;
- versioning;
- deprecation.

An unowned skill library becomes operational debt.

## Exercise

Design a registry for five generic enterprise skills.

Define the metadata required for discovery, composition, permissions, evaluation and ownership.

Then design one deterministic composition and one model-assisted composition using those skills.

## Takeaway

> Skill libraries become useful systems only when capabilities can be safely discovered, composed and owned.

Next: **07 — Testing, Evaluation and Quality Gates**.
