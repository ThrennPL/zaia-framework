# Gate 3 - Delivery Readiness Checklist

Status options: pass | pass_with_notes | fail

## Objective
Confirm artifacts are ready for backlog refinement and delivery planning.

## Mandatory Checks
1. Backlog decomposition completed (epic/feature/story/task).
2. Dependency map exists and is actionable.
3. Acceptance criteria exist for delivery-relevant stories.
4. Traceability path to test intent is complete.
5. Blocking open issues are either resolved or explicitly accepted by owner.
6. Required approvals are captured where applicable.

## Evidence Required
- backlog decomposition output
- quality validation report
- traceability matrix excerpt
- approval notes

## Decision Rules
- pass: delivery can start with controlled risk.
- pass_with_notes: manageable non-blocking issues remain.
- fail: unresolved blockers, missing acceptance criteria, or incomplete traceability.

## Blocking Conditions
- no test intent linkage
- unresolved blocking issue without owner decision
- missing approval for critical compliance-dependent scope
