# Context Engineering

## Why context is the new engineering problem

Prompt engineering focuses on the words given to a model.

Context engineering focuses on designing the complete information environment available when a model makes a decision.

Modern AI systems succeed or fail based on what information reaches the model, when it reaches it, and how it is organised.

## The context stack

```text
System instructions
        |
Policies and constraints
        |
User intent
        |
Retrieved knowledge
        |
Tool results
        |
Conversation state
        |
Current task data
        |
Model
```

## Context is a limited resource

A larger context window does not automatically create a better system.

Problems include:

- irrelevant information;
- conflicting instructions;
- stale data;
- increased cost;
- slower responses;
- reduced attention to important details.

## Context engineering principles

### Relevance over volume

The best context is not the most context. It is the most useful context.

### Separate instructions from information

Rules, policies and data should have clear boundaries.

### Freshness matters

A model using old information can produce confident but incorrect decisions.

### Order matters

Important information should not be buried among low-value content.

## Context techniques

### Retrieval

Select relevant information at runtime.

### Compression

Reduce information while preserving meaning.

### Summarisation

Create useful state from previous interactions.

### Filtering

Remove irrelevant or unsafe information.

### Prioritisation

Rank information by importance for the current task.

## Context failure modes

### Context overload

Too much information reduces useful signal.

### Context poisoning

Incorrect or malicious information enters the model context.

### Instruction confusion

The model cannot distinguish rules from data.

### Stale context

The system uses information that is no longer valid.

## Relationship to future topics

Context engineering connects directly to:

- RAG;
- memory systems;
- agents;
- skills;
- MCP tools;
- enterprise knowledge systems.

## Practical exercise

Create two versions of an AI assistant:

Version A:
- provide all available information.

Version B:
- retrieve and rank only relevant information.

Compare:
- accuracy;
- latency;
- cost;
- user satisfaction.

## Mastery gate

You understand context engineering when you can:

- design what information a model receives;
- reduce irrelevant context;
- separate instructions from data;
- explain why bigger context windows are not a complete solution.
