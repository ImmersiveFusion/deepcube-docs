# Understanding Your Service Topology

**Difficulty:** :material-star: Beginner | **Time:** ~15 minutes

Before you troubleshoot, you need to understand your system. This walkthrough shows you how to use DeepCube's service graph and Tessa to explore your service architecture - identifying traffic patterns, critical dependencies, and potential single points of failure.

## What You'll Learn

- How to use the service graph to visualize service dependencies
- How to read traffic patterns from visual indicators
- How to identify architectural risks with Tessa
- How to use topology exploration for capacity planning

---

## Step 1: Enter the Grid and Switch to the Service Graph

1. **Enter your grid** and orient yourself on the grid.
2. **Press `N`** to switch to the service graph.

!!! info "What you see"
    The organized rows and columns of the grid dissolve. Services begin to move - drifting, separating, and regrouping based on their actual connections. The force-directed physics simulation pulls connected services toward each other and pushes unconnected ones apart. After a few seconds, the layout stabilizes into organic clusters.

    Services that communicate frequently are now physically close. Isolated services have drifted to the outer edges. The shape of your architecture is visible at a glance - something no flat dashboard can show you.

---

## Step 2: Observe the Clusters

1. **Jump with `Space`** for a momentary higher look at the layout.
2. **Identify the natural groupings** - services that cluster together share dependencies.

!!! info "What you see"
    From above, your architecture reveals its structure. You might see patterns like:

    - **A dense cluster on the left** - your frontend services and API gateways, tightly interconnected
    - **A middle band** - business logic services (orders, payments, users) connected to both the frontend cluster and the backend
    - **A cluster on the right** - databases and caches, with many incoming connections but few outgoing ones
    - **A small island** floating apart - perhaps a monitoring or logging service with minimal dependencies

    The spatial layout encodes information that would take hours to extract from a service catalog.

---

## Step 3: Read the Traffic Patterns

1. **Look at the lines connecting services.** Pay attention to their thickness and the photons flying along them.
2. **Move closer to a busy connection** to see the traffic detail.

| Visual | Meaning |
|--------|---------|
| Thick line | High throughput - a fat pipe carries heavy traffic between those services |
| Thin line | Low throughput - occasional communication |
| Photons flying along a line | Live traffic: a request emits a photon to the target, and a response sends one back |
| Translucent (glass) line | Healthy connection |
| Translucent red line | An error is occurring on that connection |

Photons are performance-gated: they appear when the frame rate is high enough, and back off under heavy load so they do not tank performance.

!!! info "What you see"
    The busiest connections in your system are immediately obvious - thick lines with photons streaming along them. You can trace the main request paths through your architecture visually: external traffic enters through the API gateway (thick incoming lines), fans out to business services (medium lines), and converges on databases (thick lines again as multiple services query the same stores). A request that emits a photon but gets none back is a visible failure or timeout.

    Quieter connections - background jobs, health checks, async messaging - appear as thin threads with only the occasional photon.

---

## Step 4: Ask Tessa for the Dependency Map

1. **Open the chat panel** and type:
   ```
   Show me the service dependency map
   ```
2. **Review the structured output** Tessa provides.

!!! info "What you see"
    Tessa produces a structured breakdown of your topology:

    - **Total services:** 22
    - **Inbound entry points:** `api-gateway`, `webhook-receiver`
    - **Most connected service:** `user-service` (11 incoming, 3 outgoing)
    - **Database services:** `postgres-primary`, `redis-cache`, `elasticsearch`
    - **Isolated services:** `log-aggregator` (no inbound dependencies)

    This gives you the data behind what you're seeing visually. The numbers confirm what the spatial layout suggests - and they're useful for sharing with team members who aren't in the 3D environment.

---

## Step 5: Identify Single Points of Failure

1. **Look for services with many incoming connections** - these are hubs that many other services depend on.
2. **Teleport to the most connected service** and select it by clicking.

!!! info "What you see"
    In the service graph, single points of failure stand out visually. They sit at the center of a starburst of connections - many lines converging on a single node. `user-service` is a prime example: eleven other services depend on it. If it goes down, all eleven are affected.

    When you select it, the dependency lines highlight, and you can count the connections. Hover the node for its tooltip to read its current load and metrics.

---

## Step 6: Ask Tessa About Pressure

1. **Ask Tessa:**
   ```
   Which services are under the most pressure?
   ```
2. **Review the pressure analysis.**

!!! info "What you see"
    Tessa analyzes load, latency trends, and capacity utilization across your grid. She ranks the most pressured services:

    | Service | Throughput | P95 Latency | CPU | Pressure |
    |---------|-----------|-------------|-----|----------|
    | `api-gateway` | 2,400 req/s | 45ms | 72% | High |
    | `user-service` | 1,800 req/s | 62ms | 68% | High |
    | `postgres-primary` | 3,200 queries/s | 8ms | 55% | Medium |
    | `order-service` | 420 req/s | 95ms | 41% | Medium |
    | `search-service` | 180 req/s | 210ms | 38% | Low |

    The services under the most pressure are your entry points and shared dependencies - exactly the ones that would cause the widest blast radius if they failed. This is the information you need for capacity planning conversations.

!!! tip "ProTip"
    Compare the pressure ranking with the visual layout. The most pressured services typically sit at the densest intersection of connections in the service graph. If a pressured service is also a single point of failure, it deserves priority attention.

---

## Step 7: Explore Architectural Patterns

1. **Move through the different clusters**, examining the connections up close.
2. **Switch between the grid (`M`) and the service graph (`N`)** to see the same services in different arrangements.

!!! info "What you see"
    As you move through the clusters, architectural patterns become tangible:

    - **Fan-out patterns:** A single gateway dispatching to many downstream services - visible as one node with many outgoing lines spreading like a tree
    - **Fan-in patterns:** Multiple services converging on a shared database - visible as many lines funneling into one node
    - **Service meshes:** Tightly interconnected groups where every service talks to every other - visible as dense, web-like connection clusters
    - **Chains:** Sequential dependencies where A calls B calls C - visible as linear paths through the topology

    Toggling back to the grid (`M`) and then returning to the service graph (`N`) reinforces the contrast: the grid shows you all services equally, while the service graph reveals the actual communication structure.

---

## Step 8: Plan Your Next Steps

Use what you've learned for:

| Use Case | Action |
|----------|--------|
| **Architecture review** | Share the topology view with your team to validate the dependency structure |
| **Capacity planning** | Focus scaling efforts on high-pressure services with many dependents |
| **Resilience planning** | Add redundancy to single points of failure identified in the service graph |
| **Onboarding** | Walk new team members through the live topology to build system understanding |
| **Incident preparation** | Know your critical paths before an incident happens |

---

## Summary

| Step | Action | Outcome |
|------|--------|---------|
| 1 | Switched to the service graph | Saw services arrange by dependencies |
| 2 | Observed clusters from above | Identified natural service groupings |
| 3 | Read traffic line indicators | Understood throughput and health of each connection |
| 4 | Asked Tessa for dependency map | Got a structured breakdown of the topology |
| 5 | Found single points of failure | Identified hub services with many dependents |
| 6 | Asked about pressure | Got a ranked list of services by load and risk |
| 7 | Explored patterns up close | Recognized fan-out, fan-in, and chain architectures |

**Your architecture, visible and understandable in minutes instead of hours of documentation digging.**

## Related

- [Investigating a Latency Spike](latency-spike.md) - Troubleshooting a specific service
- [Root Cause Analysis with Tessa](root-cause-analysis.md) - Diagnosing cascading failures
- [Navigation & Controls](../Guides/Navigation/index.md) - Full keyboard and mouse reference
