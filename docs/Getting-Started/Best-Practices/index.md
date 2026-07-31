# OpenTelemetry Best Practices

Guidelines for effective instrumentation and observability with Immersive APM.

## Resource Attributes

Set resource attributes to identify your services clearly in Immersive APM:

```
OTEL_SERVICE_NAME=my-service
OTEL_RESOURCE_ATTRIBUTES=service.version=1.2.3,deployment.environment=production
```

**Recommended attributes:**

| Attribute | Description | Example |
|-----------|-------------|---------|
| `service.name` | Unique service identifier | `checkout-api` |
| `service.version` | Deployment version | `1.2.3` |
| `deployment.environment` | Environment name | `production`, `staging` |
| `service.namespace` | Logical grouping | `ecommerce` |

## Auto vs Manual Instrumentation

**Start with auto-instrumentation** - It captures HTTP, database, and messaging telemetry with zero code changes.

| Language | Auto-Instrumentation |
|----------|---------------------|
| Java | [Java Agent](https://opentelemetry.io/docs/languages/java/automatic/){ target="_blank" } |
| .NET | [.NET Auto-Instrumentation](https://opentelemetry.io/docs/languages/net/automatic/){ target="_blank" } |
| Python | [Python Auto-Instrumentation](https://opentelemetry.io/docs/languages/python/automatic/){ target="_blank" } |
| Node.js | [Node.js Auto-Instrumentation](https://opentelemetry.io/docs/languages/js/automatic/){ target="_blank" } |

**Add manual instrumentation** when you need:

- Custom business metrics (orders processed, revenue)
- Domain-specific span attributes
- Fine-grained control over what's captured

## Semantic Conventions

Use [OpenTelemetry Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/){ target="_blank" } for consistent attribute naming:

```
# HTTP
http.request.method=GET
http.response.status_code=200
url.path=/api/users

# Database
db.system=postgresql
db.operation.name=SELECT

# Messaging
messaging.system=rabbitmq
messaging.operation.type=publish
```

Using standard conventions helps Immersive APM display richer context automatically.

## Sampling Strategies

For high-traffic applications, implement sampling to control data volume:

| Strategy | When to Use |
|----------|-------------|
| **Always On** | Development, low-traffic services |
| **Probabilistic** | Production with moderate traffic |
| **Rate Limiting** | High-traffic services |
| **Parent-Based** | Distributed systems (respects upstream decisions) |

```bash
# Sample 10% of traces
OTEL_TRACES_SAMPLER=parentbased_traceidratio
OTEL_TRACES_SAMPLER_ARG=0.1
```

## Performance Tips

### Batch Exports

Configure batching to reduce network overhead:

```bash
OTEL_BSP_MAX_QUEUE_SIZE=2048
OTEL_BSP_MAX_EXPORT_BATCH_SIZE=512
OTEL_BSP_SCHEDULE_DELAY=5000
```

### Limit Attribute Size

Avoid large attribute values that bloat telemetry:

- Keep string attributes under 1KB
- Limit array attributes to essential items
- Don't include full request/response bodies

### Use Async Exports

Ensure telemetry export doesn't block your application's critical path. Most OpenTelemetry SDKs export asynchronously by default.

## Common Pitfalls

!!! warning "Avoid These Mistakes"

    **Missing service.name** - Services appear as "unknown" in Immersive APM

    **Over-instrumentation** - Every function call doesn't need a span; focus on meaningful operations

    **Sensitive data in attributes** - Never include passwords, tokens, or PII in telemetry

    **Ignoring errors** - Ensure exceptions are captured and attached to spans

## Checklist

Before going to production:

- [ ] `service.name` is set and meaningful
- [ ] `deployment.environment` distinguishes prod/staging/dev
- [ ] Auto-instrumentation is configured for frameworks in use
- [ ] Sampling is appropriate for traffic volume
- [ ] No sensitive data in attributes
- [ ] Telemetry export is working (verify in Immersive APM)

## Related

- [Instrument Your Application](../../Instrument/index.md) - Setup guide
- [OpenTelemetry Docs](https://opentelemetry.io/docs/){ target="_blank" } - Official documentation
- [Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/){ target="_blank" } - Attribute naming standards
