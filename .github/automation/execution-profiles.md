# Phase F Hardening: Automation Execution Profiles

Status: active
Owner: environment owner

## 1. Purpose
Define execution profiles for running ZAIA automation workflows in controlled environments.

## 2. Profiles
### 2.1 profile_dev
Use for local validation and dry runs.
- artifact_generator: dry-run allowed
- quality_gate_validator: full checks
- diagnostics_report: sample window
- external writes: disabled

### 2.2 profile_stage
Use for pre-production validation.
- artifact_generator: draft output enabled
- quality_gate_validator: full checks + remediation output
- diagnostics_report: full staging data window
- external writes: disabled

### 2.3 profile_prod
Use for production analytical operations.
- artifact_generator: draft output enabled with audit event requirement
- quality_gate_validator: mandatory for gate transitions
- diagnostics_report: scheduled and on-demand
- external writes: disabled in baseline, require explicit future policy change

## 3. Shared Runtime Requirements
- orchestrator-only execution authority
- complete input envelope validation
- complete audit event emission
- placeholder verification complete or partial (not blocked)

## 4. Profile Selection Rules
1. Use profile_dev for local repository iteration.
2. Use profile_stage before first production onboarding.
3. Use profile_prod only after stage sign-off.

## 5. Failure Behavior
If any blocking validation fails:
- stop workflow execution,
- emit blocking status,
- record failure details in audit log,
- require remediation before rerun.
