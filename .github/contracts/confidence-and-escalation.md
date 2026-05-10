# Confidence and Escalation Contract

Status: active
Owner: orchestrator governance
Version: 1.0.0

## Formula
confidence =
  w_source_coverage * source_coverage +
  w_data_freshness * data_freshness +
  w_context_completeness * context_completeness +
  w_internal_consistency * internal_consistency

## Constraints
- component range: 0.0-1.0
- weights sum to 1.0
- weights and score must be auditable

## Routing by confidence
- 0.80-1.00: completed path
- 0.60-0.79: completed_with_notes + uncertainty annotations
- 0.40-0.59: escalated with blockers
- <0.40: immediate blocking escalation
