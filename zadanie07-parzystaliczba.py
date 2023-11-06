liczba = int(input("podaj liczbe: "))

if liczba == 0:
    print(f"{liczba} jest zerem")
elif liczba % 2 == 0 and liczba > 17:
    print(f"{liczba} jest liczbą parzystą i wieksza od 17")
elif liczba % 2 == 0 and liczba <= 17:
    print(f"{liczba} jest liczbą parzystą i mniejsza lub rowna 17")
elif liczba % 2 == 1 and liczba > 17:
    print(f"{liczba} jest liczbą nieparzystą i wiekszą od 17")
elif liczba % 2 == 1 and liczba <= 17:
    print(f"{liczba} jest liczbą nieparzystą i jest mniejsza lub rowną 17")