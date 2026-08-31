#!/usr/bin/env python3
"""Verify every page's meta description is the one its source declares.

WHY THIS EXISTS. On 2026-08-29 the Getting Started description had never
rendered. Its text contains "Grid: explore", and a colon followed by a space
in an unquoted YAML scalar is a parse error, so mkdocs discarded the front
matter and silently served site_description instead. `mkdocs build --strict`
did not flag it. Neither did redirect parity or the routing tests, because
none of them look at what a page SAYS about itself.

The defect shipped, and the reason it shipped is that the only check that
would have caught it was run by hand in a session and never committed. This
file is that check, committed.

Two passes, because they fail differently:
  1. PARSE   every front-matter block. A YAML error here is silent at build
             time and the page falls back without saying so.
  2. COMPARE the rendered <meta name=description> against the source value.
             Catches the fallback actually reaching the page, whatever the
             cause.

Usage:
  python scripts/check-meta-descriptions.py            # parse pass only
  python scripts/check-meta-descriptions.py --site DIR # both passes
"""
import argparse, glob, html, io, os, re, sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

FM = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
META = re.compile(r'<meta\s+name=["\']?description["\']?\s+content="([^"]*)"', re.I)


def sources(docs_dir):
    """Yield (relpath, description or None). Raises on unparseable front matter."""
    out, errors, seen = {}, [], 0
    for p in sorted(glob.glob(os.path.join(docs_dir, "**", "*.md"), recursive=True)):
        rel = os.path.relpath(p, docs_dir).replace(os.sep, "/")
        text = io.open(p, encoding="utf-8").read()
        m = FM.match(text.lstrip("\ufeff"))
        if not m:
            continue
        seen += 1
        try:
            data = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as e:
            errors.append((rel, str(e).splitlines()[0]))
            continue
        if isinstance(data, dict) and data.get("description"):
            out[rel] = str(data["description"])
    return out, errors, seen


def rendered_path(site_dir, rel):
    if rel.endswith("index.md"):
        return os.path.join(site_dir, rel[: -len("index.md")], "index.html")
    return os.path.join(site_dir, rel[:-3], "index.html")


def normalise(s):
    """Source may use HTML entities (&trade;); rendered output decodes them."""
    return html.unescape(s).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", default="docs")
    ap.add_argument("--site", help="built site dir; enables the compare and fallback passes")
    ap.add_argument("--config", default="mkdocs.yml",
                    help="read site_description from here for the fallback pass")
    ap.add_argument("--allow-fallback", default="index.html", metavar="REL",
                    help="comma-separated rendered pages permitted to serve the site "
                         "fallback (default: the homepage, per the 2026-08-29 ruling)")
    args = ap.parse_args()

    descs, parse_errors, seen = sources(args.docs)
    failures = list(parse_errors)

    for rel, err in parse_errors:
        print("FAIL  unparseable front matter: %s\n        %s" % (rel, err))
        print("        A colon followed by a space in an unquoted YAML scalar is the usual cause.")
        print("        Quote the value.")

    print("parsed %d front-matter blocks, %d declare a description, %d unparseable" %
          (seen, len(descs), len(parse_errors)))

    if args.site:
        mismatched = 0
        for rel, want in sorted(descs.items()):
            page = rendered_path(args.site, rel)
            if not os.path.exists(page):
                print("FAIL  no rendered page for %s (looked for %s)" % (rel, page))
                failures.append((rel, "missing render"))
                continue
            m = META.search(io.open(page, encoding="utf-8").read())
            got = m.group(1) if m else ""
            if normalise(got) != normalise(want):
                mismatched += 1
                failures.append((rel, "mismatch"))
                print("FAIL  %s does not serve its own description" % rel)
                print("        source:   %s" % normalise(want)[:100])
                print("        rendered: %s" % normalise(got)[:100])
                print("        Most likely the page fell back to site_description.")
        print("compared %d rendered pages, %d mismatched" % (len(descs), mismatched))

    if args.site:
        # THE ACTUAL INVARIANT. The compare pass only checks pages that DECLARE a
        # description, so it cannot see a page that has none and silently inherits
        # the site-wide string. That is the defect that shipped: every page served
        # the same slogan and nothing noticed. Canon (2026-08-29) states it plainly:
        # a site-level fallback is a smell, not a feature. If it is showing on a
        # page, that page is missing its own description.
        fallback = None
        try:
            for line in io.open(args.config, encoding="utf-8"):
                if line.startswith("site_description:"):
                    fallback = normalise(line.split(":", 1)[1].strip())
                    break
        except OSError:
            pass
        if fallback:
            allowed = {a.strip() for a in args.allow_fallback.split(",") if a.strip()}
            inherited = []
            for root_dir, _, names in os.walk(args.site):
                for n in names:
                    if n != "index.html":
                        continue
                    page = os.path.join(root_dir, n)
                    rel = os.path.relpath(page, args.site).replace(os.sep, "/")
                    if rel in allowed:
                        continue
                    m = META.search(io.open(page, encoding="utf-8").read())
                    if m and normalise(m.group(1)) == fallback:
                        inherited.append(rel)
            for rel in sorted(inherited):
                print("FAIL  %s serves the site fallback, so it has no description of "
                      "its own" % rel)
                failures.append((rel, "inherits fallback"))
            print("checked %d rendered pages for silent fallback, %d inheriting"
                  % (sum(1 for _, _, ns in os.walk(args.site) for x in ns
                         if x == "index.html"), len(inherited)))

    if failures:
        print("\n%d problem(s). A page that does not describe itself is served to search "
              "engines and chat unfurls with whatever the fallback says." % len(failures))
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
