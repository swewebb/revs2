# Type Hinting

--

**Type hinting** är ett verktyg för att ge programmerare möjlighet att specificera vilken typ av data som funktioner och variabler förväntas hantera.

--

Det hjälper till att göra koden mer läsbar och att identifiera potentiella buggar tidigare i utvecklingsprocessen.

--

Python 3.10 introducerade flera förbättringar som förenklar och förstärker användningen av type hints.

---

# Variabler

--

**Type hints** kan användas för att ange vilken typ en variabel ska ha.

--

## Utan type hints

--

```python []
age = 25
name = "Pelle"

age = "kaka"
name = "Pelle"

print(f"Du heter {name} och är {age} gammal")
```

--

BILD

--

## Med type hints

--

```python []
age: int = 25
name: str = "Pelle"

age = "kaka"
name = "Pelle"

print(f"Du heter {name} och är {age} gammal")
```

--

BILD

---

# Funktioner

--

Vi kan använda **type hints** för att specificera typer för funktioners argument och returvärden:

```python []
def add_numbers(a: int, b: int) -> int:
  """DOCSTRING"""
  return a + b
```

--

Här specificeras att både **a** och **b** ska vara heltal (int), och att funktionen returnerar ett heltal.

--

Bild

---

# Förbättringar i Python 3.10

--

## Union Operator (|)

Från och med **Python 3.10** kan du använda **|** för att ange flera möjliga typer.

```python []
def process_value(value: int | str) -> str:
  """DOCSTRING"""
  if isinstance(value, int):
    return f"Number: {value}"

  return f"Text: {value}"
```

[isinstance](https://www.w3schools.com/python/ref_func_isinstance.asp)

--

Tidigare var samma kod skriven med **Union**

```python [1-3]
from typing import Union

def process_value(value: Union[int, str]) -> str:
  """DOCSTRING"""
  if isinstance(value, int):
    return f"Number: {value}"

  return f"Text: {value}"
```

---

# Andra viktiga verktyg <br> för Type Hinting

--

## Generics

```python []
def process_data(data: list[int], config: dict[str, str]) -> None:
  """DOCSTRING"""
  for number in data:
    print(f"Processing {number} with config {config}")
```

**Generics** används för att ange typer för mer komplexa strukturer, som **listor** och **dictionaries**.

Från och med **Python 3.9** kan du använda inbyggd syntax.

--

```python []
from typing import List, Dict

def process_data(data: List[int], config: Dict[str, str]) -> None:
  """DOCSTRING"""
  for number in data:
    print(f"Processing {number} with config {config}")
```

Om du kör en tidigare version av Python måste du använda modulen **typing**

--

## TypedDict

```python []
from typing import TypedDict

class UserInfo(TypedDict):
  """DOCSTRING"""
  id: int
  name: str
  email: str

def print_user_info(user: UserInfo) -> None:
  """DOCSTRING"""
  print(f"{user['name']} ({user['id']}) - {user['email']}")

user = UserInfo(id=1, name="Pelle", email="pelle@kofot.com")

print_user_info(user)
```

--

```text []
Pelle (1) - pelle@kofot.com
```

--

För mer strukturerade data kan vi använda oss av **TypedDict** för att specificera typer i **dictionaries**.

---

# SLUT!
