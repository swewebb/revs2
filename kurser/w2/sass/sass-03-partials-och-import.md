# Partials och import

## Webbutveckling 2

---

# Partials och import

--

Med **partials** kan vi dela upp vår sass i flera filer som vi sedan kan importera in vår sassfil.

När vi skapar en partial så börjar namnet på filen alltid med ett **understreck**, till exempel **_colors.scss**.

--

```scss []
$primary-color: #b0b;
$secondary-color: #0097e6;
```
Här ovan ser vi innehållet i **_colors.scss**.

```scss []
@import "colors";

h1 {
    color: $primary-color;
}
```

Vi kan nu importera filen.

Som du ser hoppar vi över både understrecket och filändelsen när vi importerar en partial.

---

# SLUT!