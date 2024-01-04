import urllib.request
import json
from pprint import pprint

url = "https://api.nbp.pl/api/exchangerates/rates/A/usd/last/?format=json"

with urllib.request.urlopen(url) as odpowiedz_serwera:
    wynik = json.load(odpowiedz_serwera)

USD = wynik['rates'][0]['mid']

kwota = float(input("Podaj kwotę: "))
waluta = input("Podaj walute: ")

if waluta == "USD":
    wynik = kwota * USD

print(f"{kwota} {waluta} to {wynik} PLN")