# v1.0 Repository Audit and Hardening Plan

Date: 2026-09-18

## Executive status

The authoritative master roadmap defines 28 domains and Domains 12–28 now have dedicated curriculum tracks, but the repository is not yet ready to be labelled a clean v1.0 release.

The audit found four release blockers:

1. **Privacy leakage:** a repository-wide code search for the private project name `example platform` returns more than 50 curriculum files. These references must be removed or rewritten as generic public examples before promotion.
2. **Authoritative-domain gap:** Domains 08 (Memory Systems), 09 (Orchestration and Multi-Agent Systems), and 10 (Evaluation and Reliability) do not currently have dedicated curriculum directories matching the master roadmap.
3. **Domain 06/07 structural overlap:** `mcp-skills-tools/` combines material belonging to both Skills and Agent Harnesses and MCP/Tool Ecosystems. It should be audited and separated or explicitly mapped without losing useful material.
4. **Legacy/supplemental overlap:** older tracks such as `open-source-models-infrastructure/` and `ai-product-engineering-commercialisation/` overlap later authoritative domains and contain private-project references. They require classification, sanitization and either archival, migration or explicit supplemental status.

## Confirmed consistency issues

### Root README

The root README still states:

> Current stage: Foundations curriculum / early public architecture.

That status is stale now that the 28-domain curriculum sequence has been built. The root navigation also exposes only the Foundations track rather than a complete domain index.

### Domain 18

`multimodal-ai/README.md` describes an older nine-part curriculum and links to older filenames while a newer ten-chapter Domain 18 track also exists. The README and file set need consolidation.

### Domain 16

The GPU and inference infrastructure track is structurally complete, but several chapters are materially shorter than the later enterprise-level standard. Depth should be normalized during editorial review.

### Domain 12 and broader privacy

The known Domain 12 private references are part of a larger problem. Search confirms private-project naming in Agents, MCP/Skills, Security/Governance, Multimodal, legacy Open-Source Infrastructure, supplemental Product/Commercialisation and AI System Design content.

## Release hardening sequence

### P0 — Privacy and public-safety cleanup

- Remove private project/company implementation references from all public curriculum.
- Replace only with generic examples where the lesson remains useful.
- Search for related proprietary names and internal implementation details, not just one project name.
- Re-run repository-wide privacy search before release.

### P1 — Restore authoritative 28-domain structure

- Create dedicated Domain 08 Memory Systems.
- Create dedicated Domain 09 Orchestration and Multi-Agent Systems.
- Create dedicated Domain 10 Evaluation and Reliability.
- Audit Domain 06 and Domain 07 against the master roadmap and separate their curriculum boundaries.
- Verify Domain 11 against the authoritative Security, Permissions and Governance scope.

### P2 — Consolidate duplicate and legacy tracks

- Map every legacy chapter to an authoritative domain or mark it supplemental.
- Avoid deleting useful material until migration is verified.
- Remove contradictory or stale navigation.
- Consolidate Domain 18 old/new chapter structure.

### P3 — Editorial normalization

For every authoritative domain verify:

- README and chapter links resolve.
- Naming matches the master roadmap.
- learning objectives are explicit;
- concepts, architecture, failure modes, security, evaluation and exercises are present where relevant;
- private examples are absent;
- terminology is consistent;
- model/vendor claims are evidence-aware and time-sensitive claims are sourced;
- chapters meet the curriculum authoring standard.

### P4 — Repository navigation and contributor experience

- Replace Foundations-only root navigation with all 28 domains.
- Add a completion/status matrix.
- Add prerequisites and recommended paths.
- Add cross-domain links.
- Validate CONTRIBUTING, SECURITY, Code of Conduct, authoring standard and decision framework.
- Add issue/PR templates if absent.

### P5 — Release engineering

- Run link and Markdown validation.
- Run privacy/secret scanning.
- Add CI checks for broken internal links and prohibited private terms.
- Define versioning/release policy.
- Produce v1.0 changelog/release notes.
- Tag v1.0 only after P0–P5 gates pass.

## v1.0 release gate

The repository should not be called v1.0-ready until:

- all 28 authoritative domains have an explicit home;
- no private implementation references remain;
- duplicate tracks are classified;
- navigation resolves to the authoritative curriculum;
- internal links pass;
- curriculum depth/format has been reviewed;
- privacy and secret scans pass;
- the final AI Operating System capstone links back to the prerequisite domains.

## Principle

> Curriculum completion and repository release readiness are different milestones. The content can be broad enough to cover the roadmap while the repository still needs structural, privacy, editorial and release-engineering hardening.
