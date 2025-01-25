# Python - Kapitel 10

---

# Importera random

--

```python []
import random
```

```python []
from random import randint
```

Vi använder slumptal i Python genom att importera modulen **random**

---

# random()

--

Ger ett flyttal i intervallet **0 - 1.0**

Blir _aldrig_ exakt **0** eller **1**.

--

```python []
import random

r: float = random.random()
print(r)
```

```python []
0.33244833625067194
```

--

```python []
from random import random

r: float = random()
print(r)
```

```python []
0.14875270475440316
```

---

# randrange()

--

Ger ett slumptal (heltal) i motsvarande range

--

```python []
# 1-10 heltal
from random import randrange

r: int = randrange(1, 10 + 1)
print(r)
```

```python []
3
```

--

```python []
# 1-10 udda heltal
from random import randrange

r: int = randrange(1, 10, 2)
print(r)
```

```python []
9
```

--

```python []
# 1-10 udda heltal
from random import randrange

for i in range(10):
    r: int = randrange(1, 10, 2)
    print(r, end=" ")
```

```python []
9 7 9 7 9 3 7 3 7 1
```

--

```python []
# 0-10 jämna heltal
from random import randrange

r: int = randrange(0, 10, 2)
print(r)
```

```python []
4
```

--

```python []
# 0-10 jämna heltal
from random import randrange

for i in range(10):
    r: int = randrange(0, 10, 2)
    print(r, end=" ")
```

```python []
2 0 8 4 6 8 8 0 4 2
```

--

```python []
# 0-10 jämna heltal
from random import randrange

listan: list[int] = [randrange(0, 10, 2) for _ in range(10)]

print(*listan, sep=', ')
```

```python []
8, 0, 0, 2, 4, 0, 0, 4, 4, 4
```

--

```python []
# 0-10 jämna heltal
from random import randrange

r: str = ', '.join([str(randrange(0, 10, 2)) for i in range(10)])
print(r)
```

```python []
8, 0, 0, 2, 4, 0, 0, 4, 4, 4
```

---

# randint()

--

Ger ett heltal mellan **a** och **b**.

Utdatan kan verkligen anta extremvärdet.

--

```python []
# 1-10 heltal = alias till randrange(a, b+1)
from random import randint

r: int = randint(1, 10)
print(r)
```

```python []
10
```

---

# choice()

--

Väljer slumpmässigt ett element ur en sekvens, t.ex. en sträng, lista, tippel eller en range

--

```python []
# Väljer ett slumpmässigt element ur en sekvens
from random import choice

text: str = "ABCDE"
r: str = choice(text)

print(r)
```

```python []
B
```

--

```python []
# Väljer ett slumpmässigt element ur en sekvens
from random import choice

lista: list[str] = ['Kalle', 'Ada', 'Humle', 'Dumle']
r: str = choice(lista)

print(r)
```

```python []
Ada
```

--

```python
# Väljer ett slumpmässigt element ur en sekvens
from random import choice

listan: tuple[str, ...] = 'Kalle', 'Ada', 'Humle', 'Dumle'
r = choice(listan)

print(r)
```

```python []
Dumle
```

--

```python []
# Väljer ett slumpmässigt element ur en sekvens
from random import choice

numbers: int = range(50, 60 +1)
r: int = choice(numbers)

print(r)
```

```python []
57
```

---

# shuffle()

--

Blandar sekvensen _x_ på plats.

--

```python []
from random import shuffle

listan: list[int] = [7, 65, 5, 42, 45, 12]
shuffle(listan)
print(listan)
```

```python []
[12, 45, 42, 7, 65, 5]
```

--

```python []
from random import shuffle

listan: list[int] = [7, 65, 5, 42, 45, 12]
slumpad: list[int] = listan.copy()
shuffle(slumpad)

print(listan, slumpad, sep="\n")
```

```python []
[7, 65, 5, 42, 45, 12]
[45, 12, 65, 7, 42, 5]
```

---

# sample()

--

Drar slumpmässigt _k_ st element ur en population.

--

```python []
from random import sample

listan: list[str] = ['Kalle', 'Ada', 'Pelle', 'Marie', 'Elina', 'Olle']

val: list[str] = sample(listan, k=2)

print(val)
```

```python []
['Marie', 'Kalle']
```

---

# getstate() och setstate()

--

Läs av och sätt generatorns "**tillstånd**" för att kunna återupprepa en viss slumptalsföljd

--

```python []
from random import random

r1: float = random()
r2: float = random()

print(r1, r2, sep='\n')

r1: float  = random()
r2: float  = random()

print('\n', r1, r2, sep='\n')
```

```python []
0.6089971386840282
0.8501426052332153

0.3275715753540863
0.7877835005292809
```

--

```python [1, 3, 10]
from random import getstate, random, setstate

state: float  = getstate()

r1: float  = random()
r2: float  = random()

print(r1, r2, sep='\n')

setstate(state)

r1: float  = random()
r2: float  = random()

print(r1, r2, sep='\n')
```

```python []
0.9746084144708325
0.9100866238071204

0.9746084144708325
0.9100866238071204
```

---

# Slut!
