Laboration: Implementering och Konfiguration av VLAN i Cisco IOS

Kurs: Nätverksteknologier
Mål: Att förstå och implementera VLAN (Virtual Local Area Network) i en Cisco IOS-miljö, använda två switchar för att skapa ett segmenterat nätverk, och konfigurera VLAN utan att använda en router.
Förutsättningar: Grundläggande förståelse för nätverkskonfigurationer och användning av Cisco IOS.

1. Introduktion

VLAN är en teknik som används för att dela upp ett fysiskt nätverk i flera logiska nätverk. Detta möjliggör bättre nätverkshantering, ökad säkerhet och effektiv användning av bandbredd. I denna laboration ska vi konfigurera VLAN på två Cisco-switchar (utan en router), vilket kommer att segmentera trafik mellan olika enheter i nätverket.

Denna laboration syftar till att skapa två VLAN på två Cisco-switchar, konfigurera trunk-portar mellan switcharna, samt testa kommunikationen mellan enheter inom samma VLAN och mellan olika VLAN. 2. Utrustning och material

    Två Cisco-switchar (t.ex. Cisco Catalyst 2960)
    Fyra datorer eller virtuella maskiner (dessa kommer att tilldelas till olika VLAN)
    Konsol eller terminal för att ansluta till switcharna

3. Topologi

   Switch 1 (SW1): Huvud-switch
   Switch 2 (SW2): Sekundär switch
   VLAN 10: Första nätverket (t.ex. för HR-enheter)
   VLAN 20: Andra nätverket (t.ex. för IT-enheter)
   Trunkport: Anslutning mellan Switch 1 och Switch 2 (Port 24 på båda switcharna)

Datorer:
Dator A (VLAN 10) — Switch 1
Dator B (VLAN 10) — Switch 1
Dator C (VLAN 20) — Switch 2
Dator D (VLAN 20) — Switch 2

Switch 1 <-----> Switch 2

4.  Steg för konfiguration
    4.1. Skapa VLAN på Switch 1 och Switch 2

        Anslut till Cisco-switcharna via terminalen och logga in med administratörsbehörighet.
        Konfigurera VLAN på båda switcharna.

På Switch 1 (SW1):

SW1# configure terminal
SW1(config)# vlan 10
SW1(config-vlan)# name HR
SW1(config-vlan)# exit
SW1(config)# vlan 20
SW1(config-vlan)# name IT
SW1(config-vlan)# exit

På Switch 2 (SW2):

SW2# configure terminal
SW2(config)# vlan 10
SW2(config-vlan)# name HR
SW2(config-vlan)# exit
SW2(config)# vlan 20
SW2(config-vlan)# name IT
SW2(config-vlan)# exit

4.2. Tilldela portar till VLAN

På Switch 1 (SW1):

    Tilldela Port 1 och Port 2 till VLAN 10 (HR)
    Tilldela Port 3 och Port 4 till VLAN 20 (IT)

SW1(config)# interface range fa0/1 - 2
SW1(config-if-range)# switchport mode access
SW1(config-if-range)# switchport access vlan 10
SW1(config-if-range)# exit
SW1(config)# interface range fa0/3 - 4
SW1(config-if-range)# switchport mode access
SW1(config-if-range)# switchport access vlan 20
SW1(config-if-range)# exit

På Switch 2 (SW2):

    Tilldela Port 1 och Port 2 till VLAN 10 (HR)
    Tilldela Port 3 och Port 4 till VLAN 20 (IT)

SW2(config)# interface range fa0/1 - 2
SW2(config-if-range)# switchport mode access
SW2(config-if-range)# switchport access vlan 10
SW2(config-if-range)# exit
SW2(config)# interface range fa0/3 - 4
SW2(config-if-range)# switchport mode access
SW2(config-if-range)# switchport access vlan 20
SW2(config-if-range)# exit

4.3. Konfigurera Trunkport mellan Switch 1 och Switch 2

På Switch 1 (SW1):

SW1(config)# interface fa0/24
SW1(config-if)# switchport mode trunk
SW1(config-if)# switchport trunk allowed vlan 10,20
SW1(config-if)# exit

På Switch 2 (SW2):

SW2(config)# interface fa0/24
SW2(config-if)# switchport mode trunk
SW2(config-if)# switchport trunk allowed vlan 10,20
SW2(config-if)# exit

4.4. Verifiering av VLAN-konfiguration

För att säkerställa att VLAN-konfigurationen har genomförts korrekt kan följande kommandon användas:

På Switch 1 (SW1):

SW1# show vlan brief

På Switch 2 (SW2):

SW2# show vlan brief

Dessa kommandon ska visa de VLAN som skapats och tilldelade portar.
4.5. Testa kommunikation mellan enheter

För att testa VLAN-konfigurationen kan enheterna på samma VLAN (t.ex. Dator A och Dator B i VLAN 10) kommunicera med varandra. Testa detta genom att pinga mellan enheterna på samma VLAN.

Exempelvis, pinga från Dator A till Dator B:

C:\> ping [IP-adressen på Dator B]

För att testa att VLAN-segmenteringen fungerar, försök att pinga mellan Dator A (VLAN 10) och Dator C (VLAN 20). Kommunikationen ska inte vara möjlig, eftersom de befinner sig i olika VLAN.
4.6. Ta bort VLAN

Om VLAN-konfigurationen behöver tas bort, använd följande kommando:

På Switch 1 (SW1):

SW1(config)# no vlan 10
SW1(config)# no vlan 20

På Switch 2 (SW2):

SW2(config)# no vlan 10
SW2(config)# no vlan 20

5. Slutsats

Genom denna laboration har VLAN-konfigurationen implementerats på två Cisco-switchar. Genom att använda trunkportar har kommunikationen mellan de olika VLANen på de två switcharna möjliggjorts. Segregationen av trafik mellan olika VLAN har också bekräftats genom tester, vilket demonstrerar fördelarna med VLAN-tekniken i att förbättra nätverkshantering och säkerhet.

VLAN-tekniken gör det möjligt att segmentera nätverk baserat på funktioner, avdelningar eller säkerhetskrav, vilket förbättrar både nätverksprestanda och hanterbarhet.

---

Laboration: Implementering av Management VLAN och SSH-konfiguration i Cisco IOS

Mål: Att konfigurera ett separat management VLAN på två Cisco-switchar, sätta upp en management IP-adress för varje switch och konfigurera SSH för fjärrhantering.

1. Introduktion

I denna del av laborationen kommer vi att lägga till ett management VLAN (t.ex. VLAN 99) på varje switch och tilldela IP-adresser för detta VLAN. Vi kommer också att konfigurera SSH för att tillåta säker fjärråtkomst till switcharna, och skapa lokala användarkonton för autentisering. 2. Steg för konfiguration
2.1. Skapa och konfigurera Management VLAN (VLAN 99)

Först skapar vi VLAN 99 på båda switcharna och tilldelar portarna som ska vara en del av management VLAN.

På Switch 1 (SW1):

SW1# configure terminal
SW1(config)# vlan 99
SW1(config-vlan)# name Management
SW1(config-vlan)# exit

På Switch 2 (SW2):

SW2# configure terminal
SW2(config)# vlan 99
SW2(config-vlan)# name Management
SW2(config-vlan)# exit

2.2. Tilldela IP-adresser till Management VLAN på varje switch

För att kunna administrera switcharna via nätverket, måste vi tilldela en IP-adress till Management VLAN 99 på varje switch.

På Switch 1 (SW1):

SW1# configure terminal
SW1(config)# interface vlan 99
SW1(config-if)# ip address 192.168.10.10 255.255.255.0
SW1(config-if)# no shutdown
SW1(config-if)# exit

På Switch 2 (SW2):

SW2# configure terminal
SW2(config)# interface vlan 99
SW2(config-if)# ip address 192.168.10.11 255.255.255.0
SW2(config-if)# no shutdown
SW2(config-if)# exit

2.3. Konfigurera standard gateway för switcharna

För att switcharna ska kunna nå varandra eller andra nätverksresurser, konfigurera en default gateway på varje switch. Eftersom vi inte använder en router i denna laboration, kan vi använda den enhetens IP-adress som fungerar som gateway.

På Switch 1 (SW1):

SW1# configure terminal
SW1(config)# ip default-gateway 192.168.10.1
SW1(config)# exit

På Switch 2 (SW2):

SW2# configure terminal
SW2(config)# ip default-gateway 192.168.10.1
SW2(config)# exit

2.4. Aktivera SSH på switcharna

För att säkerställa att endast auktoriserade användare kan logga in på switcharna via SSH, ska vi konfigurera SSH och skapa lokala användarkonton. För detta ändamål måste vi också skapa en domain-namn och konfigurera en kryptografisk nyckel.

På Switch 1 (SW1):

    Aktivera SSH och ställ in ett domännamn:

SW1# configure terminal
SW1(config)# ip domain-name example.com

    Skapa en RSA-nyckel för SSH:

SW1(config)# crypto key generate rsa

Du blir ombedd att ange storleken på RSA-nyckeln, välj en nyckelstorlek på 1024 bits.

    Skapa en lokal användare och tilldela en lösenord:

SW1(config)# username admin privilege 15 secret adminpassword

    Aktivera SSH-servern:

SW1(config)# line vty 0 15
SW1(config-line)# login local
SW1(config-line)# transport input ssh
SW1(config-line)# exit

    Kontrollera SSH-konfigurationen:

SW1# show ip ssh

På Switch 2 (SW2):

    Aktivera SSH och ställ in ett domännamn:

SW2# configure terminal
SW2(config)# ip domain-name example.com

    Skapa en RSA-nyckel för SSH:

SW2(config)# crypto key generate rsa

Välj en nyckelstorlek på 1024 bits.

    Skapa en lokal användare och tilldela en lösenord:

SW2(config)# username admin privilege 15 secret adminpassword

    Aktivera SSH-servern:

SW2(config)# line vty 0 15
SW2(config-line)# login local
SW2(config-line)# transport input ssh
SW2(config-line)# exit

    Kontrollera SSH-konfigurationen:

SW2# show ip ssh

2.5. Testa SSH-åtkomst

För att testa SSH-konfigurationen, använd en SSH-klient (som PuTTY eller en terminal) för att logga in på switcharna.

För att logga in på Switch 1:

ssh admin@192.168.10.10

För att logga in på Switch 2:

ssh admin@192.168.10.11

Använd det lokala användarnamnet och lösenordet ("admin" och "adminpassword") för att autentisera.
2.6. Verifiera IP-konfiguration och SSH-åtkomst

För att verifiera IP-konfigurationen på varje switch, använd kommandot:

På Switch 1 (SW1):

SW1# show ip interface brief

På Switch 2 (SW2):

SW2# show ip interface brief

Kontrollera att VLAN 99 har fått rätt IP-adress och är "up". 3. Slutsats

Genom denna laboration har vi implementerat ett separat management VLAN (VLAN 99) på båda switcharna, konfigurerat IP-adresser för management-access, och satt upp SSH för säker fjärrhantering. Genom att skapa lokala användare och autentisering med SSH säkerställs att endast behöriga användare kan administrera switcharna.

Denna typ av konfiguration är viktig i nätverksmiljöer där säkerhet och fjärråtkomst är avgörande för effektiv nätverkshantering.
