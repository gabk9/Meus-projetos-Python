LISTA = [5, 2, 9, 1]
for i in range(len(LISTA)):
    for j in range(i+1, len(LISTA)):
        if LISTA[i] > LISTA[j]:
            LISTA[i], LISTA[j] = LISTA[j], LISTA[i]
print(LISTA) 