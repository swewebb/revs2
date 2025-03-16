text: str = ""

try:
    with open('./kurser/misc/textfil.txt', encoding = 'UTF-8') as f:
        text = f.read()
except FileNotFoundError:
    text = 'Filen kan inte öppnas!'
except Exception as error:
    text = f'Oväntat fel: {error}'
finally:
    print(text)
