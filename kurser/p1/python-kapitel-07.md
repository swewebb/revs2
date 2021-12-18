# Python - Kapitel 7

---

# DEC till BIN - Metod 1

--

## 75 till binärt

![bin-dec](images/talsystem/dec-bin-1.png)

<p style="text-align: center"><b>75d = 1001011b</b></p>

--

## 148 till bin

![bin-dec](images/talsystem/dec-bin-2.png)

<p style="text-align: center"><b>148d = 10010100b</b></p>

--

## 596 till bin

![bin-dec](images/talsystem/dec-bin-3.png)

<p style="text-align: center"><b>596d = 1001010100b</b></p>

---

# DEC till BIN - Metod 2


--

## 75 till binärt

![dec](images/talsystem/dec-bin-4.png)

<p style="text-align: center"><b>75d = 1001011b</b></p>
<p style="text-align: center">Läs det binära talet nerifrån och uppåt</p>


--

## 148 till bin

![dec](images/talsystem/dec-bin-5.png)

<p style="text-align: center"><b>148d = 10010100b</b></p>

--

## 596 till bin

![dec](images/talsystem/dec-bin-6.png)

<p style="text-align: center"><b>596d = 1001010100b</b></p>


---

# BIN till DEC - Metod 1

--

# 1010111 till decimalt

<p>
<span class="bluetext">1 * 2<sup>6</sup></span> +
<span class="greentext">0 * 2<sup>5</sup></span> +
<span class="redtext">1 * 2<sup>4</sup></span> +
<span class="purpletext">0 * 2<sup>3</sup></span> +
<span class="orangetext">1 * 2<sup>2</sup></span> +
<span class="pinktext">1 * 2<sup>1</sup></span> +
<span class="turkostext">1 * 2<sup>0</sup></span>
</p>

<p>
<span class="bluetext">1 * 64</span> +
<span class="greentext">0 * 32</span> +
<span class="redtext">1 * 16</span> +
<span class="purpletext">0 * 8</span> +
<span class="orangetext">1 * 4</span> +
<span class="pinktext">1 * 2</span> +
<span class="turkostext">1 * 1</span>
</p>

<p>
<span class="bluetext">1 * 64</span> +
<span class="redtext">1 * 16</span> +
<span class="orangetext">1 * 4</span> +
<span class="pinktext">1 * 2</span> +
<span class="turkostext">1 * 1</span>
</p>

<p>
<span class="bluetext">64</span> +
<span class="redtext">16</span> +
<span class="orangetext">4</span> +
<span class="pinktext">2</span> +
<span class="turkostext">1</span> = 87
</p>

<p><b>1010111b = 87d</b></p>

---

# BIN till DEC - Metod 2

--

# 1010111 till decimalt

![bin](images/talsystem/bin-dec-1.png)

<p style="text-align: center">64 + 16 + 4 + 2 + 1 = 87</p>

<p style="text-align: center"><b>1010111b = 87d</b></p>

--

# 11101101 till decimalt

![bin](images/talsystem/bin-dec-2.png)

<p style="text-align: center">128 + 64 + 32 + 8 + 4 + 1 = 237</p>

<p style="text-align: center"><b>11101101b = 237d</b></p>

--

# 1110110101010111 till decimalt

![bin](images/talsystem/bin-dec-3.png)

<p style="text-align: center">32768 + 16384 + 8192 + 2048 +  1024 + <br> 256 + 64 + 16 + 4 + 2 + 1 = 60759</p>

<p style="text-align: center"><b>1110110101010111b = 60759d</b></p>

---

# BIN till DEC - Metod 3

--

# 1010111 till decimalt

![bin](images/talsystem/bin-dec-4.png)

--

# 11101101 till decimalt

![bin](images/talsystem/bin-dec-5.png)

--

# 1110110101010111 till decimalt

![bin](images/talsystem/bin-dec-6.png)

---

# DEC till HEX

--

## 47 till hexadecimalt

![hex](images/talsystem/dec-hex-1.png)

<p style="text-align: center">"2 15" &rarr; 2F</p>

<p style="text-align: center"><b>47d = 2Fh</b></p>

--

## 232 till hexadecimalt

![hex](images/talsystem/dec-hex-2.png)

<p style="text-align: center"><b>323d = 143h</b></p>

--

## 3805 till hexadecimalt

![hex](images/talsystem/dec-hex-3.png)

<p style="text-align: center">"14 13 13" &rarr; EDD</p>

<p style="text-align: center"><b>3805d= EDDh</b></p>

---

# HEX till DEC

--

## 2F till decimalt

<p style="text-align: center">2*16<sup>1</sup> + F*16<sup>0</sup></p>
<p style="text-align: center">2*16<sup>1</sup> + 15*16<sup>0</sup></p>
<p style="text-align: center">32 + 15 = 47</p>
<p style="text-align: center"><b>2Fh = 47d</b></p>

--

## 143 till decimalt

<p style="text-align: center">1*16<sup>2</sup> + 4*16<sup>1</sup> + 3*16<sup>0</sup></p>
<p style="text-align: center">256 + 64 + 3 = 323</p>
<p style="text-align: center"><b>143h = 323d</b></p>

--

## EDD till decimalt

<p style="text-align: center">E*16<sup>2</sup> + D*16<sup>1</sup> + D*16<sup>0</sup></p>
<p style="text-align: center">14*16<sup>2</sup> + 13*16<sup>1</sup> + 13*16<sup>0</sup></p>
<p style="text-align: center">3584 + 208 + 13 = 3805</p>


<p style="text-align: center"><b>EDDh = 3805d</b></p>

---

# BIN till HEX

--

<p style="text-align: center">Dela upp i grupper om fyra från minst värd siffra</p>
<p style="text-align: center">Översätt från binärt till decimal form,<br> om 10-15 ange A-F.</p>

--

![tabell](images/talsystem/hex-bin-tabell.png)

--

**Kolumn ett** = Varannan nolla och etta osv

**Kolumn två** = Två nollor, två ettor osv.

**Kolumn tre** = Fyra nollor, fyra ettor osv.

**Kolumn fyra** = Åtta nollor, åtta ettor osv.

Första värdet kommer alltid vara enbart nollor i BIN.

Sista värdet kommer alltid vara enbart ettor i BIN.

--

## 101 till hexadecimalt

<p style="text-align: center">101</p>

<p style="text-align: center"><b>0101b = 5h</b></p>


--

## 10101110110 till hexadecimalt

<p style="text-align: center">10101110110</p>

<p style="text-align: center">
<span class="greentext">0101</span> <span class="bluetext">0111</span> <span class="purpletext">0110</span> =
<span class="greentext">5</span> <span class="bluetext">7</span> <span class="purpletext">6</span></p>

<p style="text-align: center"><b>10101110110b = 576h</b></p>


--

## 1011111111010 till hexadecimalt

<p style="text-align: center">1011111111010</p>


<p style="text-align: center">
<span class="redtext">0001</span> <span class="greentext">0111</span> <span class="bluetext">1111</span> <span class="purpletext">1010</span> =
<span class="redtext">1</span> <span class="greentext">7</span> <span class="bluetext">15</span> <span class="purpletext">10</span>
</p>

<p style="text-align: center">
<span class="redtext">1</span> <span class="greentext">7</span> <span class="bluetext">15</span> <span class="purpletext">10</span> =
<span class="redtext">1</span> <span class="greentext">7</span> <span class="bluetext">F</span> <span class="purpletext">A</span>
</p>

<p style="text-align: center"><b>1011111111010b = 17FAh</b></p>

---

# HEX till BIN

--

Översätt varje siffra för sig till 4-bitars binär form, använd tabellen.

--

![tabell](images/talsystem/hex-bin-tabell.png)

--

## 5 till binärt

<p style="text-align: center">5 = 0101</p>

<p style="text-align: center"><b>5h = 101b</b></p>

--

## 576 till binärt

<p style="text-align: center">5 = 0101, 7 = 0111, 6 = 0110</p>
<p style="text-align: center">576h = 0101 0111 0110</p>
<p style="text-align: center"><b>576h = 10101110110b</b></p>

--

## 17FA till binärt

<p style="text-align: center">1 = 0001, 7 = 0111, F = 1111, A = 1010</p>
<p style="text-align: center">17FAh = 0001 0111 1111 1010b</p>
<p style="text-align: center"><b>17FAh = 1011111111010b</b></p>

---

# SLUT!
