namn: list[str] = ["Kalle", "Ann", "Olle-Bertil", "Erik"]
sorterat: list[str] = sorted(namn, key=lambda x: len(x))
print(sorterat)