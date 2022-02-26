# Linux-08

## Pakethantering

---

# Pakethanterare

--

Det finns en mängd olika pakethanterare t.ex **apt**, **yum**, **dnf**, **pacman**

Vi kommer att inrikta oss på **apt** som Ubuntu använder sig av.

---

# APT

--

Används för att installera, ta bort, uppdatera, uppgradera etc paket.

Hanterar automatiskt beroenden som ett paket som ska installeras (möjligen) har.

--

## Läsa in aktuella paket

```text
apt update
```

--

## Uppdatera paketen

```text
sudo apt upgrade
```

--

## Installera paket

```text
sudo apt install paket1 paket2
```

--

## Ta bort paket

```text
sudo apt remove paket
```

```text
sudo apt purge paket
```

```text
sudo apt autoremove
```

--

## Söka

```text
apt search namn
```

--

## Visa information

```text
apt show namn
```

--

## Lista

```text
apt list --installed
```

```text
apt list --upgradable
```

---

# Uppdatera till en ny <br>version av Ubuntu

--

```text
sudo do-release-upgrade
```

---

# Slut!