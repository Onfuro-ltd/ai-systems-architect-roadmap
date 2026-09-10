# Hybrid Search

## Why Hybrid Search Exists

Semantic search is powerful, but it is not sufficient for enterprise knowledge systems.

A mature retrieval system usually combines:

- semantic understanding;
- exact matching;
- structured filtering;
- ranking intelligence.

Hybrid search combines different retrieval approaches to improve reliability.

## The limitation of pure approaches

### Pure keyword search

Traditional search is strong at:

- exact terms;
- identifiers;
- product codes;
- legal references;
- technical names.

Example:

`ASIN B0ABC123`

or:

`VAT Article 39`

However, it struggles when the user expresses meaning differently from the source material.

### Pure vector search

Semantic retrieval is strong at:

- concepts;
- paraphrases;
- related ideas;
- natural language questions.

However, it can struggle with:

- exact identifiers;
- numbers;
- codes;
- rare terms;
- highly specific references.

## Hybrid architecture

A production retrieval system combines multiple signals:

```text
                    User Query
                         |
          +--------------+--------------+
          |                             |
          v                             v
   Keyword Retrieval            Semantic Retrieval
          |                             |
          +--------------+--------------+
                         |
                         v
                  Result Fusion
                         |
                         v
                    Re-ranking
                         |
                         v
                Context Selection
                         |
                         v
                       LLM
```

## Retrieval signals

### Lexical matching

Uses exact terms and token relationships.

Useful for:

- SKUs;
- names;
- regulations;
- error messages;
- technical identifiers.

### Semantic matching

Uses embeddings to identify conceptual similarity.

Useful for:

- questions;
- explanations;
- knowledge discovery;
- related concepts.

### Metadata filtering

Adds deterministic constraints.

Examples:

- tenant;
- department;
- document type;
- date range;
- access permissions.

## Why enterprise systems need hybrid retrieval

Real business questions often contain both meaning and precision.

Example:

> "Why did ASIN B09XYZ returns increase after the supplier change?"

The system needs:

Exact matching:
- ASIN;
- supplier name;
- dates.

Semantic understanding:
- returns increase;
- quality problems;
- customer complaints.

Business filtering:
- correct company;
- authorised user;
- relevant timeframe.

## Ranking and fusion

Combining retrieval methods creates another challenge: results need to be ranked.

Common approaches include:

- weighted scoring;
- reciprocal rank fusion;
- learning-to-rank methods;
- neural re-rankers.

The correct choice depends on:

- data volume;
- latency requirements;
- accuracy requirements;
- operational complexity.

## Common mistakes

### Mistake 1: Assuming vector search replaces databases

Operational data should usually remain in operational systems.

Examples:

Keep in databases:

- current inventory;
- account balances;
- order status.

Use retrieval systems for:

- policies;
- explanations;
- documentation;
- historical knowledge.

### Mistake 2: Ignoring metadata

A highly relevant document is still wrong if the user is not allowed to access it.

### Mistake 3: Optimising retrieval without measuring outcomes

Better retrieval does not automatically mean better answers.

Evaluate the complete chain:

```text
Retrieval quality
        +
Context quality
        +
Generation quality
        +
Business outcome
```

## Enterprise design principle

Hybrid search is not about adding more search technologies. It is about combining complementary signals so the system can find the right knowledge with confidence.

The goal is not maximum retrieved information.

The goal is the smallest amount of highest-quality information required for a reliable decision.

## Mastery Gate

A learner should be able to:

- explain when semantic search is insufficient;
- design a hybrid retrieval architecture;
- choose appropriate retrieval signals;
- understand the trade-offs between recall, precision, latency and cost;
- evaluate retrieval quality independently from answer quality;
- design permission-aware retrieval for enterprise environments.
