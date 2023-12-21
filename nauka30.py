import urllib.request
import json
from pprint import pprint

url = "https://api.nbp.pl/api/exchangerates/tables/A/"

with urllib.request.urlopen(url) as odpowiedz_serwera:
    wynik = json.load(odpowiedz_serwera)

USD = wynik['currency'][0]['mid'] # 3.9645 teraz

pprint(USD)
# Przeliczenie różnych kursów, program

kwota = float(input("Podaj kwotę: "))
waluta = input("Podaj Walute: ")

if waluta == "USD":
    przeliczenie = kwota * USD

print(f"{kwota} {waluta} to {przeliczenie} PLN.")