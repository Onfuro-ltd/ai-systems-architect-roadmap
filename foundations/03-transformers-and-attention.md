# 03 — Transformers and Attention

Attention is the mechanism that lets a model dynamically combine information from different positions in its input. The Transformer turned that mechanism into the centre of a scalable architecture.

For an AI systems architect, the goal is not to memorise matrix notation. It is to understand what attention computes, where its costs come from, how context is represented, and which limitations reappear later in retrieval, long-context systems and agent design.

## Learning outcomes

By the end of this module, you should be able to:

- explain queries, keys and values conceptually;
- describe self-attention and causal masking;
- understand positional information and multi-head attention;
- trace a simplified decoder-only transformer forward pass;
- reason about attention complexity and long-context trade-offs;
- understand why attention is not equivalent to memory, search or factual grounding.

## 1. The attention problem

Suppose a model processes:

> The trophy would not fit in the suitcase because it was too large.

To interpret `it`, the representation needs information from elsewhere in the sequence. Attention provides a learned mechanism for deciding which positions should influence one another.

At a conceptual level:

```text
current position asks: "what information is relevant to me?"
                         ↓
compare against other positions
                         ↓
assign relevance weights
                         ↓
combine their information
                         ↓
produce a context-aware representation
```

## 2. Query, key and value intuition

For each token representation, the network derives three learned projections:

- **Query (Q):** what this position is looking for;
- **Key (K):** what this position advertises about itself;
- **Value (V):** the information this position can contribute.

A simplified attention calculation is:

```text
Attention(Q, K, V) = softmax(QKᵀ / √d) V
```

The dot products between queries and keys produce similarity/relevance scores. Softmax converts those scores into a weighted distribution. The weighted values are then combined.

Do not interpret the learned relationships too literally. Attention weights are useful computational signals, but they are not a guaranteed faithful explanation of model reasoning.

## 3. Self-attention

In self-attention, Q, K and V are derived from the same sequence.

```text
sequence representations
   ├──→ Q
   ├──→ K
   └──→ V
          ↓
      attention
          ↓
contextualised sequence
```

Each position can construct a new representation using information from other permitted positions.

## 4. Causal attention

Autoregressive language models must not see future tokens when predicting the next token.

A causal mask enforces this:

```text
position 1 can attend to: 1
position 2 can attend to: 1,2
position 3 can attend to: 1,2,3
position 4 can attend to: 1,2,3,4
```

During training, this mask allows many positions to be processed in parallel while preserving the autoregressive objective.

During generation, output still proceeds token by token because each newly generated token becomes context for the next step.

This distinction helps explain why training parallelism and inference latency behave differently.

## 5. Multi-head attention

A single attention calculation does not need to capture every useful relationship.

Multi-head attention performs multiple learned attention projections in parallel, then combines them.

Conceptually, different heads can become useful for different kinds of relationships, but avoid simplistic claims that a specific head always represents a single human-readable concept.

```text
input
 ├── head 1 attention ──┐
 ├── head 2 attention ──┤
 ├── head 3 attention ──┤→ combine → projection
 └── head N attention ──┘
```

## 6. Position matters

Attention by itself does not automatically encode token order. Transformers therefore inject or derive positional information.

The original Transformer used positional encodings. Modern architectures may use learned positional embeddings, rotary position embeddings (RoPE), relative position methods and other variants.

An architect should understand the consequence: supported context length is not merely an application configuration. It interacts with how the model was trained and how position is represented.

## 7. Feed-forward layers matter too

A Transformer is not "just attention".

Each block also contains token-wise feed-forward transformations, residual connections and normalisation.

A simplified modern decoder block:

```text
hidden state
     ↓
normalisation
     ↓
causal self-attention
     ↓
residual connection
     ↓
normalisation
     ↓
feed-forward / MLP
     ↓
residual connection
     ↓
next block
```

Architecture details vary. Some modern models replace dense feed-forward layers with sparse experts, which is covered in the Mixture-of-Experts module.

## 8. From text to logits

A simplified decoder-only language model forward path is:

```text
text
 ↓
tokeniser
 ↓
token IDs
 ↓
embeddings + positional information
 ↓
transformer blocks × N
 ↓
final hidden representation
 ↓
output projection
 ↓
logits over vocabulary
 ↓
softmax / decoding strategy
 ↓
next token
```

The process repeats until the system stops generation.

This is the mechanism beneath a surprising amount of apparent complexity.

## 9. Why context has a cost

Classic full self-attention compares positions with other positions, leading to quadratic scaling in the attention matrix with sequence length: roughly `O(n²)` in sequence length for that component.

If sequence length doubles, the number of pairwise attention relationships can grow by about four times.

Real-world inference cost is more nuanced because implementations use optimised kernels, KV caching, grouped-query attention, sliding/local attention and other techniques. But the core lesson remains: **long context is not free**.

## 10. KV cache and autoregressive inference

When generating tokens, recomputing keys and values for the entire previous sequence on every step would be wasteful.

Inference systems commonly cache previous key/value representations:

```text
existing context → cached K/V
new token        → compute new K/V
                     ↓
               attend over cache
                     ↓
               generate next token
```

The KV cache improves generation efficiency but consumes memory that grows with sequence length, batch size, layer count and model architecture.

This is one reason long-context serving can become a GPU-memory and concurrency problem even when model weights fit comfortably.

## 11. Attention is not memory

A long context window gives the model access to tokens presented in the current context. That is not the same as durable memory.

```text
Context window = information available to this inference episode
Memory system  = information persisted, selected and retrieved across episodes
```

A system that dumps everything ever seen into an enormous prompt has not solved memory architecture.

It has created a context-management problem.

## 12. Attention is not retrieval

Attention operates over representations already supplied to the model. Retrieval decides **what information should enter the context in the first place**.

```text
large knowledge corpus
       ↓
retrieval system
       ↓
selected evidence
       ↓
model context
       ↓
attention
```

This distinction becomes critical in RAG design.

## 13. Attention is not guaranteed reasoning

Attention enables flexible interaction among representations. It does not guarantee:

- correct logical inference;
- factual grounding;
- faithful explanations;
- consistent arithmetic;
- policy compliance.

Reasoning quality depends on model training, task difficulty, inference strategy, verification and system design.

## 14. Long-context traps

### "It fits" does not mean "it uses everything equally well"

Performance can vary depending on where information appears, how much irrelevant content is present and whether the task requires retrieving distant details.

### More context can make a task worse

Irrelevant or conflicting context can distract the model and increase latency/cost.

### Context windows do not replace databases

Transactional truth, permissions, freshness and structured querying remain external-system responsibilities.

### Context windows do not replace evaluation

A vendor-advertised maximum length does not tell you how your workload performs across that length.

## 15. Practical build — inspect attention-era mechanics

Use a small open transformer implementation or educational notebook.

Perform these experiments:

1. Tokenise a sentence and inspect token IDs.
2. Run a forward pass and inspect output logits.
3. Change one earlier token and compare later predictions.
4. Compare generation latency at several context lengths.
5. If tooling permits, inspect KV-cache memory growth.
6. Test a long document by placing the critical fact near the beginning, middle and end.

Record the results instead of assuming the behaviour.

## 16. Architecture implications

Understanding attention should change real decisions:

- Retrieve relevant evidence rather than injecting entire corpora.
- Budget context length as a cost and latency resource.
- Separate persistent memory from prompt context.
- Benchmark long-context behaviour on your task.
- Treat model attention as internal computation, not an audit trail.
- Keep access-control enforcement outside the model.

## Primary reading

- Vaswani et al., **Attention Is All You Need** — https://arxiv.org/abs/1706.03762
- Devlin et al., **BERT** — https://arxiv.org/abs/1810.04805
- Brown et al., **Language Models are Few-Shot Learners** — https://arxiv.org/abs/2005.14165

## Mastery gate

**Understand:** explain Q/K/V, causal masking, multi-head attention, positional information and the difference among context, memory and retrieval.

**Build:** inspect a transformer forward path and measure at least one context-length effect.

**Architect:** design a context strategy that explicitly separates retrieval, persistent memory and model context, with latency/cost assumptions stated and tested.
