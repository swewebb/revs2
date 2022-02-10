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

Ger ett flyttal i intervallet 0,..,1.0.

Blir aldrig exakt 0 eller 1.

--

```python []
import random

r = random.random()
print(r)
```

```html []
0.33244833625067194
```

--

```python []
from random import random

r = random()
print(r)
```

```html []
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

r = randrange(1, 10 + 1)
print(r)
```

```html []
3
```

--

```python []
# 1-10 udda heltal
from random import randrange

r = randrange(1, 10, 2)
print(r)
```

```html []
9
```

--

```python []
# 1-10 udda heltal
from random import randrange

for i in range(10):
    r = randrange(1, 10, 2)
    print(r, end=" ")
```

```html []
9 7 9 7 9 3 7 3 7 1
```

--

```python []
# 0-10 jämna heltal
from random import randrange

r = randrange(0, 10, 2)
print(r)
```

```html []
4
```

--

```python []
# 0-10 jämna heltal
from random import randrange

for i in range(10):
    r = randrange(0, 10, 2)
    print(r, end=" ")
```

```html []
2 0 8 4 6 8 8 0 4 2
```

--

```python []
# 0-10 jämna heltal
from random import randrange

r = ', '.join([str(randrange(0, 10, 2)) for i in range(10)])
print(r)
```

```html []
8, 0, 0, 2, 4, 0, 0, 4, 4, 4
```

---

# randint()

--

Ger ett heltal mellan a och b.

Utdatan kan verkligen anta extremvärdet.

--

```python []
# 1-10 heltal = alias till randrange(a, b+1)
from random import randint

r = randint(1, 10)
print(r)
```

```html []
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

text = "ABCDE"
r = choice(text)

print(r)
```

```html []
B
```

--

```python []
# Väljer ett slumpmässigt element ur en sekvens
from random import choice

lista = ['Kalle', 'Ada', 'Humle', 'Dumle']
r = choice(lista)

print(r)
```

```html []
Ada
```

--

```python
# Väljer ett slumpmässigt element ur en sekvens
from random import choice

tupel = 'Kalle', 'Ada', 'Humle', 'Dumle'
r = choice(tupel)

print(r)
```

```html []
Dumle
```

--

```python []
# Väljer ett slumpmässigt element ur en sekvens
from random import choice

numbers = range(50, 60 +1)
r = choice(numbers)

print(r)
```

```html []
57
```

---

# shuffle()

--

Blandar sekvensen _x_ på plats.

--

```python []
from random import shuffle

listan = [7, 65, 5, 42, 45, 12]
shuffle(listan)
print(listan)
```

```html []
[12, 45, 42, 7, 65, 5]
```

--

```python []
from random import shuffle

listan = [7, 65, 5, 42, 45, 12]

slumpad = listan.copy()
shuffle(slumpad)
print(listan, slumpad, sep="\n")
```

```html []
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

listan = ['Kalle', 'Ada', 'Pelle', 'Marie', 'Elin', 'Olle']

val = sample(listan, k=2)

print(val)
```

```html []
['Marie', 'Kalle']
```

---

# getstate() och setstate()

--

Läs av och sätt generatorns "**tillstånd**" för att kunna återupprepa en viss slumptalsföljd

--

```python []
from random import random

r1 = random()
r2 = random()

print(r1, r2, sep='\n')

r1 = random()
r2 = random()

print('\n', r1, r2, sep='\n')
```

```html []
0.6089971386840282
0.8501426052332153

0.3275715753540863
0.7877835005292809
```

--

```python [1, 3, 10]
from random import getstate, random, setstate

state = getstate()

r1 = random()
r2 = random()

print(r1, r2, sep='\n')

setstate(state)

r1 = random()
r2 = random()

print(r1, r2, sep='\n')
```

```html []
0.9746084144708325
0.9100866238071204

0.9746084144708325
0.9100866238071204
```

---

# Slut!
