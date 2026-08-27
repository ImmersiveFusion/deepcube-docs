#!/usr/bin/env python3
"""Routing tests for the built site: real 301s, case tolerance, no loops.

Runs the REAL artifact through the REAL server and asserts behaviour, so a
routing regression fails here instead of in Search Console six weeks later.
Every case below is one that has actually broken during development:

  - trailingSlash normalised the slash before redirects were consulted, so
    legacy 301s redirected to themselves-with-a-slash and never fired.
  - `:rest*` wildcards passed the tail through unchanged AND shadowed the
    deeper exact rules, so /dc/3d/guides resolved to /DC/3D/guides and 404'd.
  - case canonicalisation via `redirects` looped forever, including on the
    correct-case URL, because matching is case-insensitive.

Run locally:
    mkdocs build
    python scripts/gen-serve-config.py --out site/serve.json
    npm install --prefix site --omit=dev   # if not already present
    python scripts/test-routing.py

Or against an already-running server:
    python scripts/test-routing.py --base-url http://127.0.0.1:8080

Exits non-zero on the first failing expectation, and prints every result.
"""
import argparse
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"          # deploy root: config + node_modules live here
PUBLIC = SITE / "public"      # served root: the site, and nothing else

# (path, expected_status, expected_location_substring_or_None)
REDIRECT_CASES = [
    ("/IAPM/3D/", 301, "/DC/3D/"),
    ("/iapm/3d/", 301, "/DC/3D/"),          # lower case: IIS served this, Linux must too
    ("/IAPM/3d/", 301, "/DC/3D/"),          # mixed case
    ("/copilot/", 301, "/DC/3D/Overview/ai-assistant/"),
    ("/COPILOT/", 301, "/DC/3D/Overview/ai-assistant/"),
]

# Wrong-case content must resolve internally: 200, and crucially zero hops.
CONTENT_CASE_CASES = [
    "/DC/3D/",
    "/dc/3d/",
    "/Getting-Started/",
    "/getting-started/",
    "/GETTING-STARTED/",
    "/Resources/API/",
    "/resources/api/",
    "/DC/3D/Guides/",
    "/dc/3d/guides/",
    "/DC/3D/Guides/Installation/Windows/",
    "/dc/3d/guides/installation/windows/",
]

# Must terminate. These are the shapes that looped when case canonicalisation
# was expressed as a redirect instead of a rewrite.
# A directory listing also returns 200, which is how cleanUrls:false shipped
# past a suite that only asserted status codes. Check the TITLE.
#
# site_name is read from mkdocs.yml rather than pinned here. The point of these
# cases is "this is a rendered page, not a directory listing", not "the brand is
# spelled thus", and a copy of the brand in a test is one more place a rename has
# to remember to visit. It did not: renaming the site broke this suite before it
# broke anything a reader could see. Same one-reader rule the redirect maps
# follow, for the same reason.
def _site_name() -> str:
    text = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    m = re.search(r"^site_name:\s*(.+?)\s*$", text, re.MULTILINE)
    if not m:
        sys.exit("could not read site_name from mkdocs.yml")
    return m.group(1).strip().strip("'\"")


SITE_NAME = _site_name()

TITLE_CASES = [
    ("/", SITE_NAME),
    ("/DC/3D/", SITE_NAME),
    ("/dc/3d/", SITE_NAME),
]

# Build artifacts must not be downloadable from a public docs site.
MUST_NOT_SERVE = [
    "/serve.json",
    "/package.json",
    "/package-lock.json",
    "/oryx-manifest.toml",
    "/node_modules.tar.gz",
]

NO_LOOP_CASES = ["/Getting-Started/", "/getting-started/", "/DC/3D/", "/dc/3d/"]


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *_args, **_kwargs):
        return None


def fetch(url: str, follow: bool):
    opener = urllib.request.build_opener() if follow else urllib.request.build_opener(NoRedirect)
    try:
        with opener.open(url, timeout=15) as r:
            return r.status, r.headers.get("Location"), 0
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Location"), 0
    except urllib.error.URLError as e:
        return None, str(e.reason), 0


def start_server(port: int):
    entry = SITE / "node_modules" / "serve" / "build" / "main.js"
    if not entry.exists():
        print(f"[skip] {entry} missing. Run: npm install --prefix site --omit=dev", file=sys.stderr)
        return None
    proc = subprocess.Popen(
        ["node", str(entry), str(PUBLIC), "-c", str(SITE / "serve.json"), "-l", str(port)],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    for _ in range(40):
        status, _, _ = fetch(f"http://127.0.0.1:{port}/", follow=True)
        if status:
            return proc
        time.sleep(0.5)
    proc.terminate()
    raise RuntimeError("serve did not come up")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", default=None, help="test an already-running server")
    ap.add_argument("--port", type=int, default=8099)
    args = ap.parse_args()

    if not (SITE / "serve.json").exists():
        print("[FAIL] site/serve.json missing. Run gen-serve-config.py first.", file=sys.stderr)
        return 1

    cfg = json.loads((SITE / "serve.json").read_text(encoding="utf-8"))
    if "trailingSlash" in cfg:
        print("[FAIL] serve.json sets trailingSlash; it fires before redirects and breaks them.", file=sys.stderr)
        return 1
    bad = [r for r in cfg.get("rewrites", []) if ":rest" in r.get("source", "")]
    if bad:
        print(f"[FAIL] {len(bad)} rewrite(s) use :rest* wildcards; they shadow exact rules.", file=sys.stderr)
        return 1

    proc = None
    base = args.base_url
    if not base:
        proc = start_server(args.port)
        if proc is None:
            return 1
        base = f"http://127.0.0.1:{args.port}"

    failures = 0
    try:
        print(f"redirects: {len(cfg['redirects'])}  rewrites: {len(cfg['rewrites'])}\n")

        print("legacy redirects (real 301, correct target, case-insensitive)")
        for path, want_status, want_loc in REDIRECT_CASES:
            status, loc, _ = fetch(base + path, follow=False)
            ok = status == want_status and loc and want_loc in loc
            print(f"  {'ok  ' if ok else 'FAIL'} {path:<38} {status} -> {loc}")
            failures += 0 if ok else 1

        print("\nwrong-case content resolves internally (200, no redirect)")
        for path in CONTENT_CASE_CASES:
            status, loc, _ = fetch(base + path, follow=False)
            ok = status == 200 and not loc
            print(f"  {'ok  ' if ok else 'FAIL'} {path:<38} {status}{' -> ' + loc if loc else ''}")
            failures += 0 if ok else 1

        print("\npages are pages, not directory listings")
        for path, want in TITLE_CASES:
            try:
                with urllib.request.urlopen(base + path, timeout=15) as r:
                    body = r.read(4000).decode("utf-8", "replace")
                m = re.search(r"<title>([^<]*)", body)
                title = m.group(1) if m else "<no title>"
            except Exception as e:
                title = f"<error {e}>"
            ok = want in title and "Files within" not in title
            print(f"  {'ok  ' if ok else 'FAIL'} {path:<38} {title}")
            failures += 0 if ok else 1

        print("\nbuild artifacts are not publicly served")
        for path in MUST_NOT_SERVE:
            status, _, _ = fetch(base + path, follow=False)
            ok = status in (403, 404)
            print(f"  {'ok  ' if ok else 'FAIL'} {path:<38} {status}")
            failures += 0 if ok else 1

        print("\nno redirect loops")
        for path in NO_LOOP_CASES:
            status, _, _ = fetch(base + path, follow=True)
            ok = status == 200
            print(f"  {'ok  ' if ok else 'FAIL'} {path:<38} {status}")
            failures += 0 if ok else 1
    finally:
        if proc:
            proc.terminate()

    print()
    if failures:
        print(f"[FAIL] {failures} expectation(s) failed.")
        return 1
    print("[OK] routing behaves.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
