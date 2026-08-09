#!/usr/bin/env python3
"""Generate serve.json for the Azure App Service Linux (Node + serve) deploy.

Two rule sets, and the distinction is load-bearing (see DOC-SP-075 F12):

  redirects  301s for the legacy path moves. serve matches these
             CASE-INSENSITIVELY, which is why this stack was chosen over
             nginx: nginx `location =` is exact and would 404 every
             lowercase legacy link that IIS has been quietly serving.

  rewrites   internal resolution for wrong-case CONTENT paths. These must
             NOT be redirects. Because matching is case-insensitive, a
             redirect from /getting-started to /Getting-Started also matches
             its own destination and loops forever, on the correct-case URL
             too. Verified: curl exits 47 after 10 hops. Rewrites resolve
             internally, emit no Location, and cannot loop.

Source of truth is mkdocs.yml redirect_maps, the same map
check-redirect-parity.py validates. Never hand-edit serve.json.

Usage: python scripts/gen-serve-config.py [--out site/serve.json]
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def to_url(path: str) -> str:
    """Normalize a redirect_maps .md path to a directory URL, no trailing slash.

    serve matches paths without a trailing slash and handles both forms, so we
    emit the bare form. 'a/b/index.md' -> '/a/b', 'a/b.md' -> '/a/b'.
    """
    p = path.strip().strip("'\"")
    p = re.sub(r'/index\.md$', '', p)
    p = re.sub(r'\.md$', '', p)
    p = p.strip('/')
    return '/' + p if p else '/'


def parse_redirect_maps(mkdocs: Path):
    """Pull the redirect_maps block out of mkdocs.yml.

    Deliberately a line scanner rather than a YAML load: mkdocs.yml carries
    python object tags that a plain yaml.safe_load rejects.
    """
    pairs = []
    in_block = False
    for line in mkdocs.read_text(encoding='utf-8').splitlines():
        if re.match(r'^\s*redirect_maps:\s*$', line):
            in_block = True
            continue
        if in_block:
            if line.strip() and not line.startswith((' ', '\t')):
                break
            m = re.match(r"^\s*'([^']+)'\s*:\s*'([^']+)'\s*$", line)
            if m:
                src, dst = to_url(m.group(1)), to_url(m.group(2))
                if src != dst:
                    pairs.append((src, dst))
            elif re.match(r'^\s*[a-z_]+:\s*$', line, re.I):
                break
    return pairs


def mixedcase_dirs(docs_dir: Path):
    """EVERY docs directory whose URL path contains an uppercase character.

    Top-level alone is not enough, and this was proven rather than assumed: a
    rewrite of /dc/:rest* to /DC/:rest* turns /dc/3d/ into /DC/3d/, which still
    404s because the second segment is wrong too. The fix has to name the whole
    path, so we emit one rule per directory.

    Returned longest-first. Order is load-bearing: serve takes the first match,
    so a shallow /dc/:rest* placed before /dc/3d/:rest* would shadow it and
    reintroduce the exact bug above.
    """
    out = []
    for child in sorted(docs_dir.rglob('*')):
        if not child.is_dir():
            continue
        rel = child.relative_to(docs_dir).as_posix()
        if any(c.isupper() for c in rel):
            out.append(rel)
    out.sort(key=lambda p: (-p.count('/'), -len(p), p))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=str(ROOT / 'site' / 'serve.json'))
    args = ap.parse_args()

    redirect_pairs = parse_redirect_maps(ROOT / 'mkdocs.yml')
    dirs = mixedcase_dirs(ROOT / 'docs')

    # Destinations carry the trailing slash so the 301 lands directly on the
    # canonical directory form (R-DOCS-008) instead of needing a second hop.
    # Sources omit it: serve matches both forms from the bare source.
    redirects = [
        {'source': s, 'destination': d if d.endswith('/') else d + '/', 'type': 301}
        for s, d in redirect_pairs
    ]

    # NO trailingSlash setting. Proven: with trailingSlash enabled, serve
    # normalises the slash BEFORE consulting redirects, so /IAPM/3D returned a
    # 301 to /IAPM/3D/ and the real redirect never fired. Leaving it unset lets
    # the redirect match first, which is what we need.

    # Case tolerance. Lowercase source, canonical destination, longest path
    # first. Rewrites, never redirects: a case-insensitive redirect matches its
    # own destination and loops forever (DOC-SP-075 F12).
    # EXACT rules only, one per directory. No `:rest*` wildcards.
    #
    # Proven the hard way: a wildcard passes the remainder through UNCHANGED,
    # so /dc/3d/:rest* turned /dc/3d/guides into /DC/3D/guides, still wrong in
    # the tail. Worse, the wildcard also SHADOWS the deeper exact rule, because
    # serve takes the first match and the wildcard sits above it. Removing the
    # wildcards is what makes nested paths resolve.
    rewrites = [
        {'source': f'/{d.lower()}', 'destination': f'/{d}/index.html'}
        for d in dirs
    ]

    config = {
        'cleanUrls': False,
        'redirects': redirects,
        'rewrites': rewrites,
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(config, indent=2) + '\n', encoding='utf-8')

    print(f'wrote {out}')
    print(f'  redirects: {len(redirects)}')
    print(f'  rewrites:  {len(rewrites)}  (from {len(dirs)} mixed-case dirs)')

    dupes = {}
    for r in redirects:
        dupes.setdefault(r['source'].lower(), []).append(r['destination'])
    conflicts = {k: v for k, v in dupes.items() if len(set(v)) > 1}
    if conflicts:
        print('\nCONFLICT: same source, different targets, case-insensitively:', file=sys.stderr)
        for k, v in conflicts.items():
            print(f'  {k} -> {sorted(set(v))}', file=sys.stderr)
        return 1

    # A redirect whose destination is itself a redirect source is a chain, and
    # chains dilute exactly the signal this exercise exists to preserve.
    srcs = {r['source'].lower() for r in redirects}
    chains = [r for r in redirects if r['destination'].lower() in srcs]
    if chains:
        print(f'\nWARNING: {len(chains)} redirect(s) point at another redirect source (chain):', file=sys.stderr)
        for r in chains[:10]:
            print(f"  {r['source']} -> {r['destination']}", file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main())