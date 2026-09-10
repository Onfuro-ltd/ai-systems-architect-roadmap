# 05 — Training, Inference and Scaling

A production AI architect must separate two very different economic and technical problems: **training a model** and **running a trained model**.

Confusing them leads to poor decisions about fine-tuning, self-hosting, GPU requirements, latency and cost.

## Learning outcomes

By the end of this module, you should be able to:

- distinguish pre-training, post-training, fine-tuning and inference;
- explain the basic compute/data/model-size trade-off;
- understand what scaling laws do and do not imply;
- explain prefill vs autoregressive decode at inference time;
- reason about latency, throughput, memory and utilisation;
- understand why model size alone is a weak architecture-selection criterion;
- compare API inference, rented GPUs and owned hardware at a conceptual level.

## 1. The lifecycle of a modern model

A simplified lifecycle is:

```text
raw data
  ↓
collection / filtering / deduplication
  ↓
tokenisation
  ↓
pre-training
  ↓
base model
  ↓
post-training / instruction tuning / preference optimisation
  ↓
deployable model
  ↓
inference
  ↓
application feedback + evaluation
```

Different providers use different recipes, and many frontier training details are proprietary. The architecture-level distinction is still useful.

## 2. Pre-training

Pre-training exposes a model to a very large corpus under a general objective such as next-token prediction.

For autoregressive language modelling:

```text
previous tokens
      ↓
model
      ↓
predict probability of next token
```

Repeated over enormous numbers of examples, the model learns broad statistical structure.

Pre-training is capital-intensive because it combines:

- large datasets;
- many optimisation steps;
- large accelerator clusters;
- high memory bandwidth;
- distributed training;
- checkpointing and fault recovery;
- extensive data and systems engineering.

For most application teams, training a frontier model from scratch is not economically rational.

## 3. Post-training

A raw pre-trained model may be capable but poorly suited to user interaction.

Post-training can improve instruction following, safety behaviour, domain performance and output preferences.

Common families include:

- supervised fine-tuning (SFT);
- preference optimisation;
- reinforcement-learning-based alignment;
- distillation;
- domain adaptation.

The detailed techniques belong later in the roadmap. The foundation principle is:

> The behaviour users experience is a product of both pre-training and post-training.

Two models with similar base architectures can behave very differently after post-training.

## 4. Fine-tuning is not the same as giving a model knowledge at runtime

Fine-tuning changes model parameters.

Retrieval supplies information at inference time.

```text
Fine-tuning:
training examples → parameter updates → changed model behaviour

Retrieval:
query → external search → evidence → context → current answer
```

Fine-tuning is usually better suited to repeated behaviour, style, task patterns or specialist capabilities than to rapidly changing factual knowledge.

Use later evaluation modules to decide empirically.

## 5. Inference

Inference uses the trained parameters to process new inputs and generate outputs.

No general gradient-based parameter update is required for ordinary inference.

For autoregressive generation:

```text
input context
    ↓
prefill
    ↓
first next-token distribution
    ↓
choose token
    ↓
decode next token
    ↓
repeat
```

### Prefill

The model processes the supplied input/context and constructs internal state, including data used for KV caching.

Long prompts can make prefill expensive.

### Decode

The model generates new tokens sequentially. Each new token depends on previous output.

This sequential dependency makes generation latency behave differently from bulk parallel training.

## 6. Latency vs throughput

These are different objectives.

### Latency

How long one request waits for useful output.

Useful metrics include:

- time to first token;
- inter-token latency;
- total task duration.

### Throughput

How much work a system completes over time.

Useful metrics include:

- tokens/second;
- requests/second;
- successful tasks/hour.

Batching may improve throughput while hurting individual-request latency. Architecture choices depend on workload.

## 7. Memory matters as much as raw compute

Inference performance depends on more than theoretical FLOPs.

Important constraints include:

- model-weight memory;
- KV-cache memory;
- memory bandwidth;
- activation memory;
- batch size;
- precision/quantisation;
- inter-GPU communication;
- sequence length.

This is why two GPUs with similar headline compute can behave differently for LLM workloads.

## 8. Scaling laws

Scaling-law research found empirical relationships between model performance and resources such as parameter count, dataset size and training compute.

Kaplan et al. documented power-law relationships across broad ranges of model/data/compute scale.

Primary source: https://arxiv.org/abs/2001.08361

A crucial lesson is not "make the model as large as possible". It is that performance and resource allocation can exhibit predictable structure.

## 9. Compute-optimal training

Hoffmann et al. (Chinchilla) challenged the practice of increasing model size while leaving training data relatively under-scaled. Their experiments suggested that, under the studied compute budgets, parameter count and training-token volume should be balanced more aggressively than in several preceding large models.

Primary source: https://arxiv.org/abs/2203.15556

Architecture lesson:

```text
parameter count alone
        ≠
training quality
        ≠
capability
        ≠
economic efficiency
```

A smaller, better-trained model can outperform a larger but undertrained one on important workloads.

## 10. Scaling is multidimensional

Modern system performance can be improved by scaling different resources:

```text
more / better training data
more model parameters
more training compute
better architecture
better post-training
longer / better selected context
more inference-time compute
external tools
retrieval
specialist models
```

The economically optimal choice may not be increasing the base model.

## 11. Model size is not a procurement strategy

When selecting a model, measure task-level characteristics such as:

- success rate;
- latency;
- cost per successful task;
- instruction adherence;
- tool-use accuracy;
- structured-output reliability;
- context behaviour;
- safety;
- language/domain performance.

A 10× larger model that improves success by 1% may be wasteful for one task and essential for another.

## 12. API vs rented GPU vs owned hardware

### Hosted API

Advantages:
- low setup overhead;
- elastic capacity;
- access to frontier models;
- provider handles serving infrastructure.

Trade-offs:
- recurring usage cost;
- provider dependence;
- data-governance constraints;
- less control over internals.

### Rented GPU infrastructure

Advantages:
- more model/control flexibility;
- pay for compute when needed;
- good for experimentation and bursty workloads.

Trade-offs:
- operational work;
- storage/transfer cost;
- utilisation risk;
- infrastructure variability.

### Owned hardware

Advantages:
- predictable local capacity;
- privacy/control;
- potentially favourable economics under sustained utilisation.

Trade-offs:
- capital expense;
- depreciation;
- power/cooling;
- hardware failure;
- capacity becomes fixed;
- operations burden.

The correct answer is workload-dependent and often hybrid.

## 13. Quantisation

Model weights can often be represented with reduced numerical precision to reduce memory and improve serving practicality.

Conceptually:

```text
higher precision
→ more memory / potentially higher fidelity

lower precision / quantised
→ less memory / often faster or cheaper
→ possible quality trade-off
```

Quantisation is not universally free. Test the exact model and workload.

## 14. Caching and reuse

Inference economics can change materially when work is reused.

Examples include:

- prompt/prefix caching;
- KV-cache reuse within generation;
- semantic/application caches;
- cached tool results;
- precomputed embeddings.

Caching should preserve correctness boundaries. Stale answers, tenant leakage and policy changes can make an otherwise efficient cache unsafe.

## 15. Failure modes

### Underutilised accelerators
Expensive GPUs spend substantial time idle.

### Out-of-memory failures
Weights fit, but long contexts, batching or KV cache exceed capacity.

### Cost blindness
Teams optimise per-token price instead of cost per completed business outcome.

### Benchmark procurement
A model is selected because it leads a public benchmark but performs poorly on internal tasks.

### Fine-tuning before baseline evaluation
Teams pay for training before testing prompt, retrieval or workflow improvements.

### Scaling complexity instead of capability
More GPUs, parameters or agents are added when the bottleneck is poor data or process design.

## 16. Practical build

Choose at least two models of different sizes or serving classes and run the same test set.

Record:

```text
model
input tokens
output tokens
latency
success/failure
estimated cost
cost per successful task
```

Then vary context length and, where possible, batching.

The objective is to observe that the "best model" changes depending on the optimisation target.

## 17. Architect's checklist

You should be able to explain:

- pre-training vs post-training vs inference;
- why fine-tuning differs from retrieval;
- prefill vs decode;
- latency vs throughput;
- why VRAM and memory bandwidth matter;
- what scaling laws actually establish;
- why parameter count is insufficient for model selection;
- how to compare hosted and self-hosted inference economically.

## Primary reading

- Kaplan et al., **Scaling Laws for Neural Language Models** — https://arxiv.org/abs/2001.08361
- Hoffmann et al., **Training Compute-Optimal Large Language Models** — https://arxiv.org/abs/2203.15556
- Brown et al., **Language Models are Few-Shot Learners** — https://arxiv.org/abs/2005.14165

## Mastery gate

**Understand:** describe the complete lifecycle from data to deployed inference and explain the major resource constraints.

**Build:** benchmark at least two model/serving choices using task success, latency and cost.

**Architect:** produce a short deployment decision showing why a workload should use hosted APIs, rented compute, owned compute or a hybrid — with assumptions that can later be tested.
