# Prompt: Integration Mapping

## Intent
Run an integration-focused analytical cycle to map systems, interfaces, data flows, and dependency risks for solution design and delivery readiness.

## When to Use
Use this prompt when cross-system interactions, interface contracts, event flows, or integration uncertainty are significant.

## Execution Instructions
1. Assign TASK-ID in format `T-{YYYYMMDD}-{NNN}`.
2. Define integration scope and system boundaries.
3. Invoke Integration subagent with full input envelope.
4. Validate output envelope contract.
5. Apply confidence and escalation policy.
6. Return synthesized integration handover package for downstream validation.

## Shared Contract References
Use shared contracts for reusable policy blocks:
- Input envelope: `.github/contracts/subagent-input-envelope.md`
- Output envelope: `.github/contracts/subagent-output-envelope.md`
- Confidence and escalation: `.github/contracts/confidence-and-escalation.md`

## Required Integration Content
Ensure the resulting artifact contains:
- source and target system mapping
- interface and contract mapping
- data and event flow sequencing
- dependency graph and ownership boundaries
- integration risk and operational constraint notes
- at least one visual in Mermaid or PlantUML (for example Flowchart or Sequence Diagram) for key ambiguous or repair-required flows, chosen by diagram type
- positive foundations that can be reused in target architecture
- remediation proposals with implementation sequencing

## Confidence and Escalation Rules
Use shared contract:
- `.github/contracts/confidence-and-escalation.md`

## Output Handover Contract
Produce a synthesized handover package for:
- NFR subagent
- Risk and Compliance subagent
- Quality subagent

Include explicit notes on:
- unresolved interface ambiguity
- uncertain dependency assumptions
- missing evidence affecting design confidence
- design options that reduce ambiguity and improve delivery readiness

## Constraints
- No direct subagent-user communication.
- No direct subagent MCP usage.
- Do not present inferred contracts as FACT.
- Do not omit uncertainty in critical integration paths.
- Do not return gap-only analysis without proposed integration remediation design.
