---
title: Tessa tools
diataxis: reference
tags: [reference, tessa, tools]
---

# Tessa tools

This page documents the built-in tools Tessa uses autonomously during conversations.

## Core tools

These tools are available in every Tessa conversation, on every DeepCube surface, regardless of Grid connection.

| Tool | What It Does |
|------|--------------|
| **Read** | Read files from your workspace |
| **Write** | Create or overwrite files (creates parent directories automatically) |
| **Edit** | Make targeted edits to existing files |
| **Glob** | Find files by pattern |
| **Grep** | Search file contents with regex |
| **LS** | List directory contents |
| **Workspace** | Manage workspaces (list, current, register, unregister, add/remove reference, create, delete, rename) |
| **Memory** | Remember and recall facts across sessions |
| **Voice** | List available voices, preview samples, and report the current voice. Selecting Tessa's voice is done in account preferences today, not through the assistant. |
| **Task** | Spawn sub-agents for parallel or complex work |
| **WebSearch** | Search the web for information |
| **WebFetch** | Fetch and analyze web pages |
| **GetCurrentTime** | Current date and time queries |

## Diagnostic tools

When Tessa is connected to a Grid, she also has access to diagnostic tools via the Cloud Brain. These cover health checks, root cause analysis, pressure detection, service maps, and more. For the full catalog, see [Tessa diagnostics](assistant-diagnostics.md).

## Notes

- Tessa selects tools autonomously based on what you ask; you don't invoke them by name.
- The **Write** and **Edit** tools only run inside Active Workspaces; Reference workspaces are read-only.
- The **Task** tool spawns sub-agents that run with restricted, read-only permissions (file reads and search only).

## Related

- **For concept and design:** see [Tessa - Your AI Assistant](../Overview/ai-assistant.md).
- **For the hat catalog:** see [Tessa hats](assistant-hats.md).
- **For the skill catalog:** see [Tessa skills](assistant-skills.md).
