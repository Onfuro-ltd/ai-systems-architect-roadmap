# Vector Databases

## Purpose

Vector databases are an important component in many knowledge systems, but they are not the knowledge system itself.

A common misconception is:

> Add documents to a vector database and the AI becomes knowledgeable.

In reality, a vector database provides a mechanism for storing and searching representations. The quality of the overall system depends on the complete architecture around it.

## The problem they solve

Traditional databases are excellent at exact queries:

- find customer ID 123;
- retrieve order number 456;
- filter products where stock is below 10.

But many AI applications need semantic retrieval:

- find documents about similar concepts;
- locate relevant policies despite different wording;
- retrieve information related to a user's question.

Vector search addresses this by comparing representations rather than only matching keywords.

## How vectors work

An embedding model converts content into a numerical representation:

```text
Document
   |
   v
Embedding model
   |
   v
[0.12, -0.44, 0.91, ...]
```

Content with similar meaning tends to have representations that are closer together in vector space.

## Similarity search

A query follows a similar path:

```text
User question
      |
      v
Query embedding
      |
      v
Similarity search
      |
      v
Relevant candidates
```

Common similarity measures include:

- cosine similarity;
- dot product;
- Euclidean distance.

The correct metric depends on the embedding model and system design.

## Vector database responsibilities

A production vector system typically manages:

- vector storage;
- indexing;
- similarity search;
- metadata filtering;
- namespaces/tenancy;
- updates and deletion;
- access controls;
- operational scaling.

It does not provide:

- truth;
- reasoning;
- business rules;
- permission decisions;
- document quality.

## Metadata is essential

A mature knowledge system stores more than vectors.

Example:

```json
{
  "document": "amazon_policy.pdf",
  "section": "returns",
  "tenant": "company_a",
  "created": "2026-01-01",
  "permission": "operations"
}
```

Metadata enables:

- filtering;
- security boundaries;
- freshness management;
- better retrieval.

## Hybrid search

Pure vector search is not always enough.

Many production systems combine:

```text
Semantic search
       +
Keyword search
       +
Metadata filters
       +
Ranking
```

This is often called hybrid retrieval.

## Scaling considerations

Important architectural decisions:

### Data volume

Small internal knowledge bases and internet-scale search systems require different approaches.

### Update frequency

A legal policy updated daily has different requirements from archived documents.

### Latency

Retrieval speed affects user experience and agent workflows.

### Cost

Storage, indexing and query volume all contribute to operating cost.

## Common mistakes

### Mistake 1: Putting everything into embeddings

Not all data requires semantic search.

Structured data often belongs in:

- relational databases;
- analytics systems;
- operational APIs.

### Mistake 2: Ignoring metadata

Without metadata, retrieval becomes difficult to control.

### Mistake 3: Assuming top results are correct

Retrieval requires evaluation.

Similarity does not equal truth.

## Enterprise architecture pattern

A mature system often looks like:

```text
Source Systems
      |
      v
Document Processing
      |
      v
Embedding Pipeline
      |
      v
Vector Index
      |
      v
Retriever
      |
      v
Ranking
      |
      v
Context Assembly
      |
      v
AI Application
```

## Connection to AI Operating Systems

Vector databases are one layer of a larger intelligence architecture:

```text
Knowledge Sources
       |
       v
Knowledge Layer
       |
       v
Retrieval
       |
       v
AI Reasoning
       |
       v
Validated Action
```

The durable capability is not owning a vector database. It is owning a reliable knowledge lifecycle.

## Mastery gate

You understand vector databases when you can:

- explain when vector search is appropriate and when it is not;
- design metadata and permission strategies;
- compare semantic, keyword and hybrid retrieval;
- diagnose poor retrieval quality;
- explain why embeddings do not equal knowledge;
- design an evaluation approach for retrieval quality.
