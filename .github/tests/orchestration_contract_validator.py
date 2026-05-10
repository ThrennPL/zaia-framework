#!/usr/bin/env python3
"""ZAIA orchestration contract validator.

Validates markdown analysis artifacts for key contract checks:
1. TA-ID format with UTC Z suffix
2. Required output envelope fields in subagent artifacts
3. Basic final_status consistency checks
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List


TASK_FILE_RE = re.compile(r".*-T-\d{8}-\d{3}\.md$", re.IGNORECASE)
TA_ID_ANY_RE = re.compile(r"\bTA-[A-Z0-9\-]+-T-\d{8}-\d{3}-\d{8}T\d{6}Z?\b")
TA_ID_VALID_RE = re.compile(r"^TA-[A-Z0-9\-]+-T-\d{8}-\d{3}-\d{8}T\d{6}Z$")

ENVELOPE_REQUIRED = [
    "status",
    "technical_artifact",
    "retrieval_first_performed",
    "context_version",
    "confidence_score",
    "confidence_rationale",
    "positive_foundations",
    "remediation_proposals",
    "role_specific_value",
    "open_issues",
    "episodic_memory_entry",
    "source_links",
]


@dataclass
class Finding:
    severity: str
    file: Path
    message: str


@dataclass
class ValidationResult:
    findings: List[Finding]

    @property
    def has_errors(self) -> bool:
        return any(f.severity == "error" for f in self.findings)


def iter_target_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.md"):
        if TASK_FILE_RE.match(path.name):
            yield path


def check_ta_id_format(path: Path, text: str, findings: List[Finding]) -> None:
    for token in TA_ID_ANY_RE.findall(text):
        if not TA_ID_VALID_RE.match(token):
            findings.append(
                Finding(
                    severity="error",
                    file=path,
                    message=f"Invalid TA-ID format (must end with UTC Z): {token}",
                )
            )


def check_output_envelope(path: Path, text: str, findings: List[Finding]) -> None:
    lower = text.lower()
    if "required output envelope" not in lower:
        return

    for field in ENVELOPE_REQUIRED:
        if field.lower() not in lower:
            findings.append(
                Finding(
                    severity="error",
                    file=path,
                    message=f"Missing output envelope field: {field}",
                )
            )


def check_final_status_consistency(path: Path, text: str, findings: List[Finding]) -> None:
    lower = text.lower()
    if "final_status:" not in lower:
        return

    in_review = re.search(r"^\s*final_status:\s*in_review\s*$", text, re.IGNORECASE | re.MULTILINE)
    if not in_review:
        return

    verdict_markers = [
        "final team verdict",
        "gate 0:",
        "gate 1:",
        "no-go",
        "go/no-go",
    ]
    if any(marker in lower for marker in verdict_markers):
        findings.append(
            Finding(
                severity="error",
                file=path,
                message="final_status is in_review but final verdict markers are present.",
            )
        )


def validate_file(path: Path) -> ValidationResult:
    text = path.read_text(encoding="utf-8", errors="replace")
    findings: List[Finding] = []
    check_ta_id_format(path, text, findings)
    check_output_envelope(path, text, findings)
    check_final_status_consistency(path, text, findings)
    return ValidationResult(findings=findings)


def run(root: Path) -> int:
    all_findings: List[Finding] = []
    files = list(iter_target_files(root))

    if not files:
        print(f"No target markdown files found under: {root}")
        return 0

    for file_path in files:
        result = validate_file(file_path)
        all_findings.extend(result.findings)

    if not all_findings:
        print(f"Validation passed. Checked {len(files)} file(s).")
        return 0

    errors = [f for f in all_findings if f.severity == "error"]
    warnings = [f for f in all_findings if f.severity == "warning"]

    for finding in all_findings:
        print(f"[{finding.severity.upper()}] {finding.file}: {finding.message}")

    print("\nSummary:")
    print(f"- files_checked: {len(files)}")
    print(f"- errors: {len(errors)}")
    print(f"- warnings: {len(warnings)}")

    return 1 if errors else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate ZAIA orchestration markdown contracts.")
    parser.add_argument(
        "--path",
        default="Documents/Analysis",
        help="Directory to scan for TASK-ID markdown artifacts (default: Documents/Analysis)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.path)
    if not root.exists():
        print(f"Path does not exist: {root}")
        return 2
    return run(root)


if __name__ == "__main__":
    sys.exit(main())


