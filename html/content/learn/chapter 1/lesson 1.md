---
title: Your First C++ Program
difficulty: Beginner
---

# Your First C++ Program

To get started, create a new folder to hold your projects. You can store this folder anywhere on your computer; in this example, we will place it on the `C:` drive:

```powershell
mkdir C:\Projects
```

Next, create a new folder inside `Projects` named `Testing`. This is where your code will live:

```powershell
mkdir C:\Projects\Testing
```

Open the `Testing` folder in VS Code and create a file named `main.cpp`. Paste the following code into `main.cpp`:

```cpp
#include <iostream>

int main() {
    std::cout << "Hello World!\n";
    return 0;
}
```

!!! tip

    You don't need to understand how every line of this code works just yet. We will cover the details in upcoming lessons!

To compile your code, open the integrated terminal in VS Code (`Ctrl + ~` or `Cmd + ~`) and run:

```powershell
clang++ main.cpp -o main.exe
```

Once compiled, you will see a new `main.exe` executable file in your project folder. To execute your program run this:

```powershell
.\main.exe
```

When you run `main.exe` you should get a output that looks something like this:

```text
Hello World!
```

Great you just compiled and ran your first C++ program!