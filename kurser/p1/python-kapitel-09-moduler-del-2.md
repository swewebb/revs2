# Moduler - Del 2

--

**if \_\_name\_\_ == "\_\_main\_\_":**

Används för att säkerställa att en del av koden endast körs när filen körs direkt som ett skript, och inte när den importeras som en modul i ett annat program.

Vanlig praxis som hjälper till att organisera och återanvända kod bättre.

--

När en Pythonfil körs direkt, sätts variabeln **\_\_name\_\_** till **"\_\_main\_\_"**.

När en fil importeras som en modul i ett annat program, sätts **\_\_name\_\_** till filens namn (utan .py).

--

Används för att separera "skriptlogik" (sånt som ska köras omedelbart) från funktioner och klasser som kan återanvändas.

Förhindrar att kod körs oavsiktligt när filen importeras.

---

# Exempel 1

--

## Utan kontroll

--

### Filen script.py

```python []
def hello() -> None:
  """DOCSTRING"""
  print("Hej från funktionen!")

print("Detta körs alltid!")

hello()
```

```
Detta körs alltid!
Hej från funktionen!
```

--

### Filen app.py

```python []
import script
```

```
Detta körs alltid!
Hej från funktionen!
```

--

## Med kontroll

--

### Filen script.py

```python []
def hello() -> None:
  """DOCSTRING"""
  print("Hej från funktionen!")


if __name__ == "__main__":
  print("Detta körs bara om filen körs direkt!")

  hello()
```

```
Detta körs bara om filen körs direkt!
Hej från funktionen!
```

--

### Filen app.py

```python []
import script
```

Ingenting körs från importen!

---

# Exempel 2

--

## Filen calculator.py

```python []
def add(a: float, b: float) -> float:
    """DOCSTRING"""
    return a + b

def subtract(a: float, b: float) -> float:
    """DOCSTRING"""
    return a - b

if __name__ == "__main__":
    # Tester
    print(f"Adderar: {add(3, 4)}")
    print(f"Adderar: {add(0.22, 4.78)}")
    print("-" * 20)
    print(f"Subtraherar: {subtract(10, 4)}")
    print(f"Subtraherar: {subtract(10.10, 0.10)}")
```

--

```text []
Adderar: 7
Adderar: 5.0
--------------------
Subtraherar: 6
Subtraherar: 10.0
```

--

## Filen app.py

```python []
from calculator import add, subtract

def main() -> None:
    """DOCSTRING"""
    print(add(3, 5))
    print(subtract(5, 2))

if __name__ == "__main__":
    main()
```

```
8
3
```

Här ser vi att testkoden i **calculator.py** inte körs.

---

# SLUT!
