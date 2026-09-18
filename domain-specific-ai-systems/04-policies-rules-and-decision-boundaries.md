# 04 — Policies, Rules and Decision Boundaries

## Purpose

Separate exact organizational policy from probabilistic interpretation.

## Policy layers

Policies may govern eligibility, permissions, thresholds, calculations, approvals, data use, action limits and escalation.

## Deterministic boundary

If the organization can state a rule exactly, encode it in a policy/rules layer rather than relying on the model to remember and obey prose.

## Interpretation

AI can map messy evidence into structured facts that a deterministic rule evaluates.

```text
Unstructured evidence
      ↓
AI extraction / interpretation
      ↓
Validated canonical facts
      ↓
Deterministic policy
      ↓
Allowed / denied / escalate
```

## Policy versions

Record which policy version governed a consequential decision.

## Exceptions

Represent authorized exceptions explicitly with owner, reason, scope and expiry.

## Conflicts

Define precedence between law/contract, organizational policy, domain rule, user preference and model suggestion.

## Exercise

Convert a prose-heavy operating policy into model interpretation steps and deterministic enforcement rules.

## Takeaway

> Models can interpret policy context; they should not silently become the policy engine.

Next: **05 — Domain Skills, Workflows and Tool Contracts**.
