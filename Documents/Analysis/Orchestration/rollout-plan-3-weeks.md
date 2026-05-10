# ZAIA Orchestration Rollout Plan (3 Weeks)

Status: active
Owner: program owner
Start date: 2026-05-10

## Week 1 - Contract and Policy Lock
Goal: lock operational policy and required artifacts.

Activities:
1. Confirm scenario matrix as execution baseline.
2. Confirm single-agent exception policy.
3. Confirm requirements-only mapping.
4. Confirm discrepancy parallelization rule.
5. Publish audit-summary template usage guidance.

Owners:
- orchestrator governance
- quality owner
- template owner

Exit criteria:
- scenario matrix approved
- backlog statuses updated
- policy deltas merged
- no unresolved blocking comments

## Week 2 - Validation and Backfill
Goal: operationalize checks and remove known violations.

Activities:
1. Run orchestration_contract_validator.py on Documents/Analysis.
2. Backfill missing envelope markers in impacted artifacts.
3. Normalize TA-ID UTC formatting issues.
4. Re-run validator and capture clean report.

Owners:
- quality owner
- artifact owners

Exit criteria:
- validator returns zero errors on agreed scope
- pilot findings closed or formally waived with owner decision
- updated evidence report persisted

## Week 3 - Pilot and Go-Live
Goal: run live execution using new standard.

Activities:
1. Execute 2 new tasks with scenario-first delegation.
2. Persist final report and team memory for both tasks.
3. Persist task-audit-summary for both tasks.
4. Review throughput and discrepancy handling performance.

Owners:
- orchestrator governance
- subagent owners
- quality owner

Exit criteria:
- both tasks completed under new standard
- all required artifacts persisted
- no blocking contract violations
- go-live recommendation documented

## Governance and Risk Controls
- No-go if audit-summary missing for closure tasks.
- No-go if final_status and verdict are inconsistent.
- No-go if unresolved blocking discrepancy has no escalation record.

## Required Evidence Set
1. scenario-delegation-matrix.md
2. implementation-backlog.md
3. task-audit-summary.template.yaml
4. pilot-validation-report-T-20260510-001.md
5. validator output snapshot for week 2 and week 3


