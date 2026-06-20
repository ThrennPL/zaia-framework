# Evidence Pack Hardening Policy

Status: active
Owner: quality owner
Version: 1.0.0

## Purpose
Define minimal hardening requirements for evidence_pack before broad rollout.

## Scope
Applies to tasks that introduce or modify evidence_pack contracts, ingestion, migration, or rollout strategy.

## Mandatory controls
1. Record identity control:
- Every new evidence record must have `evidence_id`.
- Uniqueness must be enforced at tenant scope.
- ID conflict behavior must be defined and testable.

2. Lineage control:
- Every new evidence record must include lineage metadata.
- Lineage completeness status must be explicit (`complete` or `partial`).
- Parent linkage rules must be validated against existing record IDs.

3. Compatibility control:
- API evolution must be additive-first.
- Legacy clients must remain supported without mandatory new request fields.

4. Migration and backfill control:
- Backfill strategy must define batch size, retry policy, and checkpoint resume.
- Completion thresholds must be measurable and time-bounded.

5. Rollout and rollback control:
- Feature-flag sequence must be explicit by rollout ring.
- Rollback triggers must include objective metric thresholds.
- Rollback rehearsal evidence with measured timing is mandatory before broad rollout.

## Gate rules
Gate decision must be `fail` if any condition is true:
1. No explicit `evidence_id` uniqueness and collision rule.
2. No explicit lineage completeness definition for new records.
3. No rollback trigger thresholds.
4. No rollback rehearsal evidence.

## Required evidence package for hardening review
1. Contract and compatibility document.
2. Migration and backfill plan.
3. Test and DoD plan.
4. Rollout and rollback checklist.
5. Daily status and owner mapping for decision windows.

## Configuration baseline (repo-resident)
This policy is self-contained and MUST NOT depend on files outside versioned repository paths.

Minimum baseline that must be present in task evidence package:
1. Identity and lineage data contract:
- `evidence_id` is server-generated when missing.
- `evidence_id` is immutable and unique at tenant scope.
- lineage fields include `source_system`, `source_event_id`, `ingest_run_id`, `parent_evidence_ids`, `created_at_utc`.
- write conflict for duplicate ID is defined and testable.

2. API compatibility contract:
- add-only API evolution for evidence endpoints.
- legacy clients remain supported without new mandatory request fields.
- parent linkage validation behavior is explicitly defined.

3. Migration and backfill contract:
- add-only schema change sequence.
- backfill defines batch size, max workers, retry count, and checkpoint resume behavior.
- closure thresholds define required coverage for new and historical records.

4. Test and DoD contract:
- critical scenarios include: missing ID generation, duplicate ID conflict handling, parent linkage validation, and checkpoint resume after interruption.
- acceptance thresholds and DoD checklist are explicit.

5. Rollout and rollback contract:
- feature flags include read, write, backfill, and strict-validation controls.
- rollout uses staged rings with explicit promotion criteria.
- rollback order is defined and includes objective trigger thresholds (latency, error rate, ID-collision rate).
- rollback rehearsal evidence with measured timing is mandatory.

Recommended repository location for optional concrete templates:
- `.github/artifacts/templates/`
- `.github/quality-gates/`
- `.github/orchestration/`

## Enforcement notes
This policy extends existing quality-gate workflow and does not replace global audit, classification, or retrieval-first requirements.
