# Release and Versioning Policy

## Purpose

AI Systems Architect Roadmap is a living curriculum and architecture knowledge base. Releases provide stable, reviewable checkpoints without implying that AI technology stops changing.

## Version model

The project uses human-readable release tags:

```text
vMAJOR.MINOR
vMAJOR.MINOR.PATCH
```

### Major

Use a major release for changes that materially redefine the public curriculum contract, such as:

- replacing the 28-domain taxonomy;
- changing mastery/assessment semantics incompatibly;
- restructuring canonical domain identities;
- changing repository licensing in a way that requires explicit migration review.

### Minor

Use a minor release for substantial backward-compatible additions such as new or materially expanded curriculum, evidence/evaluation frameworks, supported learning paths or governance capabilities.

### Patch

Use a patch release primarily for backward-compatible corrections such as factual/source refreshes, broken links, editorial clarifications, security corrections and repository-maintenance fixes.

## Living-content rule

A release freezes the repository state, not the truth of every fast-moving claim. Time-sensitive claims should remain dated/versioned and evidence-aware.

## Release procedure

1. Build release engineering on a reviewable branch.
2. Run `python3 scripts/validate_repository.py --release`.
3. Open one cumulative pull request to `main`.
4. Require repository-quality CI to pass.
5. Resolve review findings without weakening the release gates.
6. Ensure a deliberate repository license exists before the first public v1 tag.
7. Merge to `main`.
8. Confirm CI on the exact merged `main` SHA.
9. Run `python3 scripts/validate_repository.py --tag-ready`.
10. Create the annotated `v1.0` tag on that exact main commit.
11. Publish the GitHub release using `docs/releases/v1.0-release-notes.md`.
12. Verify that the tag/release points to the intended main SHA.

## Why tags are not created on feature branches

A public release tag should identify the reviewed state users receive from the default branch. Tagging a feature branch before merge can create a release commit that is not actually the canonical repository state.

## Licensing gate

This repository is public and intended for broad collaboration, but a license is a legal choice by the maintainers.

Release automation deliberately does **not** invent a license. The first public v1 tag is blocked until a `LICENSE` or `LICENSE.md` file is deliberately selected and added.

## Required release evidence

Every release should retain:

- changelog entry;
- release notes;
- successful repository-quality CI;
- internal-link/Markdown validation;
- privacy/prohibited-term scan;
- high-signal secret scan;
- relevant editorial/security evaluation evidence;
- exact release commit SHA.

## Corrections after release

Published tags should not be silently moved. Correct `main`, document the correction and publish a patch release. Revoke/rotate any exposed credential rather than merely deleting it from the latest file.

## Principle

> A release is a reproducible evidence checkpoint, not a claim that the roadmap will never change.
