numeros = []

while (n := int(input("Digite um número (0 para sair): "))) != 0:
    numeros.append(n)

if numeros:
    print(f"\nA média é: {sum(numeros) / len(numeros):.2f}")
else:
    print("\nImpossível calcular a média (nenhum número foi inserido).")
 