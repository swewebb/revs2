# Python - Kapitel 11

---

# Inledning

--

Fel som inträffar när datorn kör en kod vi skrivit kan indelas i följande typer:

--

## Runtime (logiska fel)

Vi har programmerat fel, tänkt fel, eller gör någon form av förbjuden operation, t.ex:

- Indexerar utanför en listas sista element
- Försökt dela med noll
- Användaren matar in data av fel typ så att programmet inte kan fortsätta som tänkt

--

## Syntaxfel (kompileringsfel / interpreteringsfel)

Vi har använt fel syntax.

Här hinner koden aldrig köras utan avbryts under ett inledande skede.

--

Syntaxfel får vi klara av genom att rätta koden, och i viss mån även runtime-fel, men många fel som inträffar under körning behöver inte leda till att programmet kraschar om vi har en felhantering, s.k. **undantagshantering (exceptions)**

---

# Exempel på fel som kan inträffa

--

```python []
kvot = 10/0
print(kvot)
```

```python [4]
Traceback (most recent call last):
  File "ex1.py", line 1, in <module>
    kvot = 10/0
ZeroDivisionError: division by zero
```

--

```python []
lista = ['A', 'B', 'C']
print(lista[3]);
```

```python [4]
Traceback (most recent call last):
  File "ex2.py", line 3, in <module>
    print(lista[3]);
IndexError: list index out of range
```

--

```python []
foo = 'Teknik'
print(bar)
```

```python [4]
Traceback (most recent call last):
  File "ex3.py", line 2, in <module>
    print(bar)
NameError: name 'bar' is not defined
```

--

```python []
txt = 'Teknik'
print('Texten är {}'.formats(txt))
```

```python [3-4]
Traceback (most recent call last):
  File "ex4.py", line 2, in <module>
    print('Texten är {}'.formats(txt))
AttributeError: 'str' object has no attribute 'formats'
```

--

```python []
txt = 'Teknik'
print txt
```

```python [4-5]
File "ex5.py", line 2
    print txt
          ^
SyntaxError: Missing parentheses in call to 'print'.
Did you mean print(txt)?
```

--

```python []
import teknik

txt = 'Teknik'
print(txt)
```

```python [4]
Traceback (most recent call last):
  File "ex5.py", line 1, in <module>
    import teknik
ModuleNotFoundError: No module named 'teknik'
```

---

# Fullständig felhantering i Python

--

```python []
try:
	Programblock för att försöka något som kan orsaka problem
	[raise feltyp]
except [feltyp]:
	Programblock för att fånga upp eventuella undantag
else:
	Programblock som körs om inget undantag inträffade
finally:
	Programblock som alltid körs oavsett vad som hänt
```

--

**else** och **finally** kan utelämnas

Man kan ha flera **except** för olika typer av fel

Vill man själv utlösa ett undantag i try-blocket kan man använda **raise**

---

# Exempel

--

```python []
try:
    txt = 'Teknik'
    print(x)
except:
    print('Ett undantag har hänt')
```

```html []
Ett undantag har hänt
```

--

```python []
try:
    txt = 'Teknik'
    print(x)
except NameError:
    print('Variabeln x är ej deklarerad')
except:
    print('Ett annat undantag har hänt')
```

```html []
Variabeln x är ej deklarerad
```

--

```python []
try:
    txt = 'Teknik'
    print(10/0)
except NameError:
    print('Variabeln x är ej deklarerad')
except:
    print('Ett annat undantag har hänt')
```

```html []
Ett annat undantag har hänt
```

--

```python []
try:
    txt = 'Teknik'
    print(x)
    print(10/0)
except NameError:
    print('Variabeln x är ej deklarerad')
except:
    print('Ett annat undantag har hänt')
```

```html []
Variabeln x är ej deklarerad
```

--

```python []
try:
    txt = 'Teknik'
    print(x)
except NameError as e:
    print(e)
```

```html []
name 'x' is not defined
```

--

```python []
try:
    txt = 'Teknik'
    x = 10/0
    print(x)
except (NameError, ZeroDivisionError) as e:
    print(e)
```

```html []
division by zero
```

--

```python []
try:
    txt = 'Teknik'
    x = 10/2
    print(y)
except (NameError, ZeroDivisionError) as e:
    print(e)
```

```html []
name 'y' is not defined
```

--

```python []
try:
    x = int(input("Ange ett heltal: "))
    y = 100 / x
    print('Kvoten =', y)
except ValueError:
    print("Felaktigt värde")
except ZeroDivisionError:
    print("Nolldivision")
except:
    print('Ett annat undantag har hänt')
```

```text []
Ange ett heltal: 55.55
Felaktigt värde
```

```text []
Ange ett heltal: 0
Nolldivision
```

--

```python []
try:
    tal = int(input("Ange ett jämt heltal: "))
    assert tal % 2 == 0
except:
    print("Inget jämt heltal!")
else:
    omvänt = 1/tal
    print(omvänt)
```

```text []
Ange ett jämt heltal: 5
Inget jämt heltal!
```

```text []
Ange ett jämt heltal: teknik
Inget jämt heltal!
```

```text []
Ange ett jämt heltal: 8
0.125
```

--

```python []
try:
    x = 5
    if x < 10:
        raise ValueError('x ska inte vara mindre än 10')
except ValueError as e:
    print(e)
```

```html []
x ska inte vara mindre än 10
```

---

# Definition av egna feltyper

--

I Python kan vi definiera egna typer av undantag som vi kan flagga för.

Man behöver inte göra något inne i själva feldefinitionen, där räcker det med **pass**.

--

```python []
class ReallyStupidError(Exception):
    pass

try:
    if int(input("Ange ett positivt tal: ")) < 0:
        raise ReallyStupidError
except ReallyStupidError:
    print("Du är inte vidare smart, du!")
else:
    print("Det är ett positivt tal!")
```

```txt []
Ange ett positivt tal: 5
Det är ett positivt tal!
```

```txt []
Ange ett positivt tal: -5
Du är inte vidare smart, du!
```

---

# Vanlig användning vid inmatning

--

```python []
while True:
    x = input('Ange ett reellt tal: ')
    try:
        x_num = float(x)
        print('Du angav talet: ', x_num)
        break
    except:
        print(x,' är inte ett tal! Vänligen försök igen.')
```

```text []
Ange ett reellt tal: teknik
teknik är inte ett tal! Vänligen försök igen.
Ange ett reellt tal: 5.55
Du angav talet: 5.55
```

---

```python []
def add_numbers(a: float, b: float) -> float:
    """DOCSTRING"""
    try:
        return a + b
    except TypeError:
        print("Fel: Inmatningen måste vara numerisk.")
        return 0.0

if __name__ == "__main__":
    resultat = add_numbers(5, 10.5)
    print(f"{resultat=}")
```

--

```text []
resultat=15.5
```

```python []
resultat = add_numbers("kaka", 10.5)
```

```text []
Fel: Inmatningen måste vara numerisk.
resultat=0.0
```

---

# Slut
