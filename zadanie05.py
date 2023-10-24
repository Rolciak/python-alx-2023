# Program na obliczenie BMI przez wage i wzrost

waga = float(input("Ile ważysz (napisz w kg): "))
wzrost = float(input("Ile masz centrymetrów wzrostu: "))

wzrost_metry = wzrost / 100
BMI = waga / (wzrost_metry ** 2)

if BMI < 18.5:
    print(f"Wynik BMI wynosi: {BMI} masz niedowagę.")
elif 18.5 <= BMI < 24.9:
    print(f"Wynik BMI wynosi: {BMI} masz właściwą wage.")
elif 25 <= BMI < 29.9:
    print(f"Wynik BMI wynosi: {BMI} masz nadwagę.")
else:
    print(f"Wynik BMI wynosi: {BMI} jesteś otyły.")
