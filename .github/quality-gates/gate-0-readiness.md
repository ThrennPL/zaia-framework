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

## Evidence Required
- task header block
- ownership list
- data classification note
- source inventory snapshot

## Decision Rules
- pass: all mandatory checks complete.
- pass_with_notes: non-blocking minor documentation gaps only.
- fail: missing owner, missing data classification, or missing scope.

## Blocking Conditions
- no accountable owner
- no data classification
- no task identity
