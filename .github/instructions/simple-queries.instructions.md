---
applyTo: "**"
---

# ZAIA Simple Query Handling Instructions

## Goal
Handle simple user requests quickly without unnecessary delegation while preserving orchestrator governance.

## Definition of simple query
A query is simple when it is:
- low risk
- answerable directly by orchestrator
- not dependent on multi-document synthesis
- not requiring formal decision records

## Allowed direct responses
- plain clarification answers
- quick repository checks (file exists, simple path confirmation)
- short conceptual distinctions
- brief operational guidance with no policy decision impact

## Mandatory switch to full orchestration
Switch to standard orchestration mode if any of the following applies:
1. user asks for audit, architecture, compliance, or risk verdict
2. user asks for multi-step plan requiring cross-agent contributions
3. user asks for persistent output artifacts
4. confidence is below 0.80 for critical claim
5. unresolved conflict between evidence sources appears

## Response style for simple queries
- answer directly and briefly
- avoid creating artificial orchestration artifacts
- include file references when relevant
- suggest escalation to full mode only when needed

## Traceability note
- Lightweight mode interactions may be logged operationally but do not require full final report persistence.
- Any transition from lightweight mode to standard orchestration mode starts a new TASK-ID lifecycle.
