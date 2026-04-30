# Phase E MVP: MCP Governance Controls

Status: active
Owner: environment owner

## 1. Purpose
Define enforceable MCP governance controls for safe enterprise use.

## 2. Tool Allowlist
Allowed categories:
- jira_read
- confluence_read
- git_metadata_read
- ocr_extract_read

Blocked by default:
- all write-capable integrations
- tools with unknown data-classification behavior

## 3. Data Classification Gate
Before every MCP call, orchestrator must validate:
1. task data classification level,
2. tool classification compatibility,
3. least-privilege access scope.

If validation fails: block call and escalate.

## 4. Sensitive Data Masking Policy
Mandatory masking before passing retrieved content to subagents when sensitive data is present.

Minimum masking classes:
- personal identifiers
- account and token-like strings
- direct contact details
- legal identifiers where required by policy

## 5. Mandatory MCP Audit Fields
Each MCP call must emit:
- task_id
- timestamp_utc
- tool_name
- operation_name
- parameters_safe_summary
- data_classification
- masking_applied (yes/no)
- call_status (success/fail)
- error_summary (if fail)
- duration_ms

## 6. Guardrail Validation Rules
A call is non-compliant if any condition holds:
- tool not in allowlist,
- operation not read-only in Phase E,
- missing audit fields,
- missing classification validation,
- missing required masking.

## 7. Escalation Rules
On non-compliance:
1. stop call execution,
2. raise blocking escalation to orchestrator control path,
3. record incident in audit log.
