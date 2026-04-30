# Phase F Workflow: Audit Diagnostics Report Generator

Status: active
Owner: environment owner

## 1. Objective
Automate owner-readable diagnostics reports from audit logs without requiring raw-log analysis.

## 2. Scope
In scope:
- reliability metrics
- confidence metrics
- escalation metrics
- MCP tool health metrics
- discrepancy metrics
- trend deltas by reporting period

## 3. Inputs
Required:
- reporting_window
- task_id set or task filter
- audit-log data source reference

Optional:
- baseline period for comparison
- alert threshold overrides

## 4. Generation Steps
1. Collect audit events for reporting scope.
2. Validate minimal event integrity fields.
3. Calculate metrics from diagnostic-metrics definitions.
4. Generate trend deltas versus baseline period.
5. Flag threshold violations.
6. Produce owner-readable markdown report.
7. Record report-generation event in audit log.

## 5. Mandatory Metrics
- task_completion_rate
- task_failure_rate
- escalation_rate_by_agent
- mean_confidence_by_agent
- mcp_call_success_rate_by_tool
- unresolved_discrepancy_rate

## 6. Output Contract
- report_status: success | failed
- report_window
- generated_at
- metric_table
- alerts
- interpretation_notes

## 7. Guardrails
- no personally sensitive raw content in report output,
- include only safe summaries for diagnostics,
- preserve task_id traceability for every alert.
