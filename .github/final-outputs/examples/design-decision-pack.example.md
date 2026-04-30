# Example: Design Decision Pack

## Header
- Report ID: RPT-2026-002
- Task ID: T-20260430-102
- Template Type: Design Decision Pack
- Version: 1.0
- Status: approved
- Owner: Lead System Analyst
- Date: 2026-04-30
- Data Classification: internal

## 1. Task Context and Scope
- Design objective: Select integration pattern for onboarding checks.
- Scope boundaries: Eligibility and sanction checks.
- Assumptions and constraints: Existing API gateway remains mandatory.

## 2. Subagent Contributions
- Requirements defined acceptance criteria for latency.
- Integration mapped synchronous and event-driven options.
- NFR provided availability and observability thresholds.

## 3. Discrepancies and Outcome
- Conflict: sync flow favored by ops, async favored by architecture.
- Outcome: hybrid pattern selected with async fallback.

## 4. Orchestrator Synthesis (FACT | INFERENCE | ASSUMPTION | UNCERTAIN)
- FACT: API gateway policy requires central auth checks.
- INFERENCE: hybrid model reduces peak-time failures.
- ASSUMPTION: current event bus capacity can absorb incremental traffic.
- UNCERTAIN: failover behavior under quarter-end load.

## 5. Recommendations and Rationale
- Approve hybrid integration design.
- Add ADR for fallback and retry policy.

## 6. Open Issues and Required Decisions
- Blocking: event-bus capacity sign-off.
- Non-blocking: naming convention update for retry metrics.

## 7. Source Trail and Identifiers
- Sources: SRC-31, SRC-35, SRC-41.
- Linked IDs: SD-2026-001, ADR-042, NFR-PERF-003.

## 8. Design-Specific Addendum
- Option matrix: sync, async, hybrid.
- Impact summary: medium complexity, lower operational risk.
- ADR candidates: retry policy, timeout policy.
