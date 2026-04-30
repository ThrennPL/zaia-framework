# Example: Discovery Outcome Report

## Header
- Report ID: RPT-2026-001
- Task ID: T-20260430-101
- Template Type: Discovery Outcome Report
- Version: 1.0
- Status: approved
- Owner: Lead Analyst
- Date: 2026-04-30
- Data Classification: internal

## 1. Task Context and Scope
- Request summary: Discover gaps in onboarding process documentation.
- Scope boundaries: Front-office onboarding only.
- In-scope and out-of-scope: In-scope retail onboarding, out-of-scope post-sale servicing.

## 2. Subagent Contributions
- Discovery extracted stakeholder map and open questions.
- Domain provided term normalization.
- Confidence summary: 0.76 with noted uncertainty in exception paths.

## 3. Discrepancies and Outcome
- Conflict: onboarding completion definition differs across sources.
- Outcome: maintain domain glossary definition and revise process interpretation.

## 4. Orchestrator Synthesis (FACT | INFERENCE | ASSUMPTION | UNCERTAIN)
- FACT: current documents omit exception escalation owner.
- INFERENCE: missing owner likely drives processing delays.
- ASSUMPTION: same escalation gap exists in two regional teams.
- UNCERTAIN: impact magnitude due to stale monthly KPI source.

## 5. Recommendations and Rationale
- Run focused workshop for escalation ownership.
- Update process model before requirements decomposition.

## 6. Open Issues and Required Decisions
- Blocking: confirm regional exception-owner model.
- Non-blocking: align KPI dictionary labels.

## 7. Source Trail and Identifiers
- Sources: SRC-12 (current), SRC-19 (stale).
- Linked IDs: PRD-2026-001, TMP-2026-001.

## 8. Discovery-Specific Addendum
- Stakeholder map: BA, Ops Lead, Compliance, Branch Manager.
- Information-gap backlog: 5 items.
- Hypothesis priority: H1, H3, H2.
