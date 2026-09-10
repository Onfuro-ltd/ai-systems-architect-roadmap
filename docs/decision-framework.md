# AI Technology Decision Framework

AI Systems Architect Roadmap evaluates technologies by architectural value and evidence, not novelty, popularity or marketing reach.

Use this framework for models, frameworks, protocols, agent systems, memory products, infrastructure, research claims and AI-enabled applications.

## Step 1 — Strip away the branding

Describe the technology in one sentence without its product name or marketing language.

Ask:
- What is it actually doing?
- Which layer of the AI system does it affect?
- Is the underlying idea new, or is this a better implementation/packaging of an existing pattern?

## Step 2 — Define the problem

A technology without a clear problem is usually a distraction.

Document:
- the user/system problem;
- who experiences it;
- how the problem is solved today;
- why the existing solution is insufficient.

## Step 3 — Identify the architectural layer

Classify where it belongs, for example:
- model/inference;
- prompting/context;
- knowledge/RAG;
- agent/runtime;
- skills/harness;
- memory;
- MCP/tools/integrations;
- orchestration/workflow;
- evaluation;
- security/governance;
- data/infrastructure;
- user experience;
- business decision layer.

This exposes overlap. Two exciting products may simply compete for the same architectural responsibility.

## Step 4 — Evaluate evidence

Prefer evidence in this order:

1. reproducible real-world evaluation;
2. independent benchmarks with disclosed methodology;
3. primary technical documentation/research;
4. credible production case studies;
5. vendor benchmarks;
6. demonstrations;
7. social-media claims.

A demo proves possibility, not reliability.

## Step 5 — Test the important dimensions

### Capability
Does it solve the stated problem materially better?

### Reliability
What happens across repeated runs, edge cases and long tasks?

### Security
What data, credentials and permissions does it receive? What can it change?

### Economics
Consider model/API cost, compute, storage, engineering, maintenance and operational overhead.

### Latency
Does the architecture remain useful at realistic response times?

### Scale
What changes with more users, tenants, tools, data or concurrent workflows?

### Portability
Does adoption create unnecessary model/vendor/framework lock-in?

### Observability
Can actions, decisions, failures, tool calls and costs be inspected?

### Maintainability
What happens when APIs, models, prompts, schemas or dependencies change?

### Outcome value
Does it improve a meaningful user, operational or business outcome?

## Step 6 — Look for hidden costs and failure modes

Explicitly investigate:
- hallucinations and silent errors;
- context degradation;
- prompt injection;
- permission escalation;
- stale memory/knowledge;
- cascading agent errors;
- tool/API failures;
- rate limits;
- model/provider outages;
- data leakage;
- human review burden;
- lock-in;
- operational complexity;
- evaluation maintenance.

## Step 7 — Compare against doing nothing

The correct comparison is not always Technology A vs Technology B.

Ask whether the capability is worth adding at all. Extra agents, memory, orchestration and middleware can reduce reliability if they do not produce measurable benefit.

## Step 8 — Assign a Technology Radar verdict

### IGNORE
Evidence is weak, the problem is unimportant, the approach is misleading, or the cost/complexity exceeds likely value.

### WATCH
The idea is strategically interesting but immature, unproven or not yet required.

### EXPERIMENT
Evidence is sufficient to justify a controlled test against a baseline.

### ADOPT
The capability is mature enough and valuable enough for defined production use cases.

### BUILD AROUND
The concept is sufficiently durable and foundational that architecture should intentionally support it. This rating normally applies to principles/protocols/patterns more often than individual vendors.

## Step 9 — Record what would change the verdict

Every evaluation should state:
- current verdict;
- confidence;
- evidence used;
- major unresolved questions;
- conditions that would upgrade or downgrade the verdict;
- review date where appropriate.

This prevents the Technology Radar from becoming permanent opinion.

## Recommended review template

```markdown
# Technology / Concept

## One-sentence description

## Problem solved

## Architectural layer

## What is genuinely new

## Evidence

## Strengths

## Limitations and failure modes

## Security / governance

## Economics / operational cost

## Alternatives

## Production maturity

## Verdict
IGNORE / WATCH / EXPERIMENT / ADOPT / BUILD AROUND

## Confidence
Low / Medium / High

## What would change this verdict?

## Suggested experiment (if applicable)
```

## Principle

**Do not ask whether a technology is exciting. Ask whether it earns a place in the architecture.**
