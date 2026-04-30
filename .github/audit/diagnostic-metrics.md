# ZAIA Diagnostic Metrics

Status: active
Owner: environment owner
Data source: audit logs per TASK-ID

## 1. Purpose
Provide owner-readable operational diagnostics without requiring raw-log analysis.

## 2. Core Diagnostic Questions
1. Is orchestration starting and completing reliably?
2. Which subagent escalates most and why?
3. What is average confidence per subagent?
4. Which processing stages consume most time?
5. Which MCP tools fail most often?
6. Are prompt changes correlated with failures or confidence drops?

## 3. Required Metrics
### 3.1 Orchestration reliability
- task_completion_rate = completed_tasks / started_tasks
- task_failure_rate = failed_tasks / started_tasks
- task_escalation_rate = tasks_with_escalation / started_tasks

### 3.2 Subagent behavior
- escalation_rate_by_agent = escalated_invocations / total_invocations
- mean_confidence_by_agent = avg(confidence_score)
- low_confidence_share_by_agent = invocations_below_0_6 / total_invocations
- contract_failure_rate_by_agent = envelope_failures / total_invocations

### 3.3 Time and flow
- mean_task_duration_ms
- p95_task_duration_ms
- mean_invocation_duration_ms_by_agent
- mean_escalation_resolution_latency_ms

### 3.4 MCP tool health
- mcp_call_success_rate_by_tool
- mcp_call_failure_rate_by_tool
- mean_mcp_call_duration_ms_by_tool

### 3.5 Discrepancy handling
- discrepancy_frequency = tasks_with_discrepancy_round / started_tasks
- unresolved_discrepancy_rate = unresolved_rounds / total_rounds

### 3.6 Version stability
- change_frequency_by_asset
- regression_after_change_rate = failed_tasks_within_window / changed_deployments

## 4. Reporting Cadence
- Daily: reliability and failures
- Weekly: confidence trends and escalation patterns
- Monthly: version stability and systemic bottlenecks

## 5. Dashboard Output Format
For each metric expose:
- metric_name
- current_value
- previous_period_value
- delta
- interpretation_note

## 6. Alert Thresholds (Baseline)
- task_failure_rate > 0.10 -> alert
- contract_failure_rate_by_agent > 0.05 -> alert
- mcp_call_failure_rate_by_tool > 0.10 -> alert
- unresolved_discrepancy_rate > 0.15 -> alert
- low_confidence_share_by_agent > 0.30 -> review

## 7. Interpretation Rules
- One-day spikes are signals, not conclusions.
- Confirm with 7-day trend before structural prompt changes.
- Always correlate failures with recent version changes.
