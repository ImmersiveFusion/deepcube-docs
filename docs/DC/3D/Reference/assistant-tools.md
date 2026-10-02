---
title: Tessa tools
diataxis: reference
tags: [reference, tessa, tools]
---

# Tessa tools

This page documents the built-in tools Tessa uses autonomously during conversations.

## Core tools

These are the tools Tessa has in the DeepCube 3D client. They are available in
every conversation there, with or without a Grid connection. Other surfaces
register their own set, so a tool here is not a promise about Studio or Web.

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
| **Feedback** | Send feedback about a tool, a response, or Tessa herself. Categorised as bug, suggestion, quality, performance, UX or praise. |
| **WebPost** | Send an HTTP POST to a URL and return the status, notable headers and the body. For driving an API, not for reading a page. |
| **GetPreferences** | Read your preferences, and which of them she is allowed to change. |
| **SetPreference** | Change a preference, for the subset marked as hers to change. |

## Shoebox tools

A shoebox is a Mermaid diagram of services calling each other, and a run of it. Ask
for one in words and Tessa builds it; you never choose a language or a stack.

| Tool | What It Does |
|------|--------------|
| **MakeShoebox** | Build a shoebox from a described topology - services, APIs, a call chain - as a diagram and a run. |
| **RunShoebox** | Fire the diagram already loaded in the conversation, optionally several times with a delay between them. Up to five runs. |
| **ShareShoebox** | Return a URL that opens the loaded diagram in the Shoebox editor. It does not run anything. |

!!! note "Running several times on purpose"
    **RunShoebox** taking a repeat count is what lets you watch an intermittent
    failure happen exactly once - a replica that breaks on the third call, for
    instance, rather than one that breaks every time.

## Diagnostic tools

When Tessa is connected to a Grid, she also has access to diagnostic tools via the Cloud Brain. These cover health checks, root cause analysis, pressure detection, service maps, and more. For the full catalog, see [Tessa diagnostics](assistant-diagnostics.md).

## Notes

- Tessa selects tools autonomously based on what you ask; you don't invoke them by name.
- The **Write** and **Edit** tools only run inside Active Workspaces; Reference workspaces are read-only.
- The **Task** tool spawns sub-agents that run with restricted, read-only permissions (file reads and search only).
- **WebPost** can only reach hosts on an allowlist the client configures. It is the
  one tool here that writes to somewhere other than your own machine.
- **SetPreference** covers only the preferences marked as hers. Redaction, sign-in
  and the frame budget are deliberately outside it. See [Preferences](../Guides/Preferences/index.md).

## Related

- **For concept and design:** see [Tessa - Your AI Assistant](../Overview/ai-assistant.md).
- **For the hat catalog:** see [Tessa hats](assistant-hats.md).
- **For the skill catalog:** see [Tessa skills](assistant-skills.md).
