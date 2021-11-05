# Variabler o. nästling

## Webbutveckling 2

---

# Variabler

--

```scss []
$primary-color: #b0b;
$font-stack: arial, helvetica, sans-serif;

h1 {
  color: $primary-color;
  font-family: $font-stack;
}
```

--

Som du ser har vi deklarerat två variabler. När det gäller att namge variabler följer vi dessa regler:

  * Börjar alltid med $-tecken
  * Enbart små bokstäver (a-z, 0-9)
  * Får inte börja med en siffra
  * Vi använder bindestreck för uppdelning av namn.

--

```css []
h1 {
    font-family: arial, helvetica, sans-serif;
    color: #b0b;
}
```

Vårt exempel kommer att genera följande CSS-regel i formatmallen.

---

# Nästling

--

```scss []
$primary-color: #b0b;

nav {
    a {
        font-weight: bold;
        color: $primary-color;

        &:hover {
            text-decoration: none;
        }
    }
}
```

I sass så kan vi nästla selektorer. **&-tecknet** använder vi för att referera till föräldraselektorn.

--

```css []
nav a {
    font-weight: bold;
    color: #b0b;
}

nav a:hover {
    text-decoration: none;
}
```

Så här kommer formatmallen se ut när vi har konverterat scss:en till css.

--

```scss []
.article {
    &-100 {
        width: 100%;
    }
    &-50 {
        width: 50%;
    }
    &-25 {
        width: 25%;
    }
}
```

I det här exemplet använder vi **&-tecknet** för att lägga till i slutet på klassnamnet **.article**, till exempel **.article-100**.

--

Nästla inte djupare än vad du behöver.

[Läs följande artikel på Sitepoint för mer information](https://www.sitepoint.com/sass-basics-nesting/).

---

# SLUT!