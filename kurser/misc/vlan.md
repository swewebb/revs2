---
# VLAN i Cisco IOS

## Introduktion

- **VLAN** står för Virtual Local Area Network
- Används för att segmentera nätverk logiskt
- Förbättrar säkerhet och nätverkseffektivitet
- Stöds av de flesta nätverksutrustningar, inklusive Cisco-switchar

---

## Fördelar med VLAN

- **Segmentering**: Skapar mindre nätverkssegment
- **Säkerhet**: Separering av trafik förhindrar obehörig åtkomst
- **Effektivitet**: Minskad broadcast-trafik
- **Flexibilitet**: Enheter kan vara i samma VLAN oavsett fysisk plats

---

## Grundläggande VLAN-konfiguration

```bash
Switch> enable
Switch# configure terminal
Switch(config)# vlan 10
Switch(config-vlan)# name Sales
Switch(config-vlan)# exit
```

- VLAN 10 skapas och ges namnet "Sales"

---

## Tilldela VLAN till en port

```bash
Switch(config)# interface FastEthernet 0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
Switch(config-if)# exit
```

- Porten **FastEthernet 0/1** tilldelas VLAN 10

---

## Trunk-port för flera VLAN

```bash
Switch(config)# interface GigabitEthernet 0/1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20,30
Switch(config-if)# exit
```

- En trunk-port tillåter trafik från flera VLAN

---

## Verifiering av VLAN-konfiguration

```bash
Switch# show vlan brief
Switch# show interfaces trunk
```

- **`show vlan brief`**: Visar konfigurerade VLAN och deras portar
- **`show interfaces trunk`**: Visar trunk-portar och deras VLAN

---

## Laboration: VLAN med två switchar

### Mål

- Skapa två VLAN: **green (VLAN 10)** och **pink (VLAN 20)**
- Använd VLAN 99 för management
- Konfigurera trunk-länk mellan två switchar

### Konfiguration

#### Switch 1

```bash
Switch1> enable
Switch1# configure terminal
Switch1(config)# vlan 10
Switch1(config-vlan)# name green
Switch1(config-vlan)# exit
Switch1(config)# vlan 20
Switch1(config-vlan)# name pink
Switch1(config-vlan)# exit
Switch1(config)# vlan 99
Switch1(config-vlan)# name management
Switch1(config-vlan)# exit

Switch1(config)# interface GigabitEthernet 0/1
Switch1(config-if)# switchport mode trunk
Switch1(config-if)# switchport trunk allowed vlan 10,20,99
Switch1(config-if)# exit
```

#### Switch 2

```bash
Switch2> enable
Switch2# configure terminal
Switch2(config)# vlan 10
Switch2(config-vlan)# name green
Switch2(config-vlan)# exit
Switch2(config)# vlan 20
Switch2(config-vlan)# name pink
Switch2(config-vlan)# exit
Switch2(config)# vlan 99
Switch2(config-vlan)# name management
Switch2(config-vlan)# exit

Switch2(config)# interface GigabitEthernet 0/1
Switch2(config-if)# switchport mode trunk
Switch2(config-if)# switchport trunk allowed vlan 10,20,99
Switch2(config-if)# exit
```

---

Att undvika VLAN 1 för management är en säkerhets- och nätverksbästa praxis av flera skäl:

1. Standard-VLAN och broadcast-problem

VLAN 1 är standard-VLAN på många switchar, och all okonfigurerad trafik skickas som standard på detta VLAN. Detta innebär att broadcast-, unicast flood- och multicast-trafik kan belasta nätverket och potentiellt störa management-trafik. 2. Sårbarhet för attacker

Eftersom VLAN 1 används av standardprotokoll som CDP, LLDP, VTP och DTP, kan det vara en måltavla för attacker. Om management-trafik körs på VLAN 1 kan en angripare lättare sniffa eller injicera skadlig trafik. 3. Svårt att segmentera nätverket

Att använda VLAN 1 för management innebär att det blir svårare att skapa tydliga nätverkssegment. För en säker och organiserad nätverksdesign bör management-trafik separeras från användardata, gästnätverk och andra system. 4. Oönskad trafik och konfigurationsproblem

VLAN 1 används ofta som ett "default"-VLAN på switchar. Detta kan leda till att management-trafik oavsiktligt blandas med annan trafik om VLAN-konfigurationen inte är strikt definierad. 5. Bästa praxis och rekommendationer

Cisco och andra nätverksleverantörer rekommenderar att man skapar ett dedikerat VLAN för management, t.ex. VLAN 10 eller VLAN 99, och konfigurerar switchar och accesspunkter att endast tillåta nödvändig management-trafik på detta VLAN.
Rekommenderad lösning

    Skapa ett dedikerat management VLAN (exempelvis VLAN 10).
    Konfigurera switchar och enheter att använda detta VLAN för management.
    Begränsa access till management-VLAN genom ACL:er eller private VLANs.
    Se till att management-VLAN inte är tillgängligt från vanliga användarnätverk.

Att använda ett separat VLAN för management ökar säkerheten och gör nätverket mer stabilt och hanterbart. 🚀

---

# KONNAAA

## Skapa VLAN 99 och tilldela en IP-adress

conf t
!
vlan 99
name Management
!
interface vlan 99
ip address 192.168.10.10 255.255.255.0
no shutdown
!

## Blockera VLAN 1 på trunkportar

interface range GigabitEthernet0/1 - 48
switchport trunk allowed vlan remove 1
!

## Ställa in en management-port (exempel: Gig0/24)

interface GigabitEthernet0/24
description Management Port
switchport mode access
switchport access vlan 99
!

## Konfigurera SSH och lokal autentisering

hostname Switch01
!
ip domain-name example.local
!
crypto key generate rsa
modulus 2048
!
ip ssh version 2
!
username admin privilege 15 secret MySecurePassword
!
line vty 0 4
transport input ssh
login local
!

## Förbättra säkerheten

access-list 10 permit 192.168.10.0 0.0.0.255
!
line vty 0 4
access-class 10 in
!

Detta gör så att endast enheter i 192.168.10.0/24 kan ansluta till switchen via SSH.

---

# Lägg till Port Security på accessportar

Port Security används för att förhindra obehöriga enheter från att ansluta till switchen genom att begränsa antalet tillåtna MAC-adresser per port.

Här är en säker konfiguration för accessportar (t.ex. VLAN 99 för management och klientnätverk):

## Aktivera Port Security på accessportar

interface range GigabitEthernet0/1 - 23
switchport mode access
switchport port-security
switchport port-security maximum 2
switchport port-security violation restrict
switchport port-security mac-address sticky

Aktiverar Port Security
🔹 Tillåter max 2 MAC-adresser per port
🔹 Vid okänd MAC-adress: "Restrict" (blockerar men loggar händelsen)
🔹 Sticky MAC-adresser lär sig automatiskt och sparas

## Aktivera Port Security på management-porten (Gig0/24)

interface GigabitEthernet0/24
switchport mode access
switchport access vlan 99
switchport port-security
switchport port-security maximum 1
switchport port-security violation shutdown
switchport port-security mac-address sticky

🔹 Management-porten tillåter endast 1 MAC-adress
🔹 Shutdown-läge används vid obehörig enhet (porten måste manuellt återaktiveras)

## Åtgärda blockerad port (om en okänd MAC-adress ansluter)

Om en port stängs av (violation shutdown) måste den återaktiveras:

interface GigabitEthernet0/24
shutdown
no shutdown

## Visa Port Security-status

Se vilka MAC-adresser som är lärda och vilka portar som har säkerhetsincidenter:

show port-security
show port-security interface GigabitEthernet0/24

---

# Storm Control för att begränsa skadlig broadcast, multicast och unicast-flooding

## Aktivera Storm Control på accessportar

interface range GigabitEthernet0/1 - 23
storm-control broadcast level 5.00
storm-control multicast level 5.00
storm-control unicast level 10.00
storm-control action shutdown

🔹 Begränsar Broadcast och Multicast till 5% av portens bandbredd
🔹 Begränsar okänd Unicast-trafik till 10%
🔹 Om en gräns överskrids → Porten stängs av (shutdown-läge)

## Aktivera Storm Control på management-porten (Gig0/24)

interface GigabitEthernet0/24
storm-control broadcast level 2.00
storm-control multicast level 2.00
storm-control unicast level 5.00
storm-control action restrict

🔹 Strängare regler för management-porten
🔹 Om gränsen överskrids → Restrict-läge (begränsar men stänger inte av porten)

## Åtgärda en blockerad port

Om en port stängs av pga Storm Control kan du återaktivera den manuellt:

interface GigabitEthernet0/X
shutdown
no shutdown

## Visa Storm Control-status

show storm-control
show storm-control interface GigabitEthernet0/24

🔹 Visar aktiva begränsningar och om några portar har blockerat trafik

---

# DHCP Snooping för att skydda nätverket från falska DHCP-servrar

## Aktivera DHCP Snooping på switchen

conf t
!
ip dhcp snooping
ip dhcp snooping vlan 99
ip dhcp snooping vlan 10
ip dhcp snooping vlan 20
ip dhcp snooping vlan 30
!

🔹 Aktiverar DHCP Snooping globalt och på relevanta VLAN (t.ex. VLAN 99 för management och VLAN 10, 20, 30 för klienter)

## Ange betrodda och obetrodda portar

Betrodda portar ska endast finnas på trunkar eller uplink-portar där en riktig DHCP-server är ansluten.

interface GigabitEthernet0/1
description Uplink to Router/DHCP Server
ip dhcp snooping trust
!
interface range GigabitEthernet0/2 - 48
description Access Ports (Clients)
ip dhcp snooping limit rate 10
!

🔹 Gig0/1 är en betrodd port (DHCP-servern är ansluten här)
🔹 Alla andra accessportar är obetrodda och begränsar DHCP-svar till max 10 per sekund

## Förhindra attacker med Option 82

Option 82 används för att verifiera legitima DHCP-förfrågningar:

ip dhcp snooping information option allow-untrusted

🔹 Tillåter Option 82 i vissa scenarier, men blockerar oönskad manipulation

## Kontrollera att DHCP Snooping är aktiverat

show ip dhcp snooping
show ip dhcp snooping binding

🔹 Visar aktiva DHCP-bindingar och status på DHCP Snooping

---

# Dynamic ARP Inspection (DAI) för att skydda mot ARP-spoofing

Dynamic ARP Inspection (DAI) förhindrar ARP-spoofing-attacker genom att säkerställa att endast giltiga ARP-meddelanden tillåts på nätverket. DAI använder DHCP Snooping Binding Table för att verifiera att ARP-förfrågningar kommer från legitima enheter.

1️⃣ Aktivera DAI på switchen

conf t
!
ip arp inspection vlan 99
ip arp inspection vlan 10
ip arp inspection vlan 20
ip arp inspection vlan 30
!

🔹 Aktiverar ARP-inspektion på VLAN 99 (management) samt klient-VLAN (10, 20, 30)
2️⃣ Definiera betrodda och obetrodda portar

Precis som med DHCP Snooping, bör endast uplink-portar mot betrodda nätverksenheter (exempelvis routrar och DHCP-servrar) vara "trusted". Alla andra portar är "untrusted" som standard.

interface GigabitEthernet0/1
description Uplink to Router/DHCP Server
ip arp inspection trust
!
interface range GigabitEthernet0/2 - 48
description Access Ports (Clients)
ip arp inspection limit rate 100
!

🔹 Gig0/1 är betrodd (kopplad till router eller DHCP-server)
🔹 Alla klientportar är obetrodda och begränsas till max 100 ARP-paket per sekund för att förhindra överbelastningsattacker
3️⃣ Kontrollera och felsöka DAI

Se vilka ARP-förfrågningar som blockeras:

show ip arp inspection statistics
show ip arp inspection vlan 99
show ip arp inspection interfaces

🔹 Visar om några attacker upptäcks och vilka portar som inspekteras

Om en legit enhet blockeras av DAI kan du manuellt lägga till en statisk ARP-binding:

arp access-list STATIC_ARP
permit ip 192.168.10.50 mac 00a1.b2c3.d4e5
!
ip arp inspection filter STATIC_ARP vlan 99 static

🔹 Tvingar switchen att godkänna en specifik MAC-IP-kombination

---

# BPDU Guard för att skydda STP och förhindra oönskade switchar

BPDU Guard används för att förhindra anslutning av obehöriga switchar genom att blockera BPDU-meddelanden på accessportar. Om en port tar emot en BPDU (som används för Spanning Tree Protocol), stänger BPDU Guard automatiskt av porten för att förhindra nätverksloopar och STP-attacker.
1️⃣ Aktivera BPDU Guard på accessportar

conf t
!
interface range GigabitEthernet0/2 - 48
description Access Ports (Clients)
spanning-tree portfast
spanning-tree bpduguard enable
!

🔹 PortFast aktiveras, vilket innebär att porten direkt går till forwarding state utan att vänta på STP
🔹 BPDU Guard stänger av porten om den tar emot ett BPDU-meddelande
2️⃣ Aktivera BPDU Guard globalt (gäller alla PortFast-portar)

spanning-tree portfast default
spanning-tree bpduguard default

🔹 Aktiverar BPDU Guard automatiskt på alla PortFast-portar
3️⃣ Återställa en port som har stängts av av BPDU Guard

Om en port tar emot BPDU och stängs av (err-disable) kan du manuellt återaktivera den:

interface GigabitEthernet0/X
shutdown
no shutdown

För att automatiskt återaktivera porten efter en viss tid:

errdisable recovery cause bpduguard
errdisable recovery interval 60

🔹 Porten återställs automatiskt efter 60 sekunder
4️⃣ Kontrollera BPDU Guard-status

show spanning-tree summary
show spanning-tree interface GigabitEthernet0/24

🔹 Visar vilka portar som har BPDU Guard aktiverat och om några har stängts av

---

# Root Guard för att skydda STP-topologin

Root Guard används för att förhindra obehöriga switchar från att bli STP Root Bridge, vilket kan leda till nätverksinstabilitet eller attacker där en angripare försöker ta kontroll över Spanning Tree-topologin.
1️⃣ Aktivera Root Guard på betrodda uplink-portar

Root Guard ska endast aktiveras på gränssnitt där det inte ska komma en ny Root Bridge, t.ex. på access-switchars uplinks mot distributions- eller core-switchar.

conf t
!
interface GigabitEthernet0/1
description Uplink to Core/Distribution Switch
spanning-tree guard root
!

🔹 Om en Root Bridge-annons (superior BPDU) tas emot på denna port → Porten går i "Root-Inconsistent" state och blockerar trafiken
2️⃣ Kontrollera Root Guard-status

För att se om någon port har satts i Root-Inconsistent state:

show spanning-tree inconsistentports

🔹 Visar om någon port har blockerats av Root Guard
3️⃣ Återställa en port som har blockerats av Root Guard

Om en port satts i Root-Inconsistent state, och du har löst nätverksproblemet, återaktivera den manuellt:

interface GigabitEthernet0/1
shutdown
no shutdown

Eller vänta – så fort den felaktiga BPDU:n slutar tas emot kommer Root Guard att återställa porten automatiskt.

---

# MAC Address Spoofing Protection och IP Source Guard för att stärka säkerheten

MAC Address Spoofing Protection och IP Source Guard är två funktioner som skyddar nätverket mot attacker där angripare försöker maskera sina MAC- eller IP-adresser för att komma åt nätverket. Här är hur du aktiverar dessa skydd.
1️⃣ MAC Address Spoofing Protection (Port Security)

Port Security används för att skydda mot MAC-adress spoofing genom att tillåta ett definierat antal MAC-adresser per port och blockera alla andra. Detta förhindrar att en angripare använder en annan enhets MAC-adress för att få tillgång till nätverket.

conf t
!
interface range GigabitEthernet0/1 - 48
switchport mode access
switchport port-security
switchport port-security maximum 2
switchport port-security violation restrict
switchport port-security mac-address sticky
!

🔹 Tillåter max 2 MAC-adresser per port
🔹 Restrict-läge innebär att porten blockerar obehöriga enheter, men loggar händelsen
🔹 Sticky MAC-adresser lär sig automatiskt och sparar de MAC-adresser som är anslutna till portarna
2️⃣ IP Source Guard (Skyddar mot IP-spoofing)

IP Source Guard blockerar trafik från IP-adresser som inte matchar de som är associerade med en port i DHCP Snooping Binding Table. Det förhindrar attacker där en enhet försöker spoofa sin IP-adress för att lura nätverket.

För att aktivera IP Source Guard krävs att DHCP Snooping redan är aktiverat, eftersom det använder DHCP-leases för att identifiera giltiga IP-adresser för varje port.

conf t
!
interface range GigabitEthernet0/1 - 48
ip verify source
!

🔹 Verifierar att IP-adresser matchar DHCP-leases och blockerar all trafik med en felaktig IP-adress
🔹 Skyddar mot IP-spoofing-attacker genom att använda en binding table från DHCP Snooping
3️⃣ Konfigurera för att blockera ogiltiga IP/MAC-kombinationer

För att förbättra säkerheten ytterligare kan du ställa in att IP Source Guard ska blockera alla paket med ogiltiga IP och MAC-kombinationer:

ip source binding 192.168.10.10 00a1.b2c3.d4e5 vlan 99 interface GigabitEthernet0/24
!

🔹 Binder en IP-adress och en MAC-adress till en specifik port för att säkerställa att endast den enheten kan kommunicera med den IP-adressen
4️⃣ Kontrollera IP Source Guard och Port Security-status

För att verifiera att IP Source Guard och Port Security fungerar som de ska, använd följande kommandon:

show ip source binding
show port-security
show port-security interface GigabitEthernet0/24

🔹 Visar aktiva IP-MAC-bindingar och portens säkerhetsstatus

---

# NTP Authentication för att säkra NTP-kommunikation

NTP Authentication skyddar nätverket från falska NTP-servrar som kan manipulera tidssynkronisering, vilket är kritiskt för säkerheten och drift i nätverken. Genom att använda autentisering för NTP-synkronisering kan du se till att endast auktoriserade servrar används för att synkronisera tid.
1️⃣ Aktivera NTP och konfiguration av autentisering

För att aktivera NTP autentisering och konfigurera den på switchen, följ dessa steg:

conf t
!
ntp authenticate
ntp authentication-key 1 md5 YourSecretKey
ntp trusted-key 1
!

🔹 ntp authenticate aktiverar autentisering för NTP.
🔹 ntp authentication-key 1 md5 YourSecretKey skapar en MD5 autentiseringstangent (ersätt "YourSecretKey" med din egen nyckel).
🔹 ntp trusted-key 1 markerar nyckeln som betrodd och gör den användbar för autentisering.
2️⃣ Konfigurera NTP-servern med autentisering

Lägg till den betrodda NTP-servern och använd den autentiseringstangent som definierades ovan:

ntp server 192.168.10.100 key 1

🔹 192.168.10.100 är IP-adressen för den betrodda NTP-servern.
🔹 key 1 innebär att autentisering med nyckel 1 används för att verifiera serverns äkthet.
3️⃣ Kontrollera NTP-konfigurationen

För att verifiera att NTP Autentisering är aktiverat och att den synkroniserade tiden är korrekt, använd följande kommandon:

show ntp status
show ntp associations
show ntp authentication

🔹 show ntp status visar om enheten är korrekt synkroniserad med en betrodd NTP-server.
🔹 show ntp associations visar detaljer om NTP-anslutningar och deras status.
🔹 show ntp authentication visar status för autentisering och de nycklar som används.
4️⃣ Hantera felaktig autentisering

Om autentiseringen misslyckas eller om en obehörig server försöker synkronisera tiden, kommer du att se ett varningsmeddelande om att autentisering misslyckades. För att hantera detta kan du kontrollera loggarna:

show logging

🔹 Detta ger dig information om eventuella autentiseringsproblem och hjälper till att felsöka.
