# Moduler - Del 1

---

# Använda import

--

```python []
import math

x: float = 1.4
y: int = math.ceil(1.4)
z: int = math.floor(1.4)

print(f"{x=}, {y=}, {z=}")
```

```html []
x=1.4, y=2, z=1
```

[Python math Module](https://www.w3schools.com/python/module_math.asp)

--

## Använda import med alias

```python []
import math as m

x: float = 1.4
y: int = m.ceil(1.4)
z: int = m.floor(1.4)

print(f"{x=}, {y=}, {z=}")
```

```html []
x=1.4, y=2, z=1
```

---

# Använda from \_\_ import \_\_

--

## Importera vissa funktioner

```python []
from math import ceil, floor

x: float = 1.4
y: int = ceil(1.4)
z: int = floor(1.4)

print(f"{x=}, {y=}, {z=}")
```

--

## Importera allt

```python []
from math import *

x: float = 1.4
y: int = ceil(1.4)
z: int = floor(1.4)

print(f"{x=}, {y=}, {z=}")
```

**Undvik det här sättet!**

Det kan skapa otydlig kod och namnkonflikter. I det här fallet omdefinieras den inbyggda funktionen **pow**.

---

# Isolera en import

--

```python []
def supersecret(number: float) -> float:
  """DOCSTRING"""
  import math
  return math.sqrt(number)

print(supersecret(16))
```

--

```python []
def supersecret(number: float) -> float:
  """DOCSTRING"""
  from math import sqrt
  return sqrt(number)

print(supersecret(16))
```

---

# SLUT!
