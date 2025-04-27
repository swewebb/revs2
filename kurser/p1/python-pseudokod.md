# Pseudokod

---

# Vad är pseudokod?

--

Ett sätt att beskriva algoritmer utan att skriva riktig kod

Använder enkla, begripliga instruktioner

Hjälper till att planera program innan man skriver kod

---

# Varför använda pseudokod?

--

Fokus på logik, inte syntax

Lätt att ändra och diskutera

Förståeligt för alla, oavsett programmeringsspråk

---

# Sekventiella steg

--

```text
Start
Läs in ett tal
Addera 5 till talet
Skriv ut resultatet
Stopp
```

---

# Villkor

--

```text
Start
Läs in ett tal
Om talet > 0
    Skriv ut "Positivt"
Annars
    Skriv ut "Noll eller negativt"
Stopp
```

---

# Loop

--

```text
Start
Sätt räknare till 1
Medan räknare <= 5
    Skriv ut räknare
    Öka räknare med 1
Stopp
```

---

# Finns inget "pseudospråk"

--

Det finns inget officielt pseudospråk, men det gäller att DU skriver så att någon annan förstår.

--

```text
VAR summa = 0

LOOP fem varv
    VAR tal = INPUT 'Ange ett tal:'
    ADD tal till summa

VAR avg = summa / 5; Avrunda till tre decimaler

PRINT '------------'
PRINT 'Summan är', summa
PRINT 'Medelvärdet är', avg
PRINT '------------'
```

--

```text
FUNKTION summera(talserien)
    VAR summa = 0
    LOOPA tal UR talserien
        summa += tal
    RETURNERA summa

VAR x = summera(talserien)
PRINT x
```

--

```text
Deklarera fnamn, tilldela värde via input 'Skriv in ditt förnamn:'
Deklarera enamn, tilldela värde via input 'Skriv in ditt efternamn:'
Deklarera full_name, tilldela värdet av fnamn mellanslag enamn
Deklarera new_name, tilldela None

Loopa igenom ett tecken i taget ur full_name
    Om tecknet är litet
        Ändra till stort tecken
        Lägg till tecknet till new_name
    Om tecknet är stort
        Ändra till litet tecken
        Lägg till tecknet till new_name

Skriv ut new_name värde
```

---

# Tips för bra pseudokod

--

Använd tydliga och enkla ord

Fokusera på vad som ska göras, inte hur

Strukturera logiskt

---

# SLUT
