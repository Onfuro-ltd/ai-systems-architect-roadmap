# Re-ranking

## Purpose

Retrieval systems usually generate a set of possible knowledge candidates. Re-ranking is the process of improving the order of those candidates before they are provided to the language model.

The key idea:

> Retrieval finds possible answers. Re-ranking decides which possibilities deserve attention.

A production RAG system should not assume that the first similarity matches are the most useful results.

---

## Why re-ranking exists

A basic retrieval pipeline often looks like:

```
User query
    |
    v
Embedding search
    |
    v
Top-k documents
    |
    v
LLM
```

This is useful, but similarity is not the same as relevance.

A document can be:

- semantically similar but not answer the question;
- relevant in isolation but missing important context;
- outdated;
- lower priority than another document.

Re-ranking adds an additional relevance judgement layer.

---

## Retrieval versus ranking

### Retrieval

Optimised for recall:

> Find enough possible information that the answer is probably somewhere in the candidates.

### Ranking

Optimised for precision:

> Put the most useful information first.

A common architecture is:

```
Large candidate set
        |
        v
Fast retrieval
        |
        v
Smaller candidate set
        |
        v
More expensive ranking
        |
        v
Final context
```

This balances quality and cost.

---

## Re-ranking approaches

## 1. Vector similarity ranking

The simplest approach.

Advantages:

- fast;
- scalable;
- inexpensive.

Limitations:

- does not deeply compare query and document meaning;
- can miss exact relevance.

---

## 2. Cross-encoder re-ranking

A cross-encoder evaluates the query and document together.

Conceptually:

```
Query + Document
        |
        v
Relevance model
        |
        v
Score
```

Advantages:

- stronger relevance judgement;
- better precision.

Trade-off:

- higher latency and compute cost.

---

## 3. LLM-based re-ranking

A language model can judge candidate relevance.

Advantages:

- flexible;
- can understand complex requirements;
- useful for difficult reasoning tasks.

Limitations:

- expensive;
- slower;
- requires careful evaluation;
- introduces another model dependency.

---

## Multi-stage retrieval architecture

Enterprise systems often use multiple stages:

```
User query
    |
    v
Keyword + Vector Retrieval
    |
    v
Hundreds of candidates
    |
    v
Filtering
    |
    v
Re-ranking
    |
    v
Top documents
    |
    v
Context assembly
    |
    v
Generation
```

The goal is not maximum retrieval. The goal is maximum useful information per unit of context.

---

## Re-ranking trade-offs

Every improvement has costs.

Consider:

- accuracy improvement;
- latency increase;
- infrastructure cost;
- complexity;
- maintenance burden.

A simple question should always be asked:

> Does the improvement create better outcomes worth the additional complexity?

---

## Failure modes

### Correct document ranked too low

Cause:

- poor scoring;
- missing metadata;
- weak query understanding.

### Irrelevant documents ranked highly

Cause:

- superficial similarity;
- outdated information;
- missing business context.

### Too much ranking complexity

Cause:

- adding layers without measuring improvement.

---

## Enterprise considerations

A mature ranking system may consider:

- semantic relevance;
- keyword relevance;
- freshness;
- authority;
- permissions;
- user role;
- document confidence;
- business priority.

Example:

A finance policy approved yesterday may outrank an older general document even if both are semantically similar.

---

## Connection to AI systems architecture

Re-ranking is part of the intelligence layer between knowledge and reasoning:

```
Knowledge Sources
        |
        v
Retrieval
        |
        v
Re-ranking
        |
        v
Context Engineering
        |
        v
AI Reasoning
        |
        v
Validated Outcome
```

It improves the information available to the model without changing the model itself.

---

## Mastery gate

You understand re-ranking when you can:

- explain why similarity is not enough;
- choose between retrieval and ranking strategies;
- measure retrieval improvement;
- understand latency and cost trade-offs;
- design a multi-stage retrieval pipeline;
- identify when added ranking complexity is not justified.
