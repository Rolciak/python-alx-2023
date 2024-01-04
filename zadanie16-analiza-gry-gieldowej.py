import urllib.request
import json

def pobierz_kursy_waluty(kod_waluty):
    url = f'http://api.nbp.pl/api/exchangerates/rates/A/{wybrana_waluta[0]}/last/30/?format=json'

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data['rates']
    except urllib.error.HTTPError as e:
        print(f'error {e.code}')
        return None

def analiza_gry_gieldowej(lista_walut):
    for kod_waluty in lista_walut:
        kursy = pobierz_kursy_waluty(kod_waluty)

        if kursy:
            cena_zakupu = kursy[0]['mid']
            cena_dzis = kursy[-1]['mid']
            zysk_strata = cena_dzis - cena_zakupu

            print(f"Analiza gry giełdowej dla {kod_waluty}:")
            print(f"Cena zakupu miesiąc temu: {cena_zakupu}")
            print(f"Aktualna cena: {cena_dzis}")

            if zysk_strata > 0:
                print(f"Zysk: {zysk_strata}")
            elif zysk_strata < 0:
                print(f"Strata: {abs(zysk_strata)}")
            else:
                print("Brak zmiany wartości.")
        else:
            print(f"Brak danych dla {kod_waluty} do analizy.")

wybrana_waluta = ["USD"]

analiza_gry_gieldowej(wybrana_waluta)
