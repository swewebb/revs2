# Python - Kapitel 2

## Lösningar

---

# e02-01

--

## Lösning 1

```python [ ]
print('Hello world')
```

--

## Lösning 2

```python
txt='Hello world'

print(txt)
```

---

# e02-02

--

## Lösning 1

```python
print("Lisa \"Superkodaren\" Hammare")
```

--

## Lösning 2

```python
print('Lisa "Superkodaren" Hammare')
```

--

## Lösning 3

```python
txt="Lisa \"Superkodaren\" Hammare"
print(txt)
```

--

## Lösning 4

```python
txt='Lisa "Superkodaren" Hammare'
print(txt)
```

---

# e02-03

--

## Lösning 1

```python
a = 50
b = 960
c = a + b

print(a, '+', b ,'=', c)
```

--

## Lösning 2

```python
a = 50
b = 960
c = a + b

print('{} + {} = {}'.format(a, b, c))
```

--

## Lösning 3

```python
a = 50
b = 960
c = a + b

print(f'{a} + {b} = {c}')
```

--

## Lösning 4

```python
a = 50
b = 960
c = a + b

print(str(a) + ' + ' + str(b) + ' = ' + str(c))
```

---

# e02-04

--

## Lösning 1

```python
a = 25
b = 7
c = a % b

print(a, '%', b ,'=', c)
```

--

## Lösning 2

```python
a = 25
b = 7
c = a % b

print('{} % {} = {}'.format(a, b, c))
```

--

## Lösning 3

```python
a = 25
b = 7
c = a % b

print(f'{a} % {b} = {c}')
```

--

## Lösning 4

```python
a = 50
b = 960
c = a % b

print(str(a) + ' % ' + str(b) + ' = ' + str(c))
```

---

# e02-05

--

## Lösning 1

```python
a = 25
b = 7
c = a // b

print(a, '//', b ,'=', c)
```

--

## Lösning 2

```python
a = 25
b = 7
c = a // b

print('{} // {} = {}'.format(a, b, c))
```

--

## Lösning 3

```python
a = 25
b = 7
c = a // b

print(f'{a} // {b} = {c}')
```

--

## Lösning 4

```python
a = 50
b = 960
c = a // b

print(str(a) + ' // ' + str(b) + ' = ' + str(c))
```

---

# e02-06

--

## Lösning 1

```python
a = 10
b = 20
c = a + b

print('Summan av {:.2f} och {:.2f} är {:.2f}'.format(a, b, c))
```

--

## Lösning 2

```python
a = 10
b = 20
c = a + b

print(f'Summan av {a:.2f} och {b:.2f} är {c:.2f}')
```

---

# e02-07

--

## Lösning 1

```python
dec = 24

print('Dec: {} är Bin: {:08b}'.format(dec, dec))
```

--

## Lösning 2

```python
dec = 24

print('Dec: {0} är Bin: {0:08b}'.format(dec))
```

--

## Lösning 3

```python
dec = 24

print(f'Dec: {dec} är Bin: {dec:08b}')
```

---

# e02-08

--

## Lösning 1

```python
txt = input("Ange ett heltal:")
dec = int(txt)

print('Dec: {} är Bin: {:08b}'.format(txt, dec))
```

--

## Lösning 2

```python
dec = int(input("Ange ett heltal:"))

print('Dec: {0} är Bin: {0:08b}'.format(dec))
```

--

## Lösning 3

```python
print('Dec: {0} är Bin: {0:08b}'.format(int(input("Ange ett heltal:"))))
```

--

## Lösning 4

```python
dec = int(input("Ange ett heltal:"))

print(f'Dec: {dec} är Bin: {dec:08b}')
```

---

# Slut
