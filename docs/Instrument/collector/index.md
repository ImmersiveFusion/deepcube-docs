# OpenTelemetry Collector

{!template/subscription-required.mdp!}

The OpenTelemetry Collector is a vendor-agnostic proxy that receives, processes, and exports telemetry data. This guide covers when to use a Collector, how to configure it for DeepCube, and deployment options for Docker and Kubernetes.

[:octicons-arrow-left-24: Back to Instrument Overview](../index.md)

## When to Use a Collector

You can export telemetry directly from your application to DeepCube, or route it through a Collector first. Here is when each approach makes sense:

| Approach | Best For |
|----------|----------|
| **Direct export** | Simple deployments, few services, getting started quickly |
| **Via Collector** | Production deployments, multiple services, when you need batching, retry, or enrichment |

Benefits of using a Collector:

- **Centralized configuration** - Change the OTLP endpoint or API key in one place instead of every service
- **Batching and retry** - The Collector handles buffering and retries, reducing load on your applications
- **Enrichment** - Add Kubernetes metadata, environment tags, or other attributes
- **Sampling** - Apply tail-based or probabilistic sampling before export
- **Multiple destinations** - Fan out telemetry to DeepCube and other backends simultaneously
- **Protocol translation** - Accept telemetry over gRPC, HTTP, Zipkin, Jaeger, and export as OTLP

## Collector Configuration

The Collector uses a YAML configuration file with four main sections: receivers, processors, exporters, and service pipelines.

### Minimal Configuration

```yaml
# otel-collector-config.yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:
    timeout: 5s
    send_batch_size: 1024

exporters:
  otlp/deepcube:
    endpoint: otlp.deepcube.ai:443
    headers:
      api-key: YOUR-API-KEY

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp/deepcube]
    metrics:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp/deepcube]
    logs:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp/deepcube]
```

### Production Configuration

A more complete configuration with memory limiting, resource detection, and health checks:

```yaml
# otel-collector-config.yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:
    timeout: 5s
    send_batch_size: 1024
    send_batch_max_size: 2048

  memory_limiter:
    check_interval: 5s
    limit_mib: 512
    spike_limit_mib: 128

  resource:
    attributes:
      - key: environment
        value: production
        action: upsert
      - key: team
        value: platform
        action: upsert

  filter/health:
    error_mode: ignore
    traces:
      span:
        - 'attributes["http.route"] == "/health"'
        - 'attributes["http.route"] == "/ready"'

exporters:
  otlp/deepcube:
    endpoint: otlp.deepcube.ai:443
    headers:
      api-key: ${env:DEEPCUBE_API_KEY}
    retry_on_failure:
      enabled: true
      initial_interval: 5s
      max_interval: 30s
      max_elapsed_time: 300s
    sending_queue:
      enabled: true
      num_consumers: 10
      queue_size: 5000

extensions:
  health_check:
    endpoint: 0.0.0.0:13133
  zpages:
    endpoint: 0.0.0.0:55679

service:
  extensions: [health_check, zpages]
  pipelines:
    traces:
      receivers: [otlp]
      processors: [memory_limiter, filter/health, resource, batch]
      exporters: [otlp/deepcube]
    metrics:
      receivers: [otlp]
      processors: [memory_limiter, resource, batch]
      exporters: [otlp/deepcube]
    logs:
      receivers: [otlp]
      processors: [memory_limiter, resource, batch]
      exporters: [otlp/deepcube]
```

### Configuration Reference

#### Receivers

| Receiver | Description |
|----------|-------------|
| `otlp` | Accepts OTLP over gRPC (port 4317) and HTTP (port 4318) |
| `zipkin` | Accepts Zipkin format (port 9411) |
| `jaeger` | Accepts Jaeger format (ports 14250, 14268) |
| `prometheus` | Scrapes Prometheus metrics endpoints |

#### Processors

| Processor | Description |
|-----------|-------------|
| `batch` | Batches telemetry for efficient export |
| `memory_limiter` | Prevents the Collector from running out of memory |
| `resource` | Adds, updates, or removes resource attributes |
| `filter` | Drops unwanted spans, metrics, or logs |
| `k8sattributes` | Enriches telemetry with Kubernetes metadata |
| `probabilistic_sampler` | Samples a percentage of traces |
| `tail_sampling` | Makes sampling decisions based on complete traces |

#### Exporters

| Exporter | Description |
|----------|-------------|
| `otlp` | Exports via OTLP gRPC |
| `otlphttp` | Exports via OTLP HTTP |
| `debug` | Prints telemetry to stdout (for development) |

## Docker Compose Example

Run a Collector alongside your application using Docker Compose:

```yaml
# docker-compose.yaml
version: "3.9"
services:
  otel-collector:
    image: otel/opentelemetry-collector-contrib:latest
    command: ["--config", "/etc/otel/config.yaml"]
    volumes:
      - ./otel-collector-config.yaml:/etc/otel/config.yaml:ro
    ports:
      - "4317:4317"   # OTLP gRPC
      - "4318:4318"   # OTLP HTTP
      - "13133:13133" # Health check
    environment:
      - DEEPCUBE_API_KEY=YOUR-API-KEY
    restart: unless-stopped

  my-app:
    build: .
    environment:
      - OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector:4317
      - OTEL_SERVICE_NAME=my-app
    depends_on:
      - otel-collector
```

Run with:

```bash
docker compose up -d
```

!!! note "Collector image"
    Use `otel/opentelemetry-collector-contrib` (the "contrib" distribution) for the full set of receivers, processors, and exporters. The base `otel/opentelemetry-collector` image has a smaller set of components.

## Kubernetes Deployment

For Kubernetes deployments, see the [Kubernetes Instrumentation Guide](../kubernetes/index.md) which covers:

- Deploying the Collector as a DaemonSet or sidecar
- Helm chart configuration
- Integration with the OpenTelemetry Operator

### Quick Kubernetes Deployment (without Helm)

```yaml
# collector-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: otel-collector
  namespace: otel-system
spec:
  replicas: 2
  selector:
    matchLabels:
      app: otel-collector
  template:
    metadata:
      labels:
        app: otel-collector
    spec:
      containers:
        - name: collector
          image: otel/opentelemetry-collector-contrib:latest
          args: ["--config", "/etc/otel/config.yaml"]
          ports:
            - containerPort: 4317
              name: otlp-grpc
            - containerPort: 4318
              name: otlp-http
            - containerPort: 13133
              name: health
          volumeMounts:
            - name: config
              mountPath: /etc/otel
          envFrom:
            - secretRef:
                name: deepcube-api-key
          resources:
            requests:
              memory: 256Mi
              cpu: 200m
            limits:
              memory: 512Mi
              cpu: 500m
          livenessProbe:
            httpGet:
              path: /
              port: 13133
          readinessProbe:
            httpGet:
              path: /
              port: 13133
      volumes:
        - name: config
          configMap:
            name: otel-collector-config
---
apiVersion: v1
kind: Service
metadata:
  name: otel-collector
  namespace: otel-system
spec:
  selector:
    app: otel-collector
  ports:
    - name: otlp-grpc
      port: 4317
      targetPort: 4317
    - name: otlp-http
      port: 4318
      targetPort: 4318
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-collector-config
  namespace: otel-system
data:
  config.yaml: |
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: 0.0.0.0:4317
          http:
            endpoint: 0.0.0.0:4318

    processors:
      batch:
        timeout: 5s
      memory_limiter:
        check_interval: 5s
        limit_mib: 400

    exporters:
      otlp/deepcube:
        endpoint: otlp.deepcube.ai:443
        headers:
          api-key: ${env:DEEPCUBE_API_KEY}

    extensions:
      health_check:
        endpoint: 0.0.0.0:13133

    service:
      extensions: [health_check]
      pipelines:
        traces:
          receivers: [otlp]
          processors: [memory_limiter, batch]
          exporters: [otlp/deepcube]
        metrics:
          receivers: [otlp]
          processors: [memory_limiter, batch]
          exporters: [otlp/deepcube]
        logs:
          receivers: [otlp]
          processors: [memory_limiter, batch]
          exporters: [otlp/deepcube]
```

## Verify It's Working

1. Start the Collector and confirm it is healthy:

    === "Docker"

        ```bash
        curl http://localhost:13133
        ```

    === "Kubernetes"

        ```bash
        kubectl get pods -n otel-system
        kubectl logs -l app=otel-collector -n otel-system
        ```

2. Send test telemetry using `telemetrygen` (optional):

    ```bash
    docker run --rm --network host ghcr.io/open-telemetry/opentelemetry-collector-contrib/telemetrygen:latest \
      traces --otlp-endpoint localhost:4317 --otlp-insecure --traces 5
    ```

3. Open [portal.deepcube.ai](https://portal.deepcube.ai){ target="_blank" } and select your Grid
4. Click **Enter** - you should see the test traces within a few minutes

## Troubleshooting

### Collector not starting

- Check the configuration file for YAML syntax errors. Use `otelcol validate --config=config.yaml` to validate.
- Ensure the ports (4317, 4318) are not already in use.
- Check container logs: `docker logs <container>` or `kubectl logs <pod>`.

### Data not reaching DeepCube

- Verify the API key by copying a fresh one from [portal.deepcube.ai](https://portal.deepcube.ai){ target="_blank" } under **Administration > Grids > Instrument**.
- Check that the Collector can reach `otlp.deepcube.ai:443`. Test from within the container:

    ```bash
    docker exec <container> wget -q -O- https://otlp.deepcube.ai
    ```

- Enable the `debug` exporter to see what the Collector is receiving:

    ```yaml
    exporters:
      debug:
        verbosity: detailed

    service:
      pipelines:
        traces:
          exporters: [debug, otlp/deepcube]
    ```

### High memory usage

- Tune the `memory_limiter` processor. Set `limit_mib` below the container memory limit.
- Reduce `send_batch_max_size` in the `batch` processor.
- Consider adding sampling to reduce volume.

### Applications not connecting to the Collector

- Ensure the application's `OTEL_EXPORTER_OTLP_ENDPOINT` points to the Collector's address and port.
- In Docker Compose, use the service name: `http://otel-collector:4317`.
- In Kubernetes, use the Service DNS: `http://otel-collector.otel-system.svc.cluster.local:4317`.

!!! note "Plain HTTP is acceptable for cluster-internal traffic"
    The `http://` endpoints above are for application-to-Collector traffic within the same Docker network or Kubernetes cluster. The Collector's outbound connection to `otlp.deepcube.ai` always uses TLS. For multi-tenant clusters or strict security requirements, configure TLS between applications and the Collector as well.

## Further Reading

- [OpenTelemetry Collector Documentation](https://opentelemetry.io/docs/collector/){ target="_blank" }
- [Collector Configuration Reference](https://opentelemetry.io/docs/collector/configuration/){ target="_blank" }
- [Collector Contrib Components](https://github.com/open-telemetry/opentelemetry-collector-contrib){ target="_blank" }
- [Kubernetes Instrumentation Guide](../kubernetes/index.md)
- [:octicons-arrow-left-24: Back to Instrument Overview](../index.md)
