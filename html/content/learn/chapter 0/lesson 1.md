---
title: Introduction to these tutorials
difficulty: Beginner
---

# Introduction to these tutorials

Welcome to **cppwiki**!

These tutorials are designed to teach you programming step by step, starting from the basics and gradually building your understanding of **C++**. You do not need to be an expert programmer to begin. The tutorials are written for beginners and are designed to be followed in order.

The goal is not just to show you how to write code, but to help you understand **why the code works**, how the different parts fit together, and how to use what you learn in your own programs.

## What to expect

These tutorials are organized into **chapters and lessons**. Each lesson introduces a specific concept and builds on ideas introduced earlier.

As you progress, you will encounter:

- Explanations of programming concepts in simple language
- C++ code examples
- Notes and tips for important information
- Warnings about common mistakes
- Examples showing how concepts work in real programs
- Questions and exercises to help reinforce what you learned
- Links to related lessons and useful references

You should expect some concepts to become more difficult as you progress. That is normal. Programming is a skill that becomes easier through practice, so do not worry if you need to reread a lesson or experiment with the examples.

## Learn by understanding

These tutorials are not meant to be code that you copy and paste.

Whenever possible, a lesson will explain:

**What** something does.

**How** it works.

**Why** you would use it.

For example, instead of showing you:

```cpp
std::cout << "Hello, world!";
```

the tutorial can explain that `std::cout` is used to send output to the console, what the `<<` operator is doing in this context, and why the statement ends with a semicolon.

Understanding these details will help you write programs on your own instead of relying on memorized examples.

## Code examples

Throughout the Learn section, you will see code displayed in formatted code blocks.

For example:

```cpp
#include <iostream>

int main()
{
    std::cout << "Hello, cppwiki!\n";
    return 0;
}
```

When you see an example like this, take some time to read it. You do not need to understand every line immediately. The tutorial will explain unfamiliar parts as they become relevant.

You may also see **inline code** such as `int`, `std::cout`, or `main()` when a specific part of the code is being discussed.

## Notes, tips, warnings, and other callouts

Some lessons use special callouts to make important information easier to notice.

For example:

!!! note "Note"

    Notes contain useful information or additional details about the current topic.

!!! tip "Tip"

    Tips provide helpful advice that can make learning or writing code easier.

!!! warning "Warning"

    Warnings point out common mistakes, confusing behavior, or things you should be careful about.

!!! danger "Important"

    Important warnings highlight situations where something can go seriously wrong, such as introducing a bug or misunderstanding how a feature works.

These callouts are there to make important information stand out without interrupting the main explanation.

## Following the lessons

For the best learning experience, it is recommended that you work through the lessons in order.

Earlier lessons introduce concepts that later lessons will expect you to understand. Skipping too much material can make later topics unnecessarily difficult.

You should also **write and run the code yourself** whenever possible.

Reading an example is useful, but typing it, changing it, breaking it, fixing it, and experimenting with it will teach you much more.

For example, after seeing:

```cpp
int number = 10;
```

try changing `10` to another value and see what happens.

Experimentation is an important part of learning programming.

## Making mistakes is part of learning

Your code will not always work on the first attempt.

You may encounter:

- Compiler errors
- Warnings
- Unexpected output
- Logic mistakes
- Syntax mistakes
- Programs that behave differently from what you expected

This is completely normal.

Learning to **read errors, find problems, and fix your code** is one of the most important programming skills you can develop.

Do not be afraid to experiment. A broken program can often teach you just as much as a working one.

## What you should do in each lesson

A good way to work through a cppwiki lesson is:

1. Read the explanation.
2. Study the examples.
3. Type the code yourself.
4. Compile and run it.
5. Experiment by changing the code.
6. Make sure you understand the concept before moving on.

You do not need to memorize everything.

Focus on understanding the ideas. You can always come back to a lesson later when you need to review something.

## What these tutorials are trying to teach you

By the time you work through the Learn section, you should have more than a collection of C++ syntax memorized.

You should gradually learn how to:

- Think about problems like a programmer
- Break problems into smaller parts
- Read and understand code
- Write your own C++ programs
- Use variables, functions, conditions, loops, and other language features
- Find and fix errors
- Understand how different parts of a program interact
- Build larger programs from smaller concepts

The further you go, the more these individual concepts will start connecting together.

## One step at a time

Programming can feel overwhelming when you look at everything at once.

You do not need to learn everything at once.

Each lesson is one step. Learn that step, practice it, and then move on to the next one.

By combining many small concepts, you will eventually be able to build programs that initially seemed far too complicated.

Take your time, experiment with the examples, and most importantly, **keep writing code**.

!!! note "Note"

    For the rest of this tutorial we are assuming you are using the clang++ compiler and you are on linux.