# Inbyggda funktioner

---

# Introduktion

--

Det finns idag över 1000 inbyggda funktioner.

Vi kommer att titta på några av dessa nu medan vissa andra kommer du att få söka upp i manualen.

Manualen finns som du vet på [http://php.net](http://php.net)

---

# strlen o. mb_strlen

--

**String lenght**, returnerar antalet tecken i en sträng.

0 ses som falskt, 1 - oändligheten ses som sant

--

```php [2]
$password = "kaka";
$length = strlen($password);

echo "<p>strlen = $length</p>";
```

```
strlen = 4
```

--

```php []
$password = "åäö";
$length = strlen($password);

echo "<p>strlen = $length</p>";
```

```
strlen = 6
```

Hoppsan!!!

--

```php [2]
$password = "kaka";
$length = mb_strlen($password, "utf-8");

echo "<p>strlen = $length</p>";
```

```
strlen = 4
```

--

```php [2]
$password = "åäö";
$length = mb_strlen($password, "utf-8");

echo "<p>strlen = $length</p>";
```

```
strlen = 3
```

---

## strcmp o. strcasecmp

--

**strcmp**,string compare

Används för att jämföra om två
strängar är lika.

Om så returneras 0.

_Returns < 0 if string1 is less than string2; > 0 if string1 is greater than string2, and 0 if they are equal._

**strcasecmp**, om man inte vill ta hänsyn till versaler och gemener

--

```php [4]
$password1 = "kaka";
$password2 = "kaka";

if (strcmp($password1, $password2) === 0) {
    echo "<p>Lika</p>";
} else {
    echo "<p>Olika</p>";
}
```

```
Lika
```

--

```php [4]
$password1 = "KAKA";
$password2 = "kaka";

if (strcmp($password1, $password2) === 0) {
    echo "<p>Lika</p>";
} else {
    echo "<p>Olika</p>";
}
```

```
Olika
```

--

```php [4]
$password1 = "KAKA";
$password2 = "kaka";

if (strcasecmp($password1, $password2) === 0) {
    echo "<p>Lika</p>";
} else {
    echo "<p>Olika</p>";
}
```

```
Lika
```

---

# is_numeric

--

Används för att kontrollera om en variabels värde är ett tal (eller numerisk sträng) eller inte.

Returnerar **TRUE** om tal och **FALSE** om ej tal.

--

```php [5]
$test = [3.14, 42, "42", "tal 73", "text"];
$r = [];

foreach ($test as $value) {
    if (is_numeric($value)) {
        $r[] = "tal";
    } else {
        $r[] = "ej tal";
    }
}

echo "<p>" . implode(", ", $r) . "</p>";
```

```html
tal, tal, tal, ej tal, ej tal
```

---

# strtoupper o. strtolower

--

**strtoupper**, konvertera gemener till versaler

**strtolower**, konvertera versaler till gemener

Båda har problem med svenska tecken!

--

```php [3,4]
$text1 = "small";
$text2 = "BIG";
$upper = strtoupper($text1);
$lower = strtolower($text2);

echo "<p>$upper, $lower</p>";
```

```html
SMALL, big
```

--

```php [3,4]
$text1 = "låg";
$text2 = "HÖG";
$upper = strtoupper($text1);
$lower = strtolower($text2);

echo "<p>$upper, $lower</p>";
```

```html
LåG, hÖg
```

---

# mb_convert_case

--

Lösningen på problemet med **strtoupper** o. **strtolower**.

Arbetar med olika lägen (mode), se dokumentationen.

--

## Gemener till versaler

```php [2]
$text = "låg";
$result = mb_convert_case($text, MB_CASE_UPPER, "utf-8");

echo "<p>$result</p>";
```

```html
LÅG
```

--

## Versaler till gemener

```php [2]
$text = "HÖG";
$result = mb_convert_case($text, MB_CASE_LOWER, "utf-8");

echo "<p>$result</p>";
```

```html
hög
```

---

# str_replace

--

Med funktionen **str_replace** kan man ersätta delar av en sträng med ett annat innehåll.

--

```php [2]
$orginal = "Fy fan vad brysselkål är äckligt";
$modified = str_replace("fan", "bubblans", $orginal);

echo "<p>$modified</p>";
```

```html
Fy bubblans vad brysselkål är äckligt
```

---

# explode

--

Returnerar en array med strängar utifrån vald separator.

--

```php [2]
$text = "Kålle, Ada, Kurt";
$exploded = explode(",", $text);

echo "<ol>";
foreach ($exploded as $value) {
    echo "<li>" . $value . "</li>";
}
echo "</ol>";
```

```html
1. Kålle 2. Ada 3. Kurt
```

---

# implode

--

Gör om en array till en textsträng.

--

```php [2]
$arr = ['kanin', 'hare', 'räv'];
$imploded = implode(", ", $arr);

echo "<p>" . $imploded . "</p>";
```

```html
kanin, hare, räv
```

---

# count

--

Räknar antal element i en array.

--

```php [2]
$arr = ['kanin', 'hare', 'räv'];
$antal = count($arr);

echo "<p>" . $antal . "</p>";
```

```html
3
```

---

# str_split o. mb_str_split

--

Gör om en sträng till en array.

--

## str_split

```php [2]
$text = "Kalle";
$splitted = str_split($text);

print_r($splitted);
```

```html
Array ( [0] => K [1] => a [2] => l [3] => l [4] => e )
```

--

```php [2]
$text = "Kålle";
$splitted = str_split($text);

print_r($splitted);
```

```html
Array ( [0] => K [1] => � [2] => � [3] => l [4] => l [5] => e )
```

Hoppsan!

--

## mb_str_split

```php [2,3]
$text = "Kålle";
// $splitted = mb_str_split($text);
$splitted = mb_str_split($text, "utf-8");

print_r($splitted);
```

```html
Array ( [0] => K [1] => å [2] => l [3] => l [4] => e )
```

---

# substr o. mb_substr

--

Om man har en väldigt lång text och vill korta av den kan man använda sig **substr**.

--

## substr

```php [3]
$text = "Efter många om och men har Google meddelat att speltjänsten Stadia når vägs ände. Den 18 januari 2023 går den i graven för gott.";

$short = substr($text, 0, 14); // string, start, stop

echo "<p>" . $short . "</p>";
```

```html
Efter många o
```

--

```php [3]
$text = "Efter många om och men har Google meddelat att speltjänsten Stadia når vägs ände. Den 18 januari 2023 går den i graven för gott.";

$short = substr($text, 0, 8); // string, start, längd

echo "<p>" . $short . "</p>";
```

```html
Efter m�
```

Hoppsan!

--

## mb_substr

```php [3]
$text = "Efter många om och men har Google meddelat att speltjänsten Stadia når vägs ände. Den 18 januari 2023 går den i graven för gott.";

// $short = mb_substr($text, 0, 8);
$short = mb_substr($text, 0, 8, "utf-8");

echo "<p>" . $short . "</p>";
```

```html
Efter må
```

---

# SlUT!
