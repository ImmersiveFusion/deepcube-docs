# Logs

{!template/subscription-required.mdp!}

The Logs API provides access to structured log data collected from your instrumented applications. Search logs with filters, retrieve individual log entries, and discover available filter options.

!!! info "Authentication Required"
    All endpoints require a valid `Authorization: Bearer {token}` or `api-key: {key}` header. See [Authentication](authentication.md).

---

## Search Logs

Search and filter log entries within a time range.

```
POST /apm/logs/{gridSecondaryId}
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Request Body

`LogListFilterModel`:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `rangeStart` | `datetime` (ISO 8601) | Yes | Start of time window |
| `rangeEnd` | `datetime` (ISO 8601) | Yes | End of time window |
| `severityLevel` | `string` | No | Filter by severity (`Trace`, `Debug`, `Information`, `Warning`, `Error`, `Fatal`) |
| `serviceName` | `string` | No | Filter by service name |
| `body` | `string` | No | Full-text search within log message body |
| `traceId` | `string` | No | Filter by correlated trace ID |
| `spanId` | `string` | No | Filter by correlated span ID |
| `attributes` | `object` | No | Key-value attribute filters |
| `page` | `integer` | No | Page number (default: `1`) |
| `pageSize` | `integer` | No | Results per page (default: `20`, max: `100`) |

### Example Request

```bash
curl -X POST "https://api-azure.iapm.app/apm/logs/3fa85f64-5717-4562-b3fc-2c963f66afa6?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "rangeStart": "2026-04-02T12:00:00Z",
    "rangeEnd": "2026-04-02T13:00:00Z",
    "severityLevel": "Error",
    "serviceName": "payment-service"
  }'
```

### Example Response

```json
{
  "items": [
    {
      "id": "log-0042",
      "timestamp": "2026-04-02T12:15:33.221Z",
      "severityLevel": "Error",
      "body": "Payment gateway returned HTTP 503: Service Unavailable",
      "serviceName": "payment-service",
      "traceId": "def456abc789012345678901",
      "spanId": "span-017",
      "attributes": {
        "http.status_code": 503,
        "payment.provider": "stripe",
        "payment.amount": 149.99
      }
    },
    {
      "id": "log-0043",
      "timestamp": "2026-04-02T12:15:34.002Z",
      "severityLevel": "Error",
      "body": "Retry exhausted for payment processing",
      "serviceName": "payment-service",
      "traceId": "def456abc789012345678901",
      "spanId": "span-018",
      "attributes": {
        "retry.count": 3,
        "exception.type": "PaymentException"
      }
    }
  ],
  "totalCount": 156,
  "page": 1,
  "pageSize": 20
}
```

---

## Get Log Entry Details

Retrieve the full details of a specific log entry.

```
GET /apm/logs/{gridSecondaryId}/details/{spanId}
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `spanId` | path | `string` | Yes | Span identifier for the log entry |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/logs/3fa85f64-5717-4562-b3fc-2c963f66afa6/details/span-017?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "id": "log-0042",
  "timestamp": "2026-04-02T12:15:33.221Z",
  "severityLevel": "Error",
  "severityNumber": 17,
  "body": "Payment gateway returned HTTP 503: Service Unavailable",
  "serviceName": "payment-service",
  "traceId": "def456abc789012345678901",
  "spanId": "span-017",
  "attributes": {
    "http.status_code": 503,
    "payment.provider": "stripe",
    "payment.amount": 149.99,
    "net.peer.name": "api.stripe.com",
    "deployment.environment": "production"
  },
  "resource": {
    "service.name": "payment-service",
    "service.version": "1.8.3",
    "host.name": "prod-payment-02",
    "os.type": "linux"
  }
}
```

---

## Get Log Filters

Retrieve available filter options for the log search interface. Returns severity levels, service names, and attribute keys present in the data.

```
GET /apm/logs/{gridSecondaryId}/filters
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/logs/3fa85f64-5717-4562-b3fc-2c963f66afa6/filters?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "severityLevels": [
    "Trace",
    "Debug",
    "Information",
    "Warning",
    "Error",
    "Fatal"
  ],
  "serviceNames": [
    "order-service",
    "payment-service",
    "inventory-service",
    "notification-service"
  ],
  "attributeKeys": [
    "http.status_code",
    "exception.type",
    "deployment.environment",
    "payment.provider"
  ]
}
```

!!! tip "Building Search UIs"
    Call the filters endpoint first to populate dropdown menus in your search interface, then pass selected values to the search endpoint.
