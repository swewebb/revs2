# Emmet i Visual Studio Code

--

![Enter](images/emmet/emmet-enkel.gif)

**Emmet** är inbyggt från början i _Visual Studio Code_ och vi använder **ENTER** för att köra vår emmetsträng

--

![Enter](images/emmet/emmet-klick-vsc.gif)

Du kan även trycka på **skiftnyckeln** som dyker upp för att köra emmetsträngen.

---

# Skapa dokumentmallen

--

![Enter](images/emmet/emmet-dokmall.gif)

För att skapa dokumentmallen (html) använder vi **utropstecknet**.

---

# Använda plustecknet

--

![Enter](images/emmet/emmet-plus-vsc.gif)

Använder man plustecknet så skapar man två element efter varandra. Skriver vi **h1+p** kommer vi således få först en **h1:a** och därefter ett **p**.

När vi har kört vår emmetsträng så får vi insättnigspunkter för innehållet i taggarna och vi kan nu använda **TAB** för att hoppa mellan dem.

---

# Använda gångertecknet

--

![Enter](images/emmet/emmet-star-vsc.gif)

Vill vi skapa flera element av samma typ så kan vi använda oss av gångertecknet, t.ex **p*3**.

---

# Använda pil

--

![Enter](images/emmet/emmet-pil1-vsc.gif)

Med pilen kan vi lägga till barntaggar.

--

![Enter](images/emmet/emmet-pil2-vsc.gif)

Vi kan även använda pilen tillsammans med **lorem** för att fylla en tagg med innehåll.

---

# Använda parenteser

--

## Exempel 1

--

```html
<h1></h1>
<p></p>
<p></p>
<ol>
  <li></li>
  <li></li>
</ol>
<p></p>
```

Låt säga att vi vill skapa koden ovan med hjälp av emmet

--

![Enter](images/emmet/emmet-parentes-vsc.gif)

För att göra det skriver vi **h1+p\*2+(ol>li*2)+p**

--

## Exempel 2

--

```html
<div class="card">
  <h1></h1>
  <img src="" alt="">
  <p></p>
</div>
<div class="card">
  <h1></h1>
  <img src="" alt="">
  <p></p>
</div>
```

Låt säga att vi vill skapa koden ovan med hjälp av emmet. För att göra det skriver vi **(.card>h1+img+p)\*2**

---

# Sätta attribut

--

![Enter](images/emmet/emmet-attribut1-vsc.gif)

Med hjälp av **fyrkantsparenteser** kan vi sätta värdet på ett attribut.

Vill vi sätta flera attribut samtidigt använder vi ett mellanslag mellan attributen, t.ex <br> **input[name=test value=test]**.

---

# Lägga till innehåll

--

![Enter](images/emmet/emmet-klammer-vsc.gif)

Med hjälp av **klammerparenteser** ("måsvingar") kan vi lägga till innehåll i en tagg direkt i emmetsträngen.

--

![Enter](images/emmet/emmet-klammer2-vsc.gif)

Här visar jag hur vi kan sätta både attribut och innehåll på en gång.

---

# Lägga till en kommentar vid slutet på klasser/id:n

--

![Enter](images/emmet/emmet-kommentar-vsc.gif)

Vill man lägga till en automatisk kommentar som visar var en klass/id slutar använder vi **pipetecknet + c**, t.ex **.card>(h1+p)|c**

---

# Lägga till flera <br> klasser på en gång

--

![Enter](images/emmet/emmet-klasser-vsc.gif)

Om man vill lägga till flera klasser på en gång så skriver man ihop klasserna, t.ex **.klass1.klass2**

---

# Lägga till nummer

--

![Enter](images/emmet/emmet-nummer-vsc.gif)

Man kan med **$-tecknet** lägga till nummer.

I exemplet här skriver vi **ul>li.item${listpunkt $}\*3** och som du ser kan vi numrera t.ex både klassnamn och i innehållet.

---

# SLUT!