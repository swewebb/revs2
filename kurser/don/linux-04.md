# linux-04

---

# En kort introduktion till kommandoraden

--

![Bild1](images/linux-04-01.png)

---

# Kommandoprompt

--

Det är vid prompten vi skriver våra kommandon.
Kan skilja sig åt i utseende, men i vårt fall ser den ut så här….
- <span class=bluetext>pelle</span>@<span class=redtext>mediaserver</span>:<span class=greentext>~/filmer</span><span class=orangetext>$</span>
- <span class=bluetext>pelle</span> = användaren som är inloggad
- <span class=redtext>mediaserver</span> = datorn man är inloggad på
- <span class=greentext>~/filmer</span> = Anger vart i filträdet man befinner sig
- <span class=orangetext>$</span> = Anger att man är inloggad som "vanlig" användare. # = root

Obs! Det finns en mängd olika andra skal än bash som vi kör.

---

# Använda den inbyggda manualen

--

```
man ls
```

--

| Kapilel |Innehåller                    |
|:--------|------------------------------|
| 1       | Vanliga exekverbara kommandon och program|
| 2       | Systemanrop(funktioner som tillhandahålls av kärnan)|
| 3       | Biblioteksanrop(funktioner som tillhandahålls av programbiblitek)|
| 4       | Specialfiler, ex. enheter i /dev|
| 5       | Konfigurationsfiler och filformat|
| 6       | Spel|
| 7       | Blandat och övrigt|
| 8       | Kommandon för systemadministration|
| (9)       | (Specifikt för kärnan och dess rutiner)|

--

`printf`är både ett kommando för att skriva formaterad text samt en funktion i standardbiblioteket för C.

```
man printf
```

Öppnar manualen för kommandot `printf`

```
man 3 printf
```

Öppnar manualen för funktionen `printf` i C

--

Se [https://www.kernel.org/doc/man-pages/](https://www.kernel.org/doc/man-pages/)

--

## Navigera inuti en manualsida


| Tangent    |Åstadkommer                                 |
|:-----------|--------------------------------------------|
| Retur      | Rullar ner på sidan en rad i taget         |
| Nedåtpil   | Rullar ner på sidan en taget               |
| Mellanslag | Rullar ner på sidan en sida i taget        |
| Uppåtpil   | Rullar uppåt på sidan en rad i taget       |
| b          | Rullar uppåt på sidan en sida i taget      |
| /          | Öppnar sökfältet                           |
| n          | Sök efter nästa förekomst av sökordet      |
| N          | Sök efter föregående förekomst av sökordet |
| q          | Avslustar man                              |

---

# Hitta kommandon

Med kommandot `apropos` kan man hitta kommandon.

---

# Filmer

--

**HakTip - Linux Terminal 101**
- [How To Use Man Pages](https://www.youtube.com/watch?v=BWLSqZZfKc4)
- [type, which, and apropos](https://www.youtube.com/watch?v=CQvkF4LHY58)