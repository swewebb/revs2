# Python - Kapitel 16

---

# Repetition om listor m.m.

--

```python
txt: str = 'abcdefghijklmnop'
sliced: str = txt[1:4+1]
print(sliced)
```

```
bcde
```

--

```python
txt: str = 'abcdefghijklmnop'
splitted = txt.split('d')
print(splitted)
```

```python
['abc', 'efghijklmnop']
```

--

```python
txt: str = 'abcdefghijklmnop'
lista: list[str] = list(txt)
print(lista)
```

```python
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
```

--

```python
txt: str = 'abcdefghijklmnop'
lista: list[str] = list(txt)
sliced: list[str] = lista[1:4+1]
print(sliced)
```

```python
['b', 'c', 'd', 'e']
```

--

```python
txt: str = 'abcdefghijklmnop'
lista: list[str] = list(txt)
sammanfogad: str = '-'.join(lista)

print(sammanfogad)
```

```python
a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p
```

--

```python
sammanfogad: str = '-'.join(list('abcdefghijklmnop'))

print(sammanfogad)
```

```python
a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p
```

--

```python
txt: str = 'abcdefghijklmnop'
lista: list[str] = list(txt)
tippel: tuple[str, ...] = tuple(txt)

print(lista, end='\n\n')
print(tippel)
```

```python
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']

('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p')
```

---

# Sammanfattning av listmetoder och listfunktioner

--

## len(lista)

--

Längden av listan. Sista index är `len(lista)-1`

```python
lista: list[str] = ['A', 'B', 'C', 'D']
x: int = len(lista)
y: int = len(lista)-1

print(f"{x=}, {y=}")

```

```python
x=4, y=3
```

--

## sorted(lista)

--

Returnerar en sorterad lista, där elementen måste vara av samma typ

```python
lista: list[str] = ['X', 'B', 'E', 'D']
sorterad_lista: list[str] = sorted(lista)

print(f"{lista=}")
print(f"{sorterad_lista=}")
```

```python
lista=['X', 'B', 'E', 'D']
sorterad_lista=['B', 'D', 'E', 'X']
```

--

## lista.append(x)

--

Lägger till elementet **x** i slutet av listan

```python
lista: list[str] = ['A', 'B', 'C', 'D']
lista.append('X')
print(lista)
```

```python
['A', 'B', 'C', 'D', 'X']
```

--

## lista.extend(lista2)

--

Förlänger listan med en annan lista

```python
lista1: list[str] = ['A', 'B', 'C', 'D']
lista2: list[str] = ["X", "Y", "Z"]
lista1.extend(lista2)

print(f"{lista1=}")
```

```python
lista1=['A', 'B', 'C', 'D', 'X', 'Y', 'Z']
```

--

## lista.insert(i,x)

--

Infogar elementet **x** på plats **i**.

```python
lista: list[str] = ['A', 'B', 'C', 'D']
lista.insert(2, 'Y')

print(f"{lista=}")
```

```python
lista=['A', 'B', 'Y', 'C', 'D']
```

--

## lista.remove(x)

--

Tar bort första elementet med värdet **x**

```python
lista: list[str] = ['A', 'B', 'C', 'D', 'C']
lista.remove('C')

print(f"{lista=}")
```

```python
lista=['A', 'B', 'D', 'C']
```

--

## lista.pop(i)

--

Tar bort elementet med index **i** och returnerar värdet. Om **i** utelämnas är standard (default) att sista värdet tas bort.

```python
lista: list[str] = ['A', 'B', 'C', 'D']
lista.pop()
lista.pop(1)

print(f"{lista=}")
```

```python
lista=['A', 'C']
```

--

## lista.index(x)

--

Returnerar index för första förekomst av element **x**.

```python
lista: list[str] = ['A', 'B', 'C', 'D', 'C', 'C']
plats = lista.index('C')

print(f"{plats=}")
```

```python
plats=2
```

--

## lista.count(x)

--

Returnerar antalet element med värdet **x**.

```python
lista: list[str] = ['A', 'B', 'C', 'D', 'C', 'C']
antal = lista.count('C')

print(f"{antal=}")
```

```python
antal=3
```

--

## lista.sort()

--

Sorterar listan på plats

```python
lista: list[str] = ['E', 'B', 'A', 'D', 'C']
lista.sort()

print(lista)
```

```python
['A', 'B', 'C', 'D', 'E']
```

--

## lista.reverse()

--

Vänder på ordningen av elementen i listan.

```python
lista: list[str] = ['A', 'B', 'C', 'D']
lista.reverse()

print(lista)
```

```python
['D', 'C', 'B', 'A']
```

---

# Enumerate

--

Ibland vill man loopa över en sträng/lista/tippel så att man har tillgång till både index och listelementet samtidigt, och då kan man använda `enumerate`.

--

```python
txt: str = 'Teknik'

for index, char in enumerate(txt):
    print(index, char)
```

```python
0 T
1 e
2 k
3 n
4 i
5 k
```

--

```python
tippel: tuple[str, ...] = tuple('Teknik')

print(tippel)

for index, char in enumerate(tippel):
    print(index, char)
```

```python
('T', 'e', 'k', 'n', 'i', 'k')
0 T
1 e
2 k
3 n
4 i
5 k
```

---

# Dictionaries

## _Associativ array_

## _Ordböcker_

--

Förutom vanliga strängar, tipplar och listor finns i Python en datatyp som kallas för "associativ array", eller en "dictionary".

Denna datatyp fungerar ungefär som en lista, men istället för heltalsindex används ett namn på varje element, en s.k. **key**, vanligtvis en sträng, men det kan vara ett tal också.

--

Ett dictionary består av en mängd par där första delen kallas för **nyckel** och andra delen för **värde**.

Varje par av nyckel-värde kallas för en **post** eller **item**.

--

Istället för hakparenteser används "måsvingar" **{ }** och **kolon** när dictionariet definieras, men hakparenteser används så snart vi gör indexeringar i det.

---

# Skapa en ordbok

--

```python
skateboard: dict[str, str | float] = {
    "brand": "Creature",
    "model": "Martinez Calavera",
    "width": 8.99,
    "length": 32.64
}

print(skateboard)
```

```python
{'brand': 'Creature', 'model': 'Martinez Calavera', 'width': 8.99, 'length': 32.64}
```

--

**dict[str, str | float]** betyder att **skateboard** är en ordbok där:

- Nycklarna (_str_) alltid är av typen **str** (sträng).
- Värdena (_str | float_) kan vara antingen **str** (sträng) eller **float** (decimaltal).

---

# Hämta ut data

--

```python
skateboard: dict[str, str | float] = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

brand: str = skateboard["brand"]
print(brand)
```

```python
Creature
```

--

```python
skateboard: dict[str, str | float] = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}
brand: str = skateboard.get("brand")
print(brand)
```

```python
Creature
```

--

```python
from typing import KeysView

skateboard: dict[str, str | float] = {
    "brand": "Creature",
    "model": "Martinez Calavera",
    "width": 8.99,
    "length": 32.64
}

keys: KeysView[str]  = skateboard.keys()
print(keys)
```

```python
dict_keys(['brand', 'model', 'width', 'length'])
```

--

```python
skateboard: dict[str, str | float] = {
    "brand": "Creature",
    "model": "Martinez Calavera",
    "width": 8.99,
    "length": 32.64
}

keys: list[str] = list(skateboard.keys())
print(keys)
```

```python
['brand', 'model', 'width', 'length']
```

--

```python
from typing import ValuesView

skateboard: dict[str, str | float] = {
    "brand": "Creature",
    "model": "Martinez Calavera",
    "width": 8.99,
    "length": 32.64
}

parts: ValuesView[str | float] = skateboard.values()

print(parts)
```

```python
dict_values(['Creature', 'Martinez Calavera', 8.99, 32.64])
```

--

```python
skateboard: dict[str, str | float] = {
    "brand": "Creature",
    "model": "Martinez Calavera",
    "width": 8.99,
    "length": 32.64
}

parts: list[str | float] = list(skateboard.values())

print(parts)
```

```python
['Creature', 'Martinez Calavera', 8.99, 32.64]
```

--

```python
from typing import ItemsView

skateboard: dict[str, str | float] = {
    "brand": "Creature",
    "model": "Martinez Calavera",
    "width": 8.99,
    "length": 32.64
}

part_info: ItemsView[str, str | float] = skateboard.items()
print(part_info)
```

```python
dict_items([('brand', 'Creature'), ('model', 'Martinez Calavera'), ('width', 8.99), ('length', 32.64)])
```

--

```python
skateboard: dict[str, str | float] = {
    "brand": "Creature",
    "model": "Martinez Calavera",
    "width": 8.99,
    "length": 32.64
}

part_info: list[tuple[str, str | float]] = list(skateboard.items())
print(part_info)
```

```
[('brand', 'Creature'), ('model', 'Martinez Calavera'), ('width', 8.99), ('length', 32.64)]
```

--

```python
skateboard: dict[str, str | float] = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}


if "model" in skateboard:
    print("Finns!")
```

```python
Finns!
```

---

# Ändra

--

```python
skateboard: dict[str, str | float] = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 3.64
}

skateboard["length"] = 32.64
print(skateboard)
```

```python
{'brand': 'Creature', 'model': 'Martinez Calavera', 'width': 8.99, 'length': 32.64}
```

--

```python
skateboard: dict[str, str | float] = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 3.64
}

skateboard.update({"length": 32.64})
print(skateboard)
```

```python
{'brand': 'Creature', 'model': 'Martinez Calavera', 'width': 8.99, 'length': 32.64}
```

---

# Lägga till

--

```python
skateboard: dict[str, str | float] = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

skateboard["wheelbase"] = 14.25
print(skateboard)
```

```python
{'brand': 'Creature', 'model': 'Martinez Calavera', 'width': 8.99, 'length': 3.64, 'wheelbase': 14.25}
```

--

```python
skateboard: dict[str, str | float] = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

skateboard.update({"wheelbase": 14.25})
print(skateboard)
```

```python
{'brand': 'Creature', 'model': 'Martinez Calavera', 'width': 8.99, 'length': 3.64, 'wheelbase': 14.25}
```

---

# Ta bort

--

```python
skateboard: dict[str, str | float] = {
  "brand": "Creature",
  "kaka": "jepp",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

skateboard.pop("kaka")
print(skateboard)
```

```python
{'brand': 'Creature', 'model': 'Martinez Calavera', 'width': 8.99, 'length': 3.64}
```

--

```python
skateboard: dict[str, str | float] = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

skateboard.popitem()
print(skateboard)
```

```python
{'brand': 'Creature', 'model': 'Martinez Calavera', 'width': 8.99}
```

--

```python
skateboard: dict[str, str | float] = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "kaka": "jepp",
  "width": 8.99,
  "length": 32.64
}

del skateboard["kaka"]
print(skateboard)
```

```python
{'brand': 'Creature', 'model': 'Martinez Calavera', 'width': 8.99, 'length': 32.64}
```

--

```python
skateboard: dict[str, str | float] = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "kaka": "jepp",
  "width": 8.99,
  "length": 32.64
}

del skateboard
print(skateboard)
```

```python
Traceback (most recent call last):
  File "demo.py", line 10, in <module>
    print(skateboard)
NameError: name 'skateboard' is not defined
```

--

```python
skateboard: dict[str, str | float] = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "kaka": "jepp",
  "width": 8.99,
  "length": 32.64
}

skateboard.clear()
print(skateboard)
```

```python
{}
```

---

# Loopa

--

```python
skateboard: dict[str, str | float] = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

for txt in skateboard:
    print(txt)
```

```
brand
model
width
length
```

--

```python
skateboard: dict[str, str | float] = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

for txt in skateboard.keys():
    print(txt)
```

```
brand
model
width
length
```

--

```python
skateboard: dict[str, str | float] = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

for txt in skateboard:
    part_info: str | float = skateboard[txt]
    print(part_info)
```

```
Creature
Martinez Calavera
8.99
32.64
```

--

```python
skateboard: dict[str, str | float] = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

for txt in skateboard:
    part_info = skateboard.get(txt)
    print(part_info)
```

```
Creature
Martinez Calavera
8.99
32.64
```

--

```python
skateboard: dict[str, str | float] = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

for value in skateboard.values():
    print(value)
```

```
Creature
Martinez Calavera
8.99
32.64
```

--

```python
skateboard: dict[str, str | float] = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

for key, value in skateboard.items():
    print(key, value, sep=": ")
```

```
brand: Creature
model: Martinez Calavera
width: 8.99
length: 32.64
```

---

# Kopiera

--

```python
skateboard: dict[str, str | float] = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

kopia: dict[str, str | float] = skateboard.copy()
print(kopia)
```

```python
{'brand': 'Creature', 'model': 'Martinez Calavera', 'width': 8.99, 'length': 32.64}
```

--

```python
skateboard: dict[str, str | float] = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

kopia: dict[str, str | float] = dict(skateboard)
print(kopia)
```

```python
{'brand': 'Creature', 'model': 'Martinez Calavera', 'width': 8.99, 'length': 32.64}
```

---

# Nästlade

--

```python
skateboards: dict[str, dict[str, str | float]] = {
    "board1": {"brand": "Creature",
               "model": "Martinez Calavera",
               "width": 8.99,
               "length": 32.64},
    "board2": {"brand": "Prime Heritage",
               "model": "Dune Curb Crusher",
               "width": 8.25,
               "length": 31.75},
}

print(skateboards)
```

```python
{'board1': {'brand': 'Creature', 'model': 'Martinez Calavera', 'width': 8.99, 'length': 32.64}, 'board2': {'brand': 'Prime Heritage', 'model': 'Dune Curb Crusher', 'width': 8.25, 'length': 31.75}}
```

--

```python
skateboards: dict[str, dict[str, str | float]] = {
    "board1": {"brand": "Creature",
               "model": "Martinez Calavera",
               "width": 8.99,
               "length": 32.64},
    "board2": {"brand": "Prime Heritage",
               "model": "Dune Curb Crusher",
               "width": 8.25,
               "length": 31.75},
}

board: dict[str, str | float] = skateboards["board1"]
print(board)
```

```python
{'brand': 'Creature', 'model': 'Martinez Calavera', 'width': 8.99, 'length': 32.64}
```

--

```python
skateboards: dict[str, dict[str, str | float]] = {
    "board1": {"brand": "Creature",
               "model": "Martinez Calavera",
               "width": 8.99,
               "length": 32.64},
    "board2": {"brand": "Prime Heritage",
               "model": "Dune Curb Crusher",
               "width": 8.25,
               "length": 31.75},
}

model: str = skateboards["board1"]["model"]
print(board)
```

```python
Martinez Calavera
```

--

```python
skateboards: dict[str, dict[str, str | float]] = {
    "board1": {"brand": "Creature",
               "model": "Martinez Calavera",
               "width": 8.99,
               "length": 32.64},
    "board2": {"brand": "Prime Heritage",
               "model": "Dune Curb Crusher",
               "width": 8.25,
               "length": 31.75},
}

skateboards["board3"] = {
    "brand": "Tired",
    "model": "Logo Two on Chuck",
    "width": 8.625,
    "length": 32.00
}

print(skateboards)
```

```python
{'board1': {'brand': 'Creature', 'model': 'Martinez Calavera', 'width': 8.99, 'length': 32.64}, 'board2': {'brand': 'Prime Heritage', 'model': 'Dune Curb Crusher', 'width': 8.25, 'length': 31.75}, 'board3': {'brand': 'Tired', 'model': 'Logo Two on Chuck', 'width': 8.625, 'length': 32.0}}
```

--

```python
skateboards: dict[str, dict[str, str | float]] = {
    "board1": {"brand": "Creature",
               "model": "Martinez Calavera",
               "width": 8.99,
               "length": 32.64},
    "board2": {"brand": "Prime Heritage",
               "model": "Dune Curb Crusher",
               "width": 8.25,
               "length": 31.75},
}

del skateboards["board2"]

print(skateboards)
```

```python
{'board1': {'brand': 'Creature', 'model': 'Martinez Calavera', 'width': 8.99, 'length': 32.64}}
```

--

```python
skateboards: dict[str, dict[str, str | float]] = {
    "board1": {"brand": "Creature",
               "model": "Martinez Calavera",
               "width": 8.99,
               "length": 32.64},
    "board2": {"brand": "Prime Heritage",
               "model": "Dune Curb Crusher",
               "kaka": "jepp",
               "width": 8.25,
               "length": 31.75},
}

del skateboards["board2"]["kaka"]

print(skateboards)
```

```python
{'board1': {'brand': 'Creature', 'model': 'Martinez Calavera', 'width': 8.99, 'length': 32.64}, 'board2': {'brand': 'Prime Heritage', 'model': 'Dune Curb Crusher', 'width': 8.25, 'length': 31.75}}
```

--

```python
skateboards: dict[str, dict[str, str | float]] = {
    "board1": {"brand": "Creature",
               "model": "Martinez Calavera",
               "width": 8.99,
               "length": 32.64},
    "board2": {"brand": "Prime Heritage",
               "model": "Dune Curb Crusher",
               "width": 8.25,
               "length": 31.75},
}

for board, info in skateboards.items():
    print(board, info)
```

```python
board1 {'brand': 'Creature', 'model': 'Martinez Calavera', 'width': 8.99, 'length': 32.64}
board2 {'brand': 'Prime Heritage', 'model': 'Dune Curb Crusher', 'width': 8.25, 'length': 31.75}
```

--

```python
skateboards: dict[str, dict[str, str | float]] = {
    "board1": {"brand": "Creature",
               "model": "Martinez Calavera",
               "width": 8.99,
               "length": 32.64},
    "board2": {"brand": "Prime Heritage",
               "model": "Dune Curb Crusher",
               "width": 8.25,
               "length": 31.75},
}

for board, info in skateboards.items():
    print(board)
    for detail, value in info.items():
        print(f"   {detail} : {value}")
    print('------------------')
```

--

```
board1
    brand :  Creature
    model :  Martinez Calavera
    width :  8.99
    length :  32.64
------------------
board2
    brand :  Prime Heritage
    model :  Dune Curb Crusher
    width :  8.25
    length :  31.75
------------------
```

---

# Slut!
