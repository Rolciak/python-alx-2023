uczen_a = {"imie": "Mateusz", "oceny": [5,5,5,5]}

uczen_b = {"imie": "Marcin"}

oceny_ucznia_a = uczen_a['oceny']

uczen_b['oceny'] = [*oceny_ucznia_a]

print(uczen_b)

uczen_a['oceny'].append(3)
uczen_a['oceny'][1] = 1

print(uczen_a)
print(uczen_b)