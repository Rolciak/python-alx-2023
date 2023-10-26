# Pytania

kwota = float(input("Podaj kwote: "))
waluta = input("Podaj walute (USD, EUR, CHF, FUNT): ")

# Waluty i przeliczone ceny na złote

USD = 4.20
EUR = 4.46
CHF = 4.70
FUNT = 5.12

# Obliczenie walut na złotówki

if waluta == "USD":
    wynik = kwota * USD
elif waluta == "EUR":
    wynik = kwota * EUR
elif waluta == "CHF":
    wynik = kwota * CHF
elif waluta == "FUNT":
    wynik = kwota * FUNT
else:
    print(f"Nie znana waluta. {waluta}?")
    exit()

print(f"{kwota} {waluta} to jest {wynik} złoty")




