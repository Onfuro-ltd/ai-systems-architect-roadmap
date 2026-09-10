# LoRA & Parameter Efficient Training

## Principle

> Modern AI systems usually adapt models efficiently rather than retraining them from scratch.

## Why Full Fine-Tuning Is Difficult

Updating all model parameters requires:

- large GPU memory;
- expensive compute;
- significant datasets;
- complex training pipelines.

## LoRA

Low-Rank Adaptation adds small trainable components while keeping the base model frozen.

Benefits:

- lower memory requirements;
- faster training;
- smaller deployment artefacts;
- easier experimentation.

## QLoRA

QLoRA combines quantisation with LoRA to make fine-tuning larger models possible on more affordable hardware.

## When To Use

Good candidates:

- consistent writing style;
- classification tasks;
- domain-specific behaviour;
- structured outputs.

Poor candidates:

- frequently changing facts;
- live business data;
- information better handled through retrieval or tools.

## SEMLIS Relevance

Potential uses:

- marketplace listing style adaptation;
- product categorisation;
- internal analysis formats;
- specialised commerce workflows.

The goal is not to create a bigger model. The goal is to create a better specialised system.
