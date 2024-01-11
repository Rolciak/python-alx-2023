nazwa_pliku = 'dane.txt'
with open(nazwa_pliku, 'r') as plik:
    wszystko = plik.readlines()

print(wszystko)

with open(nazwa_pliku, 'r') as plik:
    for linia in plik:
        print(linia)