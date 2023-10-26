# Program ktory powie czy jestes pelnoletni czy niepelnoletni

dataurodzenia = int(input("Podaj rok urodzenia: "))
rok = 2023

wiek = rok - dataurodzenia

if wiek > 18:
    print(f"Masz {wiek} lat i jesteś pełnoletni!")
else:
    print(f"Masz {wiek} lat i jesteś niepełnoletni!")
    