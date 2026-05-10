# Configuration Reorganization Proposal

Status: completed
Date: 2026-05-10
Owner: orchestrator governance
Task ID: T-20260510-005

## 1. Why now
Current .github structure is functionally rich but contains repeated policy blocks across multiple files.
Largest files indicate concentration risk and maintenance overhead:
- .github/agents/orchestrator.md
- .github/copilot-instructions.md
- .github/agents/*.md family

## 2. What is worth defining next (missing standards)
1. Agent SLA and timeout policy
- Per-agent expected response latency and retry budget.
- Distinguish synchronous vs deferred completion.

2. Retry and fallback strategy
- When to retry same agent vs switch to alternate agent.
- Maximum retry count before user escalation.

3. Human approval matrix
- Explicit decision classes requiring HITL sign-off.
- Approval owners and evidence required.

4. Data sensitivity routing matrix
- Mapping data_classification -> allowed tools, required model profile, persistence constraints.

5. Prompt and model change governance
- Change windows for model-profile overrides.
- Mandatory rollback trigger conditions.

6. Artifact lifecycle policy
- Active/archive/deprecated states.
- Retention and migration for operational artifacts.

## 3. Recommended structural refactor (non-breaking first)
Create shared contract modules and reduce duplication by reference.

### 3.1 New folders
- .github/contracts/
- .github/policies/

### 3.2 New shared files
- .github/contracts/subagent-input-envelope.md
- .github/contracts/subagent-output-envelope.md
- .github/contracts/confidence-and-escalation.md
- .github/contracts/discrepancy-protocol.md
- .github/policies/model-routing-policy.md
- .github/policies/single-agent-exception-policy.md

### 3.3 Keep in place, but slim down
- .github/copilot-instructions.md -> high-level governance only + links to contracts/policies.
- .github/agents/orchestrator.md -> orchestrator role/runbook only + links.
- .github/agents/*.md -> role-specific logic only; remove repeated generic envelope/confidence text.

## 4. What to move out of .github
Keep in .github only configuration, standards, templates, tests, and automation.

Operational artifacts should remain in Documents/Analysis paths:
- rollout plans
- implementation backlogs
- pilot reports
- historical audit analyses

## 5. Migration plan
### Phase 1 (safe, additive)
- [x] 1. Add contracts/policies shared files.
- [x] 2. Add cross-links from existing files.
- [x] 3. Keep old content intact to avoid regressions.

### Phase 2 (dedup)
- [x] 1. Remove repeated sections from agent docs and prompts.
- [x] 2. Leave short references to shared contracts.
- [x] 3. Run contract checks after each batch.

### Phase 3 (stabilization)
- [x] 1. Update tests to validate references and version tags.
- [x] 2. Update changelog and rollback runbook.
- [x] 3. Approve as new baseline.

## 9. Execution log
- 2026-05-10: Completed Phase 1 step 1 by creating shared files:
	- .github/contracts/subagent-input-envelope.md
	- .github/contracts/subagent-output-envelope.md
	- .github/contracts/confidence-and-escalation.md
	- .github/contracts/discrepancy-protocol.md
	- .github/policies/model-routing-policy.md
	- .github/policies/single-agent-exception-policy.md
- 2026-05-10: Completed Phase 1 step 2 by adding cross-links in:
	- .github/copilot-instructions.md
	- .github/agents/orchestrator.md
	- .github/instructions/README.md
- 2026-05-10: Completed Phase 1 step 3; no legacy policy blocks removed in Phase 1.
- 2026-05-10: Completed Phase 2 step 1 and 2 by deduplicating repeated sections and leaving shared-contract references in:
	- .github/agents/backlog.md
	- .github/agents/discovery.md
	- .github/agents/domain.md
	- .github/agents/integration.md
	- .github/agents/knowledge-repository.md
	- .github/agents/nfr.md
	- .github/agents/process.md
	- .github/agents/quality.md
	- .github/agents/requirements.md
	- .github/agents/risk-compliance.md
	- .github/prompts/orchestrate-full-analysis.prompt.md
	- .github/prompts/discovery-analysis.prompt.md
	- .github/prompts/integration-mapping.prompt.md
- 2026-05-10: Completed Phase 2 step 3 by running checks:
	- Contract validator: `D:/Programs/Python313/python.exe .github/tests/orchestration_contract_validator.py --path Documents/Analysis`.
	- Result: 7 known historical errors in legacy analysis artifacts under Documents/Analysis (no new config-level regressions from current dedup batch).
	- Sanity scan: no remaining literal `` `r`n `` markers in `.github/agents/*.md`.
- 2026-05-10: Completed Phase 3 step 1 by extending `.github/tests/agent-contract-tests.md` with CT-011 (shared-reference integrity) and CT-012 (version tags in shared modules).
- 2026-05-10: Completed Phase 3 step 2 by updating:
	- .github/versioning/CHANGELOG.md (v1.6.0)
	- .github/versioning/rollback-runbook.md (shared-module rollback scope and verification checks)
- 2026-05-10: Completed Phase 3 step 3; approved as new baseline and set document status to completed.

## 6. Priority and effort
- P0: shared contracts extraction (medium)
- P1: agent/prompt deduplication (medium-high)
- P1: governance matrices (medium)
- P2: historical harmonization (low-medium)

## 7. Success criteria
1. No duplicated generic envelope blocks across agent files.
2. Single source of truth for confidence/escalation policy.
3. Clear split: configuration in .github, operations in Documents/Analysis.
4. Reduced size and complexity of top 2 largest policy files.

## 8. Initial file impact map
Likely update targets:
- .github/copilot-instructions.md
- .github/agents/orchestrator.md
- .github/agents/discovery.md
- .github/agents/requirements.md
- .github/agents/domain.md
- .github/agents/integration.md
- .github/agents/process.md
- .github/agents/backlog.md
- .github/agents/nfr.md
- .github/agents/risk-compliance.md
- .github/agents/quality.md
- .github/agents/knowledge-repository.md
- .github/prompts/*.prompt.md (selected files)


