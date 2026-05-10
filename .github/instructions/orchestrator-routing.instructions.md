---
applyTo: "**"
---

# ZAIA Orchestrator Routing Instructions

## Intent
Define one-entry routing for all user requests.

## Core rule
- Orchestrator is always invoked as the first and only user-facing entrypoint.
- Orchestrator decides execution mode and whether subagents are needed.

## Execution modes

1. Lightweight mode (no subagent delegation)
- Use when request is simple, low-risk, and does not require cross-artifact synthesis.
- Examples:
  - short factual clarification
  - status check
  - quick explanation without repository-wide analysis
  - simple formatting or path confirmation
- Behavior:
  - no subagent invocation
  - no discrepancy round
  - no full orchestration report
  - concise user response

2. Standard orchestration mode
- Use when request requires analysis, evidence, trade-offs, or repository updates.
- Behavior:
  - assign TASK-ID
  - build delegation plan
  - run required subagents
  - validate output envelopes
  - synthesize one final response
  - persist final report and Team Memory update

3. Escalation-heavy mode
- Use when blockers, unresolved conflicts, or low confidence appear.
- Behavior:
  - perform one discrepancy round
  - continue non-conflicting work in parallel
  - escalate to user with structured options when unresolved

## Routing decision checklist
A request is lightweight only if all conditions are true:
1. no policy/compliance/governance impact
2. no cross-agent synthesis required
3. no ambiguous requirements needing structured decomposition
4. no artifact persistence required

If any condition is false, use standard orchestration mode.

## Safety rule
- Never bypass orchestrator entrypoint.
- Never allow direct subagent-user interaction.
- Never allow direct subagent MCP usage.
