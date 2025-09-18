produtos = []

for j in range(4):
    nome = input("Digite o nome do produto: ")
    custo = float(input("Me diga o preço do produto: "))
    estoque = int(input("Me diga o estoque do produto: "))
    print()

    novo = {"ID": int(bin(len(produtos) + 1)[2:]), "Nome": nome, "Preço": custo, "Estoque": estoque}
    produtos.append(novo)

print(f"{"Produtos Cadastrados":=^32}")
for i in produtos:
    print(f"{i["ID"]:0>7} - {i['Nome']} ", end="")
    print(f"{i['Preço']:.2f}R$ - Estoque: {i['Estoque']}")
    print()