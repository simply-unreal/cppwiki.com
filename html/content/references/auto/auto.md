---
title: auto
difficulty: Beginner
---

# auto

The C++ `auto` keyword tells the compiler to **deduce the type of a variable from its initializer**.

Instead of explicitly writing the type, you can let the compiler determine it:

```cpp
auto number = 42;
```

Here, `number` is deduced as `int`.

!!! tip

    `auto` does not mean that the variable has no type. The type is determined by the compiler at compile time.

## Basic Syntax

```cpp
auto variable = initializer;
```

Example:

```cpp
auto age = 25; // int
auto price = 19.99; // double
auto name = "Alice"; // const char *
```

## Why Use auto?

`auto` is useful when:

- The type is long or complicated.
- The type is already obvious from the initializer.
- Working with iterators and templates.
- Writing generic code.
- Avoiding unnecessary repetition.

For example:

```cpp
std::vector<std::string>::const_iterator it = names.cbegin();
```

Can be simplified to:

```cpp
auto it = names.cbegin();
```

The resulting type is the same.

## Type Deduction

`auto` follows rules similar to template type deduction.

### Integer Values

```cpp
auto x = 10;
```

`x` is an `int`.

```cpp
auto x = 10L;
```

`x` is a `long`.

```cpp
auto x = 10LL;
```

`x` is a `long long`.

### Floating Point Values

```cpp
auto a = 3.14;
```

`a` is a `double`.

```cpp
auto b = 3.14f;
```

`b` is a `float`.

### Characters

```cpp
auto letter = 'A';
```

`letter` is a `char`.

### Boolean Values

```cpp
auto ready = true;
```

`ready` is a `bool`.

## `auto` and References

A plain `auto` declaration usually removes references from the deduced type.

```cpp
int value = 10;
int& reference = value;

auto x = reference;
```

Here, `x` is a `int` not `int&`.

To preserve the reference, use `auto&`:

```cpp
auto& x = reference;
```

Now `x` is an `int&`.

Changing `x` changes the original variable:

```cpp
int value = 10;

auto& ref = value;
ref = 20;
```

Now `value` is `20`.

## auto and const

A top-level `const` is not normally preserved when using plain `auto`.

```cpp
const int value = 10;

auto x = value; // int
```

To preserve `const`, use `const auto`:

```cpp
const auto x = value;
```

Now `x` is a `const int`.

For references, `const auto&` is commonly useful:

```cpp
const std::string name = "Alice";

const auto& ref = name;
```

## `auto` with Pointers

Pointers can also be deduced:

```cpp
int value = 42;
auto ptr = &value; // int *
```

You can also write:

```cpp
auto* ptr = &value;
```

Both forms deduce a `int *`.

## auto with Arrays

An important distinction occurs when copying an array.

```cpp
int values[] = {1, 2, 3};

auto x = values; // int *
```

This happens because the array decays to a pointer.

To preserve the array type, use a reference:

```cpp
auto& x = values;
```

Now `x` refers to the complete array.

## auto with Strings

String literals have an array type:

```cpp
auto text = "Hello"; // const char *
```

For a C++ `std::string`:

```cpp
#include <string>

auto text = std::string("Hello"); // std::string
```

## auto with Iterators

One of the most common uses of `auto` is with iterators.

Without `auto`:

```cpp
std::vector<int>::iterator it = numbers.begin();
```

With `auto`:

```cpp
auto it = numbers.begin();
```

This is especially helpful when the iterator type is long.

Example:

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers = {10, 20, 30};

    for (auto it = numbers.begin(); it != numbers.end(); ++it) {
        std::cout << *it << '\n';
    }
}
```

## Range Based for Loops

`auto` works especially well with range-based loops.

```cpp
#include <vector>
#include <iostream>

int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5};

    for (auto number : numbers) {
        std::cout << number << '\n';
    }
}
```

For references:

```cpp
for (auto& number : numbers) {
    number *= 2;
}
```

For read-only access without copying:

```cpp
for (const auto& number : numbers) {
    std::cout << number << '\n';
}
```

A common modern C++ pattern is:

```cpp
for (const auto& item : container) {
    // use item
}
```

## auto with Functions

Since C++14, `auto` can be used as a function return type when the compiler can deduce the return type from the function body.

```cpp
auto add(int a, int b) {
    return a + b; // returns int type
}
```

Another example:

```cpp
auto square(double value) {
    return value * value; // returns double type
}
```

The return statements must be compatible with the deduced return type.

## auto with Lambdas

Lambdas have unique compiler generated types that are difficult or impossible to name directly.

`auto` is therefore commonly used:

```cpp
auto greet = []() {
    return "Hello";
};
```

Another example:

```cpp
auto add = [](int a, int b) {
    return a + b;
};
```

You can then call it normally:

```cpp
std::cout << add(10, 20);
```

## auto with Structured Bindings

Structured bindings commonly use `auto`.

```cpp
#include <utility>

std::pair<int, std::string> get_user() {
    return {42, "Alice"};
}

int main() {
    auto [id, name] = get_user();
    // id = int
    // name = std::string
}
```

References can also be used:

```cpp
auto& [id, name] = user;
```

## auto in Variable Declarations

A declaration must have an initializer when using `auto`.

Valid:

```cpp
auto x = 10;
```

Invalid:

```cpp
auto x;
```

The compiler cannot determine the type of `x` without an initializer.

This is also invalid:

```cpp
auto x = {};
```

because the initializer does not provide enough information to deduce a type.

## Multiple auto Variables

Each `auto` declaration must deduce a type from its own initializer.

```cpp
auto a = 10; // int
auto b = 20.5; // double
```

You can declare multiple variables only when the deduced type is compatible:

```cpp
auto a = 10, b = 20; // both are int
```

This is invalid:

```cpp
auto a = 10, b = 20.5;
```

because the declarations would require different deduced types.

## auto Does Not Mean Dynamic Typing

C++ remains statically typed.

```cpp
auto value = 10;
```

After compilation, `value` has a specific type: `int`.

You cannot later assign an unrelated type:

```cpp
auto value = 10;

value = "hello"; // invalid
```

## auto vs Explicit Types

These declarations are equivalent in the resulting type:

```cpp
int count = 10;
auto count = 10;
```

The main difference is how the source code expresses the type.

Explicit type:

```cpp
std::unordered_map<std::string, std::vector<int>>::const_iterator it = data.cbegin();
```

Using `auto`:

```cpp
auto it = data.cbegin();
```

The second form is usually easier to read and maintain.

## Common Mistakes

### Forgetting the Initializer

Incorrect:

```cpp
auto value;
```

Correct:

```cpp
auto value = 10;
```

### Assuming const Is Preserved

```cpp
const int value = 10;
auto copy = value;
```

`copy` is an `int`, not a `const int`.

Use:

```cpp
const auto copy = value;
```

when const qualification should be part of the new object.

### Accidentally Copying Large Objects

Consider:

```cpp
for (auto item : large_container) {
    // item is a copy
}
```

For read-only access use this:

```cpp
for (const auto& item : large_container) {
    // no object copy
}
```

For modification:

```cpp
for (auto& item : large_container) {
    // modifies the original element
}
```

## Best Practices

Use `auto` when the initializer makes the type obvious:

```cpp
auto count = 100;
auto name = std::string("Alice");
auto it = container.begin();
```

Use an explicit type when the type includes important information that is not obvious:

```cpp
std::chrono::milliseconds timeout = 500ms;
```

Avoid using `auto` to hide an important information.

## Summary

The `auto` keyword lets C++ deduce a variable's type from its initializer.

The most common forms are:

```cpp
auto value = expression;
const auto value = expression;
auto& value = expression;
const auto& value = expression;
auto* value = &expression;
auto&& value = expression;
```