# Filhantering i Python

---

# Vad är filhantering?

--

Möjligheten att läsa och skriva filer på datorn.

Viktigt för att spara data permanent.

Python har inbyggda funktioner för filhantering.

--

## Textfiler

- Textfiler
- XML
- CSV
- JSON
- Källkod
- ...

--

## Binärfiler

- Kompilerad kod
- Mediafiler
- ...

---

# Öppna en fil i Python

--

```python []
# Öppnar en fil för läsning
fil = open("exempel.txt", "r", encoding = "UTF-8")

# Läser filens innehåll
data = fil.read()
print(data)

# Stänger filen
fil.close()
```

---

# Skriva till en fil

--

```python []
# Öppnar en fil för skrivning
fil = open("exempel.txt", "w", encoding = "UTF-8")

# Skriver till filen
fil.write("Hej, detta är en testtext!\n")

# Stänger filen
fil.close()
```

**"w"** betyder att vi öppnar filen i skrivläge.

**OBS!** Om filen redan finns skrivs den över!

---

# Lägga till text i en fil

--

```python []
# Öppnar en fil för att lägga till text
fil = open("exempel.txt", "a", encoding = "UTF-8")

# Lägger till en rad
fil.write("Här är en till rad med text.\n")

# Stänger filen
fil.close()
```

**"a"** lägger till ny text utan att radera tidigare innehåll.

---

# Bästa praxis: `with open()`

--

```python []
with open("exempel.txt", "r", encoding = "UTF-8") as fil:
    innehall = fil.read()
    print(innehall)
```

Python stänger automatiskt filen när blocket avslutas.

---

# Läsa fil rad för rad

--

```python []
with open("exempel.txt", "r", encoding = "UTF-8") as fil:
    for rad in fil:
        print(rad.strip())
```

Bra vid stora filer där **.read()** kan bli minneskrävande.

**strip()** tar bort extra radbrytningar.

---

# Lägga till felhantering

--

```python []
try:
    with open("exempel.txt", "r", encoding = "UTF-8") as fil:
        innehall = fil.read()
        print(innehall)
except FileNotFoundError:
    print("Filen hittades inte, kontrollera filnamnet!")
except Exception as error:
    print(f"Ett oväntat fel inträffade: {error}")
```
