#cenzurowany_email = (email[0] + '_____________') + email[15:17] + '________'

email = input("Podaj adres e-mail: ")

pierwsza_litera = email[0]
nazwa, domena = email.split("@")
#pierwsza_litera_domeny = pozycja_at + 1

ocenzurowana_nazwa = nazwa[0] + '_' * (len(nazwa) - 2) + nazwa[-1]
ocenzurowana_domena = domena[0] + '_' * (len(domena) - 2) + domena[-1]

ocenzurowany_email = ocenzurowana_nazwa + '@' + ocenzurowana_domena

print(f"Twój ocenzurowany email: {ocenzurowany_email}")