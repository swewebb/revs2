# `auto-fit`, `auto-fill` samt `minmax()`

---

# Skillnad mellan `auto-fill` och `auto-fit`

--

**auto-fill** och **auto-fit** används för att definiera hur kolumner eller rader i ett grid-layout ska hanteras när det finns ledigt utrymme.

Båda används med **repeat()** i **grid-template-columns** eller **grid-template-rows** för att skapa dynamiska layouter.

--

**auto-fill** fyller griden med så många enheter som möjligt, men lämnar eventuellt ledigt utrymme om griden inte är full.

**auto-fit** anpassar storleken på enheterna för att fylla hela utrymmet, vilket gör att det kan bli mindre "tomt" utrymme.

---

# HTML

--

```html []
<div class="parent">
  <div class="child child-1">Child 1</div>
  <div class="child child-2">Child 2</div>
  <div class="child child-3">Child 3</div>
  <div class="child child-4">Child 4</div>
  <div class="child child-5">Child 5</div>
  <div class="child child-6">Child 6</div>
  <div class="child child-6">Child 7</div>
  <div class="child child-6">Child 8</div>
</div>
```

---

# Exempel 1: `auto-fill` och `minmax()`

--

## CSS

--

---

# Exempel 2: `auto-fit` och `minmax()`

--

## CSS

--

```css [5]
.parent {
  width: 60%;

  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1rem;
}
```

--

BILD i browser

--

BILD i inspekt.

--

## Beskrivning

**repeat(auto-fit, minmax(300px, 1fr))**. Skapar dynamiska kolumner som passar in i det tillgängliga utrymmet.

**auto-fit**. Kolumnerna anpassas automatiskt för att passa i förälderns bredd.

**minmax(300px, 1fr)**. Varje kolumn kommer att vara minst 300px bred, men kan växa upp till lika stor bredd som de andra kolumnerna beroende på det tillgängliga utrymmet.

---

# SLUT!
