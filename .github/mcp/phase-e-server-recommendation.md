# Phase E Addendum: Recommended MCP Server Set (V1)

Status: active
Owner: environment owner

## 1. Recommendation Summary
Use a staged rollout with strict orchestrator-only access and read-only operations first.

Recommended order:
1. E0: Atlassian + GitHub + Filesystem (read-only).
2. E1: Memory server with retention and masking controls.
3. E2: OCR pilot under controlled policy.

Sequential-thinking server is recommended for orchestration quality, but not required to start V1.

## 2. Recommended Servers by Capability
### 2.1 Atlassian (Jira + Confluence)
Choose one profile:
- Cloud profile: atlassian/atlassian-mcp-server (Rovo MCP, OAuth-based).
- Data Center/Server profile: sooperset/mcp-atlassian (self-hosted integration model).

Policy in Phase E:
- read-only operations only.
- no create/update/delete operations.

### 2.2 GitHub
Recommended server:
- @modelcontextprotocol/server-github

Phase E scope:
- repository metadata read
- issues and pull request read

Write actions are deferred beyond Phase E.

### 2.3 Filesystem
Recommended server:
- @modelcontextprotocol/server-filesystem

Phase E scope:
- read-only file access constrained to repository workspace.
- deny access outside configured workspace roots.

### 2.4 Memory
Recommended server:
- @modelcontextprotocol/server-memory

Activation stage:
- E1, after retention and masking policy confirmation.

Use case:
- team episodic memory and semantic continuity across sessions.

### 2.5 Sequential Thinking
Recommended server:
- @modelcontextprotocol/server-sequential-thinking

Role:
- improved orchestration planning depth and synthesis quality.

Activation:
- optional in V1, recommended after E0 baseline stability.

## 3. Minimal Scope and Access Baseline
For all enabled servers in Phase E:
1. read-only permissions,
2. least-privilege scopes,
3. orchestrator-only invocation,
4. full audit logging.

## 4. Cloud vs Data Center Decision Gate
Before enabling Atlassian integration, decide deployment profile:
1. Cloud profile if organization uses Atlassian Cloud tenancy.
2. Data Center/Server profile if on-prem or self-managed deployment is in use.

Record selected profile and owner in MCP configuration notes.

## 5. Compliance and Guardrails
All server usage must satisfy:
- allowlist-based tool policy,
- data classification compatibility checks,
- sensitive-data masking requirements,
- blocking escalation on non-compliance.

## 6. Out of Scope for Phase E
- write-side actions in Jira/Confluence/GitHub
- autonomous publication of generated artifacts
- bypassing orchestrator MCP authority
