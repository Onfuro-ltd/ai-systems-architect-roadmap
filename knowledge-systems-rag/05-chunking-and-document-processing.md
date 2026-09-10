# Chunking and Document Processing

## Why this matters

A retrieval system can only retrieve what has been represented correctly.

Many failed RAG implementations start with a simple pipeline:

```text
PDF
 ↓
Split every N tokens
 ↓
Create embeddings
 ↓
Store vectors
```

This approach ignores a fundamental truth:

> Documents contain structure, meaning and relationships. A knowledge system must preserve those properties.

Chunking is not merely a technical preprocessing step. It is a knowledge modelling decision.

---

# 1. The document processing pipeline

A production knowledge system usually follows:

```text
Source documents
        ↓
Collection
        ↓
Parsing
        ↓
Cleaning
        ↓
Structure detection
        ↓
Chunking
        ↓
Metadata enrichment
        ↓
Embedding
        ↓
Indexing
        ↓
Evaluation
```

Every stage affects retrieval quality.

Poor parsing creates poor chunks. Poor chunks create poor retrieval. Poor retrieval creates poor answers.

---

# 2. Understanding document structure

Documents are not equal.

Examples:

## A policy document

Important structure:

- sections;
- clauses;
- exceptions;
- definitions;
- effective dates.

## A product catalogue

Important structure:

- SKU;
- specifications;
- compatibility;
- pricing;
- categories.

## A legal agreement

Important structure:

- parties;
- obligations;
- conditions;
- termination clauses.

A generic splitter treats all of these incorrectly.

---

# 3. Chunking strategies

## Fixed-size chunking

Split content by characters or tokens.

Advantages:

- simple;
- predictable;
- inexpensive.

Problems:

- breaks meaning;
- separates related information;
- ignores document structure.

Useful as a baseline, not a universal solution.

---

## Recursive chunking

Attempts to split using natural boundaries:

```text
Document
 ↓
Sections
 ↓
Paragraphs
 ↓
Sentences
```

Better preserves meaning while controlling size.

---

## Semantic chunking

Creates chunks based on meaning rather than length.

Example:

Instead of:

```text
Chunk 1:
Half of a pricing policy

Chunk 2:
The exception rules
```

A semantic approach attempts to preserve:

```text
Complete pricing rule
+
Complete exception logic
```

---

## Structure-aware chunking

For enterprise systems this is often the most valuable approach.

Use existing structure:

```text
Heading
   ↓
Section
   ↓
Paragraph
   ↓
Metadata
```

The chunk retains its meaning and location.

---

# 4. Chunk size trade-offs

There is no perfect chunk size.

Large chunks:

Advantages:

- more context;
- fewer retrieval fragments.

Disadvantages:

- more irrelevant information;
- higher token cost;
- harder ranking.

Small chunks:

Advantages:

- precise retrieval;
- lower context usage.

Disadvantages:

- lose relationships;
- require more retrieval assembly.

The correct choice depends on:

- document type;
- query type;
- model context window;
- evaluation results.

---

# 5. Metadata enrichment

A chunk should not be just text.

A useful knowledge object contains:

```json
{
  "content": "...",
  "source": "supplier_policy.pdf",
  "section": "Returns",
  "created_date": "2026-01-01",
  "version": "3",
  "owner": "operations",
  "access_level": "internal"
}
```

Metadata enables:

- filtering;
- permissions;
- freshness management;
- citations;
- debugging.

---

# 6. Tables and structured data

A major RAG failure comes from treating tables like plain text.

Example:

A pricing table:

| Tier | Discount |
|---|---|
| 10 units | 5% |
| 100 units | 15% |

The relationship between columns matters.

Possible approaches:

- preserve table structure;
- convert to structured records;
- use specialised document models;
- store relational data separately.

Not all knowledge belongs in embeddings.

---

# 7. Document freshness and versioning

Enterprise knowledge changes.

A production system needs:

- document version;
- effective date;
- expiry date;
- source authority;
- update history.

Otherwise the AI may retrieve outdated information.

---

# 8. What should not be embedded

A mature architect asks:

> Does this information belong in semantic retrieval?

Avoid embedding everything automatically.

Examples better handled elsewhere:

- transactional records;
- live inventory counts;
- financial balances;
- permissions;
- rapidly changing operational state.

A knowledge system works alongside databases, not instead of them.

---

# 9. Evaluation-driven chunking

The correct workflow:

```text
Choose chunking strategy
        ↓
Create evaluation questions
        ↓
Measure retrieval quality
        ↓
Compare alternatives
        ↓
Deploy best approach
```

Do not choose chunk sizes because a blog post recommended them.

---

# 10. Architecture principle

The goal is not:

> Put more information into the model.

The goal is:

> Deliver the right information, at the right time, with the right permissions, in a form the model can use.

That is knowledge engineering.

---

# Mastery gate

A learner should be able to:

- explain why naive chunking fails;
- choose chunking strategies for different document types;
- preserve metadata and provenance;
- identify when information should not be embedded;
- design evaluation experiments for retrieval quality;
- explain why document processing is part of AI architecture, not just data preparation.
