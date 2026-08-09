"""Shared parsing for the redirect maps. ONE normalizer, imported by everything.

This module exists because there were briefly two parsers of mkdocs.yml that
normalized differently (one emitted a trailing slash, one stripped it). Two
readers of the same source that disagree is the drift class this repo has
already been bitten by twice: src/web.config went dead while looking live, and
src/redirects.conf sat dormant pointing at a server that was not there.

Consumers:
  check-redirect-parity.py   validates mkdocs.yml against src/redirects.conf
  gen-serve-config.py        emits serve.json for the Linux/Node deploy

Canonical URL form here is the trailing-slash directory form (R-DOCS-008).
Callers that need the bare form strip it themselves, at the edge, once.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def to_url(path: str) -> str:
    """Normalize a redirect_maps .md path to a trailing-slash directory URL.

    'a/b/index.md' -> '/a/b/',  'a/b.md' -> '/a/b/'.  http(s) targets pass
    through untouched so callers can filter them.
    """
    path = path.strip().strip("'\"")
    if path.startswith("http"):
        return path
    path = re.sub(r"/index\.md$", "/", path)
    path = re.sub(r"\.md$", "/", path)
    if not path.startswith("/"):
        path = "/" + path
    if not path.endswith("/"):
        path += "/"
    return path


def parse_mkdocs(text: str, include_external: bool = False) -> dict:
    """Extract redirect_maps pairs from mkdocs.yml.

    include_external matters and the two callers genuinely differ:

      parity checking  drops external targets, because the nginx map expresses
                       them differently and comparing them is noise.
      serve.json       KEEPS them. Eight of these are live social vanity links
                       (/social/x/, /link/discord/ and friends). Filtering them
                       out silently 404s all eight.
    """
    pairs = {}
    for m in re.finditer(r"^\s*'([^']+)':\s*'([^']+)'", text, re.M):
        src, dst = m.group(1), m.group(2)
        if dst.startswith("http") and not include_external:
            continue
        pairs[to_url(src)] = to_url(dst)
    return pairs


def parse_conf(text: str) -> dict:
    """Extract internal 301 pairs from the nginx redirects.conf. External targets dropped."""
    pairs = {}
    for m in re.finditer(r"^location = (\S+)\s*\{\s*return 301\s+(\S+?);?\s*\}", text, re.M):
        src, dst = m.group(1), m.group(2)
        if dst.startswith("http"):
            continue
        src = src if src.endswith("/") else src + "/"
        dst = dst if dst.endswith("/") else dst + "/"
        pairs[src] = dst
    return pairs


def load_mkdocs_pairs(include_external: bool = False) -> dict:
    return parse_mkdocs((ROOT / "mkdocs.yml").read_text(encoding="utf-8"), include_external)


def load_conf_pairs() -> dict:
    return parse_conf((ROOT / "src" / "redirects.conf").read_text(encoding="utf-8"))


def mixedcase_dirs(docs_dir: Path = None) -> list:
    """Every docs directory whose URL path contains an uppercase character.

    Longest-first. Order matters to consumers that take the first match.
    """
    docs_dir = docs_dir or (ROOT / "docs")
    out = []
    for child in sorted(docs_dir.rglob("*")):
        if not child.is_dir():
            continue
        rel = child.relative_to(docs_dir).as_posix()
        if any(c.isupper() for c in rel):
            out.append(rel)
    out.sort(key=lambda p: (-p.count("/"), -len(p), p))
    return out
