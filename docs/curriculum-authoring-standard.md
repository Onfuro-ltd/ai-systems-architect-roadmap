# Curriculum Authoring Standard

This document defines the minimum quality bar for educational content in AI Systems Architect Roadmap.

The repository is intended to scale to a large contributor community without becoming a collection of disconnected tutorials, vendor documentation rewrites or opinion pieces.

Every curriculum contribution should help a reader make better **systems decisions**.

## 1. Write for durable understanding

Prefer concepts that survive tool changes.

Good:

> Explain why tool schemas, permissions and retry semantics matter in agent systems.

Weak:

> Click these five buttons in Framework X.

Provider- or framework-specific examples are welcome when they teach a general principle, but the principle must remain visible.

## 2. State learning outcomes first

Every substantial module should define what a learner should be able to explain, build or decide after completing it.

Use observable outcomes such as:

- explain the difference between X and Y;
- implement a representative version;
- measure failure mode Z;
- choose between approaches under stated constraints;
- design an architecture with specified controls.

Avoid outcomes such as "understand AI better."

## 3. Explain the problem before the solution

Every technology exists in response to some constraint.

A topic should establish:

```text
previous approach
      ↓
limitation / bottleneck
      ↓
new idea
      ↓
new capability
      ↓
new trade-offs
```

Without this sequence, learners memorise terminology instead of architecture.

## 4. Separate mechanism from metaphor

Metaphors are useful for initial intuition, but they must not become technically false explanations.

Examples:

- an LLM is not literally a database;
- an MoE expert is not literally an employee;
- a context window is not durable memory;
- attention weights are not guaranteed explanations of reasoning;
- an agent is not automatically autonomous intelligence.

After using a metaphor, explain the actual mechanism at the appropriate depth.

## 5. Every module should connect four competency levels

### Understand
Explain concepts, terminology, purpose and trade-offs.

### Build
Create a representative implementation or experiment.

### Architect
Make a production decision involving reliability, security, cost, scale and integration.

### Lead
Define standards, governance, evaluation or organisational decision criteria where appropriate.

Not every introductory file needs a full leadership exercise, but it should not contradict the competency model.

## 6. Required module structure

Substantial curriculum modules should normally contain:

```text
Title
Purpose / framing
Learning outcomes
Core concepts
Architecture / mechanism
Important distinctions
Failure modes
Security / governance implications
Economics / performance implications
Practical build or experiment
Architect's checklist
Primary reading / sources
Mastery gate
```

Sections may be combined where that improves clarity. Do not force headings merely to satisfy a template.

## 7. Teach distinctions explicitly

Many AI failures arise from concept conflation.

High-value curriculum should explicitly separate concepts such as:

```text
model vs agent
context vs memory
retrieval vs generation
embedding similarity vs factual truth
training vs inference
fine-tuning vs RAG
MoE routing vs model routing
benchmark score vs production success
model confidence vs calibrated risk
capability vs permission
```

If two concepts are commonly confused, address the confusion directly.

## 8. Architecture diagrams should clarify responsibility

Prefer simple text/Mermaid diagrams that show information or control flow.

A good diagram answers at least one question:

- What calls what?
- Where does data move?
- Where is state stored?
- Where is policy enforced?
- Where can failure occur?
- Which component owns a responsibility?

Do not add decorative diagrams that provide no additional understanding.

## 9. Practical exercises must generate evidence

Avoid exercises whose only output is "the demo worked."

A strong exercise asks the learner to compare, measure or falsify an assumption.

Examples:

- compare two tokenizers on multilingual and structured data;
- measure retrieval recall under different chunking strategies;
- test an agent against tool failures;
- measure context length against latency and task success;
- compare a model-only answer with deterministic verification;
- inject adversarial inputs and record failures.

Where appropriate, require a baseline.

## 10. Include failure modes

A technology is not understood until its failure modes are understood.

At minimum consider:

- incorrect output;
- silent failure;
- distribution shift;
- stale information;
- context overflow;
- dependency/provider failure;
- permission error;
- prompt injection;
- data leakage;
- retries/duplicate actions;
- latency collapse;
- cost escalation;
- human review burden.

Only include failure modes relevant to the topic.

## 11. Include security where capability can affect data or actions

Security should not be isolated into one later chapter.

When a topic handles data, tools, memory, external services or actions, address:

- authentication;
- authorization;
- least privilege;
- tenant isolation;
- secret handling;
- data minimisation;
- prompt/tool injection;
- audit logs;
- approval requirements;
- destructive/irreversible actions.

Never suggest that a model should be the sole enforcement mechanism for an authorization decision.

## 12. Include economics and operations where relevant

An architecture that works only when cost and latency are ignored is incomplete.

Consider:

- tokens/request;
- accelerator memory;
- throughput;
- latency;
- concurrency;
- storage;
- external API cost;
- human review cost;
- maintenance burden;
- observability;
- failure recovery;
- cost per successful outcome.

Avoid reducing economics to vendor list price.

## 13. Prefer primary sources

For technical claims, source priority should normally be:

1. original research paper;
2. official specification or protocol documentation;
3. official technical documentation;
4. independent reproducible research;
5. credible production case study;
6. vendor marketing;
7. social-media commentary.

Use secondary explanations when they materially improve learning, but do not rely on them for foundational technical claims when primary material is available.

## 14. Date fast-moving claims

Architecture principles can be durable; model rankings and product features are not.

For claims likely to change, include:

- date checked;
- model/version;
- benchmark/version;
- pricing date where relevant;
- source.

Avoid writing "Model X is the best" without a task, metric and date.

## 15. Separate fact, inference and recommendation

Contributors should make it clear when a statement is:

- established by a cited source;
- observed in an experiment;
- inferred from evidence;
- a recommendation or opinion.

This is especially important for emerging agent and reasoning research.

## 16. Do not benchmark theatre

Benchmark results are useful evidence, not final truth.

When presenting a benchmark, state where possible:

- task/dataset;
- metric;
- model/version;
- prompting/inference method;
- hardware if relevant;
- sample size;
- known contamination concerns;
- whether results were independently reproduced.

For application decisions, prefer representative internal or reproducible task sets.

## 17. Vendor neutrality

The roadmap may discuss OpenAI, Anthropic, Google, Meta, Mistral, Alibaba/Qwen, DeepSeek, Microsoft, Amazon, NVIDIA and other vendors when relevant.

No vendor should become the implicit architecture.

When teaching a provider-specific capability:

1. state the general capability;
2. show where it sits in the architecture;
3. identify provider-specific implementation details;
4. note portability considerations;
5. compare credible alternatives where useful.

## 18. Keep proprietary systems out of public examples

Do not publish confidential business logic, private datasets, credentials, customer information, internal infrastructure details or proprietary decision algorithms.

Use synthetic or generic examples that preserve the educational lesson.

## 19. Mastery gates must require judgement

A mastery gate should not ask only for definitions.

Good:

> Design a permission-aware retrieval architecture and justify where semantic search stops and deterministic authorization begins.

Weak:

> Define RAG.

A strong mastery gate proves the learner can transfer knowledge to architecture.

## 20. Review checklist for maintainers

Before merging a substantial curriculum contribution, verify:

```text
[ ] learning outcomes are observable
[ ] problem and historical motivation are clear
[ ] mechanism is technically accurate
[ ] commonly confused concepts are distinguished
[ ] practical work generates measurable evidence
[ ] failure modes are included
[ ] security/governance is addressed where relevant
[ ] economics/operations are addressed where relevant
[ ] primary sources support important technical claims
[ ] fast-moving claims are dated/versioned
[ ] vendor-specific content is framed as an implementation, not the architecture
[ ] mastery gate requires real judgement
[ ] no confidential/proprietary information is exposed
```

## Final standard

A contribution is successful when a reader leaves with a more accurate mental model, has produced evidence through practical work, and can make a better architecture decision than they could before reading it.

**We are not optimising for the number of pages in this repository. We are optimising for the quality of judgement it produces.**
