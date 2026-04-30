# Phase F Hardening: Automation Production Readiness Checklist

Status options: ready | conditionally_ready | not_ready
Owner: environment owner

## 1. Objective
Determine whether ZAIA automation workflows are safe for production analytical usage.

## 2. Mandatory Checks
1. Execution profile selected and documented.
2. Integration tests IT-001..IT-006 completed.
3. Required audit fields emitted by all workflows.
4. Blocking failure behavior verified.
5. Placeholder and onboarding dependencies satisfied.
6. No unresolved blocking defects.

## 3. Evidence Required
- execution profile record
- integration test report
- sample workflow outputs
- audit log excerpts
- owner sign-off

## 4. Decision Rules
- ready: all mandatory checks pass.
- conditionally_ready: no blocking defects but non-blocking actions remain.
- not_ready: one or more blocking conditions present.

## 5. Blocking Conditions
- missing integration test completion,
- unresolved blocking defect,
- missing audit traceability,
- missing owner sign-off.
