# Flödesschema

---

# Vad är ett flödesschema?

--

En grafisk beskrivning av hur ett program arbetar.

Visar steg för steg vad som ska göras.

Hjälper till att planera och förstå programflödet.

---

# Varför använder vi flödesscheman?

--

Tydligör tankegångar innan kodning.

Lättare att hitta fel.

Underlättar förklaringar för andra.

---

# Grundläggande symboler

--

**Oval**: Start / Stopp

**Rektangel**: Process (t.ex. beräkning)

**Parallellogram**: Input / Output

**Romb**: Beslut (villkor)

---

# Räkna ut summan av två tal

--

```mermaid
flowchart TD
    A([Start]) --> B[/Mata in två tal/]
    B --> C[Beräkna summan]
    C --> D[/Skriv ut summan/]
    D --> E([Stopp])
```

---

# Är talet positivt?

--

```mermaid
flowchart TD
    A([Start]) --> B[/Mata in ett tal/]
    B --> C{Talet > 0?}
    C -- Ja --> D[/Skriv "Positivt tal"/]
    C -- Nej --> E[/Skriv "Inte positivt"/]
    D --> F([Stopp])
    E --> F
```

---

# Repetera tills ett villkor är falskt

--

```mermaid
flowchart TD
    A([Start]) --> B[/Initiera variabler/]
    B --> C{Villkor sant?}
    C -- Ja --> D[Utför process]
    D --> C
    C -- Nej --> E([Stopp])
```

---

## Repetera ett bestämt antal gånger

--

```mermaid
flowchart TD
    A([Start]) --> B[/Initiera variabel, t.ex. i = 0/]
    B --> C{i < antal?}
    C -- Ja --> D[Utför process]
    D --> E[Uppdatera i]
    E --> C
    C -- Nej --> F([Stopp])
```

---

```mermaid
flowchart TD
    Start([Start])
    Input1[/Ange tal 1/]
    Input2[/Ange tal 2/]
    Compare{Är tal 1 större än tal 2?}
    Greater1[> Skriv ut tal 1]
    Compare2{Är tal 1 mindre än tal 2?}
    Greater2[> Skriv ut tal 2]
    Equal[> Skriv ut Lika stora]
    End([Slut])

    Start --> Input1
    Input1 --> Input2
    Input2 --> Compare
    Compare -- Ja --> Greater1
    Greater1 --> End
    Compare -- Nej --> Compare2
    Compare2 -- Ja --> Greater2
    Greater2 --> End
    Compare2 -- Nej --> Equal
    Equal --> End

```

---

```mermaid
flowchart TD
    Start([Start])
    InputStart[/Ange start/]
    InputStop[/Ange stopp/]
    InitI[Z sätt i = start]
    Check{Är i <= stop?}
    PrintI[> Skriv ut i]
    IncrementI[Öka i med 1]
    End([Slut])

    Start --> InputStart
    InputStart --> InputStop
    InputStop --> InitI
    InitI --> Check
    Check -- Ja --> PrintI
    PrintI --> IncrementI
    IncrementI --> Check
    Check -- Nej --> End

```

---

```mermaid
flowchart TD
    Start([Start])
    InputN[/n = input "Ange antal tal:"/]
    KontrollN{Är n > 0?}
    NyttN[/n = input "Ange antal tal:"/]
    InitTotal[total = 0]
    InitI[i = 0]
    ForLoopStart{i < n?}
    InputX[/x = input "Ange talet:"/]
    AddX[total += x]
    ÖkaI[i += 1]
    BeräknaMedel[average = total / n]
    SkrivUtMedel[print Medelvärde]
    Slut([Slut])

    Start --> InputN --> KontrollN
    KontrollN -- Nej --> NyttN --> KontrollN
    KontrollN -- Ja --> InitTotal --> InitI --> ForLoopStart
    ForLoopStart -- Ja --> InputX --> AddX --> ÖkaI --> ForLoopStart
    ForLoopStart -- Nej --> BeräknaMedel --> SkrivUtMedel --> Slut

```

# SLUT!
