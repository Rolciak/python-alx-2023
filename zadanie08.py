def oblicz_bmi(waga, wzrost, jednostka_wagi='kg', jednostka_wzrostu='m'):

    if jednostka_wagi.lower() == 'g':
        waga /= 1000

    if jednostka_wzrostu.lower() == 'cm':
        wzrost /= 100 

    bmi = waga / (wzrost ** 2)

    return bmi

waga = float(input("Podaj wagę: "))
jednostka_wagi = input("Podaj jednostkę wagi (g lub kg): ")
wzrost = float(input("Podaj wzrost: "))
jednostka_wzrostu = input("Podaj jednostkę wzrostu (cm lub m): ")

wynik_bmi = oblicz_bmi(waga, wzrost, jednostka_wagi, jednostka_wzrostu)

if wynik_bmi < 18.5:
    print(f"Wynik BMI wynosi: {wynik_bmi} masz niedowagę.")
elif 18.5 <= wynik_bmi < 24.9:
    print(f"Wynik BMI wynosi: {wynik_bmi} masz właściwą wage.")
elif 25 <= wynik_bmi < 29.9:
    print(f"Wynik BMI wynosi: {wynik_bmi} masz nadwagę.")
else:
    print(f"Wynik BMI wynosi: {wynik_bmi} jesteś otyły.")