imiona = [
    'mateusz',
    'adam',
    'michal',
    'iwo',
    'stanislaw',
    'artem',
]

for imie in imiona:
    # TODO: przy każdej osobie napisać długość imienia
    print('----------')
    print(f'* Imię: {imie}')
    print(f'* Długość znaków: {len(imie)}')
print('----------')
dodanie_imion = "".join(imiona)
suma_imiona = len(dodanie_imion)
print(f'* Długość sumeryczna: {suma_imiona}')