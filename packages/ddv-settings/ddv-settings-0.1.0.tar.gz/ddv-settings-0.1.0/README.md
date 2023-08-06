# DDV Settings

Module for easily reading and exporting settings from files

## Example

**settings.ini**
```
[a]
b = c
d = e

[f]
g = h
j = k
```

Code that loads settings from `settings.ini` and uses them:
```
import os
import sys
from ddv.settings import read, export

read("settings.ini")
export(sys.modules[__name__], True, "TEST")

print("Variable TEST_A_B == c")
print(TEST_A_B)

print("Env Var TEST_F_G == h")
print(os.environ.get("TEST_F_G"))
```

**Output:**
```
Variable TEST_A_B == c
c
Env Var TEST_F_G == h
h
```