# 01 — Experiment Tracking and Reproducibility

## Purpose

AI experiments are meaningful only when their inputs, configuration, outputs and evaluation can be reconstructed.

> If you cannot explain exactly what changed between two runs, you do not have an experiment—you have anecdotes.

## Experiment identity

Track code revision, model/provider revision, prompt/template, dataset/evaluation version, retrieval configuration, tools, decoding parameters, runtime, hardware where relevant, environment and random seeds where useful.

## Hypothesis first

Record the failure being addressed, expected improvement, primary metric, regression limits and acceptance threshold before running the experiment.

## Runs and artifacts

Store metrics, traces, sample outputs, evaluation reports, checkpoints/adapters, logs and relevant cost/latency measurements against a stable run ID.

Large artifacts can live in object/model storage while the experiment system stores immutable references and hashes.

## Reproducibility

Exact bit-for-bit reproduction may be impossible with nondeterministic providers or hardware. Operational reproducibility means enough lineage exists to recreate the configuration and explain material differences.

## Comparisons

Compare against the strongest relevant baseline under the same evaluation conditions. Change controlled variables where possible.

## Secrets and privacy

Do not store credentials or unrestricted sensitive prompts/responses in experiment metadata. Apply redaction, access controls, retention and tenant boundaries.

## Exercise

Design an experiment record for comparing two models, two prompts and one retrieval change without losing causal clarity.

## Takeaway

> Experiment tracking converts trial-and-error into cumulative engineering knowledge.

Next: **02 — Model, Prompt, Dataset and Artifact Versioning**.
