import random

ile_rzutow = 10000

# for _ in range(100):
#    k6 = random.randint(1, 6)
#    print(k6)

rzuty = [random.randint(1, 6) for _ in range(ile_rzutow)]

print(rzuty)

print("spodziewana wartość: ", ile_rzutow / 6)

print(rzuty.count(1))
print(rzuty.count(2))
print(rzuty.count(3))
print(rzuty.count(4))
print(rzuty.count(5))
print(rzuty.count(6))