# Installing C++

Now that you know what C++ actually is, we can get started with installing the tools you need to program in it.

## Windows

On Windows, we'll use [Scoop](https://scoop.sh/) to install Clang, the C and C++ compiler.

First, make sure Scoop is installed. If you don't have it yet, follow the instructions on the [Scoop website](https://scoop.sh/).

Once Scoop is installed, open **PowerShell** and run:

```powershell
scoop install llvm
```

This will install LLVM, which includes **Clang** and **Clang++**.

If the command succeeded, you can run this to make sure Clang++ is actually installed:

```powershell
clang++ --version
```

That should output something similar to this:

```text
clang version 22.1.8
Target: x86_64-pc-windows-msvc
Thread model: posix
InstalledDir: ...
```

!!! note

    Don't worry if the output of `clang++ --version` does not exactly match the output shown above. The version and other details may be different. As long as `clang++ --version` works, you should be good to go!

## Installing a Code Editor

Now that you have Clang++ installed, you can choose a code editor.

!!! tip

    A code editor is a matter of personal preference, so use whatever you like!

For this tutorial, we will be using VS Code, but you can use any code editor you want.

Since we're using Scoop, you can install VS Code directly from PowerShell:

```powershell
scoop bucket add extras
scoop install vscode
```

Once VS Code is installed, you'll need the C++ extension. Use this keyboard shortcut to open the Extensions panel:

<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>X</kbd>

Now find the extension called **C/C++ Extension Pack** by **Microsoft**.

This will give you everything you need to get started with programming in C++!

!!! note

    If something doesn't work for you, feel free to search for a solution, ask an AI, or look up a YouTube tutorial!