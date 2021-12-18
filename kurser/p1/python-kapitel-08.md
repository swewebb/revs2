# Python - Kapitel 8

---

# Listor

En lista är helt enkelt en ordnad samling element som var och en kan identifieras med ett nummer inom hakparenteser, ett index, precis som i en sträng.

---

# Exempel på listor

--

```python
tal = [1, 2, 4, 8, 16, 32, 64, 128, 256]
```

Numreringen börjar på 0 och slutar på längden-1

--

```python
gottOchBlandat = ['Frukt', 1,'Lakrits', 2, False]
```

Elementen behöver inte heller vara av samma typ

--

```python
tal = [1, 2, 4, 8, 16, 32, 64, 128, 256]

print(tal)
```

```python
[1, 2, 4, 8, 16, 32, 64, 128, 256]
```

--

```python
tal = [1, 2, 4, 8, 16, 32, 64, 128, 256]

print(tal[1])
```

```python
2
```

--

```python
tal = [1, 2, 4, 8, 16, 32, 64, 128, 256]

print(tal[15])
```

```python
Traceback (most recent call last):
  File "c:/Users/elev/git/P1/chapter-08/exempel/ex1.py", line 7, in <module>
    print(tal[15])
IndexError: list index out of range
```

--

```python
gottOchBlandat = ['Frukt', 1,'Lakrits', 2, False]

print(gottOchBlandat[-1])
```


```python
False
```

---

# Listor av listor

--

Kallas ofta för **matriser**. Representerar ofta 2-dim. data.

Listorna i listan kan vara av olika längd

Indexeras med dubbla hakparenteser

--

```python
matrix = [[1, 2, 3], [4 ,5, 6], [7, 8, 9, 10]]

print(matrix[1])
```

```python
[4, 5, 6]
```

--

```python
matrix = [[1, 2, 3], [4 ,5, 6], [7, 8, 9, 10]]

print(matrix[1][0])
```

```python
4
```

--

```python
tictactoe = [['X',' ','O'],[' ','X','O'],[' ','O','X']]

for row in tictactoe:
    print(row)
```

```
['X', ' ', 'O']
[' ', 'X', 'O']
[' ', 'O', 'X']
```

---

# Listor är föränderliga

--

Strängar är oföränderliga, men det gäller inte listor

Vi kan lägga till element, ta bort, ändra, osv…

--

## Lägga till i slutet

```python
lista = [1, 2, 3, 4]
lista.append(5)

print(lista)
```

```python
[1, 2, 3, 4, 5]
```

--

## Ändra ett värde

```python
lista = [1, 2, 3, 4]
lista[2] = 3.14

print(lista)
```

```python
[1, 2, 3.14, 4, 5]
```

--

## Radera ett värde (1)

```python
lista = [1, 2, 3, 4]
lista.pop(2)

print(lista)
```

```python
[1, 2, 4]
```

--

## Radera ett värde (2)

```python
lista = [1, 2, 3, 4]
lista.pop(-1)

print(lista)
```

```python
[1, 2, 3]
```

--

## Lägga till på en specifik plats

```python
lista = [1, 2, 4]
lista.insert(2, 3)

print(lista)
```

```python
[1, 2, 3, 4]
```

---

# Loopa igenom listor

--

# For

```python
mylist = [5, 6,8 ,9, 10, 2.58, 8.19]
product = 1;

for i in mylist:
    product *= i

print(product)
print('{:.2f}'.format(product))
```

```python
456412.31999999995
456412.32
```

--

## While

```python
mylist = [5, 6, 8, 9, 10, 2.58, 8.19]
product = 1
i = 0

while i < len(mylist):
    product *= mylist[i]
    i += 1

print(product)
print(f'{product:.2f}')
```

```python
456412.31999999995
456412.32
```

---

# Skapa en lista av en sträng

--

```python
mening = input("Skriv en mening: ")
lista = list(mening)

print(lista)
```

```python
Skriv en mening: Teknik är bäst
['T', 'e', 'k', 'n', 'i', 'k', ' ', 'ä', 'r', ' ', 'b', 'ä', 's', 't']
```

--

```python
mening = input("Skriv en mening: ")
lista = list(mening)

while True:
    siffra = input('Ange index på bokstaven du vill ändra (return avslutar):')

    if not siffra:
        break
    elif int(siffra) < 0 or int(siffra) > len(mening) - 1:
        print("Felaktig inmatning. Försök igen!")
    else:
        lista[int(siffra)] = input("Skriv ny bokstav för index " + siffra + ": ")

print("Din mening är nu: " + ''.join(lista))
```

--

```html
Skriv en mening: Pelle
Ange index på bokstaven du vill ändra (return avslutar):
Din mening är nu: Pelle
```

```html
Skriv en mening: Pälle
Ange index på bokstaven du vill ändra (return avslutar):1
Skriv ny bokstav för index 1: e
Ange index på bokstaven du vill ändra (return avslutar):
Din mening är nu: Pelle
```

---

# Initiera en lista

--

```python
list = [0] * 15

print(list)
```

```python
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

```python
list = [0 for i in range(15)]
print(list)
```

```python
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

---

# Mata in i en lista

--

```python
tal = []

for i in range(1,6):
    tal.append(float(input('Ange tal ' + str(i) + ' : ')))

print('Dina inmatade tal:')

for j in tal:
    print(j)
```

```python
Ange tal 1 : 5
Ange tal 2 : 5.5
Ange tal 3 : 6.6
Ange tal 4 : 7
Ange tal 5 : 8
Dina inmatade tal:
5.0
5.5
6.6
7.0
8.0
```

---

# Största och minsta talet

--

```python
tal = []

for i in range(1,6):
    tal.append(float(input('Ange tal ' + str(i) + ' : ')))

xmin = tal[0]
xmax = tal[0]

# Hitta min och max
for i in range(1, len(tal)):
    if tal[i] < xmin:
        xmin = tal[i]
    elif tal[i] > xmax:
        xmax = tal[i]

print('Minsta och största talen är {}, {}'.format(xmin,xmax))
```

```python
Ange tal 1 : 4
Ange tal 2 : 5
Ange tal 3 : 9
Ange tal 4 : 2
Ange tal 5 : 1
Minsta och största talen är 1.0, 9.0
```

--

```python
tal = []

for i in range(1,6):
    tal.append(float(input('Ange tal ' + str(i) + ' : ')))

xmin = min(tal)
xmax = max(tal)

print('xmin =', xmin)
print('xmax =', xmax)
```

```python
Ange tal 1 : 5
Ange tal 2 : 6
Ange tal 3 : 7
Ange tal 4 : 1
Ange tal 5 : 9
xmin = 1.0
xmax = 9.0
```

---

# Tipplar/Tuplar

--

En tupel består av följd (0 eller flera) av element. Elementen kan t.ex. vara heltal, flyttal, strängar, tupler och listor.

Den väsentliga skillnaden mot listor är att tupel-objekt inte går att ändra (eng. **immutable**).

Definieras m.h.a vanliga parenteser istället för hakparenteser

--

## Lista

```python
lista = [1, 2, 3]
print(lista[1])

lista.append(4)
print(lista)
```

```python
2
[1, 2, 3, 4]
```

--

## Tuplar

```python
tippel = (1, 2, 3)

print(tippel)
print(tippel[1])
```

```python
(1, 2, 3)
2
```

--

```python
tippel = (1, 2, 3)
tippel.append(4)
```

```python
Traceback (most recent call last):
  File "c:/Users/elev/git/P1/chapter-08/exempel/ex9.py", line 17, in <module>
    tippel.append(4)
AttributeError: 'tuple' object has no attribute 'append'
```

---

# Packa och packa upp värden med tipplar

--

## Packa ihop

```python
multiple = 1, 2, 3, 4, 5

print(multiple)
```

```python
(1, 2, 3, 4, 5)
```

--

## Packa upp

```python
multiple = 1, 2, 3, 4, 5

ett, två, tre, fyra, fem = multiple
print(fyra)
```

```python
4
```

--

```python
multiple = 1, 2, 3, 4, 5

ett, två, tre = tre, två, ett

print(ett)
print(två)
print(tre)
```

```python
3
2
1
```

---

# Listor vs tupler

--

```python
from timeit import timeit

listTime = timeit(stmt='[1,2,3,4,5,6,7,8,9,10]', number=1000000)
tupleTime = timeit(stmt='(1,2,3,4,5,6,7,8,9,10)', number=1000000)

print(listTime)  # 0.0597786
print(tupleTime) # 0.007808499999999996
```

--

```python
listan = ['Kålle', 'Ada', 'Kalle', 'Lotta', 'Nicko', 'Pulver', 'Humle', 'Dumle']
tupler = ('Kålle', 'Ada', 'Kalle', 'Lotta', 'Nicko', 'Pulver', 'Humle', 'Dumle')

print('listan=',listan.__sizeof__())
print('tupler=',tupler.__sizeof__())
```

```python
listan= 52
tupler= 44
```

---

# Allt i Python är referenser

--

Som vi sett tidigare är varje variabel i Python en form av referens till en minnesplats där variabelns värde ligger.

När vi sedan ändrar variabelns värde skapas en annan minnesplats där värdet läggs och referensen ändras till den nya platsen.

Detta möjliggör den dynamiska typningen som är kännetecknande för Python.

--

Vi kanske inte märker så mycket av detta så länge vi arbetar med oföränderliga datatyper, men med listor blir det annorlunda.
En lista i Python är en lång rad med referenser till olika data.

(Data som inte längre används rensar Python bort själv, s.k. **garbage collection**.  Vi kan rensa själva med kommandot `del`)

--

## Ändrar i samma lista

```python
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = lista1
lista1.append(10)
lista2.append(11)

print('Lista1 = ', end='')
print(lista1)
print('Lista2 = ', end='')
print(lista2)
```

```python
Lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
```

--

# Kopia av en lista

```python
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [x for x in lista1] # list comprehension
lista2.append(11)

print('Lista1 = ', end='')
print(lista1)
print('Lista2 = ', end='')
print(lista2)
```

```python
Lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
```

--

```python
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = lista1[:]
lista2.append(11)

print('Lista1 = ', end='')
print(lista1)
print('Lista2 = ', end='')
print(lista2)
```

```python
Lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
```

--

```python
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = lista1[::-1]

print('Lista1 = ', end='')
print(lista1)
print('Lista2 = ', end='')
print(lista2)
```

```python
Lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Lista2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

--

## Slå ihop listor

```python
a = [1,2,3,4,5]
b = [6,7,8,9,10]
b.append(a)

print(b)
```

```python
[6, 7, 8, 9, 10, [1, 2, 3, 4, 5]]
```

Hoppsan!

--

```python
a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = a + b

print(c)
```

```python
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

--

```python
a = [1,2,3,4,5]
b = [6,7,8,9,10]
a.extend(b)

print(a)
```

```python
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

--

## "List comprehensions"

```python
factors = [1, 2, 3, 4, 5]
squares = []
cubics = []

for f in factors:
    squares.append(f**2)
    cubics.append(f**3)

for i in range(len(factors)):
    print(factors[i], squares[i], cubics[i])
```

--

```python
factors = [1, 2, 3, 4, 5]
squares = [factor**2 for factor in factors]
cubics = [factor**3 for factor in factors]

for i in range(0,len(factors)):
    print(factors[i], squares[i], cubics[i])
```

```html
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
```

--

```python
factors = [1,2,3,4,5]
squares = [factor**2 for factor in factors]
cubics = [factor**3 for factor in factors]

for i in range(0,len(factors)):
    f = str(factors[i]).rjust(4)
    s = str(squares[i]).rjust(4)
    c = str(cubics[i]).rjust(4)
    print(f, s, c)
```

```html
   1    1    1
   2    4    8
   3    9   27
   4   16   64
   5   25  125
```

--

```python
numbers = list(range(1,21))
odd = []
even = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)
```

--

```python
numbers = list(range(1,21))
even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 == 1]

print(even)
print(odd)
```

```python
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

---

# Listmetoder och listfunktioner

--

## len()

```python
lista = ['kalle', 'lotta', 'kålle', 'ada']

längd = len(lista)
print(längd)
print(lista[längd - 1])
```

```python
4
ada
```

Längden av listan.

--

## sorted()

```python
lista = ['kalle', 'lotta', 'kålle', 'ada']
sorterad = sorted(lista)
```

```python
print(sorterad)
['ada', 'kalle', 'kålle', 'lotta']
```

Returnerar en sorterad lista, där elementen måste vara av samma typ

--

```python
lista = ['kalle', 'lotta', 'kålle', 'ada']
sorterad = sorted(lista)
fallande = sorterad[::-1]
```

```python
print(fallande)
['lotta', 'kålle', 'kalle', 'ada']
```

--

## .append()

```python
listan = ['a','b','c', 'd']
listan.append('e')

print(listan)
```

```python
['a', 'b', 'c', 'd', 'e']
```

Lägger till elementet x i slutet av listan

--

## .extend()

```python
list1 = ['a','b','c']
list2 = [1, 2, 3]
list1.extend(list2)

print(list1)
print(list2)
```

```python
['a', 'b', 'c', 1, 2, 3]
[1, 2, 3]
```

Förlänger listan med en annan lista (jfr +-operatorn)

--

## .insert()

```python
listan = ['a','b','c']
x=1
listan.insert(1, x)

print(listan)
```

```python
['a', 1, 'b', 'c']
```

Infogar elementet **x** på plats **i**.

--

## .remove()

```python
lista = ['kalle', 'lotta', 'kålle', 'ada', 'lotta']
lista.remove('lotta')

print(lista)
```

```python
['kalle', 'kålle', 'ada', 'lotta']
```

Tar bort första elementet med värdet **x**

--

## .pop()

```python
listan = ['a','b','c']
listan.pop()

print(listan)
```

```python
['a', 'b']
```

Tar bort elementet med index **i** och returnerar värdet. Om **i** utelämnas är default att sista värdet tas bort.

--

## .index()

```python
lista = ['kalle', 'lotta', 'kålle', 'ada', 'lotta']
x = lista.index('ada')

print(x)
```

```python
3
```

Returnerar index för första förekomst av element **x**

--

## .count()

```python
lista = ['kalle', 'lotta', 'kålle', 'ada', 'lotta', 'lotta']
x = lista.count('lotta')

print(x)
```

```python
3
```

Returnerar antalet element med värdet **x**.

--

## .sort()

```python
lista = ['kalle', 'lotta', 'kålle', 'ada', 'lotta', 'lotta']
lista.sort()

print(lista)
```

```python
['ada', 'kalle', 'kålle', 'lotta', 'lotta', 'lotta']
```

Sorterar listan på plats

--

## .reverse()

```python
lista = ['kalle', 'lotta', 'kålle', 'ada', 'lotta', 'lotta']
lista.reverse()

print(lista)
```

```python
['lotta', 'lotta', 'ada', 'kålle', 'lotta', 'kalle']
```

Vänder på ordningen av elementen i listan.

--

## .join

```python
lista = ['kalle', 'lotta', 'kålle', 'ada']
x = ", ".join(lista)

print(x)
```

```python
kalle, lotta, kålle, ada
```

---

# SLUT!

