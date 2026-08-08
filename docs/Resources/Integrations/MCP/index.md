---
title: MCP Server
diataxis: how-to
tags: [how-to, mcp, integration, ai-agents]
---

# MCP Server

This guide shows how to connect an external AI agent to your DeepCube data using the DeepCube MCP Server.

The [DeepCube MCP Server](https://github.com/ImmersiveFusion/deepcube-mcp-server) is an open-source [Model Context Protocol](https://modelcontextprotocol.io) server that exposes your grid's traces, logs, and diagnostics to any MCP-capable agent. It lets a coding assistant such as GitHub Copilot in VS Code query your telemetry directly, in agent mode, the same telemetry Tessa works with inside DeepCube.

The server is published on GitHub under the MIT license, with pre-built binaries for Windows, Linux, and macOS.

## What you can do with it

Once connected, your agent can ask about your live telemetry in natural language and the server answers from your grid. The tools cover:

| Area | Tools |
|------|-------|
| **Grid** | Get grid information |
| **Traces** | Get traces in a time range, get a trace by span ID, get the spans in a distributed trace, get a span's tags, get a trace's errors |
| **Logs** | Get logs in a time range, get a log by span ID |
| **Diagnostics** | System health, root cause diagnosis, service dependency map, pressure points, trend analysis, alert summary, incident timeline, per-service detail, slowest endpoints, deployment changes, and time-window comparison |

All results are returned as structured data the agent reads in the conversation.

## Prerequisites

- A DeepCube subscription and a **Grid API key** (create one in your account; see [API keys](../../../Getting-Started/Api-Key/index.md)).
- [.NET 10 SDK](https://dotnet.microsoft.com/download) to build and run the server.
- An MCP-capable client. The instructions below use **VS Code with GitHub Copilot agent mode**.

## Install

Clone and build the server:

```bash
git clone https://github.com/ImmersiveFusion/deepcube-mcp-server.git
cd if-apm-mcp-server/src/IF.APM.App.MCP.Server
dotnet build
```

Pre-built binaries for each platform are also available from the repository's [GitHub Releases](https://github.com/ImmersiveFusion/deepcube-mcp-server/releases).

## Configure in VS Code

Add the server to your workspace's `.vscode/mcp.json`. This example prompts for your API key on first use and keeps it out of the file:

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "if-key",
      "description": "DeepCube API Key",
      "password": true
    }
  ],
  "servers": {
    "IF.APM.App.MCP.Server": {
      "type": "stdio",
      "command": "dotnet",
      "args": [
        "run",
        "--project",
        "${workspaceFolder}/IF.APM.App.MCP.Server/IF.APM.App.MCP.Server.csproj"
      ],
      "env": {
        "IF_ApiKey": "${input:if-key}"
      }
    }
  }
}
```

Then open Copilot Chat, switch to **Agent** mode, and the DeepCube tools become available to the agent. See the [VS Code MCP documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) for enabling MCP servers.

## Configuration reference

The server reads its configuration from environment variables prefixed with `IF_`.

| Variable | Required | Purpose |
|----------|----------|---------|
| `IF_ApiKey` | Yes | Your DeepCube Grid API key. The server exchanges it for an access token and reads the grid it belongs to. |
| `IF_BaseUrl` | No | The API endpoint. Defaults to `https://api-azure.iapm.app`. |

The transport is **stdio**: the client launches the server as a subprocess and exchanges MCP messages over standard input and output. The API key identifies which grid the agent can see, so an agent only ever reads the data that key is authorized for.

## Related

- **For sending telemetry to DeepCube:** see [Instrument your application](../../../Instrument/index.md).
- **For the direct HTTP API:** see [API Reference](../../API/index.md).
- **For managing API keys:** see [API keys](../../../Getting-Started/Api-Key/index.md).
