# 04 — Agent Harness Architecture

## Purpose

An agent harness is the operational control layer around model-driven reasoning.

It connects a model to skills, context, tools, state, policies, validation, evaluation and observability while controlling how execution proceeds.

The harness does not make the model deterministic. It creates deterministic boundaries around probabilistic behaviour where control is required.

## Core Principle

> The model provides reasoning capability. The harness provides execution control.

A powerful model alone is not a production agent architecture.

## Model, Agent and Harness

These concepts should not be collapsed into one abstraction.

### Model

Provides probabilistic reasoning and generation capability.

### Agent

Uses model reasoning to pursue an objective, potentially across multiple steps and capabilities.

### Harness

Provides the software boundary in which that reasoning is allowed to operate.

The model may propose what should happen next. The harness determines how that proposal is interpreted, validated and permitted to proceed.

## Reference Architecture

```text
User / System Request
         |
         v
Agent Harness
         |
         +-- Identity / Session
         +-- Skill Selection
         +-- Context Assembly
         +-- Model Routing
         +-- Tool Mediation
         +-- State Management
         +-- Rules / Policies
         +-- Lifecycle Controls
         +-- Validation
         +-- Evaluation
         +-- Observability
         +-- Failure / Escalation
         |
         v
Controlled Outcome
```

The exact implementation can vary, but production systems need explicit ownership of these concerns somewhere in the architecture.

## Request Boundary

The harness receives an execution request and establishes the conditions under which it can run.

This can include:

- caller identity;
- requested capability;
- execution scope;
- available state;
- applicable policy;
- time or cost constraints;
- correlation and trace identifiers.

The request boundary prevents execution from beginning as an unstructured conversation with unrestricted system access.

## Execution Lifecycle

A controlled execution can be represented as:

```text
Request
   |
   v
Identify / Authorise
   |
   v
Select Capability
   |
   v
Assemble Context
   |
   v
Invoke Model
   |
   v
Interpret Proposed Action
   |
   v
Validate / Authorise
   |
   v
Execute or Escalate
   |
   v
Observe / Evaluate
   |
   v
Return Outcome
```

The exact stages vary by system, but consequential transitions should be explicit.

## Identity and Session

The harness should know enough about the execution identity and session to apply the correct controls.

This can include:

- user or service identity;
- tenant or workspace;
- current session;
- delegated authority;
- previous workflow state.

Identity is not the same as permission. Identity establishes who or what is acting; policy determines what that actor may do.

## Skill Selection

The harness can expose a bounded set of skills appropriate to the task and caller.

Selection may be deterministic, model-assisted or hybrid.

A model should not automatically gain access to every capability merely because those capabilities exist.

## Context Assembly

The harness is responsible for constructing the execution context required by the selected capability.

This includes controlling:

- source selection;
- relevance;
- provenance;
- freshness;
- isolation;
- context budgets.

Context engineering is covered in detail in Lesson 03.

## Model Routing

A harness may support one or more models.

Routing can consider:

- capability requirements;
- latency;
- cost;
- context length;
- modality;
- reliability history;
- policy constraints.

Model routing should remain an implementation decision around the capability rather than forcing every skill to depend permanently on one provider.

## Tool Mediation

A model-generated tool call should be treated as a proposed action, not automatic authority.

The harness can mediate:

- tool availability;
- arguments;
- schemas;
- permissions;
- approval requirements;
- rate limits;
- execution timeouts;
- retries;
- result validation.

The tool boundary is one of the most important control points in an agent system.

## State Management

The harness may maintain execution state across steps.

State can include:

- current goal;
- completed steps;
- pending actions;
- tool results;
- approvals;
- retry counts;
- checkpoints.

Durable long-term memory is a separate concern covered in Domain 08.

## Rules and Policies

The harness can apply deterministic rules around model behaviour.

Examples include:

- prohibited actions;
- required approvals;
- allowed tools;
- data-access restrictions;
- retry limits;
- spending limits;
- mandatory validation.

Policy should not depend solely on the model remembering instructions.

## Validation

Validation should occur before important outputs or actions are accepted.

Possible layers include:

- schema checks;
- deterministic business rules;
- evidence checks;
- consistency checks;
- secondary evaluation;
- human approval.

The model should not be the final authority over its own consequential actions.

## Failure and Escalation

Production harnesses need explicit failure behaviour.

Examples include:

- retry with bounded limits;
- switch strategy;
- switch model;
- request missing information;
- return a structured failure;
- escalate to a human;
- stop safely.

Infinite retries and fabricated success are both architectural failures.

## Observability

A harness should make execution inspectable.

Useful telemetry can include:

- request identifiers;
- selected skill;
- model and version;
- context sources;
- tool calls;
- validation outcomes;
- approvals;
- latency;
- token usage;
- cost;
- errors;
- final status.

Sensitive content should be logged according to privacy and security policy rather than indiscriminately.

## Evaluation

Harness evaluation goes beyond whether the final text looks good.

A system can measure:

- task completion;
- correct capability selection;
- correct tool use;
- policy compliance;
- recovery behaviour;
- latency;
- cost;
- escalation quality.

Domain 10 covers evaluation and reliability in depth.

## Harness vs Orchestrator

A harness controls the execution environment around an agent or model-driven capability.

An orchestrator coordinates work across workflows, agents or long-running processes.

A system may combine the two, but they solve different architectural problems.

Orchestration is covered in Domain 09.

## Harness vs MCP

A harness can consume capabilities exposed through MCP, direct APIs, function calling or other interfaces.

MCP does not replace the harness.

Domain 07 covers MCP and tool ecosystems.

## Exercise

Design a harness for a generic research-and-review agent.

Specify:

1. request boundary;
2. skill selection;
3. context assembly;
4. model routing;
5. permitted tools;
6. validation;
7. approval points;
8. retry and escalation rules;
9. observability;
10. evaluation signals.

Then identify which decisions may be delegated to the model and which must remain deterministic.

## Takeaway

> The harness is the control plane around probabilistic reasoning.

A production agent is not only a model with tools. It is a controlled execution system with explicit boundaries, validation, observability and failure behaviour.

Next: **05 — Rules, Hooks and Lifecycle Controls**.
