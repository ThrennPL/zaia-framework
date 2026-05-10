# Prompt: Discovery Analysis

## Intent
Run a discovery-focused analytical cycle to structure early-stage understanding before design and backlog decomposition.

## When to Use
Use this prompt when the request includes unclear scope, fragmented source materials, unknown stakeholders, or missing context.

## Execution Instructions
1. Assign TASK-ID in format `T-{YYYYMMDD}-{NNN}`.
2. Define discovery objective and scope boundaries.
3. Invoke Discovery subagent with full input envelope.
4. Validate output envelope contract.
5. Check confidence and apply escalation behavior if needed.
6. Return a synthesized discovery package for downstream agents.

## Shared Contract References
Use shared contracts for reusable policy blocks:
- Input envelope: `.github/contracts/subagent-input-envelope.md`
- Output envelope: `.github/contracts/subagent-output-envelope.md`
- Confidence and escalation: `.github/contracts/confidence-and-escalation.md`

## Required Discovery Content
Ensure the resulting artifact contains:
- stakeholder map
- problem framing and business drivers
- constraints and assumptions
- open questions
- information gaps
- hypotheses and validation priorities
- positive foundations reusable for next-stage design
- remediation proposals for top-priority discovery gaps

## Confidence and Escalation Rules
Use shared contract:
- `.github/contracts/confidence-and-escalation.md`

## Output Handover Contract
Produce a synthesized handover package for:
- Requirements subagent
- Process subagent
- Domain subagent

Include explicit notes on:
- unresolved blockers
- uncertainty hotspots
- missing evidence requiring retrieval

## Constraints
- No direct subagent-user communication.
- No direct subagent MCP usage.
- Do not present assumptions as facts.
- Do not skip claim labeling.
