# Artifact Location Policy

Status: active
Owner: orchestrator governance
Version: 1.0.0

## Purpose
Define mandatory persistence locations for orchestrator and subagent artifacts to avoid manual post-run file moves.

## Base folders
- Final reports: `Documents/Analysis/`
- Team memory updates: `Documents/Analysis/Team-Memory/`
- Agent technical artifacts: `Documents/Analysis/Agents/{agent-id}/`

## Agent folder mapping
- orchestrator -> `Documents/Analysis/Agents/orchestrator/`
- discovery -> `Documents/Analysis/Agents/discovery/`
- requirements -> `Documents/Analysis/Agents/requirements/`
- domain -> `Documents/Analysis/Agents/domain/`
- integration -> `Documents/Analysis/Agents/integration/`
- process -> `Documents/Analysis/Agents/process/`
- backlog -> `Documents/Analysis/Agents/backlog/`
- nfr -> `Documents/Analysis/Agents/nfr/`
- risk-compliance -> `Documents/Analysis/Agents/risk-compliance/`
- quality -> `Documents/Analysis/Agents/quality/`
- knowledge-repository -> `Documents/Analysis/Agents/knowledge-repository/`

## Naming rules
- Final report filename: `{task-topic-slug}-{TASK-ID}.md`
- Team memory filename: `team-memory-update-{TASK-ID}.md`
- Agent artifact filename: `{task-topic-slug}-{artifact-scope}-{TASK-ID}.md`

## Enforcement rules
1. Final orchestrator report must be saved in `Documents/Analysis/` (root of analysis folder).
2. Team memory must be saved only in `Documents/Analysis/Team-Memory/`.
3. Every technical artifact produced by a subagent must be saved in that subagent's mapped folder.
4. Links in final report and audit summary must reference these canonical locations.
5. If canonical folders do not exist, create them before persistence.

