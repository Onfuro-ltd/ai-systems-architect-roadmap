# 02 — Embeddings and Semantic Search

## What problem embeddings solve

Computers traditionally search using exact matching.

Example:

A keyword search for:

```text
refund policy
```

may miss:

```text
customer reimbursement rules
```

because the words differ even though the meaning is related.

Embeddings introduce a way to represent meaning numerically.

## What is an embedding?

An embedding is a numerical representation of information produced by a model.

The goal is not to store the original meaning in a human-readable form. The goal is to place related concepts closer together in a mathematical space.

Conceptually:

```text
Meaning
  ↓
Embedding model
  ↓
Vector representation
  ↓
Similarity comparison
```

## Semantic search

Semantic search retrieves information based on meaning rather than only matching words.

Example:

Query:

"How do I return a damaged item?"

May retrieve:

"Product defect replacement procedure"

because the concepts are related.

## Similarity and distance

Systems compare vectors using methods such as:

- cosine similarity;
- dot product;
- Euclidean distance.

The choice depends on the embedding model and system design.

## Embeddings are not understanding

A critical principle:

> A vector representation is a useful retrieval mechanism, not human-like comprehension.

Poor retrieval can still happen because of:

- ambiguous queries;
- bad chunking;
- missing metadata;
- poor source documents;
- domain mismatch.

## Architecture role

Embeddings are one component:

```text
Document
   ↓
Embedding model
   ↓
Vector index
   ↓
Similarity search
   ↓
Retrieved context
   ↓
LLM
```

## Design decisions

A knowledge architect must decide:

- which embedding model fits the domain;
- how documents are segmented;
- whether multilingual support is required;
- how often indexes are updated;
- how retrieval quality is measured.

## Practical lesson

Better embeddings do not automatically create a better AI system. Retrieval quality depends on the complete pipeline: ingestion, metadata, indexing, search, ranking and evaluation.
