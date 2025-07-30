n = int(input("Me diga um número: "))
fatorial = 1

for i in range(n, 0, -1):
    fatorial *= i

print(f"O fatorial de {n} é {fatorial}") 