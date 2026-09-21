# Agent Memory

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **Agent Memory** within Agents;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Core Principle

Memory does not make an agent intelligent by itself. Memory gives an agent access to relevant information from previous interactions, experiences, and knowledge.

A production agent needs controlled memory, not unlimited memory.

## Types of Agent Memory

### Working Memory

Temporary information needed for the current task.

Examples:
- Current conversation context
- Active plan
- Current tool results

### Short-Term Memory

Information retained during a session.

Examples:
- User preferences during a workflow
- Previous decisions in the current task

### Long-Term Memory

Information preserved across sessions.

Examples:
- User preferences
- Business rules
- Historical interactions

## Memory Architecture

```text
Agent
 |
 +-- Working Memory
 |
 +-- Session Memory
 |
 +-- Long-Term Memory
 |
 +-- External Knowledge Systems
```

## Memory Is Not The Same As Knowledge

Important distinction:

Knowledge systems provide trusted organisational information.

Memory stores useful context about interactions and experiences.

Do not use memory as a replacement for databases, policies, or RAG systems.

## Memory Risks

Poor memory design can create:

- privacy issues
- incorrect assumptions
- outdated information
- security leaks
- unwanted persistence

## Memory Governance

Enterprise agents require:

- retention policies
- access controls
- deletion capability
- user transparency
- audit trails

## Example: Commerce Agent

A useful commerce agent may remember:

- preferred reporting format
- approved business rules
- previous decisions

It should not permanently remember:

- sensitive credentials
- unrelated private information
- temporary errors

## Key Rule

The best agent memory is selective, controlled, and purpose-driven.

## Architect exercise

Design or inspect a representative system that uses **Agent Memory**. Produce an architecture sketch, identify at least three failure modes, state one security or governance control where relevant, define one measurable success criterion, and compare the design with a simpler baseline. Record what evidence would justify keeping the added complexity.
