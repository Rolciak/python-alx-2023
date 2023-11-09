slowo = input("Podaj słowo zawierające literę a lub dłuższe niż 5 liter ")

if 'a' in slowo or len(slowo) > 5:
    print("Zawiera A lub ma wystarczającą długość")
else:
    print("Źle! (Brak litery A i za krótkie)")
