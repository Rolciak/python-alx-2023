liczby = [4, 5, 7, 10, 3, 5, 5, 6, 5, 5, 4, 4, 10, 1, 3, 3, 3, 3]

# wynik: [4, 5, 7, 10, 3, 6, 1]
# wypisać unikalne liczby (bez powtórzeń)
# (usunąć duplikaty)
# (oraz ile ich jest)

unikalne = []

for liczba in liczby:
    if liczba not in unikalne:
        unikalne.append(liczba)
print(unikalne)

unikalne2 = set(liczby)

print(unikalne2)

# nie można wyjąć elementu nr 3
# print(unikalne2[3])

unikalne3 = list(unikalne2)
print(unikalne3[3])

zbiorA = {1, 2, 3, 4, 5, 6}
zbiorB = {4, 5, 6, 7, 8, 9}

print(f'{zbiorA = }')
print(f'{zbiorB = }')
print(f'{zbiorA | zbiorB = }') # suma zbiorów
print(f'{zbiorA & zbiorB = }') # część wspólna zbiorów
print(f'{zbiorA - zbiorB = }') # różnica zbiorów
print(f'{zbiorA ^ zbiorB = }') # różnica symetryczna zbiorów

xxx = {"imie": "Mateusz"}   # to jest słownik, bo jest klucz: wartość
yyy = {"Mateusz"} # to jest zbiór, bo nie ma dwukropka
zzz = {}  # pusty słownik
zzz = dict()  # pusty słownik
z22 = set()  # pusty zbiór

print(type(zzz))