<!--
Diataxis REFERENCE template.

A reference page documents facts for lookup. The reader knows what they're
looking for and needs to find it fast. They are not here to read.

Write this template with:
- Austere prose. No narrative. No "you might want to..."
- Consistent structure across same-type pages. If sibling reference pages
  use Name / Description / Example columns, this page uses them too.
- Tables and code blocks over paragraphs.
- Cross-link to explanation pages for the *why*. Never inline the why here.
- Stable. Reference pages change when the underlying fact changes, not
  when the writing style does.

If you're writing sentences that explain why something is the way it is,
that content belongs in an explanation page. Link to it; don't inline it.

Reference: https://diataxis.fr/reference/
-->
---
title: <Replace with the thing being documented (e.g. "Tessa commands")>
diataxis: reference
tags: [reference, <topic-tag>]
---

# <Same as title>

This page documents <the thing>.

## <Group name, e.g. "Voice commands">

| <Name> | <Description> | <Default> | <Example> |
|---|---|---|---|
| `<value>` | <one-line description> | `<default>` | `<example>` |
| `<value>` | <description> | `<default>` | `<example>` |

## <Next group, e.g. "Session commands">

| <Name> | <Description> | <Default> | <Example> |
|---|---|---|---|
| `<value>` | <description> | `<default>` | `<example>` |

## <Next group, if applicable>

```
<code block for syntax, file format, or other structured fact>
```

## Notes

- <Behavioral fact a user needs to look up.>
- <Caveat or boundary condition.>
- <Version note: e.g. "Available in DeepCube Studio 0.8+">

## Related

- **For background on <concept>:** see [<explanation page>](<path>).
- **For step-by-step usage:** see [<how-to page>](<path>).
- **To learn this from scratch:** see [<tutorial page>](<path>).
