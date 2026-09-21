# Security Policy

## Purpose

AI systems and AI engineering repositories can expose security risks through code, examples, integrations, credentials, data, workflows and guidance. This policy explains how to report security concerns about this repository and the practices contributors should follow.

## Supported content

Security reports are most useful when they concern:

- repository automation or CI behaviour;
- scripts or examples that could expose credentials or execute unsafe actions;
- published guidance that would create a material security vulnerability if followed;
- accidental publication of secrets, private data or proprietary information;
- dependency or supply-chain risks introduced by repository-owned code;
- AI-specific security issues such as prompt/tool injection, excessive permissions, cross-tenant leakage or unsafe autonomous actions.

General disagreements about architecture or AI-safety philosophy belong in normal issues/discussions rather than confidential vulnerability reporting.

## Reporting a vulnerability

**Do not publish sensitive vulnerability details in a public issue or pull request.**

When GitHub's **Private vulnerability reporting / Report a vulnerability** control is available for this repository, use it.

If no private reporting control is available, open a minimal public issue that says you need a private security contact **without including exploit details, credentials, personal data or other sensitive material**. A maintainer can then provide an appropriate private channel.

## What to include

Where safe, provide:

- affected file, workflow or component;
- impact and realistic attack path;
- reproduction steps or proof of concept;
- required permissions/preconditions;
- suggested mitigation if known;
- whether secrets or personal data may have been exposed.

Never include live credentials in the report.

## Coordinated disclosure

Please allow maintainers to investigate and prepare a correction before publishing exploit details that could put users at risk. Repository history may remain public even after a fix, so secrets must be rotated rather than merely deleted from the latest commit.

## Contributor security requirements

Contributors must not submit:

- API keys, tokens, passwords or private certificates;
- customer or employee data;
- proprietary company datasets or business logic;
- private infrastructure addresses or credentials;
- examples that grant models unrestricted production permissions.

AI-related contributions should prefer least privilege, deterministic authorization boundaries, explicit approval for consequential actions, tenant isolation, secret separation, auditability and evaluation before autonomy.

## Dependency and example safety

When adding code or dependencies:

- prefer maintained, reviewable dependencies;
- pin or constrain versions where reproducibility/security requires it;
- avoid scripts that download and execute unverified remote code;
- keep secrets out of prompts, logs and model-visible context;
- sandbox generated or untrusted code where execution is required.

## Security is cross-cutting

Security is not isolated to Domain 11. Any domain that handles data, tools, memory, external systems, code execution or consequential action should address the relevant controls.

See [Domain 11 — Security, Permissions and Governance](./11-security-permissions-governance/README.md) and the [Curriculum Authoring Standard](./docs/curriculum-authoring-standard.md).
