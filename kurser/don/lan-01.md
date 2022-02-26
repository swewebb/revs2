# Introduktion nätverk

---

# Fördelar och nackdelar med nätverk

--

## Fördelar

Lättare, billigare och enklare att kommunicera med varandra.

Man kan arbeta, styra och övervaka saker på distans.

Alla har tillgång till samma information samtidigt.

Underlättar programuppdateringar till alla.

Lättare att säkerhetskopiera data.

Enklare att dela på gemensamma resurser, som skrivare, servrar, internetuppkopplingar etc.

Lättare att koppla ihop datorkomponenter från olika tillverkare.

--

## Nackdelar

Någon måste sköta nätverket.

Administration kostar pengar.

Systemet är sårbart.

Om nätverket slutar fungera blir det stora problem.

Känslig information kan lätt kopieras, skickas och avlyssnas.

Utvecklingen går snabbt vilket gör att man ofta måste uppgradera sitt system.

---

# Hastighet

--

Kilobit, Megabit och Gigabit

bps, b/s, bit/s

Seriellt!

100Mbps != 100 MBps

100Mbps / 8 = 12,5 MB/s

"Internet hemma" = Upp- och nedladdning

---

# Nätverk

--

PAN - LAN - MAN - WAN

--

## PAN

Personal Area Network

Allra minsta nätverket, ca. ett par meter

Bluetooth, IR

--

## LAN

Local Area Network

Lokalt nätverk, fastighetsnät

Begränsad geografisk spridning

Hög överföringshastighet

Ägs och hanteras av ägaren själv (företaget…)

Oberoende av kommersiella tele- och datanät.

Möjlighet att ansluta olika typer av utrustning.

--

## MAN

Metropolitan Area Network

Stadsnät

Större geografisk utsträckning

Lägre lägsta överföringshastighet än i LAN

Nätet behöver inte ägas i sin helhet av brukaren.

[http://www.gastabudstaden.se/](http://www.gastabudstaden.se/)

--

## WAN

Wide Area Network

Stor utsträckning (land, världsdel, värld)

Internet bygger på flera WAN:s

---

# Nätverkstopologier

--

## Bussnät

I ett bussnät kopplas alla enheterna samman längst en gemensam buss.

Ofta koaxialkablar i nätverk (LAN).

CAN-bussen i fordon

--

## Ringnät

Noderna är kopplade till varandra utan någon central enhet.

Detta är möjligt eftersom alla datorer har två anslutningar, en från föregående dator och en till nästa dator.

En nackdel med ringnät är att de är relativt känsliga för störningar.

Ringnät är inte speciellt vanliga idag utan idag byggs i huvudsak stjärnnät när man bygger ett nytt nätverk (LAN)

--

## Stjärnnät

Alla noder är kopplade till en central punkt som kallas för nav, t.ex en hubb eller switch.

Är den vanligaste topologin i nyinstallerade nätverk idag.

Den är billig att installera och om någon del av nätverket fallerar behöver inte nödvändigtvis hela nätet påverkas.

---

# Fysisk och logisk topologi

--

Fysisk topologi = Hur nätverket är byggt

Logisk topologi = Hur nätverket fungerar

--

Ethernet med hubb

Fysisk stjärna

Logisk buss

--

Token Ring

Fysisk stjärna

Logisk ring

---

# Nätverkskortet

--

Är gränssnittet mellan dator och nätverk

Transportera info från/till nätverket

Om (gammal) PCI, omvandla datan mellan parallell (i datorn) och seriell (på nätverket)

--

BILD

--

## RJ45

Vanligaste kontakten i dag.

BILD

--

## Fiber

BILD

--

## BNC

Riktigt "old school"

BILD

--

## MAC-adressen

BILD

Alla kort innehåller en unik inbränd adress, MAC-adressen.

MAC-adressen är fysisk adress som man inte kan byta (nja…)

MAC-adressen är 48-bitar lång.

ipconfig /all

--

BILD

Indelad i två delar

Del 1, OUI, är en adress för varje tillverkare.

Del 2 är löpnummer.

Använder vanligen hex för att förkorta.

Kan skrivas på olika sätt, ingen standard

---

# Överföringsmedia – Trådat nätverk

--

## Twisted Pair

Den kabeltyp vi kommer att koncentrera oss på.

Ni ska ha en grundläggande kunskap om kablar, de som utbildar sig till elektriker ska ha en djupare kunskap om olika kabeltyper.

--

## Twisted Pair – U/UTP

Unshielded twisted pair

Vanligaste typen idag

Kallas vanligen UTP

--

## Twisted Pair – F/UTP

En folie runt alla paren

Kallas även ScTP, Screened Twisted Pair

--

## Twisted Pair - Sammanställning

BILD

## Twisted Pair - Kategorier

**Cat 5**

Används i Fast Ethernet/100Base-TX

Har en hastighet på 100 Mbps.

**Cat 5e**

Används för Fast Ethernet.

Stöder hastigheter upp till 1Gbps

**Cat 6**

Används i Gigabit Ethernet/1000BASE-T-nätverk.

Stöder 10Gbps upp till 55m.

**Cat 6a**

10Gbps upp till 100m

--

## Kabeltyper

### Straight-through (patch, rak) kabel

Används för att koppla samman olika typer av utrustning.

### Crossover (korsad) kabel

Används för att koppla samman lika typer av utrustning.
