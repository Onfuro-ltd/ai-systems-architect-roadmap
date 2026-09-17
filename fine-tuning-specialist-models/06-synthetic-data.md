# 06 — Synthetic Data

## Purpose
Synthetic data can expand coverage, create edge cases, transform formats, and reduce some labeling cost. It can also amplify errors.

> Synthetic data is generated evidence, not automatically ground truth.

## Uses
Synthetic generation can create variations, hard negatives, simulated dialogues, structured transformations, rare-case candidates, multilingual variants, and teacher outputs.

## Provenance
Record generator model/version, prompt/template version, reference inputs, generation settings, validation status, and dataset version.

Never silently mix generated and verified data.

## Grounding and validation

```text
Trusted source → synthetic generator → deterministic/human validation → dataset candidate
```

Use deterministic validators for schemas, calculations, constraints, and references. Model-based review is useful but is not independent truth.

## Diversity and mismatch
Large generated datasets can be superficial paraphrases. Measure semantic diversity and production coverage.

Synthetic examples may be cleaner than real inputs. Preserve a real-world holdout with noise and ambiguity.

## Error amplification

```text
Teacher error → synthetic example → student training → repeated systematic error
```

Analyze failure clusters before scaling generation.

## Privacy and contamination
Synthetic does not guarantee anonymity. Generators can reproduce sensitive source content.

Never generate training examples from held-out evaluation answers.

## Economics
Count generation, validation, filtering, review, and storage. Optimize cost per useful validated example, not per generated row.

## Exercise
Design a synthetic-data factory with trusted seeds, generation strategies, provenance, validators, human sampling, diversity checks, contamination controls, and real holdout evaluation.

## Takeaway
> Synthetic data is a force multiplier for a good data pipeline and a force multiplier for errors in a poorly governed one.

Next: **07 — Distillation and Specialist Models**.
