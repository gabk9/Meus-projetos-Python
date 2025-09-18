lista = []

while True:
    nome = input("Me diga um nome: ")
    if nome.lower() != "sair":
        lista.append(nome)
    else:
        break

print("Nomes: ", lista)