# .NET Instrumentation

{!template/subscription-required.mdp!}

Instrument your .NET applications with OpenTelemetry to send traces, metrics, and logs to DeepCube. This guide covers ASP.NET Core, console applications, and worker services.

[:octicons-arrow-left-24: Back to Instrument Overview](../index.md)

## NuGet Packages

Install the required packages for your project:

=== "ASP.NET Core"

    ```bash
    dotnet add package OpenTelemetry.Extensions.Hosting
    dotnet add package OpenTelemetry.Exporter.OpenTelemetryProtocol
    dotnet add package OpenTelemetry.Instrumentation.AspNetCore
    dotnet add package OpenTelemetry.Instrumentation.Http
    dotnet add package OpenTelemetry.Instrumentation.SqlClient    # if using SQL Server
    dotnet add package OpenTelemetry.Instrumentation.EntityFrameworkCore  # if using EF Core
    ```

=== "Console / Worker Service"

    ```bash
    dotnet add package OpenTelemetry
    dotnet add package OpenTelemetry.Exporter.OpenTelemetryProtocol
    dotnet add package OpenTelemetry.Instrumentation.Http
    dotnet add package OpenTelemetry.Extensions.Hosting  # for worker services
    ```

## ASP.NET Core Setup

Add OpenTelemetry to your `Program.cs`:

```csharp
using OpenTelemetry.Metrics;
using OpenTelemetry.Resources;
using OpenTelemetry.Trace;
using OpenTelemetry.Logs;

var builder = WebApplication.CreateBuilder(args);

// Configure OpenTelemetry
builder.Services.AddOpenTelemetry()
    .ConfigureResource(resource => resource
        .AddService(
            serviceName: builder.Configuration["Otel:ServiceName"] ?? "my-aspnet-app",
            serviceVersion: typeof(Program).Assembly.GetName().Version?.ToString() ?? "1.0.0"))
    .WithTracing(tracing => tracing
        .AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation()
        .AddSqlClientInstrumentation(options =>
        {
            options.SetDbStatementForText = true;
        })
        .AddEntityFrameworkCoreInstrumentation()
        .AddOtlpExporter(options =>
        {
            options.Endpoint = new Uri("https://otlp.deepcube.ai");
            options.Headers = "api-key=YOUR-API-KEY";
        }))
    .WithMetrics(metrics => metrics
        .AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation()
        .AddRuntimeInstrumentation()
        .AddOtlpExporter(options =>
        {
            options.Endpoint = new Uri("https://otlp.deepcube.ai");
            options.Headers = "api-key=YOUR-API-KEY";
        }));

// Configure logging export
builder.Logging.AddOpenTelemetry(logging =>
{
    logging.IncludeFormattedMessage = true;
    logging.IncludeScopes = true;
    logging.AddOtlpExporter(options =>
    {
        options.Endpoint = new Uri("https://otlp.deepcube.ai");
        options.Headers = "api-key=YOUR-API-KEY";
    });
});

var app = builder.Build();
// ... rest of your app configuration
app.Run();
```

## Console Application Setup

For console applications without the hosting infrastructure:

```csharp
using OpenTelemetry;
using OpenTelemetry.Resources;
using OpenTelemetry.Trace;

// Create a tracer provider
using var tracerProvider = Sdk.CreateTracerProviderBuilder()
    .ConfigureResource(resource => resource
        .AddService("my-console-app"))
    .AddHttpClientInstrumentation()
    .AddOtlpExporter(options =>
    {
        options.Endpoint = new Uri("https://otlp.deepcube.ai");
        options.Headers = "api-key=YOUR-API-KEY";
    })
    .Build();

// Create a meter provider
using var meterProvider = Sdk.CreateMeterProviderBuilder()
    .ConfigureResource(resource => resource
        .AddService("my-console-app"))
    .AddOtlpExporter(options =>
    {
        options.Endpoint = new Uri("https://otlp.deepcube.ai");
        options.Headers = "api-key=YOUR-API-KEY";
    })
    .Build();

// Your application logic here
var tracer = tracerProvider.GetTracer("my-console-app");
using var span = tracer.StartActiveSpan("my-operation");
span.SetAttribute("operation.type", "batch-processing");

// Do work...

span.SetStatus(Status.Ok);
```

## Worker Service Setup

For background worker services using `IHostedService`:

```csharp
using OpenTelemetry.Metrics;
using OpenTelemetry.Resources;
using OpenTelemetry.Trace;

var builder = Host.CreateApplicationBuilder(args);

builder.Services.AddOpenTelemetry()
    .ConfigureResource(resource => resource
        .AddService("my-worker-service"))
    .WithTracing(tracing => tracing
        .AddHttpClientInstrumentation()
        .AddOtlpExporter(options =>
        {
            options.Endpoint = new Uri("https://otlp.deepcube.ai");
            options.Headers = "api-key=YOUR-API-KEY";
        }))
    .WithMetrics(metrics => metrics
        .AddRuntimeInstrumentation()
        .AddOtlpExporter(options =>
        {
            options.Endpoint = new Uri("https://otlp.deepcube.ai");
            options.Headers = "api-key=YOUR-API-KEY";
        }));

builder.Services.AddHostedService<MyWorker>();

var host = builder.Build();
host.Run();
```

## Environment Variable Configuration

Instead of hardcoding values, use environment variables. The OpenTelemetry .NET SDK reads these automatically:

| Variable | Value | Description |
|----------|-------|-------------|
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `https://otlp.deepcube.ai` | OTLP collector endpoint |
| `OTEL_EXPORTER_OTLP_HEADERS` | `api-key=YOUR-API-KEY` | Authentication header |
| `OTEL_SERVICE_NAME` | `your-service-name` | Service name shown in DeepCube |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | `grpc` | Protocol (grpc or http/protobuf) |

When using environment variables, your code simplifies to:

```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(tracing => tracing
        .AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation()
        .AddOtlpExporter())  // reads from environment variables
    .WithMetrics(metrics => metrics
        .AddAspNetCoreInstrumentation()
        .AddOtlpExporter());  // reads from environment variables
```

Set the variables in your launch profile, Docker configuration, or deployment environment:

=== "launchSettings.json"

    ```json
    {
      "profiles": {
        "MyApp": {
          "environmentVariables": {
            "OTEL_EXPORTER_OTLP_ENDPOINT": "https://otlp.deepcube.ai",
            "OTEL_EXPORTER_OTLP_HEADERS": "api-key=YOUR-API-KEY",
            "OTEL_SERVICE_NAME": "my-app"
          }
        }
      }
    }
    ```

=== "Dockerfile"

    ```dockerfile
    ENV OTEL_EXPORTER_OTLP_ENDPOINT=https://otlp.deepcube.ai
    ENV OTEL_EXPORTER_OTLP_HEADERS=api-key=YOUR-API-KEY
    ENV OTEL_SERVICE_NAME=my-app
    ```

=== "appsettings.json"

    ```json
    {
      "Otel": {
        "ServiceName": "my-app",
        "Endpoint": "https://otlp.deepcube.ai",
        "ApiKey": "YOUR-API-KEY"
      }
    }
    ```

    ```csharp
    .AddOtlpExporter(options =>
    {
        options.Endpoint = new Uri(builder.Configuration["Otel:Endpoint"]!);
        options.Headers = $"api-key={builder.Configuration["Otel:ApiKey"]}";
    })
    ```

## Custom Spans and Attributes

Create custom spans to trace your own business operations:

```csharp
using System.Diagnostics;

// Define an ActivitySource (equivalent to a Tracer in OpenTelemetry terms)
private static readonly ActivitySource ActivitySource = new("MyApp.Orders");

public async Task<Order> ProcessOrderAsync(int orderId)
{
    // Start a new span
    using var activity = ActivitySource.StartActivity("ProcessOrder");

    // Add attributes for context
    activity?.SetTag("order.id", orderId);
    activity?.SetTag("order.type", "standard");

    try
    {
        var order = await _repository.GetOrderAsync(orderId);
        activity?.SetTag("order.total", order.Total);

        await _paymentService.ChargeAsync(order);

        // Add an event to mark a milestone
        activity?.AddEvent(new ActivityEvent("payment.completed"));

        await _fulfillmentService.FulfillAsync(order);

        activity?.SetStatus(ActivityStatusCode.Ok);
        return order;
    }
    catch (Exception ex)
    {
        activity?.SetStatus(ActivityStatusCode.Error, ex.Message);
        activity?.RecordException(ex);
        throw;
    }
}
```

Register your `ActivitySource` with the tracer provider:

```csharp
.WithTracing(tracing => tracing
    .AddSource("MyApp.Orders")  // register your ActivitySource
    .AddAspNetCoreInstrumentation()
    // ...
)
```

## Custom Metrics

Define and record custom metrics:

```csharp
using System.Diagnostics.Metrics;

// Define a Meter
private static readonly Meter Meter = new("MyApp.Orders");

// Define instruments
private static readonly Counter<long> OrdersProcessed =
    Meter.CreateCounter<long>("orders.processed", "orders", "Number of orders processed");

private static readonly Histogram<double> OrderProcessingDuration =
    Meter.CreateHistogram<double>("orders.processing.duration", "ms", "Order processing time");

public async Task ProcessOrderAsync(Order order)
{
    var stopwatch = Stopwatch.StartNew();

    await DoProcessingAsync(order);

    stopwatch.Stop();
    OrdersProcessed.Add(1, new KeyValuePair<string, object?>("order.type", order.Type));
    OrderProcessingDuration.Record(stopwatch.Elapsed.TotalMilliseconds);
}
```

Register your `Meter` with the meter provider:

```csharp
.WithMetrics(metrics => metrics
    .AddMeter("MyApp.Orders")  // register your Meter
    .AddAspNetCoreInstrumentation()
    // ...
)
```

## Logging Integration

OpenTelemetry integrates with `Microsoft.Extensions.Logging`. Once configured (see the ASP.NET Core setup above), your existing `ILogger` calls are exported automatically:

```csharp
public class OrderController : ControllerBase
{
    private readonly ILogger<OrderController> _logger;

    public OrderController(ILogger<OrderController> logger)
    {
        _logger = logger;
    }

    [HttpPost]
    public async Task<IActionResult> CreateOrder(CreateOrderRequest request)
    {
        // This log entry is automatically exported to DeepCube
        _logger.LogInformation("Creating order for customer {CustomerId} with {ItemCount} items",
            request.CustomerId, request.Items.Count);

        // Structured logging attributes become span attributes
        try
        {
            var order = await _orderService.CreateAsync(request);
            _logger.LogInformation("Order {OrderId} created successfully", order.Id);
            return Ok(order);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Failed to create order for customer {CustomerId}", request.CustomerId);
            return StatusCode(500);
        }
    }
}
```

## Verify It's Working

1. Run your instrumented application
2. Make a few HTTP requests to generate trace data
3. Open [portal.iapm.app](https://portal.iapm.app){ target="_blank" } and select your Grid
4. Click **Enter** - you should see your service and traces within a few minutes

!!! tip "Quick verification with console exporter"
    During development, add the console exporter to see telemetry output locally:

    ```bash
    dotnet add package OpenTelemetry.Exporter.Console
    ```

    ```csharp
    .WithTracing(tracing => tracing
        .AddConsoleExporter()  // prints spans to console
        .AddOtlpExporter(/* ... */))
    ```

## Troubleshooting

### No data appearing in DeepCube

- **Check the endpoint**: Ensure `https://otlp.deepcube.ai` is reachable from your application. Test with `curl https://otlp.deepcube.ai`.
- **Verify the API key**: Copy a fresh key from [portal.iapm.app](https://portal.iapm.app){ target="_blank" } under **Administration > Grids > Instrument**.
- **Check for package version conflicts**: Ensure all `OpenTelemetry.*` packages are the same version.

### Spans are created but not exported

- Ensure the `ActivitySource` name used in your code matches what you registered with `.AddSource("...")`.
- Check that `TracerProvider` is not disposed before your application finishes processing.

### High memory usage

- Use `BatchActivityExportProcessor` (the default with OTLP exporter) rather than `SimpleActivityExportProcessor`.
- Reduce the batch size if your application produces a very high volume of spans.

### Logs not appearing

- Confirm `AddOpenTelemetry()` is called on `builder.Logging`, not just `builder.Services`.
- Ensure `IncludeFormattedMessage` is set to `true` if you want the rendered log message.

## Further Reading

- [OpenTelemetry .NET Documentation](https://opentelemetry.io/docs/languages/net/){ target="_blank" }
- [OpenTelemetry .NET API Reference](https://github.com/open-telemetry/opentelemetry-dotnet){ target="_blank" }
- [:octicons-arrow-left-24: Back to Instrument Overview](../index.md)
