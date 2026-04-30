# ZAIA Environment Changelog

All notable changes to ZAIA orchestration assets are documented in this file.

## 1.5.0 - 2026-04-30
### Metadata
- author: environment owner
- rationale: define Phase F hardening controls for execution, integration tests, and production readiness
- regression-test-reference: .github/tests/agent-contract-tests.md and .github/tests/project-artifact-quality-tests.md

### Added
- .github/automation/execution-profiles.md
- .github/automation/integration-test-plan.md
- .github/automation/production-readiness-checklist.md

### Updated
- README.md with Phase F hardening visibility.

## 1.4.0 - 2026-04-30
### Metadata
- author: environment owner
- rationale: establish Phase F operational automation workflow baseline
- regression-test-reference: .github/tests/agent-contract-tests.md and .github/tests/project-artifact-quality-tests.md

### Added
- Phase F automation workflow assets:
  - .github/automation/artifact-generator-workflow.md
  - .github/automation/quality-gate-validator-workflow.md
  - .github/automation/audit-diagnostics-report-workflow.md

### Updated
- README.md repository structure and maturity state with Phase F baseline.

## 1.3.0 - 2026-04-30
### Metadata
- author: environment owner
- rationale: deliver Phase E MVP retrieval controls and Phase G MVP adaptation assets
- regression-test-reference: .github/tests/agent-contract-tests.md and .github/tests/project-artifact-quality-tests.md

### Added
- Phase E MVP MCP assets:
  - .github/mcp/read-only-integration-baseline.md
  - .github/mcp/governance-controls.md
  - .github/mcp/ocr-pilot.md

- Phase G MVP adaptation assets:
  - .github/prompts/project-configuration.prompt.md
  - .github/placeholders/placeholder-catalog.md

### Updated
- README.md with MCP and maturity-state updates.

## 1.2.0 - 2026-04-30
### Metadata
- author: environment owner
- rationale: complete baseline governance and artifact standardization
- regression-test-reference: .github/tests/agent-contract-tests.md (target scope validation)

### Added
- Phase C mandatory artifact templates:
  - .github/artifacts/templates/prd.template.md
  - .github/artifacts/templates/solution-design.template.md
  - .github/artifacts/templates/adr.template.md
  - .github/artifacts/templates/btm.template.md
  - .github/artifacts/templates/qgc.template.md
  - .github/artifacts/templates/tmp.template.md

### Updated
- ZAIA-implementation-gap-plan.md marked Phase C as completed.

## 1.1.0 - 2026-04-30
### Metadata
- author: environment owner
- rationale: operationalize governance controls and owner diagnostics
- regression-test-reference: .github/tests/agent-contract-tests.md (contract guardrails retained)

### Added
- Phase B governance assets:
  - .github/audit/audit-log-schema.md
  - .github/audit/diagnostic-metrics.md
  - .github/prompts/discrepancy-resolution.prompt.md
  - .github/quality-gates/gate-0-readiness.md
  - .github/quality-gates/gate-1-discovery-quality.md
  - .github/quality-gates/gate-2-design-quality.md
  - .github/quality-gates/gate-3-delivery-readiness.md
  - .github/quality-gates/gate-4-release-auditability.md

### Updated
- ZAIA-implementation-gap-plan.md marked Phase B as completed.

## 1.0.0 - 2026-04-30
### Metadata
- author: environment owner
- rationale: establish initial ZAIA orchestrator and subagent baseline
- regression-test-reference: pending at initial bootstrap

### Added
- Global orchestrator behavior policy.
- Orchestrator agent contract.
- 10 specialist subagent contracts.
- 10 key analytical scenario prompts.
- Initial implementation gap review plan.

### Quality and Governance Notes
- Baseline contracts align with ZAIA operating model.
- Phase A compliance-hardening assets introduced:
  - contract test specification
  - synthetic fixture set
  - versioning policy
  - rollback runbook

### Known Follow-up
- superseded by versions 1.1.0 and 1.2.0.
