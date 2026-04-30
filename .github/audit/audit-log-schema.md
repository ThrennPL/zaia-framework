# ZAIA Audit Log Schema

Status: active
Owner: environment owner
Retention: 365 days

## 1. Purpose
Define a human-readable, task-centric audit schema for the ZAIA orchestration lifecycle.

## 2. Record Identity
Every audit record must include:
- audit_record_id
- task_id
- timestamp_utc
- event_type
- actor_type (orchestrator | subagent | system)
- actor_id
- status (started | completed | completed_with_notes | escalated | failed)

## 3. Mandatory Event Types
Required event families per TASK-ID:
1. orchestration_started
2. delegation_plan_created
3. subagent_invocation_started
4. subagent_invocation_completed
5. mcp_tool_call_started
6. mcp_tool_call_completed
7. escalation_raised
8. escalation_resolved
9. discrepancy_round_started
10. discrepancy_round_completed
11. synthesis_started
12. synthesis_completed
13. task_closed

## 4. Event Payload Fields
### 4.1 Orchestration start
- initiated_by
- user_request_excerpt
- data_classification
- context_version

### 4.2 Delegation plan
- subtask_list
- agent_mapping
- dependency_graph_summary
- rationale

### 4.3 Subagent invocation
- subagent_id
- prompt_version
- input_envelope_validation (pass | fail)
- output_envelope_validation (pass | fail)
- confidence_score
- escalation_flag
- duration_ms

### 4.4 MCP tool calls
- tool_name
- safe_parameters
- result_status
- error_summary (if failed)
- duration_ms

### 4.5 Escalations
- escalation_code
- escalation_priority (blocking | non-blocking)
- raised_by
- resolution_path (mcp_retrieval | alternate_subagent | user_clarification)
- resolution_latency_ms

### 4.6 Discrepancy rounds
- participating_agents
- conflict_scope
- positions (maintain | revise | scope)
- decision_rationale
- unresolved_flag

### 4.7 Synthesis and closure
- used_technical_artifacts
- final_report_status
- open_issues_count
- blocking_open_issues_count

## 5. Confidence Traceability
Each decision-level event must include:
- confidence_formula_version
- confidence_components
- confidence_weights
- confidence_score

## 6. Readability Constraints
- Logs must be human-readable markdown or JSON with clear key names.
- Records must be searchable by task_id.
- Each event entry must be independently understandable without external decoding.

## 7. Minimum Integrity Rules
- Missing task_id invalidates record.
- Missing event_type invalidates record.
- Missing timestamp_utc invalidates record.
- Missing status invalidates record.
- Any invalid record must be flagged and repaired before task closure.
