# 06 — Reasoning and Test-Time Compute

Modern models can often improve difficult-task performance when they are allowed to spend more computation during inference. This changes an important systems-design assumption: capability is not determined only by the model selected before the request begins.

The architect's question becomes:

> How much computation, search and verification should this task receive before the system commits to an answer or action?

## Learning outcomes

By the end of this module, you should be able to:

- distinguish model capability from inference strategy;
- explain why intermediate reasoning can help some tasks;
- understand self-consistency, search and verification conceptually;
- explain test-time/inference-time compute;
- reason about adaptive compute allocation;
- understand why longer reasoning does not guarantee correctness;
- design verification outside the model for consequential tasks.

## 1. What do we mean by reasoning?

"Reasoning" is used loosely in AI discussions. For this roadmap, treat it operationally:

> A system is using reasoning-oriented computation when it performs intermediate inference, decomposition, search, checking or verification intended to improve a final decision on a task that cannot be solved reliably by a single immediate prediction.

This definition avoids making unnecessary claims about whether a model reasons in the same way humans do.

## 2. Direct answer vs intermediate computation

A simple model interaction may look like:

```text
problem
   ↓
model
   ↓
answer
```

A reasoning-oriented interaction may look like:

```text
problem
   ↓
decompose / derive / search
   ↓
intermediate state
   ↓
check / compare / revise
   ↓
answer
```

The intermediate work can happen inside one model call, across multiple calls, through external search, or through deterministic tools.

## 3. Chain-of-thought as a historical inflection point

Wei et al. showed that providing examples containing intermediate reasoning steps could substantially improve performance on several arithmetic, symbolic and commonsense tasks for sufficiently large models.

Primary source: https://arxiv.org/abs/2201.11903

The durable lesson is not that applications should expose private reasoning traces. The durable lesson is:

> Some tasks benefit from allocating intermediate computation rather than forcing an immediate answer.

Production systems should evaluate outcomes, not rely on persuasive-looking reasoning text as proof of correctness.

## 4. Sampling multiple candidates

One way to spend additional inference compute is to produce several candidate solutions and select or aggregate among them.

```text
             ┌→ candidate A ─┐
problem ─────┼→ candidate B ─┼→ select / vote / verify → answer
             └→ candidate C ─┘
```

This can improve robustness on some workloads but multiplies cost and may fail when all candidates share the same misconception.

## 5. Verification

A system can separate generation from checking:

```text
proposer
   ↓
candidate
   ↓
verifier / tests / rules / external evidence
   ↓
accept, revise or reject
```

Verification can be:

- another model;
- the same model under a different prompt/role;
- deterministic code;
- a compiler or test suite;
- a calculator;
- database constraints;
- retrieval from authoritative sources;
- a human reviewer.

The best verifier depends on the task.

For deterministic domains, deterministic verification is usually stronger than asking a model whether its own answer is correct.

## 6. Search over solutions

Instead of producing one linear attempt, systems can explore alternatives and choose among them.

Conceptually:

```text
state
 ├── possible step A → ...
 ├── possible step B → ...
 └── possible step C → ...
            ↓
       scoring/verifier
            ↓
       continue best path(s)
```

This resembles established search/planning ideas. Modern models can generate candidate states or heuristics, while external logic manages the search.

## 7. Test-time compute

Test-time compute means allocating additional computation during inference to improve an answer.

Research has shown that, for some tasks and difficulty regimes, intelligently allocating inference computation can outperform simply using a much larger model under comparable compute constraints.

Primary source:
- Snell et al., **Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters** — https://arxiv.org/abs/2408.03314

This should not be generalised into "small models always beat large models with reasoning." The paper itself emphasises that the effectiveness depends on problem difficulty and inference strategy.

## 8. Adaptive compute is more important than maximum compute

Easy tasks do not need the same computational budget as difficult ones.

A production system might route tasks like:

```text
request
   ↓
difficulty / risk classifier
   ├── low → fast inexpensive path
   ├── medium → stronger model or extra checking
   └── high → search + tools + verifier + possible human approval
```

This is a precursor to model routing and orchestration later in the roadmap.

## 9. Reasoning is not factual grounding

A model can reason carefully from a false premise and produce a coherent but incorrect conclusion.

```text
bad / stale premise
       ↓
high-quality inference
       ↓
wrong conclusion
```

Therefore:

- retrieval supplies evidence;
- reasoning transforms evidence;
- verification checks claims/actions;
- policy determines what is allowed.

These are separate architectural responsibilities.

## 10. Reasoning is not guaranteed reliability

More intermediate computation can still produce:

- repeated hallucination;
- confirmation of an initial mistake;
- unnecessary complexity;
- higher latency;
- higher cost;
- persuasive but invalid explanations;
- verifier failure.

An architecture should allocate more compute only where evaluation shows that it improves the desired outcome.

## 11. Hidden-chain reasoning and system design

Do not make a production system depend on obtaining or storing a model's hidden internal reasoning.

Instead, design around observable artefacts:

- final outputs;
- tool calls;
- cited evidence;
- structured intermediate decisions where intentionally exposed;
- test results;
- verifier scores;
- policy decisions;
- execution traces.

These are auditable system objects. They can be evaluated without assuming a generated explanation faithfully represents internal model cognition.

## 12. Reasoning with tools

Some problems are better solved by handing exact subproblems to tools:

```text
language model
   ├── arithmetic → calculator
   ├── current fact → retrieval/search
   ├── code validity → compiler/tests
   ├── inventory truth → database/API
   └── permission → policy engine
```

A strong system does not ask the model to approximate something a deterministic tool can answer exactly.

## 13. Risk-adjusted inference

The amount of reasoning and verification should correlate not only with difficulty but with consequence.

Example:

```text
low-risk copy suggestion
→ one model pass may be adequate

pricing recommendation
→ evidence + calculation + validation

irreversible financial action
→ deterministic constraints + approval + audit trail
```

The model's confidence is not, by itself, a sufficient risk control.

## 14. Economics

Reasoning-oriented systems can multiply inference cost.

Measure:

```text
base model cost
+ number of candidate generations
+ verifier calls
+ tool calls
+ retrieval
+ latency cost
+ human review cost
--------------------------
= total cost per task
```

Then divide by successful outcomes rather than raw requests.

A more expensive reasoning path can be economically superior if it materially reduces failure or human intervention.

## 15. Practical build

Create a benchmark of at least 30 tasks containing easy, medium and difficult examples.

Compare:

1. direct answer baseline;
2. stronger model baseline;
3. multi-candidate strategy;
4. tool-assisted strategy;
5. proposer + verifier strategy.

Record:

- accuracy/success;
- latency;
- token usage;
- tool calls;
- cost;
- failure category.

Then design a simple router that sends only the harder or higher-risk tasks to the expensive path.

## 16. Failure-analysis exercise

For every failed reasoning task, classify the failure:

```text
knowledge/evidence failure
reasoning failure
tool-selection failure
tool-execution failure
verification failure
instruction failure
policy failure
```

This is much more useful than recording "the model hallucinated."

## 17. Architect's checklist

You should be able to explain:

- direct generation vs reasoning-oriented inference;
- why additional inference compute can help;
- why its value varies by task difficulty;
- candidate sampling, search and verification;
- why generated reasoning text is not proof;
- why deterministic tools are preferable for exact operations;
- how task risk should affect inference budget;
- how to evaluate reasoning economics.

## Primary reading

- Wei et al., **Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** — https://arxiv.org/abs/2201.11903
- Snell et al., **Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters** — https://arxiv.org/abs/2408.03314

## Mastery gate

**Understand:** explain inference-time compute without equating visible reasoning text with guaranteed correctness.

**Build:** benchmark at least three inference strategies on a fixed task set.

**Architect:** implement a risk/difficulty-aware strategy that spends extra compute only where measured value justifies it and uses deterministic verification where possible.
