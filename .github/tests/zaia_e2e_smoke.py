#!/usr/bin/env python3
"""ZAIA end-to-end smoke test.

This test validates the orchestration baseline end-to-end at repository level:
1) Core governance/config artifacts exist.
2) Scenario matrix includes S1-S9.
3) Subagent docs use shared contract references.
4) Template selection includes key routing additions.
5) Historical artifact validator runs and reports only known baseline issues.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List


REPO_ROOT = Path(__file__).resolve().parents[2]

REQUIRED_FILES = [
    ".github/copilot-instructions.md",
    ".github/agents/orchestrator.md",
    ".github/contracts/subagent-input-envelope.md",
    ".github/contracts/subagent-output-envelope.md",
    ".github/contracts/confidence-and-escalation.md",
    ".github/contracts/discrepancy-protocol.md",
    ".github/policies/model-routing-policy.md",
    ".github/policies/single-agent-exception-policy.md",
    ".github/policies/artifact-location-policy.md",
    ".github/orchestration/scenario-delegation-matrix.md",
    ".github/final-outputs/template-selection-rules.md",
    ".github/tests/orchestration_contract_validator.py",
]

AGENTS = [
    "backlog",
    "discovery",
    "domain",
    "integration",
    "knowledge-repository",
    "nfr",
    "process",
    "quality",
    "requirements",
    "risk-compliance",
]

KNOWN_VALIDATOR_ISSUES = {
    "Documents\\Analysis\\voltreserve-hub-enterprise-governance-review-T-20260430-001.md: Missing output envelope field: retrieval_first_performed",
    "Documents\\Analysis\\voltreserve-hub-enterprise-governance-review-T-20260430-001.md: Missing output envelope field: context_version",
    "Documents\\Analysis\\voltreserve-hub-governance-gate-assessment-T-20260430-001.md: Invalid TA-ID format (must end with UTC Z): TA-QUALITY-T-20260430-001-20260430T120000",
    "Documents\\Analysis\\vrh-e-fr-sd-coherence-validation-T-20260430-001.md: Missing output envelope field: retrieval_first_performed",
    "Documents\\Analysis\\vrh-e-fr-sd-coherence-validation-T-20260430-001.md: Missing output envelope field: context_version",
    "Documents\\Analysis\\vrh-e-fr-sd-coherence-validation-T-20260430-001.md: Missing output envelope field: confidence_rationale",
    "Documents\\Analysis\\Orchestration\\pilot-validation-report-T-20260510-001.md: Invalid TA-ID format (must end with UTC Z): TA-QUALITY-T-20260430-001-20260430T120000",
}


@dataclass
class CheckResult:
    name: str
    ok: bool
    details: str = ""


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def check_required_files() -> CheckResult:
    missing: List[str] = []
    for rel in REQUIRED_FILES:
        if not (REPO_ROOT / rel).exists():
            missing.append(rel)
    if missing:
        return CheckResult("required_files", False, "Missing: " + ", ".join(missing))
    return CheckResult("required_files", True)


def check_scenario_matrix() -> CheckResult:
    text = read_text(REPO_ROOT / ".github/orchestration/scenario-delegation-matrix.md")
    found = set(re.findall(r"\bS([1-9])\b", text))
    expected = set(str(i) for i in range(1, 10))
    if found != expected:
        return CheckResult("scenario_matrix", False, f"Expected S1-S9, found: {sorted(found)}")
    return CheckResult("scenario_matrix", True)


def check_agent_contract_refs() -> CheckResult:
    missing: List[str] = []
    for agent in AGENTS:
        path = REPO_ROOT / ".github" / "agents" / f"{agent}.md"
        text = read_text(path)
        required = [
            ".github/contracts/subagent-input-envelope.md",
            ".github/contracts/subagent-output-envelope.md",
            ".github/contracts/confidence-and-escalation.md",
        ]
        for marker in required:
            if marker not in text:
                missing.append(f"{path.as_posix()} -> {marker}")
    if missing:
        return CheckResult("agent_contract_refs", False, "Missing refs: " + " | ".join(missing))
    return CheckResult("agent_contract_refs", True)


def check_template_mapping() -> CheckResult:
    text = read_text(REPO_ROOT / ".github/final-outputs/template-selection-rules.md")
    required_markers = [
        "requirements-only clarification tasks -> Discovery Outcome Report with requirements addendum",
        "If a task spans multiple scenarios, select the template by dominant decision risk:",
    ]
    missing = [m for m in required_markers if m not in text]
    if missing:
        return CheckResult("template_mapping", False, "Missing markers: " + " | ".join(missing))
    return CheckResult("template_mapping", True)


def run_validator(python_cmd: List[str], target_path: str) -> CheckResult:
    cmd = python_cmd + [".github/tests/orchestration_contract_validator.py", "--path", target_path]
    proc = subprocess.run(
        cmd,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    output = (proc.stdout or "") + ("\n" + proc.stderr if proc.stderr else "")
    errors = []
    for line in output.splitlines():
        line = line.strip()
        if line.startswith("[ERROR]"):
            normalized = line.replace("[ERROR] ", "")
            normalized = normalized.replace(str(REPO_ROOT) + "\\", "")
            errors.append(normalized)

    unexpected = [e for e in errors if e not in KNOWN_VALIDATOR_ISSUES]
    if unexpected:
        return CheckResult(
            "artifact_validator",
            False,
            "Unexpected validator errors: " + " | ".join(unexpected),
        )

    if proc.returncode not in (0, 1):
        return CheckResult(
            "artifact_validator",
            False,
            f"Validator exited with unexpected code {proc.returncode}",
        )

    if errors:
        return CheckResult(
            "artifact_validator",
            True,
            f"Known baseline issues only: {len(errors)}",
        )

    return CheckResult("artifact_validator", True, "No errors")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run ZAIA E2E smoke test")
    parser.add_argument(
        "--python-cmd",
        nargs="+",
        default=[sys.executable],
        help="Python command prefix, e.g. python or conda run -n env python",
    )
    parser.add_argument(
        "--analysis-path",
        default="Documents/Analysis",
        help="Path passed to orchestration_contract_validator.py",
    )
    args = parser.parse_args()

    checks = [
        check_required_files(),
        check_scenario_matrix(),
        check_agent_contract_refs(),
        check_template_mapping(),
        run_validator(args.python_cmd, args.analysis_path),
    ]

    print("ZAIA E2E smoke results:")
    for c in checks:
        status = "PASS" if c.ok else "FAIL"
        if c.details:
            print(f"- {c.name}: {status} ({c.details})")
        else:
            print(f"- {c.name}: {status}")

    failed = [c for c in checks if not c.ok]
    if failed:
        print(f"\nOverall: FAIL ({len(failed)} checks failed)")
        return 1

    print("\nOverall: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


