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
import sys

# Parsing lives in redirect_map so there is exactly one reader of mkdocs.yml.
# gen-serve-config.py imports the same functions; a second parser that
# normalized differently is how these maps drift apart.
from redirect_map import load_conf_pairs, load_mkdocs_pairs


def main() -> int:
    mk = load_mkdocs_pairs()
    conf = load_conf_pairs()

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
