# P5 Release Engineering Report

## Result

> **P5 release engineering: PASS for release-candidate preparation.**

The engineering gates are implemented and passing. The public v1.0 tag is intentionally not created on the P5 feature branch.

## Automated repository gate

Added:

- `scripts/validate_repository.py`
- `.github/workflows/repository-quality.yml`

The validator checks required structure, UTF-8 integrity, Markdown fences, internal links, authoritative domain homes, final-capstone prerequisite navigation, prohibited private-term fingerprints and high-signal credential patterns.

The prohibited private names themselves are not stored in the public validator; only one-way SHA-256 fingerprints are committed.

## Reachable-history checks

The local P5 runner additionally scanned all reachable commits for prohibited private terms, prohibited commit-message terms and high-signal credential patterns. These checks passed before P5 closure.

## CI

GitHub Actions now runs the release-quality validator for pull requests, pushes to `main` and manual dispatch.

## Release policy

`docs/release-policy.md` defines version semantics, canonical-main tagging, evidence requirements and correction policy.

## v1.0 preparation

Prepared:

- `docs/v1.0-release-checklist.md`
- `docs/releases/v1.0-release-notes.md`
- updated `CHANGELOG.md`
- updated root release-candidate status.

## Intentional publication blockers

### Repository license — RESOLVED AFTER P5 ENGINEERING CLOSURE

No `LICENSE`/`LICENSE.md` existed at the P4 checkpoint, so P5 correctly left licensing as a deliberate maintainer decision.

Before the v1.0 merge, the maintainers selected and added a scoped dual-license model:

- Apache License 2.0 for software/code;
- Creative Commons Attribution 4.0 International for curriculum/documentation.

The root `LICENSE` defines scope and the complete license texts are retained under `LICENSES/`.

### Canonical main — STILL REQUIRED

The cumulative P5 branch must be reviewed and merged into `main`, followed by green CI on the exact merged main SHA.

## Tag rule

Only after the license and canonical-main gates are satisfied should maintainers run:

```bash
python3 scripts/validate_repository.py --tag-ready
git tag -a v1.0 -m "AI Systems Architect Roadmap v1.0"
git push github v1.0
```

The tag belongs on the verified `main` SHA, not on the feature branch.

## Interpretation

P0–P5 engineering hardening is complete as a release candidate.

**v1.0 publication is not yet complete** until the unchecked final-publication items in the release checklist are actually satisfied.
