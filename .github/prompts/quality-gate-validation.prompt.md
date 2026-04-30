# Prompt: Quality Gate Validation

## Intent
Run a quality-focused analytical cycle to validate artifact readiness against ZAIA quality gates and determine pass/pass_with_notes/fail outcome.

## When to Use
Use this prompt before publication to project repository, before stakeholder review, or before delivery handover.

## Execution Instructions
1. Assign TASK-ID in format `T-{YYYYMMDD}-{NNN}`.
2. Define target quality gate stage and artifact set.
3. Invoke Quality subagent with full input envelope.
4. Validate output envelope contract.
5. Apply confidence and escalation policy.
6. Return synthesized quality decision package with remediation path.

## Mandatory Input Envelope for Quality Subagent
- `task_id`
- `objective`
- `working_context`
- `permissions_scope`
- `data_classification`
- `required_confidence_threshold`

## Mandatory Output Envelope Validation
Require all fields:
- `status`: completed | completed_with_notes | escalated | failed
- `technical_artifact`
- `retrieval_first_performed`: true | false
- `context_version`
- `confidence_score` and `confidence_rationale`
- claim labels: FACT | INFERENCE | ASSUMPTION | UNCERTAIN
- `positive_foundations`
- `remediation_proposals`
- `role_specific_value`
- `open_issues` with blocking/non-blocking
- `episodic_memory_entry`
- `source_links` with freshness

## Required Quality Validation Scope
Ensure the resulting artifact evaluates:
- metadata completeness and ID conformity
- internal consistency
- cross-artifact consistency
- ambiguity and duplicate findings
- logical gap detection
- traceability completeness
- positive foundations supporting readiness
- remediation proposals with sequence and re-validation trigger

## Required Quality Outcome
Require one explicit status:
- pass
- pass_with_notes
- fail

Include:
- rationale
- blocking vs non-blocking findings
- release-readiness implication

## Confidence and Escalation Rules
- 0.80-1.00: proceed normally
- 0.60-0.79: proceed with uncertainty annotations
- 0.40-0.59: escalate with partial validation and blockers
- below 0.40: blocking escalation, stop publication

## Publication Blocking Rule
If any blocking finding exists, do not classify as pass.
If fail, include mandatory remediation sequence and re-validation trigger.

## Output Handover Contract
Produce a synthesized handover package for:
- Orchestrator synthesis
- remediation owners
- re-validation checkpoint planning

Include explicit notes on:
- blockers requiring human decision
- dependencies for remediation
- minimum evidence needed for successful re-check

## Constraints
- No direct subagent-user communication.
- No direct subagent MCP usage.
- Do not output pass without evidence-linked findings.
- Do not downplay blocking issues.
