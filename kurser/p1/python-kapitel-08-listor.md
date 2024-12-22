# Python - Kapitel 8 - Listor

---

# Listor

En lista är helt enkelt en ordnad samling element som var och en kan identifieras med ett nummer inom hakparenteser, ett index, precis som i en sträng.

Strängar (som vi arbetat med) är oföränderliga, men det gäller inte listor.

Vi kan lägga till element, ta bort, ändra, osv…

---

# Skapa en lista

--

```python []
number_list = [1, 2, 4, 8, 16, 32, 64, 128, 256]
mixed_list = ["Frukt", 1,"Lakrits", 2, False]

print(number_list, mixed_list, sep="\n")
```

```python []
[1, 2, 4, 8, 16, 32, 64, 128, 256]
["Frukt", 1, "Lakrits", 2, False]
```

En lista skapas med hakparenteser **[ ]**.

---

# Hämta ut ett värde ur en lista

--

```python []
number_list = [1, 2, 4, 8, 16, 32, 64, 128, 256]

print(number_list[1])
```

```python []
2
```

Indexeringen börjar på **0** och slutar på **längden-1**

--

```python []
number_list = [1, 2, 4, 8, 16, 32, 64, 128, 256]

print(number_list[-1])
```

```python []
256
```

--

```python []
number_list = [1, 2, 4, 8, 16, 32, 64, 128, 256]

print(number_list[15])
```

```python []
Traceback (most recent call last):
  File "c:/git/P1/ex1.py", line 3, in <module>
    print(number_list[15])
IndexError: list index out of range
```

--

```python []
number_list = [1, 2, 4, 8, 16, 32, 64, 128, 256]

print(number_list[:4])
```

```python[]
[1, 2, 4, 8]
```

Skriver ut de fyra första elementen i listan (0 - 3)

--

```python []
number_list = [1, 2, 4, 8, 16, 32, 64, 128, 256]

print(number_list[4:])
```

```python []
[16, 32, 64, 128, 256]
```

Skriver ut alla element från index 4 och framåt

--

```python []
number_list = [1, 2, 4, 8, 16, 32, 64, 128, 256]

print(number_list[3:6])
```

```python []
[8, 16, 32]
```

Skriver ut alla element från index 3 (inklusive) till index 6 (exklusive).

---

# Lägga till i en lista

--

## Lägga till i slutet

```python [2]
numbers = [1, 2, 3, 4]
numbers.append(50)

print(numbers)
```

```python []
[1, 2, 3, 4, 5]
```

Lägger till heltalet **50** i slutet av listan

--

## Lägga till på en specifik plats

```python [2]
numbers = [1, 2, 4]
numbers.insert(2, 3)

print(numbers)
```

```python []
[1, 2, 3, 4]
```

Lägger till heltalet **3** på indexposition **2** (den tredje positionen) i listan.

Alla element från index 2 och framåt flyttas ett steg åt höger för att ge plats åt det nya värdet.

---

# Radera i en lista

--

## Radera ett värde (1)

```python [2]
numbers = [1, 2, 3, 4]
numbers.pop()

print(numbers)
```

```python []
[1, 2, 3]
```

Metoden **.pop()** tar bort det sista elementet i listan.

--

## Radera ett värde (2)

```python [2]
numbers = [1, 2, 3, 4]
numbers.pop(2)

print(numbers)
```

```python []
[1, 2, 4]
```

Metoden **.pop(2)** tar bort elementet vid index **2** (det tredje elementet i listan), vilket är 3 i detta fall.

--

## Radera ett värde (3)

```python [2]
numbers = [1, 2, 3, 4]
numbers.pop(-2)

print(numbers)
```

```python []
[1, 2, 4]
```

Metoden **.pop(-2)** tar bort elementet vid index **-2**, vilket innebär det näst sista elementet i listan.

--

## Radera första förekomsten

```python [2]
names = ["kalle", "lotta", "
", "ada", "lotta"]
names.remove("lotta")

print(names)
```

```python []
["kalle", "kålle", "ada", "lotta"]
```

Tar bort första elementet med värdet **x**

--

## Rensa en lista

```python [2]
names = ["kalle", "lotta", "kålle", "ada", "lotta"]
names.clear()

print(names)
```

```python []
[]
```

Listan kommer att finnas kvar, men den är nu tom.

--

## Radera en hel lista

```python [2]
names = ["kalle", "lotta", "kålle", "ada", "lotta"]
del names

print(names)
```

```python []
Traceback (most recent call last):
  File "c:\git\p1\ex.py", line 4, in <module>
    print(names)
          ^^^^^
NameError: name "names" is not defined
```

Listan kommer att raderas helt och hållet.

---

# Räkna i en lista

--

## Längden på en lista

```python [3]
names = ["kalle", "lotta", "kålle", "ada"]

number_of_names = len(names)

print(number_of_names)
```

```python []
4
```

--

## Antal element med ett visst värde

```python [3]
names = ["kalle", "lotta", "kålle", "ada", "lotta", "lotta"]

number_of_name = names.count("lotta")

print(number_of_name)
```

```python []
3
```

Returnerar antalet element med värdet **x**.

---

# Sortera en lista

--

## Sortera till en ny lista

```python [2]
lista = ["kalle", "lotta", "kålle", "ada"]
sorterad = sorted(lista)
print(sorterad)
```

```python []
["ada", "kalle", "kålle", "lotta"]
```

Returnerar en sorterad lista.

Elementen måste vara av samma typ.

--

## Sortera på plats

```python [2]
numbers = [12, 7, 17, 29, 2]
numbers.sort()

print(numbers)
```

```python []
[2, 7, 12, 17, 29]
```

--

```python [2]
names = ["kalle", "lotta", "kålle", "ada", "lotta"]
names.sort()

print(names)
```

```python []
["ada", "kalle", "kålle", "lotta", "lotta"]
```

--

```python [2]
mixed = [12, "kalle", "ada", 42]
mixed.sort()

print(mixed)
```

```python []
Traceback (most recent call last):
  File "c:\git\P1\ex.py", line 10, in <module>
    mixed.sort()
TypeError: "<" not supported between instances of "str" and "int"
```

--

```python [2]
numbers = [12, 7, 17, 29, 2]
numbers.sort(reverse = True)

print(numbers)
```

```python []
[29, 17, 12, 7, 2]
```

Fungerar även på listor med strängar.

--

```python []
names = ["kalle", "lotta", "Kålle", "ada", "lotta"]
names.sort()

print(names)
```

```python []
["Kålle", "ada", "kalle", "lotta", "lotta"]
```

**sort()** sorterar först på stora bokstäver och sedan små.

--

```python [2]
names = ["kalle", "lotta", "Kålle", "ada", "lotta"]
names.sort(key = str.lower)

print(names)
```

```python []
["ada", "kalle", "Kålle", "lotta", "lotta"]
```

---

# Vända en lista

--

```python [2]
names = ["kalle", "lotta", "Kålle", "ada", "lotta"]
names.reverse()

print(names)
```

```python []
["lotta", "ada", "Kålle", "lotta", "kalle"]
```

---

# Loopa ut en lista

--

## While

```python [3-7]
names = ["kalle", "lotta","ada"]

i = 0

while i < len(names):
  print(names[i])
  i += 1
```

```python []
kalle
lotta
ada
```

--

Variabeln **i** är satt till **0** från början och fungerar som en räknare som håller reda på den aktuella positionen i listan.

Inuti loopen ökar **i** med **1** för att kunna hämta nästa element i listan.

--

## For

```python [3-4]
names = ["kalle", "lotta","ada"]

for name in names:
  print(name)
```

```python []
kalle
lotta
ada
```

--

```python [3-4]
names = ["kalle", "lotta","ada"]

for i in range(len(names)):
  print(f"{i}: {names[i]}")
```

```python []
0: kalle
1: lotta
2: ada
```

---

# Kopiera en lista

--

```python [1-5]
names = ["Kalle"]
new_names = names

names.append("Marie")
newc_names.append("Elina")

print(names, new_names, sep="\n")
```

```python []
["Kalle", "Marie", "Elin"]
["Kalle", "Marie", "Elin"]
```

Aj då! Det här blev ingen kopia.

--

```python [2]
names = ["Kalle"]
new_names = names.copy()

names.append("Marie")
new_names.append("Elina")

print(names, new_names, sep="\n")
```

```python []
["Kalle", "Marie"]
["Kalle", "Elina"]
```

--

```python [2]
names = ["Kalle"]
new_names = [el for el in names]

names.append("Marie")
new_names.append("Elina")

print(names, new_names, sep="\n")
```

```python []
["Kalle", "Marie"]
["Kalle", "Elina"]
```

--

```python [2]
names = ["Kalle"]
new_names = names[:]

names.append("Marie")
new_names.append("Elina")

print(names, new_names, sep="\n")
```

```python []
["Kalle", "Marie"]
["Kalle", "Elina"]
```

--

```python [2]
names = ["Kalle", "Lisa"]
new_names = names[::-1]

names.append("Marie")
new_names.append("Elina")

print(names, new_names, sep="\n")
```

```python []
["Kalle", "Lisa", "Marie"]
["Lisa", "Kalle", "Elina"]
```

---

# Slå samman listor

--

```python [1-3]
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
b.append(a)

print(b)
```

```python []
[6, 7, 8, 9, 10, [1, 2, 3, 4, 5]]
```

Aj då! Det blev ju inte bra...

--

```python [3]
a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = a + b

print(c)
```

```python []
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

--

```python [3]
a = [1,2,3,4,5]
b = [6,7,8,9,10]
a.extend(b)

print(a)
```

```python []
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

# index()

--

```python []
names = ['kalle', 'lotta', 'kålle', 'ada', 'lotta']
x = names.index('ada')

print(x)
```

```python []
3
```

Returnerar **index** för första förekomst av element **x**

---

# Min- och max i en lista

--

```python []
numbers = [3, 6,1, 8, 10, 7]

# Antagande att första talet i listan är minst
xmin = numbers[0]

# Antagande att första talet i listan är störst
xmax = numbers[0]

# Hitta min och max
for number in numbers:
    # Om aktuellt nummer är mindre än xmin,
    # sätt xmin till aktuellt nummer
    if number < xmin:
        xmin = number

    # Om aktuellt nummer är större än xmax,
    # sätt xmax till aktuellt nummer
    if number > xmax:
        xmax = number

print(f'Minst: {xmin}, Max: {xmax}')
```

--

```python [3-4]
numbers = [3, 6,1, 8, 10, 7]

xmin = min(numbers)
xmax = max(numbers)

print(f'Minst: {xmin}, Max: {xmax}')

```

--

```python [3]
numbers = [3, 6,1, 8, 10, 7]

print(f'Minst: {min(numbers)}, Max: {max(numbers)}')
```

---

# Ett par exempel

--

## Använda en for-loop till inputs

```python []
numbers = []

number_of_inputs = int(input("Ange antal tal du vill lägga till: "))

for i in range(number_of_inputs):
  number = float(input(f"Ange tal {i + 1}: "))
  numbers.append(number)

print(numbers)
```

--

```python []
numbers = []

for i in range(int(input("Ange antal tal du vill lägga till: "))):
   numbers.append(float(input(f"Ange tal {i + 1}: ")))

print(numbers)
```

--

```python []
numbers = [float(input(f"Ange tal {i + 1}: ")) for i in range(int(input("Ange antal tal du vill lägga till: ")))]

print(numbers)
```

--

## Använda en while-loop för _n_ antal inputs

```python []
numbers = []
i = 0

print("Mata in talen i serien. Avsluta inmatningen med Enter")

while True:
    number = input(f"Ange tal {i + 1} : ")

    # Avsluta loopen om användaren trycker på Enter
    if number == "":
        break

    # Kontrollera om inmatningen är ett giltigt tal
    if number.replace('.', '', 1).replace('-', '', 1).isdigit():
        # Omvandlar till float och lägger till i listan
        numbers.append(float(number))
        i += 1
    else:
        print("Ogiltig inmatning, ange ett giltigt tal.")

print("Inmatade tal:", numbers)
```

--

## Förklaring

**isdigit()** är en inbyggd metod i Python som används för att kontrollera om alla tecken i en sträng är siffror.

Om strängen bara innehåller siffror (0 till 9), returnerar metoden **True** annars returnerar den **False**.

Observera att **isdigit()** fungerar endast för heltal utan några andra symboler (som punkter, minustecken eller mellanslag).

--

```python []
number.replace('.', '', 1).replace('-', '', 1).isdigit()
```

**.replace('.', '', 1)** tar bort en eventuell punkt en gång (för decimaler).

**.replace('-', '', 1)** tar bort ett eventuellt minustecken en gång (för negativa tal).

Om det nu är ett heltal, vilket testas med **isdigit()** är villkoret sant.

---

# Slut!
