# Partials och importering

## Webbutveckling 2

---

# Introduktion

--

Med **partials** kan vi dela upp vår sass i flera filer som vi sedan kan importera in vår sassfil.

När vi skapar en partial så börjar namnet på filen alltid med ett **understreck**, till exempel **_colors.scss**.

---

# Vår webbplats

--

## src/partials/_colors.scss

```scss []
$body: hsl(0, 0%, 41%);
$primary-color: hsl(300, 100%, 37%);
$secondary-color: hsl(201, 100%, 45%);
```
Här ovan ser vi innehållet i **_colors.scss**.

--

## src/style.scss

```scss []
@use 'partials/colors';

h1 {
  color: colors.$primary-color;
}
```

Vi kan nu importera filen med **@use**.

Som du ser hoppar vi över både understrecket och filändelsen när vi importerar en partial.

--

## dist/css/style.css

```css []
h1{color:#bd00bd}
/*# sourceMappingURL=style.css.map */
```

Här ser vi resultatet när gulp:en har gjort sitt.

--

## src/style.scss

```scss []
@use 'partials/colors' as c;

h1 {
  color: c.$primary-color;
}
```

Här har vi kortat ner namnet på vår partial.

--

## src/style.scss

```scss []
@use 'partials/colors' as *;

h1 {
  color: $primary-color;
}
```

Här har vi använt jokertecknet när vi importerar.

--

## src/base/_index.scss

```scss []
@forward 'base/bg';
@forward 'base/center';
@forward 'base/flex';
@forward 'base/resets';
```

Istället för att behöva importera alla partials en och en så kan vi använda oss av en speciell fil med namnet **_index.scss** för att exportera våra partials.

--

## src/style.scss

```scss []
@use 'base/' as *;
@use 'partials/colors' as *;

h1 {
  color: $primary-color;
}
```

Nu behöver vi bara importera sökvägen till **base/** för att få tillgång till alla filer som vi där har exporterat.

--

## dist/css/style.css

```css []
body{background-color:dimgray}.center{display:grid;margin:0;min-height:100vh;place-items:center}.flex{display:flex;gap:2rem}*,:after,:before{box-sizing:border-box}html{box-sizing:inherit}body{margin:0;min-height:100vh;padding:0}h1{color:#bdaa00}
/*# sourceMappingURL=style.css.map */
```

--

## src/partials/_index.scss

```scss []
@forward 'partials/colors';
```

--

## src/style.scss

```scss []
@use 'base/' as *;
@use 'partials/' as *;

h1 {
  color: $primary-color;
}
```

---

# SLUT!