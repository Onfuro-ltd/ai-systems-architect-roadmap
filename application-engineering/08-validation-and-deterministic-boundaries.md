# Validation and Deterministic Boundaries

## Why this matters

Large language models are powerful because they are flexible. The same flexibility creates a fundamental engineering challenge: model output is probabilistic.

Traditional software usually expects:

```
Input
  |
Function
  |
Predictable Output
```

AI applications introduce a different reality:

```
Input
  |
Model
  |
Likely Output
```

A production AI system must therefore create boundaries where deterministic software takes responsibility.

The goal is not to remove AI uncertainty. The goal is to design systems that remain reliable despite it.

---

# Core Principle

**AI should recommend, interpret and generate. Deterministic systems should enforce rules, permissions and irreversible actions.**

A mature architecture separates:

- intelligence;
- validation;
- policy;
- execution;
- audit.

Example:

```
AI analysis
      |
      v
Structured recommendation
      |
      v
Validation layer
      |
      v
Business rules
      |
      v
Permission check
      |
      v
Human approval (if required)
      |
      v
Action
      |
      v
Audit record
```

---

# 1. The validation problem

A model can produce output that is:

- syntactically valid but logically wrong;
- confident but unsupported;
- incomplete;
- inconsistent with business rules;
- unsafe to execute.

Example:

AI output:

```json
{
  "recommendation": "increase_price",
  "confidence": 0.94
}
```

This does not answer:

- Is the product allowed to increase price?
- Would it violate marketplace rules?
- Is stock sufficient?
- Are competitors changing prices?
- Is the confidence calibrated?

Confidence from a model is not automatically a guarantee of correctness.

---

# 2. Types of validation

## Schema validation

Checks structure.

Examples:

- required fields exist;
- correct data types;
- allowed values;
- valid formats.

Tools:

- JSON Schema;
- typed models;
- API contracts.

---

## Semantic validation

Checks meaning.

Example:

A model returns:

```
quantity = -50
```

The JSON is valid, but the business meaning is impossible.

---

## Business rule validation

Rules owned by the organisation should not be delegated to a model.

Example:

```
IF refund > £500
THEN require approval
```

The AI may recommend the refund.

The policy engine decides whether it is permitted.

---

## Security validation

Checks:

- user permissions;
- tenant boundaries;
- sensitive data exposure;
- tool access;
- credential usage.

---

# 3. Deterministic boundaries

The most important design decision is deciding where AI stops.

Weak architecture:

```
User
 |
AI
 |
Database update
```

Stronger architecture:

```
User
 |
AI interpretation
 |
Recommendation
 |
Validation
 |
Policy engine
 |
Approved action
 |
Database update
```

The second architecture allows intelligence without uncontrolled autonomy.

---

# 4. Human-in-the-loop design

Human review should not mean every AI action requires manual approval.

Good systems use progressive autonomy.

Example:

Low risk:

```
AI completes automatically
```

Medium risk:

```
AI recommends
Human confirms
```

High risk:

```
AI prepares
Human decides
```

The objective is not maximum automation.

The objective is maximum safe automation.

---

# 5. Confidence and uncertainty

Confidence should be treated carefully.

A model saying:

```
I am 95% confident
```

does not necessarily mean:

```
There is a 95% probability the answer is correct.
```

Systems should combine:

- model confidence signals;
- retrieval evidence;
- validation results;
- historical accuracy;
- business impact.

---

# 6. Irreversible actions

The more irreversible the action, the stronger the boundary should be.

Examples:

Lower risk:

- draft email;
- summarise document;
- classify ticket.

Higher risk:

- issue refunds;
- change pricing;
- modify financial records;
- delete data;
- publish legal/compliance statements.

A useful rule:

```
Potential damage increases
        |
        v
Required validation increases
```

---

# 7. Validation architecture patterns

## Pattern: AI + Rules Engine

```
AI
 |
Recommendation
 |
Rules engine
 |
Action
```

Useful when policies are clear.

---

## Pattern: AI + Human Approval

```
AI
 |
Suggested action
 |
Human review
 |
Execution
```

Useful for uncertain or high-value decisions.

---

## Pattern: AI + Verification Agent

```
Agent A
 |
Creates answer
 |
Agent B
 |
Checks answer
 |
Final result
```

Useful where independent checking improves reliability.

---

# 8. Example: Commerce AI system

A commerce intelligence system should not directly do:

```
AI
 |
Change all product prices
```

Better:

```
AI analyses:
- sales velocity
- margin
- competitor pricing
- stock
- advertising

        |
        v

Recommendation

        |
        v

Pricing constraints

        |
        v

Approval policy

        |
        v

Marketplace update
```

This pattern applies to inventory, advertising, VAT and finance decisions.

---

# Common mistakes

## Mistake 1
"The model is accurate enough, so let it act."

Accuracy is not the same as operational safety.

## Mistake 2
Adding more agents instead of adding controls.

More reasoning does not replace governance.

## Mistake 3
Using prompts as business rules.

Business-critical rules belong in software.

## Mistake 4
No audit trail.

A production AI system must explain:

- what happened;
- why it happened;
- what data was used;
- what model acted;
- what tools were called.

---

# Mastery gate

You understand validation boundaries when you can:

- explain why model output cannot directly control critical actions;
- design validation layers around AI outputs;
- identify where deterministic code should replace AI judgement;
- design human approval workflows;
- protect sensitive actions with permissions and policies;
- build auditability into AI workflows;
- balance automation with reliability.

---

# Architectural principle

**The best AI systems are not those that give AI the most control. They are those that give AI the right level of control.**
