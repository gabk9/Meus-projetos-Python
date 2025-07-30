mat = []

for i in range(3):
    linha = []
    for j in range(4):
        valor = int(input(f"Me diga o número da posição[{i}][{j}]: "))
        linha.append(valor)
    mat.append(linha)

print("\nMatriz digitada:")
for linha in mat:
    for valor in linha:
        print(f"{valor:2d}", end=" ")
    print()


maior = mat[0][0]
menor = mat[0][0]
pos_maior = (0, 0)
pos_menor = (0, 0)

for i in range(3):
    for j in range(4):
        if mat[i][j] > maior: 
            maior = mat[i][j]
            pos_maior = (i, j)
        if mat[i][j] < menor:
            menor = mat[i][j]
            pos_menor = (i, j)

print(f"\nO maior valor da matriz é {maior} e está na posição {pos_maior}")
print(f"O menor valor da matriz é {menor} e está na posição {pos_menor}")
