#!/usr/bin/env python3
"""Generate serve.json for the Azure App Service Linux (Node + serve) deploy.

Two rule sets, and the distinction is load-bearing (see DOC-SP-075):

  redirects  301s for the legacy path moves. serve matches these
             CASE-INSENSITIVELY, which is why this stack was chosen over
             nginx: nginx `location =` is exact and would 404 every lowercase
             legacy link that IIS has been quietly serving for years.

  rewrites   internal resolution for wrong-case CONTENT paths. These must NOT
             be redirects. Because matching is case-insensitive, a redirect
             from /getting-started to /Getting-Started also matches its own
             destination and loops forever, on the correct-case URL too.
             Rewrites resolve internally, emit no Location, cannot loop.

Parsing is imported from redirect_map so there is exactly one reader of
mkdocs.yml. serve.json is a BUILD OUTPUT, written into site/ and never
committed, for the same reason the site itself is not committed.

Run:    python scripts/gen-serve-config.py --out site/serve.json
Verify: python scripts/test-routing.py
"""
import argparse
import json
import sys

from redirect_map import ROOT, load_mkdocs_pairs, mixedcase_dirs


# Pinned, not floated. The startup command runs this exact build; a surprise
# major here changes routing semantics in production.
SERVE_VERSION = "14.2.4"


def build_config() -> dict:
    pairs = load_mkdocs_pairs(include_external=True)  # social vanity links must survive
    dirs = mixedcase_dirs()

    # Sources drop the trailing slash: serve matches both forms from the bare
    # source. Destinations keep it so the 301 lands directly on the canonical
    # directory form (R-DOCS-008) rather than needing a second hop.
    redirects = [
        {"source": src.rstrip("/") or "/", "destination": dst, "type": 301}
        for src, dst in sorted(pairs.items())
        if src != dst
    ]

    # EXACT rules only, one per directory, no `:rest*` wildcards. A wildcard
    # passes the remainder through UNCHANGED, so /dc/3d/:rest* turned
    # /dc/3d/guides into /DC/3D/guides, still wrong in the tail; and it also
    # SHADOWED the deeper exact rule, because serve takes the first match.
    rewrites = [
        {"source": "/" + d.lower(), "destination": f"/{d}/index.html"}
        for d in dirs
    ]

    # Security and cache headers are committed SOURCE at src/serve-headers.json,
    # following the house pattern from spatialobservability.org/dist/serve.json.
    # Only the routing half of serve.json is generated; the headers are
    # hand-owned and reviewed, and merged in here so there is still one file at
    # runtime.
    headers_path = ROOT / "src" / "serve-headers.json"
    headers = json.loads(headers_path.read_text(encoding="utf-8")).get("headers", [])

    # NO trailingSlash key, and this is a deliberate divergence from the house
    # pattern, which sets it. With it enabled serve normalises the slash BEFORE
    # consulting redirects, so /IAPM/3D returned a 301 to /IAPM/3D/ and the real
    # redirect never fired. spatialobservability.org can afford it because it has
    # no redirect map; this site has 182 of them.
    # cleanUrls MUST stay true, which is serve's default. With it false, the
    # root stops resolving index.html and serve renders a directory listing of
    # wwwroot instead of the homepage. It does not break /DC/ or any other
    # directory, only "/", which is exactly the URL no test covered until it
    # shipped. Verified both ways.
    return {
        "cleanUrls": True,
        "headers": headers,
        "redirects": redirects,
        "rewrites": rewrites,
    }


def lint(config: dict) -> int:
    """Structural checks on the generated map. Returns an exit code."""
    rc = 0
    redirects = config["redirects"]

    dupes = {}
    for r in redirects:
        dupes.setdefault(r["source"].lower(), []).append(r["destination"])
    conflicts = {k: sorted(set(v)) for k, v in dupes.items() if len(set(v)) > 1}
    if conflicts:
        print("CONFLICT: same source, different targets, case-insensitively:", file=sys.stderr)
        for k, v in conflicts.items():
            print(f"  {k} -> {v}", file=sys.stderr)
        rc = 1

    # A redirect whose destination is itself a redirect source is a chain, and
    # chains dilute exactly the signal this exercise exists to preserve.
    srcs = {r["source"].lower().rstrip("/") for r in redirects}
    chains = [r for r in redirects if r["destination"].lower().rstrip("/") in srcs]
    if chains:
        print(f"WARNING: {len(chains)} redirect(s) chain into another redirect source:", file=sys.stderr)
        for r in chains[:10]:
            print(f"  {r['source']} -> {r['destination']}", file=sys.stderr)

    return rc


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "site" / "serve.json"))
    args = ap.parse_args()

    config = build_config()

    out = __import__("pathlib").Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")

    # package.json ships beside serve.json so the deployed artifact carries its
    # own server. Emitted here rather than heredoc'd into two separate CI files,
    # which is how the pinned version drifts.
    pkg = out.parent / "package.json"
    pkg.write_text(
        json.dumps({
            "name": "deepcube-docs-site",
            "private": True,
            "dependencies": {"serve": SERVE_VERSION},
        }, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"wrote {out}")
    print(f"wrote {pkg}  (serve {SERVE_VERSION})")
    print(f"  redirects: {len(config['redirects'])}")
    print(f"  rewrites:  {len(config['rewrites'])}")
    return lint(config)


if __name__ == "__main__":
    sys.exit(main())
