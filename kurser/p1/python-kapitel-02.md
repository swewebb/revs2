# Python - Kapitel 2

---

# Utskrift

--

Utskrift görs med `print(…) `

```python [ ]
print('Hello World')

Hello World
```

Kommandon i Python är **case sensitive**

---

# Variabler

--

All programmering använder variabler, ungefär som vi använder x och y i ekvationer i matematiken

--

I matematiken: om **x** är **4** så är verkligen **x = 4**. 

--

I programmering är variabeln **x** istället en referens – en form av pekare till en specifik minnesadress – som råkar ha värdet 4.

--

Vi tilldelar variabler värden genom "lika med"-tecknet med värdet på höger sida och variabelnamnet till vänster

Variablerna deklareras i och med att vi börjar använda dem

--

```python [ ]
a = 17
b = 3
print(a + b)
20
```

--

```python [ ]
a = 17
b = 3
b = 10
print(a + b)
27
```

--

```python [ ]
a = 17
b = 3
c = a + b
print(c)
20
```

--

## Variabelnamn

Variabler får kallas vad som helst, men får inte innehålla några aritmetiska operatorer och inte heller bestå av reserverade ord (reserverade ord kan ingå i namnet) och inte börja på siffror

Variabelnamn får innehåll å, ä, ö. Men det är snyggast att undvika och använda svengelska uttryck.

---

# Aritmetiska operatorer

--

Addition, subtraktion, multiplikation, division

Parenteser: ()

Prioritetsregler: (), **, *, /, %, + -

--

```python [ ]
print(3+5)
8
print(3 + 2 * 2)
7
```

---

# Andra aritmetiska operatorer i Python

--

## Modulo-operatorn

Modulo-operatorn, ger resten vid division: %

```python [ ]
print(15 % 4)
3
print(12 % 4)
0
```

--

## Heltalsdivision

Heltalsdivision, ger "hela" antalet ggr som nämnaren ryms i täljaren: //

**Observera:** //-operatorn avrundas nedåt, ger lite olika effekt för positiva och negativa tal

```python [ ]
print(21 // 8)
2

print(21 // -8)
-3
```

--

## Exponentierings-operatorn

Exponentierings-operatorn, ger vanliga "upphöjt i": **

```python [ ]
print(10**3)
1000
```

```python [ ]
print(2**3)
8
```

---

# Heltal

--

Heltal representeras normalt med 2, 4 eller 8 bytes i datorns minne. 

Med 8 byte kan vi representera heltal upp till 2^64-1. 

Python tar dock mer minne om det behövs (gränsen sätts vid internminnets storlek)

--

```python [ ]
print(2 ** 64 - 1)
18446744073709551615

print(2 ** 128 - 1)
340282366920938463463374607431768211455
```

---

## Flyttal

--

Flyttal kodas i minnet som en exponentdel och mantissa, ungefär som mycket stora eller små tal visas på en räknare. 

--

Python har inte statisk typkontroll, vilket gör att vi inte behöver ange vilken typ av tal vi arbetar med innan vi börjar göra operationer. 

I andra språk behöver man explicit typa sina variabler, så icke i Python

Aritmetiska operationer kan blanda flyttal och heltal, men svaret blir då ett flyttal (ett flyttal som råkar vara ett heltal anges med en decimalnolla)

--

```python [ ]
print(1.283456789E12)
1283456789000.0

print(0.0000000000123456789)
1.23456789e-11

print(6 + 4 * 0.5)
8.0
```

---

# Omvandling

--

Emellanåt vill man omvandla heltal till flyttal och tvärtom. Då finns inbyggda funktioner att tillgå.

--

**`float(x)`** omvandlar heltalet **x** till ett flyttal

```python [ ]
float(4)
4.0

a = float(4)
print(a)
4.0

a = 5
print(a)
5

a = 6.0
print(a)
6.0
```

--

**`int(x)`** omvandlar flyttalet **x** till ett heltal via trunkering (decimalerna skärs bort, helt enkelt – trunkering används också vid heltalsdivision)

```python [ ]
a = 6.2
print(a)
6.2

int(a)
6

print(a)
6.2

a = int(a)
print(a)
6
```

--

En variabels värde kan ändras genom tilldelning eller olika operationer, ofta med förkortat skrivsätt **+=**, **-=**, **\**=**, ...

```python [ ]
x = 5
x += 2
print(x)
7

x *=2
print(x)
14

x = 8
x **= 2
print(x)
64
```

---

# Teckensträngar

--

Teckensträngar är en följd av tecken, och anges i Python av citationstecken

Det är okej med enkla eller dubbla citationstecken

--

```python [ ]
print("Kalle Kanin")
Kalle Kanin

print('Kalle Kanin')
Kalle Kanin
```

--

Med trippla citationstecken kan man ha texter som spänner över flera rader i källkoden

```python [ ]

print("""en lång sträng som går
... över flera
... rader så att säga""")

en lång sträng som går
över flera
rader så att säga
```

--

Vill man räkna med teckensträngar som innehåller siffror måste dessa konverteras först (heltal och flyttal kan blandas utan konvertering, men siffror och teckensträngar är olika typer)

```python [ ]
print('123' + 123)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

--


```python [ ]
print(int('123') + 123)

246
```

--

```python [ ]
print(int('123kaka') + 123)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '123kaka'
```

--

Strängar kan konkateneras med '+' och förmeras med '*'

```python [ ]
print('Hej' + 'san')

Hejsan

print(5 * 'Hej')

HejHejHejHejHej
```

--

Heltal och flyttal omvandlas till strängar med funktionen `str()`

```python [ ]
print(a, b)

5 bananer

print(str(a) + b)

5bananer
```

---

# Skriva ut flera saker med print

--

`print` kan användas för att skriva ut flera saker samtidigt genom att man anger dem med kommatecken mellan.

```python [ ]
a = 'gula'
b = 'bananer'

print(a, b)

gula bananer
```

--

`print` sätter in ett separationstecken (vanligen mellanslag) mellan varje sak (vill man undvika det får man konkatenera strängarna istället och lägga in mellanslag själv).

```python [ ]
a = 'gula'
b = 'bananer'

print(a + b)

gulabananer
```

--

`print` kan innehålla saker som måste räknas ut eller matas in innan det kan skrivas ut.

```python [ ]
r = 4

print('Cirkeln har arean ', '3.14 * r ** 2', 'kvm')

Cirkeln har arean  3.14 * r ** 2 kvm

print('Cirkeln har arean ', eval('3.14 * r ** 2'), 'kvm')

Cirkeln har arean  50.24 kvm
```

Funktionen `eval` kör en Python-kodsnutt inne i Python.

---

# Escapesekvenser i strängar

--

Escapesekvenser är koder som markerar att något av särskild betydelse följer, t.ex. som styrkoder för en utskrift

Många språk, inkl Python, används backslash, **\** plus ett annat tecken för att markera olika saker

--

| Escapesekvens | Beskrivning                          |
| ------------- | -------------------------------------|
| \n            | Radbrytning                          |
| \t            | Tab                                  |
| \r            | Return, hoppar till kolumn 1         |
| \\"           | Utskrift av dubbelt citationstecken  |
| \\'           | Utskrift av enkelt citationstecken   |
| \\\           | Utskrift av backslash                |
| \b            | Backa ett steg i utskriften          |

--

```python [ ]
txt = "Bosse \"Bildoktorn\" Andersson"

print(txt)

Bosse "Bildoktorn" Andersson.
```

---

# Manipulera print-funktionen

--

`print` använder vanligen en radframmatning, **\n**, som avslutning på varje utskrift, samt mellanslag som separationstecken.

Detta kan ändras genom att lägga till ett par parametrar som anger separationstecken och avslutningstecken.

```python [ ]
print('Kurt', 'Bengt', 'Eva-Britt', sep=' och ', end = '.\n')

Kurt och Bengt och Eva-Britt.
```

---

# Manipulera print-funktionen – avancerad utmatning

--

`print` kan styras ytterligare genom format-metoden för strängar.

Till exempel om vill man infoga vissa strängar på vissa platser i en utskrift.

--

I Python används "måsvingar" för att markera plats för infogningen, och efter strängen skriver man en formatmetod.

```python [ ]
print('{} och {} satsar {} kr var på tipset'.format('Kal', 'Ada', 50))

Kal och Ada satsar 50 kr var på tipset
```

--

I formatmetoden kan man ange ordning för infogningen med siffror, annars sker den i tur och ordning.

```python [ ]
print('{1} och {0} satsar {2} kr var på tipset'.format('Kal', 'Ada', 50))

Ada och Kal satsar 50 kr var på tipset
```

--

Inom måsvingen kan man också ange antal tecken för infogningen samt dess formatering, t.ex betyder **4.2f** fyra tecken, flyttal med två decimaler.

--

```python [ ]
print('{1} och {0} satsar {2:4.2f} kr var på tipset'.format('Kal', 'Ada', 50))

Ada och Kal satsar 50.00 kr var på tipset
```

Flyttal med minst fyra tecken, flyttal med två decimaler.

--

```python [ ]
print('{1} och {0} satsar {2:08.2f} kr var på tipset'.format('Kal', 'Ada', 50))

Ada och Kal satsar 00050.00 kr var på tipset
```

Flyttal med minst åtta tecken, flyttal med två decimaler samt visa "leading zeros" vid behov.

--

```python [ ]
print('{:02X} {:02X} {:02X}'.format(255,128,5))

FF 80 05
```

Hexadecimala tal med minst två tecken, samt visa "leading zeros" vid behov.

--

En komplett tabell är som följer:

| Tecken | Beskrivning                     |
|--------|---------------------------------|
| s		   | sträng                          |
| f		   | flyttal                         |
| d		   | heltal på decimal form          |
| x		   | hexadecimalt heltal med gemener |
| X		   | hexadecimalt heltal, versaler   |
| b		   | heltal på binär form            |
| e		   | flyttal på exponentform         |

--

Höger-, vänsterjustering och centrering anges med >, <, ^

```python [ ]
num = 9

print('Talet {0:<4d} skrivs binärt som {0:^8b} så det så'.format(num))

Talet 9    skrivs binärt som   1001   så det så

print('Talet {0:>4d} skrivs binärt som {0:^8b} så det så'.format(num))

Talet    9 skrivs binärt som   1001   så det så
```

--


```python [ ]
num = 9

print('Talet {0:<04d} skrivs binärt som {0:0^8b} så det så'.format(num))

Talet 9000 skrivs binärt som 00100100 så det så
```

**Tänk dig för!** Vad händer här?

---

# Inmatningar

--

Inmatningar från användaren görs med input-funktionen.

För att kunna räkna med inmatad data eller göra formaterade utskrifter kan man behöva konvertera data.

--

```python [ ]
pris = input('Ange pris per kilo: ')

Ange pris per kilo: 55

print('Kilopris = {0:4.2f} kr per kilo'.format(float(pris)))

Kilopris = 55.00 kr per kilo
```

---

# Slut
