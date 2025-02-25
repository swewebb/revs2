# JavaScript Moduler

---

# Vad är en modul?

--

En **modul** är en återanvändbar del av kod

Hjälper till att organisera och underhålla kod

Möjliggör **separation av logik** och **återanvändning**

---

# ES-moduler (ESM)

--

## Vad är ES-moduler?

Introducerades i **[ES6 (2015)](https://www.w3schools.com/js/js_es6.asp)**

Använder **import** och **export**

Exekveras **i strikt läge** ("use strict")

Stöds direkt i moderna webbläsare

--

## Exempel

```js []
// math.js
export function add(a, b) {
  return a + b;
}
```

```js []
// main.js
import { add } from "./math.js";

console.log(add(2, 3)); // 5
```

---

# Named och Default Exports

--

## Named Export

```js []
// helpers.js
export function greet(name) {
  return `Hej, ${name}!`;
}

export const pi = 3.1415;
```

```js []
// main.js
import { greet, pi } from "./helpers.js";

console.log(greet("Elina"));
console.log(pi);
```

--

## Default Export

```js []
// user.js
export default function getUser() {
  return { name: "Pelle" };
}
```

```js []
// main.js
import getUser from "./user.js";

console.log(getUser());
```

---

# Flera moduler används tillsammans

--

```js []
// math.js
export function add(a, b) {
  return a + b;
}

export function multiply(a, b) {
  return a * b;
}
```

--

```js []
// greetings.js
export function greet(name) {
  return `Hej, ${name}!`;
}
```

--

```js []
// main.js
import { add, multiply } from "./math.js";
import { greet } from "./greetings.js";

console.log(greet("Elina"));
console.log("2 + 3 =", add(2, 3));
console.log("2 * 3 =", multiply(2, 3));
```

--

# Användning av moduler i HTML

--

När man arbetar med **ES-moduler** i webbläsaren används **type="module"** i script-taggen.

--

```html [9]
<!DOCTYPE html>
<html lang="sv">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Moduler i JavaScript</title>
  </head>
  <body>
    <script type="module" src="./main.js"></script>
  </body>
</html>
```

---

# Läs mer

--

[https://www.w3schools.com/js/js_modules.asp](https://www.w3schools.com/js/js_modules.asp)

[https://javascript.info/modules-intro](https://javascript.info/modules-intro)

---

# SLUT!
