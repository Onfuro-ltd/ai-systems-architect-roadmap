# 09 — Foundations Capstone

The Foundations section is not complete when you can repeat terminology. It is complete when you can inspect a model-driven system, explain what is happening at the model layer, measure important trade-offs and avoid architectural mistakes caused by weak mental models.

This capstone turns the previous modules into one integrated exercise.

## Capstone objective

Build and evaluate a small **model comparison laboratory** that makes the foundations observable.

The laboratory should let you compare at least two models or model configurations on the same task set while recording:

```text
input
↓
tokenisation
↓
context construction
↓
model / inference strategy
↓
output
↓
validation
↓
metrics
```

The goal is not to build a polished product. The goal is to create evidence for architectural decisions.

## Required capabilities

Your lab should support:

- at least two models or model configurations;
- token counting or tokenizer inspection where available;
- configurable context size;
- deterministic test cases;
- latency measurement;
- input/output logging with sensitive-data controls;
- success/failure labelling;
- cost estimation where pricing is applicable;
- at least one reasoning-oriented inference strategy;
- at least one multimodal test if supported by the selected models.

## Suggested architecture

```text
                    TEST DATASET
                         |
                         v
                 TASK NORMALISER
                         |
          +--------------+--------------+
          |                             |
          v                             v
   Model / Config A               Model / Config B
          |                             |
          +--------------+--------------+
                         |
                         v
                     VALIDATOR
                         |
                         v
                  METRIC COLLECTOR
                         |
          +--------------+--------------+
          |              |              |
       quality        latency         cost
          |              |              |
          +--------------+--------------+
                         |
                         v
                  DECISION REPORT
```

Keep the evaluator independent from the model where the task allows deterministic checking.

## Part 1 — Build the task set

Create at least 50 tasks spanning several categories.

Recommended categories:

### Factual extraction
Provide controlled source text and require exact fields.

### Structured output
Require a schema with deterministic validation.

### Long-context retrieval
Place critical information at different positions and add irrelevant context.

### Reasoning
Include arithmetic, logical or multi-step tasks with known answers.

### Exact identifiers
Use SKUs, UUID-like strings, codes or numbers to expose tokenisation and copying errors.

### Multilingual input
Use at least two languages if your intended systems are multilingual.

### Multimodal input
Include images or documents where supported.

The dataset should include both easy and difficult tasks and at least a few intentionally unanswerable cases.

## Part 2 — Inspect tokenisation

For representative inputs, record:

```text
characters
words
model/tokenizer
input tokens
```

Compare:

- normal prose;
- structured JSON;
- identifiers;
- non-English text;
- repeated context.

Write a short analysis of what this implies for context limits and cost.

## Part 3 — Measure context behaviour

Run the same tasks under different context conditions:

1. minimum required context;
2. useful context plus irrelevant material;
3. critical evidence near the beginning;
4. critical evidence near the middle;
5. critical evidence near the end.

Measure whether performance changes.

Do not conclude that a model "supports" a context length merely because the API accepts it.

## Part 4 — Compare direct vs additional inference compute

For the reasoning subset, compare at least:

```text
direct response
vs
extra reasoning / candidate generation / verification
```

Where possible, include a deterministic tool-assisted path.

Record whether additional compute actually improves success enough to justify its cost and latency.

## Part 5 — Compare model scale or class

Choose models that differ meaningfully in capability, size, architecture or price.

Record:

| Metric | Model A | Model B |
| --- | --- | --- |
| Task success rate | | |
| Structured output success | | |
| Long-context success | | |
| Reasoning success | | |
| Median latency | | |
| Input tokens | | |
| Output tokens | | |
| Estimated cost | | |
| Cost per successful task | | |

If one model is sparse/MoE, also document total vs active parameters where authoritative information is available.

## Part 6 — Multimodal test

If the models support vision or documents, create several controlled tasks containing:

- clearly visible facts;
- small or ambiguous details;
- one case where the correct answer is "not visible" or "cannot be determined".

Measure unsupported claims as failures.

Compare against a specialist tool where one exists.

## Part 7 — Failure taxonomy

Do not record only "wrong answer".

Classify failures:

```text
tokenisation / representation
context selection
knowledge / grounding
reasoning
instruction following
structured output
visual / audio perception
verification
latency / timeout
cost threshold
unknown / requires investigation
```

This taxonomy will become more detailed later in the Evaluation and Reliability section.

## Part 8 — Produce an Architecture Decision Record

Write a short ADR answering:

### Decision
Which model/configuration should be the default for this workload?

### Context
What tasks and constraints were evaluated?

### Evidence
What results support the decision?

### Trade-offs
What does the chosen option do worse?

### Escalation path
Which requests should be routed to a stronger or more expensive path?

### Verification
Which outputs require deterministic checks or human review?

### Revisit trigger
What new evidence would cause the decision to be reviewed?

## Required outputs

A completed capstone should produce:

```text
capstone/
├── README.md
├── dataset/
├── results/
├── failure-taxonomy.md
├── architecture-decision-record.md
└── reproducibility-notes.md
```

Do not commit secrets, private customer data or proprietary datasets to a public repository.

## Minimum quality bar

Your project should make it possible for another person to reproduce the evaluation or understand exactly why they cannot.

Document:

- model/version where available;
- date of evaluation;
- inference settings;
- test dataset version;
- evaluation rules;
- hardware where locally hosted;
- cost assumptions;
- known limitations.

## Questions you must be able to answer after the capstone

### Model layer
What is learned in parameters, and what is supplied at runtime?

### Transformer layer
What role do attention, position and autoregressive generation play?

### Token layer
Why do tokenisation and context length affect cost and behaviour?

### Scaling layer
Why did the larger model win or lose on your actual tasks?

### Reasoning layer
Where did additional inference compute improve results, and where was it wasteful?

### MoE layer
If applicable, how did total and active parameters affect your deployment assumptions?

### Multimodal layer
Which tasks benefited from a general multimodal model, and which were better handled by specialist tools?

### Systems layer
Which responsibilities must remain outside the model?

## Graduation criteria

You pass Foundations when you can defend all of the following with evidence:

- **I understand the model as a probabilistic component, not an oracle.**
- **I can distinguish training, adaptation and runtime context.**
- **I can measure model choices on representative tasks.**
- **I understand why long context is not memory.**
- **I understand why embeddings are not a permission system or factual database.**
- **I understand why more parameters or more reasoning compute are not automatically better.**
- **I know when deterministic software should constrain or verify model behaviour.**
- **I can explain my model choice in terms of quality, latency, cost, risk and replaceability.**

## What comes next

After completing this capstone, proceed to **AI Application Engineering**.

The next stage moves from understanding model behaviour to building reliable software around models: structured outputs, tool use, retries, state, validation, APIs and deterministic execution boundaries.
