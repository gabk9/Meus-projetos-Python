lista = [2, 5, 4, 3, 1]
aux = 0

for i in range(len(lista) - 1):
    for j in range(len(lista) - i - 1):
        if lista[j] > lista [j + 1]:
            aux = lista[j]
            lista[j] = lista[j + 1]
            lista[j + 1] = aux

print(lista)