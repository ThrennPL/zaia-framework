# Phase F Hardening: Automation Integration Test Plan

Status: active
Owner: quality owner

## 1. Purpose
Validate end-to-end interoperability between generator, gate validator, diagnostics, and governance constraints.

## 2. Test Scope
In scope:
- artifact-generator-workflow
- quality-gate-validator-workflow
- audit-diagnostics-report-workflow
- placeholder-verification and onboarding readiness dependencies

## 3. Preconditions
- contract tests pass
- project artifact quality tests pass
- placeholder verification status is complete or partial

## 4. Integration Test Cases
| Test ID | Scenario | Expected Result |
|---|---|---|
| IT-001 | Generate PRD draft then run Gate 0 validation | generation success and gate decision emitted |
| IT-002 | Generate SD draft with unresolved critical placeholder | generation blocked with clear reason |
| IT-003 | Run Gate 2 validation with missing evidence | fail decision with blocking finding |
| IT-004 | Run diagnostics report for last 7 days | report generated with required metrics |
| IT-005 | Trigger non-compliant MCP metadata in workflow input | execution blocked and audit incident logged |
| IT-006 | Full chain: generate -> validate -> diagnostics | all outputs traceable by task_id |

## 5. Success Criteria
- all integration tests pass,
- every workflow emits required output contract,
- all failures are actionable and traceable.

## 6. Exit Criteria for Hardening
Hardening phase is complete when:
- IT-001..IT-006 pass in stage profile,
- no unresolved blocking defects remain,
- owner sign-off is recorded.
