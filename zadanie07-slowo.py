slowo = str(input("podaj slowo: "))
dlugosc_tekstu = int(len(slowo))

if dlugosc_tekstu == 0:
    print("Nie podales slowa")
elif ' ' in slowo:
    print("slowo zawiera spacje")
elif dlugosc_tekstu > 5 and 'nie' not in slowo:
    print(f"Slowo jest dluzsze niz 5 liter i nie zawiera slowa NIE")
elif dlugosc_tekstu > 5 and 'nie' in slowo:
    print("slowo jest dluzsze niz 5 liter i zawiera slowo NIE")
elif dlugosc_tekstu <= 5 and 'nie' not in slowo:
    print(f"Slowo jest krotsze lub rowne 5 liter i nie zawiera slowa NIE")
elif dlugosc_tekstu <= 5 and 'nie' in slowo:
    print("slowo jest krotsze lub rowne 5 liter i zawiera slowo NIE")