Laboration: VLAN i Cisco IOS

Syfte: Syftet med denna laboration är att förstå och konfigurera Virtual Local Area Networks (VLANs) i en Cisco-switch. Målet är att kunna skapa, konfigurera och hantera VLAN på två switchar utan användning av en router, samt att kontrollera kommunikationen mellan olika VLAN.

Utrustning:

    2 Cisco-switchar (t.ex. Cisco 2960)
    4 datorer (två per switch)
    Konsol-kablar och nätverkskablar för att ansluta enheterna

Förberedelser:

    Starta upp båda switcharna och anslut datorerna till switcharna med hjälp av nätverkskablar.
    Anslut båda switcharna via en Ethernet-kabel.

Laborationssteg:
Steg 1: Konfigurera VLAN på den första switchen

    Logga in på den första switchen via konsol eller telnet.

    Använd följande kommando för att komma till privilegierat läge:

Switch> enable

Gå in i global konfigurationsläge:

Switch# configure terminal

Skapa två VLAN (VLAN 10 och VLAN 20):

Switch(config)# vlan 10
Switch(config-vlan)# name Sales
Switch(config-vlan)# exit
Switch(config)# vlan 20
Switch(config-vlan)# name HR
Switch(config-vlan)# exit

Tilldela VLAN till specifika portar. Antag att du vill tilldela port 1 till VLAN 10 och port 2 till VLAN 20:

Switch(config)# interface range fa0/1 - 2
Switch(config-if-range)# switchport mode access
Switch(config-if-range)# switchport access vlan 10
Switch(config-if-range)# exit

Upprepa för VLAN 20 på port 3:

    Switch(config)# interface range fa0/3 - 4
    Switch(config-if-range)# switchport mode access
    Switch(config-if-range)# switchport access vlan 20
    Switch(config-if-range)# exit

Steg 2: Konfigurera VLAN på den andra switchen

    Logga in på den andra switchen och upprepa samma process för att skapa VLAN 10 och VLAN 20.

    Skapa VLAN och ge dem namn:

Switch2(config)# vlan 10
Switch2(config-vlan)# name Sales
Switch2(config-vlan)# exit
Switch2(config)# vlan 20
Switch2(config-vlan)# name HR
Switch2(config-vlan)# exit

Tilldela VLAN till specifika portar på den andra switchen. Om port 1 är kopplad till datorer i VLAN 10 och port 2 till datorer i VLAN 20, använd följande kommandon:

Switch2(config)# interface range fa0/1 - 2
Switch2(config-if-range)# switchport mode access
Switch2(config-if-range)# switchport access vlan 10
Switch2(config-if-range)# exit

Upprepa för VLAN 20 på port 3:

    Switch2(config)# interface range fa0/3 - 4
    Switch2(config-if-range)# switchport mode access
    Switch2(config-if-range)# switchport access vlan 20
    Switch2(config-if-range)# exit

Steg 3: Testa VLAN-konfigurationen

    Konfigurera IP-adresser på varje dator i respektive VLAN:
        Dator i VLAN 10 får en IP-adress i t.ex. 192.168.10.0/24 (t.ex. 192.168.10.2)
        Dator i VLAN 20 får en IP-adress i t.ex. 192.168.20.0/24 (t.ex. 192.168.20.2)

    Kontrollera att datorerna i samma VLAN kan kommunicera med varandra:
        Från dator 1 (VLAN 10) pinga dator 2 (VLAN 10).
        Från dator 3 (VLAN 20) pinga dator 4 (VLAN 20).

    Kontrollera att datorerna i olika VLAN inte kan kommunicera med varandra (utan en router för routing mellan VLAN).

Steg 4: Verifiera VLAN-konfigurationen

    Använd kommandot show vlan brief för att kontrollera vilka VLAN som är skapade och vilka portar som tillhör varje VLAN.

Switch# show vlan brief

Använd show interfaces för att kontrollera statusen för de konfigurerade portarna.

    Switch# show interfaces status

Steg 5: Skriv en slutsats

Sammanfatta resultatet av laborationen:

    Har VLAN konfigurerats korrekt?
    Kan datorer inom samma VLAN kommunicera med varandra?
    Kan datorer i olika VLAN kommunicera utan en router?

Slutsats: I denna laboration har vi konfigurerat VLAN på två Cisco-switchar utan att använda en router. Vi har sett att VLAN skapar logiskt separerade nätverk där enheter inom samma VLAN kan kommunicera med varandra, men enheter i olika VLAN inte kan kommunicera utan en router.
