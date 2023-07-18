# Att skriva ut

---

# Kod - Ex1

--

```php []
<?php

$music = "Napalm Death";
echo $music;

```

--

![bild](bilder/php-print-ex1a.png)

--

```php []
<?php

$music = "Napalm Death";
echo "$music";

```

--

![bild](bilder/php-print-ex1b.png)

--

```php []
<?php

$music = 'Napalm Death';
echo $music;

```

--

![bild](bilder/php-print-ex1c.png)

--

```php []
<?php

$music = 'Napalm Death';
echo '$music';

```

--

![bild](bilder/php-print-ex1d.png)

---

# Kod - Ex2

--

```php []
<?php

$music = "Napalm Death";
echo "<p>" . $music . " är grymt bra</p>";

```

--

![bild](bilder/php-print-ex2a.png)

--

```php []
<?php

$music = "Napalm Death";
echo "<p>$music är grymt bra</p>";

```

--

![bild](bilder/php-print-ex2b.png)

--

```php []
<?php

$music = "Napalm Death";
echo '<p>$music är grymt bra</p>';

```

--

![bild](bilder/php-print-ex2c.png)

---

# Kod - Ex3

--

```php []
<?php

$namn = "Bosse "Bildoktorn" Andersson";
echo "<p>" . $namn . "</p>";

```

--

![bild](bilder/php-print-ex3a.png)

--

```php []
<?php

$namn = "Bosse \"Bildoktorn\" Andersson";
echo "<p>" . $namn . "</p>";

```

--

![bild](bilder/php-print-ex3b.png)

---

# Escapetecken

--

| Teckenkombination | Resultat            |
| ----------------- | ------------------- |
| \\"               | "                   |
| \\'               | '                   |
| \\\               | \                   |
| \\$               | $                   |
| \n                | Ny rad i HTML-koden |
| \t                | TAB i HTML-koden    |

---

# echo vs print

--

`echo` och `print` är mer eller mindre desamma.

`echo` har inget returvärde.

`print` har returvärdet **1** så det kan användas i uttryck.

--

```php []
/* Because print has a return value, it can be used
in expressions The following outputs "hello world" */
if ( print "hello" ) {
    echo " world";
}
```

--

![bild](bilder/php-print-ex4a.png)

---

# SLUT!
