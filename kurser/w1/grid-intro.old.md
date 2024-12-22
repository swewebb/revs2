# CSS Grid: En Grundläggande Introduktion

---

# Vad är CSS Grid?

--

- Ett 2D-layoutsystem
- Designat för att skapa flexibla och responsiva grid-baserade layouter.
- Perfekt för att arrangera innehåll i rader och kolumner.

---

# Fördelar med CSS Grid

--

- **Flexibilitet**: Lätt att anpassa layout.
- **Responsiv design**: Fungerar bra på olika skärmstorlekar.
- **Enkelhet**: Mindre kod jämfört med äldre layouttekniker.

---

# Grundläggande begrepp

--

- **Grid Container**: Ett element som definierar ett grid (t.ex. `<div>` med `display: grid;`).
- **Grid Items**: Barn till grid-containern som placeras i rutnätet.
- **Grid Lines**: Linjer som separerar rader och kolumner.
- **Grid Cells**: Individuella rutor i rutnätet.

---

## Syntax: Grid Container

```css
div {
  display: grid;
  grid-template-columns: 100px 200px auto;
  grid-template-rows: 50px 50px;
  gap: 10px;
}
```

- `grid-template-columns`: Definierar kolumnstorlekar.
- `grid-template-rows`: Definierar radstorlekar.
- `gap`: Avstånd mellan rader och kolumner.

---

## Placeringsmetoder för Grid Items

### Automatisk placering

```css
div {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}
```

### Manuellt placera items

```css
.item {
  grid-column: 1 / 3; /* Sträcker sig över kolumn 1 till 3 */
  grid-row: 2 / 4; /* Sträcker sig över rad 2 till 4 */
}
```

---

## Responsiva Grid-layouter

### Använda media queries

```css
@media (max-width: 600px) {
  div {
    grid-template-columns: 1fr;
  }
}
```

### Auto-fit och auto-fill

```css
div {
  grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
}
```

- `auto-fit`: Anpassar antal kolumner tillgängligt utrymme.
- `auto-fill`: Behåller antalet kolumner, även om de är tomma.

---

## Exempel: En enkel layout

```html
<div class="grid-container">
  <div class="item">1</div>
  <div class="item">2</div>
  <div class="item">3</div>
</div>
```

```css
.grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 20px;
}

.item {
  background: lightblue;
  padding: 20px;
  text-align: center;
}
```

---
