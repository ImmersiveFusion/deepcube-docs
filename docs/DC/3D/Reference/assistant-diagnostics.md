---
title: Tessa diagnostics
diataxis: reference
tags: [reference, tessa, diagnostics]
---

# Tessa diagnostics

This page documents the diagnostic capabilities Tessa offers when connected to a Grid.

> Tessa doesn't just answer questions - she runs real diagnostics against your live telemetry. Every response is backed by actual data from your Grid.

## How Diagnostics Work

When you ask Tessa a question, she selects the right diagnostic tool, queries your Grid data, and synthesizes the results into a clear answer. She can chain multiple tools together for complex investigations - for example, checking system health, then drilling into the unhealthy service, then comparing it to yesterday's performance.

Tessa queries **traces, logs, and metrics** through dedicated tools, often chaining several in a single response. You don't need to specify which data source to check - she selects the right tools based on your question.

## Diagnostic Capabilities

### System Health Check

Get an instant overview of your system's current state. Tessa reports overall system health including per-service states, error rates, the Apdex score, and the top errors across your Grid.

!!! example "Try asking"
    - "How is my system doing?"
    - "Give me a health check"
    - "Is everything healthy?"
    - "What's the overall status right now?"

---

### Alert Summary

See the current alert status derived from your system health thresholds. Tessa pulls active and recent alerts and explains what they mean.

!!! example "Try asking"
    - "Are there any active alerts?"
    - "What alerts fired in the last 24 hours?"
    - "Has anything triggered a warning today?"

---

### Root Cause Analysis

> Underlying tool: `GetDiagnosis`

Tessa diagnoses current system issues by analyzing recent errors, grouping them by root cause, and ranking them by severity.

!!! example "Try asking"
    - "Why is checkout slow?"
    - "What's causing 500 errors on the payment service?"
    - "Root cause the latency spike at 2pm"
    - "Why did order-service start failing?"

---

### Pressure Detection

Identify services under active strain before they fail. Tessa detects services under pressure by comparing the current window against a 30-minute baseline.

!!! example "Try asking"
    - "Is there pressure building anywhere?"
    - "Which services are under stress?"
    - "Are any services approaching their limits?"
    - "What's at risk of failing soon?"

---

### Trend Analysis

Understand how metrics are changing over time. Tessa analyzes latency, error rate, and throughput trends by comparing recent performance against a baseline, and flags anything unusual.

!!! example "Try asking"
    - "Show me the latency trend for auth-service"
    - "How has error rate changed over the last 6 hours?"
    - "Is response time getting worse on the /api/users endpoint?"
    - "What's the throughput trend for the database?"

---

### Service Dependency Map

Understand how services connect and depend on each other. Tessa returns a service dependency map: each service, its inter-service dependencies, and its health, latency, and error rates. This is structured data she reports in the conversation, not a separate rendered diagram.

!!! example "Try asking"
    - "Show me the service dependency map"
    - "What services depend on order-service?"
    - "Map out the request path from gateway to database"
    - "What are the downstream dependencies of auth-service?"

---

### Service Detail

> Underlying tool: `GetServiceDetail`

Drill into a single named service for a focused view: error rate, latency, top errors, top endpoints, and dependencies for that service alone.

!!! example "Try asking"
    - "Tell me about order-service"
    - "What's the current state of payment-service?"
    - "Give me the details for auth-service"

---

### Incident Timeline

> Underlying tool: `GetIncidentTimeline`

Build a chronological view of events to understand what happened and in what order. Tessa assembles a service-level event sequence - when each service first errored, spiked in latency, or degraded.

!!! example "Try asking"
    - "Build me a timeline of events in the last hour"
    - "What happened between 2pm and 3pm?"
    - "Show me the sequence of events leading up to the outage"
    - "What events occurred around the time errors started?"

---

### Slowest Endpoints

Find the endpoints dragging down your system's performance. Tessa returns the top 20 slowest endpoints ranked by P99 latency.

!!! example "Try asking"
    - "What are the slowest endpoints?"
    - "Which API calls take the longest?"
    - "Show me the top 10 slowest endpoints in the last hour"
    - "Are there any endpoints with p99 latency over 2 seconds?"

---

### Deployment Correlation

> Underlying tool: `GetDeploymentCorrelation`

Detect what changed in your system recently. Tessa surfaces new service versions, new services, new endpoints, and new hosts, so you can line changes up against performance shifts.

!!! example "Try asking"
    - "What changed recently?"
    - "Were there any deployments in the last 24 hours?"
    - "Did a deployment cause this regression?"
    - "What was deployed right before errors started?"

---

### Time-Window Comparison

Compare two time periods to understand what changed. Tessa compares system performance between two time windows (by default, the last 15 minutes versus the same window yesterday), evaluating differences in latency, error rates, and throughput.

!!! example "Try asking"
    - "Compare the last hour to the same time yesterday"
    - "How does this morning compare to last Monday?"
    - "Is performance better or worse than last week?"
    - "Compare pre-deployment to post-deployment metrics"

---

## Trace and log access

For trace-specific and log-specific questions, Tessa has a separate family of tools that read directly from your Grid's trace and log stores. Where the diagnostic capabilities above synthesize across data sources, these tools fetch specific traces, spans, or logs by ID or filter.

| Tool | What it does |
|---|---|
| `GetTraces` | Find traces matching a time range or filter |
| `GetTrace` | Fetch a single trace by ID |
| `GetTraceSpans` | List the spans inside a specific trace |
| `GetTraceSpanTags` | Read attributes on a specific span |
| `GetTraceSpanEvents` | Read events recorded on a specific span |
| `GetTraceErrors` | Pull error-related spans from a trace |
| `GetTraceLogs` | Pull logs correlated to a trace |
| `GetLogs` | Find logs matching a time range or filter |
| `GetLog` | Fetch a single log entry |
| `GetTraceFilterFacets` | List available filter values for trace queries |
| `GetLogFilterFacets` | List available filter values for log queries |

Tessa selects from this family automatically when you ask trace- or log-specific questions.

!!! example "Try asking"
    - "Find slow traces for the checkout flow"
    - "Show me traces with errors on payment-service"
    - "What does a typical request to /api/orders look like?"
    - "Find traces where database calls took over 500ms"
    - "Show me logs from the last hour with 'timeout' in the message"

---

## APM context and dashboards

These tools surface the broader Grid context that informs Tessa's answers but are rarely invoked directly by a single user question.

| Tool | What it does |
|---|---|
| `GetGridInfo` | Information about the current Grid (capabilities, scope) |
| `GetAvailableCharts` | Discover what charts can be rendered |
| `GetRangeData` | Pull metric data for a time range |
| `GetDashboard` | Fetch a specific dashboard definition |

## Context Awareness in 3D

In DeepCube, Tessa knows where you are. She tracks your current room and what you're looking at, which means you can ask contextual questions without specifying the target.

| Where You Are | What Tessa Knows |
|---------------|------------------|
| Standing near a service node | Which service you're investigating |
| Inside the Diagnostics cube | Which trace you're viewing |
| Viewing the service graph | The overall topology you see |
| Looking at a performance chart | The metric and time range in view |

!!! tip "Contextual shorthand"
    Instead of "What's the health of order-service?", you can walk up to the order-service node and just ask "What's wrong here?" - Tessa fills in the context.

## Chaining Diagnostics

Tessa's real power shows when she chains multiple diagnostics together. A single question like "Why did checkout break after today's deployment?" might trigger:

1. **Deployment detection** - to identify what was deployed
2. **Time-window comparison** - to compare before and after
3. **Root cause analysis** - to trace the chain of causation
4. **Trace exploration** - to find specific failing traces

You don't need to run these one at a time. Ask the high-level question and let Tessa orchestrate the investigation.
