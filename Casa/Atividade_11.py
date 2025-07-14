palavra = str(input("Me diga uma palavra: ")).lower()

if palavra == palavra[::-1]:
    print("Palíndromo")
else:
    print("Não é um palíndromo")