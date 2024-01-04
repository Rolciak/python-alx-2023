...
...
...
a = 10
b = 90
# chciałybm zamienić je miejscami
# chcę osiągnąć sytuację, że a == 90 a b == 10

# tak zrobilibyśmy to w starych językach programowania, np. C
# temp = a
# a = b
# b = temp

a, b = b, a

print(f'{a = }, {b = }')

oceny = [5, 4, 3, 5, 89, 234, 123]
#matematyka = oceny[0]
#polski = oceny[1]
#wf = oceny[2]

# matematyka, polski, wf, *reszta = oceny
matematyka, polski, wf, *_ = oceny

print(f'{matematyka = } {polski = } {wf = }')