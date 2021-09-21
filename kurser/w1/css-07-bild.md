# CSS - Bilder

## Webbutveckling 1

---

# Positionera bilder

--

## Utgångspunkt

```html
<h1>En rubrik</h1>
<img src="http://placekitten.com/180/180" alt="">

<p>Lorem...</p>

<img src="http://placekitten.com/180/180" alt="">

<p>Lorem...</p>
```

```css [ ]
p {
  border: 1px solid #000;
  width: 500px;
}
```

--

![bild](images/css-bild-1.PNG)

--

```css [ ]
img {
  float: left;
  clear: both;
  margin: 0 10px 0 0;
}
```

För egenskapen `float` har vi värdena *left*, *right*, *none*.

För egenskapen `clear` har vi värdena *left*, *right*, *both* och *none*.

--

![bild](images/css-bild-2.PNG)

--

Saxat från MDN (https://developer.mozilla.org/en-US/docs/Web/CSS/clear) om `clear`

![bild](images/css-bild-3.png)

---

# Slut!
