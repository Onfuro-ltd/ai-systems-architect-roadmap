# 04 — Tokens, Context and Embeddings

Many AI architecture mistakes begin with three words that are used casually but mean very different things: **tokens**, **context** and **embeddings**.

Tokens are the units a model processes. Context is the information available to a particular inference run. Embeddings are learned numerical representations used to encode meaning or similarity. They interact, but they are not interchangeable.

## Learning outcomes

By the end of this module, you should be able to:

- explain why language models operate on tokens rather than raw words;
- understand subword tokenisation and vocabulary trade-offs;
- distinguish context-window capacity from usable information quality;
- explain embeddings and vector similarity;
- distinguish token embeddings, hidden states and retrieval embeddings;
- reason about context cost, truncation, chunking and retrieval design;
- identify multilingual and domain-specific tokenisation issues.

## 1. Why tokenisation exists

Neural networks operate on numbers, not raw text. A tokenizer converts text into discrete IDs from a vocabulary.

```text
"AI systems are useful"
          ↓
tokeniser
          ↓
[token_id_1, token_id_2, ...]
          ↓
embedding lookup
          ↓
vectors processed by the model
```

Using whole words creates an enormous vocabulary and fails on unseen words. Using individual characters produces much longer sequences. Subword tokenisation provides a practical compromise.

## 2. Subword tokenisation

Methods such as Byte Pair Encoding (BPE), WordPiece, Unigram and byte-level schemes break text into reusable units smaller than or equal to words.

A word might become:

```text
"tokenisation"
→ "token" + "isation"
```

Another tokenizer may split the same text differently.

The exact segmentation is model-specific.

A historically important reference for subword use in neural machine translation is:

- Sennrich, Haddow & Birch, **Neural Machine Translation of Rare Words with Subword Units** — https://arxiv.org/abs/1508.07909

## 3. Tokenisation is an architectural concern

Tokenisation affects:

- API cost when pricing is token-based;
- effective context-window usage;
- latency;
- multilingual efficiency;
- code representation;
- unusual identifiers and SKUs;
- log and JSON processing;
- chunking for retrieval;
- maximum output sizes.

A system that stores or processes multilingual content should not assume that "one word ≈ one token" across languages.

Likewise, product codes, URLs, UUIDs, source code and dense structured data can tokenize inefficiently.

## 4. Context window

A model's context window is the bounded sequence of tokens that can influence a particular inference operation.

It can contain:

```text
system instructions
+ developer/application instructions
+ conversation history
+ retrieved documents
+ memory snippets
+ tool results
+ user input
+ model output under generation
```

The exact accounting depends on the provider and model.

The core point is that context is a **scarce runtime resource**.

## 5. Maximum context is not effective context

A model advertising a large maximum context window does not imply that:

- every token receives equal practical attention;
- every fact will be recalled reliably;
- irrelevant material has no cost;
- latency stays constant;
- output quality improves monotonically;
- the full window is economical for every request.

Architects should distinguish:

```text
maximum supported context
        ≠
effective task context
        ≠
optimal economical context
```

## 6. Context budgeting

A production request should have an intentional token budget.

Example:

```text
Total context allowance
│
├── system/policy instructions
├── task instructions
├── conversation state
├── retrieved evidence
├── tool responses
└── reserve for model output
```

Without budgeting, systems eventually fail through truncation, excessive latency, high cost or noisy prompts.

Good context engineering is selective, not accumulative.

## 7. What is an embedding?

An embedding is a vector: an ordered list of numbers learned so that useful relationships are represented geometrically.

Conceptually:

```text
"refund policy" → [0.14, -0.82, 0.31, ...]
"returns rules" → [0.12, -0.79, 0.35, ...]
```

Semantically related inputs may lie closer together in the embedding space than unrelated inputs.

The exact dimensions do not have simple independent meanings such as "dimension 14 = refunds". Meaning is distributed across the representation.

## 8. Similarity search

Retrieval systems often compare an input embedding with stored document embeddings.

A common measure is cosine similarity:

```text
similarity(a, b) = (a · b) / (||a|| ||b||)
```

A simplified retrieval flow:

```text
user query
   ↓
query embedding
   ↓
vector similarity search
   ↓
nearest chunks
   ↓
optional filtering/reranking
   ↓
selected evidence
```

This is useful but not magical. Semantic similarity is not the same as factual relevance, permission eligibility or business priority.

## 9. Three different concepts commonly called embeddings

### Token embeddings

Map discrete token IDs into continuous vectors at the model input.

### Hidden representations

Intermediate vectors produced inside model layers. These change as context is processed.

### Retrieval embeddings

Vectors intentionally produced for search, clustering or semantic comparison.

Do not assume that a generative model's internal token representation is directly equivalent to a purpose-built retrieval embedding model.

## 10. Embeddings are not a database

A vector index is often used alongside a database, not instead of one.

Use vector similarity for questions such as:

> Which documents are semantically related to this query?

Use deterministic database filtering for questions such as:

> Which orders belong to tenant X, are unpaid, and were created after date Y?

A robust architecture often combines them:

```text
query
  ↓
identity + permission filters
  ↓
metadata constraints
  ↓
semantic retrieval
  ↓
reranking
  ↓
model context
```

## 11. Chunking is a retrieval design decision

Documents are commonly split into chunks before embedding.

Chunks that are too small may lose necessary context. Chunks that are too large may contain irrelevant information and reduce retrieval precision.

Chunking can be based on:

- fixed token windows;
- paragraphs;
- headings/sections;
- semantic boundaries;
- document structure;
- domain-specific units.

There is no universal best chunk size. Measure retrieval quality on representative questions.

## 12. Context vs RAG vs memory

These three should be kept distinct:

```text
Context
= information currently visible to the model

RAG
= mechanism for finding external information and inserting selected evidence into context

Memory
= persisted information from previous interactions/events that can later be selected and reintroduced
```

A memory item ultimately has to enter current context — directly or through another computational mechanism — to influence the model's response.

## 13. Failure modes

### Token explosion
Structured data, logs or unfamiliar languages consume far more tokens than expected.

### Silent truncation
Important instructions or evidence fall outside the accepted context.

### Context dilution
Too much irrelevant information reduces effective performance.

### Embedding mismatch
The embedding model does not represent the domain or query type well enough.

### Similar-but-wrong retrieval
A semantically similar chunk is not the factually relevant one.

### Stale vectors
Source content changes but embeddings are not regenerated.

### Permission leakage
A vector search retrieves content the current user should not be allowed to access.

The last failure is especially important: semantic retrieval must not replace authorization.

## 14. Security and privacy implications

Embedding vectors are transformed representations, not automatically anonymous data.

Treat them as potentially sensitive when they are derived from sensitive source content.

A production retrieval system should define:

- tenant and user access boundaries;
- deletion propagation;
- source-document provenance;
- re-embedding/versioning strategy;
- data residency where applicable;
- logging rules;
- whether external embedding APIs are permitted for the data class.

## 15. Economics

Token and context decisions directly affect operating cost.

For each workload, measure:

```text
input tokens/request
output tokens/request
retrieval tokens added
cache hit rate
latency
cost/request
cost/successful task
```

An expensive long prompt may still be economical if it dramatically improves task success. Conversely, a cheap model with massive unnecessary context may cost more than a stronger model supplied with carefully selected evidence.

Optimise the **whole system**, not token price in isolation.

## 16. Practical build

### Experiment A — tokenizer comparison

Run the same inputs through at least two model tokenizers:

- plain English prose;
- another language;
- JSON;
- source code;
- URLs;
- product/SKU identifiers.

Measure token counts and explain the differences.

### Experiment B — context budgeting

Construct the same task with:

1. minimal relevant context;
2. relevant context plus noise;
3. a long raw document;
4. retrieved evidence only.

Compare accuracy, latency and tokens used.

### Experiment C — embedding retrieval

Create a small corpus, embed it, then test:

- semantic paraphrases;
- exact identifiers;
- negated questions;
- ambiguous terms;
- metadata filters.

Record where vector similarity works and where deterministic search or reranking is needed.

## 17. Architect's checklist

You should be able to explain:

- why models need tokenisation;
- why token counts vary across inputs and models;
- why context is a runtime budget;
- why longer context is not equivalent to better memory;
- how embeddings enable semantic retrieval;
- why vector similarity is not authorization or factual verification;
- how chunking affects retrieval;
- why context cost must be evaluated at the task level.

## Primary reading

- Sennrich, Haddow & Birch, **Neural Machine Translation of Rare Words with Subword Units** — https://arxiv.org/abs/1508.07909
- Vaswani et al., **Attention Is All You Need** — https://arxiv.org/abs/1706.03762
- Lewis et al., **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks** — https://arxiv.org/abs/2005.11401

## Mastery gate

**Understand:** distinguish tokens, token embeddings, retrieval embeddings, context, RAG and memory without conflating them.

**Build:** compare tokenisers, construct a context budget and implement a small semantic retrieval experiment.

**Architect:** design a permission-aware context/retrieval architecture with explicit cost, truncation, freshness and evaluation strategies.
