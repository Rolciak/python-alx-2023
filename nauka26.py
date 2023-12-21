suma = 0

while True:
    podana_liczba = input("Podaj liczbę: ")
    if podana_liczba == "":
        continue
    if podana_liczba == "koniec":
        break
    liczba = float(podana_liczba)
    suma += liczba
    print(f"Suma: {suma}")
    if suma > 100:
        break