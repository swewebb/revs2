# Linux-07

## Rättigheter och användare m.m

---

# Rättigheter

--

![07-01](images/linux-07-01.png)

--

## Första tecknet

\- = fil

d = mapp/katalog

l = mjuk/symbolisk länk

--

## rwx

**r** = Read = Läs

**w** = Write = Skriv

**x** = Execute = Kör

**Observera!** Mappar har **x** för att man ska kunna komma in i dem.

--

## Ägare - Grupp - Övriga

![07-02](images/linux-07-02.png)

--

## T-biten

![07-03](images/linux-07-03.png)

--

Betyder att även om en användare har skrivrättigheter i mappen, så får denne bara skrivrättighet på filer som man är ägare till, och kan således inte ta bort andra användares filer eller mappar själv (om denne inte är ägare till mappen eller medlem i gruppen som äger mappen).

En typisk sådan mapp är **/tmp**, i denna kan alla användare skriva, men inte radera saker som inte är deras egna.

Inte heller kan de radera själva mappen **/tmp**.

---

# Ändra rättigheter

--

![07-04](images/linux-07-04.png)

--

```html
rw- rw- rw-
110 110 110
421 421 421
--- --- ---
420 420 420 => 6 6 6
```

--

## chmod

![07-05](images/linux-07-05.png)

--

![07-06](images/linux-07-06.png)

Mappen har **rwx rwx r-x**, vi vill ändra så att ägaren läsa och skriva i mappen, gruppen får läsa, medan övriga inte får tillgång till mappen alls.

--

```html
rw- r-- ---
110 100 000
421 421 421
--- --- ---
420 400 000 => 6 4 0
```

--

![07-07](images/linux-07-07.png)

Nehepp… det där gick ju inget vidare!

--

```html
rwx r-x ---
110 100 000
421 421 421
--- --- ---
421 401 000 => 7 5 0
```

Kom ihåg! Mappar måste ha **x**

--

![07-08](images/linux-07-08.png)

---

# Standardrättigheter

--

## umask

![07-09](images/linux-07-09.png)

0**002** = Ägare - Grupp - Övriga

```html
000 000 010
rwx rwx r-x
```

--

![07-10](images/linux-07-10.png)

Varför stämmer standardrättigheterna för mappen och inte för filen?

Jo, filer får INTE x (execute) som standard av säkerhetsskäl.

--

Om vi vill ändra standard-rättigheterna till rwx r-x ---

```html
rwx r-x ---
000 010 111 = 027
```

--

![07-11](images/linux-07-11.png)

Filen **ny_fil** får **rw- r-- ---** och mappen **ny_mapp** får **rwx r-x ---** vilket stämmer med vår standardrättighet.

---

# Skapa en användare

--

## /etc/skel

![07-12](images/linux-07-12.png)

Mappen /etc/skel innehåller skelettet för nya användare.

--

![07-13](images/linux-07-13.png)

Om vi t.ex lägger till en mapp i **/etc/skel** så kommer alla nya användare få en mapp med samma namn i sin hemkatalog.

--

## /etc/passwd

Innehåller alla användare i systemet

"Vanliga användare" == 1000 och uppåt

--

![07-14](images/linux-07-14.png)

--

![07-15](images/linux-07-15.png)

1. Användarnamn
2. Lösenord, hanteras i **/etc/shadow**
3. Användarid (UID)
4. Gruppid (GID)
5. Hela namnet

--

![07-15](images/linux-07-15.png)

6. Rumsnummer
7. Arbetstelefon
8. Hemtelefon
9. Övrigt
10. Hemkatalog
11. Skal

--

## /etc/shadow

![07-16](images/linux-07-16.png)

Här återfinns lösenorden för användarna i krypterad form. Innehåller även annan information, t ex när kontot senast bytte lösenord.

Kvällsläsning (inget som kommer på något prov):
- [https://www.cyberciti.biz/faq/understanding-etcshadow-file/](https://www.cyberciti.biz/faq/understanding-etcshadow-file/)

--

## /etc/group

![07-16](images/linux-07-17.png)

1. Gruppnamn = projekt
2.Lösenord (används inte…)
3. GID = 1004
4. Medlemmar i gruppen = kurt och kalle

--

## Skapa användare

![07-18](images/linux-07-18.png)

--

![07-19](images/linux-07-19.png)

---

# Ta bort en användare

--

![07-20](images/linux-07-20.png)

När man tar bort en användare kommer användarens hemkatalog att finnas kvar

---

# Ändra lösenord

--

## Uppdatera eget lösenord

![07-21](images/linux-07-21.png)

--

## Uppdatera annans lösenord

![07-22](images/linux-07-22.png)

---

# Skapa en ny admin

--

En ny admin skapar vi genom att lägga till användaren till gruppen sudo

![07-23](images/linux-07-23.png)

![07-24](images/linux-07-24.png)

---

# Ta bort en admin, men inte användaren

--

Vi kan använda oss av kommandot **deluser** för att ta bort en användare från gruppen sudo.

![07-25](images/linux-07-25.png)

---

# Ändra ägare - chown

--

![07-26](images/linux-07-26.png)

--

![07-27](images/linux-07-27.png)

--

![07-28](images/linux-07-28.png)

--

![07-29](images/linux-07-29.png)

---

# Ändra grupp - chgrp

--

![07-30](images/linux-07-30.png)

![07-31](images/linux-07-31.png)

![07-32](images/linux-07-32.png)

---

# Ändra både ägare och grupp

--

![07-33](images/linux-07-33.png)

---

Slut!