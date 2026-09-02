---
title: Installing C++
difficulty: Beginner
---

# Installing C++

Now that you know what C++ actually is, we can get started with installing the tools you need to program in it.

## Ubuntu

To install Clang and Clang++, the C and C++ compilers, you need to run these two commands:

```bash
sudo apt update # Updates Ubuntu's list of available software packages

sudo apt install clang # Installs Clang and Clang++
```

If those commands succeeded, you can run this command to make sure Clang++ is actually installed:

```bash
clang++ --version
```

That should output something similar to this:

```text
clang version 22.1.8
Target: x86_64-pc-linux-gnu
Thread model: posix
InstalledDir: /usr/bin
```

!!! note

    Don't worry if the output of `clang++ --version` does not exactly match the output shown above. As long as `clang++ --version` works, you should be good to go!

## Arch

Installing Clang++ on Arch is also pretty easy. First, run:

```bash
sudo pacman -Syu # Updates the package database and upgrades installed packages
```

Then run:

```bash
sudo pacman -S clang
```

If that command succeeded, you can run this to make sure Clang++ was installed:

```bash
clang++ --version
```

That should output something similar to this:

```text
clang version 22.1.8
Target: x86_64-pc-linux-gnu
Thread model: posix
InstalledDir: /usr/bin
```

!!! note

    Don't worry if the output of `clang++ --version` does not exactly match the output shown above. As long as `clang++ --version` works, you should be good to go!

## Installing a Code Editor

Now that you have Clang++ installed, you can choose a code editor.

!!! tip

    A code editor is a matter of personal preference, so use whatever you like!

For this tutorial, we will be using VS Code, but you can use any code editor you want.

To install VS Code, go to [this link](https://code.visualstudio.com/download).

Once you're there, install the latest version for your distro. If you're on Arch and you don't see a download option, run this command in your terminal:

```bash
sudo pacman -S code
```

Once VS Code is installed, you'll need the C++ extension. Use this keyboard shortcut to open the Extensions panel:

<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>X</kbd>

Now find the extension called **C/C++ Extension Pack** by **Microsoft**.

This will give you everything you need to get started with programming in C++!

!!! note

    If something doesn't work for you, feel free to search for a solution, ask an AI, or look up a YouTube tutorial!