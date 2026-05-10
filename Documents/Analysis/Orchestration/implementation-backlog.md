# ZAIA Orchestration Implementation Backlog

Status: active
Owner: orchestrator governance

## Execution Policy
- Priority order: P0 -> P1 -> P2.
- Do not start a blocked task before dependencies are resolved.
- Each completed task must reference changed files and verification evidence.

## Tasks

### P0

1. ZAD-001 Scenario catalog S1-S9
- Goal: define operational scenarios and triggers.
- Dependencies: none.
- Output: scenario list with gate in/out and risks.
- Status: completed.
- Evidence: .github/orchestration/scenario-delegation-matrix.md

2. ZAD-002 Agent mapping by scenario
- Goal: define required and supplemental agent sets per scenario.
- Dependencies: ZAD-001.
- Output: matrix scenario -> required/supplemental agents.
- Status: completed.
- Evidence: .github/orchestration/scenario-delegation-matrix.md

3. ZAD-003 Artifact mapping by scenario
- Goal: define required subagent artifacts and final orchestrator artifact per scenario.
- Dependencies: ZAD-002.
- Output: matrix scenario -> subagent artifacts -> final template.
- Status: completed.
- Evidence: .github/orchestration/scenario-delegation-matrix.md, .github/final-outputs/template-selection-rules.md

4. ZAD-004 Minimal audit summary standard
- Goal: enforce minimal runtime evidence for closure.
- Dependencies: ZAD-001.
- Output: task-level audit summary template.
- Status: completed.
- Evidence: .github/audit/task-audit-summary.template.yaml, .github/agents/orchestrator.md

### P1

5. ZAD-005 Single-agent exception policy
- Goal: define when orchestrator-only execution is allowed.
- Dependencies: ZAD-001.
- Output: formal policy and controls.
- Status: completed.
- Evidence: .github/agents/orchestrator.md

6. ZAD-006 Requirements-only scenario mapping
- Goal: remove ambiguity for requirements clarification tasks.
- Dependencies: ZAD-001, ZAD-003.
- Output: explicit mapping in template selection.
- Status: completed.
- Evidence: .github/final-outputs/template-selection-rules.md, .github/agents/orchestrator.md

7. ZAD-007 Parallel and discrepancy execution rules
- Goal: define conflict handling with continued non-conflicting work.
- Dependencies: ZAD-002.
- Output: execution rule set.
- Status: completed.
- Evidence: .github/agents/orchestrator.md

8. ZAD-008 Envelope and ID compliance checks
- Goal: define operational checks for output envelope, TA-ID UTC format, final_status consistency.
- Dependencies: ZAD-003.
- Output: checklist plus future validator scope.
- Status: completed.
- Evidence: .github/tests/orchestration_contract_validator.py, .github/tests/agent-contract-tests.md

9. ZAD-009 Historical validation pilot
- Goal: validate rules on 2-3 historical tasks.
- Dependencies: ZAD-008.
- Output: pilot validation report with pass/fail and corrections.
- Status: completed.
- Evidence: Documents/Analysis/Orchestration/pilot-validation-report-T-20260510-001.md

10. ZAD-010 3-week rollout
- Goal: transition to operational standard.
- Dependencies: ZAD-009.
- Output: week-by-week rollout plan and owner assignments.
- Status: completed.
- Evidence: Documents/Analysis/Orchestration/rollout-plan-3-weeks.md

### P2

11. ZAD-011 Knowledge reuse feedback loop
- Goal: measure recommendation reuse from knowledge-curation.
- Dependencies: ZAD-010.
- Output: periodic reuse metrics and review cycle.
- Status: backlog.

## Definition of Done (Global)
1. Contract/documentation updates merged.
2. Required template references updated.
3. Verification checklist attached.
4. Team memory and final report persistence requirements preserved.
5. No contradiction with orchestrator boundaries and confidence policy.

