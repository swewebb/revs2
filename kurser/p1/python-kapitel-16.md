# Python - Kapitel 16

---

# Repetition om listor m.m.

--

```python
string = 'abcdefghijklmnop'
x = string[1:4+1]
print(x)
```

```
bcde
```

--

```python
string = 'abcdefghijklmnop'
x = string.split('d')
print(x)
```

```python
['abc', 'efghijklmnop']
```

--

```python
string = 'abcdefghijklmnop'
lista = list(string)
print(lista)
```

```python
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
```

--

```python
lista = list(string)
x = lista[1:4+1]
print(x)
```

```python
['b', 'c', 'd', 'e']
```

--

```python
lista = list(string)
x = '-'.join(lista)
print(x)
```

```python
a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p
```

--

```python
print('-'.join(list('abcdefghijklmnop')))
```

```python
a-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p
```

--

```python
string = 'abcdefghijklmnop'
lista = list(string)
tippel = tuple(string)

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
lista = ['A', 'B', 'C', 'D']
x = len(lista)
y = len(lista)-1

print(x, y)
```

```python
4 3
```

--

## sorted(lista)

--

Returnerar en sorterad lista, där elementen måste vara av samma typ

```python
lista = ['X', 'B', 'E', 'D']
x = sorted(lista)
print(x)
```

```python
print(sorted(['X', 'B', 'E', 'D']))
```

```python
['B', 'D', 'E', 'X']
```

--

## lista.append(x)

--

Lägger till elementet **x** i slutet av listan

```python
lista = ['A', 'B', 'C', 'D']
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
lista1 = ['A', 'B', 'C', 'D']
lista2 = [1, 2, 3]
lista1.extend(lista2)
print(lista1)
```

```python
['A', 'B', 'C', 'D', 1, 2, 3]
```

--

## lista.insert(i,x)

--

Infogar elementet **x** på plats **i**.

```python
lista = ['A', 'B', 'C', 'D']
lista.insert(2, 'X')
print(lista)
```

```python
['A', 'B', 'X', 'C', 'D']
```

--

## lista.remove(x)

--

Tar bort första elementet med värdet **x**

```python
lista = ['A', 'B', 'C', 'D', 'C']
lista.remove('C')
print(lista) 
```

```python
['A', 'B', 'D', 'C']
```

--

## lista.pop(i)

--

Tar bort elementet med index **i** och returnerar värdet. Om **i** utelämnas är standard (default) att sista värdet tas bort.

```python
lista = ['A', 'B', 'C', 'D']
lista.pop()
lista.pop(1)
print(lista) 
```

```python
['A', 'C']
```

--

## lista.index(x)

--

Returnerar index för första förekomst av element **x**.

```python
lista = ['A', 'B', 'C', 'D', 'C', 'C']
x = lista.index('C')
print(x)
```

```python
2
```

--

## lista.count(x)

--

Returnerar antalet element med värdet **x**.

```python
lista = ['A', 'B', 'C', 'D', 'C']
x = lista.count('C')
print(x)
```

```python
2
```

--

## lista.sort()

--

Sorterar listan på plats

```python
lista = ['E', 'B', 'A', 'D', 'C']
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
lista = ['A', 'B', 'C', 'D']
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
txt = 'Teknik'

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
tippel = tuple('Teknik')
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

Istället för hakparenteser används "måsvingar" { } och kolon när dictionariet definieras, men hakparenteser används så snart vi gör indexeringar i det:

---

# Skapa en ordbok

--

```python
skateboard = {
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

---

# Hämta ut data

--

```python
skateboard = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

x = skateboard["brand"]
print(x)
```

```python
Creature
```

--

```python
skateboard = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}
x = skateboard.get("brand")
print(x)
```

```python
Creature
```

--

```python
skateboard = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

x = skateboard.keys()
print(x)
```

```python
dict_keys(['brand', 'model', 'width', 'length'])
```

--

```python
skateboard = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

x = skateboard.values()
print(x)
```

```python
dict_values(['Creature', 'Martinez Calavera', 8.99, 32.64])
```

--

```python
skateboard = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

x = skateboard.items()
print(x)
```

```python
dict_items([('brand', 'Creature'), ('model', 'Martinez Calavera'), ('width', 8.99), ('length', 32.64)])
```

--

```python
skateboard = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}


if "model" in skateboard:
    print("Jo")
```

```python
Jo
```

---

# Ändra

--

```python
skateboard = {
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
skateboard = {
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
skateboard = {
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
skateboard = {
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
skateboard = {
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
skateboard = {
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
skateboard = {
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
skateboard = {
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
skateboard = {
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
skateboard = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

for x in skateboard:
    print(x)
```

```python
brand
model
width
length
```

--

```python
skateboard = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

for x in skateboard.keys():
    print(x)

```

```python
brand
model
width
length
```

--

```python
skateboard = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

for x in skateboard:
    y = skateboard[x]
    print(y)
```

```python
Creature
Martinez Calavera
8.99
32.64
```

--

```python
skateboard = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

for x in skateboard:
    y = skateboard.get(x)
    print(y)
```

```python
Creature
Martinez Calavera
8.99
32.64
```

--

```python
skateboard = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

for x in skateboard.values():
    print(x)
```

```python
Creature
Martinez Calavera
8.99
32.64
```

--

```python
skateboard = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

for key, value in skateboard.items():
    print(key, value, sep=": ")
```

```python
brand: Creature
model: Martinez Calavera
width: 8.99
length: 32.64
```

---

# Kopiera

--

```python
skateboard = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

kopia = skateboard.copy()
print(kopia)
```

```python
{'brand': 'Creature', 'model': 'Martinez Calavera', 'width': 8.99, 'length': 32.64}
```

--

```python
skateboard = {
  "brand": "Creature",
  "model": "Martinez Calavera",
  "width": 8.99,
  "length": 32.64
}

kopia = dict(skateboard)
print(kopia)
```

```python
{'brand': 'Creature', 'model': 'Martinez Calavera', 'width': 8.99, 'length': 32.64}
```

---

# Nästlade

--

```python
skateboards = {
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
skateboards = {
    "board1": {"brand": "Creature",
               "model": "Martinez Calavera",
               "width": 8.99,
               "length": 32.64},
    "board2": {"brand": "Prime Heritage",
               "model": "Dune Curb Crusher",
               "width": 8.25,
               "length": 31.75},
}

x = skateboards["board1"]
print(x)
```

```python
{'brand': 'Creature', 'model': 'Martinez Calavera', 'width': 8.99, 'length': 32.64}
```

--

```python
skateboards = {
    "board1": {"brand": "Creature",
               "model": "Martinez Calavera",
               "width": 8.99,
               "length": 32.64},
    "board2": {"brand": "Prime Heritage",
               "model": "Dune Curb Crusher",
               "width": 8.25,
               "length": 31.75},
}

x = skateboards["board1"]["model"]
print(x)
```

```python
Martinez Calavera
```

--

```python
skateboards = {
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
skateboards = {
    "board1": {"brand": "Creature",
               "model": "Martinez Calavera",
               "width": 8.99,
               "length": 32.64},
    "board2": {"brand": "Prime Heritage",
               "model": "Dune Curb Crusher",
               "width": 8.25,
               "length": 31.75},
}

skateboards["board3"] = {}
skateboards["board3"]["brand"] = "Tired"
skateboards["board3"]["model"] = "Logo Two on Chuck",
skateboards["board3"]["width"] =  8.625,
skateboards["board3"]["length"] = 32.00

print(skateboards)
```

```python
{'board1': {'brand': 'Creature', 'model': 'Martinez Calavera', 'width': 8.99, 'length': 32.64}, 'board2': {'brand': 'Prime Heritage', 'model': 'Dune Curb Crusher', 'width': 8.25, 'length': 31.75}, 'board3': {'brand': 'Tired', 'model': 'Logo Two on Chuck', 'width': 8.625, 'length': 32.0}}
```

--

```python
skateboards = {
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
skateboards = {
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
skateboards = {
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
skateboards = {
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
        print("   ", detail,": ", value)
    print('------------------')
```

--

```python
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