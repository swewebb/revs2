# Lagring i Webbläsaren med localStorage

---

# Vad är localStorage?

--

En del av **[Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API)**

Lagrar **nyckel-värde-par** i webbläsaren

Data sparas även efter att webbläsaren stängts

Endast tillgängligt för samma domän

---

# Varför ska jag använda localStorage?

--

När du behöver spara data lokalt utan server

När du behöver behålla inställningar mellan besök

När du behöver vill spara användarpreferenser

Snabbare än att använda tekniken cookies (ingen serverkommunikation)

---

# Viktigt att tänka på

--

**localStorage** är synlig i webbläsarens utvecklarverktyg

Använd **INTE** för känslig data (lösenord, personuppgifter)

Data kan raderas av användaren

---

# Grundläggande användning

--

## Spara data

```javascript
localStorage.setItem("namn", "Pelle");
```

--

## Hämta data

```javascript
let namn = localStorage.getItem("namn");
console.log(namn);
```

--

## Ta bort data

```javascript
localStorage.removeItem("namn");
```

--

## Rensa all data

```javascript
localStorage.clear();
```

---

# Spara användarens tema

--

## index.html

### Inuti head

```html []
<link rel="stylesheet" href="style.css" />
<script src="app.js" defer></script>
```

### Inuti body

```html []
<h1>Tema</h1>
<button id="changeTheme">Byt Tema</button>
```

--

## style.css

```css []
.light {
  background-color: #fafed1;
  color: #333;
}

.dark {
  background-color: #333;
  color: #fafed1;
}
```

--

## app.js

```js []
let theme = localStorage.getItem("tema") || "light";
document.body.className = theme;

const themeButton = document.getElementById("changeTheme");

themeButton.addEventListener("click", () => {
  theme = theme === "light" ? "dark" : "light";
  document.body.className = theme;

  localStorage.setItem("tema", theme);
});
```

--

## Förklaring av app.js

```js []
"use strict";
```

Aktiverar strict mode i JavaScript, vilket gör att vissa fel som annars skulle ignoreras kastar fel istället.

Det hjälper till att skriva säkrare och mer optimerad kod.

--

```js []
let theme = localStorage.getItem("tema") || "light";
```

**localStorage.getItem("tema")** hämtar det sparade temat från Local Storage.

Om det inte finns något sparat tema (null eller undefined), används "light" som standardvärde.

Variabeln **theme** innehåller antingen det sparade temat eller "light".

--

```js []
document.body.className = theme;
```

Sätter en class på body-elementet till det aktuella temat ("light" eller "dark").

--

```js []
const themeButton = document.getElementById("changeTheme");
```

Hämtar vår button med och lagrar den i **themeButton**.

--

```js []
themeButton.addEventListener("click", () => {});
```

Lägger till en händelselyssnar på vår knapp.

--

```js []
theme = theme === "light" ? "dark" : "light";
```

**Ternary operator** (? :) används för att växla mellan teman:

- Om temat är "light" ändras det till "dark".
- Om temat är "dark" ändras det till "light".

--

```js []
if (theme === "light") {
  theme = "dark";
} else {
  theme = "light";
}
```

Den här koden skulle vi kunna ha haft istället för vår **Ternary operator**

--

```js []
document.body.className = theme;
```

Uppdaterar body-elementets class till det nya temat.

--

```js []
localStorage.setItem("tema", theme);
```

Sparar det nya temat i **Local Storage**, så att det behålls även efter att sidan laddas om.

---

# SLUT!
