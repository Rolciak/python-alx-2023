# operacje na listach

chlopcy = ['Marek', 'piotrek', 'mateusz']
dziewczyny = ['marta', 'lucja', 'karolina']

wszyscy = chlopcy + dziewczyny

print(wszyscy)

# dodawanie elementow na listy

chlopcy.append("Tadeusz")
print(chlopcy)

# podmiana elementow

chlopcy[2] = 'kazimierz'
print(chlopcy)

# usuniecie elementow

del chlopcy[1]
print(chlopcy)

# dodawanie wielu elementow

panowie = ['Marcin', 'łukasz']
chlopcy.extend(panowie)

print(chlopcy)