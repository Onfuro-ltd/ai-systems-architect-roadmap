# Domain 04 — Knowledge Systems and RAG

## Learning objectives

By the end of this domain, you should be able to:

- explain the core concepts and distinctions across retrieval, chunking, ranking, hybrid search, grounding, citations, knowledge freshness, access control and retrieval evaluation.
- build or evaluate a representative implementation rather than relying on a demo;
- make architecture decisions that account for reliability, security, cost, scale and operations;
- define the evidence, evaluation and governance required before production adoption.

## Mission

Knowledge Systems teach how AI applications access, retrieve, verify and use information beyond the model's internal training data.

A foundation model provides general intelligence. A knowledge system provides the relevant, current and permission-aware information required to make useful decisions.

The goal is not to make AI know everything. The goal is to build systems that know what information is available, where it came from, whether it is trustworthy and when it should be used.

## Core principle

> A model's intelligence is limited by both its reasoning ability and the quality of the information environment it receives.

## Why this matters

Without a knowledge layer, AI systems struggle with:

- private company information;
- changing data;
- domain-specific knowledge;
- citations and provenance;
- access control;
- organisational memory.

Knowledge systems solve the connection between intelligence and trusted information.

## Learning path

```text
Information sources
        ↓
Document processing
        ↓
Chunking and representation
        ↓
Embeddings
        ↓
Retrieval
        ↓
Ranking
        ↓
Grounding
        ↓
Generation
        ↓
Evaluation
```

## Modules

01 — Why knowledge systems exist

02 — Embeddings and semantic search

03 — Vector databases

04 — RAG architecture

05 — Document processing and chunking

06 — Retrieval strategies

07 — Hybrid search

08 — Reranking

09 — Grounding and citations

10 — RAG security

11 — RAG evaluation

12 — Knowledge systems capstone

## Architecture mindset

RAG is not simply:

```text
Documents → Vector database → LLM
```

A production knowledge system requires:

```text
Sources
  ↓
Ingestion
  ↓
Processing
  ↓
Metadata
  ↓
Indexing
  ↓
Retrieval
  ↓
Permission checks
  ↓
Context assembly
  ↓
Model reasoning
  ↓
Citations
  ↓
Feedback
```

## What completion means

A learner should be able to:

- design a knowledge architecture;
- select appropriate retrieval strategies;
- understand when RAG is better than fine-tuning;
- measure retrieval quality;
- protect sensitive information;
- build systems where AI decisions are grounded in evidence.

## Canonical curriculum navigation

- [Why Knowledge Systems Exist](./01-why-knowledge-systems-exist.md)
- [Embeddings and Semantic Search](./02-embeddings-and-semantic-search.md)
- [Vector Databases](./03-vector-databases.md)
- [RAG Architecture](./04-rag-architecture.md)
- [Chunking and Document Processing](./05-chunking-and-document-processing.md)
- [Retrieval Strategies](./06-retrieval-strategies.md)
- [Hybrid Search](./07-hybrid-search.md)
- [Re-ranking](./08-re-ranking.md)
- [Grounding and Citations](./09-grounding-and-citations.md)
- [RAG Security](./10-rag-security.md)
- [RAG Evaluation](./11-rag-evaluation.md)
- [RAG Capstone — Production Enterprise Knowledge System](./12-rag-capstone.md)
