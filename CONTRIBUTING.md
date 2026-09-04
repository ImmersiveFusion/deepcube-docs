# Contributing to the DeepCube Documentation Site

Welcome. This guide is how a contributor (engineer, technical writer, product
manager, or AI agent acting on behalf of any of those) lands a useful change
in this docs site without breaking production, the search index, or the
information architecture.

This file is the **single source of truth** for editorial discipline on the
docs site. It is kept byte-identical (minus product examples) with the same
file in the Knowledge Nexus repo, so a contributor who learns one site can
work on the other.

---

## What this site is

`docs.deepcube.ai`. The external, public product documentation for
DeepCube (3D, Web, Studio) and Tessa. Built with MkDocs + Material, navigated by
the `awesome-pages` plugin, and served from Azure App Service on Linux by Node
`serve`, with all routing in `serve.json`.

`docs.immersivefusion.com` is the retired host. It still resolves and forwards, so
a link to it is not broken, but it is not where the site lives and should not be
used in new content (DOC-SP-075).

The information architecture follows the **Diataxis framework**: four
quadrants (tutorials, how-to guides, reference, explanation). Every published
page lives in exactly one quadrant. See <https://diataxis.fr>.

---

## The Diataxis discipline

The four quadrants answer four different reader questions:

| Quadrant | Reader question | Page type |
|---|---|---|
| **Tutorial** | "I'm new and want to learn by doing." | Lessons. Guaranteed to work. End in a meaningful achievement. |
| **How-to guide** | "I know what I want; show me how." | Recipes. Imperative voice. Assume competence. |
| **Reference** | "I need to look something up." | Lookups. Austere. Consistent format. |
| **Explanation** | "I want to understand why." | Discursive prose. Concepts, context, alternatives. |

A page that tries to do two of these jobs at once does both badly. If you
catch yourself writing "first you do X, but here's why we built it this way,
and the full option set is...": that's three pages.

### The two discipline rules every page MUST satisfy

1. **`diataxis:` frontmatter.** Every page declares its mode in YAML
   frontmatter so reviewers and audit scripts can verify it.

   ```yaml
   ---
   title: Installing DeepCube on Windows
   diataxis: how-to
   tags: [how-to, installation, windows]
   ---
   ```

   Valid values: `tutorial`, `how-to`, `reference`, `explanation`.

2. **First-sentence rule.** Every page opens with one sentence that names its
   mode out loud. This is the reader's contract.

   - Tutorial: *"This tutorial walks you through [achievement]."*
   - How-to: *"This guide shows how to [task]."*
   - Reference: *"This page documents [thing]."*
   - Explanation: *"This page explains [concept]."*

   If you can't write that sentence cleanly, the page is doing too many jobs.

Both rules are enforced in PR review. CI may eventually grep for them; for now,
the reviewer reads the first sentence and the frontmatter.

---

## Page templates

Start every new page from one of the four templates under
[`templates/`](templates/) at the repo root:

| Template | Use for |
|---|---|
| [`diataxis-tutorial.md`](templates/diataxis-tutorial.md) | Learning a new capability hands-on |
| [`diataxis-how-to.md`](templates/diataxis-how-to.md) | Completing a known task |
| [`diataxis-reference.md`](templates/diataxis-reference.md) | Looking up commands, options, or specs |
| [`diataxis-explanation.md`](templates/diataxis-explanation.md) | Understanding a concept or design decision |

Each template carries the frontmatter, the first-sentence skeleton, the
recommended heading structure, and inline comments explaining what goes in
each section.

The templates live in `templates/` (not under `docs/`) so they aren't built
as published pages or indexed by search. They exist only for contributors
copying them as starting points for new content.

The templates themselves are byte-identical across the docs site and the
Knowledge Nexus. Product-specific examples live here in `CONTRIBUTING.md`,
not in the templates. That's how the templates stay shareable while each
site keeps domain-appropriate guidance.

> **Note for the Knowledge Nexus session:** the Nexus convention is to
> keep templates at `docs/templates/`. Either location is acceptable as
> long as the template files themselves are byte-identical. The shared
> baseline doc (SP-071 `00-shared-baseline.md`) explicitly permits this
> per-repo path divergence.

---

## Voice and tone per quadrant

Each mode reads differently. Mixing voices is the most common drift symptom.

### Tutorial voice

- Second person, present tense. "You'll create a workspace, then connect it
  to a Grid."
- Concrete, not general. "Click **New Workspace**." Not "create a workspace."
- No alternatives. Pick one path and walk the reader down it. The tutorial
  is not the place for "you could also do X."
- Explicit prerequisites at the top. List the version, the platform, the
  prior knowledge.
- Visible result after each step. "You should now see..." If the reader
  can't tell whether step 4 worked, step 5 is impossible.

### How-to voice

- Imperative. "Run the installer. Enter your license key. Restart Studio."
- Assumes the reader knows the goal and the context. No background
  explainers. If the page needs to explain *why*, link to an explanation
  page instead of inlining the explanation.
- Numbered when sequence matters. Bulleted when it doesn't.
- Branches OK if a real choice exists. "If you're on macOS, use the DMG; on
  Windows, use the MSI." Not "you could optionally..."

### Reference voice

- Austere. No narrative. The reader is here to look up a fact, not to read.
- Consistent structure across same-type pages. If `tessa-tools.md` has a
  Name / Description / Example column, then `tessa-commands.md` has Name /
  Description / Example. Predictable lookup beats personalized exposition.
- Tables over prose where possible. Code blocks over screenshots where
  possible.
- Cross-link to explanation pages for the *why*, never repeat it here.

### Explanation voice

- Discursive. Paragraphs, not bullets. Argument and counter-argument welcome.
- Why over what. The reference page already covers what; the explanation
  covers why this design over alternatives, what the tradeoffs are, where
  the concept came from.
- Multiple perspectives allowed. "One way to think about this is X. Another
  is Y. We chose X because..."
- Can be opinionated. The other three modes can't.

---

## File and folder mechanics

### Where pages live

Top-level structure (product-first, Diataxis-within):

```text
docs/
├── index.md
├── Getting-Started/        ← cross-product tutorial hub
├── DC/
│   ├── 3D/
│   │   ├── Overview/       ← explanation
│   │   ├── Tutorials/      ← tutorials
│   │   ├── Guides/         ← how-to guides (folder named "Guides" for redirect safety; nav label is "How-to guides")
│   │   └── Reference/      ← reference
│   ├── Web/                ← same four-quadrant shape
│   └── Studio/             ← same four-quadrant shape
├── Instrument/             ← language how-tos
├── API/                    ← reference
├── Setup/                  ← docs-only setup how-tos
├── Concepts/               ← cross-product explanation
└── Resources/              ← What's New, Contact
```

### `.pages` files control nav

Navigation order and section titles come from `.pages` files (one per
directory), not from a hand-edited `nav:` block in `mkdocs.yml`. Each
`.pages` file is YAML:

```yaml
title: How-to guides       # nav label only; never renames the folder on disk
arrange:                   # partial ordering; unlisted files appear after, alphabetical
  - index.md
  - first-task.md
  - second-task.md
```

`arrange:` is partial: unlisted files are still visible, just at the end. If
a page goes missing from nav after a move, the most common cause is a typo
in `.pages`.

### The casing rule (load-bearing)

**Never change the casing of an on-disk directory.** Azure / Windows
filesystems are case-insensitive; the build zips duplicate paths and fails
when a case-only variant appears (e.g. adding `dc/` redirects when `DC/`
exists on disk).

Human labels are controlled by the `title:` key in `.pages`, not by the
folder name. You can show "DeepCube" in the nav while the folder stays
`DC/3D/` and the URL stays `/DC/3D/`. Use `title:` to relabel; never `git mv`
a directory to change capitalization.

### Every move appends a redirect

`docs/mkdocs-redirects` is configured with a large existing
`redirect_maps` block in `mkdocs.yml`. **Every file or directory move
appends a redirect entry** so inbound links don't break:

```yaml
- redirects:
    redirect_maps:
      'old/path.md': 'new/path.md'
```

The plugin emits a static client-side redirect (meta-refresh + JS); it does
**not** follow chains. If `A → B` and you later move `B → C`, the
`A → B` entry now serves a 404, so you must retarget `A → C` in place.

Before every directory-moving change, grep for existing redirect targets
inside the tree you're about to move:

```bash
grep -n "DC/3D/old-folder" /m/dobri/IF/repos/if-apm-documentation-http/mkdocs.yml
```

Every hit whose value points into the moved tree is a key you must retarget
in the same PR.

### Strict build is the gate

```bash
python -m mkdocs build --strict
```

`--strict` fails on broken internal links and nav warnings. A PR is not
mergeable until `--strict` passes cleanly. If the build complains about a
file under `docs/decisions/` or another scratch-space directory, that
content shouldn't be in `docs/` at all: either delete it or move it
outside the mkdocs source tree.

---

## Licence and contribution terms

This documentation is published under the **Apache License, Version 2.0**. The
full text is in [LICENSE](LICENSE), and it covers the documentation content and
the build tooling alike.

**You do not need to sign anything to contribute.** Apache-2.0 section 5 states
that any contribution intentionally submitted for inclusion is licensed under
the same terms, unless you explicitly say otherwise:

> Unless You explicitly state otherwise, any Contribution intentionally
> submitted for inclusion in the Work by You to the Licensor shall be under the
> terms and conditions of this License, without any additional terms or
> conditions.

So opening a pull request licenses that contribution under Apache-2.0. There is
no contributor licence agreement to sign and no `Signed-off-by` trailer to add.
This matches the other public Immersive Fusion repositories, which rely on
section 5 alone.

Two things worth knowing:

- **Submit only work you have the right to license.** Section 5 sets the terms a
  contribution arrives under; it does not verify you were entitled to grant
  them. Do not paste in text you do not own or that carries incompatible terms.
- **Trademarks are not licensed.** Section 6 expressly excludes trademark
  rights. The licence lets you reuse the documentation; it does not grant any
  right in the DeepCube or Immersive Fusion marks.

## What to do before opening a PR

1. **Start from a template.** Don't author from scratch; use one of the four
   `docs/template/diataxis-*.md` files.
2. **Pick one quadrant.** If you can't, the page needs to be split.
3. **Write the first sentence.** Make it match the quadrant. If the
   sentence sounds forced, the quadrant is wrong.
4. **Add the `diataxis:` frontmatter.** No frontmatter = no merge.
5. **If you moved or renamed a file:** append a redirect in `mkdocs.yml`,
   retarget any existing redirects whose target was inside the moved tree,
   and fix every cross-link from other pages. `grep -rl 'old-path' docs/`
   catches the cross-links.
6. **`mkdocs build --strict`.** Locally, before push. Fix every warning.
7. **Spot-check.** `mkdocs serve` and click through the changed pages plus
   one redirect from an old URL to confirm it lands correctly.

---

## What to do during PR review

Reviewers check:

- [ ] `diataxis:` frontmatter present and matches the page's actual mode
- [ ] First sentence names the mode out loud
- [ ] Voice matches the quadrant (no narrative in reference; no tables in
      explanation; no "why" in how-to)
- [ ] All moves have redirects
- [ ] All chained-redirect targets retargeted in place
- [ ] `mkdocs build --strict` is green in CI (or locally)
- [ ] Cross-links updated

If a page does multiple jobs at once, ask the author to split it. That's the
single most common review note and the most important one to enforce.

---

## When in doubt

- Read <https://diataxis.fr>. Daniele Procida's writing is short and clear.
- Look at an existing page in the same quadrant and copy the shape.
- Ask. The docs are a shared asset; misclassifying a page costs everyone.

Welcome aboard.
