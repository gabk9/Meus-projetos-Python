lista = []

for i in range(5):
    n = int(input("Me diga um número: "))
    lista.append(n)

MaiorQ50 = [x for x in lista if x > 50]

print("Maiores que 50: ", MaiorQ50)