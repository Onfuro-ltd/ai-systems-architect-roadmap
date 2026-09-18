# 05 — Agent, Tool and Workflow Evaluation

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **05 — Agent, Tool and Workflow Evaluation** within Evaluation and Reliability;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Agents and workflows must be evaluated as trajectories, not only by final text.

A system can produce an acceptable answer through unsafe, wasteful or unreliable behaviour.

## Core Principle

> Evaluate both outcome and process.

## Trajectory

An agent trajectory can contain:

- observations;
- reasoning decisions;
- tool requests;
- tool results;
- state transitions;
- delegation;
- retries;
- approvals;
- final outcome.

Not every internal model token needs to be inspected, but system actions should be observable.

## Tool Selection

Evaluate:

- correct tool selected;
- unnecessary tool avoided;
- prohibited tool not used;
- arguments valid;
- authority respected.

## Tool Result Handling

Test whether the agent:

- detects tool errors;
- handles partial data;
- avoids fabricating success;
- retries safely;
- escalates when needed.

## Workflow Evaluation

Evaluate:

- correct path;
- required gates;
- state transitions;
- approval;
- completion;
- recovery.

## Agent Completion

A common failure is premature completion.

Test whether the agent stops only when:

- objective achieved;
- required evidence exists;
- validation passed;
- no required work remains.

## Excessive Work

Also test whether the agent:

- repeats queries;
- loops;
- over-delegates;
- performs unnecessary tool calls.

Efficiency is part of reliability.

## Delegation Evaluation

For multi-agent systems, evaluate:

- correct delegation;
- bounded scope;
- worker output validity;
- synthesis;
- duplicate work;
- cancellation.

## Trace Grading

Trace grading evaluates structured execution records.

A trace evaluator can inspect:

- whether the right tool was used;
- whether the action sequence was valid;
- whether policy gates occurred;
- whether recovery was correct.

This is often more diagnostic than scoring final output alone.

## Environment Fidelity

Agent evaluations depend on the environment.

Ensure test environments represent:

- available tools;
- permissions;
- data;
- latency;
- failures.

A model can appear better in an unrealistically clean sandbox.

## Long-Horizon Evaluation

Long tasks increase failure probability.

Test:

- checkpointing;
- state persistence;
- recovery;
- context drift;
- version drift.

## Counterfactual Evaluation

Ask whether a simpler architecture performs equally well.

Compare:

- no tool vs tool;
- single agent vs multi-agent;
- no memory vs memory;
- small model vs large model.

## Exercise

Design an evaluation for an agent that performs research and then creates a structured report.

Score:

1. research coverage;
2. tool correctness;
3. citation support;
4. unnecessary calls;
5. recovery;
6. final report quality.

## Takeaway

> A reliable agent is not merely one that reaches the right answer; it reaches it through an acceptable execution path.

Next: **06 — Reliability, Regression and Failure Analysis**.
