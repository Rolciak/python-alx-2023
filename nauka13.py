a = 0b1_010_1010
b = 0b_1111_0000

print(f'[{a:10b}] {a}')
print(f'[{b:10b}] {b}')

c = a & b # and bitowe
d = a | b # or bitowe
e = a ^ b # xor bitowe
f =  b >> 1 # przesuniecie bitowe w lewo
g = b << 1 # przesuniecie bitowe w prawo

print(f'[{c:10b}] {c}')
print(f'[{d:10b}] {d}')
print(f'[{e:10b}] {e}')
print(f'[{f:10b}] {f}')

liczba = 3564354

print(liczba.bit_length) # blad
print(liczba.bit_length())
print(liczba.bit_count())