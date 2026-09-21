# 02 — Skill Design and Contracts

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **02 — Skill Design and Contracts** within Skills and Agent Harnesses;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

A reusable AI skill needs an explicit contract.

Without one, a skill can become an informal collection of instructions whose behaviour is difficult to test, compose, govern or safely reuse.

## Core Principle

> A skill should define capability, boundaries and expected behaviour — not merely instructions.

## What a Skill Contract Defines

A production skill can be described through:

- purpose;
- inputs;
- outputs;
- required context;
- required tools;
- permissions;
- execution rules;
- validation;
- failure behaviour;
- evaluation criteria;
- ownership;
- version.

Not every skill requires the same level of formality. The greater the consequence of the capability, the stronger its contract should be.

## Inputs

Inputs define what the skill requires to operate.

They may include:

- structured parameters;
- documents;
- retrieved knowledge;
- current workflow state;
- tool results;
- user or system intent.

Where practical, important inputs should use explicit schemas instead of undocumented natural-language conventions.

## Outputs

Outputs define what successful execution produces.

Examples include:

- structured data;
- analysis;
- recommendations;
- drafts;
- classifications;
- tool requests;
- workflow transitions.

Downstream systems should not have to guess the meaning or structure of consequential outputs.

## Preconditions

A skill may require conditions to be true before execution.

Examples include:

- required data exists;
- required context is sufficiently fresh;
- the caller has the necessary authority;
- required capabilities are available;
- the task falls within the skill scope.

If a precondition fails, the skill should fail safely, request what is missing or escalate rather than inventing state.

## Postconditions

Postconditions describe what should be true after successful execution.

Examples include:

- output conforms to its contract;
- required evidence is attached;
- deterministic validation has passed;
- a requested operation produced an auditable result.

## Capability Dependencies

A skill should declare what external capabilities it requires rather than assume unrestricted access.

The skill describes what it needs.

The surrounding harness and permission architecture decide what it is actually allowed to use.

This separation keeps capability definition distinct from authority.

## Validation

Validation can operate at several layers:

1. schema validation;
2. deterministic rules;
3. domain consistency checks;
4. evidence checks;
5. model-based evaluation where appropriate;
6. human review where consequences justify it.

A model should not be the sole authority for validating consequential actions.

## Failure Contracts

Production skills need explicit failure behaviour.

Possible outcomes include:

- retry;
- use an approved alternative;
- request missing information;
- return a structured failure;
- escalate for review;
- stop safely.

Silent failure and fabricated success are unacceptable production behaviours.

## Composition

Explicit contracts make skills easier to compose.

The validated output of one capability can become the defined input of another.

Composition becomes fragile when one skill depends on undocumented assumptions made by another.

## Model Independence

Durable skill architecture should separate reusable operating knowledge from model-specific implementation where practical.

Model independence does not mean every model performs equally well.

It means the reasoning engine can be evaluated, upgraded or replaced without unnecessarily rewriting the entire capability.

## Versioning

Changes to a skill can change system behaviour.

Version-controlled elements can include:

- contracts;
- instructions;
- schemas;
- tool dependencies;
- context requirements;
- validation;
- knowledge dependencies;
- evaluation suites.

A version should identify behaviour that can be reproduced and evaluated.

## Exercise

Design a skill contract for a generic document-review capability.

Define:

1. purpose;
2. required inputs;
3. expected outputs;
4. capability dependencies;
5. validation;
6. failure behaviour;
7. evaluation criteria.

Then identify which parts should be deterministic and which legitimately require model judgement.

## Takeaway

> Reusable AI capability begins with an explicit contract.

A contract turns informal model behaviour into something engineering teams can test, compose, version and govern.

Next: **03 — Context Engineering for Skills**.
