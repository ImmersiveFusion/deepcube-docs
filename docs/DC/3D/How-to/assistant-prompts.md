---
title: Write better prompts for Tessa
diataxis: how-to
tags: [how-to, tessa, prompts]
---

# Write better prompts for Tessa

This guide shows how to phrase questions so Tessa gives you the most useful answers, with 30+ example prompts organized by category.

> Get the most out of Tessa with the right questions. This guide covers 30+ example prompts organized by category, plus tips for effective prompting.

## Health and Status

Start here when you open IAPM and want a quick picture of your system.

| Prompt | What Tessa Does |
|--------|-----------------|
| "How is my system doing?" | Runs a full health check across all services |
| "Is anything unhealthy right now?" | Highlights services with active issues |
| "Are there any active alerts?" | Pulls current and recent alert activity |
| "Give me a status report" | Summarizes health, alerts, and any notable trends |
| "Is there pressure building anywhere?" | Detects services approaching failure thresholds |

## Troubleshooting

When something is wrong and you need to find out why.

| Prompt | What Tessa Does |
|--------|-----------------|
| "Why is checkout slow?" | Returns root cause analysis of the errors and ranks the slowest endpoints by P99 latency |
| "What's causing 500 errors on payment-service?" | Analyzes error traces and correlates with recent deployments |
| "Root cause the latency spike at 2pm" | Returns a chronological timeline of when each service first errored, spiked in latency, or degraded |
| "Why did order-service start failing?" | Returns root cause analysis with recent deployments and the service's dependencies, error rate, latency, and top errors |
| "What's wrong here?" *(standing near a node in 3D)* | Diagnoses the service you're looking at |
| "Is this related to the database?" | Checks the service's dependencies for database involvement |
| "What changed right before errors started?" | Returns recent deployment changes: new service versions, new services, new endpoints, and new hosts |

## Performance Analysis

Understand trends, patterns, and how your system is performing over time.

| Prompt | What Tessa Does |
|--------|-----------------|
| "Show me the latency trend for auth-service" | Returns a latency trend classification (improving, stable, or degrading) with percent-change against a baseline |
| "How has error rate changed over the last 6 hours?" | Analyzes error rate trends with context |
| "What are the slowest endpoints?" | Ranks endpoints by response time |
| "Show me the top 10 slowest endpoints in the last hour" | Filters and ranks with a time window |
| "Is response time getting worse on /api/users?" | Evaluates the trend direction and significance |
| "What's the throughput trend for the database?" | Analyzes database call volume over time |

## Comparison

Compare time windows to understand what changed.

| Prompt | What Tessa Does |
|--------|-----------------|
| "Compare the last hour to yesterday at this time" | Side-by-side comparison of key metrics |
| "How does today compare to last Monday?" | Cross-day comparison for recurring patterns |
| "Is performance better or worse than last week?" | Trend comparison with directional summary |
| "Compare pre-deployment to post-deployment" | Finds recent deployments and compares before/after |

## Exploration and Discovery

Learn about your system architecture and data flows.

| Prompt | What Tessa Does |
|--------|-----------------|
| "Show me the service dependency map" | Returns a structured breakdown of your services, their inter-service dependencies, and each one's health, latency, and error rates |
| "What services depend on order-service?" | Maps upstream dependencies |
| "Map out the request path from gateway to database" | Returns the service dependency map showing the services between gateway and database |
| "What are the downstream dependencies of auth-service?" | Maps what auth-service calls |
| "Build me a timeline of events in the last hour" | Assembles a chronological event view |
| "What deployments happened today?" | Lists recent deployment activity |

## Contextual Questions (3D)

These work best in IAPM, where Tessa uses your position and view as context.

| Prompt | What Tessa Does |
|--------|-----------------|
| "What's wrong here?" | Diagnoses whatever you're looking at |
| "Tell me about this service" | Describes the service node nearest to you |
| "Why is this trace so slow?" *(in Diagnostics cube)* | Analyzes the trace you're currently viewing |
| "What connects to this?" | Maps dependencies for the service in front of you |

## Tips for Effective Prompting

### Be specific about time

Tessa defaults to recent data, but specifying a time window gets you more targeted results.

- :material-check: "What happened between 2pm and 3pm?"
- :material-check: "Show me the last 6 hours of latency on payment-service"
- :material-close: "What happened?" *(too vague - Tessa will ask for clarification)*

### Name your services

Use the actual service names from your Grid. Tessa matches against your service catalog.

- :material-check: "Why is order-service slow?"
- :material-close: "Why is the ordering thing slow?"

### Ask follow-ups naturally

Tessa remembers the conversation. You don't need to repeat context.

- First: "Why is checkout slow?"
- Follow-up: "Is it related to the database?"
- Follow-up: "When did this start?"
- Follow-up: "Compare to yesterday"

### Combine question types

Some of the most powerful queries combine multiple angles.

- "Why is checkout slow, and did anything change recently that could explain it?"
- "Show me the service map and highlight anything unhealthy"
- "Compare this hour to yesterday and tell me what's different"

## Commands Quick Reference

These are typed commands, not natural language prompts. They are handled locally, not sent to the AI.

| Command | Effect |
|---------|--------|
| `/mute` | Mute voice output |
| `/unmute` | Enable voice output |
| `/voice` | Toggle voice on/off |
| `/hat <name>` | Wear a hat (coder, architect, researcher, reviewer, security) |
| `/hat list` | List available hats |
| `/hat off` | Remove current hat |
| `/image <path>` | Analyze an image file |
| `/paste` | Analyze image from clipboard |
| `/clear` | Clear conversation history |
| `/sessions` | List previous sessions |
| `/session new` | Start a new session |
| `/session restore <N>` | Restore a previous session |

## What Tessa Cannot Do

Being transparent about limits helps set the right expectations:

- **She cannot modify your infrastructure** - Tessa can read, write, and edit files in your workspace (Code Fix), but she does not deploy, restart services, or make infrastructure changes.
- **She cannot access data outside your Grid** - Tessa only sees telemetry data that flows into your connected Grid.
- **She cannot predict the future** - Tessa identifies trends and pressure, but she reports on what is happening and what has happened, not what will happen.

Every Tessa capability, including code fixes and infrastructure analysis, is available on every plan. Your plan changes how much you can use Tessa and how deeply she reasons on hard problems, not which capabilities you can reach. Note that lower plans have tight per-window usage limits, so a long multi-step task may use up a window before it finishes; see [query limits](../Reference/assistant-commands.md#query-limits-by-plan).
