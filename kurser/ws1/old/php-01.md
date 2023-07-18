# PHP-01

---

# Att skriva kod

--

Filändelse = **php**

**index.php**

--

PHP-koden innesluts av `<?php … ?>` om dokumentet även innehåller HTML-kod.

--

```php []
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>Exempel</h1>

  <?php
  // Här skriver vi PHP-koden
  ?>
</body>
</html>
```

--

PHP-koden har enbart `<?php` om dokumentet enbart innehåller PHP-kod. I det här fallet ska även sidan innehålla en tom rad sist.

--

```php []
<?php

// Här skriver vi PHP-koden

```

---

# Variabler

--

Börjar alltid med ett **$**-tecken.

Kan endast innehålla alfanumeriska tecken och understreck (**a-z**, **A-Z**, **0-9**, **\_**)

Kan innehålla **åäö**, men enligt en allmänt vedertagen konvention bör du undvika det.

Kan aldrig innehålla mellanslag.

Skillnad på stora och små bokstäver.

Vi använder oss av **camelCaps** för att namnge variabler (ex. **$lastName**)

--

Här har vi deklarerat variabeln number och tilldelat den ett värde om 1.

```php []
<?php

$number = 1;

```

---

# Datayper

--

| Svensk benämning | Engelsk benämning | Exempel              |
| ---------------- | ----------------- | -------------------- |
| Boolesk          | Boolean           | TRUE eller FALSE     |
| Heltal           | Integer           | 18                   |
| Flyttal          | Float             | 3.14                 |
| Sträng           | String            | "Bo Spik"            |
| Vektor           | Array             | (1, 3, "Bo", "Spik") |
| Objekt           | Object            | Alla ovanstående     |
| Resurs           | Resource          | Databaskoppling      |
| Null             | Null              | Inget värde          |

--

## Boolesk (Boolean)

Sätts med **TRUE** eller **FALSE**

Dessa nyckelord är inte känsliga för små eller stora bokstäver.

--

```php []
<?php

$var = TRUE;

```

--

## Heltal (Integer)

Består av positiva (**0, 1 , 2, …**) och negativa (**-1, -2, -3, …**) heltal.

Plattformsberoende:

- 32-bit = 2 x 10<sup>9</sup>
- 64-bit = 9 x 10<sup>18</sup>

--

```php []
<?php

$age = 42;

```

--

## Flyttal (Float)

Används för att representera stora eller små tal som inte kan beskrivas med hjälp av heltal.

Använder decimalpunkt och inte decimalkomma.

--

```php []
<?php

$num1 = 3.14;  //3.14
$num2 = 8.5E3; //8500

```

--

## Sträng (String)

Bygger på en serie symboler och/eller nummer som väljs från en teckenuppsättning.

Finns ingen begränsning hur stor en sträng kan vara i PHP, men gränsen går vid hur mycket minne det finns på den dator där PHP är i drift.

--

```php []
<?php

$lastName = "Apelsinsson";
$helloMsg = "Tjena och välkommen!";
$helloMsg = 'Tjena och välkommen!';

```

---

# Löst typat

--

```php []
<?php

$lastName = "Hammare";
$lastName = "Gullan Hammare";
$lastName = 42;
$lastName = TRUE;

```

---

# Typkonvertering

--

Behövs ibland när man verkligen vill ha koll på datatypen.

--

```php []
<?php

echo "<pre>";
$n = 1.45;
var_dump($n);

$ex1 = (int)$n;
var_dump($ex1);

$ex2 = (string)$ex1;
var_dump($ex2);

echo "</pre>";

```

--

```[]
float(1.45)
int(1)
string(1) "1"
```

---

# Kod - Ex1

--

```php []
<?php

$music = "Napalm Death";
echo $music;

```

--

```php []
<?php

$music = "Napalm Death";
echo "$music";

```

--

```php []
<?php

$music = 'Napalm Death';
echo $music;

```

--

```php []
<?php

$music = 'Napalm Death';
echo '$music';

```

---

# Kod - Ex2

--

```php []
<?php

$music = "Napalm Death";
echo $music . " är grymt bra";

```

--

```php []
<?php

$music = "Napalm Death";
echo "$music är grymt bra";

```

--

```php []
<?php

$music = "Napalm Death";
echo '$music är grymt bra';

```

---

# Vad händer här?

--

```php []
<?php

$namn = "Bosse "Bildoktorn" Andersson";
echo $namn;

```

--

BILD

--

```php []
<?php

$namn = "Bosse \"Bildoktorn\" Andersson";
echo $namn;

```

--

BILD

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

# Operatorer

--

En operator är något som verkar på en eller flera termer.

Det finns olika typer av operatorer och du kommer känna igen det mesta av det.

---

# Aritmetiska operatorer

--

| Operator | Namn           |
| -------- | -------------- |
| +        | Addition       |
| -        | Subtraktion    |
| \*       | Multiplikation |
| /        | Delat          |
| %        | Modulus        |
| \*\*     | Upphöjt        |

--

```php []
<?php

$a = 10;
$b = 3;

$mod = $a % $b;
$exp = $a ** $b;

echo "<p>" . $mod . "</p>";
echo "<p>" . $exp . "</p>";

```

---

# Tilldelningsoperatorer

--

| Tilldelning | Samma som...   |
| ----------- | -------------- |
| $a = $b;    | $a = $b;       |
| $a += $b;   | $a = $a + $b;  |
| $a -= $b;   | $a = $a - $b;  |
| $a \*= $b;  | $a = $a \* $b; |
| $a /= $b;   | $a = $a / $b;  |
| $a %= $b;   | $a = $a % $b;  |

--

```php []
<?php

$a = 10;
$b = 2;

$a = $b;
echo "<p>" . $a . "</p>";

```

--

```php []
<?php

$a = 10;
$b = 2;

$a += $b;
echo "<p>" . $a . "</p>";

```

---

# Jämförelseoperatorer

--

| Operator | Namn                     |
| -------- | ------------------------ |
| ==       | Lika med                 |
| ===      | Identisk                 |
| !=       | Inte lika med            |
| <>       | Inte lika med            |
| !==      | Inte identisk            |
| >        | Större än                |
| <        | Mindre än                |
| >=       | Större än eller lika med |
| <=       | Mindre än eller lika med |
| <=>      | Rymdskepp                |

--

```php []
<?php

$a = 10;
$b = "10";

if ($a == $b) {
    echo "Lika";
}

```

--

```php []
<?php

$a = 10;
$b = "10";

if ($a === $b) {
    echo "Identiska";
} else {
    echo "Ej Identiska";
}

```

--

```php []
<?php

$x = 5;
$y = 10;

// returns -1 because $x is less than $y
echo ($x <=> $y);
echo "<br>";

$x = 10;
$y = 10;

// returns 0 because values are equal
echo ($x <=> $y);
echo "<br>";

$x = 15;
$y = 10;

// returns +1 because $x is greater than $y
echo ($x <=> $y);

```

---

# Ökning/minskning operatorer

--

Vi har tillgång till **++** och **--**.

--

```php []
<?php

$a = 1;
$b = $a++;

echo "<p>" . $a . ", " . $b . "</p>";

```

--

```php []
<?php

$a = 1;
$b = ++$a;

echo "<p>" . $a . ", " . $b . "</p>";

```

---

# Logiska operatorer

--

Doh!

---

# Strängoperatorer

--

Doh!

--

```php []
<?php


```

---
