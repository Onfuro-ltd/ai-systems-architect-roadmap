# AI Foundations

AI systems architecture starts with a durable mental model of what modern AI systems are actually doing.

This section deliberately avoids beginning with framework tutorials. Tools change quickly. The underlying mechanisms — representation learning, tokenisation, attention, optimisation, inference, scaling, sparsity and multimodality — change much more slowly and determine what systems can and cannot do.

## Learning objective

By the end of Foundations, you should be able to explain a modern foundation model from input to output, reason about its major costs and limitations, and recognise which architectural idea is underneath a new product or research claim.

You do **not** need to become a research mathematician. You do need enough technical depth to make sound architectural decisions.

## Curriculum sequence

1. [AI history and evolution](./01-ai-history-and-evolution.md)
2. [Neural networks to transformers](./02-neural-networks-to-transformers.md)
3. [Transformers and attention](./03-transformers-and-attention.md)
4. [Tokens, context and embeddings](./04-tokens-context-and-embeddings.md)
5. [Training, inference and scaling](./05-training-inference-and-scaling.md)
6. [Reasoning and test-time compute](./06-reasoning-and-test-time-compute.md)
7. [Mixture of Experts](./07-mixture-of-experts.md)
8. [Multimodal foundations](./08-multimodal-foundations.md)
9. [Foundations capstone](./09-foundations-capstone.md)

## The mental model to carry forward

A simplified modern AI pipeline is:

```text
raw data
   ↓
representation / tokenisation
   ↓
model training
   ↓
learned parameters
   ↓
input context
   ↓
forward passes through the model
   ↓
probability distribution over outputs
   ↓
decoding / sampling
   ↓
output
```

For a production AI system, that model sits inside a much larger architecture:

```text
User / System Intent
        ↓
Application Logic
        ↓
Context + Knowledge + Memory
        ↓
Model
        ↓
Tools / Actions
        ↓
Validation + Policy + Evaluation
        ↓
Outcome
```

The rest of this repository focuses on that larger system. Foundations explains the model layer well enough that you do not design everything around misconceptions about it.

## How every foundation topic is studied

Each topic should answer these questions:

### Understand
- What problem led to this idea?
- How does it work conceptually?
- What vocabulary must an architect understand?
- What changed compared with the preceding approach?

### Build
- What small experiment exposes the mechanism?
- What can be measured rather than merely read?
- What behaviour should be inspected directly?

### Architect
- What constraints does this mechanism impose on a real system?
- What are the reliability, latency, cost and scaling implications?
- Which parts belong in application architecture rather than inside the model?

### Lead
- Which claims are durable principles and which are vendor-specific?
- What trade-offs should teams understand before committing to a technology?
- What evidence would justify changing an architectural decision?

## Foundation rules

Do not equate model fluency with factual correctness. Do not equate longer context with perfect memory. Do not equate more parameters with proportionally better outcomes. Do not equate reasoning-style output with guaranteed reasoning correctness. Do not equate an impressive benchmark with production fitness.

These distinctions recur throughout the roadmap.

## Recommended practical environment

Any environment that lets you call at least one language model and inspect token counts, latency, prompts and outputs is sufficient. For some exercises, a small open-weight model running locally is useful because it exposes tokenisation, logits, sampling and inference parameters directly.

Avoid making the curriculum dependent on a single provider SDK. The exercises should remain transferable across commercial and open models.

## Completion standard

Foundations is complete when you can:

- trace the lifecycle from training data to generated output;
- explain attention and transformer architecture at a system-design level;
- reason about tokenisation and context-window constraints;
- distinguish embeddings from generated text representations;
- separate training cost from inference cost;
- explain scaling laws without assuming that "bigger is always better";
- explain test-time compute and its cost/reliability trade-offs;
- explain sparse MoE models and why total parameters differ from active parameters;
- explain how text, image, audio and video can be represented in shared or interacting model systems;
- identify what the model layer should **not** be trusted to enforce.

Proceed to the [Foundations Capstone](./09-foundations-capstone.md) only after completing the practical exercises in the preceding topics.
