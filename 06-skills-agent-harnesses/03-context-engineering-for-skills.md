# 03 — Context Engineering for Skills

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **03 — Context Engineering for Skills** within Skills and Agent Harnesses;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

A skill should receive the information it needs to perform its capability — not every piece of information the surrounding system can access.

Context engineering is the discipline of selecting, structuring and controlling the information available to a model during execution.

For skills, this means making context requirements part of the capability design rather than treating the context window as an unstructured container.

## Core Principle

> Context is a limited engineering resource. Supply the smallest sufficient context for reliable execution.

More context is not automatically better context.

## Context as a Skill Dependency

A skill contract can declare the context required for execution.

Examples include:

- current user or system intent;
- relevant retrieved knowledge;
- validated tool results;
- current workflow state;
- applicable rules or constraints;
- selected conversation history;
- evidence required for the task.

The skill should not need unrestricted access to every available information source.

## Context, Knowledge, Memory and State

These concepts interact but should remain architecturally distinct.

### Context

Information made available to the model for the current execution.

### Knowledge

Authoritative or reference information that can be retrieved when needed.

### Memory

Information retained or derived across interactions and events for possible future use.

### State

The current condition of an execution, workflow or system.

An implementation may place information from knowledge, memory or state into the current context, but that does not make those layers equivalent.

## Context Assembly

A production harness can assemble context before invoking the model.

```text
Skill Request
     |
     v
Context Requirements
     |
     v
Retrieve / Select / Filter
     |
     v
Validate and Prioritise
     |
     v
Assemble Execution Context
     |
     v
Model
```

## Selection and Relevance

Context should be selected according to the task rather than accumulated by default.

Useful selection signals can include:

- relevance to the current objective;
- authority of the source;
- freshness;
- confidence;
- workflow state;
- permissions;
- expected information value.

The objective is context quality, not context quantity.

## Provenance

Important context should retain enough provenance for the system to understand where it came from.

Provenance can help distinguish:

- user-provided information;
- trusted system instructions;
- retrieved knowledge;
- model-generated summaries;
- tool observations;
- untrusted external content.

This becomes especially important when context can influence consequential reasoning or actions.

## Instruction and Data Boundaries

Not everything inside the context should be treated as an instruction.

External documents, webpages, messages and tool results may contain text that looks like instructions but should instead be treated as data.

A harness should preserve the distinction between trusted control instructions and untrusted task content.

## Context Isolation

Skills should receive only the context appropriate to their capability and authority.

Isolation reduces accidental disclosure, irrelevant reasoning and unintended coupling between capabilities.

For example, a classification skill may require a document and taxonomy but not unrelated user history or credentials.

## Context Budgets

Context windows are finite, but token capacity is only one constraint.

Additional context can also increase:

- latency;
- cost;
- distraction;
- conflicting evidence;
- instruction ambiguity;
- exposure of unnecessary information.

A context budget should therefore consider usefulness as well as size.

## Stale and Conflicting Context

Context can become incorrect even when retrieval itself succeeds.

Production systems should have strategies for:

- stale information;
- contradictory sources;
- duplicated evidence;
- missing timestamps;
- uncertain authority;
- obsolete workflow state.

The model should not be expected to silently resolve every conflict without architectural support.

## Compression and Summarisation

When source material is larger than the useful execution context, systems may compress or summarise it.

Compression introduces information loss, so the architecture should distinguish original evidence from derived summaries.

For consequential tasks, the system may need to preserve links or references back to authoritative source material.

## Context Failure Modes

Common failure modes include:

- retrieving relevant information but ranking it poorly;
- supplying stale state;
- omitting critical constraints;
- allowing untrusted content to influence control instructions;
- flooding the model with irrelevant information;
- losing provenance during summarisation;
- carrying context from one task into another without justification;
- assuming a large context window removes the need for selection.

These are system-design failures, not merely model failures.

## Evaluating Context Engineering

Context strategies should be evaluated against task outcomes rather than token usage alone.

Useful questions include:

- Did the skill receive the information required to succeed?
- Was unnecessary information excluded?
- Were authoritative sources prioritised?
- Could the system identify stale or conflicting information?
- Did compression preserve decision-relevant evidence?
- Did context selection improve reliability, latency or cost?

Broader evaluation methodology is covered in Domain 10.

## Domain Boundaries

Context engineering intersects with several other domains without replacing them.

**Domain 04 — Knowledge Systems and RAG** covers how authoritative information is indexed, retrieved and grounded.

**Domain 08 — Memory Systems** covers information retained or derived across interactions and events.

**Domain 11 — Security, Permissions and Governance** covers authority, trust boundaries and controls around sensitive or untrusted information.

This lesson focuses specifically on how a skill and its harness determine what information should enter the current model execution.

## Exercise

Design the context contract for a generic document-review skill.

Specify:

1. required context;
2. optional context;
3. authoritative sources;
4. freshness requirements;
5. information that must be excluded;
6. conflict-handling rules;
7. provenance requirements;
8. context-budget strategy.

Then explain what belongs to knowledge, memory, state and current execution context.

## Takeaway

> Good context engineering is selective, structured and provenance-aware.

The objective is not to fill the context window. It is to provide the smallest sufficient set of trustworthy information required for the skill to perform reliably.

Next: **04 — Agent Harness Architecture**.
