z = 0

for x in range(1, 12345679):
    y = str(x).count("8")
    print(f"{x} {y}")
    z += y
print(f"Suma 8 w liczbie: {z}")