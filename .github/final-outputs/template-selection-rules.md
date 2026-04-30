# Final Output Template Selection Rules

Status: active
Owner: environment owner

## 1. Purpose
Define deterministic rules for choosing the final orchestrator output template based on task type, escalation state, and confidence profile.

## 2. Selection Inputs
Required inputs:
- task_type
- primary objective
- dominant subagent set
- escalation_status
- confidence_band
- target audience

## 3. Task-Type Mapping
Use this default mapping:
- discovery or problem-framing tasks -> Discovery Outcome Report
- architecture/design-option tasks -> Design Decision Pack
- readiness/refinement/release-prep tasks -> Delivery Readiness Pack
- regulated-risk/compliance-heavy tasks -> Risk and Compliance Decision Pack
- leadership-update tasks -> Executive Summary for Stakeholders

## 4. Escalation-Sensitive Overrides
Override default mapping when:
1. unresolved blocking escalation exists:
- use Risk and Compliance Decision Pack if blocker is regulatory/control related,
- otherwise use Delivery Readiness Pack with explicit no-go recommendation.

2. unresolved cross-agent discrepancy exists after one discussion round:
- use Executive Summary for Stakeholders with explicit decision options.

## 5. Confidence-Threshold Routing
- confidence 0.80-1.00: keep default selected template.
- confidence 0.60-0.79: keep template and require explicit uncertainty section.
- confidence 0.40-0.59: force escalation-aware template (Delivery Readiness or Risk and Compliance Decision Pack).
- confidence below 0.40: route to Executive Summary for Stakeholders with blocking escalation notice.

## 6. Audience Overrides
- technical and delivery audience: prefer Design Decision Pack or Delivery Readiness Pack.
- risk/compliance governance audience: prefer Risk and Compliance Decision Pack.
- executive audience: prefer Executive Summary for Stakeholders.

## 7. Testability Rules
A selection result is valid only if:
1. selected template matches mapping or documented override rule,
2. applied override reason is recorded,
3. confidence-band rule is recorded,
4. final output includes the mandatory baseline sections.

## 8. Mandatory Baseline Sections (All Templates)
1. Task context and scope
2. Subagent contributions
3. Discrepancies and outcome
4. Orchestrator synthesis (FACT/INFERENCE/ASSUMPTION/UNCERTAIN)
5. Recommendations and rationale
6. Open issues and required decisions
7. Source trail and identifiers
