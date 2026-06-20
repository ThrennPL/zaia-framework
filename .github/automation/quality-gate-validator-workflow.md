# Phase F Workflow: Quality Gate Validator

Status: active
Owner: quality owner

## 1. Objective
Provide repeatable validation execution for Gate 0-4 and onboarding readiness checks.

## 2. Scope
In scope:
- gate-0-readiness
- gate-1-discovery-quality
- gate-2-design-quality
- gate-3-delivery-readiness
- gate-4-release-auditability
- project-onboarding-readiness

## 3. Inputs
Required:
- task_id
- gate_stage
- evidence package references
- linked artifact IDs

Conditional required (for evidence-pack domain changes):
- evidence_id contract references
- lineage contract references
- rollback rehearsal evidence (feature flags and measured timings)

Optional:
- waiver notes
- prior gate results

## 4. Validation Steps
1. Resolve checklist file for requested gate_stage.
2. Load required evidence references.
3. Evaluate each mandatory criterion as pass/pass_with_notes/fail.
4. Classify findings as blocking/non-blocking.
5. Compute gate decision.
6. Emit QGC-compatible output summary.
7. Record validation event in audit log.

## 5. Decision Rules
- pass: no blocking findings and all mandatory criteria satisfied.
- pass_with_notes: no blocking findings, non-blocking findings remain.
- fail: at least one blocking finding or critical evidence missing.

Evidence-pack hardening override:
- fail if evidence-pack change has no explicit evidence_id uniqueness rule.
- fail if evidence-pack change has no lineage completeness definition for new records.
- fail if evidence-pack change has no rollback trigger thresholds and rehearsal evidence.

## 6. Output Contract
- validation_status: pass | pass_with_notes | fail
- gate_stage
- finding_list
- blocking_findings_count
- non_blocking_findings_count
- remediation_actions
- revalidation_trigger

## 7. Guardrails
- no gate can be marked pass if blocking findings exist,
- unresolved critical placeholder blocks Gate 0,
- all output decisions must reference evidence IDs,
- for evidence-pack scope, references must include policy `.github/policies/evidence-pack-hardening-policy.md`.
