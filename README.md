# ZAIA Framework

ZAIA (Analytical Agents Team) is an enterprise-oriented GitHub Copilot Agent Mode framework for orchestrated business and system analysis.

This repository is not an application runtime. It is a configuration and governance framework for:
- orchestrator behavior,
- specialist subagent contracts,
- analytical prompts,
- quality gates,
- audit and test policies,
- artifact templates.

## What This Repository Provides
- Orchestrator-first operating model with human-in-the-loop governance.
- Full specialist-agent setup (11 subagent roles).
- Confidence and escalation model with auditable rules.
- Contract definitions for subagent input and output envelopes.
- Quality gate checklists (Gate 0 to Gate 4).
- Contract-test and quality-test strategy documents.
- Mandatory project artifact templates (PRD, SD, ADR, BTM, QGC, TMP).
- Final-output templates for different orchestration outcomes.

## Repository Structure
- .github/copilot-instructions.md
  Global orchestrator behavior and guardrails.

- .github/agents/
  Per-agent contract definitions (scope, I/O, escalation, technical artifact format).

- .github/prompts/
  Reusable analytical scenario prompts (orchestration, discovery, design, quality, etc.).

- .github/placeholders/
  Placeholder catalog for project-specific ZAIA adaptation.

- .github/tests/
  Contract-test and project-artifact quality-test specifications plus fixtures.

- .github/audit/
  Audit schema and diagnostic metrics definitions.

- .github/mcp/
  Phase E MCP read-only baseline, governance controls, and OCR pilot definition.
  Includes server-set recommendation and Cloud/DC decision guidance.

- .github/quality-gates/
  Stage checklists from readiness to release auditability.

- .github/artifacts/templates/
  Mandatory project artifact templates.

- .github/final-outputs/
  Final report templates, selection rules, and worked examples.

## Core Operating Principles
- Orchestrator is the only user-facing agent.
- Orchestrator is the only MCP tool authority.
- Subagents never communicate directly with users.
- Subagents never use MCP tools directly.
- Confidence and escalation behavior is explicit and auditable.
- Technical artifacts from subagents are internal and not user-facing project artifacts.

## Quick Start
1. Open this repository in VS Code with GitHub Copilot Chat enabled.
2. Ensure Copilot Agent Mode reads .github/copilot-instructions.md.
3. Use orchestrator-first prompts from .github/prompts/.
4. Select output templates from .github/final-outputs/template-selection-rules.md.
5. Validate outcomes against quality gates in .github/quality-gates/.

## How to Configure for Your Environment
### 1. Ownership and governance
Update owner fields in templates and governance documents to match your team roles.

### 2. Data classification and compliance
Adjust classification labels and compliance notes to match your internal policies.

### 3. Versioning and rollback
Adopt or adapt .github/versioning/ for your release and rollback workflow.

### 4. Quality and audit expectations
Align .github/audit/ and .github/tests/ thresholds with your governance baseline.

### 5. Prompt and agent calibration
Tune .github/agents/ and .github/prompts/ for domain-specific terminology and constraints.

## Typical Usage Flow
1. Receive user request through orchestrator.
2. Assign TASK-ID and build delegation plan.
3. Invoke required subagents with strict envelopes.
4. Validate confidence and resolve discrepancies.
5. Produce final orchestrator synthesis.
6. Validate with appropriate gate checklist.
7. Store project artifacts using mandatory templates.

## Commit Strategy
Recommended approach:
- one coherent commit per completed phase,
- or split large phases into coherent sub-packages,
- push after each phase-level commit for safe rollback points.

## Current Maturity State
Implemented baseline:
- Phase A: compliance hardening.
- Phase B: governance operations.
- Phase C: artifact standardization.
- Phase D: final-output template system.
- Phase E (MVP): MCP read-only baseline and OCR pilot definition.
- Phase G (MVP): project-configuration prompt and placeholder catalog.

Planned next:
- Phase F: automation and operational tooling.
- Phase G (full): placeholder verification flow and coverage matrix completion.

## Notes
- Some local planning files may remain intentionally untracked for private workflow use.
- Keep sensitive organizational content out of synthetic test fixtures.

## License
This repository includes a license file:
- LICENSE
