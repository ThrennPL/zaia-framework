# Gate 0 - Readiness Checklist

Status options: pass | pass_with_notes | fail

## Objective
Confirm the task is ready to enter discovery and structured analysis.

## Mandatory Checks
1. Roles and owners assigned.
2. Task-ID assigned and valid format.
3. Data classification defined.
4. Initial source set identified.
5. Scope statement present (in-scope and out-of-scope).
6. Required subagents identified at high level.
7. Project onboarding readiness completed (complete or partial, not blocked).
8. Placeholder verification runbook executed with no unresolved critical placeholders.

## Evidence Required
- task header block
- ownership list
- data classification note
- source inventory snapshot
- project-onboarding-readiness checklist output
- placeholder verification result and coverage matrix report

## Decision Rules
- pass: all mandatory checks complete.
- pass_with_notes: non-blocking minor documentation gaps only.
- fail: missing owner, missing data classification, or missing scope.

## Blocking Conditions
- no accountable owner
- no data classification
- no task identity
- onboarding readiness status is blocked
- unresolved critical placeholders in required assets
