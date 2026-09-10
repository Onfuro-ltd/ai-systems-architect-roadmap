# 01 — Why Knowledge Systems Exist

## The problem

Large language models contain broad learned patterns, but they do not automatically contain an organisation's private, current or authoritative information.

A production AI system usually needs knowledge that is:

- specific to a company;
- updated frequently;
- permission controlled;
- traceable to sources;
- evaluated for accuracy.

This creates the need for a knowledge system.

## The difference between model knowledge and organisational knowledge

A model provides:

- language ability;
- reasoning capability;
- general patterns from training.

An organisation provides:

- documents;
- databases;
- policies;
- processes;
- customer information;
- operational history;
- specialist expertise.

The AI application combines both.

## The wrong mental model

A common misconception:

> Add more documents and the AI will know everything.

Reality:

Information quality, retrieval quality and permissions determine whether the model receives useful context.

## Knowledge systems architecture

```text
Real-world information
          |
          ↓
Knowledge pipeline
          |
          ↓
Search and retrieval
          |
          ↓
Relevant context
          |
          ↓
AI reasoning
          |
          ↓
Verified output
```

## RAG is a pattern, not a product

Retrieval Augmented Generation (RAG) describes a family of architectures where external information is retrieved and provided to a model during generation.

The important engineering questions are:

- What information should be retrieved?
- How is relevance measured?
- How is access controlled?
- How fresh is the information?
- How do we know retrieval helped?

## When RAG helps

RAG is valuable when information is:

- private;
- changing;
- too large to place in prompts;
- required with citations;
- separated by permissions.

## When RAG is not the answer

RAG does not fix:

- poor source data;
- unclear business rules;
- missing evaluation;
- reasoning limitations;
- incorrect permissions.

## Strategic lesson

The future AI advantage will not only come from better models. It will come from better information systems surrounding those models.
