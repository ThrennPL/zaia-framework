# Gate 4 - Release and Auditability Checklist

Status options: pass | pass_with_notes | fail

## Objective
Confirm the analytical trail is auditable and release-facing communication is evidence-backed.

## Mandatory Checks
1. Audit log records exist for full task lifecycle.
2. MCP usage records are present and readable.
3. Escalation events and resolutions are documented.
4. Discrepancy decisions are documented if conflicts occurred.
5. Final synthesized report contains all mandatory sections.
6. Source trail and identifiers are complete.

## Evidence Required
- audit records by task_id
- final orchestrator report
- discrepancy records if applicable
- source and ID index

## Decision Rules
- pass: full auditability confirmed.
- pass_with_notes: minor readability issues with no evidence loss.
- fail: missing lifecycle events, incomplete source trail, or missing final report sections.

## Blocking Conditions
- incomplete audit chain
- missing source identifiers for major conclusions
- unresolved discrepancy with no escalation record
