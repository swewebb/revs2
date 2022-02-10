# Python - Kapitel 9

---

# Introduktion

--

<span class="fragment">Hittills har vi skrivit all kod från scratch varje gång, men en bra programmerare
strukturerar upp sin kod för att få bitar som är återanvändbara</span>

<span class="fragment">Dessa återanvändbara kodsnuttar kallas för <b>funktioner</b></span>

<span class="fragment">Vi har redan använt oss av funktioner, t.ex. `len()`, `print()`, `int()`,
`range()`, osv.</span>

<span class="fragment">Nu ska vi göra egna funktioner</span>

---

# Exempel på en funktion


--


```python []
# Exempel på en funktion med två parametrar
def skriv_summa(x, y):
    summa = x + y
    print('Summan är:', summa)

# Huvudprogram
a = 3
b = 4
skriv_summa(a, b)
```

```html
Summan är: 7
```

--

<span class="fragment">En funktion skapas genom att man definierar (**dfn**) den med **namn**, **parametrar** inom parentes, och **kolon**.</span>

<span class="fragment">Det följande programblocket (indenterat precis som vanligt efter ett kolon) tillhör funktionen.</span>

<span class="fragment">Sedan skriver vi vårt huvudprogram precis som vanligt, och anropar där vår nya funktion med argument.</span>

--

## Vad händer i anropet?

<span class="fragment">Parametrarna **x**, **y** och variabeln **summa** är lokala i funktionen och kan inte ses utanför funktionen.</span>

<span class="fragment">Värdet av argumenten i funktionsanropet kopieras till parametrarna.</span>

<span class="fragment">Funktionen exekveras.</span>

<span class="fragment">När anropet avslutats fortsätter programmet efter funktionsanropet.</span>

---

# Defaultvärden på parametrarna

--

```python []
# Exempel på en funktion med två parametrar
def skriv_summa(x, y = 1):
    summa = x + y
    print('Summan är:', summa)

# Huvudprogram
a = 3
b = 4

skriv_summa(a, b)
skriv_summa(b)
```

```html []
Summan är: 7
Summan är: 5
```

--

<span class="fragment">Det finns ibland anledning att utlämna vissa parametrar som oftast antar ett specifikt värde.</span>

<span class="fragment">Den möjligheten kan man ange i parameterlistan genom att sätta ett visst default-värde på en parameter.</span>

<span class="fragment">De parametrar som kan ha default-värde **måste ligga längst till höger i listan**, annars vet inte Pyhton vilken man har angett och vilka som ska få default-värden.</span>

---

# Funktioner som returnerar värden

--

```python []
# Exempel på en funktion som returnerar ett värde
def medelvarde(x, y):
    medel = (x + y ) / 2
    return medel

# Huvudprogram
a = 3
b = 4
m = medelvarde(a, b)

print('Medelvärdet är:', m)
```

```html []
Medelvärdet är: 3.5
```

--

Väldigt vanligt är att vi vill ha tillbaka något från funktionsanropet, dvs att det skall returnera något värde.

Detta gör vi med **return**, och värdet "förs över" till utanför funktionsanropet och sparas lokalt.

--

```python []
# Exempel på en funktion som returnerar ett värde
def medelvarde(x, y):
    """Returnerar medelvärdet av parametrarna x och y"""
    medel = (x + y ) / 2
    return medel

# Huvudprogram
a = 3
b = 4
m = medelvarde(a, b)

#print('Medelvärdet är:', m)

help(medelvarde)
```

--


```html []
medelvarde(x, y)
    Returnerar medelvärdet av parametrarna x och y
```

--

```python []
# Exempel på en funktion som returnerar ett värde
def medelvarde(x, y):
    """Returnerar medelvärdet av parametrarna x och y"""
    return (x + y ) / 2

# Huvudprogram
a = 3
b = 4
m = medelvarde(a, b)

print('Medelvärdet är:', m)
```

---

# Mer om globalt och lokalt

--

<span class="fragment">Argumentvärden som skickas in till funktioner kopieras till minnesstacken och är synliga endast inne i funktionerna.</span>

<span class="fragment">När funktionen avslutas frigörs minnet.</span>

<span class="fragment">Variabler som definieras utanför alla funktioner är dock globala, och syns överallt så länge ingen lokal variabel har samma namn och "skymmer sikten".</span>

--

```python []
b = 6

def leppard():
    b = 10
    print(b)

print(b)
leppard()
print(b)
```

```html []
6
10
6
```

--

```python []
b = 6

def leppard():
    global b
    b = 10
    print(b)

print(b)
leppard()
print(b)
```

```html
6
10
10
```

Vill man tilldela en **global variabel** inne i en funktion måste man deklarera den som **global**.

---

# Import av moduler

--

<span class="fragment">Python distribueras med en stor mängd färdigskrivna funktioner och definierade konstanter.</span>

<span class="fragment">Dessa finns samlade i moduler som kan läggas till efter eget behag med hjälp av instruktionen `import`.</span>

<span class="fragment">Exempelvis ligger en massa matematiska funktioner och konstanter i modulen **math.py**.</span>

<span class="fragment">Vid importen skriver man dock endast `import math`.</span>

<span class="fragment">Vid användning skriver man **modulnamn.funktionsnamn**.</span>

--

```python []
import math

pi = math.pi
sq = math.sqrt(2)
sin = math.sin(math.pi / 2)

print(pi, sq, sin)
```

--

```python []
from math import *

pi = pi
sq = sqrt(2)
sin = sin(pi / 2)

print(pi, sq, sin)
```

--

```python []
from math import pi, sqrt, sin

pi = pi
sq = sqrt(2)
sin = sin(pi / 2)

print(pi, sq, sin)
```

--

```python []
import math

for method in dir(math):
    print(method)
```

```html
__doc__ __loader__ __name__ __package__ __spec__ acos acosh
asin asinh atan atan2 atanh ceil comb copysign cos cosh
degrees dist e erf erfc exp expm1 fabs factorial floor fmod
frexp fsum gamma gcd hypot inf isclose isfinite isinf isnan
isqrt ldexp lgamma log log10 log1p log2 modf nan perm pi pow
prod radians remainder sin sinh sqrt tan tanh tau trunc
```

--

```python []
import math

help(math)
```

```html []
NAME
    math

DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.

    acosh(x, /)
        Return the inverse hyperbolic cosine of x.
```

---

# Docstring

--

```python []
"""Förklarande text om vad funktionen gör

Args:
    kaka (float): Beskrivande text
    bulle (int): Beskrivande text (default is 10)

Returns:
    fika (list): Beskrivande text
"""
```

Vi skriver givetvis docstring:en på engelska

---

# SLUT
