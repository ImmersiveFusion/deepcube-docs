"""Give every page its own meta description, derived from its own opening.

WHY. Until 2026-08-30 every page on this site served the same string as its
meta description, because site_description was the only description anywhere
and no page declared its own. A Slack unfurl of an installation guide and of
the release notes were indistinguishable.

WHY DERIVING IS LEGITIMATE AND NOT A SHORTCUT. The Writing Standard (canon,
2026-07-31) requires the first ~50 words of a page to stand alone as a
summary. Where a page complies, its opening paragraph IS its description; the
text already exists and simply was not reaching the <meta> tag. Sampling eight
untouched pages, seven opened with a usable summary sentence.

PRECEDENCE. An explicit `description:` in front matter always wins. This hook
only fills the gap, and skips silently when it cannot produce something
honest, so the page falls back rather than shipping a derived sentence that
misleads.

TRADEMARK. Friday's ruling (bus #2223, clarified #2270): a meta description
that names the product carries the mark ONCE, on first appearance. Not on
every appearance, because "DeepCube Web" and "DeepCube Studio" are distinct
product names and marking the family name inside them asserts a claim that
has not been filed. Written as the &trade; entity to match the &copy; already
in mkdocs.yml.
"""
import html
import re

MAX = 155

SKIP_PREFIXES = ("#", ">", "!!!", "???", "|", "---", "===", "```", ":::", "<!--", "{!", "[")
INLINE_PATTERNS = [
    (re.compile(r"!\[[^\]]*\]\([^)]*\)"), ""),            # images
    (re.compile(r"\[([^\]]+)\]\([^)]*\)(\{[^}]*\})?"), r"\1"),  # links, keep text
    (re.compile(r":[a-z0-9_-]+:"), ""),                    # :material-icon:
    (re.compile(r"`([^`]*)`"), r"\1"),                     # inline code
    (re.compile(r"\*\*([^*]+)\*\*"), r"\1"),               # bold
    (re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)"), r"\1"),      # italic
    (re.compile(r"\{[^}]*\}"), ""),                        # attr lists
    (re.compile(r"<[^>]+>"), ""),                          # raw html
]


LIST_ITEM = re.compile(r"^([-*+]|\d+[.)])\s")


def _first_paragraph(markdown):
    """First prose paragraph, or None when the page does not open with prose.

    Comment state is tracked across LINES, not per line. A multi-line HTML
    comment whose opener is skipped but whose body is not leaks authoring notes
    into the description: `Uninstallation/Windows` opens with an SP-074 note
    citing R-DOCS-005, and an earlier version of this hook would have published
    "Per R-DOCS-005, docs that quote a shipping string stay on the old" as that
    page's description. Internal rule IDs must not reach a search result.
    """
    in_fence = False
    in_comment = False
    in_admonition = False
    for raw in markdown.splitlines():
        line = raw.strip()
        if in_comment:
            if "-->" in line:
                in_comment = False
                line = line.split("-->", 1)[1].strip()
                if not line:
                    continue
            else:
                continue
        if line.startswith("```") or line.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence or not line:
            continue
        if line.startswith("<!--"):
            if "-->" not in line:
                in_comment = True
            continue
        # An admonition's opener is skipped below, but its BODY is INDENTED
        # continuation, not a new block. Taking it published the same caveat as
        # the description of three VR pages and five Studio pages, none of which
        # then described itself. The indent on the RAW line is the only signal.
        if raw[:1] in (" ", "	") and in_admonition:
            continue
        in_admonition = False
        # A list item is never a page summary. Fall back rather than guess.
        if LIST_ITEM.match(line):
            continue
        if line.startswith(("!!!", "???")):
            in_admonition = True
            continue
        if line.startswith(SKIP_PREFIXES):
            continue
        return line
    return None


# Canon assigns these to hero sections and page titles, and EXPLICITLY not to a
# meta description: "a tagline is the wrong content for it." Several pages open
# with one, so a naive derivation republishes the very thing the slot rule exists
# to remove. Stripped from the FRONT only; a tagline later in a sentence is the
# page's own prose and is left alone.
TAGLINES = (
    "Enter the World of Your Application®.",
    "Enter the World of Your Application.",
    "The next dimension of observability.",
)


def _strip_leading_tagline(text):
    changed = True
    while changed:
        changed = False
        for t in TAGLINES:
            if text.lower().startswith(t.lower()):
                text = text[len(t):].lstrip()
                changed = True
    return text


def _clean(text):
    for pattern, repl in INLINE_PATTERNS:
        text = pattern.sub(repl, text)
    text = re.sub(r"\s+", " ", text).strip()
    return _strip_leading_tagline(text)


def _rendered_len(text):
    """Length as a READER sees it. `&trade;` is 7 source characters and 1 glyph.

    Measuring the source string here would be measuring the wrong thing: the
    ~155 character budget belongs to the rendered snippet, not to the markup
    that produces it.
    """
    return len(html.unescape(text))


DANGLING = {
    "a", "an", "and", "as", "at", "but", "by", "for", "from", "in", "into", "is",
    "of", "on", "or", "the", "to", "with", "you", "your", "every", "their", "its",
    "this", "that", "these", "those", "it", "we", "our", "not", "are", "was",
}


def _truncate(text, limit=MAX):
    """Prefer whole sentences. Never end on a dangling function word.

    Cutting on length alone produced "See how every.", "as they unfold in."
    and "computer. The." A description ending mid-clause reads as broken text
    in a search result, which is worse than a shorter complete one.
    """
    if _rendered_len(text) <= limit:
        return text

    # 1. Longest run of COMPLETE sentences that fits.
    kept = ""
    for sentence in re.findall(r"[^.!?]*[.!?]", text):
        if _rendered_len(kept + sentence) > limit:
            break
        kept += sentence
    if _rendered_len(kept) >= 60:
        return kept.strip()

    # 2. Otherwise cut on a word boundary, then drop trailing function words.
    cut = text
    while cut and _rendered_len(cut) > limit - 1:
        cut = cut[:-1]
    if "&" in cut[-7:]:          # never sever an entity
        cut = cut[: cut.rindex("&")]
    words = cut.split(" ")
    if len(words) > 1:
        words = words[:-1]
    while len(words) > 6 and words[-1].strip(",;:").lower() in DANGLING:
        words.pop()
    return " ".join(words).rstrip(" ,;:") + "."


def _mark(text):
    """Mark the product ONCE, on first appearance. Entity form."""
    text = text.replace("\u2122", "")
    m = re.search(r"DeepCube(?!&trade;)", text)
    if not m:
        return text
    return text[: m.end()] + "&trade;" + text[m.end():]


def on_page_markdown(markdown, *, page, config, files):
    if page.meta.get("description"):
        return markdown
    para = _first_paragraph(markdown)
    if not para:
        return markdown
    text = _clean(para)
    # Too short to be a summary, or it is a leftover directive. Leave it alone.
    if len(text) < 40:
        return markdown
    page.meta["description"] = _truncate(_mark(text))
    return markdown
