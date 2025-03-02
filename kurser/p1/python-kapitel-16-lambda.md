# Lambda-funktioner i Python

---

# Vad är en lambda-funktion?

--

En **lambda-funktion** är en _anonym funktion_ i Python.

Den kan ha obegränsat antal argument men endast ett uttryck.

Används ofta för korta, enkla funktioner.

```python []
lambda argument1, argument2: uttryck
```

---

# Exempel 1

--

## Utan lambda-funktion

```python []
def addera(x: int, y: int) -> int:
    """DOCSTRING"""
    return x + y

print(addera(3, 5))
```

--

## Med lambda-funktion

```python []
addera = lambda x, y: x + y
print(addera(3, 5))
```

```text []
8
```

---

# Exempel 2

--

## Utan lambda-funktion

--

```python []
nummer: list[int] = [1, 2, 3, 4]
kub_lista: list[int] = [x**3 for x in nummer]

print(kub_lista)
```

```python []
[1, 8, 27, 64]
```

--

```python []
def kub(x: int) -> int:
    """DOCSTRING"""
    return x**3

nummer: list[int] = [1, 2, 3, 4]
kub_lista: list[int] = list(map(kub, nummer))

print(kub_lista)
```

```python []
[1, 8, 27, 64]
```

--

## Med lambda-funktion

```python []
nummer: list[int] = [1, 2, 3, 4]
kub: list[int] = list(map(lambda x: x**3, nummer))
print(kub)
```

```python []
[1, 8, 27, 64]
```

---

# Exempel 3

--

## Utan lambda-funktion

```python []
nummer: list[int] = [1, 2, 3, 4, 5, 6]
jämna: list[int] = []

for x in nummer:
    if x % 2 == 0:
        jämna.append(x)

print(jämna)
```

```python []
[2, 4, 6]
```

--

```python []
nummer: list[int] = [1, 2, 3, 4, 5, 6]
jämna: list[int] = [x for x in nummer if x % 2 == 0]
print(jämna)
```

```python []
[2, 4, 6]
```

--

```python []
def är_jämn(x: int) -> bool:
    """DOCSTRING"""
    return x % 2 == 0

nummer: list[int] = [1, 2, 3, 4, 5, 6]
jämna: list[int] = list(filter(är_jämn, nummer))

print(jämna)
```

```python []
[2, 4, 6]
```

--

## Med lambda-funktion

```python []
nummer = [1, 2, 3, 4, 5, 6]
jämna = list(filter(lambda x: x % 2 == 0, nummer))
print(jämna)
```

```python []
[2, 4, 6]
```

---

# Exempel 4

--

## Utan lambda-funktion

```python []
def längd(x: str) -> int:
    """DOCSTRING"""
    return len(x)

namn: list[str] = ["Kalle", "Ann", "Olle-Bertil", "Erik"]
sorterat: list[str]  = sorted(namn, key=längd)

print(sorterat)
```

```python []
['Ann', 'Erik', 'Kalle', 'Olle-Bertil']
```

--

## Med lambda-funktion

```python []
namn: list[str] = ["Kalle", "Ann", "Olle-Bertil", "Erik"]
sorterat: list[str] = sorted(namn, key=lambda x: len(x))
print(sorterat)
```

```python []
['Ann', 'Erik', 'Kalle', 'Olle-Bertil']
```

---

# Extra

--

[Lambda Expressions & Anonymous Functions](https://www.youtube.com/watch?v=25ovCm9jKfA)

[Python Lambda](https://www.w3schools.com/python/python_lambda.asp)

[Lambda-funktioner i Python: Inline funktioner och syntax](https://makerelectronics.se/inline-funktioner-i-python/)

---

# SLUT!
