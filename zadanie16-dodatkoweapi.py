import urllib.request
import json
from pprint import pprint

url = "https://randomuser.me/api/"

with urllib.request.urlopen(url) as odpowiedz_serwera:
    wynik = json.load(odpowiedz_serwera)

imie = wynik['results'][0]['name']['first']
nazwisko = wynik['results'][0]['name']['last']
wiek = wynik['results'][0]['registered']['age']
email = wynik['results'][0]['email']
numer_telefonu = wynik['results'][0]['phone']

print(f"Imie i nazwisko: {imie} {nazwisko}")
print(f"Wiek: {wiek}")
print(f"E-mail: {email}")
print(f"Numer Telefonu: {numer_telefonu}")