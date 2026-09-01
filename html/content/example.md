---
title: Complete Markdown Test
chapter: 1
item: 999
difficulty: Advanced
tags: markdown, testing, cpp, python, html, css
---

# Complete Markdown Test

This page is a **complete test** of the Markdown features supported by the `cppwiki` builder.

It contains *italic text*, **bold text**, ***bold italic text***, `inline code`, ~~strikethrough~~, <mark>highlighted text</mark>, <kbd>Ctrl</kbd> + <kbd>C</kbd>, H<sub>2</sub>O, x<sup>2</sup>, and an <abbr title="Application Programming Interface">API</abbr>.

---

## 1. Headings

This section exists to test headings and the automatic table of contents.

### 1.1 Heading Level 3

This is a level-three heading.

#### 1.1.1 Heading Level 4

This is a level-four heading.

##### 1.1.1.1 Heading Level 5

This is a level-five heading.

###### 1.1.1.1.1 Heading Level 6

This is a level-six heading.

---

## 2. Text Formatting

Normal text.

**Bold text**

*Italic text*

***Bold italic text***

~~Strikethrough text~~

`inline code`

<mark>Highlighted text</mark>

<kbd>Ctrl</kbd> + <kbd>C</kbd>

H<sub>2</sub>O

x<sup>2</sup>

<abbr title="HyperText Markup Language">HTML</abbr>

You can combine formatting:

**Bold with `inline code`**

***Bold italic with `inline code`***

---

## 3. Links

Normal link:

[Open Example](https://example.com)

Link to Python:

[Python](https://www.python.org/)

Link to C++ reference:

[cppreference](https://en.cppreference.com/)

Automatic URL:

https://www.example.com

Email:

<hello@example.com>

Internal link:

[Jump to the admonition section](#11-admonitions)

---

## 4. Images

![Example placeholder image](https://via.placeholder.com/800x250 "Example Image")

![Another example image](https://via.placeholder.com/400x200)

---

## 5. Unordered Lists

- C++
- Python
- JavaScript
- TypeScript
- HTML
- CSS
- JSON
- Bash

Nested unordered list:

- Programming
    - C++
    - Python
    - JavaScript
- Web
    - HTML
    - CSS
- Data
    - JSON
    - Text

Deeply nested list:

- Level 1
    - Level 2
        - Level 3
            - Level 4
                - Level 5

---

## 6. Ordered Lists

1. Install Python.
2. Install Markdown.
3. Create the project.
4. Write Markdown.
5. Build HTML.
6. Open the browser.

Nested ordered list:

1. Learn Markdown.
    1. Headings
    2. Paragraphs
    3. Links
    4. Lists
2. Learn the extensions.
    1. Tables
    2. Admonitions
    3. Attributes
3. Build the website.

---

## 7. Mixed Lists

1. Programming Languages
    - C++
    - Python
    - JavaScript

2. Web Technologies
    - HTML
    - CSS

3. Data Formats
    - JSON
    - Text

---

## 8. Blockquotes

Simple quote:

> This is a blockquote.

Multiline quote:

> Markdown is simple.
>
> Markdown is readable.
>
> Markdown can also contain code.

Nested quote:

> First level.
>
> > Second level.
>
> > Another second-level paragraph.
>
> Back to the first level.

---

## 9. Code

### 9.1 Inline Code

Use `std::cout` to print text in C++.

Use `print()` in Python.

Use `console.log()` in JavaScript.

---

### 9.2 C++

```cpp
#include <iostream>
#include <string>

int main() {
    std::string name = "cppwiki";

    std::cout << "Hello, " << name << "!" << '\n';

    return 0;
}
```

### 9.3 Test

!!! note "notde"
    This is a note.

!!! warning "wardning"
    This is a warning.

!!! danger "dandger"
    This is danger.

!!! tip "tidp"
    This is a tip.