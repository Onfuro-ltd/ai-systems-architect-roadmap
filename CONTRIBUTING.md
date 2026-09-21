# Contributing to AI Systems Architect Roadmap

Thank you for contributing to **AI Systems Architect Roadmap**.

This project is intended to become a long-lived, evidence-driven knowledge resource for people designing and operating AI-native systems. We welcome contributors, but we deliberately maintain a higher bar than a typical link collection or tutorial repository.

The objective is not to collect more AI content. The objective is to improve the quality of technical and architectural judgement.

## Read before contributing

Please read:

1. [Curriculum Authoring Standard](./docs/curriculum-authoring-standard.md)
2. [AI Technology Decision Framework](./docs/decision-framework.md)
3. [Master Roadmap](./roadmap/master-roadmap.md)
4. [Assessment Model](./roadmap/assessment-model.md)
5. [Security Policy](./SECURITY.md)
6. [Code of Conduct](./CODE_OF_CONDUCT.md)

Substantial curriculum pull requests that do not follow the authoring standard may be asked to change structure or evidence before content-level review.

## Valuable contributions

High-value contributions include:

- durable AI architecture principles;
- technically rigorous curriculum modules;
- reproducible experiments;
- evaluation methodologies and datasets that can be shared safely;
- AI security and governance practices;
- agent, memory, RAG, MCP and orchestration patterns;
- inference and infrastructure analysis;
- architecture decision records and failure analyses;
- well-scoped technology evaluations;
- case studies that distinguish evidence from opinion;
- corrections supported by primary or stronger evidence.

Low-value contributions include:

- undifferentiated lists of AI tools;
- promotional vendor copy;
- social-media claims presented as fact;
- tutorial rewrites that add no architectural understanding;
- benchmark claims without methodology/context;
- mass-generated content that has not been technically reviewed;
- duplicate technologies that occupy an existing architectural responsibility without meaningful comparison.

## Curriculum contributions

Curriculum content should normally include:

```text
Purpose / problem
Learning outcomes
Core mechanism
Architecture
Important distinctions
Failure modes
Security / governance
Economics / operations
Practical experiment
Architect's checklist
Primary sources
Mastery gate
```

See the full [Curriculum Authoring Standard](./docs/curriculum-authoring-standard.md).

Practical exercises should produce evidence. A happy-path demo is not sufficient proof of understanding or reliability.

## Technology submissions

When proposing a model, framework, protocol, tool or architectural pattern, evaluate it using the [AI Technology Decision Framework](./docs/decision-framework.md).

At minimum include:

1. one-sentence description without marketing language;
2. problem solved;
3. architectural layer;
4. what is genuinely new;
5. evidence;
6. limitations and failure modes;
7. security/governance implications;
8. economic/operational implications;
9. credible alternatives;
10. production maturity;
11. current verdict;
12. what evidence would change the verdict.

Available Technology Radar verdicts are:

- **IGNORE**
- **WATCH**
- **EXPERIMENT**
- **ADOPT**
- **BUILD AROUND**

A verdict is not a permanent endorsement. It should change when evidence, maturity or architecture changes.

## Source quality

Prefer sources in roughly this order:

1. original research papers;
2. official specifications;
3. official technical documentation;
4. independently reproducible research;
5. credible production case studies;
6. vendor benchmarks;
7. social-media commentary.

Use secondary material when it improves understanding, but foundational claims should be grounded in primary sources where practical.

For fast-moving claims, include dates and versions.

## Fact, observation and recommendation

Make it clear whether a statement is:

- sourced fact;
- result of a reproducible experiment;
- inference from evidence;
- recommendation/opinion.

Do not present an inference or vendor claim as settled fact.

## Pull request scope

Prefer focused pull requests that reviewers can reason about deeply.

Good examples:

```text
Add transformer attention module
Add reproducible context-window experiment
Correct MoE active-parameter explanation
Evaluate framework X against existing agent-harness criteria
```

Avoid combining unrelated curriculum areas and technology reviews in one very large change unless there is a clear structural reason.

## Changes to architecture or taxonomy

Changes to any of the following deserve stronger review:

- master roadmap domains;
- competency model;
- assessment methodology;
- Technology Radar verdict definitions;
- security principles;
- cross-cutting architectural terminology.

Such changes should explain:

```text
Current design
Problem with current design
Proposed change
Evidence/rationale
Migration impact
Alternatives considered
```

## Reproducibility

Benchmarks and experiments should document enough context for another contributor to reproduce or meaningfully interpret the result.

Where relevant include:

- model and version;
- date;
- dataset/test-set version;
- inference configuration;
- prompts/instructions if publishable;
- hardware;
- sample size;
- validation method;
- cost assumptions;
- known limitations.

Do not upload credentials, customer data, private datasets or proprietary company information.

## Security

Security is a cross-cutting requirement, not a separate optional topic.

Contributions involving agents, tools, memory, external systems or data access should consider:

- authentication;
- authorization;
- least privilege;
- data minimisation;
- tenant isolation;
- secret management;
- prompt/tool injection;
- approval gates;
- auditability;
- destructive or irreversible actions.

Do not propose a model as the sole enforcement mechanism for permissions or critical invariants.

## Vendor neutrality

Vendor-specific examples are allowed and often useful. However:

- teach the general capability first;
- state which details are provider-specific;
- discuss portability where relevant;
- avoid making one vendor's product structure the repository's architecture.

## Writing quality

Write clearly enough for a motivated learner while preserving technical accuracy.

Prefer:

- precise terminology;
- short architecture diagrams;
- concrete examples;
- explicit trade-offs;
- measurable exercises.

Avoid:

- unexplained buzzwords;
- anthropomorphic claims presented as mechanisms;
- unsupported superlatives;
- unnecessary complexity;
- filler generated merely to make a section longer.

## Issue and pull request workflow

Use the repository's issue templates so reports arrive with enough context to act on:

- **Curriculum / correction** — missing topics, technical corrections, broken learning flow or evidence gaps;
- **Technology evaluation** — proposals to evaluate a model, framework, protocol, product or pattern;
- **Repository improvement** — navigation, contributor experience, automation or maintenance work.

Before opening a new issue, check the [Master Roadmap](./roadmap/master-roadmap.md), [Domain Status Matrix](./roadmap/domain-status.md) and existing issues to avoid duplicate taxonomy.

Pull requests should:

- address one coherent problem;
- link the relevant issue when one exists;
- explain why the change improves architectural judgement;
- identify primary sources for material technical claims;
- state important failure/security/economic implications where relevant;
- confirm that no secrets, private data or proprietary implementation details were added;
- update navigation when files or domain boundaries change.

Use the pull request template as a review contract rather than deleting its checklist.

## Branch and commit scope

Branch names should communicate intent, for example:

```text
curriculum/<domain>-<topic>
fix/<short-description>
docs/<short-description>
repo/<short-description>
```

Prefer a small number of coherent commits that preserve reviewable checkpoints. Avoid mixing taxonomy changes, large editorial rewrites and unrelated fixes unless the migration genuinely requires them.

## AI-assisted contributions

AI tools may assist research, drafting, editing or coding, but contributors remain responsible for every submitted claim and line of code.

AI-assisted content must still:

- satisfy the curriculum authoring standard;
- use real, inspectable sources rather than fabricated citations;
- distinguish uncertain/inferred claims;
- avoid private or proprietary information;
- be technically reviewed by the contributor before submission.

Mass-generated content that merely satisfies headings is not an acceptable contribution.


## Licensing of contributions

This repository uses two licenses with explicit scope. Read the root [LICENSE](./LICENSE) before contributing.

Unless maintainers explicitly agree otherwise before accepting a contribution:

- standalone software, scripts, automation, configuration and other code-like contributions are submitted under **Apache License 2.0**;
- curriculum, documentation, prose, diagrams and other educational-content contributions are submitted under **Creative Commons Attribution 4.0 International**;
- code snippets contributed inside documentation may also be reused under **Apache License 2.0** as described in the root licensing notice.

Do not contribute material you do not have the right to license under the applicable terms. Third-party material must retain its original licensing and attribution requirements.

By intentionally submitting a contribution for inclusion in this repository, you confirm that you have authority to submit it under the applicable project license.

## Repository validation

Before submitting a pull request, run:

```bash
python3 scripts/validate_repository.py --release
```

The validator uses only the Python standard library and checks required repository structure, UTF-8/Markdown fence integrity, internal Markdown links, prohibited private-term fingerprints and high-signal credential patterns.

The same gate runs in GitHub Actions. Release/tag preparation has an additional `--tag-ready` mode that also requires the repository license.


## Maintainer review principle

A contribution should leave the reader able to make a **better architecture decision** than before reading it.

If it only increases the amount of content in the repository, it is not enough.

## Community standard

Disagreement about architecture, research interpretation or technology maturity is welcome when it is evidence-based and respectful.

The project should be willing to change its conclusions when better evidence appears.

That is a feature, not a weakness.
