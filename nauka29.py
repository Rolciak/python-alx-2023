uczniowie = [
    {"imie": "Mateusz", "oceny": [4, 5, 6, 3, 3, 5]},
    {"imie": "Marcin", "oceny": [3, 5, 6, 2, 3, 2]},
    {"imie": "Piotr", "oceny": [2, 5, 5, 3, 6, 6]},
    {"imie": "Paweł", "oceny": [1, 6, 2, 3, 2, 5]},
]

for uczen in uczniowie:
    imie = uczen['imie']
    oceny = uczen['oceny']
    srednia = sum(oceny) / len(oceny)
    print(f'{imie} {srednia}')