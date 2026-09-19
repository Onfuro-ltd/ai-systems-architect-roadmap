#!/usr/bin/env python3
"""Repository quality gate for AI Systems Architect Roadmap.

Uses only the Python standard library so it can run locally and in GitHub Actions.
No private/project names are stored here: prohibited names are represented only by
SHA-256 fingerprints of normalized one- or two-token phrases.
"""

from pathlib import Path
from urllib.parse import unquote
import argparse
import hashlib
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]

PROHIBITED_TERM_HASHES = {
    '10ab38744758dadfe313350a37e88fc4f3331c0cbbd640f87538fa50c5c6000f',
    '3037de29798f46fc407354758a0a562ce898666262dcc0ada088f25aeb4a4b82',
    '3d15867b1c665502f91006ef71904e695f8b58e012772df3e207361012651d91',
    '5d1b5846b081d8f3a697cf2c741ed0fc0f4fe1e0f61f0298a535ca2f7ba7f3de',
    'b3384fd6a791071f5602416530560f8ab0ea71e0485ee2e629904fef38749ea0',
    'c0abcf570e13b7544663a47a64f5c6e588c38a3f497d451ac8fe3035ae2d5aa4',
    'cdd07bc2a9e5e4348cbae597f63d2482a2cde886dbafffa2920d97dad30e2bc7',
    'f687e3d36b0cad7cb1d9677d5a83fe530307d232118f43564d1dc6a04d797ac3',
    'fe1057a6fbdafc1b02ed474bfb724db02b7cc5375fd7116ffd441d0166a55259'
}

SECRET_PATTERNS = [
    ("AWS access key", re.compile(r"(?<![A-Z0-9])AKIA[0-9A-Z]{16}(?![A-Z0-9])")),
    ("GitHub token", re.compile(r"(?<![A-Za-z0-9])gh[pousr]_[A-Za-z0-9]{36,255}")),
    ("GitHub fine-grained token", re.compile(r"github_pat_[A-Za-z0-9_]{50,255}")),
    ("OpenAI-style secret", re.compile(r"(?<![A-Za-z0-9])sk-[A-Za-z0-9_-]{20,}")),
    ("Slack token", re.compile(r"(?<![A-Za-z0-9])xox[baprs]-[A-Za-z0-9-]{10,}")),
    ("Google API key", re.compile(r"AIza[0-9A-Za-z_-]{35}")),
    ("Stripe live secret", re.compile(r"sk_live_[0-9A-Za-z]{16,}")),
    ("Private key material", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
]

TEXT_SUFFIXES = {
    ".md", ".txt", ".py", ".yml", ".yaml", ".json", ".toml", ".ini",
    ".cfg", ".conf", ".sh", ".ps1", ".xml", ".csv", ".tsv",
}

REQUIRED_BASE = [
    "README.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "roadmap/master-roadmap.md",
    "roadmap/domain-directory-map.md",
    "roadmap/domain-status.md",
    "roadmap/prerequisites-and-paths.md",
    "docs/curriculum-authoring-standard.md",
    "docs/decision-framework.md",
    "ai-operating-system/10-final-ai-operating-system-capstone.md",
]

REQUIRED_RELEASE = [
    "scripts/validate_repository.py",
    ".github/workflows/repository-quality.yml",
    "docs/release-policy.md",
    "docs/v1.0-release-checklist.md",
    "docs/releases/v1.0-release-notes.md",
    "CHANGELOG.md",
]

DOMAIN_READMES = [
    "foundations/README.md",
    "application-engineering/README.md",
    "knowledge-systems-rag/README.md",
    "agents/README.md",
    "06-skills-agent-harnesses/README.md",
    "07-mcp-tool-ecosystems/README.md",
    "08-memory-systems/README.md",
    "09-orchestration-multi-agent/README.md",
    "10-evaluation-reliability/README.md",
    "11-security-permissions-governance/README.md",
    "ai-system-design/README.md",
    "data-event-architecture/README.md",
    "open-source-local-ai/README.md",
    "fine-tuning-specialist-models/README.md",
    "gpu-inference-infrastructure/README.md",
    "mlops-llmops/README.md",
    "multimodal-ai/README.md",
    "computer-use-interface-agents/README.md",
    "physical-ai-robotics/README.md",
    "ai-economics-model-routing/README.md",
    "enterprise-ai/README.md",
    "ai-product-design/README.md",
    "business-automation/README.md",
    "decision-intelligence/README.md",
    "domain-specific-ai-systems/README.md",
    "ai-native-commerce-operations/README.md",
    "ai-operating-system/README.md",
]

def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()

def tracked_files():
    raw = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT)
    return [ROOT / x.decode("utf-8") for x in raw.split(b"\0") if x]

def read_text(path):
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None

def candidate_private_fingerprints(text):
    words = re.findall(r"[a-z0-9]+", text.lower())
    for i, word in enumerate(words):
        yield hashlib.sha256(word.encode()).hexdigest()
        if i + 1 < len(words):
            phrase = word + " " + words[i + 1]
            yield hashlib.sha256(phrase.encode()).hexdigest()

def contains_prohibited_term(text):
    return any(h in PROHIBITED_TERM_HASHES for h in candidate_private_fingerprints(text))

def secret_hits(text):
    hits = []
    for label, rx in SECRET_PATTERNS:
        for match in rx.finditer(text):
            # Permit obviously synthetic placeholders.
            line_start = text.rfind("\n", 0, match.start()) + 1
            line_end = text.find("\n", match.end())
            if line_end < 0:
                line_end = len(text)
            line = text[line_start:line_end].lower()
            if any(marker in line for marker in (
                "example", "placeholder", "redacted", "your_", "<token>",
                "<secret>", "fake", "dummy"
            )):
                continue
            hits.append(label)
            break
    return hits

def relative_link_issues(path, text):
    issues = []
    # Markdown links/images. External URLs and local anchors are intentionally skipped.
    for m in re.finditer(r"!?\[[^\]]*\]\(([^)]+)\)", text):
        target = m.group(1).strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "tel:", "#")):
            continue
        # Strip optional Markdown title after a space if the target is not wrapped in <>.
        if target.startswith("<") and ">" in target:
            target = target[1:target.index(">")]
        elif " " in target:
            target = target.split(" ", 1)[0]
        target = unquote(target.split("#", 1)[0])
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            issues.append(target)
    return issues

def validate_current_tree(release=False, tag_ready=False):
    errors = []
    files = tracked_files()

    required = list(REQUIRED_BASE)
    if release or tag_ready:
        required += REQUIRED_RELEASE
    if tag_ready:
        if not ((ROOT / "LICENSE").is_file() or (ROOT / "LICENSE.md").is_file()):
            errors.append("Tag-ready gate: repository license is missing (LICENSE or LICENSE.md).")

    for rel in required:
        if not (ROOT / rel).exists():
            errors.append(f"Required path missing: {rel}")

    for rel in DOMAIN_READMES:
        if not (ROOT / rel).is_file():
            errors.append(f"Authoritative domain README missing: {rel}")

    for path in files:
        rel = path.relative_to(ROOT)
        # Read text-like files plus all Markdown. Skip binaries safely.
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {
            "LICENSE", "Dockerfile", "Makefile"
        }:
            continue
        text = read_text(path)
        if text is None:
            errors.append(f"Text file is not valid UTF-8: {rel}")
            continue
        if "\ufffd" in text:
            errors.append(f"UTF-8 replacement character present: {rel}")
        if contains_prohibited_term(text):
            errors.append(f"Prohibited private-term fingerprint found: {rel}")
        for label in secret_hits(text):
            errors.append(f"Possible {label} found: {rel}")

        if path.suffix.lower() == ".md":
            if text.count("```") % 2:
                errors.append(f"Unbalanced fenced code block: {rel}")
            for target in relative_link_issues(path, text):
                errors.append(f"Broken internal Markdown link: {rel} -> {target}")

    capstone = ROOT / "ai-operating-system/10-final-ai-operating-system-capstone.md"
    if capstone.is_file():
        cap_text = capstone.read_text(encoding="utf-8")
        if "## Prerequisite domains" not in cap_text:
            errors.append("Final Domain 28 capstone lacks prerequisite-domain navigation.")

    if release or tag_ready:
        workflow = ROOT / ".github/workflows/repository-quality.yml"
        if workflow.is_file():
            wt = workflow.read_text(encoding="utf-8")
            if "scripts/validate_repository.py --release" not in wt:
                errors.append("Repository-quality workflow does not invoke the release gate.")

    return errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--release", action="store_true",
                        help="require P5 release-engineering artifacts")
    parser.add_argument("--tag-ready", action="store_true",
                        help="require release artifacts plus a repository LICENSE")
    args = parser.parse_args()

    errors = validate_current_tree(release=args.release or args.tag_ready,
                                   tag_ready=args.tag_ready)
    if errors:
        print("REPOSITORY QUALITY GATE=FAIL")
        for error in errors:
            print(" -", error)
        return 1

    print("PASS: required repository structure")
    print("PASS: UTF-8 and Markdown fence checks")
    print("PASS: internal Markdown links")
    print("PASS: prohibited private-term fingerprint scan")
    print("PASS: high-signal secret scan")
    if args.release or args.tag_ready:
        print("PASS: P5 release-engineering artifacts")
    if args.tag_ready:
        print("PASS: repository license present")
        print("TAG-READY QUALITY GATE=PASS")
    else:
        print("REPOSITORY QUALITY GATE=PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
