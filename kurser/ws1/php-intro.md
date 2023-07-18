# Introduktion

---

# PHP

--

PHP = PHP: Hypertext Preprocessor

Används på [77,5%](https://w3techs.com/technologies/overview/programming_language) (2023-07-13) av alla webbplatser.

---

# Användningsområde

--

- Generera dynamiskt innehåll
- Filhantering
- Ta emot data från formulär
- Hantera kakor och sessioner
- Arbeta med databaser
- Hantera användare
- Kryptera data

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
<html lang="sv">
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

# SLUT
