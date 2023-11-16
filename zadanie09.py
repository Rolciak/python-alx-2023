email = input("Podaj adres e-mail: ")

cenzurowany_email = (email[0] + '_____________') + email[15:17] + '________'

print(f"Twój ocenzurowany email: {cenzurowany_email}")