# Linux-09

---

# Omdirigering av data

--

![linux-09-01](images/linux-09-01.png)

--

| Vad             | Fildeskriptor |
| --------------- | ------------- |
| standard input  | 0             |
| standard output | 1             |
| standard error  | 2             |

En **fildeskriptor** är ett nummer som hänvisar till vilken dataström vi vill komma åt eller omdirigera.

--

![linux-09-02](images/linux-09-02.png)

---

# Omdirigering av utdata

--

## Enkel omdirigering

--

![linux-09-03](images/linux-09-03.png)

--

![linux-09-04](images/linux-09-04.png)

--

## Avancerad omdirigering

--

![linux-09-06](images/linux-09-06.png)

Kommandot vi körde gav inget fel, därför är **felmeddelande.txt** tom.

Filen **utdata.txt** kommer innehålla resultatet av vår listning.

--

![linux-09-07](images/linux-09-07.png)

Kommandot vi körde gav fel, vilket vi ser i **felmeddelande.txt** .

Filen **utdata.txt** kommer att vara tom.

--

![linux-09-08](images/linux-09-08.png)

Vill vi få både **stdout** och **stderr** till samma fil använder vi **&>**

--

## Lägga till data

--

![linux-09-09](images/linux-09-09.png)

**Problem!** När vi kör den andra omdirigeringen skrivs resultatet från den första över.

--

![linux-09-10](images/linux-09-10.png)

**Lösning!** Vi använder **>>** för att lägga till (_append_) i filen.

**Fundering...** Vad gör första raden?

---

# Omdirigering av indata

--

![linux-09-11](images/linux-09-11.gif)

**wc** = Word Count (avsluta med **CTRL + D**)

2 = Två rader

6 = Sex ord

28 = 28 tecken

--

![linux-09-12](images/linux-09-12.png)

Klassen har fyra rader, fyra ord och 23 tecken.

--

![linux-09-13](images/linux-09-13.png)

Klassen är osorterad.

--

![linux-09-14](images/linux-09-14.png)

Vi sorterar klassen vid utskrift på skärmen.

--

![linux-09-15](images/linux-09-15.png)

Vi sorterar klassen och skriver den sorterade klassen till filen **klass-sorterad.txt**

---

# Rörledningar

--

Utdata (**stdout**) från ett program skickas som indata (**stdin**) till ett annat program.

--

![linux-09-16](images/linux-09-16.png)

--

![linux-09-17](images/linux-09-17.png)

--

![linux-09-18](images/linux-09-18.png)

--

![linux-09-19](images/linux-09-19.png)

---

# Flera kommandon på samma rad

--

## Listoperatorer

**&&** AND (och)

**||** OR (eller)

**;** Kör nästa kommando

--

## &&

--

```html
kommando1 && kommando2
```

Kommando2 kommer enbart att köras om kommando1 avslutas korrekt.

--

![linux-09-20](images/linux-09-20.png)

--

![linux-09-21](images/linux-09-21.png)

--

## ||

--

```html
kommando1 || kommando2
```

Kommando2 kommer enbart att köras om kommando1 INTE avslutas korrekt.

--

![linux-09-22](images/linux-09-22.png)

--

![linux-09-23](images/linux-09-23.png)

--

## ;

--

```html
kommando1 ; kommando2
```

Kommando2 kommer att köras oavsett vad kommando1 gör.

--

![linux-09-24](images/linux-09-24.png)

---

# Slut!
