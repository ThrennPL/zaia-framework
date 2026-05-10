# Subagent Input Envelope Contract

Status: active
Owner: orchestrator governance
Version: 1.0.0

## Required fields
- task_id
- objective
- working_context
- permissions_scope
- data_classification
- required_confidence_threshold

## Validation rules
1. Missing any required field -> reject invocation.
2. Subagent must escalate with explicit missing-field list.
3. Orchestrator must log envelope validation result.
