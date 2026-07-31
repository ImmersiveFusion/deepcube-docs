# Diagnostics

{!template/subscription-required.mdp!}

The Diagnostics API is the most powerful section of the IAPM API. It provides automated system health analysis, root cause diagnosis, pressure detection, trend analysis, service dependency mapping, incident timelines, and time-window comparison - all computed from your live telemetry data.

!!! info "Authentication Required"
    All endpoints require a valid `Authorization: Bearer {token}` or `api-key: {key}` header. See [Authentication](authentication.md).

---

## System Health

Get a comprehensive health overview of your system, including per-service health status, error rates, and Apdex scores.

```
GET /apm/diagnostics/{gridSecondaryId}/health
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/diagnostics/3fa85f64-5717-4562-b3fc-2c963f66afa6/health?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "overallStatus": "degraded",
  "timestamp": "2026-04-03T10:00:00Z",
  "services": [
    {
      "serviceName": "order-service",
      "status": "healthy",
      "errorRate": 0.2,
      "apdex": 0.94,
      "requestCount": 15230,
      "avgLatencyMs": 120
    },
    {
      "serviceName": "payment-service",
      "status": "degraded",
      "errorRate": 8.5,
      "apdex": 0.61,
      "requestCount": 4820,
      "avgLatencyMs": 2340
    },
    {
      "serviceName": "inventory-service",
      "status": "healthy",
      "errorRate": 0.1,
      "apdex": 0.97,
      "requestCount": 9100,
      "avgLatencyMs": 45
    }
  ]
}
```

!!! tip "Apdex Score"
    Apdex (Application Performance Index) ranges from 0 to 1. Scores above 0.9 indicate satisfied users; below 0.7 signals performance problems.

---

## Alert Status

Retrieve active alerts triggered by threshold rules configured for your Grid.

```
GET /apm/diagnostics/{gridSecondaryId}/alerts
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/diagnostics/3fa85f64-5717-4562-b3fc-2c963f66afa6/alerts?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "alerts": [
    {
      "id": "alert-001",
      "ruleName": "High Error Rate",
      "severity": "critical",
      "serviceName": "payment-service",
      "condition": "error_rate > 5%",
      "currentValue": 8.5,
      "triggeredAt": "2026-04-03T09:45:12Z",
      "status": "firing"
    },
    {
      "id": "alert-002",
      "ruleName": "Elevated Latency",
      "severity": "warning",
      "serviceName": "payment-service",
      "condition": "p95_latency > 2000ms",
      "currentValue": 2340,
      "triggeredAt": "2026-04-03T09:47:30Z",
      "status": "firing"
    }
  ]
}
```

---

## Root Cause Analysis

Get automated root cause analysis grouped by probable cause. The diagnostics engine correlates errors, latency spikes, and anomalies to identify underlying issues.

```
GET /apm/diagnostics/{gridSecondaryId}/diagnosis
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/diagnostics/3fa85f64-5717-4562-b3fc-2c963f66afa6/diagnosis?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "diagnoses": [
    {
      "cause": "Database connection pool exhaustion",
      "confidence": 0.92,
      "severity": "critical",
      "affectedServices": ["payment-service", "order-service"],
      "evidence": [
        "Connection pool wait time increased 15x in the last 30 minutes",
        "payment-service: 847 timeout exceptions from connection pool",
        "Database active connections at 100% capacity (200/200)"
      ],
      "firstDetected": "2026-04-03T09:42:00Z",
      "impactedTraceCount": 1243
    },
    {
      "cause": "Upstream dependency degradation",
      "confidence": 0.78,
      "severity": "warning",
      "affectedServices": ["notification-service"],
      "evidence": [
        "SMTP gateway response times increased from 50ms to 800ms",
        "3 consecutive health check failures for smtp.provider.com"
      ],
      "firstDetected": "2026-04-03T09:55:00Z",
      "impactedTraceCount": 89
    }
  ]
}
```

!!! note "Confidence Scores"
    Each diagnosis includes a confidence score (0 to 1). Higher scores indicate stronger correlation between the identified cause and observed symptoms.

---

## Pressure Detection

Detect active system pressure - resource contention, queue buildup, saturation, and throttling happening right now.

```
GET /apm/diagnostics/{gridSecondaryId}/pressure
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/diagnostics/3fa85f64-5717-4562-b3fc-2c963f66afa6/pressure?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "pressurePoints": [
    {
      "type": "connection_pool",
      "serviceName": "payment-service",
      "resource": "PostgreSQL primary",
      "utilization": 100,
      "capacity": 200,
      "queueDepth": 47,
      "severity": "critical",
      "detectedAt": "2026-04-03T09:42:00Z"
    },
    {
      "type": "thread_pool",
      "serviceName": "order-service",
      "resource": "Worker thread pool",
      "utilization": 87,
      "capacity": 100,
      "queueDepth": 12,
      "severity": "warning",
      "detectedAt": "2026-04-03T09:50:00Z"
    }
  ]
}
```

---

## Trends

Retrieve latency, error rate, and throughput trends over time.

```
GET /apm/diagnostics/{gridSecondaryId}/trends
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/diagnostics/3fa85f64-5717-4562-b3fc-2c963f66afa6/trends?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "latency": {
    "trend": "increasing",
    "changePercent": 45.2,
    "current": {
      "p50": 180,
      "p95": 2340,
      "p99": 4500
    },
    "baseline": {
      "p50": 95,
      "p95": 450,
      "p99": 900
    }
  },
  "errorRate": {
    "trend": "increasing",
    "changePercent": 320.0,
    "current": 8.5,
    "baseline": 2.0
  },
  "throughput": {
    "trend": "decreasing",
    "changePercent": -15.3,
    "currentRps": 245,
    "baselineRps": 289
  }
}
```

---

## Service Dependency Map

Retrieve the service dependency graph showing how services communicate, with traffic volume and error rates on each edge.

```
GET /apm/diagnostics/{gridSecondaryId}/services
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/diagnostics/3fa85f64-5717-4562-b3fc-2c963f66afa6/services?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "services": [
    {
      "name": "api-gateway",
      "type": "SERVER",
      "requestCount": 25000,
      "errorRate": 3.2
    },
    {
      "name": "order-service",
      "type": "SERVER",
      "requestCount": 15230,
      "errorRate": 0.2
    },
    {
      "name": "payment-service",
      "type": "SERVER",
      "requestCount": 4820,
      "errorRate": 8.5
    }
  ],
  "edges": [
    {
      "source": "api-gateway",
      "target": "order-service",
      "requestCount": 12400,
      "errorRate": 0.1,
      "avgLatencyMs": 135
    },
    {
      "source": "order-service",
      "target": "payment-service",
      "requestCount": 4820,
      "errorRate": 8.5,
      "avgLatencyMs": 2280
    },
    {
      "source": "payment-service",
      "target": "PostgreSQL",
      "requestCount": 19200,
      "errorRate": 12.3,
      "avgLatencyMs": 1800
    }
  ]
}
```

!!! tip "Visualizing the Service Map"
    The service dependency data maps directly to the 3D service topology rendered in the IAPM Diagnostics cube. Use the `edges` array to reconstruct the call graph in your own tooling.

---

## Incident Timeline

Get a chronological timeline of incidents, anomalies, and significant events detected in your system.

```
GET /apm/diagnostics/{gridSecondaryId}/timeline
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/diagnostics/3fa85f64-5717-4562-b3fc-2c963f66afa6/timeline?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "events": [
    {
      "timestamp": "2026-04-03T09:30:00Z",
      "type": "deployment",
      "description": "payment-service v1.8.3 deployed to production",
      "severity": "info",
      "serviceName": "payment-service"
    },
    {
      "timestamp": "2026-04-03T09:42:00Z",
      "type": "anomaly",
      "description": "Connection pool utilization exceeded 95% threshold",
      "severity": "warning",
      "serviceName": "payment-service"
    },
    {
      "timestamp": "2026-04-03T09:45:12Z",
      "type": "alert",
      "description": "High error rate alert triggered: 8.5% (threshold: 5%)",
      "severity": "critical",
      "serviceName": "payment-service"
    },
    {
      "timestamp": "2026-04-03T09:55:00Z",
      "type": "anomaly",
      "description": "Upstream SMTP gateway degradation detected",
      "severity": "warning",
      "serviceName": "notification-service"
    }
  ]
}
```

---

## Service Deep Dive

Get detailed diagnostics for a single service, including endpoint-level performance, error breakdown, and dependency health.

```
GET /apm/diagnostics/{gridSecondaryId}/service/{serviceName}
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `serviceName` | path | `string` | Yes | Name of the service to inspect |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/diagnostics/3fa85f64-5717-4562-b3fc-2c963f66afa6/service/payment-service?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "serviceName": "payment-service",
  "status": "degraded",
  "apdex": 0.61,
  "errorRate": 8.5,
  "requestCount": 4820,
  "endpoints": [
    {
      "operation": "POST /api/payments",
      "requestCount": 3200,
      "errorRate": 12.1,
      "avgLatencyMs": 2800,
      "p95LatencyMs": 4500
    },
    {
      "operation": "GET /api/payments/{id}",
      "requestCount": 1620,
      "errorRate": 0.5,
      "avgLatencyMs": 85,
      "p95LatencyMs": 200
    }
  ],
  "topErrors": [
    {
      "exceptionType": "System.TimeoutException",
      "message": "Connection pool exhausted",
      "count": 387,
      "percentage": 94.2
    }
  ],
  "dependencies": [
    {
      "name": "PostgreSQL",
      "status": "degraded",
      "errorRate": 12.3,
      "avgLatencyMs": 1800
    },
    {
      "name": "stripe-api",
      "status": "healthy",
      "errorRate": 0.3,
      "avgLatencyMs": 250
    }
  ]
}
```

---

## Slowest Endpoints

Get the top 20 slowest SERVER-type endpoints across all services.

```
GET /apm/diagnostics/{gridSecondaryId}/slowest-endpoints
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/diagnostics/3fa85f64-5717-4562-b3fc-2c963f66afa6/slowest-endpoints?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "endpoints": [
    {
      "rank": 1,
      "serviceName": "payment-service",
      "operation": "POST /api/payments",
      "avgLatencyMs": 2800,
      "p95LatencyMs": 4500,
      "p99LatencyMs": 6200,
      "requestCount": 3200,
      "errorRate": 12.1
    },
    {
      "rank": 2,
      "serviceName": "report-service",
      "operation": "GET /api/reports/generate",
      "avgLatencyMs": 1850,
      "p95LatencyMs": 3200,
      "p99LatencyMs": 4100,
      "requestCount": 450,
      "errorRate": 2.0
    },
    {
      "rank": 3,
      "serviceName": "order-service",
      "operation": "POST /api/orders/bulk",
      "avgLatencyMs": 980,
      "p95LatencyMs": 1800,
      "p99LatencyMs": 2500,
      "requestCount": 120,
      "errorRate": 0.8
    }
  ]
}
```

!!! note "SERVER Spans Only"
    This endpoint returns only SERVER-type spans, filtering out CLIENT, PRODUCER, and CONSUMER spans to focus on your application's own endpoint performance.

---

## Change Detection

Detect recent deployments and configuration changes that may correlate with performance shifts.

```
GET /apm/diagnostics/{gridSecondaryId}/changes
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/diagnostics/3fa85f64-5717-4562-b3fc-2c963f66afa6/changes?api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "changes": [
    {
      "type": "deployment",
      "serviceName": "payment-service",
      "detectedAt": "2026-04-03T09:30:00Z",
      "previousVersion": "1.8.2",
      "currentVersion": "1.8.3",
      "performanceImpact": {
        "latencyChange": "+145%",
        "errorRateChange": "+325%",
        "assessment": "negative"
      }
    },
    {
      "type": "scaling",
      "serviceName": "order-service",
      "detectedAt": "2026-04-03T08:00:00Z",
      "description": "Instance count changed from 3 to 5",
      "performanceImpact": {
        "latencyChange": "-22%",
        "errorRateChange": "-5%",
        "assessment": "positive"
      }
    }
  ]
}
```

!!! tip "Post-Deployment Validation"
    Combine the changes endpoint with the [Compare](#compare-time-windows) endpoint to quantify the impact of a deployment by comparing a baseline window (before) with the current window (after).

---

## Compare Time Windows

Compare two time windows side by side to identify performance regressions or improvements. Useful for before/after deployment analysis, week-over-week comparison, or incident vs. normal operation.

```
GET /apm/diagnostics/{gridSecondaryId}/compare
```

### Parameters

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| `gridSecondaryId` | path | `string` (UUID) | Yes | Grid identifier |
| `currentStart` | query | `datetime` (ISO 8601) | Yes | Start of the current (comparison) window |
| `currentEnd` | query | `datetime` (ISO 8601) | Yes | End of the current window |
| `baselineStart` | query | `datetime` (ISO 8601) | Yes | Start of the baseline window |
| `baselineEnd` | query | `datetime` (ISO 8601) | Yes | End of the baseline window |
| `api-version` | query | `string` | Yes | API version - `2.0` |

### Example Request

```bash
curl -X GET "https://api-azure.iapm.app/apm/diagnostics/3fa85f64-5717-4562-b3fc-2c963f66afa6/compare?currentStart=2026-04-03T09:30:00Z&currentEnd=2026-04-03T10:30:00Z&baselineStart=2026-04-02T09:30:00Z&baselineEnd=2026-04-02T10:30:00Z&api-version=2.0" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### Example Response

```json
{
  "baseline": {
    "rangeStart": "2026-04-02T09:30:00Z",
    "rangeEnd": "2026-04-02T10:30:00Z",
    "avgLatencyMs": 95,
    "p95LatencyMs": 450,
    "errorRate": 2.0,
    "throughputRps": 289,
    "apdex": 0.93
  },
  "current": {
    "rangeStart": "2026-04-03T09:30:00Z",
    "rangeEnd": "2026-04-03T10:30:00Z",
    "avgLatencyMs": 180,
    "p95LatencyMs": 2340,
    "errorRate": 8.5,
    "throughputRps": 245,
    "apdex": 0.61
  },
  "deltas": {
    "avgLatencyMs": {
      "absolute": 85,
      "percent": 89.5
    },
    "p95LatencyMs": {
      "absolute": 1890,
      "percent": 420.0
    },
    "errorRate": {
      "absolute": 6.5,
      "percent": 325.0
    },
    "throughputRps": {
      "absolute": -44,
      "percent": -15.2
    },
    "apdex": {
      "absolute": -0.32,
      "percent": -34.4
    }
  },
  "regressions": [
    {
      "serviceName": "payment-service",
      "metric": "errorRate",
      "baselineValue": 1.2,
      "currentValue": 12.1,
      "changePercent": 908.3
    }
  ]
}
```
