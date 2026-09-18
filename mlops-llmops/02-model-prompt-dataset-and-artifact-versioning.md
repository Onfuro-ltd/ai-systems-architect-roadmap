# 02 — Model, Prompt, Dataset and Artifact Versioning

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **02 — Model, Prompt, Dataset and Artifact Versioning** within MLOps and LLMOps;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Any dependency capable of changing AI behaviour must have an identifiable version.

## System release manifest

```text
Application code
+ Model/provider revision
+ Prompt/skill version
+ Retrieval/index configuration
+ Dataset/eval version
+ Tool schemas
+ Policy/configuration
+ Runtime/quantization
= AI system release
```

## Immutable identity

Prefer immutable versions, content hashes or provider revision identifiers over mutable labels such as "latest".

Record aliases separately from the artifact they currently resolve to.

## Prompts and skills

Treat prompts, system instructions, tool descriptions and reusable skills as code-like production assets: review, test, version and roll them back.

## Data and indexes

Version source snapshot or lineage, transformation/chunking, embedding model, index build and retrieval configuration. A vector index without provenance is not reproducible knowledge infrastructure.

## Models and adapters

Bind tuned models/adapters to base revision, tokenizer, dataset, training configuration, license lineage and evaluation.

## Configuration

Feature flags, routing thresholds, context limits and policy configuration can change outcomes without a code deployment. Include them in release history.

## Compatibility

Maintain explicit compatibility between models, adapters, tokenizers, schemas, runtimes and tool contracts.

## Exercise

Create a release manifest capable of reconstructing one production AI decision six months later.

## Takeaway

> Version the system that produced the behaviour, not only the model that generated the text.

Next: **03 — Evaluation Pipelines and Quality Gates**.
