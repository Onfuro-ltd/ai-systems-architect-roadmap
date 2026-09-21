# 09 — Capstone: Design a Production Orchestration System

## Objective

Design an orchestration architecture for a complex task and justify every layer of coordination.

The capstone should demonstrate restraint as well as capability.

## Scenario

Choose a generic task such as:

- complex research;
- multi-document analysis;
- software change workflow;
- operational exception investigation;
- enterprise review process.

## Part 1 — Task Topology

Describe:

- sequential dependencies;
- parallelisable work;
- uncertain branches;
- irreversible actions;
- approval points.

Draw the dependency graph.

## Part 2 — Complexity Decision

Compare:

1. deterministic workflow;
2. single agent;
3. multi-agent design.

Explain why the chosen architecture is necessary.

## Part 3 — State Machine

Define states for:

- received;
- active;
- waiting;
- retrying;
- approved;
- completed;
- failed;
- cancelled;
- escalated.

Define valid transitions.

## Part 4 — Agent Boundaries

For every agent, define:

- purpose;
- context;
- tools;
- permissions;
- outputs;
- stopping condition.

Remove any agent that does not need independent reasoning.

## Part 5 — Routing and Parallelism

Define:

- router;
- fan-out;
- concurrency;
- dependency handling;
- fan-in;
- synthesis.

## Part 6 — Long-Running Behaviour

Define:

- checkpoints;
- queue;
- events;
- durable timers;
- human wait states;
- restart recovery.

## Part 7 — Validation

Define:

- deterministic gates;
- model-based evaluation;
- independent review;
- approval.

## Part 8 — Failure Recovery

Design behaviour for:

- worker timeout;
- invalid result;
- duplicated delivery;
- partial side effect;
- dependency outage;
- failed synthesis.

Include compensation where necessary.

## Part 9 — Observability

Specify:

- root run ID;
- child lineage;
- state transition log;
- traces;
- metrics;
- cost attribution;
- queue metrics.

## Part 10 — Evaluation

Evaluate:

- final outcome quality;
- tool correctness;
- route correctness;
- unnecessary delegation;
- retry behaviour;
- cost;
- latency;
- recovery.

Compare the multi-agent design with a single-agent baseline.

## Architectural Review Questions

Before completion, answer:

1. Could deterministic software replace any agent?
2. Could one agent replace several?
3. Does each worker have a bounded contract?
4. Is parallel work genuinely independent?
5. Is shared state controlled?
6. Can the workflow resume after restart?
7. Are retries safe?
8. Can operators cancel it?
9. Can every side effect be traced?
10. Does the added complexity measurably improve outcomes?

## Completion Criteria

Another engineer should be able to determine:

- why orchestration is needed;
- why each agent exists;
- what state is durable;
- how work is routed;
- how concurrency is controlled;
- how failures recover;
- how humans intervene;
- how the system is observed;
- how complexity is justified.

## Takeaway

> The best orchestration design is the simplest one that reliably handles the real structure of the work.

Next: **Domain 10 — Evaluation and Reliability**.
