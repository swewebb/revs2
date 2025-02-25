# Skapa och hantera element i JavaScript

---

# Skapa ett nytt element

--

```js []
const nyttElement = document.createElement("div");
nyttElement.textContent = "Hej, detta är ett nytt element!";
```

**document.createElement(tag)** skapar ett nytt element.

**textContent** sätter textinnehållet.

--

## Varför använda textContent istället för innerHTML?

**textContent** hanterar endast text och förhindrar att HTML-kod exekveras, vilket gör det säkrare.

**innerHTML** tolkar HTML och kan potentiellt introducera säkerhetsrisker såsom XSS-attacker.

Använd **textContent** när du bara vill sätta eller ändra text.

---

# Lägga till ett element i DOM

--

```js [1, 6]
const container = document.getElementById("container");

const nyttElement = document.createElement("div");
nyttElement.textContent = "Hej, detta är ett nytt element!";

container.appendChild(nyttElement);
```

**appendChild** lägger till ett element som barn till ett annat.

Vi behöver först hämta det överordnade elementet.

---

# Ändra egenskaper och attribut

--

```js [5-7]
const container = document.getElementById("container");

const nyttElement = document.createElement("div");
nyttElement.textContent = "Hej, detta är ett nytt element!";
nyttElement.style.color = "red";
nyttElement.setAttribute("class", "highlight");
nyttElement.classList.add("extra");

container.appendChild(nyttElement);
```

**.style** används för att ändra CSS.

**setAttribute(name, value)** lägger till eller ändrar attribut.

**classList.add(className)** lägger till en CSS-klass utan att skriva över befintliga klasser.

---

# Hantera klasser med classList

--

```js []
nyttElement.classList.remove("extra");
nyttElement.classList.toggle("active");
```

**classList.remove(className**) tar bort en specifik klass.

**classList.toggle(className)** lägger till klassen om den saknas och tar bort den om den redan finns.

---

# Händelselyssnare

--

```js []
nyttElement.addEventListener("click", () => {
  console.log("Elementet klickades!");
});
```

**addEventListener(event, callback)** registrerar en händelse, i det här fallet ett klick

---

# Ta bort element

```js []
container.removeChild(nyttElement);
```

**removeChild** tar bort ett element från sin förälder.

Alternativt kan vi använda **element.remove()**.

---

# Sammanfattning

--

Skapa element med **createElement**.

Lägg till dem med **appendChild**.

Ändra egenskaper med **.style** och **setAttribute**.

--

Hantera klasser med **classList.add**, **classList.remove** och **classList.toggle**.

Använd **textContent** istället för **innerHTML** för säkerhet.

Lyssna på händelser med **addEventListener**.

Ta bort element med **removeChild** eller **remove()**.

---

# Demo

--

```html
<!DOCTYPE html>
<html lang="sv">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>JS DOM Exempel</title>
    <style>
      .text {
        color: red;
      }
    </style>
  </head>
  <body>
    <button id="add">Lägg till element</button>
    <div id="container"></div>

    <script>
      document.getElementById("add").addEventListener("click", () => {
        const element = document.createElement("p");
        element.textContent = "Ett nytt stycke!";
        element.classList.add("text");
        document.getElementById("container").appendChild(element);
      });
    </script>
  </body>
</html>
```
