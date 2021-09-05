# Python - Kapitel 18

---

# Filer

--

## Binärfiler

- Kompilerad kod
- Mediafiler
- ...

--

## Textfiler

- Textfiler
- XML
- CSV
- JSON
- Källkod
- ...

---

# Öppna, stänga o läsa filer

--

```html
Anne-Alica Anniesson
Bo-Balder Bjarnsson
Cliff-Cåre Claesson
```

--

```python
f = open('./textfil.txt', encoding = 'UTF-8')
text = (f.read())
f.close()

print(text)
```

```html
Anne-Alica Anniesson
Bo-Balder Bjarnsson 
Cliff-Cåre Claesson 
```

--

```python
f = open('./fil.txt', encoding = 'UTF-8')
text = f.read()
f.close()

print(text)
```

```html
Traceback (most recent call last):
  File "ex1.py", line 1, in <module>
    f = open('./fil.txt', encoding = 'UTF-8')
FileNotFoundError: [Errno 2] No such file or directory: './fil.txt' 
```

--

```python
try:
    f = open('./textfil.txt', encoding = 'UTF-8')
    text = f.read()
    f.close()
except:
    text = 'Filen kan inte öppnas!'
finally:
    print(text)
```

--

```python
with open('./textfil.txt', encoding = 'UTF-8') as f:
    text = f.read()

print(text)
```

--

```python
try:
    with open('./textfil.txt', encoding = 'UTF-8') as f:
        text = f.read()
except FileNotFoundError:
    text = 'Filen kan inte öppnas!'

print(text)
```

---

# Mer om att läsa filer

--

## readlines()

```python
try:
    with open('./textfil.txt', encoding = 'UTF-8') as f:
        text = f.readlines()
        print(text)
except FileNotFoundError:
    print('Filen kan inte öppnas!')
```

```html
['Anne-Alica Anniesson\n', 'Bo-Balder Bjarnsson\n', 'Cliff-Cåre Claesson']
```

--

## readline()

```python
try:
    with open('./textfil.txt', encoding = 'UTF-8') as f:
        text = f.readline()
        print(text)
except FileNotFoundError:
    print('Filen kan inte öppnas!')
```

```html
Anne-Alica Anniesson
```

--

```python
try:
    with open('./textfil.txt', encoding = 'UTF-8') as f:
        print(f.readline())
        print(f.readline())
except FileNotFoundError:
    print('Filen kan inte öppnas!')
```

```html
Anne-Alica Anniesson

Bo-Balder Bjarnsson
```

--

```python
try:
    with open('./textfil.txt', encoding = 'UTF-8') as f:
        print(f.readline(), end='')
        print(f.readline(), end='')
except FileNotFoundError:
    print('Filen kan inte öppnas!')
```

```html
Anne-Alica Anniesson
Bo-Balder Bjarnsson
```

--

```python
try:
    with open('./textfil.txt', encoding = 'UTF-8') as f:
        for line in f:
            print(line, end='')
except FileNotFoundError:
    print('Filen kan inte öppnas!')
```

```html
Anne-Alica Anniesson
Bo-Balder Bjarnsson
Cliff-Cåre Claesson
```

--

## read()

```python
try:
    with open('./textfil.txt', encoding = 'UTF-8') as f:
        text = f.read(4)
        print(text)
except FileNotFoundError:
    print('Filen kan inte öppnas!')
```

```
Anne
```

--

```python
try:
    with open('./textfil.txt', encoding = 'UTF-8') as f:
        text = f.read(4)
        print(text)
        text = f.read(6)
        print(text)
except FileNotFoundError:
    print('Filen kan inte öppnas!')
```

```html
Anne
-Alica
```

--

```python
try:
    with open('./textfil.txt', encoding = 'UTF-8') as f:
        sizeToRead = 5
        txt = f.read(sizeToRead)
        
        while len(txt) > 0:
            print(txt, end=' * ')
            txt = f.read(sizeToRead)

except FileNotFoundError:
    print('Filen kan inte öppnas!')
```

```html
Anne- * Alica *  Anni * esson * 
Bo-B * alder *  Bjar * nsson *
Clif * f-Cår * e Cla * esson *
```

---

# Skriva

--

```python
listan = ['Å', 'Ä', 'Ö']

with open('./listan.txt', 'w', encoding = 'UTF-8') as f:
    for x in listan:
        f.write(x)
```

```html
ÅÄÖ
```

--

```python
listan = ['Å', 'Ä', 'Ö']

with open('./listan.txt', 'w', encoding = 'UTF-8') as f:
    for x in listan:
        f.write(x)
        f.write('\n')
```

```html
Å
Ä
Ö
```

--

```python
listan = ['Å', 'Ä', 'Ö']

with open('./listan.txt', 'w', encoding = 'UTF-8') as f:
    for x in listan:
        print(x, file=f)
```

```html
Å
Ä
Ö
```

--

```python
Traceback (most recent call last):
  File "ex-w-3.py", line 3, in <module>
    with open('./listan.txt', 'w', encoding = 'UTF-8') as f:
PermissionError: [Errno 13] Permission denied: './listan.txt'
```

--

```python
try:
    listan = ['Å', 'Ä', 'Ö']

    with open('./listan.txt', 'w', encoding = 'UTF-8') as f:
        for x in listan:
            print(x, file=f)
except PermissionError:
    print('Går ej att skriva filen')
```

```
Går ej att skriva filen
```

--

```python
try:
    listan = ['Å', 'Ä', 'Ö']

    with open('./listan.txt', 'w', encoding = 'UTF-8') as f:
        for x in listan:
            print(x, file=f)
except Exception as e:
    print(e)
```

```html
[Errno 13] Permission denied: './listan.txt'
```

--

```python
try:
    listan = ['Å', 'Ä', 'Ö']

    with open('./listan.txt', 'a', encoding = 'UTF-8') as f:
        for x in listan:
            print(x, file=f)
except Exception as e:
    print(e)
```

```html
Å
Ä
Ö
Å
Ä
Ö
```

--

```python
try:
    txt = input('Skriv in post: ')

    with open('./post.txt', 'a', encoding = 'UTF-8') as f:
        f.write(txt)
        f.write('\n')
except Exception as e:
    print(e)
```

```html
Skriv in post: Plugga inför NP MA3   
```

```html
Plugga inför NP FY1
Plugga inför NP MA3
```

--

```python
try:
    pic = 'bild.png'

    with open(pic, 'rb') as rf:
        with open('kopia.png', 'wb') as wf:
            chunk = 1024
            picChunk = rf.read(chunk)

            while len(picChunk) > 0:
                wf.write(picChunk)
                picChunk = rf.read(chunk)
except Exception as e:
    print(e)
```

---

# Lägen

--

## w

Filen skall öppnas för skrivning (w=write). 

Finns filen redan skrivs den över, annars skapas en ny fil.

--

## r


Filen skall öppnas för läsning (r=read). 

Filen måste finnas sedan tidigare.

--

## a

Filen skall öppnas för skrivning i slutet (a=append). 

Finns filen läggs data in sist i filen, annars skapas en ny fil.

--

## +

Läggs till modesträngen om man vill både läsa och skriva i samma filöppning.

--

```python
myfile = './testfile.txt'

f = open(myfile, 'r')  # Öppna för endast läsning
f = open(myfile, 'r+') # Öppna för läsning och skrivning
f = open(myfile, 'w')  # Öppna för skrivning
```

---

# Tricks

--

```python
import os

myfile = './testfile.txt'

if os.path.exists(myfile):
    print('Filen finns')
else:
    print('Filen finns inte')
```

Modulen `os` kan användas för att ta reda på om en fil finns.

--

```python
import os

myfile = './textfil.txt'

if os.path.exists(myfile):
    with open(myfile, encoding = 'UTF-8') as f:
        text = f.read()

    print(text)
```

---

# Slut!