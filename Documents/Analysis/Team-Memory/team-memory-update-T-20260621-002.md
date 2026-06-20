# Team Memory Update
team_memory_id: TMU-T-20260621-002
task_id: T-20260621-002
date_utc: 2026-06-21

- Generic evidence-package requirement was insufficient for evidence_pack domain hardening decisions.
- Evidence Pack Hardening v1 now mandates three gate-critical controls: evidence_id uniqueness, lineage completeness for new records, rollback rehearsal with thresholds.
- Quality gate workflow now has explicit fail overrides when these controls are missing.
- Keep OKF introduction deferred; first validate one stable hardening cycle on evidence_pack.
