#!/usr/bin/env python3
"""Check that the two redirect maps agree.

The site keeps redirects in two places (see src/redirects.conf header):
  - mkdocs.yml `redirect_maps`  -> the live meta-refresh fallback (HTTP 200)
  - src/redirects.conf          -> the prepared nginx real-301 layer (dormant until cutover)

They must not disagree. This script normalizes both to /source/ -> /target/ URL
pairs (internal targets only; external http(s) targets are ignored) and reports:

  CONFLICT  same source redirected to different targets in the two files  -> exit 1
  only-in-mkdocs / only-in-conf   informational set differences           -> exit 0

Run manually: python scripts/check-redirect-parity.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def to_url(path: str) -> str:
    """Normalize a redirect_maps .md path to a directory URL."""
    path = path.strip()
    if path.startswith("http"):
        return path
    path = re.sub(r"/index\.md$", "/", path)
    path = re.sub(r"\.md$", "/", path)
    if not path.startswith("/"):
        path = "/" + path
    if not path.endswith("/"):
        path += "/"
    return path


def parse_mkdocs(text: str) -> dict:
    pairs = {}
    for m in re.finditer(r"^\s*'([^']+)':\s*'([^']+)'", text, re.M):
        src, dst = m.group(1), m.group(2)
        if dst.startswith("http"):
            continue
        pairs[to_url(src)] = to_url(dst)
    return pairs


def parse_conf(text: str) -> dict:
    pairs = {}
    for m in re.finditer(r"^location = (\S+)\s*\{\s*return 301\s+(\S+?);?\s*\}", text, re.M):
        src, dst = m.group(1), m.group(2)
        if dst.startswith("http"):
            continue
        src = src if src.endswith("/") else src + "/"
        dst = dst if dst.endswith("/") else dst + "/"
        pairs[src] = dst
    return pairs


def main() -> int:
    mk = parse_mkdocs((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
    conf = parse_conf((ROOT / "src" / "redirects.conf").read_text(encoding="utf-8"))

    conflicts = [(s, mk[s], conf[s]) for s in mk.keys() & conf.keys() if mk[s] != conf[s]]
    only_mk = sorted(mk.keys() - conf.keys())
    only_conf = sorted(conf.keys() - mk.keys())

    print(f"internal redirects: mkdocs.yml={len(mk)}  redirects.conf={len(conf)}  shared={len(mk.keys() & conf.keys())}")
    if only_mk:
        print(f"\n[info] {len(only_mk)} source(s) only in mkdocs.yml:")
        for s in only_mk:
            print(f"    {s} -> {mk[s]}")
    if only_conf:
        print(f"\n[info] {len(only_conf)} source(s) only in redirects.conf:")
        for s in only_conf:
            print(f"    {s} -> {conf[s]}")
    if conflicts:
        print(f"\n[FAIL] {len(conflicts)} source(s) redirect to DIFFERENT targets:")
        for s, a, b in conflicts:
            print(f"    {s}: mkdocs={a}  conf={b}")
        return 1
    print("\n[OK] no conflicting targets between the two maps.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
