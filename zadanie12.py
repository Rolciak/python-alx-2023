# trójkąt
print("Trojkat:")

for star in range(13):
    print(star * '*')

# trójkąt symetryczny
print("Trojkat symetryczny")

for trojkat_sym in range(5):
    print((7 - trojkat_sym) * '.' + (2 * trojkat_sym + 1) * '*')

# choinka
print("Choinka:")

for choinka in range(5):
    print((7 - choinka) * ' ' + (2 * choinka + 1) * '*')

for choinka in range(1, 5):
    print((7 - choinka) * ' ' + (2 * choinka + 1) * '*')