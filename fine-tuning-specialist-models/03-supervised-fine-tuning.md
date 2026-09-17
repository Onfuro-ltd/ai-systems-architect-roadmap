# 03 — Supervised Fine-Tuning

## Purpose
Supervised fine-tuning adapts a pretrained model toward desired input-output behaviour using curated examples.

> Training loss measures fit to examples. Held-out task success measures usefulness.

## Lifecycle

```text
Input / context → desired response → model prediction → loss → parameter update
```

Record a strong base-model baseline first, including prompt, context, tools, decoding configuration, and held-out results.

## Production-shaped data
Use the intended interaction pattern where practical. If production uses chat roles, tool calls, structured output, or domain context, training representation should reflect it.

## Training configuration
Version learning rate, epochs/steps, effective batch size, sequence length, optimizer, scheduler, regularization, packing, model revision, tokenizer, code, and environment.

## Overfitting and regression
Watch train-vs-validation behaviour. More epochs are not automatically better.

Specialization can damage other capabilities, so maintain regression tests for behaviours the deployment still needs. A narrowly routed specialist may accept different trade-offs from a general assistant.

## Structured tasks and tools
SFT can work well for stable extraction, classification, transformation, formatting, and domain patterns. External schema/business validation remains necessary.

Training may improve tool-selection behaviour, but permissions, idempotency, and verified tool outcomes remain external controls.

## Checkpoints
Evaluate candidate checkpoints rather than assuming the final one is best. Bind every artifact to its exact dataset and configuration.

## Privacy and serving
Training infrastructure, logs, checkpoints, trackers, and caches can expose sensitive data. Govern them accordingly.

Include serving memory, latency, throughput, and cost in the experiment.

## Exercise
Design an SFT experiment for a narrow structured task with baseline, splits, configuration tracking, checkpoint evaluation, regression suite, promotion gate, and rollback.

## Takeaway
> SFT is a controlled behaviour-learning experiment. Promote only when held-out evidence shows improvement without unacceptable regressions.

Next: **04 — LoRA and QLoRA**.
