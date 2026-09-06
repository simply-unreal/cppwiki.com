---
title: How to Make an Article
difficulty: Beginner
---

# How to Make an Article

Articles on cppwiki are written in **Markdown** and converted into HTML by
`build.py`. This keeps the source easy to read while producing pages that can
be published by the website.

## Create the Markdown file

Create a file with the `.md` extension inside `html/content`. You can organize
related articles in a subdirectory, such as `html/content/special`.

For example, this article is stored at:

```text
html/content/special/make.md
```

The file name becomes the name of the generated page. In this example,
`make.md` becomes `make.html`.

## Add front matter

Front matter goes at the top of the file between two lines containing three
hyphens. It sets information about the article:

```markdown
---
title: How to Make an Article
difficulty: Beginner
---
```

The `title` is used in the page title. If you leave out `title`, the builder uses the first level
one heading or the file name.

## Write the article

Use a level one heading for the article title and level two headings for its
main sections:

```markdown
# Article title

An introduction should explain what the reader will learn.

## First section

Explain the first idea with short paragraphs and examples.
```

Markdown supports useful formatting such as **bold text**, *italic text*,
lists, links, tables, and fenced code blocks.

For code examples, put the language after the opening backticks:

````markdown
```cpp
#include <iostream>

int main() {
    std::cout << "Hello, cppwiki!\n";
}
```
````

The language name lets the generated page label the code block correctly.

## Build the HTML page

Run `build.py` from the repository root:

```text
python build.py
```

The script finds every Markdown file in `html/content`, converts each one, and
writes the HTML file next to its source. The output for this article is:

```text
html/content/special/make.html
```

You do not need to write the HTML by hand. Run the builder again whenever you
change the Markdown source so the generated page stays up to date.

## Publish the article

The next step is to commit to the cppwiki github. Once you have commited your article i will add it the the repository.