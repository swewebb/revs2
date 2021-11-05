# Mixins

## Webbutveckling 2

---

# Mixins

--

Mixins kan vi använda oss av för att kunna återanvända en gruppering av CSS-regler.

--

```scss []
@mixin clearfix() {
  *zoom: 1;
  &::before, &::after {
    content: '';
    display: table;
  }
  &:after {
    clear: both;
  }
}
```

I det här fallet har vi en mixin som heter **clearfix** och den återfinns i **_mixins.scss**.

--

```scss []
@import "mixins";

.wrapper {
  @include clearfix;
}
```

Här ser vi ett exempel på hur vi kan inkludera vår mixin clearfix.

--

```scss []
@mixin roundcorners($radius) {
  border-top-left-radius: $radius;
  border-bottom-right-radius: $radius;
}
```

Man kan även skicka med ett eller flera värden till sin mixins parametrar (här **$radius**).

I det här fallet skickar vi med vilken radie vi vill ha i de två hörnen.

--

```scss []
@import "mixins";

.box {
    @include roundcorners(1.5rem);
}
```

Så här kan det se ut när vi använder oss av vår mixin och skickar med ett värde.

--

```scss []
@import "mixins";

$val: 1.5rem;

.box {
    @include roundcorners($val);
}
```

Givetvis kan värdet vi skickar med återfinnas i en variabel.

--

```scss []
@mixin roundcorners($radius: 1rem) {
  border-top-left-radius: $radius;
  border-bottom-right-radius: $radius;
}
```

Vi kan även ange ett standardvärde.

--

```scss []
@import "mixins";

.box1 {
    @include roundcorners(); // 1rem
}

.box2 {
    @include roundcorners(1.5rem); // 1.5rem
}
```

Här ser vi två exempel, ett utan att vi skickar med något argument och ett där vi skickar med ett argument.

---

# Länkar

--

* [Sass Tutorial 4 - @mixins in sass](https://www.youtube.com/watch?v=zlxcjVn6xEg)
* [Sass Tutorial 5 - Mixin arguments everything you need to know](https://www.youtube.com/watch?v=CMan2craSag)

---

# SLUT!
