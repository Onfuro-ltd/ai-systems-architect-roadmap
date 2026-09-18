# 01 — When to Fine-Tune and When Not To

## Learning outcomes

By the end of this module, you should be able to:

- explain the role of **01 — When to Fine-Tune and When Not To** within Fine-Tuning and Specialist Models;
- distinguish the mechanism from adjacent concepts and identify the main architectural trade-offs;
- identify realistic failure modes, control boundaries and operating constraints;
- apply the concept to a representative production design and define evidence that would validate the choice.

## Purpose

Fine-tuning is one intervention among many. Before changing model weights, identify the actual failure and choose the cheapest, safest, most maintainable layer that can correct it.

> Fine-tune stable learned behaviour. Do not fine-tune around an architecture problem.

## Diagnose the failure

Weak results can come from missing facts, poor retrieval, weak instructions, missing workflow state, missing deterministic rules, tool failures, insufficient model capability, unstable behaviour, or wrong output conventions.

If you tune before isolating the failure domain, you can create an expensive model that still fails for the original reason.

## Intervention ladder

```text
Prompt / instruction
        ↓
Context engineering
        ↓
RAG / authoritative retrieval
        ↓
Tool / API access
        ↓
Skill / workflow
        ↓
Deterministic code / policy
        ↓
Model routing
        ↓
Fine-tuning / specialist model
```

This is a diagnostic ladder, not a rigid sequence.

## Prompting

Use prompting when the base model already has the capability but needs clearer task definition, format, examples, constraints, or context. Prompt changes are easier to inspect, version, test, and reverse than weight changes.

## RAG

Use RAG for changing, proprietary, sourceable, or auditable knowledge. Do not repeatedly retrain merely to refresh facts.

```text
Changing knowledge → governed source → retrieval → model
```

## Tools

Use tools when the model must observe or act on live systems. A tuned model cannot reliably know a value that changed after training.

## Deterministic code and policy

Use deterministic controls for requirements that must be exact, enforceable, testable, or auditable: permissions, calculations, transaction invariants, eligibility rules, limits, and validation.

Model proposal → deterministic rule/policy → accept, reject, or escalate.

## Skills and workflows

Use skills when the missing capability is a reusable procedure: steps, tool sequence, validation, recovery, and operating knowledge. Procedures remain inspectable and portable across models.

## Memory

Use memory/state for user-, session-, or workflow-specific information with explicit lifecycle rules. Fine-tuning a shared model is generally the wrong mechanism for individual changing state.

## Model routing

Before training, check whether a different existing model already solves the task. Compare its lifecycle economics with building and operating a tuned model.

## When tuning becomes attractive

Fine-tuning is strongest when the gap is stable, repeated, measurable, and behavioural. Candidates include consistent classification/extraction, normalization, specialized language patterns, recurring output conventions, task transformations, tool-selection tendencies, or enabling a smaller model to perform a high-volume bounded task.

## Knowledge vs behaviour vs capability

```text
Knowledge gap  → retrieval / tools
Behaviour gap  → prompting first, then consider tuning
Capability gap → stronger/specialist model or deeper training
```

Fine-tuning cannot reliably manufacture capabilities unsupported by the base model.

## Establish the baseline first

Before training, evaluate the strongest reasonable baseline with clear instructions, relevant examples, correct context, tools, structured outputs, and deterministic validation.

Only then can the incremental value of tuning be measured.

## Fine-tuning hypothesis

Define a falsifiable objective: current held-out performance, desired production gate, expected latency/token/cost improvement, and regressions that are unacceptable.

"We should fine-tune because this is our domain" is not a measurable hypothesis.

## Economics

Compare prompt/RAG/tool improvements, higher-capability model routing, and the full fine-tuning lifecycle.

Lifecycle cost includes data collection, cleaning, labeling, training, experiments, evaluation, deployment, monitoring, retraining, and governance.

A cheaper inference call can still create a more expensive system.

## What fine-tuning is not

Fine-tuning is not a database for current facts, an authorization mechanism, deterministic validation, guaranteed factuality, or automatic privacy.

Keep current prices/state, permissions, policy enforcement, secrets, transaction state, and rules requiring exact traceability outside weights.

## Multi-tenancy

Per-tenant tuning can create data-isolation risk, model proliferation, weak per-tenant datasets, serving complexity, evaluation burden, and difficult deletion/upgrade requirements.

First consider shared specialists plus tenant-specific retrieval, configuration, skills, memory, or policy.

## Warning signs

Do not tune merely because facts change frequently, the task is unclear, no held-out evaluation exists, examples are untrustworthy, the real problem is retrieval, deterministic rules are being learned instead of enforced, the base model works with better instructions, another model is cheaper overall, or nobody owns the dataset/model lifecycle.

## Decision matrix

| Requirement | Likely first choice |
|---|---|
| Current factual knowledge | RAG / tool |
| Exact calculation | Deterministic code |
| Permission enforcement | Policy / authorization |
| Reusable procedure | Skill / workflow |
| User-specific history | Memory / state |
| Better task instruction | Prompt/context |
| Different capability | Model routing |
| Stable repeated behaviour | Fine-tuning candidate |
| High-volume narrow task | Specialist/tuned candidate |

## Architecture decision record

A fine-tuning ADR should capture the observed gap, baseline, alternatives, why alternatives are insufficient, dataset governance, success/regression metrics, expected economics, serving impact, privacy/security impact, and rollback.

## Example: changing knowledge

For current policies:

```text
Authoritative policy store
        ↓
Versioned retrieval
        ↓
Model interpretation
        ↓
Provenance
```

Tune only a separate stable behavioural problem, not the changing policy itself.

## Example: high-volume extraction

```text
Verified examples
      ↓
Tune smaller model
      ↓
Held-out evaluation
      ↓
Production shadow
      ↓
Cost / quality comparison
      ↓
Route eligible workload
```

The business case is measured cost per successful extraction.

## Consequential actions

Even a tuned specialist remains inside deterministic controls:

```text
Authoritative evidence
      ↓
Specialist recommendation
      ↓
Deterministic validation
      ↓
Policy / permission
      ↓
Approval where required
      ↓
Idempotent execution
      ↓
Verified outcome
```

## Architect checklist

Ask what exact failure is being solved; whether it is knowledge, behaviour, capability, workflow, state, or enforcement; what the strongest baseline is; whether behaviour is stable; whether governed data and clean held-out tests exist; what regression risks exist; whether an existing specialist suffices; whether economics matter; and how versioning, monitoring, rollback, and durable knowledge will work.

## Exercise

Evaluate five failures: stale factual answers, inconsistent JSON extraction, incorrect permission decisions, a repeated multi-step procedure, and expensive high-volume classification.

Choose the correct intervention for each, then design a controlled experiment only for the case where tuning is genuinely justified.

## Takeaway

> Fine-tuning should follow diagnosis, not enthusiasm. Use it when a stable learned behaviour is the bottleneck and measured improvement justifies the dataset, training, serving, evaluation, and governance lifecycle.

Next: **02 — Dataset Design and Data Quality**.
