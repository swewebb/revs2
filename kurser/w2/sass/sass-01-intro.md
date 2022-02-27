# SASS

## Webbutveckling 2

---

# Centralt innehåll

Språk med stöd för variabler för att förenkla CSS-generering.

---

# Sass?

--

Sass är CSS-preprocessor vilket innebär att vi kodar formatmallarna i språket **sass/scss** för att sedan via någon tjänst konvertera till vanlig css.

--

När man pratar om **sass** så menar de flesta egentligen **scss**.

I **sass** (som kom först) har man tagit bort anvädningen av klammerparenteser.

I **scss** använder man klammerparenteser som vi är vana med, så när vi pratar om **sass** så menar vi **scss**.

--

## Sass

```scss []
$font-size: 18px;
$text-color: #000;

html
    font-size: $font-size;
    color: $text-color;

```

--

## Scss

```scss []
$font-size: 18px;
$text-color: #000;

html {
    font-size: $font-size;
    color: $text-color;
}
```

---

# Node.js

--

Hämta hem **node.js** från [https://nodejs.org/en/](https://nodejs.org/en/).

Välj senaste versionen!

Installera programmet (next-next-next...)

--

## Kontroll att node och npm fungerar

```txt
PS D:\git\> node --version
v17.6.0

PS D:\git\> npm --version
8.5.1
```

När installationen är klar kontrollerar du att **node** och **npm** (_Node Package Manager_) finns.

---

# Sätta upp projektet

--

1. Skapa förvaringsplats
1. Klona ner
1. Mappstruktur
1. Initiera projektet
1. Installera globala moduler/paket
1. Installera lokala moduler/paket
1. Konfigurera gulpfile.js
1. Gitignore
1. Pusha

---

## Skapa förvaringsplats

Skapa en ny privat förvaringsplats med namnet <br> **w2-sass**.

Glöm inte att bjuda in läraren!

---

## Klona ner

```text []
git clone https://github.com/swewebb/w2-sass.git
```

Klona ner förvaringsplatsen i mappen **C:\git**

---

## Mappstruktur

```text []
src/
  scss/
    base/
      _bg.scss
      _center.scss
      _flex.scss
      _index.scss
      _reset.scss
    partials/
      _index.scss
    style.scss
index.html
```

Vi kommer att hålla mappstrukturen relativt enkel.

Ladda ner zippen!

---

## Initiera projektet

```text []
npm init -y
```

--

```text []
PS D:\git\w2-sass> npm init -y
Wrote to D:\git\w2-sass\package.json:

{
  "name": "w2-sass",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

--

Du kommer nu ha en ny fil med namnet **package.json**.

---

## Installera globala moduler/paket

```text []
npm install --global gulp gulp-cli sass
```

---

## Installera lokala moduler/paket

```text []
npm install --save-dev gulp gulp-sass gulp-postcss cssnano sass
```

Det kommer nu att dyka upp en ny mapp som heter **node_modules**.

--

```js []
"devDependencies": {
    "cssnano": "^5.0.17",
    "gulp": "^4.0.2",
    "gulp-postcss": "^9.0.1",
    "gulp-sass": "^5.1.0",
    "sass": "^1.49.9"
}
```

I **package.json** kommer vi nu finna vilka paket vårt projekt behöver.

---

## Konfigurera gulpfile.js

```js []
const {src, dest, watch, series} = require('gulp')
const sass = require('gulp-sass')(require('sass'))
const postcss = require('gulp-postcss')
const cssnano = require('cssnano')
```

Börja med att skapa filen **gulpfile.js**.

--

```js []
// HTML-hanteraren
function copyHtml() {
    return src('src/**/*.html')
      .pipe(dest('dist'))
}

exports.default = series(
  copyHtml
)
```

--

```text []
PS D:\git\w2-sass>gulp
[11:06:17] Using gulpfile D:\git\w2-sass\gulpfile.js
[11:06:17] Starting 'default'...
[11:06:17] Starting 'copyHtml'...
[11:06:17] Finished 'copyHtml' after 29 ms
[11:06:17] Finished 'default' after 32 ms
```

Om vi nu kör **gulp** så kommer vår funktion att köras.

Vi kommer nu att se en ny mapp **dist** och det är i den här mappen allt som vi vill publicera återfinnas, i vårt fall **index.html**.

--

```js []
// Sass-hanteraren ,
function scssTask() {
  return src('src/scss/**/*.scss', {sourcemaps: true})
    .pipe(sass())
    .pipe(postcss([cssnano()]))
    .pipe(dest('dist/css', {sourcemaps: '.'}))
}

exports.default = series(
  scssTask,
  copyHtml
)
```

Nu bygger vi upp funktionen för att hantera scss:en.

--

```
PS D:\git\w2-sass> gulp
[11:11:59] Using gulpfile D:\git\w2-sass\gulpfile.js
[11:11:59] Starting 'default'...
[11:11:59] Starting 'scssTask'...
[11:12:00] Finished 'scssTask' after 898 ms
[11:12:00] Starting 'copyHtml'...
[11:12:00] Finished 'copyHtml' after 11 ms
[11:12:00] Finished 'default' after 913 ms
```

Vi kontrollerar även att den fungerar. Det kommer nu att dyka upp en ny mapp i **dist**, nämligen **css**.

I den kommer det att finnas två filer, **style.css** och **style.css.map**.

--

```js []
// Kontrollanten
function watchTask() {
  watch('src/scss/**/*.scss', scssTask)
  watch('src/**/*.html', copyHtml)
}

exports.default = series(
  scssTask,
  copyHtml,
  watchTask
)
```

Vi vill inte behöva köra **gulp** om och om igen så vi skapar oss en kontrollant som håller koll på när vi sparar och kör då våra funktioner.

--

```text []
PS D:\git\w2-sass> gulp
[11:20:52] Using gulpfile D:\git\w2-sass\gulpfile.js
[11:20:52] Starting 'default'...
[11:20:52] Starting 'scssTask'...
[11:20:53] Finished 'scssTask' after 883 ms
[11:20:53] Starting 'copyHtml'...
[11:20:53] Finished 'copyHtml' after 6.84 ms
[11:20:53] Starting 'watchTask'...
```

När vi nu kör **gulp** så kan se ut som att allt har hängts sig... men så är inte fallet. Vår kontrollant körs nu och väntar på att få något att göra.

---

## .gitignore

I den här filen lägger vi till sådant som INTE ska hanteras av Git.

**Observera!** Filen heter **.gitignore**

``` []
node_modules
.cache
```

---

## Pusha

Pusha upp allt till GitHub.

---

# Återanvändning

```text
npm install
```

Då vi har **package.json** kan vi använda den för att skapa ett nytt projekt. Glöm inte att sedan lägga till **gulpfile.js** och **.gitignore**.

---

# Länkar

- [https://nodesource.com/blog/an-absolute-beginners-guide-to-using-npm/](https://nodesource.com/blog/an-absolute-beginners-guide-to-using-npm/)

---

# SLUT!
