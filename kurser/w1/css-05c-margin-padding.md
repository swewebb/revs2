# CSS - Marginaler och padding

## Webbutveckling 1

---

# Marginal

--

Med marginal menas avståndet från ett element till ett annat.

Anges med egenskaperna **margin**, **margin-top**, **margin-right**, **margin-bottom** och **margin-left**.

--

## Lite förberande kod

Här kommer den kod vi kommer att utgå för att förklara margin. Kolla igenom den om du vill, inget krav!

--

```html []
<div class="box box__1">Box 1</div>
<div class="box box__2">Box 2</div>
```

--

```css []
body {
  margin: 0;
  padding: 0;
}

.box {
  width: 100px;
  height: 100px;

  display: grid;
  justify-content: center;
  align-items: center;

  font-family: Arial, sans-serif;
  font-size: 25px;
  color: #FFF;
}

.box__1 {
    background:#0984E3;
}

.box__2 {
    background-color: #E84393;
}
```

--

![bild](images/css-margin-padding-1.png)

--

## Marginal med ett värde

```css [3]
.box__1 {
  background:#0984E3;
  margin: 20px;
}

.box__2 {
    background-color: #E84393;
}
```

Anger vi ett värde så kommer vi få samma marginal på alla fyra sidor.

--

![bild](images/css-margin-padding-2.png)

--

## Marginal med två värden

```css [3]
.box__1 {
  background:#0984E3;
  margin: 20px 50px;
}

.box__2 {
  background-color: #E84393;
}
```

Anger vi två värden så kommer det första värdet ange **top/bottom** och det andra **left/right**.

--

![bild](images/css-margin-padding-3.png)

--

## Marginal med fyra värden

```css [3]
.box__1 {
  background:#0984E3;
  margin: 20px 30px 40px 50px;
}

.box__2 {
  background-color: #E84393;
}
```

Anger vi två värden så kommer vi ange **top**, **right**, **bottom**, **left**

--

![bild](images/css-margin-padding-4.png)

--

## Margin Collapse


```css [3, 8]
.box__1 {
  background:#0984E3;
  margin: 20px;
}

.box__2 {
  background-color: #E84393;
  margin: 20px;
}
```

Om vi anger en marginal även för **box__2** så skulle man kunna tro att den totala marginalen mellan de två boxarna skulle bli 40px, men så blir det inte utan de går över varandra och den marginal med störst värde vinner.

--

![bild](images/css-margin-padding-5.png)

--

## Margin med auto

```css [2]
.box {
  margin: 0 auto;
  width: 60%;
  max-width: 800px;
  background:#0984E3;
}
```

Med värdet **auto** kan vi centrera ett element horisontellt.

--

![css-margin-padding-auto](images/css-margin-padding-auto.png)

---

# Padding

--

Med **padding** menas avståndet från kanten på en tagg till själva innehållet.

Anges med egenskaperna **padding**, **padding-top**, **padding-right**, **padding-bottom** och **padding-left**.

--

## Ingen padding

--

![bild](images/css-margin-padding-7.png)

--

## Padding med ett värde

--

```css [10]
.box {
  width: 400px;

  font-family: Arial, sans-serif;
  font-size: 50px;
  color: #FFF;

  background:#0984E3;

  padding: 2rem;
}
```

--

![bild](images/css-margin-padding-8.png)

--

## Padding med två värden

--

```css [10]
.box {
  width: 400px;

  font-family: Arial, sans-serif;
  font-size: 50px;
  color: #FFF;

  background:#0984E3;

  padding: 4rem 2rem;
}
```

--

![bild](images/css-margin-padding-9.png)

--

## Padding med fyra värden

--

```css [10]
.box {
  width: 400px;

  font-family: Arial, sans-serif;
  font-size: 50px;
  color: #FFF;

  background:#0984E3;

  padding: 1rem 2rem 3rem 4rem;
}
```

--

![bild](images/css-margin-padding-10.png)

--

![bild](images/css-margin-padding-11.png)

---

# SLUT
