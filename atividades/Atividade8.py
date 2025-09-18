lista = [int(input("Me diga um número: ")) for _ in range(5)]

NovaLista = [x for x in lista if x != max(lista) and x != min(lista)]

print(f"Média de {NovaLista} é: {sum(NovaLista) / len(NovaLista)}")