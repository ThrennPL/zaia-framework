# ZAIA Framework

ZAIA (Analytical Agents Team) is an enterprise-oriented GitHub Copilot Agent Mode framework for orchestrated business and system analysis.

This repository is not an application runtime. It is a configuration and governance framework for:
- orchestrator behavior,
- specialist subagent contracts,
- analytical prompts,
- quality gates,
- audit and test policies,
- artifact templates.

## Project Goal
ZAIA helps teams run repeatable, auditable, and human-governed analytical work with AI agents.

The goal is to move from ad hoc prompt usage to a governed orchestration model where:
- roles and ownership are explicit,
- every major claim is evidence-backed,
- quality gate decisions are traceable,
- final outputs are consistent and reusable across projects.

## What This Repository Provides
- Orchestrator-first operating model with human-in-the-loop governance.
- Full specialist-agent setup (11 subagent roles).
- Confidence and escalation model with auditable rules.
- Contract definitions for subagent input and output envelopes.
- Quality gate checklists (Gate 0 to Gate 4).
- Contract-test and quality-test strategy documents.
- Mandatory project artifact templates (PRD, SD, ADR, BTM, QGC, TMP).
- Final-output templates for different orchestration outcomes.

## How ZAIA Works End-to-End
1. A user request enters through the orchestrator.
2. The orchestrator defines scope, assigns TASK-ID, and builds a delegation plan.
3. Specialist subagents are invoked with strict input envelopes.
4. Subagent outputs are validated against mandatory output contracts.
5. Confidence and discrepancy handling determines proceed vs escalate behavior.
6. Orchestrator synthesizes one user-facing report.
7. Output is validated against Gate 0-4 criteria and recorded with source trail.
8. Team memory and audit records are persisted for reuse and traceability.

Expected result:
- one final synthesized report,
- explicit findings and remediation,
- complete source trail and identifiers,
- gate-ready auditability evidence.

## Repository Structure
- .github/copilot-instructions.md
  Global orchestrator behavior and guardrails.

- .github/agents/
  Per-agent contract definitions (scope, I/O, escalation, technical artifact format).

- .github/prompts/
  Reusable analytical scenario prompts (orchestration, discovery, design, quality, etc.).

- .github/placeholders/
  Placeholder catalog for project-specific ZAIA adaptation.
  Includes verification runbook, coverage matrix, and example configuration.

- .github/tests/
  Contract-test and project-artifact quality-test specifications plus fixtures.

- .github/audit/
  Audit schema and diagnostic metrics definitions.

- .github/mcp/
  Phase E MCP read-only baseline, governance controls, and OCR pilot definition.
  Includes server-set recommendation and Cloud/DC decision guidance.

- .github/automation/
  Phase F operational workflows for artifact generation, gate validation, and diagnostics reporting.
  Includes hardening assets: execution profiles, integration test plan, and production readiness checklist.

- .github/quality-gates/
  Stage checklists from readiness to release auditability.
  Includes project onboarding readiness checklist used with Gate 0.

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

## Prerequisites
- VS Code.
- GitHub Copilot Chat with Agent Mode enabled.
- Access to this repository with .github configuration files intact.

## Quick Start
1. Open this repository in VS Code with GitHub Copilot Chat enabled.
2. Ensure Agent Mode reads .github/copilot-instructions.md.
3. Start from an orchestrator prompt in .github/prompts/.
4. Select output template using .github/final-outputs/template-selection-rules.md.
5. Validate output against the relevant gate in .github/quality-gates/.

Success check:
- A generated report includes task context, findings, recommendations, open issues, and source trail.

## How to Customize ZAIA for Your Organization
Use this sequence to adapt ZAIA to your needs.

### Placeholder strategy (progressive precision)
Use placeholders where increased precision is needed, but keep default behavior usable without immediate customization.

Operating modes:
- Zero-config mode: general analytical work with default ZAIA behavior.
- Configured mode: project-specific precision for governance, compliance, agent behavior, and function-level constraints.

Rule of thumb:
- Introduce placeholders in areas where policy, domain language, or risk tolerance varies by organization.
- Keep mandatory contracts and boundary rules stable.
- Treat critical placeholders as onboarding requirements for production analytical cycles.

Recommended placeholder insertion points:
- agent contracts: scope constraints, escalation sensitivity, domain-specific checks,
- prompts: business vocabulary, expected evidence depth, approval language,
- quality/audit assets: thresholds, policy labels, retention and traceability depth,
- final outputs: organization naming, reporting context, and owner metadata.

### 1. Set ownership and governance
Update owner fields and approval responsibilities in templates and governance documents.

Files to review first:
- .github/copilot-instructions.md
- .github/artifacts/templates/
- .github/final-outputs/templates/

Expected outcome:
- Clear accountability model per artifact and per gate decision.

### 2. Define data classification and compliance profile
Align labels, retention rules, and compliance assumptions with internal policy.

Files to review first:
- .github/placeholders/placeholder-catalog.md
- .github/placeholders/placeholder-coverage-matrix.md
- .github/quality-gates/project-onboarding-readiness.md

Expected outcome:
- No unresolved critical placeholders for classification, retention, or policy alignment.

### 3. Tune agent and prompt behavior to domain context
Adjust terminology, constraints, and analysis depth for your business domain.

Files to review first:
- .github/agents/
- .github/prompts/

Expected outcome:
- Higher relevance of findings and fewer generic outputs.

### 4. Calibrate quality and audit thresholds
Set test and audit expectations to your governance baseline.

Files to review first:
- .github/tests/
- .github/audit/
- .github/automation/quality-gate-validator-workflow.md

Expected outcome:
- Stable and repeatable pass/pass_with_notes/fail behavior.

### 5. Validate onboarding readiness before first production cycle
Run placeholder and onboarding checks before regular usage.

Files to review first:
- .github/placeholders/placeholder-verification-runbook.md
- .github/quality-gates/project-onboarding-readiness.md
- .github/prompts/project-configuration.prompt.md

Expected outcome:
- Onboarding status complete or partial, not blocked.

Single-pass configuration note:
- Use `.github/prompts/project-configuration.prompt.md` as the single configuration prompt to fill critical placeholders and optional agent/function precision placeholders in one run.

### Minimal configuration baseline (critical placeholders)
Before first production analytical cycle, resolve only the critical placeholders:
- {{PROJECT_NAME}}
- {{ENVIRONMENT_OWNER}}
- {{DATA_CLASSIFICATION_BASELINE}}
- {{COMPLIANCE_PROFILE}}
- {{MCP_ALLOWED_TOOLS}}
- {{RETENTION_DAYS}}

Expected outcome:
- A minimal, policy-safe project profile with low onboarding overhead.

## Usage Examples with Expected Results

### Example A: Governance Audit Prompt (single request)
User prompt:
"Review our current project governance setup and assess Gate 0 and Gate 1 readiness. Provide blocking and non-blocking findings with remediation."

Expected result:
- A final orchestrator report with:
  - clear readiness decision for Gate 0 and Gate 1,
  - labeled claims (FACT/INFERENCE/ASSUMPTION/UNCERTAIN),
  - blocking vs non-blocking issues,
  - remediation sequence and re-validation trigger,
  - source trail and identifiers.

### Example B: Boundary Mapping and Auditability Check
User prompt:
"Map our agent boundaries (always do / ask first / never do) to ZAIA quality gates and evaluate if these rules are script-auditable."

Expected result:
- A mapping table from boundary tiers to gate criteria,
- classification of what is already automatable vs what requires rule formalization,
- concrete recommendations for rule-to-signal conversion,
- open decisions needed from governance owner.

### Example C: Customization Sprint for a New Team
Scenario:
You are onboarding a new team in a regulated domain and need ZAIA adaptation in one cycle.

Suggested sequence:
1. Run project-configuration prompt.
2. Resolve placeholders and run onboarding readiness.
3. Calibrate tests and gate thresholds.
4. Execute a pilot analysis task and inspect gate outcome.

Expected result:
- Team-specific ZAIA configuration,
- resolved critical placeholders,
- first pilot report that passes readiness checks,
- known list of residual non-blocking gaps.

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
- Phase G (full): project-configuration prompt, placeholder catalog, verification runbook, coverage matrix, and onboarding readiness integration.
- Phase F: automation workflow definitions for artifact generation, quality-gate validation, and diagnostics reporting.

Planned next:
- Phase F implementation hardening: execute integration tests and production readiness sign-off.

## Notes
- Some local planning files may remain intentionally untracked for private workflow use.
- Keep sensitive organizational content out of synthetic test fixtures.

## License
This repository includes a license file:
- LICENSE
