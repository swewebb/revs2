# Sortering av Dictionary

---

# Sortera efter nycklar

--

## Stigande ordning

```python []
data = {"b": 3, "a": 2, "c": 1}
sorterat = dict(sorted(data.items()))
print(sorterat)
```

```python []
{'a': 2, 'b': 3, 'c': 1}
```

**sorted()** kan användas för att sortera nycklarna.

--

**data.items()**

Hämtar alla nyckel-värde-par från **data** som en lista av _tuples_

```python []
[("b", 3), ("a", 2), ("c", 1)]
```

--

**sorted(data.items())**

Sorterar listan efter nycklarna då **sorted()** sorterar tuples efter första elementet.

```python []
[("a", 2), ("b", 3), ("c", 1)]
```

--

**dict(sorted(data.items()))**

Omvandlar den sorterade listan tillbaka till en ordbok

```python []
"a": 2, "b": 3, "c": 1}
```

--

## Fallande ordning

```python []
data = {"b": 3, "a": 2, "c": 1}
sorterat = dict(sorted(data.items(), reverse=True))
print(sorterat)
```

```python []
{'c': 1, 'b': 3, 'a': 2}
```

Lägg till **reverse=True** för att sortera i fallande ordning.

---

# Sortera efter värden

--

## Stigande ordning

```python []
data = {"äpple": 5, "banan": 2, "citron": 7}
sorterat = dict(sorted(data.items(), key=lambda x: x[1]))
print(sorterat)
```

```python []
{'banan': 2, 'äpple': 5, 'citron': 7}
```

Använd **sorted()** med lambda-funktion.

--

### Vad gör lambdan?

**lambda x: x[1]** är en anonym funktion som tar en _tuple_ **x** och returnerar dess _andra element_ (**x[1]**, alltså _värdet_ i ordboken).

I vårt fall har vi **(5, 2, 7)**

--

## Fallande ordning

```python []
data = {"äpple": 5, "banan": 2, "citron": 7}
sorterat = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
print(sorterat)
```

```python []
{'citron': 7, 'äpple': 5, 'banan': 2}
```

Lägg till **reverse=True** för att sortera i fallande ordning.

---

# SLUT!
