# Python Instrumentation

{!template/subscription-required.mdp!}

Instrument your Python applications with OpenTelemetry to send traces, metrics, and logs to DeepCube. This guide covers Django, Flask, FastAPI, auto-instrumentation, and manual SDK usage.

[:octicons-arrow-left-24: Back to Instrument Overview](../index.md)

## Install Packages

Install the core OpenTelemetry packages:

```bash
pip install opentelemetry-distro opentelemetry-exporter-otlp
```

Then install auto-instrumentation libraries for your framework:

=== "Django"

    ```bash
    pip install opentelemetry-instrumentation-django
    ```

=== "Flask"

    ```bash
    pip install opentelemetry-instrumentation-flask
    ```

=== "FastAPI"

    ```bash
    pip install opentelemetry-instrumentation-fastapi
    ```

=== "All Available"

    ```bash
    # Install all available auto-instrumentation packages
    opentelemetry-bootstrap -a install
    ```

## Auto-Instrumentation (Quickest Start)

The `opentelemetry-instrument` command wraps your application and automatically instruments supported libraries:

```bash
OTEL_EXPORTER_OTLP_ENDPOINT=https://otlp.deepcube.ai \
OTEL_EXPORTER_OTLP_HEADERS="api-key=YOUR-API-KEY" \
OTEL_SERVICE_NAME=my-python-app \
opentelemetry-instrument python your_app.py
```

For framework-specific entry points:

=== "Django"

    ```bash
    OTEL_EXPORTER_OTLP_ENDPOINT=https://otlp.deepcube.ai \
    OTEL_EXPORTER_OTLP_HEADERS="api-key=YOUR-API-KEY" \
    OTEL_SERVICE_NAME=my-django-app \
    opentelemetry-instrument python manage.py runserver
    ```

=== "Flask"

    ```bash
    OTEL_EXPORTER_OTLP_ENDPOINT=https://otlp.deepcube.ai \
    OTEL_EXPORTER_OTLP_HEADERS="api-key=YOUR-API-KEY" \
    OTEL_SERVICE_NAME=my-flask-app \
    opentelemetry-instrument flask run
    ```

=== "FastAPI"

    ```bash
    OTEL_EXPORTER_OTLP_ENDPOINT=https://otlp.deepcube.ai \
    OTEL_EXPORTER_OTLP_HEADERS="api-key=YOUR-API-KEY" \
    OTEL_SERVICE_NAME=my-fastapi-app \
    opentelemetry-instrument uvicorn main:app
    ```

=== "Gunicorn"

    ```bash
    OTEL_EXPORTER_OTLP_ENDPOINT=https://otlp.deepcube.ai \
    OTEL_EXPORTER_OTLP_HEADERS="api-key=YOUR-API-KEY" \
    OTEL_SERVICE_NAME=my-app \
    opentelemetry-instrument gunicorn myapp.wsgi:application
    ```

## Django Setup (Programmatic)

For more control, configure OpenTelemetry in your Django `settings.py` or a startup module:

```python
# otel_setup.py
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.instrumentation.django import DjangoInstrumentor

def configure_opentelemetry():
    resource = Resource.create({
        SERVICE_NAME: "my-django-app",
    })

    provider = TracerProvider(resource=resource)

    exporter = OTLPSpanExporter(
        endpoint="https://otlp.deepcube.ai",
        headers={"api-key": "YOUR-API-KEY"},
    )
    provider.add_span_processor(BatchSpanProcessor(exporter))

    trace.set_tracer_provider(provider)

    # Instrument Django
    DjangoInstrumentor().instrument()
```

Call `configure_opentelemetry()` early in your application startup - for example, in your `wsgi.py` or `manage.py`:

```python
# wsgi.py
import os
from django.core.wsgi import get_wsgi_application
from otel_setup import configure_opentelemetry

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

configure_opentelemetry()

application = get_wsgi_application()
```

## Flask Setup (Programmatic)

```python
from flask import Flask
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# Configure OpenTelemetry
resource = Resource.create({SERVICE_NAME: "my-flask-app"})
provider = TracerProvider(resource=resource)
exporter = OTLPSpanExporter(
    endpoint="https://otlp.deepcube.ai",
    headers={"api-key": "YOUR-API-KEY"},
)
provider.add_span_processor(BatchSpanProcessor(exporter))
trace.set_tracer_provider(provider)

# Create and instrument the Flask app
app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
```

## FastAPI Setup (Programmatic)

```python
from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

# Configure OpenTelemetry
resource = Resource.create({SERVICE_NAME: "my-fastapi-app"})
provider = TracerProvider(resource=resource)
exporter = OTLPSpanExporter(
    endpoint="https://otlp.deepcube.ai",
    headers={"api-key": "YOUR-API-KEY"},
)
provider.add_span_processor(BatchSpanProcessor(exporter))
trace.set_tracer_provider(provider)

# Create and instrument the FastAPI app
app = FastAPI()
FastAPIInstrumentor.instrument_app(app)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
```

## Manual Instrumentation

Create custom spans to trace your own business logic:

```python
from opentelemetry import trace

tracer = trace.get_tracer("myapp.orders")

def process_order(order_id: int):
    with tracer.start_as_current_span("process_order") as span:
        span.set_attribute("order.id", order_id)

        order = get_order(order_id)
        span.set_attribute("order.total", order.total)

        try:
            charge_payment(order)
            span.add_event("payment.completed")

            fulfill_order(order)

            span.set_status(trace.StatusCode.OK)
            return order

        except Exception as e:
            span.set_status(trace.StatusCode.ERROR, str(e))
            span.record_exception(e)
            raise
```

### Custom Metrics

```python
from opentelemetry import metrics

meter = metrics.get_meter("myapp.orders")

orders_counter = meter.create_counter(
    "orders.processed",
    unit="orders",
    description="Number of orders processed",
)

order_duration = meter.create_histogram(
    "orders.processing.duration",
    unit="ms",
    description="Order processing time",
)

def process_order(order):
    import time
    start = time.time()

    do_processing(order)

    duration_ms = (time.time() - start) * 1000
    orders_counter.add(1, {"order.type": order.type})
    order_duration.record(duration_ms)
```

## Environment Variable Configuration

The OpenTelemetry Python SDK reads these variables automatically:

| Variable | Value | Description |
|----------|-------|-------------|
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `https://otlp.deepcube.ai` | OTLP collector endpoint |
| `OTEL_EXPORTER_OTLP_HEADERS` | `api-key=YOUR-API-KEY` | Authentication header |
| `OTEL_SERVICE_NAME` | `your-service-name` | Service name shown in DeepCube |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | `grpc` | Protocol (grpc or http/protobuf) |
| `OTEL_TRACES_EXPORTER` | `otlp` | Trace exporter type |
| `OTEL_METRICS_EXPORTER` | `otlp` | Metrics exporter type |
| `OTEL_LOGS_EXPORTER` | `otlp` | Logs exporter type |
| `OTEL_PYTHON_LOG_LEVEL` | `info` | OpenTelemetry SDK log level |

## Verify It's Working

1. Run your instrumented application
2. Send a few HTTP requests to generate traces
3. Open [portal.deepcube.ai](https://portal.deepcube.ai){ target="_blank" } and select your Grid
4. Click **Enter** - you should see your service and traces within a few minutes

!!! tip "Quick verification with console exporter"
    Add the console exporter to see spans printed to stdout during development:

    ```bash
    pip install opentelemetry-exporter-otlp
    ```

    ```python
    from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

    provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
    ```

## Troubleshooting

### No data appearing in DeepCube

- Verify the API key by copying a fresh one from [portal.deepcube.ai](https://portal.deepcube.ai){ target="_blank" } under **Administration > Grids > Instrument**.
- Check network connectivity: `python -c "import urllib.request; urllib.request.urlopen('https://otlp.deepcube.ai')"`.
- Ensure `grpcio` is installed: `pip install grpcio`. The gRPC exporter requires it.

### Auto-instrumentation not working

- Ensure `opentelemetry-instrument` is on your PATH (it is installed by `opentelemetry-distro`).
- Run `opentelemetry-bootstrap -a requirements` to see which instrumentation packages are available for your installed libraries.
- Check that framework-specific instrumentation packages are installed (e.g., `opentelemetry-instrumentation-flask`).

### Import errors or version conflicts

- Keep all `opentelemetry-*` packages at compatible versions. Use `pip install --upgrade opentelemetry-distro opentelemetry-exporter-otlp` to get a consistent set.
- Check for conflicts: `pip check`.

### Gunicorn workers not exporting

- When using Gunicorn with multiple workers, configure OpenTelemetry in a `post_fork` hook to ensure each worker has its own provider:

    ```python
    # gunicorn.conf.py
    def post_fork(server, worker):
        from otel_setup import configure_opentelemetry
        configure_opentelemetry()
    ```

## Further Reading

- [OpenTelemetry Python Documentation](https://opentelemetry.io/docs/languages/python/){ target="_blank" }
- [Python Auto-Instrumentation](https://opentelemetry.io/docs/languages/python/automatic/){ target="_blank" }
- [:octicons-arrow-left-24: Back to Instrument Overview](../index.md)
