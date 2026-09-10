# 02 — Neural Networks to Transformers

Modern foundation models are neural networks. You do not need to derive every optimisation equation to architect AI systems, but you do need a correct mental model of what a neural network learns, how information flows through it, and why transformer architectures displaced many earlier sequence models.

## Learning outcomes

By the end of this module, you should be able to:

- explain parameters, layers, activations, loss and gradient-based learning;
- distinguish training from inference;
- explain why learned representations are powerful;
- describe the limitations of recurrent sequence models;
- explain why attention and transformers changed scaling economics;
- recognise where neural networks remain probabilistic and where deterministic controls must sit outside them.

## 1. A neural network is a parameterised function

At the simplest useful level, a neural network transforms inputs into outputs using many learned numerical parameters.

```text
input
  ↓
linear transformation
  ↓
non-linearity
  ↓
more transformations
  ↓
output
```

A layer commonly computes something conceptually like:

```text
y = activation(Wx + b)
```

Where:
- `x` is the input representation;
- `W` and `b` are learned parameters;
- the activation introduces non-linearity;
- deeper networks repeatedly transform representations.

The important architectural point is that the behaviour is **learned from optimisation**, not encoded as a transparent set of business rules.

## 2. Training: learning parameters

Training repeatedly compares model predictions with a target objective, calculates error and adjusts parameters to reduce that error.

```text
training example
     ↓
forward pass
     ↓
prediction
     ↓
loss function
     ↓
backpropagation
     ↓
gradient-based parameter update
     ↓
repeat at scale
```

Three terms matter:

### Loss
A numerical objective representing how wrong the model is under the training objective.

### Gradient
Information about how changing each parameter would affect the loss.

### Optimiser
The algorithm that uses gradients to update parameters.

A model does not generally store a human-readable database of facts. Training produces distributed statistical structure across many parameters.

## 3. Representations

One of deep learning's most important ideas is representation learning.

Instead of hand-coding every useful feature, the network learns internal representations that make the training objective easier to solve.

In language, early layers may encode local or lexical patterns while later transformations can represent increasingly contextual relationships. These internal representations are not guaranteed to map cleanly to human concepts.

This matters because:

- knowledge can be distributed rather than stored in one identifiable location;
- editing one behaviour may affect others;
- explanations derived from outputs are not necessarily faithful descriptions of internal computation;
- model weights are a poor substitute for a transactional or current knowledge store.

## 4. Why depth matters

Multiple layers allow a system to build transformations on top of earlier transformations.

A shallow model may learn relatively direct correlations. A deep network can construct more abstract features and interactions.

But depth creates engineering challenges:

- optimisation instability;
- vanishing/exploding gradients in older architectures;
- memory and compute cost;
- difficult interpretability;
- sensitivity to data and training configuration.

Techniques such as residual connections, normalisation and improved optimisers made increasingly deep models practical.

## 5. Sequence modelling before transformers

Language is sequential. Earlier neural approaches often used recurrent neural networks (RNNs) and variants such as LSTMs.

A simplified recurrent model processes one step after another:

```text
token 1 → state 1
             ↓
token 2 → state 2
             ↓
token 3 → state 3
             ↓
           ...
```

The hidden state carries information forward.

This has intuitive advantages, but long sequential dependency chains create problems:

- training is difficult to parallelise across sequence positions;
- long-range information can degrade;
- long sequences increase sequential compute latency;
- a fixed hidden-state pathway can become a bottleneck.

LSTMs and GRUs improved long-range learning but did not remove the basic sequential dependency.

## 6. Attention changes the information path

Attention allows a representation at one position to directly weigh and combine information from other positions.

Instead of forcing all useful context through a long recurrent chain:

```text
token A ───────────┐
token B ───────┐   │
token C ───┐   │   │
           ↓   ↓   ↓
        attention
           ↓
context-aware representation
```

The key concept is **content-dependent routing of information**.

The model learns which other positions are relevant to the current computation.

## 7. The Transformer shift

The 2017 Transformer architecture made attention the central mechanism and removed recurrence from the core sequence-processing architecture.

Primary source: https://arxiv.org/abs/1706.03762

A simplified transformer block contains:

```text
input representations
        ↓
self-attention
        ↓
residual + normalisation
        ↓
feed-forward network
        ↓
residual + normalisation
        ↓
next block
```

Modern implementations vary significantly, but this abstraction remains useful.

## 8. Why transformers scaled so well

### Parallel training

Unlike recurrent processing, token positions can be processed substantially in parallel during training.

### Flexible long-range interaction

Attention creates direct information paths between positions rather than requiring information to pass step-by-step through the sequence.

### Hardware fit

Transformer computation maps well onto large matrix operations, which accelerators such as GPUs and TPUs execute efficiently.

### Architectural reuse

The same broad architecture can support text, images, audio, video and combinations of modalities after adapting input representations and objectives.

## 9. Encoder, decoder and encoder-decoder families

The original Transformer included both encoder and decoder stacks.

### Encoder-only

Designed to produce contextual representations of an input. BERT is the canonical historical example.

Useful historically for classification, retrieval representations and language understanding tasks.

Primary source: https://arxiv.org/abs/1810.04805

### Decoder-only

Autoregressively predicts the next token from previous context. GPT-style large language models popularised this architecture for general generative systems.

### Encoder-decoder

An encoder represents an input while a decoder generates an output conditioned on that representation. This remains useful for sequence-to-sequence tasks.

Do not assume one family is universally superior; the correct choice depends on training objective and product requirements.

## 10. Training objective vs apparent intelligence

A typical autoregressive language model is trained around next-token prediction:

```text
context tokens
      ↓
model
      ↓
probability distribution for next token
```

Repeated next-token prediction can yield surprisingly broad capabilities because accurately modelling language at scale requires learning extensive statistical structure.

But this objective has architectural consequences:

- fluent output is directly rewarded by the modelling objective;
- factual correctness is not guaranteed;
- calibrated uncertainty is not guaranteed;
- compliance with external business rules is not guaranteed;
- the model can generate plausible sequences that are operationally wrong.

Therefore, production systems require validation and external controls.

## 11. Deterministic boundaries around probabilistic models

A critical systems principle is:

```text
Probabilistic intelligence
        inside
Deterministic boundaries
```

Examples:

The model may recommend a refund, but a policy service should validate eligibility.

The model may generate a database query, but a permission layer should determine what it is allowed to access.

The model may classify an action as safe, but consequential actions should not depend solely on model self-assessment.

This principle becomes increasingly important as systems gain tools and autonomy.

## 12. Failure modes to understand

### Distribution shift
The world at deployment differs from training data.

### Spurious correlations
The model learns a shortcut that works in training but fails in another environment.

### Overfitting
The model fits training patterns without generalising adequately.

### Miscalibration
Confidence implied by output language may not correspond to actual correctness probability.

### Opaque failure
A neural model can return a plausible output without exposing an obvious internal error signal.

### Objective mismatch
The training objective may reward behaviour that differs from the user's real-world objective.

These are system-design problems, not just model-research problems.

## 13. Practical build

Implement or inspect a very small neural network before using a large model abstraction.

Suggested experiment:

1. Train a small classifier on a simple dataset.
2. Record training loss and validation loss.
3. Intentionally overfit it.
4. Change the data distribution and measure degradation.
5. Compare model confidence with actual correctness.

Then inspect a tiny transformer implementation and trace:

```text
tokens → embeddings → attention → feed-forward → logits
```

The goal is not production performance. It is to remove the "black magic" mental model.

## 14. Architect's checklist

You should be able to explain:

- what model parameters represent;
- why training and inference are fundamentally different workloads;
- why representation learning matters;
- why recurrent architectures were difficult to scale;
- what attention changes about information flow;
- why transformer computation benefits from parallel accelerators;
- why next-token prediction can produce fluent but wrong answers;
- why critical controls must live outside model weights.

## Primary reading

- Vaswani et al., **Attention Is All You Need** — https://arxiv.org/abs/1706.03762
- Devlin et al., **BERT** — https://arxiv.org/abs/1810.04805
- Brown et al., **Language Models are Few-Shot Learners** — https://arxiv.org/abs/2005.14165

## Mastery gate

**Understand:** explain a transformer as a learned parameterised system without describing it as a database or rules engine.

**Build:** train a small neural model and inspect a small transformer forward path.

**Architect:** identify which responsibilities in a proposed AI product belong outside the neural model and justify the deterministic boundaries.
