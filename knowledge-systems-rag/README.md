# Knowledge Systems and RAG

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
