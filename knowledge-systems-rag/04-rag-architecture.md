# RAG Architecture

## Purpose

Retrieval-Augmented Generation (RAG) is an architecture pattern that connects AI models with external knowledge.

The core idea:

```text
Retrieve relevant information
          +
Generate a response using that information
```

RAG helps models answer using current, private or domain-specific information without requiring the model itself to be retrained.

## Why RAG exists

Foundation models have limitations:

- knowledge cut-off dates;
- no access to private company information;
- possible hallucinations;
- inability to know changing operational data.

RAG provides a controlled knowledge access layer.

## Basic architecture

```text
User Question
       |
       v
Query Processing
       |
       v
Retriever
       |
       v
Relevant Knowledge
       |
       v
Context Assembly
       |
       v
Language Model
       |
       v
Validated Response
```

## Production RAG pipeline

A mature system contains several stages:

```text
                Knowledge Sources
                       |
                       v
              Ingestion Pipeline
                       |
                       v
          Cleaning + Classification
                       |
                       v
              Chunking Strategy
                       |
                       v
              Embedding Pipeline
                       |
                       v
              Search Indexes
                       |
                       v
                 Retrieval
                       |
                       v
                Re-ranking
                       |
                       v
              Context Assembly
                       |
                       v
                 Generation
                       |
                       v
                Evaluation
```

## Retrieval is the foundation

A weak retrieval system creates weak AI responses.

The model can only reason over the information it receives.

Therefore:

```text
Poor retrieval
      |
      v
Poor context
      |
      v
Poor answer
```

## Context assembly

Retrieval results should not simply be copied into the prompt.

A mature system considers:

- relevance;
- source authority;
- freshness;
- permissions;
- token budget;
- ordering;
- duplication.

## RAG vs fine-tuning

A common mistake is choosing fine-tuning when the problem is knowledge access.

Use RAG when you need:

- changing information;
- private documents;
- citations;
- controlled retrieval.

Consider fine-tuning when you need:

- behavioural adaptation;
- specialised output style;
- task-specific patterns.

They solve different problems.

## RAG security

Knowledge retrieval introduces new security concerns:

- unauthorised document retrieval;
- tenant leakage;
- sensitive information exposure;
- malicious documents;
- stale permissions.

Security must exist at retrieval time, not only after generation.

## Evaluation

A RAG system needs separate evaluation layers:

### Retrieval evaluation

Did the system find the correct information?

### Generation evaluation

Did the model use the information correctly?

### Outcome evaluation

Did the system improve the real task?

## Enterprise pattern

```text
Business Systems
       |
       v
Knowledge Layer
       |
       v
Permission-Aware Retrieval
       |
       v
AI Application
       |
       v
Controlled Action
```

## Connection to AI Operating Systems

RAG is an early version of a broader intelligence architecture:

```text
Knowledge
    +
Memory
    +
Tools
    +
Reasoning
    +
Evaluation
```

RAG provides the knowledge foundation required before reliable agents can operate.

## Mastery gate

You understand RAG architecture when you can:

- design an end-to-end retrieval pipeline;
- explain why retrieval quality dominates output quality;
- choose RAG vs fine-tuning appropriately;
- design permission-aware knowledge access;
- evaluate retrieval and generation separately;
- identify where RAG should not be used.
