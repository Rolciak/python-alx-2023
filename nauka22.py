imiona = [
    'Adam',
    'Ola',
    'Mateusz',
    'Michał',
    'Iwo',
    'Stanisław',
    'Artem',
    'Władysław',
    'Karina',
    'Ala',
    'Maria',
]
max_dlugosc = 0
min_dlugosc = None
for imie in imiona:
    # TODO: przy każdej osobie napisać długość imienia
    print('----------')
    print(f'* Imię: {imie}')
    dlugosc_imienia = len(imie)
    if dlugosc_imienia > max_dlugosc:
        max_dlugosc = dlugosc_imienia
    if min_dlugosc is None or dlugosc_imienia < min_dlugosc:
        min_dlugosc = dlugosc_imienia
    print(f'* Długość znaków: {len(imie)}')
print('----------')
dodanie_imion = "".join(imiona)
suma_imiona = len(dodanie_imion)
print(f'* Długość sumeryczna: {suma_imiona}')
print(f"* Długość najdluzszego imienia: {max_dlugosc}")
print(f"* Długość najkrotszego imienia: {min_dlugosc}")

for imie in imiona:
    if len(imie) == min_dlugosc:
        print(f"{imie} Najkrótrsze")
    if len(imie) == max_dlugosc:
        print(f"{imie} Najdłuższe")

print("Męskie: (bez a na końcu)")
for imie in imiona:
    if not imie.endswith('a'):
        print(f"- {imie}")

print("Damskie: (z a na końcu)")
for imie in imiona:
    if imie.endswith('a'):
        print(f"- {imie}")