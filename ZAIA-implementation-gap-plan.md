# ZAIA Implementation Gap Review and Action Plan

Date: 2026-04-30
Scope reviewed:
- zalozenia.md
- Zaia-uzupelnienie-luki-i-orkiestracja.md
- .github/copilot-instructions.md
- .github/agents/*.md
- .github/prompts/*.prompt.md

## 1. Executive Status
Current implementation is strong for orchestration contracts and role coverage.
- Implemented: global orchestrator policy, orchestrator agent contract, all 11 subagent definitions, key analytical prompts.
- Not fully implemented: contract-test assets, fixtures, explicit prompt/skill version history mechanism, rollback runbooks, quality-gate artifact templates, and auditable diagnostics packaging model.

## 2. Coverage Summary
### Fully Implemented
1. Single user-facing orchestrator model.
2. MCP access restricted to orchestrator.
3. Subagent no-direct-user and no-direct-MCP guardrails.
4. Input/output envelope definitions for subagents.
5. Confidence scoring model and escalation thresholds.
6. ID schema definitions (TASK-ID, TA-ID, PRD/SD/ADR/FR/NFR/BTM/QGC/TMP).
7. Mandatory final report structure.
8. Complete agent roster from section 6.2.

### Partially Implemented
1. Discrepancy discussion mechanism is defined in instructions, but lacks an operational prompt/playbook dedicated to conflict rounds.
2. Audit requirements are defined, but no concrete audit-log schema/template file is present.
3. Quality gates are represented by one validation prompt, but there are no per-gate checklists (Gate 0-4) as reusable templates.
4. Artifact policy is defined, but there are no authoring templates for required project artifacts (PRD, SD, ADR, BTM, QGC, TMP).

### Missing
1. Contract test suite definitions for agents (input validation, output schema, confidence behavior, escalation behavior, scope boundaries).
2. Test fixtures package for valid/invalid/low-confidence/out-of-scope scenarios per agent.
3. Prompt/skill semantic version manifest and change history ledger.
4. Rollback runbooks (manual MAJOR/MINOR, automated PATCH with contract-test gate).
5. Diagnostics view definition for audit metrics (without raw log analysis).

## 3. Gap List with Priority
### Critical (P1)
1. Missing contract testing specification and fixtures.
Reason: explicitly required in the supplemental document section on testing strategy.
Impact: no objective verification that agents honor required envelopes and escalation behavior.

2. Missing operational version/rollback assets.
Reason: semantic versioning and rollback behavior are required, including history and test-gated rollback.
Impact: high risk of silent regressions after prompt/instruction changes.

### High (P2)
1. Missing structured audit schema and diagnostics pack.
Reason: auditability requirements define mandatory events and owner-readable diagnostics.
Impact: reduced traceability and difficult incident analysis.

2. Missing reusable quality-gate checklists by gate stage (0-4).
Reason: governance model defines staged gates beyond one generic quality prompt.
Impact: inconsistent validation depth between tasks.

### Medium (P3)
1. Missing templates for mandatory project artifacts (PRD, SD, ADR, BTM, QGC, TMP).
Reason: ZAIA target artifact set is mandatory in the core assumptions.
Impact: teams may produce inconsistent artifact structures.

2. Missing dedicated conflict-resolution orchestration prompt.
Reason: discrepancy protocol is mandatory and important enough to justify a reusable scenario prompt.
Impact: non-uniform handling of inter-agent disagreements.

## 4. Action Plan
## Phase A - Compliance Hardening (P1)
1. Create `.github/tests/agent-contract-tests.md`.
Contains: test matrix for each agent input/output envelope, confidence thresholds, escalation paths, and scope-boundary behavior.

2. Create `.github/tests/fixtures/README.md` plus fixture files per scenario class.
Scenario classes: valid input, missing required fields, low-confidence context, out-of-scope request.

3. Create `.github/versioning/prompt-skill-versioning.md`.
Contains: semantic version policy, required metadata fields, release checklist.

4. Create `.github/versioning/CHANGELOG.md`.
Contains: version entries for orchestrator, agents, prompts, with rationale and regression-test references.

5. Create `.github/versioning/rollback-runbook.md`.
Contains: MAJOR/MINOR manual rollback process, PATCH auto-rollback flow, contract-test gate requirement.

## Phase B - Governance Operations (P2)
1. Create `.github/audit/audit-log-schema.md`.
Contains: required event fields for orchestration start, delegation, subagent calls, MCP usage, escalations, discrepancy rounds, synthesis completion.

2. Create `.github/audit/diagnostic-metrics.md`.
Contains: formulas and reporting format for confidence by agent, escalation frequency, stage durations, MCP reliability, failure patterns.

3. Create `.github/prompts/discrepancy-resolution.prompt.md`.
Contains: one-round conflict procedure, maintain/revise/scope decision logic, and unresolved escalation format.

4. Create `.github/quality-gates/gate-0-readiness.md` ... `gate-4-release-auditability.md`.
Contains: staged checklists aligned with ZAIA governance section.

## Phase C - Artifact Standardization (P3)
1. Create `.github/artifacts/templates/prd.template.md`.
2. Create `.github/artifacts/templates/solution-design.template.md`.
3. Create `.github/artifacts/templates/adr.template.md`.
4. Create `.github/artifacts/templates/btm.template.md`.
5. Create `.github/artifacts/templates/qgc.template.md`.
6. Create `.github/artifacts/templates/tmp.template.md`.

All templates should enforce ID headers and traceability sections.

## 5. Definition of Done for Gap Closure
A gap item is closed only when:
1. A concrete file asset exists in repository.
2. The file includes mandatory fields derived from ZAIA assumptions.
3. Cross-reference to orchestrator policy exists where applicable.
4. The asset is usable without additional interpretation by a project analyst.

## 6. Recommended Execution Order
1. Phase A (all items)
2. Phase B (audit schema, diagnostics, discrepancy prompt)
3. Phase B (gate checklists)
4. Phase C (artifact templates)

## 7. Risk Notes
1. Without Phase A, governance quality cannot be proven, only declared.
2. Without Phase B, auditability remains conceptual and hard to operate.
3. Without Phase C, artifact consistency may diverge across initiatives.
