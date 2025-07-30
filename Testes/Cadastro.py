import json

dados = []

qtd = int(input("Me diga quantas pessoas deseja cadastrar: "))

for i in range(qtd):
    pessoa = {}
    pessoa["nome"] = input("Me diga o nome da pessoa: ")
    pessoa["idade"] = input("Me diga a idade da pessoa: ")
    pessoa["cpf"] = input("Me diga o cpf da pessoa: ")
    print()
    dados.append(pessoa)

with open("Cadastro.json", "w+", encoding="utf-8") as arq:
    json.dump(dados, arq, indent=4, ensure_ascii=False)

    arq.seek(0)
    dados_lidos = json.load(arq)

print("\n=== PESSOAS CADASTRADAS ===")
for i, pessoa in enumerate(dados_lidos, start=1):
    print(f"\nPessoa {i}:")
    print(f"Nome : {pessoa['nome']}")
    print(f"Idade: {pessoa['idade']}")
    print(f"CPF  : {pessoa['cpf']}")