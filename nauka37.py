import random

kolory = ["Zielony", "niebieski", "czerwony", "biały", "Żółty", "czarny", "brązowy", "różowy", "fioletowy"]
kolor = random.choice(kolory)
print(kolor)

kilka_kolorow = random.sample(kolory, 7)
print(kilka_kolorow)

rozne_kolorow = random.choices(kolory, k=6)
print(rozne_kolorow)