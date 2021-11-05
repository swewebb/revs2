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

```scss
$font-size: 18px;
$text-color: #000;

html
    font-size: $font-size;
    color: $text-color;

```

--

## Scss

```scss
$font-size: 18px;
$text-color: #000;

html {
    font-size: $font-size;
    color: $text-color;
}
```

---

# Installation

---

# Node.js

--

Hämta hem **node.js** från [https://nodejs.org/en/](https://nodejs.org/en/).

--

![node](images/w2-sass-01-01.png)

Under installationen ser du till att bocka i rutan för att installera nödvändiga verktyg.

--

![Node-kontroll](images/w2-sass-01-02.png)

När installationen är klar kontrollerar du att **node** och **npm** (_Node Package Manager_) finns.

---

# Sätta upp projektet

--

1. Skapa förvaringsplats
1. Klona ner
1. Initiera projektet
1. Installera moduler - sass
1. Kontroll - sass
1. Installera moduler - parcel
1. Kontroll - parcel
1. Gitignore
1. Pusha

---

## Skapa förvaringsplats

Skapa en ny privat förvaringsplats med namnet **w2-sass**.

Glöm inte att bjuda in läraren!

---

## Klona ner

```text
git clone https://github.com/swewebb/w2-sass.git
```

Klona ner förvaringsplatsen i mappen **C:\git**

---

## Initiera projektet

![npm-init-1](images/w2-sass-01-03.png)

--

![npm-init-2](images/w2-sass-01-04.png)

--

![npm-init-3](images/w2-sass-01-05.png)

--

![npm-init-3](images/w2-sass-01-06.png)

---

## Installera moduler - Sass

```
npm install sass -g
npm install sass -D
```

---

![npm-installerade](images/w2-sass-01-07.png)

---

## Kontroll - Sass

![npm-kontroll-1](images/w2-sass-01-08.png)

--

![npm-kontroll-2](images/w2-sass-01-09.png)

--

![npm-kontroll-3](images/w2-sass-01-10.png)

--

![npm-kontroll-3](images/w2-sass-01-11.png)

--

![npm-kontroll-3](images/w2-sass-01-12.png)

---

## Installera moduler - Parcel

```
npm install parcel-bundler -D
```

![npm-moduler-p](images/w2-sass-01-13.png)

--

![npm-moduler-p](images/w2-sass-01-14.png)

![npm-moduler-p](images/w2-sass-01-14.png)

---

## Kontroll - Parcel

![npm-kontroll-p1](images/w2-sass-01-15.png)

--

![npm-kontroll-p2](images/w2-sass-01-16.png)

--

```
npm run dev
```

![npm-kontroll-p3](images/w2-sass-01-17.png)

--

![npm-kontroll-p3](images/w2-sass-01-18.png)

--

![npm-kontroll-p4](images/w2-sass-01-19.png)

---

## .gitignore

I den här filen lägger vi till sådant som INTE ska hanteras av Git.

**Observera!** Filen heter **.gitignore**

```
node_modules
.cache
```

---

## Pusha

Pusha upp allt till GitHub.

---

# Länkar

- [https://nodesource.com/blog/an-absolute-beginners-guide-to-using-npm/](https://nodesource.com/blog/an-absolute-beginners-guide-to-using-npm/)
- [https://parceljs.org/getting_started.html](https://parceljs.org/getting_started.html)

---

# SLUT!
