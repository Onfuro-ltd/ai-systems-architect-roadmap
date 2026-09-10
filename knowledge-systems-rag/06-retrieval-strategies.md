# Retrieval Strategies

## Purpose

Retrieval is the point where a knowledge system decides what information the AI system is allowed to see.

A weak retrieval layer produces weak AI responses even when the underlying model is highly capable.

The core principle:

> The intelligence of a RAG system depends not only on the model, but on whether the right knowledge reaches the model at the right time.

## The retrieval pipeline

```text
User Question
      |
      v
Query Understanding
      |
      v
Candidate Retrieval
      |
      v
Filtering
      |
      v
Ranking
      |
      v
Context Selection
      |
      v
Generation
```

Retrieval is not simply a database lookup. It is a decision process.

## 1. Similarity search

The simplest retrieval pattern compares the query embedding with stored document embeddings.

```text
Question
   |
Embedding
   |
Similarity search
   |
Top matching chunks
```

Advantages:
- simple implementation;
- good baseline;
- useful for semantic questions.

Limitations:
- similarity does not always mean relevance;
- may retrieve incomplete context;
- can miss exact identifiers and structured information.

## 2. Top-k retrieval

Top-k defines how many candidates are returned.

Example:

```text
Query
  |
Retrieve top 20 chunks
  |
Rank down to top 5
  |
Send best context to model
```

A larger k may improve recall but can reduce precision and consume more context.

There is no universal optimal value. It must be evaluated.

## 3. Metadata filtering

Enterprise retrieval requires more than semantic similarity.

Examples:

```json
{
 "tenant": "company_a",
 "department": "finance",
 "effective_date": "2026-01-01",
 "access_level": "manager"
}
```

Filtering can enforce:
- tenant isolation;
- permissions;
- document status;
- date ranges;
- source restrictions.

## 4. Query rewriting

Users rarely ask questions in the exact form needed for retrieval.

A retrieval system may transform:

"Why did this item lose profit?"

into:

- recent pricing changes;
- advertising cost changes;
- supplier cost changes;
- return rate history.

Query rewriting improves recall but must be evaluated because it can introduce incorrect assumptions.

## 5. Multi-query retrieval

One question may have multiple interpretations.

A system can generate several retrieval perspectives:

```text
Original question
       |
+------+------+------+
|      |      |      |
Query1 Query2 Query3
       |
       v
Combined candidates
```

Useful for complex research tasks.

## 6. Parent-child retrieval

Small chunks improve precision, but larger chunks preserve context.

Parent-child retrieval combines both:

```text
Large document section
          |
     Smaller searchable chunks
          |
     Retrieve relevant chunk
          |
     Return useful parent context
```

## 7. Context compression

Retrieval can return more information than the model needs.

Compression techniques:
- remove irrelevant text;
- summarise retrieved sections;
- extract only supporting passages.

The goal is not maximum information. The goal is maximum useful information.

## 8. Retrieval failure modes

Common failures:

### Correct document, wrong passage

The system found the right source but not the relevant section.

### Similar but incorrect information

Semantic similarity is not the same as correctness.

### Missing metadata

The right answer exists but permissions or filters hide it.

### Stale knowledge

Old information is retrieved instead of current policy.

### Context overload

Too many retrieved documents reduce model performance.

## 9. Evaluation requirements

Retrieval should be measured separately from generation.

Important metrics:

### Recall
Did we retrieve relevant information?

### Precision
Were retrieved items actually useful?

### Ranking quality
Did the best information appear first?

### End-to-end answer quality
Did retrieval improve the final result?

## Architecture principle

Do not optimise retrieval by intuition alone.

Use:

```text
Baseline
   |
Experiment
   |
Measure
   |
Compare
   |
Adopt only proven improvements
```

## Enterprise view

A mature knowledge system does not ask:

> "Which vector database should we use?"

It asks:

> "How do we reliably deliver the correct, authorised, current information required for this decision?"

That question leads to better architecture.
