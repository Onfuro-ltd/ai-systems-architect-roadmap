# 05 — Context Management

## Core Principle

Context is a limited engineering resource, not a place to put everything.

A strong AI system does not maximise context. It selects the most useful context.

## Context Architecture

```
User Goal
   ↓
Context Selection
   ↓
Relevant Information
   ↓
Model Reasoning
   ↓
Output
```

## Context vs Memory vs Knowledge

### Context
Temporary information provided to the model for the current task.

Examples:
- current conversation
- retrieved documents
- tool results
- current workflow state

### Memory
Information retained between interactions.

Examples:
- user preferences
- previous decisions
- long-term business rules

### Knowledge
Authoritative information sources.

Examples:
- policies
- documentation
- product data
- company information

These should not be treated as the same layer.

## Why More Context Is Not Always Better

Large amounts of context can create:

- higher cost;
- slower responses;
- irrelevant information;
- conflicting instructions;
- reduced reasoning quality.

The goal is context quality, not context quantity.

## Context Engineering Patterns

Production systems use:

- retrieval;
- summarisation;
- compression;
- ranking;
- filtering;
- structured state.

## Enterprise Principle

The AI system should answer:

"What information does the model need right now?"

Not:

"How much information can we send?"

## Relevance to AI Systems

For SEMLIS-style systems:

A pricing agent does not need the entire company database.

It needs:

- relevant product data;
- pricing history;
- competitor information;
- margin rules;
- approved business constraints.

Context management is what turns large data access into useful intelligence.
