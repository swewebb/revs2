# Textfiler

---

# Kontrollera om en fil finns

--

```php []
<?php
$file = "demo.txt";

if (file_exists($file)) {
  $result = "Filen finns";
} else {
  $result = "Filen finns inte";
}
?>
```

```html []
<div class="posts">
  <?= $result ?>
</div>
```

--

BILD

--

```php []
<?php
$file = "demo.txt";

$result = file_exists($file) ? "Filen finns" : "Filen finns inte";
?>
```

```html []
<div class="posts">
  <?= $result ?>
</div>
```

--

BILD

---

# Läsa hela filen

--

```php []
<?php
$file = "demo.txt";

if (file_exists($file)) {
  $result = file_get_contents($file);
} else {
  $result = "Filen finns inte";
}
?>
```

```html []
<div class="posts">
  <?= $result ?>
</div>
```

--

BILD

--

```php []
<?php
$file = "demo.txt";

$result = file_exists($file) ? file_get_contents($file) : "Filen finns inte";
?>
```

```html []
<div class="posts">
  <?= $result ?>
</div>
```

--

BILD

---

# Dump and Die

```php []
<?php

/**
 * Dump and Die
 *
 * @param  $data
 * @return void
 */
function dd($data): void
{
  echo "<pre>";
  var_dump($data);
  echo "</pre>";
  die();
}
```

---

# Läsa ut en rad i taget - A

--


```php []
<?php
require "functions.php";

$file = "demo.txt";

if (file_exists($file)) {
  $result = file($file);

  if(empty($result)) {
    $result = "Filen är tom";
  }
} else {
  $result = "Filen finns inte";
}
?>
```

```html []
<div class="posts">
  <?= dd($result) ?>
</div>
```

--

BILD

--


```php []
<div class="posts">
  <?php
  if (is_array($result)) {
    foreach ($result as $post) {
      echo "<div class='post'>";
      echo "<p>$post</p>";
      echo "</div>";
    }
  } else {
    echo "<p>$result</p>";
  }
  ?>
</div>
```

--

BILD

---

# Läsa ut en rad i taget - B

--

```php []
<?php
require "functions.php";

$file = "demo.txt";

$result = file_exists($file) ? file($file)?: "Filen är tom" : "Filen finns inte";

$check = is_array($result);
?>
```

--

```php []
<div class="posts">
  <?php
  if ($check) {
    foreach ($result as $post) {
      echo <<<POST
      <div class="post">
        <p> $post </p>
      </div>
      POST;
    }
  }

  if (!$check) {
    echo "<p>$result</p>";
  }
  ?>
</div>
```

--

BILD


---

# Dela upp rader - A

--

```html []
komplett.se|Komplett
dustin.se|Dustin
inet.se|Inet
```

--

```php []
<?php
  require "functions.php";

  $file = "links.txt";

  if (file_exists($file)) {
    $result = file($file);

    if(empty($result)) {
      $result = "Filen är tom";
    }
  } else {
    $result = "Filen finns inte";
  }
  ?>
```

--

```php [5-9]
<div class="posts">
  <?php
  if (is_array($result)) {
    foreach ($result as $post) {
      $part = explode("|", $post);

      echo "<div class='post'>";
      echo "<p><a href='https://$part[0]'>$part[1]</a></p>";
      echo "</div>";
    }
  } else {
    echo "<p>$result</p>";
  }
  ?>
</div>
```

--

BILD

---

# Dela upp rader - B

--

```html []
komplett.se|Komplett
dustin.se|Dustin
inet.se|Inet
```

--

```php []
<?php
require "functions.php";

$file = "links.txt";

$result = file_exists($file) ? file($file)?: "Filen är tom" : "Filen finns inte";

$check = is_array($result);
?>
```

--

```php [5-11]
<div class="posts">
  <?php
  if ($check) {
    foreach ($result as $post) {
      $part = explode("|", $post);

      echo <<<POST
      <div class="post">
        <p><a href='https://$part[0]'>$part[1]</a></p>
      </div>
      POST;
    }
  }

  if (!$check) {
    echo "<p>$result</p>";
  }
  ?>
</div>
```

--

BILD

---

# SLUT!
