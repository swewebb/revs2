Laboration: VLAN-konfiguration i Cisco IOS med två switchar

Syfte: Syftet med denna laboration är att skapa och konfigurera Virtual LANs (VLAN) i ett nätverk bestående av två switchar utan användning av en router. Vi kommer att skapa olika VLAN, tilldela portar till dessa VLAN och verifiera att VLAN-konfigurationen fungerar korrekt.

Material:

    2 st Cisco-switchar (t.ex. Cisco 2960)
    Datorer som ansluts till switcharna
    Console-kabel och tillgång till terminalprogram (t.ex. PuTTY eller Tera Term)

Förutsättningar:

    Grundläggande kunskaper om VLAN och nätverkskonfiguration.
    Grundläggande förståelse för hur man använder Cisco IOS-kommandon.
    Förmåga att konfigurera och hantera switchar i Cisco IOS-miljö.

Arbetsgång:
Steg 1: Förberedelse av utrustning

    Anslut båda switcharna till strömförsörjning.
    Anslut datorer till varje switch, på olika portar (t.ex. port 1 på Switch 1, port 2 på Switch 2).
    Anslut en dator eller terminal till en av switcharnas konsolport och starta terminalprogrammet.

Steg 2: Grundläggande konfiguration av switcharna

    Logga in på Cisco-switcharna via terminalen:

Switch> enable
Switch# configure terminal

Ge switcharna namn för att identifiera dem lättare:

    Switch(config)# hostname Switch1

Steg 3: Skapa VLAN

    Skapa de VLAN som du ska använda. Vi kommer att skapa två VLAN: VLAN 10 och VLAN 20.

    För Switch 1:

Switch1(config)# vlan 10
Switch1(config-vlan)# name Marketing
Switch1(config-vlan)# exit

Switch1(config)# vlan 20
Switch1(config-vlan)# name Sales
Switch1(config-vlan)# exit

För Switch 2:

    Switch2(config)# vlan 10
    Switch2(config-vlan)# name Marketing
    Switch2(config-vlan)# exit

    Switch2(config)# vlan 20
    Switch2(config-vlan)# name Sales
    Switch2(config-vlan)# exit

Steg 4: Tilldela portar till VLAN

    På Switch 1 tilldelar vi portar till respektive VLAN. T.ex. tilldelar vi port 1 till VLAN 10 och port 2 till VLAN 20.

Switch1(config)# interface range fa0/1 - 1
Switch1(config-if-range)# switchport mode access
Switch1(config-if-range)# switchport access vlan 10
Switch1(config-if-range)# exit

Switch1(config)# interface range fa0/2 - 2
Switch1(config-if-range)# switchport mode access
Switch1(config-if-range)# switchport access vlan 20
Switch1(config-if-range)# exit

På Switch 2 gör vi samma sak. Tilldela port 1 till VLAN 10 och port 2 till VLAN 20.

    Switch2(config)# interface range fa0/1 - 1
    Switch2(config-if-range)# switchport mode access
    Switch2(config-if-range)# switchport access vlan 10
    Switch2(config-if-range)# exit

    Switch2(config)# interface range fa0/2 - 2
    Switch2(config-if-range)# switchport mode access
    Switch2(config-if-range)# switchport access vlan 20
    Switch2(config-if-range)# exit

Steg 5: Konfigurera trunkport mellan switcharna

För att switcharna ska kunna kommunicera med varandra mellan VLAN, behöver vi konfigurera trunking på porten mellan switcharna. Anta att vi använder port 24 på båda switcharna för trunking.

    På Switch 1:

Switch1(config)# interface fa0/24
Switch1(config-if)# switchport mode trunk
Switch1(config-if)# switchport trunk allowed vlan 10,20
Switch1(config-if)# exit

På Switch 2:

    Switch2(config)# interface fa0/24
    Switch2(config-if)# switchport mode trunk
    Switch2(config-if)# switchport trunk allowed vlan 10,20
    Switch2(config-if)# exit

Steg 6: Verifiering av konfigurationen

    Kontrollera VLAN-konfigurationen på båda switcharna:

Switch1# show vlan brief
Switch2# show vlan brief

Kontrollera trunkstatus:

Switch1# show interfaces trunk
Switch2# show interfaces trunk

Kontrollera att portarna har tilldelats rätt VLAN:

    Switch1# show running-config
    Switch2# show running-config

    Testa kommunikationen mellan enheter i samma VLAN men på olika switchar. Till exempel, om en dator är ansluten till port 1 på Switch 1 (VLAN 10) och en annan dator är ansluten till port 1 på Switch 2 (VLAN 10), bör de kunna kommunicera.

    Testa att enheter på olika VLAN (t.ex. en dator på VLAN 10 och en på VLAN 20) inte kan kommunicera med varandra.

Steg 7: Dokumentation och avslutning

    Skriv en kort rapport som dokumenterar alla kommandon du har använt under laborationen och resultaten av de tester du har genomfört.
    Återställ switcharna till sina ursprungliga inställningar om det krävs, eller stäng av utrustningen.

Frågor för reflektion:

    Vad händer om trunkporten inte är korrekt konfigurerad?
    Vad skulle krävas för att möjliggöra kommunikation mellan VLAN, om en router inte finns tillgänglig?
    Vad är skillnaden mellan ett accessport och en trunkport på en switch?

Sammanfattning: I denna laboration har vi skapat och konfigurerat två VLAN på två Cisco-switchar utan att använda en router. Vi har tilldelat portar till olika VLAN, konfigurerat trunking mellan switcharna, och verifierat att VLAN-konfigurationen fungerar korrekt.
