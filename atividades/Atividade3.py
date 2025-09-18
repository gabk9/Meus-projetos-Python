lista = []

for i in range(5):
    palavra = input("Me diga uma palavra: ")
    lista.append(palavra)

ComA = [x for x in lista if x[0] == "a" or x[0] == "A"]

print("Palavras que começam com \"a\": ", ComA)