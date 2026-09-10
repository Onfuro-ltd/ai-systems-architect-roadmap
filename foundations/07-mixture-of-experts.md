# 07 — Mixture of Experts (MoE)

Mixture-of-Experts architectures are important because they break a common intuition: **a model's total parameter count does not necessarily equal the number of parameters used for every token**.

Sparse MoE models can contain many experts while activating only a subset for each token. This can increase capacity without proportionally increasing per-token compute, but it introduces routing, memory, communication and operational complexity.

## Learning outcomes

By the end of this module, you should be able to:

- distinguish dense and sparse models;
- explain experts and routing conceptually;
- distinguish total parameters from active parameters;
- understand capacity, load balancing and routing instability;
- explain why MoE can reduce compute growth while increasing memory/serving complexity;
- reason about when MoE matters to an application architect.

## 1. Dense model intuition

In a conventional dense transformer block, every token passes through the same feed-forward parameters in that layer.

```text
token representation
       ↓
dense feed-forward layer
       ↓
output representation
```

If the dense model grows, more parameters generally participate in every forward pass.

## 2. Sparse experts

A sparse MoE layer replaces one shared feed-forward block with several expert blocks plus a learned router.

```text
                    ┌→ Expert 1 ─┐
token → router ─────┼→ Expert 2 ─┤
                    ├→ Expert 3 ─┤→ combine → output
                    └→ Expert N ─┘
```

The router selects only a small number of experts for each token.

For example, a model may have eight available experts but route each token through two.

## 3. What is an expert?

An expert is usually a learned neural subnetwork — commonly a feed-forward/MLP component — with its own parameters.

Do not assume experts map cleanly to human categories such as:

```text
Expert 1 = maths
Expert 2 = French
Expert 3 = coding
```

Specialisation can emerge, but routing is learned and distributed. Human-readable labels are often an oversimplification.

## 4. Router

The router scores experts for each token and selects one or more.

Conceptually:

```text
token hidden state
      ↓
router scores
      ↓
[expert A: 0.62, expert B: 0.24, expert C: 0.08, ...]
      ↓
select top-k expert(s)
      ↓
process token through those experts
```

The routing mechanism itself becomes part of training and inference behaviour.

## 5. Total parameters vs active parameters

This is the most important concept.

Suppose a sparse model contains:

```text
47B total parameters
13B active parameters per token
```

That does **not** mean the model behaves exactly like a dense 13B model. Nor does it mean inference has the same memory footprint as a 13B model.

Total model weights may still need to be stored or distributed across devices even though only a subset is used for a particular token.

Mixtral 8x7B is a useful historical example. Its paper describes eight feed-forward experts with two selected per token and distinguishes total accessible parameters from active parameters.

Primary source: https://arxiv.org/abs/2401.04088

## 6. Why use MoE?

The broad objective is to increase **model capacity** faster than per-token computation.

```text
Dense scaling:
more capacity → substantially more compute/token

Sparse MoE scaling:
more available capacity
        ↓
activate only part of it/token
        ↓
compute grows more slowly than total parameter count
```

This can improve training/inference efficiency under the right architecture and infrastructure.

## 7. The price of sparsity

MoE does not create free intelligence.

It shifts costs and introduces new problems:

- more model weights to store;
- expert routing overhead;
- communication across accelerators;
- load imbalance;
- difficult batching behaviour;
- expert capacity constraints;
- training instability;
- more complex serving infrastructure.

A sparse model can therefore have attractive FLOP characteristics but still be awkward or expensive to deploy.

## 8. Load balancing

If the router sends too many tokens to a small subset of experts, those experts can become overloaded while others are underused.

```text
bad routing:
Expert A █████████████
Expert B ██
Expert C █
Expert D █
```

Training systems often include load-balancing objectives or constraints to encourage more useful expert utilisation.

This illustrates a general systems principle: **conditional computation requires resource scheduling**.

## 9. Expert capacity

Implementations may limit how many tokens an expert can process in a batch.

If demand exceeds capacity, the system needs a defined behaviour, such as alternate routing or dropping/handling excess assignments depending on the architecture.

This can affect both quality and throughput.

## 10. Communication cost

MoE works especially well when the hardware topology and distributed system can move token representations to the appropriate experts efficiently.

In multi-GPU systems:

```text
token representations
      ↓
router
      ↓
network / interconnect traffic
      ↓
GPU containing selected expert
      ↓
expert computation
      ↓
return / combine
```

Theoretical compute savings can be eroded by communication bottlenecks.

For self-hosting decisions, memory bandwidth and interconnect design may matter as much as advertised parameter count.

## 11. MoE and inference memory

Sparse activation does not mean inactive expert weights disappear.

Deployment may require:

- all expert weights on one large-memory device;
- experts distributed across several devices;
- expert offloading/streaming;
- aggressive quantisation;
- a combination of these.

A model may therefore have low active FLOPs but a large total storage and memory-management burden.

## 12. MoE is not the same as a multi-agent system

These concepts are sometimes confused because both use the word "experts".

```text
Mixture of Experts
= neural architecture inside a model

Multi-agent system
= application/runtime architecture coordinating separate model-driven actors or workflows
```

An MoE expert is not an independent agent with its own goals, tools and memory.

## 13. MoE is not the same as model routing

Model routing chooses among separate models at the system level:

```text
request
  ↓
router
  ├→ cheap model
  ├→ reasoning model
  └→ specialist model
```

MoE routing occurs inside a model, usually at token/layer level.

Both are forms of conditional computation, but at different architectural layers.

## 14. Historical importance

The Switch Transformer demonstrated a simplified sparse expert routing approach and explored training very large sparse models while addressing instability and communication cost.

Primary source:
- Fedus, Zoph & Shazeer, **Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity** — https://arxiv.org/abs/2101.03961

Mixtral later made sparse MoE architecture highly visible in widely used open-weight language models.

Primary source:
- Jiang et al., **Mixtral of Experts** — https://arxiv.org/abs/2401.04088

## 15. How to read MoE marketing claims

When a model is described as "X billion parameters," ask:

```text
How many total parameters?
How many active parameters/token?
How many experts?
How many experts selected/token?
What precision?
What memory footprint?
What hardware topology?
What measured throughput/latency?
What task quality?
```

Without these details, parameter counts can be misleading.

## 16. Application-architecture implications

An application developer using a hosted API may not need to care whether the provider's model is dense or MoE.

An architect **does** need to care when:

- self-hosting;
- estimating GPU memory requirements;
- comparing throughput;
- choosing quantisation;
- planning multi-GPU inference;
- interpreting model-size claims;
- evaluating latency variance or serving economics.

Abstraction is useful until it affects cost, performance or reliability.

## 17. Practical build

Choose one dense open model and one sparse MoE model.

For each, record:

- total parameter count;
- active parameter count if applicable;
- model storage size;
- minimum practical VRAM/RAM under your chosen quantisation;
- tokens/second on comparable hardware if available;
- quality on a small common task suite.

Then write a short explanation of why "parameter count" alone failed to predict deployment behaviour.

Optional advanced experiment: inspect routing statistics from an MoE implementation and measure expert utilisation across different input types.

## 18. Failure modes

### Parameter-count hype
A sparse model is marketed by total parameters without explaining active compute.

### Hardware mismatch
The model is theoretically efficient but performs poorly because device communication is slow.

### Expert imbalance
A small group of experts receives disproportionate traffic.

### Memory surprise
The active parameter count fits expectations, but total weights or cache requirements do not fit hardware.

### Architecture conflation
Teams confuse neural experts with application-level specialist agents.

## 19. Architect's checklist

You should be able to explain:

- dense vs sparse computation;
- experts and routing;
- total vs active parameters;
- load balancing and expert capacity;
- compute savings vs memory/communication costs;
- MoE vs multi-agent orchestration;
- MoE vs system-level model routing.

## Primary reading

- Fedus, Zoph & Shazeer, **Switch Transformers** — https://arxiv.org/abs/2101.03961
- Jiang et al., **Mixtral of Experts** — https://arxiv.org/abs/2401.04088

## Mastery gate

**Understand:** explain why a sparse model can have far more total parameters than active parameters.

**Build:** compare a dense and sparse model using deployment metrics, not only benchmark scores.

**Architect:** make a self-hosting or infrastructure recommendation that accounts for active compute, total model storage, memory, interconnect and expected utilisation.
