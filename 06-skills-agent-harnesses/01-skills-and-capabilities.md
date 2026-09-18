# 01 — Skills and Capabilities

## Purpose

Skills package reusable expertise so that AI systems can apply it consistently across tasks, models and workflows.

A skill is more than a prompt. It is a defined capability with a purpose, operating assumptions, inputs, outputs, constraints, dependencies and evaluation criteria.

## Core Principle

> Reusable capability should be explicit enough to test, version, compose and govern.

## Prompt, Tool, Skill and Agent

These concepts are related but distinct.

### Prompt

An instruction or set of instructions supplied to a model.

### Tool

An external capability the system can invoke.

### Skill

A reusable package of expertise and operating logic for accomplishing a class of tasks.

### Agent

A system that can use reasoning, skills, tools and state to pursue an objective across one or more steps.

A skill may use prompts and tools without itself being an autonomous agent.

## What a Skill Can Contain

A production skill can include:

- instructions;
- domain knowledge;
- examples;
- input and output contracts;
- context requirements;
- tool dependencies;
- validation rules;
- workflow logic;
- failure behaviour;
- evaluation criteria;
- ownership and version metadata.

The exact packaging depends on the system, but the architectural idea remains the same: capability should be separable from one-off conversation state.

## Capability Boundaries

A good skill defines what it is intended to do and what it is not intended to do.

Boundaries can include:

- supported tasks;
- unsupported tasks;
- required evidence;
- permitted tools;
- authority limits;
- escalation conditions;
- expected output forms.

Without boundaries, skills become difficult to compose safely.

## Reusability

A capability becomes more reusable when it depends on explicit contracts rather than hidden assumptions.

Useful questions include:

- What inputs does the skill require?
- What context must be present?
- What tools may it use?
- What output does it guarantee?
- What happens when required information is missing?
- How is success measured?

## Durable Operating Knowledge

Skills are a useful place to encode operating knowledge that should survive changes in models or vendors.

Examples include:

- review procedures;
- analytical methods;
- domain checklists;
- decision rules;
- escalation logic;
- validation requirements.

Durability does not mean hard-coding every decision. It means separating reusable organisational knowledge from transient model behaviour.

## Composition

Skills can be combined into larger workflows when their contracts are compatible.

```text
Intent
  |
  v
Skill A
  |
Validated Output
  |
  v
Skill B
  |
Validated Output
  |
  v
Outcome
```

Composition should remain explicit. Hidden dependencies between skills create fragile systems.

## Discovery

As skill libraries grow, systems may need mechanisms for discovering the right capability for a task.

Discovery can use:

- explicit routing;
- metadata;
- capability descriptions;
- schemas;
- policy filters;
- evaluation history.

The model may assist with selection, but the surrounding system should preserve control over what capabilities are exposed and permitted.

## Evaluation

A skill should be evaluated as a capability, not only as a prompt.

Evaluation can consider:

- task success;
- output validity;
- evidence quality;
- failure handling;
- tool use;
- latency;
- cost;
- robustness across models.

Broader evaluation design is covered in Domain 10.

## Exercise

Choose a recurring knowledge-work task and describe it as a reusable skill.

Define:

1. purpose;
2. supported inputs;
3. expected outputs;
4. context requirements;
5. tool dependencies;
6. validation;
7. failure behaviour;
8. evaluation criteria.

Then identify which parts should remain stable if the underlying model changes.

## Takeaway

> Skills turn reusable expertise into an architectural asset.

The goal is not to create a larger prompt library. The goal is to create capabilities that can be tested, composed, versioned and governed.

Next: **02 — Skill Design and Contracts**.
