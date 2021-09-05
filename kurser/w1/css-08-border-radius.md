# CSS - 08 - Runda hörn

## Webbutveckling 1

---

# Border-radius

Med egenskapen `border-radius` kan vi skapa runda hörn.

Vi behöver *inte* ha en kantlinje för att kunna använda oss av `border-radius`.

**Värden:** Längdvärden (t.ex px, rem, em) och %

---

# Alla hörn

```css
div {
  background-color: #d63031;
  border-radius: 20px;
  height: 100px;
  width: 100px;
}
```

![bild](images/css-br-1.PNG)

---

# Top-left och bottom-right | top-right och bottom-left 

```css
div {
  background-color: #d63031;
  border-radius: 20px 40px;
  height: 100px;
  width: 100px;
}
```

![bild](images/css-br-2.PNG)

---

# Top-left | top-right | bottom-right | bottom-left

```css
div {
  background-color: #d63031;
  border-radius: 20px 40px 70px 100px;
  height: 100px;
  width: 100px;
}
```

![bild](images/css-br-3.PNG)

---

# Procent

```css
div {
  background-color: #d63031;
  border-radius: 50%;
  height: 100px;
  width: 100px;
}
```

![bild](images/css-br-4.PNG)

--

```css
div {
  background-color: #d63031;
  border-radius: 50%;
  height: 100px;
  width: 200px;
}
```

![bild](images/css-br-5.PNG)

--

```css
div {
  background-color: #d63031;
  border-radius: 50% 0;
  height: 100px;
  width: 200px;
}
```

![bild](images/css-br-6.PNG)

---

# x- och y-värde


```css
div {
  background-color: #d63031;
  border-radius: 20px/40px;
  height: 100px;
  width: 200px;
}
```

![bild](images/css-br-7.PNG)

---

# Runt hörn i enbart ett hörn

Använd:
  * `border-top-left-radius`
  * `border-top-right-radius`
  * `border-bottom-right-radius`
  * `border-bottom-left-radius`

---

# Slut!
