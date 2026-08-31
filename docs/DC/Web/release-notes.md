---
description: Version history for DeepCube&trade; Web, newest first.
---

# DeepCube Web Release Notes

## Version History

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

