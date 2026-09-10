# 11 — RAG Evaluation

## Why Evaluation Exists

A RAG system cannot be improved reliably by asking whether the answer "looks good". Production systems require measurable evaluation of retrieval quality, grounding, reliability, cost, and business outcomes.

The core principle:

> An AI system without evaluation is an experiment. An AI system with evaluation becomes an engineered capability.

## The RAG Evaluation Pipeline

```text
Knowledge Sources
        ↓
Retrieval Evaluation
        ↓
Context Quality Evaluation
        ↓
Generation Evaluation
        ↓
Safety Evaluation
        ↓
Business Outcome Evaluation
```

## Retrieval Evaluation

Retrieval should be measured separately from generation.

Important metrics:

- Recall — did the system find relevant information?
- Precision — were retrieved documents actually useful?
- Ranking quality — did the best information appear first?
- Coverage — can the system answer the required questions?

## Answer Evaluation

A good answer should be evaluated for:

- Correctness
- Relevance
- Completeness
- Groundedness
- Clarity
- Appropriate uncertainty

## Groundedness Testing

The system should verify:

```text
Claim
 ↓
Evidence
 ↓
Source
 ↓
Confidence
```

An answer that sounds convincing but has no supporting evidence is a failure.

## Evaluation Datasets

Production RAG systems require curated datasets containing:

- common questions;
- difficult questions;
- ambiguous requests;
- outdated information;
- security-sensitive examples;
- known failure cases.

A strong evaluation set grows from real usage.

## Regression Testing

Any change can affect quality:

- embedding model;
- chunking strategy;
- retrieval method;
- reranker;
- prompt;
- foundation model;
- knowledge sources.

The process:

```text
Change
 ↓
Run evaluation set
 ↓
Compare results
 ↓
Review regressions
 ↓
Deploy
```

## Human Evaluation

Automated metrics are useful but incomplete.

Human review remains important for:

- usefulness;
- trust;
- business impact;
- edge cases.

## Production Feedback Loop

A mature system continuously learns:

```text
User Interaction
        ↓
Feedback
        ↓
Failure Analysis
        ↓
New Evaluation Case
        ↓
System Improvement
```

## Enterprise Principle

The goal is not to create an AI that always sounds confident.

The goal is to create a system that knows:

- what it knows;
- what it does not know;
- when to ask for help;
- when not to act.

## Connection To AI Systems Architecture

Evaluation is the control loop that allows AI systems to improve safely.

Without evaluation:

```text
AI Output → Hope
```

With evaluation:

```text
AI Output → Measurement → Improvement → Reliability
```
