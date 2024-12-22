---
# CSS Grid: Explicit vs Implicit Grid
---

## Vad är Explicit Grid?

- Ett **explicit grid** definieras direkt med `grid-template-columns` och `grid-template-rows`.
- Du anger exakt antalet rader och kolumner samt deras storlekar.

### Exempel

```css
.container {
  display: grid;
  grid-template-columns: 100px 100px;
  grid-template-rows: 50px 50px;
}
```

- Skapar ett rutnät med 2 kolumner och 2 rader.

```html
<div class="container">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>
```

### Resultat

- **Plats 1 och 2** fyller den första raden.
- **Plats 3** hamnar på rad 2, kolumn 1.

---

## Vad är Implicit Grid?

- Ett **implicit grid** skapas automatiskt av webbläsaren när grid-items placeras utanför det definierade rutnätet.
- Nya rader eller kolumner genereras dynamiskt.

### Exempel

```css
.container {
  display: grid;
  grid-template-columns: 100px 100px;
}
```

```html
<div class="container">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>
```

### Resultat

- Två kolumner definieras, men eftersom det bara finns **1 rad definierad**, skapas en andra rad automatiskt för det tredje grid-item.

---

## Anpassning av Implicit Grid

- Du kan styra storleken på de genererade raderna och kolumnerna med `grid-auto-rows` och `grid-auto-columns`.

### Exempel

```css
.container {
  display: grid;
  grid-template-columns: 100px 100px;
  grid-auto-rows: 50px;
}
```

- Implicit genererade rader kommer nu att ha en höjd på 50px.

---

## Explicit vs Implicit Grid i Praktiken

### Explicit Grid

```css
.container {
  display: grid;
  grid-template-columns: 100px 100px;
  grid-template-rows: 50px 50px;
}
```

- Skapar ett exakt rutnät.

```html
<div class="container">
  <div>1</div>
  <div>2</div>
  <div>3</div>
  <!-- Hamnar utanför det definierade rutnätet. -->
</div>
```

### Implicit Grid

```css
.container {
  display: grid;
  grid-template-columns: 100px 100px;
}
```

- Skapar automatiskt fler rader för extra innehåll.

---

## Visualisering

### Explicit Grid

| 100px | 100px |
| ----- | ----- |
| 1     | 2     |
| 3     |       |

### Implicit Grid

| 100px | 100px |
| ----- | ----- |
| 1     | 2     |
| 3     |       |

Skillnaden är att i explicit grid kan du inte placera fler items än vad som ryms inom det definierade rutnätet utan att manuellt utöka det.

---

## Rekommenderade resurser

- [MDN: Explicit vs Implicit Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout#explicit_vs_implicit_grids)
- [CSS Tricks: Grid Auto Flow](https://css-tricks.com/snippets/css/complete-guide-grid/)

---

## Frågor?

- Några frågor eller funderingar? 🌟
