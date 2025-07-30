VOGAL = ['a', 'e', 'i', 'o', 'u']

letra = str(input("Me diga uma letra apenas: ")).lower()

if letra in VOGAL:
    print("É vogal")
else:
    print("Não é vogal")

palavra = str(input("Me diga uma palavra: ")).lower()
count = sum(1 for c in palavra if c in VOGAL)
print(f"A palavra: {palavra}, tem {count} vogais") 