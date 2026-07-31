# Traces

{!template/subscription-required.mdp!}

The Traces API provides access to distributed tracing data collected by your instrumented applications. Search traces, inspect individual spans, retrieve correlated logs and errors, and explore span metadata.

!!! info "Authentication Required"
    All endpoints require a valid `Authorization: Bearer {token}` or `api-key: {key}` header. See [Authentication](authentication.md).

---

## Search Traces

Search and filter traces within a time range.

```
POST /apm/traces/{gridSecondaryId}
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Request Body

`TraceListFilterModel`:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `rangeStart` | `datetime` (ISO 8601) | Yes | Start of time window |
| `rangeEnd` | `datetime` (ISO 8601) | Yes | End of time window |
| `serviceName` | `string` | No | Filter by service name |
| `operationName` | `string` | No | Filter by operation name |
| `minDuration` | `integer` (ms) | No | Minimum span duration |
| `maxDuration` | `integer` (ms) | No | Maximum span duration |
| `status` | `string` | No | Filter by status (`OK`, `ERROR`) |
| `tags` | `object` | No | Key-value tag filters |
| `page` | `integer` | No | Page number (default: `1`) |
| `pageSize` | `integer` | No | Results per page (default: `20`, max: `100`) |

### Example Request

```bash
curl -X POST "https://api-azure.iapm.app/apm/traces/3fa85f64-5717-4562-b3fc-2c963f66afa6?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "rangeStart": "2026-04-02T00:00:00Z",
    "rangeEnd": "2026-04-03T00:00:00Z",
    "serviceName": "order-service",
    "status": "ERROR",
    "minDuration": 500
  }'
```

### Example Response

```json
{
  "items": [
    {
      "traceId": "abc123def456789012345678",
      "spanId": "span-001",
      "serviceName": "order-service",
      "operationName": "POST /api/orders",
      "duration": 1523,
      "status": "ERROR",
      "startTime": "2026-04-02T14:32:01.445Z",
      "endTime": "2026-04-02T14:32:02.968Z"
    }
  ],
  "totalCount": 47,
  "page": 1,
  "pageSize": 20
}
```

---

## Get Trace Details

Retrieve detailed information for a specific span.

```
GET /apm/traces/{gridSecondaryId}/details/{spanId}
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `spanId` | path | `string` | Yes | Span identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/traces/3fa85f64-5717-4562-b3fc-2c963f66afa6/details/span-001?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "traceId": "abc123def456789012345678",
  "spanId": "span-001",
  "parentSpanId": "span-000",
  "serviceName": "order-service",
  "operationName": "POST /api/orders",
  "spanKind": "SERVER",
  "status": "ERROR",
  "statusMessage": "Internal Server Error",
  "startTime": "2026-04-02T14:32:01.445Z",
  "endTime": "2026-04-02T14:32:02.968Z",
  "duration": 1523,
  "attributes": {
    "http.method": "POST",
    "http.url": "/api/orders",
    "http.status_code": 500,
    "net.peer.name": "db-primary.internal"
  }
}
```

---

## Get Trace Filters

Retrieve available filter options for the traces search interface. Returns service names, operation names, status values, and tag keys present in the data.

```
GET /apm/traces/{gridSecondaryId}/filters
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/traces/3fa85f64-5717-4562-b3fc-2c963f66afa6/filters?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "serviceNames": [
    "order-service",
    "payment-service",
    "inventory-service"
  ],
  "operationNames": [
    "POST /api/orders",
    "GET /api/products",
    "POST /api/payments"
  ],
  "statusValues": ["OK", "ERROR"],
  "tagKeys": [
    "http.method",
    "http.status_code",
    "deployment.environment"
  ]
}
```

---

## Get Spans for Distributed Trace

Retrieve all spans belonging to a single distributed trace. Use this to reconstruct the full call chain across services.

```
GET /apm/traces/{gridSecondaryId}/correlations/{traceId}/spans
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `traceId` | path | `string` | Yes | Distributed trace identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/traces/3fa85f64-5717-4562-b3fc-2c963f66afa6/correlations/abc123def456789012345678/spans?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "traceId": "abc123def456789012345678",
  "spans": [
    {
      "spanId": "span-000",
      "parentSpanId": null,
      "serviceName": "api-gateway",
      "operationName": "POST /api/orders",
      "spanKind": "SERVER",
      "status": "OK",
      "startTime": "2026-04-02T14:32:01.200Z",
      "duration": 1820
    },
    {
      "spanId": "span-001",
      "parentSpanId": "span-000",
      "serviceName": "order-service",
      "operationName": "POST /api/orders",
      "spanKind": "SERVER",
      "status": "ERROR",
      "startTime": "2026-04-02T14:32:01.445Z",
      "duration": 1523
    },
    {
      "spanId": "span-002",
      "parentSpanId": "span-001",
      "serviceName": "order-service",
      "operationName": "SELECT orders",
      "spanKind": "CLIENT",
      "status": "OK",
      "startTime": "2026-04-02T14:32:01.500Z",
      "duration": 45
    }
  ]
}
```

---

## Get Logs for Trace

Retrieve all log entries correlated to a specific distributed trace.

```
GET /apm/traces/{gridSecondaryId}/correlations/{traceId}/logs
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `traceId` | path | `string` | Yes | Distributed trace identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/traces/3fa85f64-5717-4562-b3fc-2c963f66afa6/correlations/abc123def456789012345678/logs?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "traceId": "abc123def456789012345678",
  "logs": [
    {
      "timestamp": "2026-04-02T14:32:01.450Z",
      "severityLevel": "Error",
      "body": "Failed to process order: database connection timeout",
      "serviceName": "order-service",
      "spanId": "span-001",
      "attributes": {
        "exception.type": "System.TimeoutException",
        "exception.message": "Connection pool exhausted"
      }
    }
  ]
}
```

---

## Get Errors for Trace

Retrieve all error events correlated to a specific distributed trace.

```
GET /apm/traces/{gridSecondaryId}/correlations/{traceId}/errors
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `traceId` | path | `string` | Yes | Distributed trace identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/traces/3fa85f64-5717-4562-b3fc-2c963f66afa6/correlations/abc123def456789012345678/errors?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "traceId": "abc123def456789012345678",
  "errors": [
    {
      "timestamp": "2026-04-02T14:32:02.900Z",
      "spanId": "span-001",
      "serviceName": "order-service",
      "exceptionType": "System.TimeoutException",
      "message": "Connection pool exhausted after 30000ms",
      "stackTrace": "at OrderService.CreateOrder(...)\n  at OrderController.Post(...)",
      "attributes": {
        "http.status_code": 500
      }
    }
  ]
}
```

---

## Get Span Tags

Retrieve all tags (attributes) for a specific span.

```
GET /apm/traces/{gridSecondaryId}/spans/{spanId}/tags
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `spanId` | path | `string` | Yes | Span identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/traces/3fa85f64-5717-4562-b3fc-2c963f66afa6/spans/span-001/tags?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "spanId": "span-001",
  "tags": {
    "http.method": "POST",
    "http.url": "/api/orders",
    "http.status_code": 500,
    "net.peer.name": "db-primary.internal",
    "net.peer.port": 5432,
    "db.system": "postgresql",
    "deployment.environment": "production",
    "service.version": "2.4.1"
  }
}
```

---

## Get Span Events

Retrieve all events recorded on a specific span (exceptions, log entries, custom events).

```
GET /apm/traces/{gridSecondaryId}/spans/{spanId}/events
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `spanId` | path | `string` | Yes | Span identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/traces/3fa85f64-5717-4562-b3fc-2c963f66afa6/spans/span-001/events?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "spanId": "span-001",
  "events": [
    {
      "name": "exception",
      "timestamp": "2026-04-02T14:32:02.900Z",
      "attributes": {
        "exception.type": "System.TimeoutException",
        "exception.message": "Connection pool exhausted after 30000ms",
        "exception.stacktrace": "at OrderService.CreateOrder(...)"
      }
    },
    {
      "name": "retry_attempt",
      "timestamp": "2026-04-02T14:32:02.100Z",
      "attributes": {
        "retry.count": 3,
        "retry.delay_ms": 200
      }
    }
  ]
}
```
