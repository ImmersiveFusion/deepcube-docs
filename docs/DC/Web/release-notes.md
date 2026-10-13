---
description: Version history for DeepCube&trade; Web, newest first.
---

# DeepCube Web Release Notes

## Version History

### 3.189.0 <small>October 13, 2026</small> { id="3.189.0" }

**Introduction:**

This release rolls up everything since 3.183.0, and the theme is seeing the rest of the grid at the moment something happened. A new Snapshot page, and a tab on every trace and log, show which services sent traces at that time, and when that cannot be known they say why instead of showing an empty list. In the API, the grid graph now keeps one node per service through restarts, which changes the shape of its nodes. The node count for a billing cycle is now rounded down.

**New Features:**

- **Snapshot**: A new **Snapshot** page, under Traces and Logs in the menu, shows how a grid was doing over the range selected in the time range picker. It has the same Apdex, request rate, error rate and p90 charts as the trace and log lists, and lists the services that sent traces in the last 5 minutes of the range. It replaces the Moment page and the Grid Summary tab of earlier builds.
- **Around This Span and Around This Log**: Trace and log details have a new tab listing every service that sent traces in the 5 minutes before the span or log line, with that span's or line's own service first and marked. **See the whole grid at this time** opens the Snapshot page on the 15 minutes ending there.
- **A Snapshot Says What It Cannot See**: If the data for a time is still arriving, the snapshot shows the newest time whose data is complete, and warns that the time is too recent only if even that is incomplete. If the services at a time cannot be determined, the snapshot gives the reason instead of an empty list, and says that a missing service means there is no information about it, not that it was down. A time whose data has aged out says the data has been removed. If loading fails, the snapshot says so and offers **Try again**.
- **Moment API**: `GET /apm/grids/{gridSecondaryId}/moment?at=` lists the services that sent traces (spans) in the 5 minutes up to the requested time, or names the reason in `state.withheld` when that could not be measured. `at` is required (a time with no offset is read as UTC), and `window` is an ISO 8601 duration (default `PT15M`, at most `PT1H`) that sets the period for the graph and figures, not the 5-minute services list; a missing `at`, an invalid `window` or an `include` other than `graph` returns `400`, and a grid you have no role on returns `404`. `include=graph` adds the grid graph for the moment's own window, in the same shape as `GET /apm/grids/{gridSecondaryId}/graph`, or `null` when the data cannot support one. `evidence.expiresAt` states when the moment's data is no longer available. The readings that change on every request are returned in the `X-Moment-Watermark` and `X-Moment-Retention-Floor` headers, not the body. Like trace and log queries, the moment and graph endpoints are rate limited and answer `429` when the limit is reached.

**Improvements:**

- **Grid Graph: One Node per Service (Breaking Change)**: In `GET /apm/grids/{gridSecondaryId}/graph`, each service node is now a whole service, with the instances that sent spans in the window listed in `instances` for display, so a restart or a rolling deploy keeps the same node instead of replacing it. Separate per-instance nodes are no longer returned, `identity.instance` is always `null`, `metrics.scope` is always `own`, and the `anchorId` and `level` fields are removed. Clients that keyed on instance nodes or read any of these fields need updating.
- **Refused Requests Count as Errors in the Graph**: A request refused with `429` now counts toward a node's error rate in the grid graph. It used to count as a success, so a service refusing most of its traffic could look healthy. Dashboards or alerts built on a node's `errorRate` may show higher values from this release.
- **Log Details Match Trace Details**: Opening a log now shows the log line itself above its trace, and the log view has the same Span View, Network Graph, Log Summary, Error Summary and Events tabs as the trace view. The Events tab used to show a "next release" placeholder.
- **The Detail Panel Leaves the List in View**: The panel that opens from a trace or log now takes about half the window instead of nearly all of it, so the list you opened it from stays beside it. On windows 1280 pixels wide or narrower it still takes most of the screen.
- **Plainer Alert Summary**: The diagnostics alert summary no longer reports "active alerts". It now says whether any service exceeded its thresholds in the window checked, and states that nothing is monitoring between checks.
- **Fewer Third-Party Scripts**: DeepCube Web no longer loads Google Analytics. The affiliate tracking script now loads only for visitors who arrived through an affiliate referral link, or who return carrying its tracking cookie, and pages now send only their origin to other sites as the referrer.

**Bug Fixes:**

- Security fixes to grid access and data isolation.
- Fixed the node count for a billing cycle being rounded to the nearest whole node. The cycle average is now rounded down instead, so an average of 6.67 nodes is billed as 6, not 7.
- Fixed editing a subscription resetting its metered node count to 1 until the next nightly usage update. An edit now leaves the items already on the subscription untouched.
- Fixed `GET /apm/grids/{gridSecondaryId}/moment` failing with `500` on every request in earlier builds.
- Fixed entering an instance returning a `routingKeyPrefix` that nothing ever published to, so a client that subscribed with it received nothing. The field is now null.
- Fixed the plan label beside the energy bar, such as "Personal subscription", running under the notification bell in the header.

**Known Issues:**

- The Moment API's figure tiles are not populated yet: every tile names a reason instead of a value. On a very busy grid, with more than 50,000 spans in the 5 minutes, the services list is also withheld, with the reason given.
- Time travel, replaying a grid over a period, remains unavailable. Snapshot shows the services at a single time.
- In some cases a new subscription is created without the plan details its grids need, and creating a grid on it is refused until the subscription is corrected.
- When creating a personal access token is refused, the API returns `403` with no machine-readable reason, or `404` for a grid or hub you cannot see. Do not retry a `403` automatically.

### 3.183.0 <small>October 1, 2026</small> { id="3.183.0" }

**Introduction:**

This release rolls up everything since 3.177.5, and the theme is being charged for what you actually did. Tessa now counts your conversation with her against your energy, not the fixed instructions sent ahead of every turn, so a visitor to a public grid is no longer stopped after one message. An invitation now grants nothing until it is accepted. Several billing fixes make each subscription pay for its own usage, and the API returns real HTTP status codes in place of server errors.

**New Features:**

- **Grid Graph Endpoint**: `GET /apm/grids/{gridSecondaryId}/graph` returns a grid's services and the connections between them as a single graph. If you lack a role on the grid, this route answers `404`, the same as for a grid that does not exist, so it never reveals which grid IDs are real.
- **Token Exchange Endpoint**: `POST /oauth2/token` follows the standard OAuth token exchange (RFC 8693): send a form-encoded body, and the `subject_token` must be the same credential you present on the request, or the call fails with `invalid_grant`. It swaps your credential for a one-hour credential that records an actor acting on your behalf, designed to identify Tessa when she acts for you. A credential issued this way cannot create a personal access token.

**Improvements:**

- **Tessa Charges for Your Message, Not the Setup**: Every Tessa request carries a large, fixed block of instructions, and of tool definitions when tools are in use, ahead of what you type. It used to be charged to you whenever the provider's short-lived cache had expired, so the same message could cost many times more on a quiet day than on a busy one. That reusable block is now credited back, so you are charged for the conversation itself: your messages, what you attach and Tessa's replies.
- **Usage Limits Agree with the Energy Bar**: Limits now count usage against whoever actually paid for it, the grid you are visiting or your own subscription, so the check that refuses a request counts usage the way the energy bar does.
- **Refusals Say Whose Allowance Ran Out**: When a request is refused, the message now names the budget that is used up: the grid's visitor allowance, or your own subscription for the current period.
- **Chat Without Tools Is Now Counted**: Tessa requests that use no tools used to record no usage. They now count toward your energy like any other request.
- **Grid Nodes Billed over the Days a Grid Reported**: A grid's node count is now averaged over the days it sent telemetry, rather than over every day of the billing cycle. A day with no telemetry, for example while an API key has expired, no longer pulls your bill down for the rest of the cycle. A grid that is switched off for part of the cycle now bills its average size while it was running, which is more than before. Averages are rounded to the nearest whole node.
- **Invitations Must Be Accepted**: Every invitation that is created is now pending and sends its link, even when the address already has an account. Access starts only when the invitee signs in and accepts, and an invitation for access the person already has is refused. The "permission granted" email that used to go out before anyone had accepted is no longer sent.
- **Clearer API Errors**: Requests that used to fail with `500` now return a status you can act on. A malformed or all-zero grid, environment or instance ID returns `404`. Chat and speech return `404` for an unknown user or a caller who is not an active participant, `429` when energy is exhausted (with a `Retry-After` header when the recharge time is known), and `503` when speech is not configured. Entering an instance while a model is briefly unavailable returns `503`. Errors use the standard RFC 9457 problem details format, except on `POST /oauth2/token`, which answers with standard OAuth error codes.
- **API Limits**: Trace and log queries now reject a range wider than 31 days, which still covers the Last 30 Days, This Month and Last Month presets, and reject a range whose start is after its end, both with `400`. Rate limits now apply to trace and log queries, diagnostics, chat, speech, energy detail, products and subscription changes, and to some endpoints that need no sign-in, which are limited per IP address. A rate-limited request returns `429`, the same status as exhausted energy; only the energy case carries `Retry-After`.
- **Secrets Are Never Cached**: The responses that carry a password, key or token now always carry `Cache-Control: no-store`, so browsers and proxies do not store them.
- **Images Without a Caption**: A chat request that sends client tools, including the streaming chat request, can now include an image with no text prompt, so you no longer need a placeholder caption. Clients generated from an earlier version of the API still require a prompt until they are regenerated.

**Bug Fixes:**

- Security fixes to grid access and data isolation.
- Fixed certain Tessa messages tying up the server for several seconds.
- Fixed a security advisory in a third-party dependency (CVE-2026-26127, denial of service).
- Fixed Tessa refusing messages after only a few turns while your budget was still unspent, because the check made before each message counted the fixed instructions that billing credits back.
- Fixed Tessa refusing every message for the rest of the day once a daily total was passed, even when the current period still had budget and the energy bar showed it.
- Fixed your personal Tessa use (home space and private grids) being charged to a public grid's visitor allowance.
- Fixed subscriptions that share one billing profile being billed the same usage figure, so a seat or node count from one subscription could be applied to the other. Each subscription is now billed its own usage.
- Fixed editing a subscription failing with "Grid quality tier was not resolved for this subscription".
- Fixed a subscription edit sent through the API without `addOns` silently adding default add-ons. Leaving `addOns` out now means no add-on change.
- Fixed inviting an email address that is shared by two accounts failing outright.
- Fixed an invitee with an email address longer than 64 characters failing their first sign-in after being invited.

**Known Issues:**

- Time travel remains unavailable while replay is being reworked.
- In some cases a new subscription is created without the plan details its grids need, and creating a grid on it is refused until the subscription is corrected.
- When creating a personal access token is refused, the API returns `403` with no machine-readable reason, or `404` for a grid or hub you cannot see. Do not retry a `403` automatically.

### 3.177.5 <small>August 30, 2026</small> { id="3.177.5" }

**Introduction:**

This release rolls up everything since 3.172.3, and the theme is charts that tell you the truth. Every chart on the Insights board was rewritten against the current telemetry, values now read in units a person can scan, and an empty panel now says which kind of empty it is. A billing fix also corrects node counts for accounts running several grids.

**Improvements:**

- **Every Insights Chart Rewritten**: All 32 charts were rebuilt against the current telemetry. The old queries did not fail, they rendered plausible but wrong numbers: latency percentiles computed over too few samples, per-route breakdowns collapsing into one unlabelled group, and an error rate that missed server errors returned cleanly. Error rate is now the share of failed responses, and rate windows are wide enough to hold enough samples to be meaningful.
- **Readable Chart Values**: Sub-second latency now reads as `450ms` rather than `0.450s`, axis units and decimal places are honoured everywhere, and the numeral that sat over every point of Request Rate is gone.
- **Absence No Longer Reads as Zero**: A missing value used to render as `0`, which is indistinguishable from genuinely measuring zero. Only a real zero prints a zero now.
- **Empty Panels Explain Themselves**: A panel with nothing in it now says whether the query failed or simply had no data, and a table chart with rows loaded no longer paints blank.

**Bug Fixes:**

- Fixed node metering counting same-named nodes across different grids as one node. Accounts running several grids seeded from the same template were under-counted; node usage now matches what the grid list has always shown.
- Fixed diagnostics time windows being read as wall-clock time rather than being converted, which could have served data from the wrong period for a request sent with a time-zone offset.

**Known Issues:**

- Time travel remains unavailable while replay is being reworked.

### Renamed to DeepCube <small>August 7, 2026</small> { id="renamed-to-deepcube" }

**Introduction:**

IAPM Web is now **DeepCube™ Web**. This is a name change only. Your account, your grids, your API keys, and your telemetry are unchanged, and no action is needed on your part.

Entries below this one keep the name they shipped under, so the record stays accurate.

### 3.172.3 <small>July 22, 2026</small> { id="3.172.3" }

**Introduction:**

This release rolls up everything since 3.169.0. Most of the work is behind the scenes (grid tier-policy redesign, secret management, health checks, and job-scheduler hardening), with a handful of visible changes around billing accuracy, onboarding, and a much faster grid list.

**Improvements:**

- **Faster Grid List**: The grid list could take 8 to 13 seconds to load; it is now indexed and loads quickly.
- **Grids Re-Tier on Plan Change**: Changing your plan now re-tiers your grids to match, regardless of who owns the grid.

**Bug Fixes:**

- Fixed onboarding so it is idempotent: interrupting or retrying quick-start signup no longer creates duplicate Stripe subscriptions, and the ZIP entry step is smoother.
- Fixed expired assistant seats being billed: seats past their valid-until date are no longer counted toward your assistant seat charge.
- Fixed the self-serve data-boundary picker so it only lists boundaries that are in rotation.

### 3.169.0 <small>June 29, 2026</small> { id="3.169.0" }

**Introduction:**

This release rolls up everything since 3.141.0. Most of the work is behind the scenes (more accurate usage metering, billing, and storage accounting), but a few changes are visible: you can now choose Tessa's voice from your account, see your own personal usage, and the Energy page shows when your AI energy recharges.

**New Features:**

- **Assistant Voice Preference**: The Account page now has a working voice picker so you can choose Tessa's voice, saved as a personal preference in your account.
- **Personal Usage View**: The Energy page now includes your own home and personal usage, not just grid usage, with your home space flagged.

**Improvements:**

- The Energy detail panel now shows a "Recharges in …" countdown when your AI energy is replenishing, so you can see when it will recover.
- More accurate usage metering across grids, including correct per-grid node counts and more precise billing.

**Bug Fixes:**

- Fixed a 403 error that prevented users from selecting their own assistant voice.
- Fixed grid node counts that always displayed as 1 regardless of how many nodes reported.
- Fixed an issue where some usage averages were silently not billed due to a precision limit.

### 3.141.0 <small>May 6, 2026</small> { id="3.141.0" }

**Introduction:**

Stage 2 of the personal subscription enablement, with smoother subscription cancellation and a build pipeline that's ready to publish updates more reliably.

**Improvements:**

- Cleaner subscription cancellation flow with extracted lifecycle handling, so cancellations and reactivations leave a consistent account state.
- Pipeline and template updates so subscription tag and publish builds stay green.

**Bug Fixes:**

- Fixed discount template bindings on the subscription confirmation page that broke after the subscription model update.

---

### 3.140.0 <small>May 5, 2026</small> { id="3.140.0" }

**Introduction:**

This release rolls out the Personal Product License model end to end. Tessa is now its own purchasable subscription on the personal plan, the Portal grows admin tools to manage seats and attestations across a tenant, and the energy bar surfaces your tier and energy source so you always know which usage pool a request is drawing from.

**New Features:**

- **Personal Product License Model**: Tessa Personal is now a first-class subscription with a published catalog, signup gating, and proper graduated tiered pricing on the energy plan.
- **Admin Seat Management**: New Portal admin pages for assigning, revoking, and attesting seats across a tenant, with role-based authorization guards.
- **Tier and Energy Source on the Energy Bar**: The Usage page energy bar now shows your current tier and which energy source a request was billed against, so personal vs grid usage is no longer ambiguous.

**Improvements:**

- Subscription catalog is published from a single source-of-truth definition, with availability gates so signup-only and inquire-only SKUs are surfaced consistently across the Portal and pricing page.
- Removed legacy bypass paths in the grid and space flows so usage is properly metered for every request.
- More accurate billing on the first day of the month, with running-cycle-average metering for grids and the Tessa assistant.
- Fixed token-window naming consistency across the SPA and SDK.
- Hardened CI so subscription pipelines stay reliable across SDK and snapshot updates.

**Bug Fixes:**

- Fixed a long-running storage meter job error that masked failures in usage rollups.
- Fixed assorted snapshot drift across the Portal admin and pricing surfaces.

---

### 3.132.0 <small>April 5, 2026</small> { id="3.132.0" }

**Introduction:**

This patch keeps Tessa's memory intact across multi-step tool conversations, so follow-up questions no longer lose the context of earlier actions.

**Bug Fixes:**

- Fixed Tessa losing file and tool context between conversation turns when using server-side tools. Follow-up questions about previously inspected data now work correctly.

---

### 3.131.0 <small>April 2, 2026</small> { id="3.131.0" }

**Introduction:**

This release gives Tessa smarter diagnostics, redesigns the energy dashboard with per-grid visibility, and adds the ability to send images to Tessa for visual analysis.

**New Features:**

- **Smarter Diagnostics**: Tessa can now fetch correlated performance data and alert summaries in a single query for faster troubleshooting.
- **Energy Dashboard Redesign**: See energy usage per grid, per tenant, and per tier with source labels and breakdown charts.
- **Vision Support**: Send screenshots and images to Tessa for visual analysis alongside your telemetry data.

**Improvements:**

- Updated pricing page to reflect current subscription features.
- Improved trace summaries with stage-level aggregation.

**Bug Fixes:**

- Fixed trace stage display for certain span types.
- Fixed energy calculations on the first of the month.

---

### 3.110.0 <small>March 17, 2026</small> { id="3.110.0" }

**Introduction:**

This release delivers faster trace and log queries through an upgraded storage backend, aligns all terminology with OpenTelemetry standards, and adds a secure gateway for AI assistant communication.

**New Features:**

- **Faster Telemetry Queries**: Upgraded storage backend for significantly faster trace and log searches with improved filtering.
- **Secure AI Gateway**: Dedicated secure channel for AI assistant communication with token-based authentication.

**Improvements:**

- Terminology updated to align with OpenTelemetry standards throughout the application.
- Health check improvements across all services.
- Security hardening for API endpoints.

**Bug Fixes:**

- Fixed occasional phantom spans appearing in trace views.
- Fixed grid template display after storage migration.

---

### 3.90.0 <small>February 25, 2026</small> { id="3.90.0" }

**Introduction:**

This release introduces the AI Assistant with real-time chat, an invitation and permission system for team collaboration, a token and energy system for usage management, and Personal Access Token support.

**New Features:**

- **AI Assistant Chat**: Integrated AI assistant with streaming chat and voice support.
- **Energy System**: Energy bar UI showing AI assistant usage with tier-aware capability levels.
- **Invitation System**: Magic-link invitation flow with role descriptions and a guest role for external collaborators.
- **Permission System**: Role-based permission management with owner authorization guards.
- **Personal Access Tokens**: PAT creation and rotation with scope validation and expiration enforcement.
- **Achievements**: Achievement badges with Coming Soon ribbons and a completed filter.
- **GitHub Login**: GitHub is now available as a login option in the Portal.
- **Welcome Email**: Automated welcome email on first login.
- **Demo Grid Selector**: Quick-access demo grid dropdown.
- **Grid Templates**: Subscription-based AI limits via grid templates.

**Improvements:**

- Guest access on public grids.
- Grid delete now uses deferred cleanup for safer removal.
- Rate limiting for API endpoints.

**Bug Fixes:**

- Fixed default role in invitation creation from "member" to "user".
- Fixed energy fallback on the `/me` endpoint.

---

### 3.82.0 <small>January 25, 2026</small> { id="3.82.0" }

**Introduction:**

This release introduces new account management features, a usage dashboard, and significant navigation improvements for a more intuitive user experience.

**New Features:**

- **Usage Dashboard**: New dashboard with sparkbox visualizations showing your telemetry usage at a glance.
- **Grid Limits UI**: View your subscription limits with interactive sparkline charts.
- **Account Page**: New dedicated account management page in the Profile section.
- **Welcome Modal**: New onboarding experience for first-time users with guided setup.
- **Portal App**: Standalone portal application with static hosting for improved performance.

**Improvements:**

- **Navigation Redesign**: New three-layout architecture for improved usability and discoverability.
- **Dark Theme Default**: Dark theme is now the default, with improved landing page styling.
- Updated Portal with IAPM branding and refined dark theme styling.
- AI usage limits now displayed based on your subscription tier.
- Improved welcome modal and empty state onboarding UX.
- Disabled buttons are now more visually obvious in dark mode.
- Improved confirmation dialog layout.

**Bug Fixes:**

- Fixed Quick Start wizard stepper checkmarks and Final checks content.
- Fixed dark mode sparkbox styling for usage dashboard.

### 3.71.1 <small>December 9, 2025</small> { id="3.71.1" }

**Introduction:**

This release delivers a major dashboard overhaul and significant improvements to trace visualization, with new ways to explore span details and service dependencies.

**New Features:**

- **Span View Tab**: Waterfall timeline visualization for detailed span analysis within traces.
- **Network Graph Tab**: Interactive service dependency visualization for trace analysis.
- **Nested Span Tags**: Collapsible tree view for exploring hierarchical span tag data.

**Improvements:**

- Major dashboard redesign with improved layout and tiles.
- Renamed Immersive APM to **IAPM** throughout the application.
- Enhanced dark/light theme support across all views.
- Improved flame graph sizing and span visibility.

**Bug Fixes:**

- Fixed sidebar styling issues in dark and light themes.
- Fixed notification dropdown layout.

### 3.60.0 <small>May 21, 2025</small> { id="3.60.0" }

**Introduction:**

This release improves the login experience, adds promo code support for billing, and includes performance improvements throughout.

**Improvements:**

- Improved landing page login flow.
- Added promo code and coupon support for billing.
- General performance improvements.

**Bug Fixes:**

- Fixed credit card expiration validation for cards expiring in the current month.

---

### 3.44.0 <small>December 28, 2024</small> { id="3.44.0" }

**Introduction:**

Infrastructure and platform improvements.

**Improvements:**

- Backend platform upgrade for improved performance and compatibility.

---

### 3.34.1 <small>September 16, 2024</small> { id="3.34.1" }

- Fixed bug: Fixes to time picker

### 3.34.0 <small>September 15, 2024</small> { id="3.34.0" }

- Re-organized products on embeddable pages.

### 3.33.0 <small>Aug 23, 2024</small> { id="3.33.0" }

- OData endpoint removal

### 3.32.0 <small>Aug 21, 2024</small> { id="3.32.0" }

- Metered billing improvements

### 3.31.0 <small>Aug 9, 2024</small> { id="3.31.0" }

- Affiliate network wire up

### 3.30.0 <small>Aug 6, 2024</small> { id="3.30.0" }

- Angular 18 upgrade

### 3.25.0 <small>July 2, 2024</small> { id="3.25.0" }

- Add the ability to show the demo IAPM grid for all accounts.

