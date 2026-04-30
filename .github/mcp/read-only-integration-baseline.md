# Phase E MVP: MCP Read-Only Integration Baseline

Status: active
Owner: environment owner

## 1. Objective
Enable safe retrieval-first MCP usage for analytical context enrichment without write-side effects.

## 2. Integration Scope (Read-Only)
### 2.1 Jira
Allowed capabilities:
- read issues by key
- read boards and sprint metadata
- read issue links and status history

Forbidden capabilities:
- create, update, transition, delete issues
- bulk write operations

### 2.2 Confluence
Allowed capabilities:
- read pages and page metadata
- read space metadata
- read attachments metadata

Forbidden capabilities:
- create, update, delete pages
- update labels, permissions, or spaces

### 2.3 Git metadata
Allowed capabilities:
- read commit history
- read branch metadata
- read pull request metadata (where available)

Forbidden capabilities:
- push, merge, force-update, tag creation, branch deletion via MCP

## 3. Operational Principle
All MCP calls are orchestrator-only.
Subagents never call MCP directly.

## 4. Baseline Retrieval Workflow
1. Orchestrator receives data gap signal.
2. Orchestrator validates data classification and purpose.
3. Orchestrator executes read-only MCP call.
4. Orchestrator logs call in audit schema.
5. Orchestrator injects retrieved context into subagent working_context.

## 5. Exit Conditions for Read-Only Baseline
A baseline request is considered compliant only if:
- all used tools are allowlisted,
- all operations are read-only,
- all calls are audit-logged,
- no sensitive payload is exposed without masking policy.
