# v1.0 Repository Audit and Hardening Plan

Date: 2026-09-18

## Executive status

The authoritative master roadmap defines 28 domains and Domains 12–28 now have dedicated curriculum tracks, but the repository is not yet ready to be labelled a clean v1.0 release.

The audit found four release blockers:

1. **Privacy leakage:** the initial repository audit identified private-project references across more than 50 curriculum files. These references required removal or conversion into generic public examples before promotion.
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

### P1 — Restore authoritative 28-domain structure — COMPLETE

- [x] Create dedicated Domain 08 Memory Systems.
- [x] Create dedicated Domain 09 Orchestration and Multi-Agent Systems.
- [x] Create dedicated Domain 10 Evaluation and Reliability.
- [x] Audit Domain 06 and Domain 07 against the master roadmap and separate their curriculum boundaries.
- [x] Verify Domain 11 against the authoritative Security, Permissions and Governance scope.
- [x] Give every roadmap domain an explicit authoritative repository home.
- [x] Make root and master-roadmap navigation resolve to those authoritative homes.

P1 completion evidence is recorded in [`roadmap/domain-directory-map.md`](../roadmap/domain-directory-map.md).

Legacy combined and supplemental tracks remain intentionally present. Their chapter-by-chapter migration, archival or supplemental classification belongs to P2 and is not treated as complete by this checkpoint.

### P2 — Consolidate duplicate and legacy tracks — COMPLETE

- [x] Map every legacy chapter to an authoritative domain or mark it supplemental.
- [x] Preserve useful historical material rather than deleting it.
- [x] Remove legacy tracks from authoritative root navigation by archiving or supplemental classification.
- [x] Consolidate Domain 18 to one canonical root chapter structure while preserving the earlier detailed set for P3 review.

P2 completion evidence is recorded in [`docs/legacy-supplemental-content-map.md`](./legacy-supplemental-content-map.md).

Archived content is not authoritative. Supplemental content extends the roadmap without creating extra authoritative domains.

### P3 — Editorial normalization — COMPLETE

For every authoritative domain:

- [x] README and chapter links resolve.
- [x] Naming matches the master roadmap and authoritative directory map.
- [x] Learning objectives are explicit.
- [x] Practical/architectural exercises are present in non-capstone modules.
- [x] Concepts, architecture, failure modes, security/governance and evaluation are represented where relevant.
- [x] Private examples are absent.
- [x] Editorial terminology and domain naming are normalized.
- [x] Fast-moving comparative claims are screened with evidence/date-aware rules.
- [x] The curriculum authoring standard is applied as the review baseline.
- [x] Domain 16 depth is materially normalized.
- [x] Durable detail from the archived Domain 18 structure is merged into the canonical track.

P3 completion evidence is recorded in [`docs/p3-editorial-normalization-report.md`](./p3-editorial-normalization-report.md).

### P4 — Repository navigation and contributor experience — COMPLETE

- [x] Replace stale Foundations-only emphasis with complete 28-domain navigation.
- [x] Add a completion/status matrix.
- [x] Add prerequisites and recommended paths.
- [x] Add cross-domain prerequisite/next-step links.
- [x] Validate and strengthen CONTRIBUTING, SECURITY and Code of Conduct while retaining the authoring standard and decision framework as canonical quality/evidence references.
- [x] Add issue and pull-request templates.

P4 completion evidence is recorded in [`docs/p4-navigation-contributor-experience-report.md`](./p4-navigation-contributor-experience-report.md).

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
