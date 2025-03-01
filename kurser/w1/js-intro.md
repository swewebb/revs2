# Introduktion till JavaScript

---

# Vad är JavaScript?

--

Ett programmeringsspråk för webben

Används för att skapa interaktiva webbsidor

---

# Hur fungerar det?

--

JavaScript körs i webbläsaren och kan:

- Manipulera HTML och CSS

- Hantera händelser (t.ex. klick, tangenttryckningar)

- Utföra beräkningar och logik

---

# Variabler

--

Variabler används för att lagra data i arbetsminnet (RAM).

Se en variabel som en låda som kan innehålla information av olika slag.

--

```js []
let firstName = "Pelle";
let status = true;

const age = 25;
```

**let** och **const** används för att deklarera variabler.

**let** används för variabler som kan ändras.

**const** används för variabler som inte ska ändras.

---

# Funktioner

--

Funktioner används för att organisera kod och återanvända logik.

```js []
function hello(firstname) {
  return `Hej, ${firstname}!`;
}

console.log(hello("Pelle"));
```

--

BILD

---

# DOM-manipulation

--

JavaScript kan ändra webbsidan dynamiskt.

--

```html []
<p id="demo">Text innan JavaScript</p>
<script src="app.js"></script>
```

```js []
const el = document.getElementById("demo");
el.innerText = "JavaScript är kul!";
```

--

```html []
<p id="demo">Text innan JavaScript</p>
<script src="app.js"></script>
```

```js []
const el = document.querySelect("#demo");
el.innerText = "JavaScript är kul!";
```

--

BILD

---

# Händelselyssnare

--

```html []
<p id="demo">Text innan JavaScript</p>
<button class="btn" id="tada">Klicka mig</button>

<script src="app.js"></script>
```

```js []
const el = document.getElementById("tada");
const txt = document.getElementById("demo");

el.addEventListener("click", () => {
  txt.innerText = "JavaScript är kul!";
});
```

--

BILD

---

# Villkor

--

```js []
let age = 18;

if (age >= 18) {
  console.log("Du är vuxen");
} else {
  console.log("Du är inte vuxen");
}
```

---

# Loopar

--

Loopar används för upprepa kod programmet.

--

## for-loopen

```js []
for (let i = 0; i < 5; i++) {
  console.log("Varv", i);
}
```

--

BILD

--

## While-loopen

```js []
let i = 0;

while (i < 5) {
  console.log(i);
  i++;
}
```

--

BILD

--

## Array.forEach

```js []
let fruits = ["apple", "banana", "cherry"];

fruits.forEach(function (fruit) {
  console.log(fruit);
});
```

--

BILD

--

---

# "Listor"

--

## Array

```js []
let fruits = ["apple", "banana", "cherry"];
```

--

## Objekt

```js []
let person = {
  name: "Anna",
  age: 25,
  city: "Stockholm",
};
```

---

# Slut!
