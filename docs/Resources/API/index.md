# API Reference

{!template/subscription-required.mdp!}

The DeepCube REST API provides programmatic access to your observability data - traces, logs, diagnostics, charts, and AI Assistant capabilities. Use it to integrate DeepCube into your workflows, build custom dashboards, or automate incident response.

## Base URL

All API requests are made to:

```
https://api-azure.deepcube.ai
```

## API Versioning

The current API version is **2.0**. You must specify the version on every request using one of these methods:

=== "Query Parameter"

    ```
    GET /apm/traces/{gridSecondaryId}/filters?api-version=2.0
    ```

=== "Header"

    ```
    X-Api-Version: 2.0
    ```

!!! warning "Version Required"
    Requests without a version specifier will be rejected with `400 Bad Request`.

## Authentication

The API supports two authentication methods:

| Method | Header | Use Case |
|--------|--------|----------|
| **OAuth 2.0** | `Authorization: Bearer {token}` | User-context access, interactive apps |
| **API Key** | `api-key: {key}` | Server-to-server, automation scripts |

See the [Authentication Guide](authentication.md) for setup instructions, token acquisition, and scopes.

## Common Parameters

These parameters appear across multiple endpoints:

| Parameter | Type | Description |
|-----------|------|-------------|
| `gridSecondaryId` | `string` (UUID) | Identifies the Grid containing your telemetry data |
| `api-version` | `string` | API version - currently `2.0` |
| `rangeStart` | `datetime` (ISO 8601) | Start of the time window for queries |
| `rangeEnd` | `datetime` (ISO 8601) | End of the time window for queries |

## Error Handling

The API returns errors in [RFC 7807 ProblemDetails](https://datatracker.ietf.org/doc/html/rfc7807) format:

```json
{
  "type": "https://tools.ietf.org/html/rfc7807",
  "title": "Bad Request",
  "status": 400,
  "detail": "The rangeStart parameter is required.",
  "instance": "/apm/traces/3fa85f64-5717-4562-b3fc-2c963f66afa6"
}
```

### Status Codes

| Code | Meaning |
|------|---------|
| `200 OK` | Request succeeded |
| `400 Bad Request` | Invalid parameters or request body |
| `401 Unauthorized` | Missing or invalid authentication |
| `403 Forbidden` | Authenticated but insufficient permissions |
| `404 Not Found` | Resource does not exist |
| `429 Too Many Requests` | Rate limit exceeded - see below |

## Rate Limiting

API requests are rate-limited per user and per Grid. When you exceed the limit, the API returns `429 Too Many Requests` with a `Retry-After` header indicating how many seconds to wait.

```
HTTP/1.1 429 Too Many Requests
Retry-After: 30
Content-Type: application/problem+json
```

!!! tip "Handling Rate Limits"
    Implement exponential backoff in your client. Check the `Retry-After` header value before retrying.

## Endpoint Groups

| Group | Endpoints | Description |
|-------|-----------|-------------|
| [Traces](traces.md) | 8 | Search, filter, and inspect distributed traces and spans |
| [Logs](logs.md) | 3 | Search and retrieve log entries with filtering |
| [Diagnostics](diagnostics.md) | 11 | Health checks, root cause analysis, pressure detection, trends, service maps |
| [Charts & Dashboards](charts.md) | 4 | Retrieve chart metadata, render charts, query dashboard layouts |
| [AI Assistant](assistant.md) | 9 | Chat with Tessa, speech synthesis/recognition, usage tracking, limits |

## Quick Start

1. [Get your API key](../../Getting-Started/Api-Key/index.md) or [set up OAuth 2.0](authentication.md)
2. Pick an endpoint group from the table above
3. Make your first request:

```bash
curl -X GET "https://api-azure.deepcube.ai/apm/diagnostics/{gridSecondaryId}/health?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```
