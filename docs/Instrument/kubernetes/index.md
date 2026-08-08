# Kubernetes Instrumentation

{!template/subscription-required.mdp!}

Deploy OpenTelemetry on Kubernetes to automatically instrument your workloads and collect cluster-wide telemetry. This guide covers the OpenTelemetry Operator, the OTel Collector as a DaemonSet or sidecar, and Helm-based configuration.

[:octicons-arrow-left-24: Back to Instrument Overview](../index.md)

## Overview

There are two main strategies for Kubernetes instrumentation:

| Strategy | Best For | How It Works |
|----------|----------|-------------|
| **OTel Operator auto-injection** | Injecting instrumentation into existing pods without code changes | The Operator injects an init container and sidecar that auto-instrument your app |
| **OTel Collector DaemonSet/Sidecar** | Centralizing telemetry collection and routing | A Collector instance receives, processes, and exports telemetry from your pods |

Most production deployments use both: the Operator for auto-instrumentation and a Collector DaemonSet for centralized export.

## OpenTelemetry Operator Auto-Instrumentation

The [OpenTelemetry Operator](https://opentelemetry.io/docs/kubernetes/operator/){ target="_blank" } can automatically inject instrumentation into your pods.

### Install the Operator

```bash
# Install cert-manager (required by the Operator)
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/latest/download/cert-manager.yaml

# Wait for cert-manager to be ready
kubectl wait --for=condition=Available deployment/cert-manager-webhook -n cert-manager --timeout=120s

# Install the OpenTelemetry Operator
kubectl apply -f https://github.com/open-telemetry/opentelemetry-operator/releases/latest/download/opentelemetry-operator.yaml
```

### Create an Instrumentation Resource

Define an `Instrumentation` custom resource that tells the Operator how to configure auto-instrumentation:

```yaml
# instrumentation.yaml
apiVersion: opentelemetry.io/v1alpha1
kind: Instrumentation
metadata:
  name: deepcube-instrumentation
  namespace: default
spec:
  exporter:
    endpoint: https://otlp.deepcube.ai
  propagators:
    - tracecontext
    - baggage
  env:
    - name: OTEL_EXPORTER_OTLP_HEADERS
      valueFrom:
        secretKeyRef:
          name: deepcube-api-key
          key: api-key
  dotnet:
    image: ghcr.io/open-telemetry/opentelemetry-operator/autoinstrumentation-dotnet:latest
  java:
    image: ghcr.io/open-telemetry/opentelemetry-operator/autoinstrumentation-java:latest
  python:
    image: ghcr.io/open-telemetry/opentelemetry-operator/autoinstrumentation-python:latest
  nodejs:
    image: ghcr.io/open-telemetry/opentelemetry-operator/autoinstrumentation-nodejs:latest
  go:
    image: ghcr.io/open-telemetry/opentelemetry-operator/autoinstrumentation-go:latest
```

!!! warning "Pin image versions in production"
    The examples above use `:latest` tags for brevity. In production, always pin to a specific version (e.g., `:1.5.0`) to ensure reproducible deployments.

### Create the API Key Secret

```bash
kubectl create secret generic deepcube-api-key \
  --from-literal=api-key="api-key=YOUR-API-KEY"
```

### Apply the Instrumentation Resource

```bash
kubectl apply -f instrumentation.yaml
```

### Annotate Your Pods

Add an annotation to your pod spec to enable auto-instrumentation for your language:

=== ".NET"

    ```yaml
    metadata:
      annotations:
        instrumentation.opentelemetry.io/inject-dotnet: "true"
    ```

=== "Java"

    ```yaml
    metadata:
      annotations:
        instrumentation.opentelemetry.io/inject-java: "true"
    ```

=== "Python"

    ```yaml
    metadata:
      annotations:
        instrumentation.opentelemetry.io/inject-python: "true"
    ```

=== "Node.js"

    ```yaml
    metadata:
      annotations:
        instrumentation.opentelemetry.io/inject-nodejs: "true"
    ```

=== "Go"

    ```yaml
    metadata:
      annotations:
        instrumentation.opentelemetry.io/inject-go: "true"
    ```

Example Deployment with auto-instrumentation:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
      annotations:
        instrumentation.opentelemetry.io/inject-java: "true"
    spec:
      containers:
        - name: my-app
          image: my-app:latest
          ports:
            - containerPort: 8080
          env:
            - name: OTEL_SERVICE_NAME
              value: my-app
```

## OTel Collector as DaemonSet

Deploy a Collector DaemonSet so every node has a local Collector instance. Your application pods export to the local Collector, which batches and forwards telemetry to DeepCube.

```yaml
# otel-collector-daemonset.yaml
apiVersion: opentelemetry.io/v1beta1
kind: OpenTelemetryCollector
metadata:
  name: deepcube-collector
  namespace: otel-system
spec:
  mode: daemonset
  env:
    - name: DEEPCUBE_API_KEY
      valueFrom:
        secretKeyRef:
          name: deepcube-api-key
          key: api-key
  config:
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
      memory_limiter:
        check_interval: 5s
        limit_mib: 512
        spike_limit_mib: 128
      k8sattributes:
        extract:
          metadata:
            - k8s.namespace.name
            - k8s.deployment.name
            - k8s.pod.name
            - k8s.node.name

    exporters:
      otlp/deepcube:
        endpoint: otlp.deepcube.ai:443
        headers:
          api-key: ${env:DEEPCUBE_API_KEY}

    service:
      pipelines:
        traces:
          receivers: [otlp]
          processors: [memory_limiter, k8sattributes, batch]
          exporters: [otlp/deepcube]
        metrics:
          receivers: [otlp]
          processors: [memory_limiter, k8sattributes, batch]
          exporters: [otlp/deepcube]
        logs:
          receivers: [otlp]
          processors: [memory_limiter, k8sattributes, batch]
          exporters: [otlp/deepcube]
```

### Point Applications to the Local Collector

Configure your application pods to export to the node-local Collector via the `status.hostIP`:

```yaml
env:
  - name: NODE_IP
    valueFrom:
      fieldRef:
        fieldPath: status.hostIP
  - name: OTEL_EXPORTER_OTLP_ENDPOINT
    value: "http://$(NODE_IP):4317"
  - name: OTEL_SERVICE_NAME
    value: my-app
```

## OTel Collector as Sidecar

For workloads that need a dedicated Collector instance per pod:

```yaml
apiVersion: opentelemetry.io/v1beta1
kind: OpenTelemetryCollector
metadata:
  name: deepcube-sidecar
spec:
  mode: sidecar
  env:
    - name: DEEPCUBE_API_KEY
      valueFrom:
        secretKeyRef:
          name: deepcube-api-key
          key: api-key
  config:
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: 0.0.0.0:4317

    processors:
      batch:
        timeout: 5s

    exporters:
      otlp/deepcube:
        endpoint: otlp.deepcube.ai:443
        headers:
          api-key: ${env:DEEPCUBE_API_KEY}

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
```

Annotate your pod to inject the sidecar:

```yaml
metadata:
  annotations:
    sidecar.opentelemetry.io/inject: "true"
```

## Helm Chart Configuration

Use the official OpenTelemetry Helm charts for a managed installation:

### Add the Helm Repository

```bash
helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts
helm repo update
```

### Install the Collector

```bash
helm install otel-collector open-telemetry/opentelemetry-collector \
  --namespace otel-system \
  --create-namespace \
  --values collector-values.yaml
```

`collector-values.yaml`:

```yaml
mode: daemonset

config:
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
    memory_limiter:
      check_interval: 5s
      limit_mib: 512

  exporters:
    otlp/deepcube:
      endpoint: otlp.deepcube.ai:443
      headers:
        api-key: YOUR-API-KEY

  service:
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

!!! warning "Protect your API key"
    For production, use a Kubernetes Secret instead of hardcoding the API key in the Helm values. Reference the secret using `envFrom` or `env` in the Collector's pod spec.

### Install the Operator via Helm

```bash
helm install otel-operator open-telemetry/opentelemetry-operator \
  --namespace otel-system \
  --create-namespace \
  --set admissionWebhooks.certManager.enabled=true
```

## ConfigMap for OTLP Endpoint

Create a shared ConfigMap that all application pods can reference:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-config
  namespace: default
data:
  OTEL_EXPORTER_OTLP_ENDPOINT: "http://deepcube-collector-opentelemetry-collector.otel-system.svc.cluster.local:4317"
  OTEL_EXPORTER_OTLP_PROTOCOL: "grpc"
```

Reference it in your Deployment:

```yaml
spec:
  containers:
    - name: my-app
      envFrom:
        - configMapRef:
            name: otel-config
      env:
        - name: OTEL_SERVICE_NAME
          value: my-app
        - name: OTEL_EXPORTER_OTLP_HEADERS
          valueFrom:
            secretKeyRef:
              name: deepcube-api-key
              key: api-key
```

## Verify It's Working

1. Deploy your instrumented workloads
2. Check that the Collector pods are running: `kubectl get pods -n otel-system`
3. Generate some traffic to your application
4. Open [portal.iapm.app](https://portal.iapm.app){ target="_blank" } and select your Grid
5. Click **Enter** - you should see your services and traces within a few minutes

!!! tip "Check Collector logs"
    ```bash
    kubectl logs -l app.kubernetes.io/name=opentelemetry-collector -n otel-system
    ```

## Troubleshooting

### Collector pods not starting

- Check pod events: `kubectl describe pod <pod-name> -n otel-system`.
- Ensure the memory limits in the Collector config do not exceed the pod resource limits.
- Verify the `deepcube-api-key` secret exists in the correct namespace.

### No data from auto-instrumented pods

- Verify the `Instrumentation` resource exists: `kubectl get instrumentation`.
- Check that the pod annotation matches the language (e.g., `inject-java`, not `inject-jvm`).
- Restart the pod after adding annotations - the injection happens at pod creation time.
- Check the init container logs: `kubectl logs <pod-name> -c opentelemetry-auto-instrumentation`.

### Applications cannot reach the Collector

- When using a DaemonSet, ensure your application uses `status.hostIP` and port `4317`.
- When using a sidecar, the Collector is at `localhost:4317`.
- Check network policies that might block traffic on port 4317.

### High resource usage on Collector

- Increase `memory_limiter` limits or add more restrictive `batch` processor settings.
- Consider switching from DaemonSet to a Deployment with HPA if the load is uneven across nodes.
- Use sampling to reduce trace volume:

    ```yaml
    processors:
      probabilistic_sampler:
        sampling_percentage: 25
    ```

## Further Reading

- [OpenTelemetry Kubernetes Documentation](https://opentelemetry.io/docs/kubernetes/){ target="_blank" }
- [OpenTelemetry Operator](https://github.com/open-telemetry/opentelemetry-operator){ target="_blank" }
- [OTel Collector Helm Chart](https://github.com/open-telemetry/opentelemetry-helm-charts){ target="_blank" }
- [Collector Guide](../collector/index.md) - Detailed Collector configuration
- [:octicons-arrow-left-24: Back to Instrument Overview](../index.md)
