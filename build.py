import html
import os
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    print("ERROR: Markdown is not installed.")
    print()
    print("Run:")
    print("python -m pip install Markdown")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent

CONTENT_DIR = ROOT / "content"
HTML_DIR = ROOT / "html"
CSS_FILE = ROOT / "css" / "style.css"


LANGUAGE_NAMES = {
    "cpp": "C++",
    "c++": "C++",
    "cxx": "C++",
    "cc": "C++",
    "c": "C",
    "python": "Python",
    "py": "Python",
    "javascript": "JavaScript",
    "js": "JavaScript",
    "typescript": "TypeScript",
    "ts": "TypeScript",
    "html": "HTML",
    "css": "CSS",
    "json": "JSON",
    "bash": "Bash",
    "sh": "Shell",
    "shell": "Shell",
    "text": "Text",
    "plaintext": "Text",
}


def indent_html_except_code(html_text, indent="            "):
    """
    Indents HTML lines for clean document formatting while strictly
    preserving inner text and newlines inside <pre>...</pre> blocks.
    """
    pattern = re.compile(r"(<pre.*?>.*?</pre>)", re.DOTALL)
    parts = pattern.split(html_text)

    result = []
    for i, part in enumerate(parts):
        # Odd indices match the <pre>...</pre> blocks captured by the group
        if i % 2 == 1:
            result.append(part)
        else:
            lines = part.split("\n")
            indented_lines = [
                f"{indent}{line}" if line.strip() else line for line in lines
            ]
            result.append("\n".join(indented_lines))

    return "".join(result)


def relative_url(source, target):
    return Path(os.path.relpath(target, source.parent)).as_posix()


def parse_front_matter(text):
    if not text.startswith("---"):
        return {}, text

    lines = text.splitlines()

    if not lines or lines[0].strip() != "---":
        return {}, text

    end = None

    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            end = index
            break

    if end is None:
        return {}, text

    metadata = {}

    for line in lines[1:end]:
        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip().lower()
        value = value.strip()

        if key == "tags":
            metadata[key] = [
                item.strip() for item in value.split(",") if item.strip()
            ]
        else:
            metadata[key] = value

    body = "\n".join(lines[end + 1:])

    return metadata, body


def get_title(metadata, markdown_text, fallback):
    if metadata.get("title"):
        return metadata["title"]

    for line in markdown_text.splitlines():
        line = line.strip()
        if line.startswith("# "):
            title = line[2:].strip()
            if title:
                return title

    return fallback


def get_page_title(metadata, markdown_text, fallback):
    return "Learn - cppwiki"


def get_metadata_html(metadata):
    parts = []

    chapter = metadata.get("chapter")
    item = metadata.get("item")
    difficulty = metadata.get("difficulty")
    tags = metadata.get("tags", [])

    if chapter:
        parts.append(
            f'<span class="meta-tag">'
            f"Chapter {html.escape(str(chapter))}"
            f"</span>"
        )

    if item:
        parts.append(
            f'<span class="meta-tag">'
            f"Item {html.escape(str(item))}"
            f"</span>"
        )

    if difficulty:
        parts.append(
            f'<span class="meta-tag">'
            f"{html.escape(str(difficulty))}"
            f"</span>"
        )

    for tag in tags:
        parts.append(
            f'<span class="meta-tag">'
            f"{html.escape(str(tag))}"
            f"</span>"
        )

    if not parts:
        return ""

    return (
        '<div class="lesson-meta">\n'
        + "\n".join(f"    {part}" for part in parts)
        + "\n</div>"
    )


def wrap_code_blocks(rendered_html):
    pattern = re.compile(
        r'<pre><code(?: class="language-([^"]+)")?>(.*?)' r"</code></pre>",
        re.DOTALL,
    )

    def replace(match):
        language = match.group(1) or ""
        code = match.group(2)

        display_name = LANGUAGE_NAMES.get(
            language.lower(), language.upper() if language else "Code"
        )

        return (
            '<div class="code-block">\n'
            f'    <div class="code-block-header">'
            f"{html.escape(display_name)}"
            f"</div>\n"
            f"    <pre><code>{code}</code></pre>\n"
            "</div>"
        )

    return pattern.sub(replace, rendered_html)


def make_toc(toc_tokens):
    if not toc_tokens:
        return ""

    def render_items(items):
        output = []

        for item in items:
            name = item["name"]
            anchor = item["id"]

            output.append(
                "<li>"
                f'<a href="#{html.escape(anchor)}">'
                f"{html.escape(name)}"
                "</a>"
            )

            children = item.get("children", [])

            if children:
                output.append("<ul>")
                output.append(render_items(children))
                output.append("</ul>")

            output.append("</li>")

        return "\n".join(output)

    return (
        '<div class="toc">\n'
        "    <h2>Contents</h2>\n"
        "    <ol>\n"
        f"{render_items(toc_tokens)}\n"
        "    </ol>\n"
        "</div>"
    )


def make_header(source):
    home_url = relative_url(source, HTML_DIR / "index.html")

    return f"""
<header class="site-header">
    <div class="header-content">

        <a class="site-logo" href="{home_url}">
            cppwiki
        </a>

        <form class="search-form">

            <label class="sr-only" for="search">
                Search cppwiki
            </label>

            <div class="search-input-wrapper">

                <span class="search-icon" aria-hidden="true">
                    ⌕
                </span>

                <input
                    id="search"
                    type="search"
                    name="q"
                    placeholder="Search cppwiki"
                    autocomplete="off"
                >

            </div>

            <button type="submit">
                Search
            </button>

        </form>

    </div>
</header>
""".strip()


def is_learn_item(source):
    try:
        relative = source.relative_to(CONTENT_DIR)
    except ValueError:
        return False

    if len(relative.parts) < 3:
        return False

    return relative.parts[0].lower() == "learn" and relative.parts[
        1
    ].lower().startswith("chapter")


def build_page(source):
    raw_text = source.read_text(encoding="utf-8")

    metadata, markdown_text = parse_front_matter(raw_text)

    fallback = source.stem.replace("-", " ").replace("_", " ").title()

    page_title = get_page_title(metadata, markdown_text, fallback)

    md = markdown.Markdown(
        extensions=[
            "extra",
            "fenced_code",
            "tables",
            "toc",
            "sane_lists",
            "attr_list",
            "admonition",
        ],
        output_format="html5",
    )

    rendered = md.convert(markdown_text)
    rendered = wrap_code_blocks(rendered)

    css_url = relative_url(source, CSS_FILE)
    header = make_header(source)
    metadata_html = get_metadata_html(metadata)
    toc_html = make_toc(md.toc_tokens)

    page = []

    page.append("<!DOCTYPE html>")
    page.append('<html lang="en">')
    page.append("<head>")
    page.append('    <meta charset="UTF-8">')
    page.append(
        '    <meta name="viewport" content="width=device-width, initial-scale=1.0">'
    )
    page.append(f"    <title>{html.escape(page_title)}</title>")
    page.append(f'    <link rel="stylesheet" href="{css_url}">')
    page.append("</head>")
    page.append("")
    page.append("<body>")
    page.append("")
    page.append(header)
    page.append("")

    page.append('    <main class="main-content">')
    page.append("")

    if is_learn_item(source):
        learn_url = relative_url(source, HTML_DIR / "learn.html")

        page.append(f'        <a class="back-button" href="{learn_url}">')
        page.append("            ← Back to Learn")
        page.append("        </a>")
        page.append("")

    page.append('        <article class="lesson-page">')
    page.append("")

    if metadata_html:
        page.append(indent_html_except_code(metadata_html, indent="            "))
        page.append("")

    if toc_html:
        page.append(indent_html_except_code(toc_html, indent="            "))
        page.append("")

    page.append(indent_html_except_code(rendered, indent="            "))
    page.append("")

    page.append("        </article>")
    page.append("")
    page.append("    </main>")
    page.append("")
    page.append("</body>")
    page.append("</html>")
    page.append("")

    output = source.with_suffix(".html")
    output.parent.mkdir(parents=True, exist_ok=True)

    output.write_text("\n".join(page), encoding="utf-8")

    print(
        f"Built: {source.relative_to(ROOT)} -> {output.relative_to(ROOT)}"
    )


def main():
    if not CONTENT_DIR.exists():
        print(f"ERROR: Content directory does not exist:\n{CONTENT_DIR}")
        sys.exit(1)

    markdown_files = sorted(CONTENT_DIR.rglob("*.md"))

    if not markdown_files:
        print(f"No Markdown files found in {CONTENT_DIR}")
        sys.exit(0)

    for source in markdown_files:
        build_page(source)

    print()
    print(f"Done. Built {len(markdown_files)} page(s).")


if __name__ == "__main__":
    main()