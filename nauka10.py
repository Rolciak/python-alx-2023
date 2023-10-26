slowo = input("Podaj slowo zawierajace litere a oraz dluzsze niz 5 liter: ")

if "a" in slowo:
    print("Zawiera A")
else:
    print("źle! brak litery A")

if len(slowo) > 5:
    print("Prawidlowa dlugosc")
else:
    print("Za krótkie")

