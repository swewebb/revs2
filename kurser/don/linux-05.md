# linux-05

---

# Filsystemet

--

<span class="fragment">Ett filsystem i Linux är väldigt standardiserat och ser ungefär likadant i alla stora distributionerna.</span>

<span class="fragment">**Filesystem Hierarchy Standard** är en standard som de flesta distributioner följer.</span>

<span class="fragment">I Linux finns inga "enheter" A:, C:, osv</span>

--

<span class="fragment">Längst upp i filsystemet har vi roten och under den återfinns allt.</span>

<span class="fragment">Tänk dig ett rotsystemet på ett träd.</span>

<span class="fragment">Ett filsystem kan spänna över flera diskar/partitioner</span>

<span class="fragment">Montering</span>

--

<span class="fragment">Ett filsystem "monteras ihop" av flera olika små filsystem.</span>

<span class="fragment">En katalog i ett filsystem blir en monteringspunkt för ett annat filsystem.</span>

<span class="fragment">Alla delar i filsystemet utgår från roten "/"och kataloger åtskiljs med snedstreck "/".</span>

<span class="fragment">Ett exempel på ett filnamn är: **/home/pelle/filen.pdf**</span>

--

![linux05-38](images/linux-05-38.png)

--

![linux05-38](images/linux-05-39.png)

--

**/**

Rotem av filsystemet.

Under denna katalog finns allt annat.

--

**/bin**

Binärfiler, vanliga användarkommandon.

Är i Ubuntu en genväg till **/usr/bin**

--

**/boot**

Filer för att starta systemet inkl. kärnan.

--

**/cdrom**

Montering av optiska media.

--

**/dev**

Enhetsfiler, ex.hårddiskar och ssd:er.

--

**/etc**

Konfigurationsfiler för systemet och dess tjänster.

--

**/home**

Hemkataloger för användarna.

Motsvararande i Microsoft Windows = C:\Users

--

**/lib, /lib32, /lib64, /libx32**

Biblioteksfiler för kärnan samt C-bibliotek.

Är i Ubuntu en genväg till **/usr/lib** osv.

--

**/lost+found**

Vid en krasch räddas filerna till denna katalog.

--

**/media**

Användarmonterade enheter brukar hamna här.

--

**/mnt**

Monteringspunkt för temporära enheter, t.ex nätverksdelningar.

--

**/opt**

Programvaror som inte hanteras av pakethanteraren.

--

**/proc**

Här ligger alla processer som körs i systemet.

--

**/root**

Detta är root:s (systemadministratörens) hemkatalog.

I Ubuntu är rootanv. inaktiverad.

--

**/run**

Innehåller bland annat system pid-filer (run-time variable data).

--

**/sbin**

Här ligger systemets exekverbara (körbara) file.

Är i Ubuntu en genväg till **/usr/sbin** osv.

--

**/snap**

Här installeras program som levereras via snap.

--

**/srv**

Kommersiella tjänster installeras ibland här.

--

**/sys**

Specialfiler för systemets kärna.

--

**/tmp**

Temporära filer.

--

**/usr**

Program och filer som oftast är tillgängliga för alla användare (users) att komma åt.

--

**/var**

Loggfiler

---

# Hemkatalog

--

<span class="fragment">Alla användare i systemet har en egen hemkatalog.</span>

<span class="fragment">Återfinns i **/home**, t.ex **/home/pelle**</span>

<span class="fragment">Det är här vi hamnar när vi loggar in.</span>

<span class="fragment">Förkortas **~**</span>

<span class="fragment">Din användare äger allt i katalogen.</span>

---

# Absoluta- och relativa sökvägar

--

**Absolut sökväg** = utgår från rooten, t.ex `cd /home/pelle`

--

**Relativ sökväg** = utgår från mappen man står i, t.ex `cd pelle`

---

# Navigera

--

`cd` = Change Directory

--

```
cd /etc/apt/
```

Förflyttar dig till katalogen **/etc/apt** oavsett var i filträdet du befinner dig.

--

```
cd /
```

Förflyttar dig till roten på filträdet oavsett var i filträdet du befinner dig.

--

```
cd ~
cd
```

Förflyttar dig till din hemkatalog (t.ex **/home/pelle**) oavsett var i filträdet du befinner dig.

--

```
cd ..
```

Förflyttar dig ett steg bakåt/uppåt i filträdet, t.ex från **/home/pelle** till **/home/**

--

```
cd ../..
```

Förflyttar dig ett steg bakåt/uppåt i filträdet, t.ex från **/home/pelle** till **/**

--

```
cd musik
```

Förflyttar dig in i katalogen **musik**, som återfinns i katalogen där du befinner dig.

---

# Lista

--

`ls` = list directory contents ("ell-ess")

--

## Enkel listning

`ls`

![linux05-01](images/linux-05-01.png)

Vit = fil, blå = katalog, turkos = mjuk länk

--

## Lista i långt format

```
ls -l
```

![linux05-02](images/linux-05-02.png)


--

## Lista dolda filer/kataloger

```
ls -a
```

![linux05-03](images/linux-05-03.png)

```
ls -A
```

![linux05-04](images/linux-05-04.png)

--

## Kombinera flera växlar

```
ls -Al
```

![linux05-05](images/linux-05-05.png)

--

## Lista annan plats

```
ls ~/start
```

![linux05-20](images/linux-05-20.png)

---

# Se vart man är

--

`pwd` = print name of current/working directory

![linux05-06](images/linux-05-06.png)

---

# Se innehållet i en fil

--

`cat` = concatenate files and print on the standardoutput

--

![linux05-06](images/linux-05-07.png)

--

![linux05-09](images/linux-05-09.png)

---

## Långt innehåll

--

Ibland får inte innehållet plats på skärmen och då vi inte kan skrolla så kommer vi inte att kunna se all information. Det här kan vi lösa mha kommandona `more` eller `less`.

--

`more`

**Enter** = hoppa fram en rad.

**Mellanslag** = hoppa fram en sida

--

```
ls /etc | more
more dump
```

--

`less`

Med `less` kan du använda upp/ned-pil för att förflytta dig i utdatat.

---

# Skapa filer

--

`touch` = change file timestamps

--

```
touch kaka
```

Skapar en tom fil med namnet kaka

![linux05-09](images/linux-05-10.png)

--

```
touch anka1 anka2 anka3
```

Skapar tre tomma filer

![linux05-11](images/linux-05-11.png)

--

```
touch --date="2020-12-24 15:00:00" anka1
```

![linux05-12](images/linux-05-12.png)

![linux05-13](images/linux-05-13.png)


--

`cat >`, avsluta med `CTRL + D`

![linux05-08](images/linux-05-08.png)

---

# Information om en fil

--

`stat` = Display file or file system status

--

![linux05-14](images/linux-05-14.png)

Här kan vi bland annat se när filen senast öppnades eller modifierades.

---

# Skapa kataloger

--

`mkdir` = make directories

--

```
mkdir test
```

Skapar en katalog där du befinner dig.

![linux05-17](images/linux-05-17.png)

--

```
mkdir ~/test
```

Skapar en katalog i din hemkatalog oavsett var du befinner dig.

![linux05-18](images/linux-05-18.png)

--

```html
mkdir -p start/del-1
mkdir -p start/del-2
```

Skapar katalogen start(om den inte finns) för att sedan skapa katalogen del-1 i den.

Skapar del-2 i mappen start (som vi skapade på raden innan).

![linux05-19](images/linux-05-19.png)

---

# Ta bort filer

--

`rm` = remove files or directories

--

```
rm kaka
```

![linux05-15](images/linux-05-15.png)

--

```
rm *.txt
```

![linux05-15](images/linux-05-16.png)

---

# Ta bort kataloger

--

`rmdir` = remove empty directories

--

```
rmdir musik
```

![linux05-21](images/linux-05-21.png)

--

```
rmdir filer
```

![linux05-22](images/linux-05-22.png)

--

```
rm -rf filer
```

---

# Kopiera filer/kataloger

--

`cp` = copy files and directories

--

```
cp fil.md fil2.md
```

![linux05-23](images/linux-05-23.png)

--

```
cp /etc/rsyslog.conf .
```

![linux05-24](images/linux-05-24.png)

--

```
cp -r ../filer .
```

![linux05-25](images/linux-05-25.png)

--

```html
cp -r filer/ backup
```

![linux05-26](images/linux-05-26.png)

---

# Flytta filer/kataloger

--

`mv` = move (rename) files

--

## Filer

```
mv fil.md filer/
```

![linux05-26](images/linux-05-26.png)

--

## Kataloger

```
mv backup/ filer/
```

![linux05-27](images/linux-05-27.png)

--

# Döpa om filer/kataloger

`mv` = move (rename) files

--

```
mv fil2.md haha.md
```

![linux05-28](images/linux-05-28.png)

---

# Länkar

--

`ln` = make links between files

--

## Mjuka länkar

--

<span class="fragment">Fungerar (nästan) som genvägarna i Microsoft Windows.</span>

<span class="fragment">Tar man bort genvägen finns originalfilen kvar.</span>

<span class="fragment">Tar man bort originalfilen så finns genvägen kvar, men den pekar till något som inte finns.</span>

--

```
ln -s orginalet linken
```

![linux05-29](images/linux-05-29.png)

--

![linux05-30](images/linux-05-30.png)

<span class="fragment">Vi öppnar nu länken (linken) i nano och skriver in lite text för att sedan avsluta nano (givetvis sparar vi).</span>

<span class="fragment">Om vi nu öppnar originalet ser vi att ändringen finns kvar.</span>

<span class="fragment">**Kom ihåg!** Mjuka länkar kan ses som genvägar i Microsoft Windows.</span>

--

![linux05-31](images/linux-05-31.png)

Här har vi raderat originalet och då ser vi att vår länk blir röd = trasig

--

![linux05-32](images/linux-05-32.png)

Öppnar vi länken (linken) i nano så ser vi att det är tomt.

--

![linux05-33](images/linux-05-33.png)

Vi passar på att skriva in lite innehåll… och spar ändringarna.

--

![linux05-34](images/linux-05-34.png)

Aha! Nu skapas originalet igen

--

## Hårda länkar

--

<span class="fragment">Hårda länkar är pekare till en fil.</span>

<span class="fragment">Flera hårda länkar kan peka på samma fil.</span>

<span class="fragment">Filen försvinner först efter att alla hårda länkar har raderats.</span>

<span class="fragment">Om du raderar originalfilen men inte de hårda länkarna finns de hårda länkarna kvar, liksom fildatan.</span>

--

```
ln orginalet link
```

![linux05-35](images/linux-05-35.png)

--

![linux05-36](images/linux-05-36.png)

Tar vi bort originalet så kommer länken fortfarande att fungera.

--

![linux05-37](images/linux-05-37.png)

---

# Jokertecken

--

* = Okänt antal tecken

- *.txt = Alla txt-filer
- f*.txt = Alla txt-filer som börjar på f
- i*.* = Alla filer som börjar på i

--

? = Ett okänt tecken

- ?.txt = Alla txt-filer som har ett tecken i filnamnet
- f??.txt = Alla txt-filer som börjar på f och har två tecken därefter
- f*.p? = Alla filer som börjar på f och vars filändelse börjar på p och följs av ett tecken

--

[] = Område

- [bf]*.txt = Alla txt-filer som börjar på b eller f
- *[2-4].html = Alla html-filer som slutar på 2, 3 eller 4.

---

# Filmer

--

**TIF275 Datorintroduktion, Chalmers**

- [Linux 1: Grunderna](https://www.youtube.com/watch?v=yzeY5H-8nVk)
- [Linux: Knep i terminalen](https://www.youtube.com/watch?v=V-tLqN5yp90)

--

**dbwebb - Blekinge Tekniska Högskola**

- [02 cat](https://www.youtube.com/watch?v=a2P26Zgy_mE)

--

**Linux Commands for Beginners**
- [Navigating the Filesystem](https://www.youtube.com/watch?v=MnY0K-3_Fjk)
- [Moving and Renaming Files](https://www.youtube.com/watch?v=cSBYvSA9rDM)

--

**HakTip - Linux Terminal 101**
- [Getting Started](https://www.youtube.com/watch?v=b5NmtmNwMgU)
- [File Manipulation](https://www.youtube.com/watch?v=e13o3DcjT6Y)
- [Using CAT with Standard Inputs](https://www.youtube.com/watch?v=SfuEdUiEFtw)

---

# Slut!