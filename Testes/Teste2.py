nome = str(input("Me diga seu nome: "))
sobrenome = str(input("Me diga seu sobrenome: "))

nomeCompleto = nome + " " + sobrenome

print("Seu nome completo é: ", nomeCompleto)

contador = len(nomeCompleto) - nomeCompleto.count(" ")

print(f"Essa string tem {contador} letras")

texto = ""

while 1:
    palavras = input("Me diga uma palavra (digite exit para sair do laço): ")
    if palavras.lower() == "exit":
        break
    texto += palavras + " "

print("O resultado da concatenação ficou:", texto.strip())
    
