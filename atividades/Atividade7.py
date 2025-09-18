palavra = input("Me diga uma palavra: ")
palavraInv = palavra[::-1]

print(f"\"{palavra}\" invertida fica \"{palavraInv}\"\nE ela ", end="")
print("é um palíndromo" if palavra == palavraInv else "não é um palíndromo")