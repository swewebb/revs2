# Python - Kapitel 8 - Tupler

---

# Tipplar/Tuplar

--

En tupel består av följd (0 eller flera) av element. Elementen kan t.ex. vara heltal, flyttal, strängar, tupler och listor.

Den väsentliga skillnaden mot listor är att tupel-objekt inte går att ändra (eng. **immutable**).

Definieras m.h.a vanliga parenteser istället för hakparenteser som vi använder i listor.

---

# Skapa en tupel

```python []
tippel = (1, 2, 3)

print(tippel)
print(tippel[1])
print(tippel[-1])
```

```python []
(1, 2, 3)
2
3
```

---

# Vad händer om vi försöker lägga till?

```python []
tippel = (1, 2, 3)
tippel.append(4)
```

```python []
Traceback (most recent call last):
  File "c:/git/p1/ex.py", line 2, in <module>
    tippel.append(4)
AttributeError: 'tuple' object has no attribute 'append'
```

---

# Metoder

--

## count()

```python []
tippel = ("kalle", "lotta", "ada", "lotta")

print(tippel.count("lotta"))
```

```python []
2
```

--

## index()

```python []
tippel = ("kalle", "lotta", "ada", "lotta")

print(tippel.index("lotta"))
```

```python []
1
```

---

# Längd

--

```python []
tippel = (1, 2, 3)

print(len(tippel))
```

```python []
3
```

---

# Packa och packa upp värden med tipplar

--

## Packa ihop

```python []
tippel = 1, 2, 3, 4, 5

print(tippel)
```

```python []
(1, 2, 3, 4, 5)
```

--

## Packa upp

```python []
tippel = (3, 5, 8, 12)

one, two, three, four = tippel
print(four)
```

```python []
12
```

Fungerar även på listor.

--

```python []
tippel = (3, 5, 8, 12)

one, two, three = tippel
print(one)
```

```python []
Traceback (most recent call last):
  File "c:\git\P1\ex.py", line 3, in <module>
    one, two, three = tippel
    ^^^^^^^^^^^^^^^
ValueError: too many values to unpack (expected 3)
```

--

```python []
tippel = (3, 5, 8, 12)

one, two, three, four = tippel

one, two, three = three, two, one

print(one)
print(two)
print(three)
```

```python []
8
5
3
```

Fungerar även på listor.

--

```python []
tippel = ("kalle", "lotta", "ada", "lotta")

print(*tippel, sep=", ")
```

```python []
kalle, lotta, ada, lotta
```

Packar upp elementen i tuppeln och skickar dem som separata argument till **print**.

**sep=", "** anger hur elementen ska separeras.

Fungerar även på listor.

--

```python []
tippel = (3, 5, 8, 12)

print(*tippel, sep=", ")
```

```python []
3, 5, 8, 12
```

--

```python []
tippel = ("kalle", 12, 3.14 , True)

print(*tippel, sep=", ")
```

```html []
kalle, 12, 3.14, True
```

---

# Listor vs tupler

--

```python []
from timeit import timeit

listTime = timeit(stmt='[1,2,3,4,5,6,7,8,9,10]', number=1_000_000)
tupleTime = timeit(stmt='(1,2,3,4,5,6,7,8,9,10)', number=1_000_000)

print(listTime)  # 0.06349750000117638
print(tupleTime) # 0.009809799999857205
```

Här använder vi modulen **timeit** för att mäta tiden det tar att skapa en lista respektive en tuppel en miljon gånger.

--

```python []
listan = ['Kålle', 'Ada', 'Kalle', 'Lotta', 'Nicko', 'Pulver', 'Humle', 'Dumle']
tupler = ('Kålle', 'Ada', 'Kalle', 'Lotta', 'Nicko', 'Pulver', 'Humle', 'Dumle')

print('listan =',listan.__sizeof__())
print('tupler =',tupler.__sizeof__())
```

```python []
listan = 104
tupler = 88
```

--

Tupel använder mindre minne jämfört med listor eftersom de inte behöver lagra extra information för att hantera ändringar.

Detta minskar både minnesåtgång och exekveringstid.

---

# SLUT!
