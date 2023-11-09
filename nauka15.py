liczba_t = input("Podaj liczbe: ")

if liczba_t.isdecimal():
    liczba = int(liczba_t)
    print(f"Liczba o jeden wieksza wynosi {liczba + 1}")
else:
    print("To nie liczba")