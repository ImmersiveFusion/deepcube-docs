---
description: "See which services sent traces at the end of your selected time range in DeepCube&trade; Web, beside the Apdex, request rate, error rate and p90 charts for that range."
---

# Snapshot


In DeepCube Web, a **snapshot** shows how your grid was doing over the range selected in the time range picker, and which services sent traces in the 5 minutes before the end of that range. It answers the question a trace or a log line raises: what else was going on at that time?

A snapshot shows you two things:

- **Four charts for the selected range:** Apdex, request rate, error rate and p90. They are the same charts shown above the **Traces** and **Logs** lists.
- **What was running:** the services that sent traces in the 5 minutes before the snapshot time.

!!! note "What the list shows and what it does not"
    The **What was running** list gives service names only. It does not show instances, a last-seen time or a service state, and it does not give figures for each service. For figures, use the four charts.

    When the list cannot be measured for a time, the snapshot shows the reason in place of the list, not an empty list. When the list was measured and no service sent traces, it says "No service sent telemetry at this time." See [When the list cannot be given](#when-the-list-cannot-be-given).

## What Snapshot is for

Use Snapshot when a trace, a log line or a chart makes you ask what else was happening at that time. It helps you:

- **Put a span or log line in context.** From a trace or a log line, **Around this span** or **Around this log** lists the services that sent traces in the 5 minutes before it, with the span's or log's own service first.
- **See the grid's overall shape for a time window.** The four charts (Apdex, request rate, error rate and p90) cover the whole range you picked.
- **Compare two periods.** Change the range in the time range picker and the page follows, so you can look at a quiet period and a busy one with the same view.
- **Share what you are looking at.** A fixed range in the address holds the same start and end for whoever opens it. See [Sharing a snapshot](#sharing-a-snapshot).

Snapshot reports what the grid received. It does not report the health, state or cause of any single service. Use the **Traces** and **Logs** lists for the detail behind a figure.

## Open a snapshot

There are three ways in.

### From the menu

Select **Snapshot** in the grid's navigation menu, directly under **Logs**. The page uses whatever range is selected in the time range picker, so you do not need to enter a time.

### From a span or a log

1. Open a trace from **Traces**, or a log line from **Logs**.
2. In the **Trace** tabs, select **Around this span** (from a trace) or **Around this log** (from a log line).

The tab shows the grid at the time the span or log line was recorded, with that span's or log's own service first. See [The Around this span and Around this log tabs](#the-around-this-span-and-around-this-log-tabs).

### See the whole grid at this time

At the top of the **Around this span** and **Around this log** tabs, select **See the whole grid at this time**. It closes the details panel and opens the **Snapshot** page with the time range picker set to the 15 minutes ending at the span's or log's time.

If the span or log line has no usable time, the link is not shown.

## What the Snapshot page shows

From top to bottom:

1. The **Snapshot** heading, and the line: "How the grid was doing over the range selected above, and which services were running at its end."
2. The four charts, for the whole selected range:

    | Chart | Shows |
    |-------|-------|
    | **Apdex** (T=500) | Apdex over the range |
    | **Request Rate** | Overall request rate |
    | **Error Rate** | Overall error rate |
    | **p90** | p90 (90th percentile) over the range |

3. **What was running**, taken at the end of the range.

### What was running

A sentence above the list states the period it covers. Usually it reads:

> Services that sent telemetry in the last 5 minutes of the selected range.

Below it, the list names each service that sent traces in those 5 minutes, sorted by service name. The list has one column, **Service**.

Read the list exactly for what it says:

- A listed service sent traces with at least one span (one step of a trace) that started in those 5 minutes. The list goes by when each span started, not by when it reached the grid.
- A service that is not listed sent no traces the grid could attribute to it in those 5 minutes. The list does not say why, and it does not say whether the service was up or down.
- The list is built from traces only. A service that sent only logs in those 5 minutes is not listed.

If the list was measured and no service sent traces, you see:

> No service sent telemetry at this time.

### Reading the list in practice

| You see | What it tells you | What it does not tell you |
|---------|-------------------|---------------------------|
| A service in the list | It sent traces in the 5 minutes covered | How many, how healthy, or which instance |
| A service you expected is not in the list | The grid has no traces it could attribute to that service in the 5 minutes covered | Why. The list does not say. A service that sent only logs, or no traces in those 5 minutes, is not listed |
| The message "No service sent telemetry at this time." | The list was measured and no service sent traces in those 5 minutes | That anything was down |
| "We cannot say what was running yet" | The list could not be measured for this time | Anything about any service |

To check an earlier period, choose a custom range that ends 5 minutes earlier and compare the two lists. Make it any length other than exactly 15, 30 or 45 minutes: the picker treats a range of exactly those lengths as **Last 15**, **30** or **45 minutes**, which ends now. Each list covers the 5 minutes before the end of its range, so the two lists do not overlap.

## How the snapshot follows the time range picker

The time range picker is the only time control on the **Snapshot** page. The page has no time control of its own.

- **The snapshot time is the end of the selected range.** The charts cover the whole range. **What was running** is taken at its end.
- **Change the range, and the page follows.** Pick a new range in the picker and the charts and the list update to match.
- **A link that names a time sets the picker.** **See the whole grid at this time** sets the picker to the 15 minutes ending at that time, so the picker always shows the range the page is using.

The **Snapshot** page does not show the time as a row of its own. Read it from the time range picker, or, when the list is taken at an earlier time, from the sentence above the list. The **Around this span** and **Around this log** tabs show the time themselves.

### When the end of the range is too recent

Data for a time keeps arriving for a few minutes afterwards. In this build, a time is treated as **complete** once it is at least 5 minutes in the past. This is an assumed delay, not a measurement of when the data has actually arrived, so very late data can still change the list after that. Before a time is treated as complete, the list for it could still change.

When you have just chosen a range such as **Last 15 minutes**, its end is the current time, so it is not treated as complete yet. Ranges such as **Today** or **This Month** end in the future. In these cases the page does not leave the list empty. It takes the list at the **newest complete time** instead, which is about 5 minutes before you opened the page or changed the range, and the sentence above the list names that time:

> Services that sent telemetry in the 5 minutes up to *time*.

The time range picker does not move, and the charts still cover the whole selected range.

The page works out the newest complete time from your computer's clock and asks for it once. If the server does not treat that time as complete either, which can happen when your computer's clock is ahead of the server's, the list is not shown and you see:

> **This time is too recent**
>
> Data for this time is still arriving, so what is shown here can still change. Do not use it for an alert or an SLO decision yet.

**What you can do:** choose a range that ends further in the past. If the alert keeps showing, check that your computer's clock is set correctly.

## The Around this span and Around this log tabs

These tabs show the snapshot for one span or one log line, with its own service first. The tab loads only when you select it.

At the top of the tab you see:

- The heading **Around this span** or **Around this log**.
- The line "What *service* and the rest of the grid were doing when this span was recorded." (or "this log was recorded").
- **Time:** the time the snapshot describes, to the second, in your own time zone with the zone named, for example `13 Oct 2026, 14:05:00 GMT+2`. Hover over it to see the same time in UTC.

Below that, a heading with the service's name and the sentence:

> Services that sent telemetry in the 5 minutes before this span.

The list shows every service that sent traces in those 5 minutes. The span's or log's own service comes first, tagged **this span** or **this log**. The rest follow, sorted by service name.

If the span's or log's own service sent no traces in those 5 minutes, the tab says so above the list:

> *service* sent no telemetry in the 5 minutes up to this span.

The tab has no time control. To see the whole grid at that time, with the charts, select **See the whole grid at this time**.

If the span or log line is so recent that its time is not treated as complete yet, the tab shows the newest complete time instead, and **Time** shows which time that is. In that case the sentences in the tab describe the time shown in **Time**, not the span or log line itself.

## Sharing a snapshot

The page address holds the selected time range, so copying the address shares the snapshot. What the other person sees depends on how the range was chosen:

| How you chose the range | What the address holds | What the other person sees |
|-------------------------|------------------------|----------------------------|
| **Last 15 minutes**, **Last 30 minutes** or **Last 45 minutes** | A length only | The last 15, 30 or 45 minutes at the time **they** open the link, not the time you were looking at |
| Any other range in the picker, such as **Today**, **Yesterday** or a custom range (unless it is exactly 15, 30 or 45 minutes long, which the picker treats as **Last 15**, **30** or **45 minutes**) | A fixed start and end | The same range you selected |
| **See the whole grid at this time** | A fixed start and end | The same 15-minute range ending at the span's or log's time |

To share a fixed time, use **See the whole grid at this time**, or a custom range that is not exactly 15, 30 or 45 minutes long, then copy the address.

Even with a fixed range, the other person can see something different from you when:

- **The end of the range was too recent when you looked.** You saw the list at the newest complete time. If they open the link later, the end of the range may be treated as complete by then, and they see the list at the end of the range itself. Check the sentence above the list: it names the period the list covers.
- **The time has passed the grid's retention.** They see that the data has been removed. See [When the list cannot be given](#when-the-list-cannot-be-given).
- **They do not have access to the grid.** They see "This time could not be loaded". See [Limits](#limits).

The **Around this span** and **Around this log** tabs have no address of their own. To share what a tab shows, select **See the whole grid at this time** and copy the address of the page it opens.

## When the list cannot be given

Sometimes the snapshot cannot say what was running. It then shows this in place of the list:

> **We cannot say what was running yet:** *reason*
>
> A service missing from here means we have no information about it, not that it was down.

The reasons you can see in this build:

| Reason shown | When it appears | What you can do |
|--------------|-----------------|-----------------|
| The data for this time has been removed under the 30-day retention. | The time is older than the data the grid still keeps. It comes with the **Data has been removed** alert (below). The period in this wording is fixed text. Your grid's trace retention setting decides. | Snapshot will not show this time. The **Traces** and **Logs** lists may still hold it, depending on your grid's retention. |
| There is too much data here to measure exactly. | More than 50,000 spans started in the 5 minutes before the snapshot time, so the list was not measured rather than measured from part of the data. | Choose a range that ends at a different time. The list is measured over the 5 minutes before the end of the range, so a quieter 5 minutes can be measured. Use the **Traces** list to look at the busy period itself. |

For a time that is too recent, the snapshot shows the **This time is too recent** alert instead of a reason. See [When the end of the range is too recent](#when-the-end-of-the-range-is-too-recent).

### Data has been removed

For a time past the grid's retention, an alert appears above the list:

> **Data has been removed**
>
> This time is past the 30-day data retention. Its data is gone and cannot be recovered.

The Snapshot page shows this message as fixed text. **The period in it is not read from your grid.** What decides whether a time counts as removed is your grid's trace retention setting, so trust that setting over the number in the message. If your grid has no trace retention set, the snapshot assumes a short history, so older times can show as removed much sooner than the number in the message suggests.

A time counts as removed once it is older than that retention, less 20 minutes. The 20 minutes are a 15-minute window that the removal check looks back over from the time, plus a 5-minute safety margin, so a snapshot stops showing data slightly before that data is deleted. The list itself still covers only the 5 minutes before the time.

## Limits

- **Time control.** The time range picker is the only time control. See [How the snapshot follows the time range picker](#how-the-snapshot-follows-the-time-range-picker).
- **Presence period.** **What was running** always covers 5 minutes and is built from traces only. See [What was running](#what-was-running).
- **Busy periods.** See [When the list cannot be given](#when-the-list-cannot-be-given).
- **Recent times.** See [When the end of the range is too recent](#when-the-end-of-the-range-is-too-recent).
- **Retention.** See [Data has been removed](#data-has-been-removed).
- **Access.** You need access to the grid. Without it, the snapshot does not load and you see "This time could not be loaded".
- **Request rate.** Snapshot requests are rate limited per caller, under the same limit as trace and log queries. If you reach the limit, you see "This time could not be loaded", and an error notification may also appear at the bottom of the screen. Wait, then select **Try again**.

## Messages you may see

| Message | What it means | What you can do |
|---------|---------------|-----------------|
| **This time could not be loaded** "The request failed, so nothing can be shown for this time. That does not mean nothing was running. Try again, or move to another time." | The request for this time failed. This includes not having access to the grid and reaching the request limit. It is not an answer about the grid. | Select **Try again**. If it keeps failing, check that you have access to the grid. |
| **No time to show** "This needs a point in time, and none was given, so nothing was looked up." | Whatever is open did not supply a time, so nothing was requested. This is not an empty grid. | On the **Snapshot** page, choose a range in the time range picker. |
| Nothing came back for this time. | The request finished without returning a snapshot. | Choose the range again, or try a different one. |
| **This time is too recent** | Even the newest complete time is not treated as complete by the server. | See [When the end of the range is too recent](#when-the-end-of-the-range-is-too-recent). |
| **Data has been removed** | The time is past the grid's retention. | See [Data has been removed](#data-has-been-removed). |
| **We cannot say what was running yet:** *reason* | The list could not be measured for this time. | See [When the list cannot be given](#when-the-list-cannot-be-given). |
| No service sent telemetry at this time. | The list was measured, and no service sent traces in those 5 minutes. | Check that traces from your services reach this grid, for example in the **Traces** list for the same range. |
| *service* sent no telemetry in the 5 minutes up to this span. (or "this log") | In a tab: the span's or log's own service sent no traces the grid could attribute to it in the 5 minutes before the span or log. The window stops just before the span's own start, so a service whose only trace is that one can appear here as silent. The rest of the list is still shown. | Read the rest of the list as usual. For the charts at that time, select **See the whole grid at this time**. |

## Related

| Topic | Link |
|-------|------|
| Everything in DeepCube Web | [Features](index.md) |
| Using DeepCube Web | [Guides](../Guides/index.md) |
| Version history | [Release Notes](../release-notes.md) |
